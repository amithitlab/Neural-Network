# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:22:42 2018

@author: CAPTAIN
"""

import numpy as np
import pandas as pd

x,y,w1,b1,w2,b2,w3,b3


def forward(x):
    z1=x.w1+b
    a1=tanh(z1)
    z2=a1.w2+b2
    a2=tanh(z2)
    z3=a2.w3+b3
    a3=softmax(z3)
