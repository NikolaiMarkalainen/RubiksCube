
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

input_directory = "./validation/Y"
output_directory = "./previewY"

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

file_list = os.listdir(input_directory)

for filename in file_list:
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        img = load_img(os.path.join(input_directory, filename))

        x = img_to_array(img)
        x = x.reshape((1, ) + x.shape)

        i = 0
        for batch in datagen.flow(x,
                                  batch_size=1,
                                  save_to_dir=output_directory,
                                  save_prefix=os.path.splitext(filename)[0],
                                  save_format='jpeg'):
            i += 1
            if i > 24:
                break