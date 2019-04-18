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

## Resources
##### These are the official docs for Frameworks we'll be using:
- [Flask](http://flask.pocoo.org/docs/1.0/)
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) Flask wrapper for SQLAlchemy
  - [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html)
  - [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/latest/core/tutorial.html)
- [Flask-Security](https://pythonhosted.org/Flask-Security/) Auth package that integrates other frameworks we'll use
  - [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
  - [passlib](https://passlib.readthedocs.io/en/stable/) Password hashing
  - [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) Form validation
- [Jinja](http://jinja.pocoo.org/docs/2.10/) HTML templating
- More to come...
