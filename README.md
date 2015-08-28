Bountyboard
===========

This is a web service that allows users to share ideas for new or existing projects and vote to support the completion of those ideas.

## How to develop on Bountyboard

The follow are the tools required for running the Bountyboard
* Python Utilities
  * pip 
  * virtualenv
  * virtualenvwrapper
* Heroku/Foreman

### Setup
Run the following:

```bash
# Install pip
sudo easy_install pip

# Install virtualenv and virtualenvwrapper
pip install virtualenv
pip install virtualenvwrapper 

# Create a folder to store your virtualenvs
mkdir ~/.virtualenvs

```

Also, add the following to your .bashrc:

```bash
# Python Virtual Environment Settings
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Finally run:

```bash
# Create the bountyboard virtual environment
source ~/.bashrc
mkvirtualenv bountyboard
workon bountyboard

# Install the Python Requirements
pip install -r requirements.txt

# Install foreman
gem install foreman
```

### How to start the bountyboard

In order to run the bountyboard, run the following:

```bash
# Start the database (only run once)
python db_create.py

# Run the bountyboard
foreman start
```

### Developing tips

When an error occurs in the browser, each line in that stack trace can be interacted with as an interactive python shell.