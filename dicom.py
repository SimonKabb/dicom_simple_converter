import pathlib

import cv2
import numpy
import pydicom
from PIL import Image
from pydicom.errors import InvalidDicomError


def make_filename(filename):
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
        'M', 'J', 'P', 'G'), 12, (512, 512))  # Initialize Video File
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
    array = numpy.reshape(array[35], (512, 512))
    data = Image.fromarray(array)
    data.save('gfg_dummy_pic.png')


def search_files():
    currentDirectory = pathlib.Path('./dicom').glob('**/*')
    # for currentFile in currentDirectory.iterdir():
    files = [x for x in currentDirectory if x.is_file()]
    for file in files:
        make_video(str(file))


if __name__ == '__main__':
    search_files()
