ansible-playbook -i hosts -u arvelt --extra-vars '{"HOST":"production","ansible_sudo_pass":"${SUDOPASS}"}' site.yml
