"""
File name:asciiShop
Keona Rollerson
"""
import urllib3, uuid
import os
import time
from PIL import Image
import sys

url = 'http://thecatapi.com/api/images/get'

def Cat(directory = None, filename = None, format = 'png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile )

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image        
        self.img = None         # Pillow var to hold image


    """
    @Description: 
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns: 
    """
    def getImage(self):
        self.name = self.getTimeStamp()
        cat.getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)
        
        self.width, self.heigth = self.img.size
        
    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass

    """

    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds 


""" 
The ascii character set we use to replace pixels. 
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0
            
        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None
        
        
    """
    Your comments here
    """
    def convertToAscii(self):
    
        if self.newWidth == "not_set":
            self.newWidth = self.width
            
        self.newHeight = int((self.heigth * self.newWidth) / self.width)
            
        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height
            
        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        

        for pixel_value in all_pixels:
            index = pixel_value / 25 # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])
    """
    @Description:image sould be flipped either horizantally or vertically
    @Returns:flipped ascii image
    """
    def flip(self, direction):
        if direction == "horizontal":
            flipped_ascii = []
            temp = list(self.imageAsAscii, self.newWidth)
            for c in temp:
                for item in c[-1]:
                    flipped_ascii.append(item)
            return flipped_ascii
        else
            flipped_ascii = self.imageAsAscii[-1]
            return flipped_ascii
   """
   @Description:Light pixels become dark pixel and vice versa
   @Returns:inverted image
   """
    def invert(self):
        self.imageAsAscii = []
        imag = self.asciiChars
        imag.reverse()
        self.inverted = imag
        all_pixels = list(self.newImage.getdata())
        
        for pixel_value in all_pixels:
            index = pixel_value // 25
            self.imageAsAscii.append(self.asciiChars[index])
        return self.imageAsAscii    
    """
    Print the image to the screen
    """
    def printImage(self):
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii)
        for c in range(0, len(self.imageAsAscii), self.newWidth):
            print (self.imageAsAscii[c:c+self.newWidth])

"""
Convert to 2D list of lists to help with manipulating the ascii image.
Example:
    
    L = [0,1,2,3,4,5,6,7,8]
    
    L = to_matrix(L,3)
    
    L becomes:
    
    [[0,1,2],
    [3,4,5],
    [6,7,8]]
"""
def listToMatrix(l, n):
    return [l[i:i+n] for i in xrange(0, len(l), n)]

if __name__=='__main__':
    awesomeCat = AsciiImage(150)
    awesomeCat.getImage()
    
    awesomeCat.convertToAscii()
    awesomeCat.printImage()
    awesomeCat.invert()
    awesomeCat.printImage()
    awesomeCat.flip("horizontal")
    awesomeCat.printImage()
