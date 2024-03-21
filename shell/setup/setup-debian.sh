#!/bin/bash
set -e pipefail

if [ "$#" -ne 4 ]; then
    echo "Please provide both a Python and a BlueZ version using the -p and -b flags respectively, each followed individually by a version string."
fi

BLUEZ_VERSION=''
PY_VERSION=''

eval set -- "$TEMP"
while true ; do
    case "$1" in
        -b )
            BLUEZ_VERSION=$2
            shift 2
        ;;
        -p )
            PY_VERSION=$2
            shift 2
        ;;
        *)
            break
        ;;
    esac 
done;

read -p "This script will install Elly development dependencies for Debian. Proceed? (y/n)? " answer
case ${answer:0:1} in
y|Y )
echo "


**********************************************************
*                                                        *
*                  Viper setup initiated                 *
*                                                        *
**********************************************************


"

echo '
Updating Aptitude core/packages. Standby...
'

# pre-script system updates
sudo apt update && sudo apt dist-upgrade -y > /dev/null

echo "


**********************************************************
*                                                        *
*               Aptitude update completed                *
*                                                        *
**********************************************************


"

echo 'Installing SDKs/runtime dependencies. Standby...'

. ./deps.sh

echo "


**********************************************************
*                                                        *
*              SDK dependencies installed                *
*                                                        *
**********************************************************


"

. ./ vsc-install.sh

echo "


**********************************************************
*                                                        *
*                   VSCodium installed                   *
*                                                        *
**********************************************************


"

. ./zsh-setup.sh

. ./xrdp-setup.sh


echo "


**********************************************************
*                                                        *
*                     Shell configured                   *
*                                                        *
**********************************************************


"

. ./pyenv-seup.sh ${PY_VERSION}

echo "


**********************************************************
*                                                        *
*                    Python configured                   *
*                                                        *
**********************************************************


"

. ./bluez-upgrade.sh ${BLUEZ_VERSION}

echo "

**********************************************************
*                                                        *
*                   BlueZ stack updated                  *
*                                                        *
**********************************************************


"

echo "


**********************************************************
*                                                        *
*          Setup process completed successfully.         *
*                                                        *
**********************************************************


* Have a nice day, friend!
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████

"


exec /bin/zsh
;;
* )
echo 'Exiting without installing...'
;;
esac
