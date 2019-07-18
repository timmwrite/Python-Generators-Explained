Generators in Python

-> Genrator function will automatically suspend and resume their excution and state around the last point of value generation.
-> The advantage is that instend of having to compute an entire series of value up front. The generation computes the value, waits untill the next value is called
-> In case the user wants to have a list, the need to transform the genator to a list with list(range(0,10))
