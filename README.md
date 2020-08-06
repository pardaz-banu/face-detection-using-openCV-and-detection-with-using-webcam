# face-detection-using-openCV-and-detection-with-using-webcam

Identifying face in an image or video by our system is an interesting thing.
Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.

--> The detection works only on grayscale images. So it is important to convert the color image to grayscale.

--> detectMultiScale function  is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours. scaleFactor specifies how much the image size is reduced with each scale. minNeighbours specifies how many neighbors each candidate rectangle should have to retain it. 

--> faces contains a list of coordinates for the rectangular regions where faces were found. We use these coordinates to draw the rectangles in our image.
