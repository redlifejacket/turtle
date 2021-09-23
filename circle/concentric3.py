#!/usr/bin/env python

# https://www.educba.com/python-turtle

from turtle import *
penup()
for a in range(40, -1, -1):
    stamp()
    left(a)
    forward(20)