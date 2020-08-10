import helpers
from easyfacenet.simple import facenet
import numpy as np
import random

class recognizer(object):
    def __init__(self):  
        # Face images location
        face_images_folder = 'images'
        filter = '*.bmp'

        # Get face images list
        self.face_images_list, self.labels = helpers.get_face_images_list(face_images_folder, filter)

        # Pre-process images
        self.face_images_aligned = facenet.align_face(self.face_images_list)

    def recognize(self, face_image_file_path):
        # Align image
        face_image_aligned = facenet.align_face([face_image_file_path])

        # Append aligned test image to the known faces
        all_images_aligned = np.append(self.face_images_aligned, face_image_aligned, axis=0)

        # Compare
        comparison_matrix = facenet.compare(all_images_aligned)

        # Get last row from the comparisons matrix, excluding test image
        last_row = comparisons_matrix[-1,0:-1];

        # Return label
        return self.labels[np.argmax(last_row)]    

    def get_random_face_image_file_path(self):
        random_index = random.randint(0, len(self.face_images_list)-1)

        return self.face_images_list[random_index]