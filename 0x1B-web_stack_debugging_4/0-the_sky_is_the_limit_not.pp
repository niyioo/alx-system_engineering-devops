# Description: Enhances Nginx server capacity to handle increased traffic.

# Task 0: Increase the ULIMIT of the default file to optimize server performance.
exec { 'fix--ulimit-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# Task 1: Restart Nginx to apply the changes made for improved performance.
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
