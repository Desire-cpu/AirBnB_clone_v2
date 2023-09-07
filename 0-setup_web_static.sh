#!/usr/bin/env bash
# Sets up the web servers.

# Install Nginx.
apt update -y >/dev/null 2>&1
apt install nginx -y >/dev/null 2>&1

# Ceates directories 
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# create index.html file
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >/data/web_static/releases/test/index.html
# Create symbolic link
ln -sf /data/web_static/releases/test /data/web_static/current
# Change ownership of files and folders inside of /data folder
chown -hR ubuntu:ubuntu /data
# Add alias to serve the content of /data/web_static/current to hbnb_static
sed -i '51i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# Restart nginx
service nginx restart
