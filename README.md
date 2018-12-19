# TOC Project 2019

Template Code for TOC Project 2019

A Facebook messenger bot based on a finite state machine
///give me something !!!

## Setup

### Prerequisite
* Python 3
* Facebook Page and App
* HTTPS Server
* Beautifulsoup

####  Hoe to Run 
open two terminal
```sh
./ngrok http 5000 	#Run Locally
```
```sh
python3 app.py      #Run the sever
```


## Finite State Machine
![fsm](./img/fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"


## Reference
[TOC-Project-2017](https://github.com/Lee-W/TOC-Project-2017) ❤️ [@Lee-W](https://github.com/Lee-W)
