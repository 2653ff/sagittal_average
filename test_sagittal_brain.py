
import numpy as np
import subprocess
import sys

# Create test data
input_data = np.repeat(np.arange(20).reshape(20, 1), 20, axis=1)
expected = np.arange(20, dtype=float)

try:
    # Save input data
    np.savetxt("brain_sample.csv", input_data, fmt="%d", delimiter=",")

    # Run Charlene's program
    subprocess.run([sys.executable, "sagittal_brain.py"], check=True)

    # Read output
    output = np.loadtxt("brain_average.csv", delimiter=",")

    print("Expected:", expected)
    print("Output:", output)

    # Check the result
    np.testing.assert_array_equal(output, expected)

finally:
    # Restore files so Git can switch between commits
    subprocess.run(
        ["git", "restore", "--", "brain_sample.csv", "brain_average.csv"],
        check=True
    )

