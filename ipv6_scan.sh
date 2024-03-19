#!/bin/bash

# Base IPv6 address
base="2001:da8:7005:395::"

# Output file for generated addresses
output="ipv6_targets.txt"

# Output file for Nmap scan results
scan_output="nmap_scan_results.txt"

# Clear output files
> "$output"
> "$scan_output"

# Generate range of addresses
for i in {1..100}; do
  echo "${base}$i" >> "$output"
done

# Use Nmap with the generated list of addresses and save the results
nmap -6 -iL "$output" -oN "$scan_output"
