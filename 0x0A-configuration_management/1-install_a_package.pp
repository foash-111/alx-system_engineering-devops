# Ensure the python3-pip package is installed
package { 'python3-pip':
  ensure => 'installed'
}

package { 'flask':
  ensure => '2.1.0'
}
