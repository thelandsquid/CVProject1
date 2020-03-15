from __future__ import division
import cv2
import numpy as np
import sys
import luv_lscl, xyz_lscl, luv_classhisteq, xyz_classhisteq, luv_histeq, xyz_histeq

def main():
    luv_lscl(sys.argv)
    xyz_lscl(sys.argv)
    luv_histeq(sys.argv)
    luv_classhisteq(sys.argv)
    xyz_histeq(sys.argv)
    xyz_classhisteq(sys.argv)

main()