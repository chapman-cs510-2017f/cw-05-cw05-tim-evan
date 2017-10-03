#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abscplane import AbsComplexPlane

###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###





##
   ## evans number: 4082341114
##







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

        listoflists = []
        for i in range(self.xlen):
            sublist = []
            for j in range(self.ylen):
                sublist.append((self.xmin + i*dx)+(self.ymin +j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists

        self.fs = []

    def __generate_planegrid(self,xmin,xmax,xlen,ymin,ymax,ylen,dx,dy):
        """Builds complex plane"""
        for i in range(xmin,xmax):           # he wants us to generate the plane in the __init__
            sublist = []
            for j in range(ymin,ymax):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            self.plane.append(sublist)
        return self.plane
#ToDo: integrate functions...

    def printTable(self):
        print("##################-Complex Plane-####################")
        for s in self.plane:
            print(*s)
        print("#####################################################")
        return

    def refresh(self):
        dx = (self.xmax - self.xmin)/(self.xlen - 1)
        dy = (self.ymax - self.ymin)/(self.ylen - 1)
        listoflists = []
        for i in range(self.xlen):
            sublist = []
            for j in range(self.ylen):
                sublist.append((self.xmin + i*dx)+(self.ymin +j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists
        self.fs = []
        return

    def apply(self, f):
        self.fs.append(f)
        for i in range(self.xlen):
            for j in range(self.ylen):
                self.plane[i][j] = f(self.plane[i][j]) ### Replace with the grid function
        return


    def setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)

        listoflists = []
        for i in range(self.xlen):
            sublist = []
            for j in range(self.ylen):
                sublist.append((xmin + i*dx)+(ymin +j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists
        return

    def applyAllF(self):
        """applies all of the transformations in fs in order to the plane
        without adding functions to fs
        """
        for k in range(len(self.fs)):
            f = self.fs[k]
            for i in range(self.xlen):
                for j in range(self.ylen):
                    self.plane[i][j] = f(self.plane[i][j])
        return

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        self.applyAllF()
        return






myPlane = ListComplexPlane(-10,10,21,-10,10,21)
myPlane.printTable()
myPlane.zoom(-5,5,6,-5,5,6)
myPlane.printTable()

def f(x):
    return x*x

myPlane.apply(f)
myPlane.printTable()