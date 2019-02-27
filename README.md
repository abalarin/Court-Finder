# Court-Finder

#### The basic necessities to run it

## Install [Python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/installing/), and [Virtualenv](https://virtualenv.pypa.io/en/latest/)
###### Once they're downloaded verify installation:
```
python --version
Python 2.7.10

pip --version
pip 19.0.3 from /Library/Python/2.7/site-packages/pip (python 2.7)

virtualenv --version
16.2.0
```
## Get Shit Started
```
# Clone and cd into this repo
git clone https://github.com/abalarin/Court-Finder.git
cd Court-Finder

# Create and activate the Virtualenv
virtualenv venv
source venv/bin/activate

# Install all dependencies
pip install -e .

# Lets flask know where the app starts, the "CourtFinder" dir
export FLASK_APP=CourtFinder

# Puts flask into dev mode
# so auto reload flask on file change & nice Traceback/stacktrace
export FLASK_ENV=development

# Run it
flask run
```

## Set up SQL...
