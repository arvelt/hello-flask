vars="{
    \"APP_USER\":\"$USER_NAME\",
    \"HOST\":\"production\",
    \"ansible_sudo_pass\":\"$SUDOPASS\"
}"
ansible-playbook -i hosts -u "${USER_NAME}" --extra-vars "${vars}" site.yml
