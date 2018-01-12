import re
import urllib.request
import numpy as np
import time
from pylab import imshow, show, get_cmap
from numpy import random

integerGenURL10000 = "https://www.random.org/integers/?num=10000&min=1&max=10000&col=1&base=10&format=plain&rnd=new"
integerGenURL6384 = "https://www.random.org/integers/?num=6384&min=1&max=6384&col=1&base=10&format=plain&rnd=new"

def testDataGen():
    arr1d = []
    lines128 = [b'100\n', b'92\n', b'52\n', b'57\n', b'23\n', b'94\n', b'99\n', b'10\n', b'1\n', b'90\n', b'8\n',
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
    for aVal in lines128:
        # print(str(aVal))
        num = int(re.findall(r'\d+', aVal.decode("utf-8"))[0])
        arr1d.append(num)

    arrnp = np.array(arr1d)
    arrfull = np.repeat(arrnp, 128)

    print(len(arrfull))

    return  arrfull

def parseData(data):
    arr1d = []
    lines = data.splitlines(True)
    print("parseData >> ",lines)

    for aVal in lines:
        num = float(re.findall(r'\d+', aVal.decode("utf-8"))[0])
        arr1d.append(num)

    return arr1d


def generator(url):
    """

    :param url:
    :param type:
    :return:
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

    :return:
    """
    arr1 = generator(integerGenURL10000)
    arr2 = generator(integerGenURL6384)
    arr = arr1.append(arr2)

    Z = np.array(arr)#random.random((5, 5))  # Test data
    #Z = random.random((128, 128))

    Z = Z.reshape(128,128)

    print(Z)
    imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
    show()

if __name__ == "__main__":
    generateRGBBitMap()

