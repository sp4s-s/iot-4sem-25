#!/bin/bash

# Local file paths (absolute, no ~ inside quotes)
LOCAL_FILE1="/home/pi/iot/src/users.csv"
LOCAL_FILE2="/home/pi/iot/src/attendance.csv"
LOCAL_FILE3="/home/pi/iot/src/logged.csv"

# Remote filenames (relative to Jottacloud root)
REMOTE_FILE1="users.csv"
REMOTE_FILE2="attendance.csv"
REMOTE_FILE3="logged.csv"

# Remote alias name from rclone config
REMOTE_NAME="jcloud"

# Function to delete and upload a file
upload_file() {
    local local_file="$1"
    local remote_file="$2"

    echo "Processing $remote_file ..."

    if rclone ls "${REMOTE_NAME}:" | grep -q "${remote_file}"; then
        echo "File $remote_file exists on Jottacloud. Deleting..."
        rclone deletefile "${REMOTE_NAME}:${remote_file}"
    fi

    echo "Uploading $local_file to Jottacloud as $remote_file ..."
    rclone copyto "$local_file" "${REMOTE_NAME}:${remote_file}"
    echo "$remote_file uploaded successfully."
    echo "---------------------------------------------"
}

# Upload all three files
upload_file "$LOCAL_FILE1" "$REMOTE_FILE1"
upload_file "$LOCAL_FILE2" "$REMOTE_FILE2"
upload_file "$LOCAL_FILE3" "$REMOTE_FILE3"
