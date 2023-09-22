# Puppet manifest to kill a process named 'killmenow'

exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => ['/usr/bin', '/bin'],
  refreshonly => true,
}
