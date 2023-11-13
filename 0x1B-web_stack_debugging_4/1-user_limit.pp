# Description: Change the OS configuration to resolve too many open files issue for holberton user.

# Task: Increase the user limits for holberton
exec { 'change-os-configuration-for-holberton-user':
  command => 'echo -e "\n*               soft    nofile          4096\n*               hard    nofile          4096" >> /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => 'grep -E "^\\*\\s+soft\\s+nofile" /etc/security/limits.conf',
}

# Task: Apply the new limits without requiring a system reboot
exec { 'apply-new-limits-for-holberton-user':
  command => 'ulimit -n 4096',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  user    => 'holberton',
  onlyif  => 'test "$(ulimit -n)" -ne 4096',
}
