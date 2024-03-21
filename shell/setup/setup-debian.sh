#!/bin/bash
set -e pipefail

. ./elly/shell/setup/versions.sh

echo "


**********************************************************
*                                                        *
*                       Elly Setup                       *
*                                                        *
**********************************************************


"

read -p "This script will install Elly dependencies for Debian. Proceed? (y/n)? " answer
case ${answer:0:1} in
y|Y )
echo "


**********************************************************
*                                                        *
*                Updating Aptitude Packages              *
*                                                        *
**********************************************************


"

echo '
Updating Aptitude core/packages. Standby...
'

# pre-script system updates
sudo apt update && sudo apt dist-upgrade -y

echo "


**********************************************************
*                                                        *
*             Installing Package Dependencies            *
*                                                        *
**********************************************************


"

echo 'Installing SDKs/runtime dependencies. Standby...'

. ./elly/shell/setup/deps.sh

echo "


**********************************************************
*                                                        *
*                   Installing VSCodium                  *
*                                                        *
**********************************************************


"

. ./elly/shell/setup/vsc-install.sh

echo "


**********************************************************
*                                                        *
*              Configuring Shell Environment             *
*                                                        *
**********************************************************


"

. ./elly/shell/setup/shell-setup.sh

. ./elly/shell/setup/xrdp-setup.sh


echo "


**********************************************************
*                                                        *
*                    Configuring Python                  *
*                                                        *
**********************************************************


"

. ./elly/shell/setup/pyenv-seup.sh "${PYTHON_VERSION}"

echo "


**********************************************************
*                                                        *
*                  Upgrading BlueZ Stack                 *
*                                                        *
**********************************************************


"

. ./elly/shell/setup/bluez-upgrade.sh "${BLUEZ_VERSION}"

echo "


**********************************************************
*                                                        *
*          Setup process completed successfully.         *
*                                                        *
**********************************************************

Your system is now equipped to use Elly and its BLE functionality.
For next steps, refer to the README located in the repo's root directory.

  * Have a nice day, friend! *
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
