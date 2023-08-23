from PIL import Image
from readImage import ReadImage

class CompresImage(ReadImage):
    def __init__(self, fileName):
        super().__init__(fileName)

    def compres(self):
        ratio = 0

        while 1:
            try:
                ratio = float(input("Selected value from range between 0 and 1: "))
                if ratio >= 0 and ratio <= 1:
                    print("Selected value from the range")
                    break
                else:
                    ratio = 0
                    print("The value is not within the range")
            except ValueError:
                print("A different value has been selected")
            except TypeError:
                print("An invalid type has been selected")

        quality = 0
        while 1:
            try:
                quality = int(input("Enter a value within the range of 1 to 95 "))
                if quality >= 1 and quality <= 95:
                    print("Selected value from the range")
                    break
                else:
                    quality = 0
                    print("The value is not within the range")
            except ValueError:
                print("A different value has been selected")
            except TypeError:
                print("An invalid type has been selected")
            except FloatingPointError:
                print("The operation failed")

        compresImage = self.image.copy()
        imageSize = compresImage.size

        compresImage = compresImage.resize((int(compresImage.size[0] * ratio), int(compresImage.size[1] * ratio)), Image.LANCZOS)
        print("File size after compression ", compresImage.size)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid ")

        compresImage.save(f'{newImageName}.jpg', quality=quality, optimize=True)
        compresImage.show()
        compresImage.close()