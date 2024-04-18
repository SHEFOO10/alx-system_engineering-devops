# set new soft & hard limit for holberton user

exec { 'increase soft limit':
  command => 'sed -i -E "/erton (hard|soft) nofile/s/[0-9]+/512/" limits.conf',
  cwd     => '/etc/security/',
  path    => '/bin/'
}
