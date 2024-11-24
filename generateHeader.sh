rm ./bmps/*.bmp
ffmpeg -i ba.mp4 -r 6 bmps/$filename%03d.bmp
./badapple.py