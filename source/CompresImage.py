from PIL import Image


class CompressImage:
    def __init__(self, reader):
        self.reader = reader

    def compress(self):
        ratio = float(input("Selected value from range between 0 and 1: "))

        if ratio < 0 or ratio > 1:
            raise ValueError("An invalid value has been selected")

        quality = int(input("Enter a value within the range of 1 to 95 "))
        if quality < 1 or quality > 95:
            raise ValueError("An invalid value has been selected")

        compressImage = self.reader.image.copy()
        compressImage = compressImage.resize(
            (int(compressImage.size[0] * ratio),
             int(compressImage.size[1] * ratio)),
            Image.LANCZOS
        )
        print("File size after compression", compressImage.size)

        self.reader.saveFile(compressImage, "compress")
