# 1. Install a package

package { 'Werkzeug':
  ensure   => '2.1.1',
  name     => 'Werkzeug',
  provider => 'pip3'
}

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
  require  => Package['Werkzeug']
}
