# configure server private key

file_line { 'SSH_Private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
}


file_line { 'Deny_Password_Auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^[#]+[\s]*PasswordAuthentication[\s]+(yes|no)$',
}
