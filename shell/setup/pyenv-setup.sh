#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Please provide a version of Python to install..."
fi

VER="${1}"

echo 'Installing pyenv...'

curl https://pyenv.run | bash > /dev/null

echo '
Installation finished. 

Adding pyenv to system path via the following zshell profile additions:
'

echo '
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.pyenv/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
' | sudo tee -a ~/.zshrc

~/.pyenv/bin/pyenv install $VER

~/.pyenv/bin/pyenv global $VER

~/.pyenv/shims/pip install --upgrade pip

echo 'Installing PyPi dependencies. Standby...'

# pip dependencies
~/.pyenv/shims/pip install wheel \
pgi \
pyopenssl \
pygobject \
asyncio \
bz2file \
flatbuffers \
dbus-python \
adafruit-circuitpython-ble \
adafruit-circuitpython-neopixel