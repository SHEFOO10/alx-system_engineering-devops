# configure server private key


# disable passowrd authentication

file_line { 'Deny_Password_Auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

# sets indentity key
file_line { 'ssh_private_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IndentityFile ~/.ssh/school',
  match  => '^#?IndentityFile',
}
