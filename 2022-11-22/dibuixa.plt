#!/usr/bin/env gnuplot

set terminal png 
set output "mergesort.png"

plot "c++.txt" with linespoints, "python.txt" with linespoints