# Puppet manifest to kill a process named "killmenow"

exec { 'kill_killmenow':
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
  subscribe   => Exec['start_my_process'],
  path        => '/usr/bin:/bin',
}

exec { 'start_my_process':
  command => 'your_start_command_here',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/bin',
}
