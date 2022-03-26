#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from moviepy.editor import *
import os
import argparse


def get_webm_list(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.webm':  
                L.append(os.path.join(root, file))  
        return L


def convert_file(file_in, file_out):
    if not os.path.exists(file_in):
        print(file_in + ' file is not exist')
        return
    if file_out:
        if '.gif' not in file_out:
            file_out += '.gif'
    else:
        file_out = os.path.splitext(file_in)[0]+'.gif'

    clip = VideoFileClip(file_in)
    clip.write_gif(file_out)


def convert_directory(file_in, file_out):
    if not os.path.exists(file_in):
        print(file_in + ' directory is not exist')
        return
    if not file_out:
        file_out = file_in

    webm_list = get_webm_list(file_in)
    for file_name in webm_list:
        if '.webm' in file_name:
            clip = VideoFileClip(file_name)
            file_name = os.path.basename(file_name)
            clip.write_gif(file_out + '/' + os.path.splitext(file_name)[0]+'.gif')


def run():
    parser = argparse.ArgumentParser(description='webm2gif')
    parser.add_argument('--file_in', '-i', help='input .webm file or directory')
    parser.add_argument('--file_out', '-o', help='output .gif file or directory, default: origin filename',
                        default=None)
    args = parser.parse_args()
    file_in = args.file_in
    file_out = args.file_out
    if '.webm' in file_in:
        convert_file(file_in, file_out)
    else:
        convert_directory(file_in, file_out)


if __name__ == '__main__':
    run()
