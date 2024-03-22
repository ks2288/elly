echo '
Modifying XRDP startup script...
'

echo '
unset DBUS_SESSION_BUS_ADDRESS
unset XDG_RUNTIME_DIR
' | sudo tee -a /etc/xrdp/startwm.sh

sudo systemctl enable xrdp

echo 'Success!'