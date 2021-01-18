import os

folder = "./data/preprocessed"

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        os.remove(file_path)
    except Exception as e: 
        print(f' Failed to delete {file_path}  Reason: {e}' )
    
