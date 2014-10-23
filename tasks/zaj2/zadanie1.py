# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):

	if stop == None and step==None:
		aktualna = 0
		step = 1
		stop = start_stop
		print("1")
		while aktualna < start_stop:
			yield aktualna
			aktualna += 1
	elif step==None:
		step = 1
		aktualna = start_stop
		print("2")
		while aktualna < stop:
			yield aktualna
			aktualna += 1
	else:
		aktualna = start_stop
		print("3")
		while aktualna < stop:
			yield aktualna
			aktualna = aktualna + step

print(list(xrange(10)))
print(list(xrange(10,15)))
print(list(xrange(20,15,-1)))
print(list(xrange(10,20,2)))
