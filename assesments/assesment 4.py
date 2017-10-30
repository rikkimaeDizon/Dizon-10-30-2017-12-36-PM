from PIL import Image

def sepia(oldPixel):
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()

    newred = int(red * 0.393 + green * 0.769 + blue * 0.189)
    green = int(red * 0.349 + green * 0.686 + blue * 0.168)
    newblue= int(red * 0.272 + green * 0.534 + blue * 0.131)
    newPixel = Pixel(newred, newgreen, newblue)

    return newPixel

def generalScale(oldimage, widthscale, heightscale):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage (oldw * widthscale, oldh * heightscale)
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col // witdhscale
            originalRow = row // heightscale
            oldPixel = oldimage.getPixel(originalCol, originalRow)
            newim.setPixel(col, row, oldPixel)
    return newim
        
##def originalScale(oldimage):
##    for row in range(oldimage.getHeight()):
##        for col in range(oldimage.getWidth()):
##            oldPixel = oldimage.getPixel(col, row)
##            sepiaImage = sepia(oldPixel)
##            oldimage.setPixel(col, row, sepiaImage)
##    return oldimage

def displayImage(Image):
        empWin = ImageWin("Image Processing", Image.getWidth(), Image.getHeight())
        Image.draw(empWin)

img = Image.open('skills.jpg')
##sepia = originalScale(img)
##new = generalScale(sepia, 1, 2)
##displayImage(new)
