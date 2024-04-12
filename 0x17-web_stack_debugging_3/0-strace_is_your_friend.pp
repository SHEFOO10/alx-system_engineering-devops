exec { 'sed -i "s/.phpp/.php/" wp-settings.php':
  cwd  => '/var/www/html',
  path => ['/usr/bin', '/usr/sbin', '/bin',]
}
