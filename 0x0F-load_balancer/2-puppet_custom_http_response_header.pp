# Install nginx and add_header directive for servers in /sites-enabled/default

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

service { 'nginx':
  ensure => running,
  name   => 'nginx',
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;
    add_header X-Served-By \"${hostname}\";

    location /redirect_me {
        return 301 https://www.youtube.com;
    }

    error_page 404 /error_page.html;
}
",
}

exec { 'reload nginx':
  path    => ['/usr/sbin', '/usr/bin', '/bin'],
  command => 'sudo service nginx reload'
}
