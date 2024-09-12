import os
import hashlib
import sys
import time

def calculate_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "FILE_NOT_FOUND"

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hashes[filepath] = calculate_file_hash(filepath)
    return file_hashes

def create_baseline(directory, baseline_path):
    print("Creating new baseline")
    if os.path.isfile(baseline_path):
        print(".baseline already exists! \nDeleting old .baseline...\nCreating new .baseline...")
        os.remove(baseline_path)
    
    with open(baseline_path, 'x'):
        pass
    
    file_hashes = scan_directory(directory)
    with open(baseline_path, "a") as f:
        for filepath, filehash in file_hashes.items():
            if not filepath.endswith('.baseline.txt'):  # Ignore the baseline file itself
                f.write(f"{filepath}|{filehash}\n")
    print("Baseline created.")

def monitor_directory(directory, baseline_path):
    filepath_filehash_dict = {}
    with open(baseline_path, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            filepath, filehash = stripped_line.split('|', 1)
            filepath_filehash_dict[filepath] = filehash

    print("Monitoring...")
    current_files = scan_directory(directory)

    # Check if files have been deleted
    for filepath in filepath_filehash_dict:
        if not os.path.isfile(filepath):
            print("A file has been DELETED  " + filepath)

    # Check for new or modified files
    for filepath, current_hash in current_files.items():
        if filepath not in filepath_filehash_dict:
            if not filepath.endswith('.baseline.txt'):  # Ignore the baseline file itself
                print("A new file has been CREATED  " + filepath)
        elif current_hash != filepath_filehash_dict[filepath]:
            if not filepath.endswith('.baseline.txt'):  # Ignore the baseline file itself
                print("A file has been MODIFIED   " + filepath)

def main():
    while True:
        print("\nMenu:")
        print("1. Set/Change Monitoring Directory")
        print("2. Create New Baseline")
        print("3. Start Monitoring")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            global monitoring_dir, bl_path
            monitoring_dir = input("Enter the path of the directory to monitor: ")
            if not os.path.isdir(monitoring_dir):
                print("Directory doesn't exist!")
            else:
                bl_path = os.path.join(monitoring_dir, '.baseline.txt')
                print(f"Monitoring directory set to: {monitoring_dir}")

        elif choice == '2':
            if not os.path.isdir(monitoring_dir):
                print("No directory set. Please set the directory first.")
            else:
                create_baseline(monitoring_dir, bl_path)

        elif choice == '3':
            if not os.path.isfile(bl_path):
                print("No baseline file found. Please create a baseline first.")
            else:
                monitor_directory(monitoring_dir, bl_path)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    monitoring_dir = os.getcwd()  # Default to current directory
    bl_path = os.path.join(monitoring_dir, '.baseline.txt')
    main()
