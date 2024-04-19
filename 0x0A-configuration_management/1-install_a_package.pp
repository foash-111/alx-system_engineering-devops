# install flask
package { 'flask':
# You can specify 'present' or 'latest' to ensure it's installed or up-to-date
ensure   => 'installed',
provider => 'pip3' # Use pip3 as the package provider.
}
