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

# Install and launch virtualenv
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate

# Install Python packages
sudo pip install django
sudo apt-get -y install libpq-dev python-dev
sudo pip install -r requirements/prod.txt

# Install Nginx
# (In Ubuntu, nginx will auto start upon installation)
sudo apt-get -y install nginx

# Setup the Nginx configuration files
sudo mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
sudo cp aws_setup/nginx.conf /etc/nginx/nginx.conf

# Launch Nginx with the new configuration.
# Because nginx is launched upong installation (in previous steps), 
# we need to restart nginx to ensure that correct configurations
# are loaded.
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx reload
sudo /etc/init.d/nginx start

# Launch Gunicorn
cd chipseqbot # change directories to the location where manage.py lives
gunicorn -w 4 config.wsgi

