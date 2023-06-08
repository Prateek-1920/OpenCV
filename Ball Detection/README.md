## APPROACH UNDERTAKEN
1. Video stream is first blurred using gaussian and median blur to reduce noise
2. This stream is then converted to HSV
3. A mask of HSV stream is made by giving lower and upper limits of the tennis ball colour.
4. Erode and dilate have been used to reduce more noise.
5. Contours are found and minEnclosingCircle is used to get the radius and centre of the circle.

## YOUTUBE VIDEO LINKS
1. Natural lighting condition - https://youtu.be/D7j35VGOZNU
2. Dim lighting condition - https://youtu.be/EwzMtGJTnDY
3. Pitch black with flash - https://youtu.be/djNIjovsWNY
4. Well lit condition - https://youtu.be/qUnEvgLRCb0
5. Yellow background - https://youtu.be/UsxWMImcBcg
