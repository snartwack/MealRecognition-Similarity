import subprocess
import os

# Get directory where run_all.py is located
script_dir = os.path.dirname(__file__)

# List of all the model scripts we want to run
scripts = [
    "qwen_code.py",
    "llava_code.py",
    "moondream_code.py",
    "yolo_code.py",
    "gemini_code.py"
]

print("====================================================", flush=True)
print("          RUNNING ALL EVALUATION SCRIPTS            ", flush=True)
print("====================================================", flush=True)

for script in scripts:
    print(f"\n[+] Executing script: {script} ...", flush=True)
    print("=" * 50, flush=True)
    
    # Get absolute path to the script
    script_path = os.path.join(script_dir, script)
    
    # Run the script as a separate process
    subprocess.run(["python", script_path])
    
    print("=" * 50, flush=True)

print("\nAll scripts have been executed successfully!", flush=True)
