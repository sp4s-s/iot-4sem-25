from pyfingerprint.pyfingerprint import PyFingerprint

try:
    sensor = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if not sensor.verifyPassword():
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Failed to initialize sensor:')
    print(e)
    exit(1)

print('Waiting for finger...')

try:
    while not sensor.readImage():
        pass

    sensor.convertImage(0x01)

    result = sensor.searchTemplate()
    positionNumber = result[0]

    if positionNumber == -1:
        print('No match found. Storing new template...')
        sensor.createTemplate()
        positionNumber = sensor.storeTemplate()
        print(f'New fingerprint stored at position #{positionNumber}')
    else:
        print(f'Fingerprint already exists at position #{positionNumber}')

    # Convert ID to hex string
    print('Unique hex ID:', hex(positionNumber))
    print('\n All Data: \n', hex(result))

except Exception as e:
    print('Operation failed:')
    print(e)
