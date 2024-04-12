#Using strace  and then using Puppet to automate fix for 500 error on Apache

exec { 'sed -i "s/.phpp/.php/" wp-settings.php':
  cwd  => '/var/www/html',
  path => ['/usr/bin', '/usr/sbin', '/bin',]
}
