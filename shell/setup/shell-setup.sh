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

source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export EDITOR=/usr/bin/nano
export VISUAL=/usr/bin/nano

alias zc="sudo nano ~/.zshrc"
alias zs="source ~/.zshrc"

# ZSH default text editor
export EDITOR=/usr/bin/nano
export VISUAL=/usr/bin/nano
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