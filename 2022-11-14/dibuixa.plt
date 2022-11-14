#!/usr/bin/env gnuplot

set terminal png 
set output "temps.png"

plot "seleccio.txt" with linespoints,  "insercio.txt" with linespoints