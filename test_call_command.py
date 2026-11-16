
import subprocess
import sys

# Run Charlene's Python program
subprocess.run(
    [sys.executable, "sagittal_brain.py"],
    check=True
)

print("Charlene's program has finished running.")
