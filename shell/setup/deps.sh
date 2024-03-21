#!/bin/bash

echo 'Setting firmware release status to:'

echo 'FIRMWARE_RELEASE_STATUS="stable"' | sudo tee /etc/default/rpi-eeprom-update

echo '
Installing development/runtime dependencies. Stand by...
'

# Elly dev dependencies
sudo apt -y install zsh \
zsh-syntax-highlighting \
openjdk-17-jdk \
openjdk-17-jdk-headless \
git \
build-essential \
python3-dev \
python3-pip \
python3-gi \
docutils-common \
llvm \
libncurses5-dev \
libncursesw5-dev \
libglib2.0-dev \
libssl-dev \
libsqlite3-dev \
zlib1g-dev \
libglib2.0-cil-dev \
libdbus-glib2.0-cil-dev \
libdbus-glib-1-dev \
libudev-dev \
libical-dev \
libreadline-dev \
python3-gi-cairo \
python3-cairo-dev \
libgirepository1.0-dev \
libcairo2-dev \
libatlas-base-dev \
libbz2-dev \
gfortran \
xz-utils \
tk-dev \
libffi-dev \
liblzma-dev \
python3-openssl \
wget \
xrdp \
xserver-xorg-input-evdev \
curl

echo '
Success!
'