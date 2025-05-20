#!/bin/bash
chmod +x file3.sh

python_file_to_run="irm.py"
condition="1"
python_file_to_run_if_match="pump.py"

output=$(python "$python_file_to_run")

if [[ "$output" == "$condition" ]]; then
  echo "Output matched '$condition'. Running '$python_file_to_run_if_match'..."
  python "$python_file_to_run_if_match"
else
  echo "Output '$output' did not match '$condition'."
fi

exit 0