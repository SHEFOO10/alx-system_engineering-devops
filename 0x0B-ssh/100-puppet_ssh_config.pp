# configure server private key

include stdlib

file_line { 'SSH Private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IndentityFile ~/.ssh/school',
  match  => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
}


file_line { 'Deny Password Auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^[#]+[\s]*PasswordAuthentication[\s]+(yes|no)$',
}
