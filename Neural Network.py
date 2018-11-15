# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:22:42 2018

@author: CAPTAIN
"""

import numpy as np
import pandas as pd



x,y,w1,b1,w2,b2=None


def sigmoid(z):
    sig=1/(1+np.exp(-z))
    return sig
    
def forward():
    global x,w1,b1,w2,b2
    z1=np.dot(X,w1)+b1
    a1=tanh(z1)
    z2=np.dot(a1,w2)+b2
    a2=tanh(z2)
    z3=np.dot(a2,w3)+b3
    a3=sigmoid(z3)
    

def backprop():
    global x,w1,b1,w2,b2
    
