#!/bin/bash

if [ $# -eq 0 ]
then 
    echo "Please provide a BlueZ version number"
else

if [[ `bluetoothctl -v` == *$BLUEZ_VERSION ]]; then
echo 'BlueZ already at given version'
else
echo 'Updating BlueZ to version $BLUEZ_VERSION...'
rm -rf bluez-$1
rm bluez-$1.tar.xz
sudo apt update && sudo apt upgrade -y
sudo apt install libglib2.0-dev libdbus-glib-1-dev libdbus-glib2.0-cil-dev libdbus-glib-1-dev libudev-dev libical-dev libreadline-dev -y
wget www.kernel.org/pub/linux/bluetooth/bluez-$1.tar.xz
tar -xvf bluez-$1.tar.xz && cd bluez-$1
./configure --prefix=/usr --mandir=/usr/share/man --sysconfdir=/etc --localstatedir=/var
make -j4
sudo make install
rm -rf bluez-$1
rm bluez-$1.tar.xz
sudo reboot

fi
fi