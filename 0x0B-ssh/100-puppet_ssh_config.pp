# configuration file

file { 'config':
  ensure  => 'present',
  mode    => '0600',
  path    => '~/.ssh/school'
  content => 'Host *\n\t IdentityFile ~/.ssh/school\n\t PasswordAuthentication no'
}
