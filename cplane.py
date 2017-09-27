#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abscplane import AbsComplexPlane

###
# Name: Evan A Walker, Tim lastName
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , TimEmailHere
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###


class ListComplexPlane(AbsComplexPlane):
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        #fs    =
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)
        print(dx)
        listoflists = []
        for i in range(xmin,xmax):
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            listoflists.append(sublist)
        print(listoflists)
        self.plane = listoflists

    def refresh(self):
        pass

    def apply(self, f):
        pass

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        pass



myPlane = ListComplexPlane(0,10,11,0,10,11)