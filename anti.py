import os
import hashlib
import json

def calculate_hash(file_path, block_size = 65536):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def save_hash_to_file(hashes, file_path = "hashes.json"):
    with open(file_path, 'w') as f:
        json.dump(hashes, f, indent=2)
        
        
def load_hashes_from_file(file_path = "hashes.json"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return  {}



def check_files_in_directory(directory, original_hashes):
    for root,_,files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            
            if file in original_hashes:
                if file_hash == original_hashes[file]:
                    print(f"File: {file} status: OK")
                else:
                    print(f"File: {file} status: CORRUPTED")
            else:
                print(f"File: {file}, status: NEW")
                
 
if  __name__ == "__main__":
    external_device_path = input('Enter external path: ')
    hashes_file_path  = "hashes.json"
    
    if os.path.exists(external_device_path):
        print(f"Checking files on external device: {external_device_path}")
        
        original_hashes = load_hashes_from_file(hashes_file_path)
        check_files_in_directory(external_device_path, original_hashes)
        
        
        updated_hashes = {file: calculate_hash(os.path.join(external_device_path, file)) for file in os.listdir(external_device_path)}
        original_hashes.update(updated_hashes)
        save_hash_to_file(original_hashes, hashes_file_path)
    else:
        print("External Device not Found")    
        
        
        
                                
                    