import re
import urllib.request
import numpy as np
import time
from pylab import imshow, show, get_cmap, savefig
from numpy import random

integerGenURL10000 = "https://www.random.org/integers/?num=10000&min=1&max=10000&col=1&base=10&format=plain&rnd=new"
integerGenURL6384 = "https://www.random.org/integers/?num=6384&min=1&max=6384&col=1&base=10&format=plain&rnd=new"

def testDataGen():
    """
    Only for TESTING - refer to main() it is commented out for final execution.
    This function is useful for offline testing without contacting Random.org
    a 128 byte response string obtained from random.org is used for solving question#1
    :return: returns a numpy array of 128 X 128
    """
    arr1d = []
    bytesResponse128 = [b'100\n', b'92\n', b'52\n', b'57\n', b'23\n', b'94\n', b'99\n', b'10\n', b'1\n', b'90\n', b'8\n',
                b'99\n', b'70\n',
                b'26\n', b'17\n', b'60\n', b'3\n', b'45\n', b'90\n', b'4\n', b'61\n', b'89\n', b'78\n', b'45\n',
                b'66\n', b'77\n',
                b'66\n', b'81\n', b'33\n', b'38\n', b'27\n', b'93\n', b'48\n', b'66\n', b'48\n', b'70\n', b'80\n',
                b'65\n',
                b'52\n', b'11\n', b'55\n', b'59\n', b'54\n', b'90\n', b'79\n', b'95\n', b'39\n', b'3\n', b'33\n',
                b'8\n', b'57\n',
                b'5\n', b'1\n', b'77\n', b'48\n', b'84\n', b'43\n', b'25\n', b'99\n', b'52\n', b'21\n', b'31\n',
                b'83\n', b'86\n',
                b'88\n', b'75\n', b'15\n', b'67\n', b'60\n', b'47\n', b'88\n', b'12\n', b'8\n', b'60\n', b'83\n',
                b'90\n', b'87\n',
                b'60\n', b'81\n', b'35\n', b'81\n', b'25\n', b'80\n', b'50\n', b'74\n', b'28\n', b'18\n', b'59\n',
                b'2\n', b'91\n',
                b'27\n', b'31\n', b'90\n', b'6\n', b'84\n', b'96\n', b'81\n', b'90\n', b'39\n', b'64\n', b'8\n',
                b'60\n', b'83\n', b'90\n', b'87\n',
                b'60\n', b'81\n', b'35\n', b'81\n', b'25\n', b'80\n', b'50\n', b'74\n', b'28\n', b'18\n', b'59\n',
                b'2\n', b'91\n',
                b'27\n', b'31\n', b'90\n', b'6\n', b'84\n', b'96\n', b'81\n', b'90\n', b'39\n', b'64\n']
    for aVal in bytesResponse128:
        # print(str(aVal))
        num = int(re.findall(r'\d+', aVal.decode("utf-8"))[0])
        arr1d.append(num)

    arrnp = np.array(arr1d)
    arrfull = np.repeat(arrnp, 128)

    print(len(arrfull))

    return  arrfull



def parseData(data):
    """
    converts the bytes data to a 1-D array of random integers
    :param data: get the byte data separated by \n
    :return: a 1D array
    """
    arr1d = []
    lines = data.splitlines(True)
    print("parseData >> ",lines)

    for aVal in lines:
        num = float(re.findall(r'\d+', aVal.decode("utf-8"))[0])
        arr1d.append(num)

    return arr1d


def generator(url):
    """
    Triggers the random.org url for integer random number generation
    :param url: http url for integer random number generation
    :return: 1-D array of those random numbers generated
    """
    print("URL Fired >> ", url)
    request = urllib.request.Request(url)
    data = None
    try:

        # fire request
        data = urllib.request.urlopen(request).read()
    except urllib.request.HTTPError as err:
        print("HTTP ERROR CODE >> ", err.code)
        print("HTTP ERROR MSG >> ", err.msg)

    output = parseData(data)
    print("output >> ", output)
    return output

def generateRGBBitMap():
    """
    uses the np-array of 128X128 with cmap=Spectral and nearest interpolation to generate the image.
    :return: displays image using matplotlib and pylab libraries
    """

    # original HTTP call from Random API
    # 128 * 128 = 16384 pixels or random numbers
    # generating the numbers in 2 batches , 10000 and 6384.
    arr1 = generator(integerGenURL10000)
    arr2 = generator(integerGenURL6384)
    arr = arr1 + arr2 # merged into 1-D array

    Z = np.array(arr)#random.random((5, 5))  # Test data
    Z = Z.reshape(128,128)          # reshape into 128X128 numpy matrix

    print(Z)
    imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest') # convert to image
    show()



def generateRGBBitMapSampleData():
    """
    only for local TESTING purposes.
    uses the np-array of 128X128 with cmap=Spectral and nearest interpolation to generate the image.
    :return: displays image using matplotlib and pylab libraries
    """

    # try with sample test data
    arr = testDataGen()

    Z = np.array(arr)# Test data
    Z = Z.reshape(128,128)

    print(Z)
    imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
    show()


if __name__ == "__main__":
    #generateRGBBitMap()    # random.org call
    generateRGBBitMapSampleData() # local testing

