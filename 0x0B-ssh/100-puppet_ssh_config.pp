# configuration file

file { 'config':
  ensure  => 'present',
  content => 'Host *\n\t IdentityFile ~/.ssh/school\n\t PasswordAuthentication no\n'
}
