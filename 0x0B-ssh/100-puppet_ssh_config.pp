# configure server private key

include stdlib

file_line { 'SSH Private key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IndentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}


file_line { 'Disable Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}
