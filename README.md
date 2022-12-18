# Dicom simple converter
## Converts dicom files to avi format.
Currently only works on mac and linux. Soon I will redo the paths to work in Windows. At the moment, I checked the performance on the files of the Siemens angiographic unit. *.ima format.

## Instructions:
- install venv
`python3 -m venv venv`
`source venv/bin/activate`

- install requirements:
`pip install -r requrements.txt`

- upload files to ./dicom 
- run program:
`python3 dicom.py`
After the end of the program, videos in .avi format will be located in the videos folder.


