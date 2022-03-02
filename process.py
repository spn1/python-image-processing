import cv2
from os import listdir
from os.path import isfile, join

# Read Filenames
image_directory = './sample_images'
image_filenames = [f for f in listdir(
    './sample_images') if isfile(f'{image_directory}/{f}')]


for filename in image_filenames:
    image = cv2.imread(f'{image_directory}/{filename}', 0)
    resized = cv2.resize(image, (100, 100))
    cv2.imwrite(f'{image_directory}/resized_{filename}', resized)

# Showing Images
# cv2.imshow("Galaxy", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
