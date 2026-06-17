import subprocess
import datetime

def run_step(name, script):
    print(f"\n--- Running {name} ---")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"ERROR in {name}: {result.stderr}")
    else:
        print(f"{name} completed successfully ✅")

print(f"Pipeline started at {datetime.datetime.now()}")
run_step("Data Collection", "scripts/collect.py")
run_step("Data Cleaning", "scripts/clean.py")
run_step("Data Loading", "scripts/load.py")
run_step("Visualization", "scripts/visualize.py")
print(f"\nPipeline finished at {datetime.datetime.now()} ✅")