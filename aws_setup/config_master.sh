#
# config_master.sh
#
# This script can be launched on a fresh Ubuntu instance. It will
# setup Nginx, Gunicorn, Django, and all Python libraries
# necessary to run the chipseqbot program. After running this script,
# the instance will be hosting chipseqbot at <IP address>.
#
# REQUIREMENTS:
# This script retrieves secret keys from environmental variables.
# Contact your system admin. to retrieve the appropriate keys.
#
# USAGE on a fresh Ubuntu machine (first read REQUIREMENTS):
#
# sudo apt-get -y install git
# git clone https://github.com/vhsvhs/chipseqbot
# cd chipseqbot
# source aws_setup/config_master.sh --> launches this script
#

# Update apt-get
sudo apt-get -y update

# Install PIP
sudo apt-get -y install python-pip

# (depricated)
# Install and launch virtualenv
#sudo pip install virtualenv
#virtualenv venv
#source venv/bin/activate

#
# Install PostgreSQL
#
sudo apt-get -y install postgresql postgresql-contrib libpq-dev

sudo -u postgres psql -c "CREATE DATABASE csbotdb"

sudo -u postgres psql --dbname=csbotdb -c "CREATE USER django WITH PASSWORD 'csbotpass'"
sudo -u postgres psql --dbname=csbotdb -c "ALTER ROLE django SET timezone TO 'UTC-8'"
sudo -u postgres psql --dbname=csbotdb -c "ALTER USER django CREATEDB"

sudo -u postgres psql --dbname=csbotdb -c "GRANT ALL PRIVILEGES ON DATABASE csbotdb TO django"
sudo -u postgres psql --dbname=csbotdb -c "ALTER USER CREATEDB"

#
# Install Python packages
#
sudo apt-get -y install python-dev
sudo pip install -r requirements/prod.txt

#
# Install Nginx
# (In Ubuntu, nginx will auto start upon installation)
#
sudo apt-get -y install nginx
sudo mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
sudo cp aws_setup/nginx.conf /etc/nginx/nginx.conf

# Launch Nginx with the new configuration.
# Because nginx is launched upong installation (in previous steps), 
# we need to restart nginx to ensure that correct configurations
# are loaded.
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx reload
sudo /etc/init.d/nginx start

#
# Setup the project database
#
cd chipseqbot # change directories to the location where manage.py lives
python manage.py createsuperuser # --> this will prompt you for a new username and password
python manage.py makemigrations csbportal
python manage.py migrate # setup the db

#
# Setup static files
#
mkdir ../assets
python manage.py collectstatic # move css, js, etc. into the appropriate assets folder

#
# Run Tests
#
python manage.py test

# Launch Gunicorn
gunicorn -w 4 config.wsgi

