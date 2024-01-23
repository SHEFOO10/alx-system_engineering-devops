# configure server private key

file_line { 'SSH_Private_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IndentityFile ~/.ssh/school',
  match  => '^#?IndentityFile',
}


file_line { 'Deny_Password_Auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}
