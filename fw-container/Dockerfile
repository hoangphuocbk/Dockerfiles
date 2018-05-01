# Pull base image
FROM ubuntu

# Author 
MAINTAINER <hoangphuocbk2.07@gmail.com>

# Install necessary tools
RUN apt-get update && apt-get install -y bridge-utils net-tools iptables ufw

# Define default command
CMD ["tcpdump", "-i", "eth0"]

