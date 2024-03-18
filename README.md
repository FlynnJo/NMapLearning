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


## Host Discovery(ping scan)

One of the very first steps in many network reconnaissance mission is to reduce a (sometimes huge) set of IP ranges into a list of active or interesing hosts.Scanning every port of every single IP address is slow and usually unnecessary.Of course what makes a host interesting depends greatly on the scan purposes.Network administrators may only be interested in hosts running a certain service,while security auditors may care about every single device with an IP address.An administrator may be comfortable using just ICMP ping to locate hosts on his internal network,while an external penetration tester may use a diverse set of dozens of probes in an attemp to evade firewall restrictions.

Let's illustrate how Nmap can be used for host discovery with practical examples for each key part mentioned:

### 1. Variety of Discovery Options
Using a combination of TCP, UDP, and ICMP probes to identify active hosts, an example might look like this:
```shell
nmap -PS22,80,443 -PU53,67,69 -PE -PP -e eth0 192.168.1.0/24
```
This command uses TCP SYN scans on ports 22, 80, and 443, UDP scans on ports 53, 67, and 69, and ICMP echo and timestamp requests over the network `192.168.1.0/24` using the network interface `eth0`.

### 2. Skipping Discovery
#### -sL (List Scan)
```shell
nmap -sL 192.168.1.0/24
```
This command lists each host within the specified subnet without sending any packets to the target hosts.

#### -Pn (Skip Host Discovery)
```shell
nmap -Pn 192.168.1.100-110
```
This will skip the host discovery phase and perform a port scan on every IP address from `192.168.1.100` to `192.168.1.110`.

### 3. Default Probes
Executing a scan without specifying any host discovery options:
```shell
nmap 192.168.1.0/24
```
Nmap will use its default set of probes (ICMP echo request, TCP SYN to port 443, TCP ACK to port 80, and ICMP timestamp request) to discover hosts in the `192.168.1.0/24` network.

### 4. Advanced Techniques for Evasion
Combining multiple -P* options to craft a more evasive scan:
```shell
nmap -PS80,443 -PA80,443 -PE -PP -e eth0 10.0.0.0/24
```
This scan targets the `10.0.0.0/24` subnet, sending TCP SYN and ACK packets to ports 80 and 443, along with ICMP echo and timestamp requests, aiming to bypass simple firewall rules.

### 5. Specialized Scans
#### -sn (No Port Scan)
```shell
nmap -sn 192.168.1.0/24
```
Also known as a ping scan, this command checks which hosts are up in the `192.168.1.0/24` range without performing a port scan.

#### -PS (TCP SYN Ping)
```shell
nmap -PS22,80,443 192.168.1.0/24
```
Sends TCP SYN packets to ports 22, 80, and 443 of each host in the subnet to identify active hosts.

#### -PA (TCP ACK Ping)
```shell
nmap -PA80 192.168.1.0/24
```
Sends TCP ACK packets to port 80 to discover hosts, aiming to identify responsive hosts by expecting RST responses.

#### -PU (UDP Ping)
```shell
nmap -PU53 192.168.1.0/24
```
Sends UDP packets to port 53 (DNS) to elicit responses from active hosts, expecting ICMP port unreachable messages from live systems.

#### -PE; -PP; -PM (ICMP Ping Types)
```shell
nmap -PE -PP -PM 192.168.1.0/24
```
Utilizes standard ICMP probes (echo, timestamp, and address mask request) to discover hosts in the specified subnet.

These examples demonstrate the versatility of Nmap's host discovery capabilities, allowing users to adapt the tool to a wide range of scenarios and objectives.
