# Install nginx and add_header directive for servers in /sites-enabled/default

package { 'nginx':
  ensure   => installed,
  name     => 'nginx'
  provider => 'apt',
}

service { 'nginx':
  ensure  => running,
  name    => 'nginx',
  restart => ''
}

file { 'default':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default'
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
