# Configuring an nginx server on ubuntu 16.04 using puppet.

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.theenduranceaneke.tech permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
