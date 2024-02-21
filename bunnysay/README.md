# bunnysay


This project was inspired by whalesay by Docker, which is an image adaptation of the classic Linux cowsay. I wanted to recreate it in Python with the purpose of learning Python and Docker.


## Installation

Clone this project to your local repository

    git clone https://github.com/dcpamir/bunnysay.git
    cd bunnysay

Run the python script

    python3 bunnysay.py --emote=happy Hello!

You can use --emote to try the different available emotes 

 - bored
 - happy
 - mad
 - shock
 - cry
 - sad
 - greedy
 
Or you can create an image from the dockerfile

    docker build -t <imagename> .

Then run the image in a container. For example

    docker run --rm <imagename> --emote=sad I am sorry

Additional Resource: 
[Download and Install Docker](https://docs.docker.com/get-docker/)
