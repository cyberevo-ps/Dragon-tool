import subprocess

def install_packages(*package_names):

    for package_name in package_names:

        try:

            # Check if package is installed

            subprocess.run(['pip', 'show', package_name], check=True)

            print(package_name + ' \033[1;31m is already installed\033[0m')

        except subprocess.CalledProcessError:

            # If package is not installed, install it

            subprocess.check_call(['pip', 'install', package_name])

            print(package_name + ' has been installed')

# List of packages to install

packages = ['requests', 'pyshorteners', 'instaloader', 'colorama' ]

# Install packages

install_packages(*packages)
