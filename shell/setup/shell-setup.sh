#!/bin/bash
set -e

echo 'Configuring shell profile...'

echo "
Adding the following alias definitions to new zshell profile:

"

echo '
setopt NO_CASE_GLOB
setopt AUTO_CD
setopt EXTENDED_HISTORY
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_DUPS
setopt HIST_REDUCE_BLANKS
setopt CORRECT
autoload -Uz compinit
compinit
autoload -Uz promptinit
promptinit
prompt clint
autoload -Uz vcs_info
precmd() { vcs_info }

source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export EDITOR=/usr/bin/nano
export VISUAL=/usr/bin/nano

alias zc="sudo nano ~/.zshrc"
alias zs="source ~/.zshrc"

# ZSH default text editor
export EDITOR=/usr/bin/nano
export VISUAL=/usr/bin/nano

alias ellyscan="python ~/elly/core/connection_utils.py scan"
alias ellyconnect="python ~/elly/core/connect_discover.py"
alias ellypair="python ~/elly/core/connection_utils.py pair"
alias ellyrefresh="bash ~/elly/shell/refresh-ble.sh"
alias ellydisconnect="bash ~/elly/shell/ble-disconnect.sh"
alias ellynotify="python ~/elly/core/util/notification_engine.py"
alias ellywrite="python ~/elly/core/util/gatt_engine.py write"

' | sudo tee ~/.zshrc

sudo chsh -s /bin/zsh $USER

echo "Adding $USER to Bluetooth group..."

sudo usermod -aG bluetooth $USER

# SSH keygen prompt

read -p "Generate new SSH key? (y/n)? " answer
case ${answer:0:1} in
y|Y )
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -q -P ""
echo "Appending SSH config file with:

"
echo 'IdentityFile ~/.ssh/id_ed25519' | sudo tee -a /etc/ssh/ssh_config

;;
* )
echo 'Skipping SSH keygen...'
;;
esac