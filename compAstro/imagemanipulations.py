import numpy as np
import scipy.ndimage
from matplotlib import pyplot
import scipy.signal


#Reading the image and assigning it into an array for transposure
def transpose_image(filename):
    sunimg = scipy.ndimage.imread(filename)
    print np.shape(sunimg)   
    print sunimg.dtype       
    sunimgtr = np.swapaxes(sunimg,0,1)
    pyplot.imshow(sunimgtr)
    pyplot.savefig('transposed.png')
    pyplot.show()
    
#Creating a combination of different color images of the original    
def color_separation(filename):
    sunimg = scipy.ndimage.imread(filename)
    colorsep, axes = pyplot.subplots(nrows=2, ncols=2)
    
    #Original image at the top left
    axes[0,0].imshow(sunimg)
    axes[0,0].legend()
    axes[0,0].set_title('Original Image')
    axes[0,0].axis('off')
    
    #Define three different arrays for red,green,blue colors
    redarray = sunimg[:,:,0]
    greenarray = sunimg[:,:,1]
    bluearray = sunimg[:,:,2]
    
    #Saving redarray at 0,1 position
    axes[0,1].imshow(redarray, cmap = pyplot.set_cmap('Reds_r')) 
    axes[0,1].legend()
    axes[0,1].set_title('Red Image')
    axes[0,1].axis('off')
    #Saving greenarray at 0,1 position
    axes[1,0].imshow(greenarray, cmap = pyplot.set_cmap('Greens_r'))
    axes[1,0].legend()
    axes[1,0].set_title('Green Image')
    axes[1,0].axis('off')
    #Saving bluearray at 1,1 position
    axes[1,1].imshow(bluearray, cmap = pyplot.set_cmap('Blues_r'))
    axes[1,1].legend()
    axes[1,1].set_title('Blue Image')
    axes[1,1].axis('off')
    
    colorsep.savefig('ColorSeparation.png')
    pyplot.show()
    

#Grayscaling of the image
def grayscale(filename):
    sunimg = scipy.ndimage.imread(filename)
    #Define three different arrays for red,green,blue colors
    redarray = sunimg[:,:,0]
    greenarray = sunimg[:,:,1]
    bluearray = sunimg[:,:,2]
    #Creating the gray scale array using the equation provided
    grayarray = np.add(np.multiply(redarray,0.299),\
                np.multiply(greenarray,0.587),np.multiply(bluearray,0.114))
    pyplot.imshow(grayarray, cmap = pyplot.set_cmap('gray'))
    pyplot.legend()
    pyplot.title('Gray scale')
    pyplot.axis('off')
    pyplot.savefig('grayscale.png')
    pyplot.show()
    

#Sobel filter of the image
def sobel_filter(filename):
    sunimg = scipy.ndimage.imread(filename)
    sob, axes = pyplot.subplots(nrows=2, ncols=2)
    #Original image at top left
    axes[0,0].imshow(sunimg)
    axes[0,0].legend()
    axes[0,0].set_title('Original Image')
    axes[0,0].axis('off')
    
    #X-Gradient (3x3)calculation and display (top right)
    Gradx = [[-1,0,1],
             [-2,0,2],
             [-1,0,1]]
    #Multiplying Gradx with a 3x3 element of the image array
    sobx = scipy.signal.convolve2d(sunimg,Gradx)
    '''
    for x in range(0,1021):     #limit = width-3 of the image
        for y in range(0,1021): #limit = height-3 of the image
            sobx=(Gradx[0][0]*sunimg[x,y])+\
                 (Gradx[0][1]*sunimg[x+1,y])+\
                 (Gradx[0][2]*sunimg[x+2,y])+\
                 (Gradx[1][0]*sunimg[x,y+1])+\
                 (Gradx[1][1]*sunimg[x+1,y+1])+\
                 (Gradx[1][2]*sunimg[x+2,y+1])+\
                 (Gradx[2][0]*sunimg[x,y+2])+\
                 (Gradx[2][1]*sunimg[x+1,y+2])+\
                 (Gradx[2][2]*sunimg[x+2,y+2])
    '''
    axes[0,1].imshow(sobx)
    axes[0,1].legend()
    axes[0,1].set_title('X-Gradient')
    axes[0,1].axis('off')
    
    #Y-Gradient calculation and display (bottom left)
    Grady = [[-1,-2,-1],
             [0,0,0],
             [1,2,1]]
    #Multiplying Grady with a 3x3 element of the image array
    soby = scipy.signal.convolve2d(sunimg,Grady)
    '''
    for x in range(0,1021):     #limit = width-3 of the image
        for y in range(0,1021): #limit = height-3 of the image
            soby=(Grady[0][0]*sunimg[x,y])+\
                 (Grady[0][1]*sunimg[x+1,y])+\
                 (Grady[0][2]*sunimg[x+2,y])+\
                 (Grady[1][0]*sunimg[x,y+1])+\
                 (Grady[1][1]*sunimg[x+1,y+1])+\
                 (Grady[1][2]*sunimg[x+2,y+1])+\
                 (Grady[2][0]*sunimg[x,y+2])+\
                 (Grady[2][1]*sunimg[x+1,y+2])+\
                 (Grady[2][2]*sunimg[x+2,y+2])
    '''
    axes[1,0].imshow(soby)
    axes[1,0].legend()
    axes[1,0].set_title('Y-Gradient')
    axes[1,0].axis('off')
    
    #Sobel Filter display (bottom right)
    sobfilter = scipy.signal.convolve(sobx,soby)
    axes[1,1].imshow(sobfilter)
    axes[1,1].legend()
    axes[1,1].set_title('Sobel Filter')
    axes[1,1].axis('off')
    
    sob.savefig('SobelFilter.png')
    pyplot.show()
    

transpose_image('f_211_193_171_1024.png')
color_separation('f_211_193_171_1024.png')
grayscale('f_211_193_171_1024.png')
sobel_filter('grayscale.png')
