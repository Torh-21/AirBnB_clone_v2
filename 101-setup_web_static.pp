# This puppet script sets up your web servers for the deployment of web_static

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Define folder structure
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><body>Hello, this is a test!</body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Give ownership to ubuntu user and group
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => template('site.erb'),
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

