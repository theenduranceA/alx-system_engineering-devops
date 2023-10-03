# Automating the task of creating a custom HTTP header respons

exec { 'update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => present,
  require => Exec['update']
}

file_line { 'add header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By "$HOSTNAME";',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
