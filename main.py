import os
from PIL import Image



folder_path = 'C:/Users/rober/Desktop/VScode/html and css course/html-css-course-master/html-css-course-master/starter/My-templates/paintings'
file_format = '.jpg'
main_folder = 'paintings'
low_res_folder = 'low-res'


files_path = folder_path
files = os.listdir(files_path)
images = []
for (index, file) in enumerate(files):
    try:
        img = Image.open(folder_path + '/' + file)
    except PermissionError:
        continue
    images.append({'title': file.replace('-', ' ').replace(file_format, ''),
                            'fullRes': f'{main_folder}/{file}',
                            'lowRes': f'{main_folder}/{low_res_folder}/{file}',
                            'height': img.height,
                            'width': img.width,
                            'id': index
                   })

print(images)
