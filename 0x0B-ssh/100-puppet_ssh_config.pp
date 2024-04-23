# configuration file

file { 'config':
  ensure  => 'present',
  mode    => '0600',
  content => 'Host *\n\t IdentityFile ~/.ssh/school\n\t PasswordAuthentication no\n'
}
