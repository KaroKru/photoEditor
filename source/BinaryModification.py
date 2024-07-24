from PIL import Image
from scipy import ndimage
import numpy as np


class MorphoTransformation:

    def __init__(self, reader):
        self.reader = reader

    def binaryzation(self):
        copyImage = self.reader.image.copy()
        greyImage = copyImage.convert("L")
        threshold = 130
        pixels = greyImage.load()
        for i in range(greyImage.size[0]):
            for j in range(greyImage.size[1]):
                if pixels[i, j] > threshold:
                    pixels[i, j] = 255
                else:
                    pixels[i, j] = 0
        greyImage = greyImage.convert("1")

        self.reader.saveFile(greyImage, "binaryzation")

    def erosion(self):
        erosionImage = self.reader.image.copy()
        erosionArray = np.array(erosionImage.convert("1"))
        erosionFiltr = np.ones((2, 1))
        erosion = ndimage.binary_erosion(
            erosionArray, structure=erosionFiltr).astype(erosionArray.dtype)
        newImage = Image.fromarray(erosion)

        self.reader.saveFile(newImage, "erosion")

    def open(self):
        openImage = self.reader.image.copy()
        openArray = np.array(openImage.convert("1"))
        openFiltr = np.ones((1, 1))
        open = ndimage.binary_opening(
            openArray, structure=openFiltr).astype(openArray.dtype)
        newImage = Image.fromarray(open)

        self.reader.saveFile(newImage, "open")

    def close(self):
        closedImage = self.reader.image.copy()
        closedArray = np.array(closedImage.convert("1"))
        closedFiltr = np.ones((2, 5))
        closed = ndimage.binary_closing(
            closedArray, structure=closedFiltr).astype(closedArray.dtype)
        newImage = Image.fromarray(closed)

        self.reader.saveFile(newImage, "close")

    def transformationOptions(self):
        operations = [
            "binaryzation",
            "erosion",
            "open",
            "close"
        ]
        print("Possible morphological transformation:")

        for id, operation in enumerate(operations, start=1):
            print(f"{id} -> {operation}")

        choose = int(input("What do you want to do? Enter an id value:"))

        match choose:
            case 1:
                self.binaryzation()
            case 2:
                self.erosion()
            case 3:
                self.open()
            case 4:
                self.close()
            case _:
                print("Selected value out of the scope")
