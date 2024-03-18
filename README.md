# NMapLearning

This repository will store the files that I use in the process of learning NMap.

To view all details about Nmap,tap in https://nmap.org/.

Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. It was designed to rapidly scan large networks, but works fine against single hosts.

In addition to the classic command-line Nmap executable, the Nmap suite includes an advanced GUI and results viewer (Zenmap), a flexible data transfer, redirection, and debugging tool (Ncat), a utility for comparing scan results (Ndiff), and a packet generation and response analysis tool (Nping).

## Downloading and Installing
RPM-based Distributions and Debian Linux and Derivatives have different ways to install.
Environment: Ubuntu 20.04.3 LTS system
Downloading, converting, and installing the `nmap` RPM package on Ubuntu are as follows:
### Download and Convert RPM Package to DEB
1. **Download the RPM Package**: The user successfully downloads the RPM package using `wget` with sudo permissions to overcome the permission denied issue.
   ```sh
   sudo wget https://nmap.org/dist-old/nmap-5.21-1.x86_64.rpm
   ```

2. **Convert the RPM Package to DEB**: After installing `alien`, a tool for converting RPM packages to DEB, the user converts the downloaded RPM package to a DEB package.
   ```sh
   sudo alien -k nmap-5.21-1.x86_64.rpm
   ```

### Install the DEB Package
1. **Install the Converted DEB Package**: The user installs the converted DEB package using `dpkg`, Ubuntu's package management command. Initially, there's an attempt to install a non-existent version, but eventually, the correct command is used for the existing package.
   ```sh
   sudo dpkg --install nmap_5.21-1_amd64.deb
   ```

This sequence of commands accurately represents how to handle an RPM package on a Debian-based system like Ubuntu, involving downloading the package, converting it from RPM to DEB format, and finally installing the DEB package.
