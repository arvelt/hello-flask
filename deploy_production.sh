expect -c "
spawn ansible-playbook -i hosts -u ${USER_NAME} --extra-vars '{"HOST":"production"' site.yml -K
expect SUDO password:
send -- ${SUDOPASS}
"
