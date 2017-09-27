#!/usr/bin/env python3

import abscplane

###
# Name: Evan A Walker, Tim lastName
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , TimEmailHere
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

class ListComplexPlane(abscplane):
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        #fs    =
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)
        listoflists = []
        for i in range(xmin,xmax):
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            listoflists.append(sublist)
            print(listoflists)
        self.plane = listoflists



#    def refresh(self):

#    def apply(self, f):

#    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
