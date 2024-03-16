# NMapLearning

This repository will store the files that I use in the process of learning NMap.

To view all details about Nmap,tap in https://nmap.org/.

Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. It was designed to rapidly scan large networks, but works fine against single hosts.

In addition to the classic command-line Nmap executable, the Nmap suite includes an advanced GUI and results viewer (Zenmap), a flexible data transfer, redirection, and debugging tool (Ncat), a utility for comparing scan results (Ndiff), and a packet generation and response analysis tool (Nping).

## Download
When I download NMap,the official download page provides me with the following information,which impresses me:
For the more security-paranoid (smart) users, GPG detached signatures and SHA-1 hashes for each release are available in the sigs directory (verification instructions). 
Let's delve into this information.

To ensure the software you've downloaded hasn't been tampered with and is indeed the official release,you can use GPG(GNU Privacy Guard)for signature verification and SHA-1 for checksum vertification.Here's a general guide on how to do this:

### Verifying with GPG(GNU Privacy Guard)
To ensure the software you've downloaded hasn't been tampered with and is indeed the official release, you can use GPG (GNU Privacy Guard) for signature verification and SHA-1 for checksum verification. Here's a general guide on how to do this:

1. **Download GPG:** If you haven't already, download and install GPG from [the official GnuPG website](https://gnupg.org/download/).

2. **Import the Public Key:** Download the public key used by the software publisher. For Nmap, you can usually find this on their official website. Import this key to your GPG keyring by running:
   ```
   gpg --import public_key_file.asc
   ```
   Replace `public_key_file.asc` with the filename of the downloaded public key.

3. **Verify the Signature:** After downloading the software and its corresponding `.sig` or `.asc` signature file, run:
   ```
   gpg --verify software.sig software.zip
   ```
   Replace `software.sig` with the signature file name and `software.zip` with the name of the downloaded software file. GPG will verify the signature and report if it is valid or not.

If the verification is successful, GPG will indicate that the signature is good and the software is untampered. If it reports that the signature is not valid, then the file may have been altered or corrupted.

### Verifying with SHA-1

1. **Calculate the SHA-1 Hash of the Downloaded File:** Use a tool to calculate the SHA-1 hash of the file you've downloaded. On Unix-like systems (Linux, macOS), you can use the `sha1sum` command:
   ```
   sha1sum software.zip
   ```
   On Windows, you can use CertUtil:
   ```
   CertUtil -hashfile software.zip SHA1
   ```
   Replace `software.zip` with the name of your downloaded file.

2. **Compare the Hashes:** Compare the calculated hash to the official SHA-1 hash provided by the software publisher (usually found on their website or alongside the file in the `sigs` directory).

If the two hashes match exactly, the file has not been altered from its original state. If they don't match, the file may have been tampered with or corrupted during download.

### Additional Notes

- It's important to download the GPG public key and SHA-1 hash from a reliable source, ideally the official website of the software publisher.
- SHA-1 is considered to be weak against well-funded attackers as of my last update. If available, consider using stronger algorithms like SHA-256 for hash verification.
- Always ensure your GPG and other cryptographic tools are up to date to protect against vulnerabilities.

This process provides a strong assurance that the software you've downloaded is genuine and has not been tampered with, leveraging both cryptographic signature and hash verification methods.
