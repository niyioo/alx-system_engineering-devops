# Description: Fix the issue of a high number of opened files

# Task: Increase the file limits for the holberton user in /etc/security/limits.conf
exec {'increase-file-limits':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['second-file-limit'],
}

# Task: Update the file limits for the holberton user in /etc/security/limits.conf
exec {'second-file-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
