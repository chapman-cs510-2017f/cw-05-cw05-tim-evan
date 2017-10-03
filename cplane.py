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
    """this function is the constructor and implements all private vars to given input,
    implements self.plane(complex plane) using the given input
    Args:
        self (key word): to refrence private vars
        xmin (int): minimum x value in table
        xmax (int): maximum x value in table
        xlen (int): # x points
        ymin (int): minimum y value in table
        ymax (int): maximum y value in table
        ylen (int): # y points
    return:
        Null: returns nothing
    """
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
                sublist.append((self.xmax - i*dx)+(self.ymin + j*dy)*1j)
            listoflists.append(sublist)
        self.plane = listoflists

        self.fs = []
        return


    def printTable(self):
        """this function prints complex plane in a legible fashion.
        Args:
            self (key word): to refrence private vars
        return:
            Null: returns nothing
        """
        print("##################-Complex Plane-####################")
        for s in self.plane:
            print(*s)
        print("#####################################################")
        return

    def refresh(self):
         """this function resets self.plane to private stored variables that define the table
         and clears all functions applied by setting self.fs = []
        Args:
            self (key word): to refrence private vars
        return:
            Null: returns nothing
        """
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
         """this function adds given input f to self.fs, then
        applies f to all pnts in self.plane
        Args:
            self (key word): to refrence private vars
            f (fxn): complex function
        return:
            Null: returns nothing
        """
        self.fs.append(f)
        for i in range(self.xlen):
            for j in range(self.ylen):
                self.plane[i][j] = f(self.plane[i][j]) ### Replace with the grid function
        return


    def setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen):
         """this function changes the complex plane size using given input values.
        Args:
            self (key word): to refrence private vars
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        return:
            Null: returns nothing
        """
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
        """applies all of the transformations in fs, in order, to the plane
        without adding functions to fs. This changes self.plane
        Args:
            self (key word): to refrence private vars
        return:
            Null: returns nothing
        """
        for k in range(len(self.fs)):
            f = self.fs[k]
            for i in range(self.xlen):
                for j in range(self.ylen):
                    self.plane[i][j] = f(self.plane[i][j])
        return

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
         """this function changes the table size using given input values,
         and re-applys all f in self.fs. this is achieved by calling setPlane and
         applyAllF, see also these fxns
        Args:
            self (key word): to refrence private vars
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        return:
            Null: returns nothing
        """
        self.setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        self.applyAllF()
        return






myPlane = ListComplexPlane(-10,10,21,-10,10,21)
myPlane.printTable()

def f(x):
    return x*x

myPlane.apply(f)
myPlane.printTable()
myPlane.zoom(-5,5,6,-5,5,6)
myPlane.printTable()
myPlane.refresh()
myPlane.printTable()