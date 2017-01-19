# Pull base image
FROM ubuntu:14.04

# Author 
MAINTAINER <hoangphuocbk2.07@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary tools
RUN \
	apt-get update && \ 
	apt-get -y install software-properties-common

# Install Java 8
RUN \
	echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list && \
	echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main " >> /etc/apt/sources.list && \
	apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys EEA14886 && \
	apt-get update && \ 
	echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
	apt-get install -y oracle-java8-installer && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer

# Define working directory
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Define default command
CMD ["bash"]
