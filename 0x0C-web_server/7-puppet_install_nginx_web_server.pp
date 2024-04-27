# Puppet manifest containing commands to automatically configure an Ubuntu machine

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create index.html with "Hello World!" content
file {'/var/www/html/index.html':
  ensure  => file,
  content => '<h1>Hello World!</h1>',
}

# Define Nginx server configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
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

  location / {
    return 200 /index.html;
  }
}
",
}

# Ensure the symbolic link is created for Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service after configuration changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
