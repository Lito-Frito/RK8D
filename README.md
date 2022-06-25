# RK8D - A retro, containerized gaming experience

![image](https://user-images.githubusercontent.com/56422761/172072005-6aa99131-0e7b-4d78-a3af-68e92b561b4f.png)

This is going to be a small project where I will recreate a few arcade games using Python. I'll then bundle the games and containerize them as a single image so people will have a centralized image for all the games. This will ensure that anyone who can run Docker will be able to play my arcade games. I'll add more games in the future.


## What This Includes
`pong.py`: This is a python version of the game pong. It's a very bare-bones version of the game. I'll be adding new features to the game first and then containerizing it.


# Getting Started

## Requirements
You'll need one of the following
* Python 
* Docker


## Quick Start
If you have Docker, you can go to [Docker Hub](https://hub.docker.com/repository/docker/crc8109/rk8d) to see where I'm hosting the image for RK8D as it is now. It only includes the game pong for now.

First, just pull the image by running the command `docker pull crc8109/rk8d:latest`. Once you pull the image, run the following command in your terminal:

`docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --rm -it crc8109/rk8d:latest`. 

This command is a little crazy because this game needs to access your screen to run properly. So to give Docker proper access, all these extra parameters are needed so that Docker can properly run the game. 


## Starting from Scratch
Clone the repo. Then run `python3 main.py`. That will start the only game made so far.