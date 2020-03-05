#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:37:18 2020

@author: virati
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def gen_lin_data(factor,noise,samples):
    x = np.random.uniform(-10,10,size=(samples,))
    y = factor * x + np.random.normal(0,noise,size=x.shape)
    
    return x,y

def simple_eg(slope=1.0,noise=0.0,samples=100):
    x,y = gen_lin_data(slope,noise,samples)
    #x = np.random.uniform(-10,10,size=(samples,))
    #y = slope * x + np.random.normal(0,noise,size=x.shape)
    
    plt.figure()
    plt.scatter(x,y)
    plt.scatter(x,np.random.normal(0,noise,size=x.shape),color='red',alpha=0.4)
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.axis('off')
    
    plt.legend(['Correlated','Uncorrelated'])
    corr_val = stats.pearsonr(x,y)
    plt.text(2,-10,s='Pearson: ' + str(corr_val[0]) + '\n p=' + str(corr_val[1]))
    plt.show()