from PIL import Image

class ReadImage:
    def __init__(self, file_name):
        self.file_name = file_name

        try:
            self.image = Image.open(file_name)
        except FileNotFoundError:
            print("The image file was not found:", file_name)
        except OSError:
            print("There was a problem opening the image:", file_name)
        except ImportError:
            print("Missing Pillow module")

    def openImage(self):
        self.image.show()

    def originalImageSize(self):
        width, height = self.image.size
        print("Initial image size (width x height): {} x {}".format(width, height))

    def originalImageColour(self):
        colour_type = self.image.mode
        print("Image color mode:", colour_type)

    def originalBytesImage(self):
        bytes_size = len(self.image.tobytes())
        print("Image size in bytes:", bytes_size)
