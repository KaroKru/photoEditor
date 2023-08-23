from readImage import ReadImage

class ChangeImageColour(ReadImage):
    def __init__(self, fileName):
        super().__init__(fileName)

    def grayscale(self):
        grayImage = self.image.copy().convert('L')

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        grayImage.save(f'{newImageName}.jpg')
        grayImage.show()
        grayImage.close()

    def bluscale(self):
        blueImage = self.image.copy()
        blueImage = blueImage.convert('RGB')
        pixels = blueImage.load()
        for i in range(blueImage.size[0]):
            for j in range(blueImage.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (0, 0, b)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        blueImage.save(f'{newImageName}.jpg')
        blueImage.show()
        blueImage.close()

    def redscale(self):
        redImage = self.image.copy()
        redImage =redImage.convert('RGB')
        pixels = redImage.load()
        for i in range(redImage.size[0]):
            for j in range(redImage.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r, 0, 0)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        redImage.save(f'{newImageName}.jpg')
        redImage.show()
        redImage.close()

    def greenscale(self):
        greenImage = self.image.copy()
        greenImage =greenImage.convert('RGB')
        pixels = greenImage.load()
        for i in range(greenImage.size[0]):
            for j in range(greenImage.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (0, g, 0)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        greenImage.save(f'{newImageName}.jpg')
        greenImage.show()
        greenImage.close()

    def userScale(self):
        try:
            red = int(input("Provide a value: "))
            green = int(input("Provide a value: "))
            blue = int(input("Provide a value: "))

            if red >= 0 and green >= 0 and blue >= 0:
                print("Positive values have been selected")
            else:
                print("Negative values have been selected")
        except ValueError:
            print("Invalid RGB values have been selected")
        except TypeError:
            print("The wrong type has been selected")

        scaleImage = self.image.copy()
        scaleImage = scaleImage.convert('RGB')
        pixels = scaleImage.load()

        try:
            for i in range(scaleImage.size[0]):
                for j in range(scaleImage.size[1]):
                    r, g, b = pixels[i, j]
                    if r > 100 and g > 100 and b > 100:
                        pixels[i, j] = (red, green, blue)
        except TypeError:
            print("The wrong type has been selected")

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        scaleImage.save(f'{newImageName}.jpg')
        scaleImage.show()
        scaleImage.close()

    def negative(self):
        oldImage = self.image.copy()
        newImage = oldImage.convert('RGB')
        pixels = newImage.load()
        for i in range(newImage.size[0]):
            for j in range(newImage.size[1]):
                r, g, b = pixels[i, j]
                rNew = 255 - r
                gNew = 255 -g
                bNew = 255 - b
                pixels[i, j] = (rNew, gNew, bNew)

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        newImage.save(f'{newImageName}.jpg')
        newImage.show()
        newImage.close()

    def sepia(self):
        sepiaImage = self.image.copy()
        width, height = sepiaImage.size
        for x in range(width):
            for y in range(height):
                red, green, blue = sepiaImage.getpixel((x, y))
                tr = int(0.393 * red + 0.769 * green + 0.189 * blue)
                tg = int(0.349 * red + 0.686 * green + 0.168 * blue)
                tb = int(0.272 * red + 0.534 * green + 0.131 * blue)
                sepiaImage.putpixel((x, y), (tr, tg, tb))

        try:
            newImageName = input("Enter the desired filename for the file; it will have the default jpg extension ")
        except ValueError:
            print("The file name is invalid")

        sepiaImage.save(f'{newImageName}.jpg')
        sepiaImage.show()
        sepiaImage.close()