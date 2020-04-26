#!/usr/bin/env bash
# setup web_static

exec { 'web_static':
command  => 'sudo apt-get update && sudo apt-get install -y nginx && sudo mkdir -p /data/ && 
sudo mkdir -p /data/web_static/ && sudo mkdir -p /data/web_static/releases/ &&
sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && 
sudo touch /data/web_static/releases/test/index.html && echo "HOLBERTON SCHOOL!" | sudo tee /data/web_static/releases/test/index.html && 
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current &&
sudo chown -R ubuntu:ubuntu /data/ &&
sudo sed -i "37 i a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default && 
sudo service nginx restart',
provider => shell,
}
