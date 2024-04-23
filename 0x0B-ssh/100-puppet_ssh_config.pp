# configuration file

file { 'ssh_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => 'Host *\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n'
}
