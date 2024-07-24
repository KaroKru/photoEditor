from PIL import Image
import os
import time


class ImageHandler:

    def __init__(self, file_name="None"):
        self.file_name = file_name
        self.image = Image.open(file_name)

    def originalImageSize(self):
        width, height = self.image.size
        print("Initial image size (width x height): {} x {}".format(
            width, height))

    def originalImageColour(self):
        colour_type = self.image.mode
        print("Image color mode:", colour_type)

    def originalBytesImage(self):
        bytes_size = len(self.image.tobytes())
        print("Image size in bytes:", bytes_size)

    def openImage(self):
        self.originalImageSize()
        self.originalBytesImage()
        self.originalImageColour()
        time.sleep(0.1)
        self.image.show()

    def saveFile(self, image, suffix):
        fileName, extension = os.path.splitext(self.file_name)
        newImageName = f"{fileName}_{suffix}"
        image.save(f"{newImageName}.jpg")
        image.show()
        image.close()
        print("Image was saved")

    def checkImage(self, file):
        self.file_name = file

        if not os.path.exists(self.file_name):
            raise FileNotFoundError(
                f"The image file was not found: {self.file_name}")

        self.open()

        if self.image is None:
            raise OSError(
                f"There was a problem opening the image: {self.file_name}")

        self.openImage()
