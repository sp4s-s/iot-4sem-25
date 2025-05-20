
from pyfingerprint.pyfingerprint import PyFingerprint
import csv
import time
import datetime
import os
import hashlib

USERS_FILE = 'users.csv'
ATTENDANCE_FILE = 'attendance.csv'
MAX_SLOTS = 1000


def format_name(name_raw):
    return name_raw.strip().title()


def ensure_csv_files():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['slot_id', 'name', 'date_added', 'time_added', 'hash', 'last_score'])
        print('🆕 Created users.csv')

    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'name', 'time', 'slot_id', 'hash', 'match_score'])
        print('🆕 Created attendance.csv')


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        reader = csv.DictReader(f)
        return {
            int(row['slot_id']): {
                'name': row.get('name', '').strip(),
                'hash': row.get('hash', '').strip()
            }
            for row in reader if row.get('slot_id')
        }


def has_attended_today(slot_id):
    today = datetime.date.today().isoformat()
    if not os.path.exists(ATTENDANCE_FILE):
        return False
    with open(ATTENDANCE_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['date'] == today and int(row['slot_id']) == slot_id:
                return True
    return False


def log_attendance(name, slot_id, fingerprint_hash, score):
    now = datetime.datetime.now()
    date_str = now.date().isoformat()
    time_str = now.strftime('%H:%M:%S')
    with open(ATTENDANCE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date_str, name, time_str, slot_id, fingerprint_hash, score])
    print(f'✅ Attendance logged: {name} at {time_str}')


def find_free_slot(used_slots):
    for i in range(MAX_SLOTS):
        if i not in used_slots:
            return i
    return -1


def update_user_entry(slot_id, name, score):
    updated = False
    rows = []
    with open(USERS_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['slot_id']) == slot_id:
                if not row['name']:
                    row['name'] = name
                    updated = True
                row['last_score'] = str(score)
            rows.append(row)

    if updated:
        with open(USERS_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['slot_id', 'name', 'date_added', 'time_added', 'hash', 'last_score'])
            writer.writeheader()
            writer.writerows(rows)


def register_user(sensor, used_slots, fingerprint_hash, score):
    print('🆕 Place finger to register...')
    while True:
        if sensor.readImage():
            try:
                sensor.convertImage(0x01)
                sensor.createTemplate()
                free_slot = find_free_slot(used_slots)
                if free_slot == -1:
                    print('❌ No free fingerprint slots available.')
                    return None, None

                sensor.storeTemplate(free_slot)

                name_raw = input('📝 Enter name for this fingerprint: ')
                name = format_name(name_raw)
                now = datetime.datetime.now()
                date_str = now.date().isoformat()
                time_str = now.strftime('%H:%M:%S')

                with open(USERS_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([free_slot, name, date_str, time_str, fingerprint_hash, score])

                print(f'✅ Registered {name} at slot {free_slot}')
                return free_slot, name

            except Exception as e:
                print(f'⚠️ Registration error: {e}')
                print('🔁 Try again.')
                time.sleep(1)
        time.sleep(0.1)


def main():
    ensure_csv_files()

    try:
        sensor = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise ValueError('Sensor password incorrect.')
    except Exception as e:
        print(f'❌ Sensor init failed: {e}')
        return

    print('📡 Fingerprint sensor ready.')

    while True:
        users = load_users()
        used_slots = set(users.keys())

        print('👉 Place finger to scan...')
        while not sensor.readImage():
            time.sleep(0.1)

        try:
            sensor.convertImage(0x01)
            characteristics = sensor.downloadCharacteristics(0x01)
            fingerprint_hash = hashlib.sha256(bytearray(characteristics)).hexdigest()

            result = sensor.searchTemplate()
            position_number = result[0]
            accuracy_score = result[1]

            if position_number >= 0:
                user_entry = users.get(position_number, {})
                name = user_entry.get('name', '').strip()

                print(f'👤 Recognized {name or "Unknown"} at slot {position_number} (score: {accuracy_score})')

                if not name:
                    name_raw = input(f'📝 Name not recorded for slot {position_number}. Enter name: ')
                    name = format_name(name_raw)
                    update_user_entry(position_number, name, accuracy_score)
                else:
                    update_user_entry(position_number, name, accuracy_score)

                if has_attended_today(position_number):
                    print('📛 Already attended today. No update.')
                else:
                    log_attendance(name, position_number, fingerprint_hash, accuracy_score)

            else:
                print('🆕 Finger not recognized.')
                slot_id, name = register_user(sensor, used_slots, fingerprint_hash, 0)
                if slot_id is not None:
                    log_attendance(name, slot_id, fingerprint_hash, 0)

        except Exception as e:
            print(f'❌ Scan error: {e}')

        print('✋ Remove finger...')
        while sensor.readImage():
            time.sleep(0.1)


if __name__ == '__main__':
    main()
