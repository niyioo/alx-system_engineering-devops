# Define an Nginx class
class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
    ensure  => file,
  }

  file { '/etc/nginx/sites-available/redirect_me':
    content => template('nginx/redirect_me.erb'),
  }

  file { '/etc/nginx/sites-enabled/redirect_me':
    ensure => link,
    target => '/etc/nginx/sites-available/redirect_me',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => File['/etc/nginx/sites-enabled/redirect_me'],
  }
}

# Include the Nginx class
include nginx

