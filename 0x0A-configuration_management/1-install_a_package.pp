# install flask
package { 'flask':
# You can specify 'present' or 'latest' to ensure it's installed or up-to-date
ensure   => '2.1.0',
provider => 'pip3' # Use pip3 as the package provider.
}
