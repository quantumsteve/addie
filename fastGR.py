import sys
import numpy as np
from PyQt4 import QtCore, QtGui, uic
import matplotlib.pyplot as plt


qtCreatorFile = "gui_fgr3.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #btn commands
        self.btnGenerateGR.clicked.connect(self.calculateGR)
        self.btnLoadSQ.clicked.connect(self.read_SQ_file)
        self.btnPlotGR.clicked.connect(self.plot_GR)
        self.btnPlotSQ.clicked.connect(self.plot_SQ)
        self.btnSaveGR.clicked.connect(self.save_GR_file)
        self.btnPlotQSQ.clicked.connect(self.plot_QSQ)
        self.btnPlotSQ.setEnabled(False)
        self.btnPlotGR.setEnabled(False)
        self.btnGenerateGR.setEnabled(False)
        self.btnSaveGR.setEnabled(False)
        self.btnPlotQSQ.setEnabled(False)

        self.btnPlotQSQ.setMinimumSize(100, 20)

        self.loaded_once = False

        #setup variables
        self.Q = []
        self.SQ = []
        self.r = []
        self.GR = []

    def read_SQ_file(self):
        self.Q = []
        self.SQ = []

        name = QtGui.QFileDialog.getOpenFileName(self, 'Opener File Thinger')
        print "opening file: "+str(name)
        with open(name, 'r') as myfile:
            data = myfile.readlines()

        #print "file length was "+str(len(data))
        #determine length of junk at start of file
        for i in range(len(data)):
            if(len(data[i].strip()) > 0): #check that not a blank line
                is_good = True
                for k in range(i,i+10):
                    if (len(data[k].strip())) > 0: #now check if THIS line isn't blank
                        try:
                            float(data[k].split()[0])
                            yes_this = True
                        except ValueError:
                            yes_this = False

                        if yes_this:
                            pass #s'all good
                        else:
                            is_good = False
                            break
                    else:
                        is_good = False
                        break
            if is_good:
                start = i
                break
            #override
            #start = 5
            #print "starting at start "+str(start)

        for i in range(0,len(data)-start):
            self.Q.append(float(data[i+start].split()[0]))
            self.SQ.append(float(data[i+start].split()[1]))

        #configure Spin Boxes based on data (assume linearly spaced)
        if self.loaded_once == False:
            self.doubleSpinBoxQmin.setValue(self.Q[0])
            self.doubleSpinBoxQmax.setValue(self.Q[len(self.Q)-1])
            self.doubleSpinBoxQmin.setMinimum(self.Q[0])
            self.doubleSpinBoxQmin.setMaximum(self.Q[len(self.Q)-2])
            self.doubleSpinBoxQmax.setMaximum(self.Q[len(self.Q)-1])
            delq = self.Q[1]-self.Q[0]
            self.doubleSpinBoxQmin.setSingleStep(delq)
            self.doubleSpinBoxQmax.setSingleStep(delq)
            self.loaded_once = True

        self.btnPlotSQ.setEnabled(True)
        self.btnGenerateGR.setEnabled(True)
        self.btnPlotQSQ.setEnabled(True)

    def save_GR_file(self):
        #name = QtGui.QFileDialog.getSaveFileName(self, 'Makey-Saves')
        maybe_name = "myGR_Qmin"+str(self.doubleSpinBoxQmin.value())+"_Qmax"+str(self.doubleSpinBoxQmax.value())+".gr"
        name = QtGui.QFileDialog.getSaveFileName(self, ('Makey-Saves'),maybe_name)
        outfile = open(name, 'w')
        for i in range(len(self.r)):
            outbit = str(self.r[i]) + " " + str(self.GR[i])+"\n"
            outfile.write(outbit)
        outfile.close()

    def calculateGR(self):
        rmax = float(self.doubleSpinBoxRmax.value())
        rmin = float(self.doubleSpinBoxRmin.value())
        delr = float(self.doubleSpinBoxDelR.value())
        qmin = float(self.doubleSpinBoxQmin.value())
        qmax = float(self.doubleSpinBoxQmax.value())

        self.r = []
        self.GR = []
        self.r=np.arange(rmin,rmax+delr,delr)
        self.GR=np.zeros(len(self.r))
        for ri in range(len(self.r)):
            completed_per = 100.0 * self.r[ri] / self.r[len(self.r)-1]
            self.progressBar.setValue(completed_per)
            for qi in range(len(self.Q)):
                if self.Q[qi] >= qmin and self.Q[qi] <= qmax:
                    self.GR[ri] = self.GR[ri] + self.Q[qi]*(self.SQ[qi])*np.sin(self.r[ri]*self.Q[qi])
        self.GR = self.GR / (16.0 * np.pi)
        self.btnPlotGR.setEnabled(True)
        self.btnSaveGR.setEnabled(True)

        print "my length for r is: "+str(len(self.r))

    def plot_QSQ(self):
        qsq = np.copy(self.SQ)
        for i in range(len(qsq)):
            qsq[i] = qsq[i] * self.Q[i]
        plt.plot(self.Q,qsq);plt.show()

    def plot_SQ(self):
        plt.plot(self.Q,self.SQ);plt.show()

    def plot_GR(self):
        plt.plot(self.r,self.GR);plt.show()

    def say_hello(self):

        print "sup"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
