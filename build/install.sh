echo Installing packages...
sudo apt-get install -y python3.7

sudo pip3 install urllib3 \
    ipinfo \
    google-api-python-client \
    google-auth-oauthlib \
    python-dateutil

# CLoning from github
echo Cloning Code
git clone https://github.com/ICTM1l1/smart-calendar.git

# Renaming file
echo renaming file
mv smart-calendar/example-private.json smart-calendar/private.json

# Setting up service
echo Setting up service
sudo mv smart-calendar/build/smart-calendar.service /lib/systemd/system/smart-calendar.service

sudo chmod 644 /lib/systemd/system/smart-calendar.service
sudo systemctl daemon-reload
sudo systemctl enable smart-calendar.service

echo "==========================="
echo "      Setup Complete!      "
echo "==========================="

echo "Restarting Raspberry, this will shutdown the system and reboot."
read -p "Press any key to continue "
sudo reboot