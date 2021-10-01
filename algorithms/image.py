from PIL import Image, ImageDraw, ImageFont
import numpy
import re
import base64
from io import BytesIO



# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)
# made function where file is opened with raw binary mode to get binary values, binary values are then converted to hex values without for loop
# https://stackoverflow.com/questions/24889338/python-image-jpeg-to-hex-code
def imgToHex(file):
    string = ''
    with open(file, 'rb') as f:
        binValue = f.read(1)
        while len(binValue) != 0:
            hexVal = hex(ord(binValue))
            string += '\\' + hexVal
            binValue = f.read(1)
    string = re.sub('0x', 'x', string) # Replace '0x' with 'x' for your needs
    return string

def imgToBin(file):
    string = ''
    with open(file, 'rb') as f:
        binValue = f.read(1)
    return binValue


# color_data prepares a series of images for data analysis
# have to make this function more efficient!
def drawhack(path="static/assets/michaelimages/", img_list=None):
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char1.jpg"},
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char2.jpg"},
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char3.jpg"},
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char4.jpg"},
        ]
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # hack testing
        img = Image.open(file)  # opens file to work
        clear = img.copy()  # creates a copy of the file used
        draw = ImageDraw.Draw(clear)  # "draws" on the clean copy
        font = ImageFont.truetype("arial.ttf", 30)  # font and fontsize
        text = "CHARMANDER"  # the text
        draw.text((0, 0), text, (255,255,255), font=font)  # the drawing process
        clear.save(path + 'new' + img_dict['file'])  # saves clean copy as "new<file>.jpg"
    # appending to img_list so the images can load on the html
    img_list.clear()
    img_list.append({'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "newchar1.jpg"},)
    img_list.append({'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "newchar2.jpg"},)
    img_list.append({'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "newchar3.jpg"},)
    img_list.append({'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "newchar4.jpg"})

    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)

        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        # hack testing
    return img_list  # list is returned with all the attributes for each image dictionary

def michael_image_data(path="static/assets/michaelimages/", img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char1.jpg"},
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char2.jpg"},
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char3.jpg"},
            {'source': "ウノユウジ https://twitter.com/uno_yu_ji", 'label': "Charmander", 'file': "char4.jpg"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # here is commit for adding text into images for Anirudh's rbg page
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary
# HACK- delete third for loop, put it in the one above, define grey data array above.

def anirudh_image_data(path="static/assets/anirudhimages/", img_list=None):  # change to anirudhimages
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Beach", 'label': "Beach", 'file': "reducedbeach.jpg"},
            {'source': "Fall", 'label': "Fall", 'file': "reducedfall.jpg"},
            {'source': "Spring", 'label': "Spring", 'file': "reducedspring.jpg"},
            {'source': "Winter", 'label': "Winter", 'file': "reducedwinter.jpg"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # HERE is commit for adding text into images
        draw = ImageDraw.Draw(img_reference)
        draw.text((25, 25), "Writing on images!", fill=(500, 500, 500))  # draw in image
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex((pixel[0]) + (pixel[1]) + (pixel[2]))[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/

        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary

def ethan_image_data(path="static/assets/ethanimages/", img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Van Theo", 'label': "GatsVo2", 'file': "gatsVo2.png"},
            {'source': "Anirudh", 'label': "POV:You're Under 16", 'file': "anirudhsus.png"},
            {'source': "Hamilton", 'label': "Evo", 'file': "vomilton.png"},
            {'source': "Liberty Park", 'label': "Scripted", 'file': "ankles.png"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # here is commit for adding text into images for Anirudh's rbg page
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary
# HACK- delete third for loop, put it in the one above, define grey data array above.

def size_hack(path="static/assets/ethanimages/", img_list=None):  # change to ethanimages plz
    global img_reference
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            # add your own
            {'source': "Van Theo", 'label': "GatsVo2", 'file': "gatsVo2.png"},
            {'source': "Anirudh", 'label': "POV:You're Under 16", 'file': "anirudhsus.png"},
            {'source': "Hamilton", 'label': "Evo", 'file': "vomilton.png"},
            {'source': "Liberty Park", 'label': "Scripted", 'file': "ankles.png"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        img = Image.open(file)  # opens file to work
        clear = img.copy()  # creates a copy of the file used
        new = clear.resize((256,256))
        new.save(path + 'new' + img_dict['file'])  # saves clean copy as "new<file>.jpg"
        # appending to img_list so the images can load on the html
    img_list.clear()
    img_list.append({'source': "Van Theo", 'label': "GatsVo2", 'file': "newgatsVo2.png"},)
    img_list.append({'source': "Anirudh", 'label': "POV:You're Under 16", 'file': "newanirudhsus.png"},)
    img_list.append({'source': "Hamilton", 'label': "Evo", 'file': "newvomilton.png"})
    img_list.append({'source': "Liberty Park", 'label': "Scripted", 'file': "newankles.png"})
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        # here is commit for adding text into images for Anirudh's rbg page
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary

def james_image_data(path="static/assets/jamesimages/", img_list=None):  # change to jamesimages
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Seagals", 'label': "Seagals", 'file': "Seagals.jpg"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)  # PIL
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
    return img_list  # list is returned with all the attributes for each image dictionary

# run this as standalone tester to see data printed in terminal
# if __name__ == "__main__":
#     local_path = "../static/img/"
#     img_test = [
#         {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
#     ]
#     items = image_data(local_path, img_test)  # path of local run
#     for row in items:
#         # print some details about the image so you can validate that it looks like it is working
#         # meta data
#         print("---- meta data -----")
#         print(row['label'])
#         print(row['format'])
#         print(row['mode'])
#         print(row['size'])
#         # data
#         print("----  data  -----")
#         print(row['data'])
#         print("----  gray data  -----")
#         print(row['gray_data'])
#         print("----  hex of data  -----")
#         print(row['hex_array'])
#         print("----  bin of data  -----")
#         print(row['binary_array'])
#         # base65
#         print("----  base64  -----")
#         print(row['base64'])
#         # display image
#         print("----  render and write in image  -----")
#         filename = local_path + row['file']
#         image_ref = Image.open(filename)
#         draw = ImageDraw.Draw(image_ref)
#         draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))  # draw in image
#         image_ref.show()
# print()