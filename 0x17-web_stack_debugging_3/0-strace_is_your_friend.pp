# Fixes error 500 on apache.

exec { '/var/www/html/wp-settings.php':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin/',
}
