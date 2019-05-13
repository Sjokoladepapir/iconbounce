import numpy as np


class Connection:
    def __init__(self, pass_trough, bounce_v, bounce_h, end_of_path):
        self.pass_trough = pass_trough
        self.bounce_v = bounce_v
        self.bounce_h = bounce_h
        self.end_of_path = end_of_path

    def connection_type(self):
        print "pass_trough",self.pass_trough,"bounce_v",self.bounce_v,\
            "bounce_h:",self.bounce_h,"end_of_path:", self.end_of_path

    def make_connection_hex(self):
        x_3 = self.pass_trough *8
        x_2 = self.bounce_v * 4
        x_1 = self.bounce_h * 2
        x_0 = self.end_of_path
        print hex(x_0+x_1+x_2+x_3)

#a = Connection(1,1,1,1)
#a.connection_type()
#a.make_connection_hex()

#print hex(-1)