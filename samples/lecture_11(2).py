from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.abspath(__file__))
filename_lenna = path + '/' + 'lenna.bmp'
filename_country = path + '/' + 'china_2.png'
data_lenna = image.imread(filename_lenna)
data_country = image.imread(filename_country)

print('Image type is: ', type(data_lenna))
print('Image shape is: ', data_lenna.shape)
print('Image type is: ', type(data_country))
print('Image shape is: ', data_country.shape)

data_lenna[data_country.shape[0], 512-250, :] = 255*data_country

# Write the modified images
image.imsave(path+'/'+'lenna-mod.jpg', data_lenna)

# use pyplot to plot the image
pyplot.imshow(data_lenna)
pyplot.show() #show the file permanently