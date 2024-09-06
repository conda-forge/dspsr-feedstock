import dspsr
m = dspsr.IOManager()
t = dspsr.TimeSeries()
m.set_output(t)
del t
del m
