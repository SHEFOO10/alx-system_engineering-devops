# 4. Client configuration file (w/ Puppet)


# Disable PasswordAuthentication in sshd_config
file_line { 'disable_password_auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

# SSH client configuration must be configured to use the
# private key ~/.ssh/school
file_line { 'use_school_private_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
