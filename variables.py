from platform import system
OS = system()
WIN = False
LIN = False
if OS == "Windows":
    WIN =True
elif OS == "Linux":
    LIN = True

DESCRIPTION = """
The "Steg_Py_Graphy" tool is a valuable asset for professionals in the fields of digital forensics and cybersecurity. 
With its user-friendly design and ability to handle various media formats, it empowers users to unveil hidden data within multimedia files, 
thereby aiding in the detection and analysis of potential security threats and concealed information."""
EG_DESCRIPTION = """
The Steg_Py_Graphy tool is a powerful tool for reverse steganography, capable of extracting concealed data from various digital media files,
including audio, video, and image formats. With its efficient scanning algorithm and support for multiple file types,
this script enables users to reveal hidden information for digital forensics, security analysis, and investigation purposes."""


