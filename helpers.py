import os
import fnmatch

def get_face_images_list(folder, filter):       
    # Get files in the folder
    files = fnmatch.filter(os.listdir(folder), filter)

    # Load all files
    face_images_list = []  
    labels = []

    for file in files:
        # Get full file path
        file_path = os.path.join(folder, file)                            

        # Get expected label
        label = file.split('.')[0]

        # Append file paths and labels
        face_images_list.append(file_path)
        labels.append(label)
        
    return (face_images_list, labels)