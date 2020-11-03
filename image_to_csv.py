import csv
from PIL import Image

image = Image.open('christof.jpg').convert('L')  #reads image in grayscale

with open('christof.csv', mode='w') as image_file:

    image_writer = csv.writer(image_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    image_writer.writerow(['x', 'y', 'scale'])

    for x in range(image.width):
        for y in range(image.height):
            image_writer.writerow([x, y, image.getpixel((x, y))])

