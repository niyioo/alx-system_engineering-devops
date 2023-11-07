# Puppet manifest to fix Apache 500 error by modifying the wp-settings.php file

exec { 'fix-apache-500-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}