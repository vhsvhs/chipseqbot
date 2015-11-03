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
#
# USAGE on a fresh Ubuntu machine (first read REQUIREMENTS):
#
# sudo apt-get install git
# git clone https://github.com/vhsvhs/chipseqbot
# cd chipseqbot
# source aws_setup/config_master.sh --> launches this script
#

# Update apt-get
sudo apt-get -y update
#sudo apt-get -y install python-django

# Install PIP
sudo apt-get -y install python-pip

# Install and launch virtualenv
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate

# Install Python packages
#sudo pip install django
sudo apt-get -y install libpq-dev python-dev
sudo pip install -r requirements/prod.txt

# Install Django
sudo apt-get -y install python-django

# Install Nginx
sudo apt-get -y install nginx

# Setup the Nginx configuration file
#sudo mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
#sudo cp aws_setup/nginx.conf /etc/nginx/nginx.conf
#sudo cp aws_setup/chipseqbot.conf /etc/nginx/conf.d/chipseqbot.conf

# Launch Nginx
sudo /etc/init.d/nginx start

# Launch Gunicorn
#cd chipseqbot
#gunicorn -w 4 config.wsgi

