# configuration file

file { 'config':
  ensure  => 'present',
  mode    => '0600',
  path    => '/etc/ssh/ssh_config'
  content => 'Host *\n\t IdentityFile ~/.ssh/school\n\t PasswordAuthentication no'
}
