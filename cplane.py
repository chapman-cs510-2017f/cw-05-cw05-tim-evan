#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
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
        self.fs    = []
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)
        listoflists = []
        for i in range(xmin,xmax):
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists

    def setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen):
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)
        listoflists = []
        for i in range(xmin,xmax):
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists
        pass

    def refresh(self):
        dx = (self.xmax - self.xmin)/(self.xlen - 1)
        dy = (self.ymax - self.ymin)/(self.ylen - 1)
        listoflists = []
        for i in range(self.xmin,self.xmax):
            sublist = []
            for j in range(self.ymin,self.ymax):
                sublist.append((self.xmin + i*dx)+(self.ymin +j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists
        pass

    def apply(self, f):
        pass

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        #self.fs    = fs
        self.plane = setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen)
        pass
    def printTable(self):
        for s in self.plane:
            print(*s)
        pass


myPlane = ListComplexPlane(-10,10,21,-10,10,21)
myPlane.printTable()