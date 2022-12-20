import pathlib

import cv2
import numpy
import pydicom
from PIL import Image, ImageEnhance
from pydicom.errors import InvalidDicomError
from sys import platform


def make_filename(filename):
    if platform == 'win32':
        filename = 'videos\\' + filename.split('\\')[1]
    else:
        filename = 'videos/' + filename.split('/')[1]
    return filename.split('.')[0] + '.avi'


def make_video(filename):
    try:
        ds = pydicom.read_file(filename)
    except InvalidDicomError:
        print(f'file {filename} is not dicom')
        return None
    array = ds.pixel_array
    video = cv2.VideoWriter(make_filename(filename), cv2.VideoWriter_fourcc(
        'M', 'J', 'P', 'G'), 12, (750, 750))  # Initialize Video File
    for frame in array:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        video.write(frame_rgb)
    video.release()


def make_photo(filename, frame):
    try:
        ds = pydicom.read_file(filename)
    except InvalidDicomError:
        return None
    array = ds.pixel_array
    array = numpy.reshape(array[20], (750, 750))
    data = Image.fromarray(array).convert('RGB')
    data.save('gfg_dummy_pic.png')

    im = Image.open('gfg_dummy_pic.png')
    im = im.convert('LA')
    # print(im.mode)
    # enhancer = ImageEnhance.Brightness(im)
    # im_output = enhancer.enhance(0.5)
    # enhancer = ImageEnhance.Contrast(im)
    # print(enhancer)
    # im_output = enhancer.enhance(10)
    # enhancer = ImageEnhance.Sharpness(im)
    # im_output = enhancer.enhance(2)
    im.save('gfg_dummy_pic1.png')


def search_files():
    currentDirectory = pathlib.Path('./dicom').glob('**/*')
    # for currentFile in currentDirectory.iterdir():
    files = [x for x in currentDirectory if x.is_file()]
    for file in files:
        make_video(str(file))


if __name__ == '__main__':
    search_files()
