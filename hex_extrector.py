##############################################################################
#  Steg Py Graphy - Python Script
# Description: Steg Py Graphy is a Python script designed to perform reverse steganography, extracting hidden files from other files. It can extract various types of files, such as images, audio, videos, or all types combined, from a single file.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import argparse
from variables import *
from extractor_stego import Stego_Extrector

def main():
    """
    Start the script and the arguments.
    """
    parser = argparse.ArgumentParser(
                        prog='Steg_Py_Graphy',
                        description=DESCRIPTION,
                        epilog=EG_DESCRIPTION)

    ###  Extract sub-command
    subparsers = parser.add_subparsers(title='Sub-Commands', dest='command')
    extract_parser = subparsers.add_parser('extract', help='Extract files')
    extract_group = extract_parser.add_mutually_exclusive_group(required=True)
    extract_group.add_argument('-f', '--file-name', type=str, dest="file_name",
                               help="Specify the name of a single file")
    extract_group.add_argument('-F', '--files-names', type=str, dest="file_names",
                               help="Specify the names of multiple files (example: file1.txt,file2.txt)")
    extract_parser.add_argument('-e', '--extract-type', type=str, required=True, action="store", dest="extract",
                                help="Specify the extract type", choices=['image', 'audio', 'video', 'all'])
    ###  Convert sub-command
    # convert_parser = subparsers.add_parser('convert', help='In Develop')

    args = parser.parse_args()

    if args.file_names:
        extract_loop(args, parser)
    elif args.command == 'extract':
        extract_statement(args, parser)
    else:
        parser.print_help()

def extract_loop(args, parser):
    """
    Loop the list of directories and enter each one to the extract statement.
    :param args: The command arguments, dict.
    :param parser: Arguments parser, object.
    :return:
    """
    for file_name in args.file_names.split(','):
        args.file_name = file_name.strip()
        extract_statement(args, parser)

def extract_statement(args, parser):
    """
    The main statement of the command arguments.
    :param args: The command arguments, dict.
    :param parser: Arguments parser, object.
    """
    stego = Stego_Extrector(args.file_name, args)
    if args.extract.lower() == "image":
        stego.image_extract(value="image")
    elif args.extract.lower() == "audio":
        stego.audio_extract(value="audio")
    elif args.extract.lower() == "video":
        stego.video_extract(value="video")
    elif args.extract.lower() == "all":
        stego.all_extract()
    else:
        parser.error("This option is not valid...")

if __name__ == "__main__":
    main()
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
