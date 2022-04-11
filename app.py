#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.patches import ConnectionPatch
import sys
from PyQt6.QtWidgets import (
    QApplication
    ,QMessageBox
    ,QWidget
    ,QLabel
    ,QPushButton
    ,QVBoxLayout
    ,QTableWidget
    ,QTableWidgetItem
    ,QLineEdit
)


#%% Class for Circle that holds complex number for fourier transform 
class Circle():
    z : complex
    
    def __init__(self, i, complex_number_str):
        # complex number
        self.z = complex(complex_number_str)
        # complex number in polar coordinates
        (self.r, self.angle) = cmath.polar(self.z)

        # r is too big to be displayed in table so r * 0.1
        self.r = 4/( (2*i + 1)* np.pi)


#%% Class for Fourier Series
class FS():
    
    def __init__(self, Circles, Cycles, Freq):
        
        self.Circles = Circles
        self.Cycles : int = Cycles
        self.Freq   : float = Freq
        
    #%% X coordinate of n circle's center
    def Xcenter(self, n,circles, theta):
        Ans = 0

        # for inside self.Circles first n circles
        for i in range(0, n):
            Ans += circles[i].r * np.cos((2*i-1) *theta)

        return Ans
    
    #%% Y coordinate of circle's center
    def Ycenter(self, n,circles, theta):
        Ans = 0

        # for inside self.Circles first n circles
        for i in range(0, n):
            Ans += circles[i].r * np.sin((2*i-1) * theta)
        return Ans
    
    #%% Radius of circle
    def Rds(self, n,circles):
        return circles[n].r
    
    #%% Plot
    
    def PlotFS(self):
        time = np.linspace(0, self.Cycles, self.Cycles* 140)
        
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(80, 60))
        fig.suptitle('Fourier Series', fontsize = 45, fontweight = 'bold')
        
        color = cm.rainbow( np.linspace(0, 1, len(self.Circles)) )
        
        for t in time:
            
            thta = 2* np.pi* t

            #%% clear the plot
            axs[0].clear()
            
            if (t > 0):
                con.remove()
            
            #%% First plot
            
            for i, c in zip(range(0, len(self.Circles)), color):
                xc = self.Xcenter(i, self.Circles,thta)
                yc = self.Ycenter(i, self.Circles, thta)
                R  = self.Rds(i, self.Circles)
                
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
            pass


app         = QApplication([])
# detect system os and set Style
app.setStyle('macos')

window      = QWidget()
v_layout    = QVBoxLayout()
# set 720 width and 360 height
window.setFixedSize(720, 360)


# create button and 1x5 table only takes integer params like 1 1 1 1 1
table = QTableWidget(1, 5)
btn2 = QPushButton('Visualise')

# set the table header
table.setHorizontalHeaderLabels(['Coefficient 1', 'Coefficient 2', 'Coefficient 3', 'Coefficient 4', 'Coefficient 5'])


v_layout.addWidget(QLabel('18011020 - DSP Fourier Transform Visualiser'))
v_layout.addWidget(QLabel('Fill the coefficients like: 2 3+j 2-2j 2 1'))
# table column default values
table.setItem(0, 0, QTableWidgetItem('2'))
table.setItem(0, 1, QTableWidgetItem('3+j'))
table.setItem(0, 2, QTableWidgetItem('2-2j'))
table.setItem(0, 3, QTableWidgetItem('2'))
table.setItem(0, 4, QTableWidgetItem('1'))

# add float input field to take frequency value
freq = QLineEdit()
# set label
freq.setPlaceholderText('Frequency: 1.0 Hz')

v_layout.addWidget(freq)
v_layout.addWidget(table)
v_layout.addWidget(btn2)

def on_btn2_clicked():
    # Circles empty list
    app_circles = []

    # read from table values to create circle
    for i in range(0, 5):
        app_circles.append(Circle(i,table.item(0, i).text()))
    
    # get frequency value
    freq_val = float(freq.text())

    fs = FS(app_circles, 3, freq_val)
    fs.PlotFS()

btn2.clicked.connect(on_btn2_clicked)

window.setLayout(v_layout)
window.show()
app.exec()


