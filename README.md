Project Name: watch_next

This is an appn that returns the title of a movie that the user is most likely to watch next, based on previous watched movies description.

Table of Contents:

-Installation
-Usage
-Author


Installation:
    
    Local installation:
    Make sure you have python installed.
    Open your terminal and change directory to where you want to install it and run the following commands:

    -git clone git@github.com:RichardFriedrichsen/watch_next.git
    -pip3 install spacy
    -python -m spacy download en_core_web_md


    Docker:
    By running the below docker command the requirements in the requirements.txt automatically get installed.

Usuage:

    Running Locally:
    Change directory into installation folder and run:

    - python watch_next.py 
    
    Docker:
    Run the following commands in the terminal

    - docker run richardfriedrichsen/watch_next_app

Author:
Richard Friedrichsen
    