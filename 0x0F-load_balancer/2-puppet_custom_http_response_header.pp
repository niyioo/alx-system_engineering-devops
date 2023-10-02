# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom Nginx configuration file to add the custom header
file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => present,
  content => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/conf.d/custom-header.conf'],
}

