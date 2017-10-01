#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

from abscplane import AbsComplexPlane

class ListComplexPlane(AbsComplexPlane):
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen

        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)

        self.plane = []
        self.fs = []

    def __generate_planegrid(self,xmin,xmax,xlen,ymin,ymax,ylen,dx,dy):
        """Builds complex plane"""
        for i in range(xmin,xmax):
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            self.plane.append(sublist)
        print(self.plane)
        return self.plane
#ToDo: integrate functions...

    def refresh(self):
        """restores to its original grid values"""
        self.plane = []
        self.fs = []
        x = self.xmin
        y = self.ymin
        xl= self.xlen
        yl = self.ylen
        dx = (xmax - x)/(xl-1)
        dy = (ymax - y)/(y1-1)

    def apply(self, f):
        self.f = f
        self.fs.append(self.f)

        for i in range(self.xlen):
            for j in range(self.ylen):
                self.plane[i][j] = f(self.plane[i][j]) ### Replace with the grid function
        self.fs.append(f)


    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen

        dx = (xmax - x)/(xlen-1)
        dy = (ymax - y)/(y1en-1)

        """Builds complex plane"""
        for i in range(xmin,xmax):
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            self.plane.append(sublist
#ToDo: integrate functions...


#myPlane = ListComplexPlane(0,10,11,0,10,11)
