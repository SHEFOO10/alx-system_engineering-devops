# Modify the ulimit in the nginx file
exec { 'replace increase ulimit from 15 to 1024':
  command   => 'sed -i -E \'s/ULIMIT=".*"/ULIMIT="-n 1024"/\' /etc/default/nginx',
  path      => ['/bin/'],
  onlyif    => 'grep -q "^ULIMIT=\".*\"$" /etc/default/nginx', # Ensures the change only happens if needed
  notify    => Exec['nginx_restart'], # Notify the restart exec when the sed command completes
}

# Restart Nginx service
exec { 'nginx_restart':
  command     => '/etc/init.d/nginx restart',
  path        => ['/sbin/', '/usr/sbin/', '/bin/', '/usr/bin/'],
  refreshonly => true,  # This ensures the exec only runs when explicitly notified
}
