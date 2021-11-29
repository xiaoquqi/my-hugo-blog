#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import re

files = glob.glob("../content/posts/*")

# Add --- in the first line if missing
#for f in files:
#    with open(f, "r") as rfhd:
#        lines = rfhd.readlines()
#        first_line = lines[0].strip()
#        if not first_line == "---":
#            print(f)
#            lines.insert(0, "---\n")
#            #print(lines)
#            #with open(f, "w+") as wfhd:
#            #    wfhd.writelines(lines)

# Replace {% img to standard markdown format
#for f in files:
#    with open(f, "r") as rfhd:
#        lines = rfhd.readlines()
#
#        for index, line in enumerate(lines):
#
#            line = line.strip()
#            if re.match(r"{\s*%\s*img", line):
#                print("Found line:", line)
#
#                image_path = None
#                m1 = re.match(r"{\s*%\s*img\s*(\/images\/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+)\s+", line)
#                if m1:
#                    image_path = m1.group(1)
#                    print(m1.group(1))
#
#                m2 = re.match(r"{\s*%\s*img\s+\w+\s+(\/images\/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+)\s+", line)
#                if m2:
#                    image_path = m2.group(1)
#                    print(m2.group(1))
#
#                new_image_path = "![](%s)\n" % image_path
#                print(new_image_path)
#                lines[index] = new_image_path
#                print(lines)
#
#        with open(f, "w+") as wfhd:
#            wfhd.writelines(lines)

SEARCH_LINES = 25
for f in files:
    with open(f, "r") as rfhd:
        lines = rfhd.readlines()
        print("Reading file:", f)

        # If we need to do replace in the file
        if_replace = False

        # In code area, ignore start #
        if_code_start = False

        for index, line in enumerate(lines):

            if re.match(r"^\s*```", line):
                if_code_start = not if_code_start
            print("if code start: [%s]%s" % (index, if_code_start))

            if re.match(r"^\s*#\s+\S+", line):
                if not if_code_start:
                    if_replace = True
            print("if file need to replace: %s" % if_replace)

            if re.match(r"^\s*#", line) and if_replace:
                print("Orig replace line is: %s" % line)
                print("Will replace line to: #%s" % line)
                lines[index] = "#%s" % line

        with open(f, "w+") as wfhd:
            wfhd.writelines(lines)
