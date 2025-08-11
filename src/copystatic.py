import os
import shutil


WORKING_PATH = "/home/claye/workspace/github.com/jcfullmer/StaticSiteGenerator"

def cp_source_to_dest(source_dir, dest_dir):
    abssource_dir = os.path.join(WORKING_PATH, source_dir)
    absdest_dir = os.path.join(WORKING_PATH, dest_dir)
    if not os.path.exists(absdest_dir):
        raise ValueError("The Destination Directory Does Not Exist.")
    if not os.path.exists(abssource_dir):
        raise ValueError("The source path does not exist")
    print("getting contents")
    if len(os.listdir(dest_dir)) > 0:
        print("Deleting Files in the Destination Directory")
        shutil.rmtree(absdest_dir)
        os.mkdir(absdest_dir)
    contents = os.listdir(abssource_dir)
    for item in contents:
        final_source = os.path.join(abssource_dir, item)
        item_path = f"{source_dir}/{item}"
        if os.path.isfile(final_source):
            print(f"Copying {item} to {absdest_dir}")
            shutil.copy(final_source, absdest_dir)
        if os.path.isdir(final_source):
            print(f"Creating {dest_dir}/{item} and recurisng function.")
            os.mkdir(f"{dest_dir}/{item}")
            cp_source_to_dest(item_path, f"{dest_dir}/{item}")
