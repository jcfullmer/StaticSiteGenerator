import os
import shutil

def cp_source_to_dest(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    if len(os.listdir(dest_dir)) > 0:
        print("Deleting Files in the Destination Directory")
        shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)
    for item in os.listdir(source_dir):
        from_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(from_path):
            print(f"Copying {item} to {dest_dir}")
            shutil.copy(from_path, dest_path)
        if os.path.isdir(from_path):
            cp_source_to_dest(from_path, dest_path)
