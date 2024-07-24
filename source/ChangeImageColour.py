from ImageInformation import ImageHandler
from PIL import Image

class ColourTransformation():
    
    def __init__(self, reader):
        self.reader = reader

    def greyscale(self):
        greyImage = self.reader.image.copy().convert('L')

        self.reader.saveFile(greyImage, "grey")

    def bluscale(self):
        blueImage = self.reader.image.copy()
        blueImage = blueImage.convert('RGB')
        pixels = blueImage.load()
        for i in range(blueImage.size[0]):
            for j in range(blueImage.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (0, 0, b)

        self.reader.saveFile(blueImage, "blue")

    def redscale(self):
        redImage = self.reader.image.copy()
        redImage = redImage.convert('RGB')
        pixels = redImage.load()
        for i in range(redImage.size[0]):
            for j in range(redImage.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r, 0, 0)

        self.reader.saveFile(redImage, "red")

    def greenscale(self):
        greenImage = self.reader.image.copy()
        greenImage =greenImage.convert('RGB')
        pixels = greenImage.load()
        for i in range(greenImage.size[0]):
            for j in range(greenImage.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (0, g, 0)

        self.reader.saveFile(greenImage, "green")

    def userScale(self):
        red = int(input("Provide value of red colour: "))
        green = int(input("Provide value of green: "))
        blue = int(input("Provide value of blue: "))

        if red < 0 or green < 0 or blue < 0:
            raise ValueError(f"Invalid RGB values have been selected")

        scaleImage = self.reader.image.copy()
        scaleImage = scaleImage.convert('RGB')
        pixels = scaleImage.load()

        for i in range(scaleImage.size[0]):
            for j in range(scaleImage.size[1]):
                r, g, b = pixels[i, j]
                if r > 100 and g > 100 and b > 100:
                    pixels[i, j] = (red, green, blue)

        self.reader.saveFile(scaleImage, "colour")

    def negative(self):
        oldImage = self.reader.image.copy()
        newImage = oldImage.convert('RGB')
        pixels = newImage.load()
        for i in range(newImage.size[0]):
            for j in range(newImage.size[1]):
                r, g, b = pixels[i, j]
                rNew = 255 - r
                gNew = 255 -g
                bNew = 255 - b
                pixels[i, j] = (rNew, gNew, bNew)

        self.reader.saveFile(newImage, "negative")

    def sepia(self):
        sepiaImage = self.reader.image.copy()
        width, height = sepiaImage.size
        for x in range(width):
            for y in range(height):
                red, green, blue = sepiaImage.getpixel((x, y))
                tr = int(0.393 * red + 0.769 * green + 0.189 * blue)
                tg = int(0.349 * red + 0.686 * green + 0.168 * blue)
                tb = int(0.272 * red + 0.534 * green + 0.131 * blue)
                sepiaImage.putpixel((x, y), (tr, tg, tb))

        self.reader.saveFile(sepiaImage, "sepia")

    def colourOptions(self):
        transformation = [
                "black and white",
                "blue", 
                "red", 
                "green", 
                "sepia", 
                "negative",
                "choose your own colour transformation"
            ]
            
        print(f"Possible colour transformation: ")
            
        for id, transformation in enumerate(transformation, start = 1):
            print(f"{id} -> {transformation}")
            
        choose = int(input("What do you want to do? Enter an id value:"))

        match choose:
            case 1:
                self.greyscale()
            case 2:
                self.bluscale()
            case 3:
                self.redscale()
            case 4:
                self.greenscale()
            case 5:
                self.sepia()
            case 6:
                self.negative()
            case 7: 
                self.userScale()
            case _:
                print(f"Selected value out of the scope")
