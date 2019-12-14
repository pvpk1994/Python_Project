import os
'''
Use Recursion to find if a given file is found in a given directory
Author: Pavan Kumar Paluri
'''

base_dir = "/Users/pavankumarpaluri"


def is_file_found(file_dir: str, filename: str) -> bool:
    global base_dir
    # get the file path using Join() function
    full_path = os.path.join(base_dir, file_dir)
    print(full_path)
    if filename in full_path:
        return True
    # Making sure the file is only a file and not a directory..
    is_file = os.path.isfile(full_path)
    if is_file:
        return False
    # Recursively search each subdirectory to find the filename
    for file in os.listdir(full_path):
        found = is_file_found(os.path.join(full_path, file), filename)
        if found:
            print("FounD")
            return True

    return False


if __name__ == '__main__':
    print(is_file_found("Documents", "input365.txt"))
