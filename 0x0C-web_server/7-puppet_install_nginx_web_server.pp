# Puppet manifest containing commands to automatically configure an Ubuntu machine 

package { 'nginx':
  ensure => installed,
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => '<h1>Hello World!</h1>'
}

file { '/etc/nginx/sites-available/default':
  ensure  => file
  content => "
  server {
    listen 80 default_server;
    listen [::]:80 default server;
    root /var/www/html;
    index index.html;
    server_name foash.tech;
    location /redirect_me {
      return 301 https://www.youtube.com/;
    }
    "
}

file { '/etc/nginx/sites-enabled/default'
  ensure  => link,
  require => FILE['/etc/nginx/sites-available/default']
  target  => '/etc/nginx/sites-available/default'

  }

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default']
}
