#!/bin/bash

# Define local file paths
LOCAL_DIR="/home/pi/iot/src"
LOCAL_FILE1="${LOCAL_DIR}/users.csv"
LOCAL_FILE2="${LOCAL_DIR}/attendance.csv"

# Remote Jottacloud destination (root)
REMOTE_NAME="jcloud"

# Remote file names (can match local names)
REMOTE_FILE1="users.csv"
REMOTE_FILE2="attendance.csv"

# Upload function
upload_file() {
    local local_file="$1"
    local remote_file="$2"

    echo ">>> Handling: $remote_file"

    if rclone ls "${REMOTE_NAME}:" | grep -q "${remote_file}"; then
        echo "File exists remotely. Deleting: $remote_file"
        rclone deletefile "${REMOTE_NAME}:${remote_file}"
    fi

    echo "Uploading $local_file to $REMOTE_NAME:$remote_file ..."
    rclone copyto "$local_file" "${REMOTE_NAME}:${remote_file}"

    echo "✅ Done with $remote_file"
    echo
}

# Run uploads
upload_file "$LOCAL_FILE1" "$REMOTE_FILE1"
upload_file "$LOCAL_FILE2" "$REMOTE_FILE2"
