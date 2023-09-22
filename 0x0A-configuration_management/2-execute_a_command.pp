# Puppet manifest to kill a process named killmenow

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin/:/usr/local/bin/:/bin/',
  refreshonly => true,
}
