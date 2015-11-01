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
# USAGE on a fresh Ubuntu machine:
# 
# sudo apt-get install git
# git clone https://github.com/vhsvhs/chipseqbot
# cd chipseqbot
# sudo source aws_setup/config_master.sh --> launches this script
#

# Install PIP
sudo apt-get install python-pip

# Install and launch virtualenv
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate

# Install Python packages
sudo apt-get install libpq-dev python-dev
sudo pip install requirements/prod.txt

