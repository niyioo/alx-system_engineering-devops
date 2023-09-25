# Puppet manifest to configure SSH client

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# SSH client configuration\n\
  Host *\n\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no\n",
}
