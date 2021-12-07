#!/bin/bash

function updates{
    # Update packages
    sudo apt-get update
    sudo apt-get install python3-pip nginx git
    sudo pip install virtualenv
    sudo pip install gunicorn
    sudo pip install -r requirements.txt
}

function github {
    # Github updates
    sudo git pull https://github.com/NastyEthan/NastyAwakened.git
    # I probably need to add to this
}

function svcupdate {
	# update service
	sudo systemctl restart nasty.service
	sudo nginx -s reload
	sudo systemctl restart nginx
}

function nasty {
  cd /home/nasty/NastyAwakened/
	updates
	github
	svcupdate
}

# bangers on bangers
nasty