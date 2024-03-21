#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Please provide a version of Python to install..."
fi

echo 'Installing pyenv...'

curl https://pyenv.run | bash

echo '
Done.
'

pyenv install 3.10.5

pyenv global 3.10.5

pip_dir=`which pip`

${pip_dir} install --upgrade pip

echo 'Installing PyPi dependencies. Standby...'

# pip dependencies
${pip_dir} install wheel \
pgi \
pyopenssl \
pygobject \
asyncio \
bz2file \
flatbuffers \
dbus-python \
adafruit-circuitpython-ble \
adafruit-circuitpython-neopixel