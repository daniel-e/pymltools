#!/bin/bash

IMGPATH=../../pymltools.wiki/images/

set -e

echo plot_perceptron_nonlin.py
./plot_perceptron_nonlin.py 
convert -resize 640 perceptron_nonlin.png $IMGPATH/perceptron_nonlin.png
rm perceptron_nonlin.png

echo plot_perceptron_xor.py
./plot_perceptron_xor.py
convert -resize 640 perceptron_xor.png $IMGPATH/perceptron_xor.png
rm perceptron_xor.png

echo plot_perceptron.py
./plot_perceptron.py
convert -resize 640 perceptron.png $IMGPATH/perceptron.png
rm perceptron.png

echo plot_perceptron_9clusters.py
./plot_perceptron_9clusters.py
convert -resize 640 perceptron_9clusters.png $IMGPATH/perceptron_9clusters.png
rm perceptron_9clusters.png

echo plot_synthetic_data.py
./plot_synthetic_data.py
convert -resize 400 syn_1.png $IMGPATH/syn_1.png
rm syn_1.png
convert -resize 400 syn_2.png syn_2a.png
convert -resize 400 syn_3.png syn_3a.png
convert +append syn_2a.png syn_3a.png $IMGPATH/syn_1_2.png
rm syn_2.png syn_2a.png syn_3.png syn_3a.png
convert -resize 400 syn_4.png $IMGPATH/syn_4.png
rm syn_4.png

