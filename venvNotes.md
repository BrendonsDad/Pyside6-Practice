# Virtual Enviornments
Making a virtual enviornment in python settings is very useful. It lets us intall specific packages to that folder and then run python scripts with that set of packages. For example, in this folder we have made a virtual enviornment, and used pip to install PySide6. I will show below how to set up a vitual enviornment

## To make a new vitrual enviornment
* python -m venv venv
    * this saves a venv folder to the current folder

## To Get into it 
* sourse venv /bin/activate

## To get out
* deactivate

## Usefulness

We can now use and install python packages in our enviornment

But first we need to set this enviornment location as our interpreter. On visual studio code,
* ctrl+shft+p 
    * select interpreter (select one in ./venv)
    * restart language interpreter ( this )


Also random but to access maya through pipe:
* cd groups/skygarud/pipeine
* python pipline maya (or houdini or whatever)


## Adding venv directory to gitignore
This is simple but nessisary. Simply create a .gitignore file, and then type venv in it. 