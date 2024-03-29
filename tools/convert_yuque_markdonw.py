#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This script is ued to format markdown which exported by yuque
#
# Format Handler:
#
#   1. Add emtpy line between paragraphs, not in ``````
#   2. Download image into static path and fix image url

import glob
import re
import os
import sys
from urllib.request import urlretrieve

current_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_path, "..", "static/images")

def usage():
    print("Usage: %s </path/to/your/filename>" % sys.argv[0])

if len(sys.argv) < 2:
    print("ERROR: No filename given")
    usage()
    sys.exit(1)

filename = sys.argv[1]

image_prefix_name = os.path.splitext(os.path.basename(filename))[0]

with open(filename, "r") as rfhd:
    lines = rfhd.readlines()
    print("Reading file:", filename)

    # if we need to add \n after line
    is_add_newline = False

    # If we need to do replace in the file
    is_replace = False

    # In code area, ignore start #
    is_code_start = False

    for index, line in enumerate(lines):
        print("----------------")
        print("Current Line is: %s" % line.strip())
        print("----------------")

        # Ignore code start or markdown metdata start
        if re.match(r"^\s*```", line) or re.match(r"^\s*---", line):
            is_code_start = not is_code_start
        #print("if code start: [%s]%s" % (index, is_code_start))

        # We only add newline for content line, by default:
        #
        #   1. Empty Line
        #   2. Start with > Line
        #
        # will be ignored
        if re.match(r"^\s*$", line.strip()) or re.match(r"^\>", line):
            print("Ignore line: %s" % line)
            is_add_newline = False
        else:
            if not is_code_start:
                is_add_newline = True
        #print("if file need to add newline: %s" % is_add_newline)

        if is_add_newline:
            print("Orig replace line is: |%s|" % line)
            print("Will replace line to: %s\n" % line)
            lines[index] = "%s\n" % line

        # Replace image, by default the image url will be:
        # ![image.png](https://cdn.nlark.com/yuque/path/xxxx.png#REMOVED_PART
        if re.match(r"!\[(.*?)\].*yuque", line):
            #replace_pattern = re.compile(r"^(!\[(.*?)\]\(https://.*?\.(jpeg|jpg|gif|png))#.*$")
            #replace_image_line = replace_pattern.sub(r"\1", line.strip()) + ")\n\n"
            #replace_image_line = replace_image_line.replace(r'(jpeg|jpg|gif|png)#(.*)+', 'png)', line)
            find_pattern = re.compile(r'https://.*?\.(jpeg|jpg|gif|png)')
            match = find_pattern.search(line)
            image_url = match.group()

            image_extname = os.path.splitext(os.path.basename(image_url))[1]

            image_name = "%s-%s%s" % (image_prefix_name, str(index), image_extname)
            save_path = os.path.join(image_path, image_name)
            print(save_path)

            print("Downloading image %s to %s..." % (image_url, save_path))
            urlretrieve(image_url, save_path)

            replace_image_line = "![%s](/images/%s)\n\n" % (image_name, image_name)
            print("Old image line: %s" % line)
            print("New image line: %s" % replace_image_line)
            lines[index] = replace_image_line

    with open(filename, "w+") as wfhd:
        wfhd.writelines(lines)
