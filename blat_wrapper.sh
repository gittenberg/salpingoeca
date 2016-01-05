#!/bin/bash
gawk '{command = ("python gen.py")
    print $0 | command
    close(command)}' RS='>' bigfile.txt