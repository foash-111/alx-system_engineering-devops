# kill a process using exec

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['usr/bin', '/bin', 'usr/sbin', '/sbin'], # pathes where the puppet will searsh for the command
  onlyif  => 'pgrep killmenow' # to ensure that the process is already running
}
