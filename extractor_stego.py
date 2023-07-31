##############################################################################
# Steg Py Graphy - Python Script
# Description: Steg Py Graphy is a Python script designed to perform reverse steganography, extracting hidden files from other files. It can extract various types of files, such as images, audio, videos, or all types combined, from a single file.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import os
from variables import *

class Stego_Extrector:
    def __init__(self,file_name:str, args:dict) -> object:
        """
            Create an object that capable of reverse steganography.
        :param file_name: String, The file name or path.
        :param args: Dict, The arguments from the parser.
        """
        self.file_path = file_name
        if "/" in file_name or "\\" in file_name:
            self.full_file_name = file_name.split("/")[-1] if "/" in file_name else file_name.split("\\")[-1]
            self.file_name = self.full_file_name.split(".")[0]
            checker = self.full_file_name.split(".")
            self.file_type = checker[1]
        else:
            self.full_file_name = file_name
            checker = self.full_file_name.split(".")
            self.file_name =  checker[0]
            self.file_type =  checker[1]
        self.args = args


    def get_file_data(self) -> bin:
        """
        Update the value of data to be updated.
        :return: Binary of the file.
        """
        with open(self.file_path, 'rb') as f:
            return f.read()


    def audio_extract(self,value:str, check:str=None)-> None:
        """
        Will initialize the process of extracting audio files from the main file.
        Include: wav, mp3, m4a, mka, mp4.
        :param value: The type of preforms.
        :param check: check the situation of the path.
        :return:
        """
        main = self.checker(check=check, namer=value)
        headers = {
            "wav": b'\x52\x49\x46\x46',
            "mp3": b'\x49\x44\x33',
            "m4a": b'\x4D\x34\x41\x20',
            "mka": b'\x1A\x45\xDF\xA3',
            "mp4": b'\x00\x00\x00\x20\x66\x74\x79\x70\x4D\x34\x41\x20\x00\x00\x00\x00\x6D\x70\x34\x32',
        }
        for key in headers:
            self.extract(headers[key], key, main)

    def all_extract(self)-> None:
        """
        Will initialize the process of extracting all types of files from the main file.
        :return:
        """
        counter = 0
        while True:
            father = f"all_{self.file_name}{counter}"
            if not os.path.exists(father):
                os.mkdir(father)
                break
            counter += 1
        self.image_extract(check=father, value="images")
        self.audio_extract(check=father, value="audio")
        self.video_extract(check=father, value="video")
        dir_list = os.listdir(father)
        for dir in dir_list:
            if len(os.listdir(f"{father}/{dir}")) == 0:
                os.rmdir(f"{father}/{dir}")

    def checker(self,namer:str, check:str=None) -> str:
        """
        Check the file name and will change the name by the free use of them.
        :param namer: The type of extraction.
        :param check: Check the path type, None: this directory, String: new path.
        :return: String of the new path.
        """
        counter = 0
        while True:
            if check is None:
                main = f"{namer}_{self.file_name}{counter}"
                if not os.path.isdir(main):
                    os.mkdir(main)
                    return main
                else:
                    counter += 1
            else:
                main = f"{check}/{namer}_{self.file_name}{counter}"
                if not os.path.isdir(main):
                    os.mkdir(main)
                    return main
                else:
                    counter += 1

    def video_extract(self,value , check=None)-> None:
        """
        Will initialize the process of extracting videos from the main file.
        Include: wmv, mkv, avi, mp4.
        :param value: The type of preforms.
        :param check: check the situation of the path.
        :return:
        """
        main = self.checker(check=check, namer=value)
        headers = {
            "wmv": b'\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C',
            "mkv": b'\x1A\x45\xDF\xA3',
            "avi": b'\x52\x49\x46\x46',
            "mp4": b'\x00\x00\x00\x18\x66\x74\x79\x70\x6D\x70\x34\x32',
        }
        for key in headers:
            self.extract(headers[key], key, main)

    def image_extract(self,value, check=None)-> None:
        """
        Will initialize the process of extracting images from the main file.
        Include: jpeg, png, gif, svg, exif.
        :param value: The type of preforms.
        :param check: check the situation of the path.
        :return:
        """
        main = self.checker(check=check, namer=value)
        headers = {
            "jpeg": b'\xFF\xD8\xFF\xE0',
            "png": b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
            "gif": b'\x47\x49\x46\x38\x39\x61',
            "svg": b'\x3C\x3F\x78\x6D\x6C',
            "exif": b'\x45\x78\x69\x66',
        }
        for key in headers:
            self.extract(headers[key], key, main)

    def extract(self, header:bin, type:str, path:str) -> None :
        """
        It will loop check via the header and the file data to extract the information.
        :param header: The GCK's file signatures for check.
        :param type: The extract type.
        :param path: The start path.
        :return:
        """
        self.data = self.get_file_data()
        start = 0
        end = 0
        count = 0
        name= f"{path}/{self.file_path.split('.')[0]}_{type}"
        os.mkdir(name)
        names = []
        while True:
            start = self.data.find(header, end)
            if start == -1:
                break
            end = self.data.find(header, start + len(header))
            if end == -1:
                end = len(self.data)
            image_data = self.data[start:end]
            with open(f"{name}/image_{count}.{type}", "wb") as image_file:
                image_file.write(image_data)
                names.append(f"{name}/image_{count}.{type}")
            count += 1
        self.final_check(names,name, type)

    def final_check(self, names:list,path:str,type:str)-> None:
        """
        Preform a check for empty directories for removal.
        :param names: List, the full path list of new directories.
        :param path: String, The start path to directory.
        :param type: String, The file type.
        :return:
        """
        counter = 0
        for name in names:
            if os.path.isfile(name):
                counter += 1
        if counter == 0:
            os.rmdir(path)
        if len(names) != 0:
            print(f"The final amount of {type} is: {len(names)}")
# License Information
# This script is open-source and released under the MIT License.
# MIT License
# Copyright (c) 2023 Dor Dahan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# For more details, see the LICENSE file in the root directory of this repository
# or visit https://github.com/D0rDa4aN919/Steg_Py_Graphy.
