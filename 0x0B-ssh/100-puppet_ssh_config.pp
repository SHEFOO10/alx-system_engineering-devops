# 4. Client configuration file (w/ Puppet)

# configured to use the private key ~/.ssh/school
file_line { 'configure_indentity':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IndentityFile ~/.ssh/school',
  match  => '^#?IndentityFile',
}

# disable passowrd authentication
file_line { 'disable_password_auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}
