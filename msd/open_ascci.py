import numpy as np
from datetime import datetime


class openAscci:

    col0 = []
    col1 = []
    data = 0.

    def __init__(self, fi):
        self.col0 = []
        self.col1 = []
        self.data = open(fi)
        
    def readfile2col(self):

        for line in self.data:
            tmp = line.rstrip('\n').split(' ')
            date_string = str(tmp[0])+" "+str(tmp[1])
            self.col0.append(datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
            self.col1.append(float(tmp[2]))

        return( np.array(self.col0), np.array(self.col1) )

    def promHourly(self, date, rate, nh):
        av_rate = []
        av_time = []

        for i in range(0, len(rate), nh):
            av_rate.append( np.sum( rate[i:i+nh]) )
            av_time.append( date[i] )

        return( np.array(av_time), np.array(av_rate)/(nh*1.) )
