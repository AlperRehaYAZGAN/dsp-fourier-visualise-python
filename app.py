import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import signal



fs=np.pi

N =50
def DTFT(x,a,b):
    num =np.array(x)
    den = np.array([1])
    ws, h = signal.freqz(num,a=den,whole=True,worN=np.linspace(a,b,512))
    plt.plot(ws,np.abs(h))
    plt.title('DTFT Spec')
    return 

x=np.arange(1,2*N+1,1)  
y=[np.cos(math.pi*i/2) for i in x]  
# Omega c -> PI ises
# Y -> sin(PI * N / 2) / PI * N -> sinc fonksiyonu
y2 = [np.sin(math.pi*i / 2)/(math.pi*i) for i in x] 
x2 = np.linspace(-N,N,2*N)
y2 = np.sinc(x2)
y2=np.array(y2)
#Sin Katsayları
print(y2)
plt.plot(x,y2)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.patches import ConnectionPatch

#%% Class for Fourier Series

class FS():
    
    def __init__(self, Circles, Cycles):
        
        self.Circles = Circles
        self.Cycles  = Cycles
        
    #%% X coordinate of circle's center
    
    def Xcenter(self, n, theta):
        
        ''' 
            X coordinate of n th circle
        '''
        
        Ans = 0
        
        if n > 0:
            for i in range(1, n + 1):
                Ans += (4/( (2*i - 1)* np.pi))* np.cos( (2*i - 1)* theta)
    
        return Ans
    
    #%% Y coordinate of circle's center
    
    def Ycenter(self, n, theta):
        
        ''' 
            Y coordinate of n th circle
        '''
        
        Ans = 0
        
        if n > 0:
            for i in range(1, n + 1):
                Ans += (4/( (2*i - 1)* np.pi))* np.sin( (2*i - 1)* theta)
    
        return Ans
    
    #%% Radius of circle
    
    def Rds(self, n):
        
        ''' 
            Radius of n th circle
        '''
        
        return 4/( (2*n + 1)* np.pi)
    
    #%% Plot
    
    def PlotFS(self):

        time = np.linspace(0, self.Cycles, self.Cycles* 70)
        
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(80, 60))
        fig.suptitle('Fourier Series', fontsize = 45, fontweight = 'bold')
        
        color = cm.rainbow( np.linspace(0, 1, self.Circles) )
        
        for t in time:
            
            thta = 2* np.pi* t
            
            #%% clear the plot
            axs[0].clear()
            
            if (t > 0):
                con.remove()
            
            #%% First plot
            
            for i, c in zip(range(0, self.Circles), color):
                xc = self.Xcenter(i, thta)
                yc = self.Ycenter(i, thta)
                R  = self.Rds(i)
                
                crl = plt.Circle((xc, yc), R, color=c, alpha = 0.5, linewidth = 2)
                axs[0].add_artist(crl)
                
                if (i > 0):
                    axs[0].plot([xco, xc], [yco, yc], color='b', linewidth = 2)
                
                xco = xc
                yco = yc
                Ro  = R
            
            axs[0].axis('square')
            axs[0].set_xlim([ -9/np.pi, 9/np.pi ])
            axs[0].set_ylim([ -9/np.pi, 9/np.pi ])
            
            #%% Second plot
            
            if (t > 0):
                axs[1].plot([to,t], [ycirc, yc], color='m', linewidth = 1.5)
            
            to    = t
            ycirc = yc
            
            axs[1].axis('square')
            axs[1].set_xlim([ 0, 18/np.pi ])
            axs[1].set_ylim([ -9/np.pi, 9/np.pi ])
        
            #%% Line
            
            con = ConnectionPatch( xyA = (t,  yc), xyB = (xc, yc), 
                                   coordsA = 'data', coordsB = 'data',
                                   axesA = axs[1], axesB = axs[0], 
                                   color = 'red')
            axs[1].add_artist(con)
            
            plt.pause(1e-11)

#%% Main

if __name__ == '__main__':
    
    # Circles, Cycles
    fs = FS(8, 2)
    fs.PlotFS()