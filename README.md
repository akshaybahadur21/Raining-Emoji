# Raining Emoji 🌧️ 🐶 🐵 🦁 🐷 🐨

[![](https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg?colorB=ff0000)](https://github.com/akshaybahadur21/Emojinator/blob/master/LICENSE.md)  [![](https://img.shields.io/badge/Akshay-Bahadur-brightgreen.svg?colorB=ff0000)](https://akshaybahadur.com)

What can be better than your favourite emojis raining?

## Code Requirements 🦄
You can install Conda for python which resolves all the dependencies for machine learning.

`pip install -r requirements.txt`

## Description 👨‍🎨
Quick, Draw! is an online game developed by Google that challenges players to draw a picture of an object or idea and then uses a neural network artificial intelligence to guess what the drawings represent. The AI learns from each drawing, increasing its ability to guess correctly in the future.The game is similar to Pictionary in that the player only has a limited time to draw (20 seconds).The concepts that it guesses can be simple, like 'foot', or more complicated, like 'animal migration'. This game is one of many simple games created by Google that are AI based as part of a project known as 'A.I. Experiments'. [Quick, Draw](https://quickdraw.withgoogle.com/)

## Emojis used
1) Apple :apple:
2) Bowtie 🎀	
3) Candle 🕯️
4) Door :door:
5) Envelope :envelope:
6) Fish :fish:
6) Guitar :guitar:
7) Ice Cream :icecream:
8) Lightning ⚡
9) Moon :first_quarter_moon_with_face:
10) Mountain :mount_fuji:
11) Star :star:
12) Tent :tent:
13) Toothbrush 🧹
14) Wristwatch :watch:

## Python  Implementation 👨‍🔬

1) Network Used- Convolutional Neural Network

If you face any problem, kindly raise an issue

## Setup 🖥️

1) Get the dataset as mentioned above and place the `.npy` files in `/data` folder.
2) First, run `LoadData.py` which will load the data from the `/data` folder and store the features and labels in  pickel files.
3) Now you need to have the data, run `QD_trainer.py` which will load data from pickle and augment it. After this, the training process begins.
2) Now you need to have the data, run `QuickDrawApp.py` which will use use the webcam to get what you have drawn.
3) For altering the model, check `QD_trainer.py`.
4) For tensorboard visualization, go to the specific log directory and run this command ` tensorboard --logdir=.` You can go to `localhost:6006` for visualizing your loss function and accuracy.


## Execution 🐉

```
python3 RainingEmoji.py
```

## Results 📊
<img src="https://github.com/akshaybahadur21/QuickDraw/blob/master/qd.gif">

## References: 🔱
 
 - [Amirabbas Asadi's toy project](https://github.com/amirabbasasadi/toy-project-cv-physics-engine)






