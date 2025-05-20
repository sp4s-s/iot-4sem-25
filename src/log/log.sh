if [[ $- == *i* ]]; then
  read -t 10 -p "" input
  if [[ -z "$input" ]]; then
    LOG_FILE="/home/pi/iot/src/log/execution_log.csv"
    mkdir -p "$(dirname "$LOG_FILE")"
    if [ ! -f "$LOG_FILE" ]; then
      echo "timestamp,event,script,output" > "$LOG_FILE"
    fi

    run_with_timeout() {
      local duration=$1
      local cmd=$2
      local label=$3
      local temp_output
      temp_output=$(mktemp)
      eval "$cmd" >"$temp_output" 2>&1 &
      local pid=$!
      sleep "$duration"
      if ps -p $pid > /dev/null; then
        kill $pid 2>/dev/null
        wait $pid 2>/dev/null
      fi
      local timestamp
      timestamp=$(date '+%Y-%m-%d %H:%M:%S')
      while IFS= read -r line; do
        echo "\"$timestamp\",\"$label\",\"$cmd\",\"$line\"" >> "$LOG_FILE"
      done < "$temp_output"
      rm "$temp_output"
    }

    run_with_timeout 10 "python3 /home/pi/iot/src/f1.py" "run_10s"
    run_with_timeout 5 "python3 /home/pi/iot/src/dht1.py" "run_5s"
    run_with_timeout 60 "/home/pi/iot/src/sent.sh" "run_bash"
  fi
fi
