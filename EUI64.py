def mac_to_ipv6(mac_address, ipv6_prefix):
    # 分割 MAC 地址为 OUI 和 NIC 特定部分，并插入FFFE
    parts = mac_address.split(":")
    eui_64 = parts[:3] + ['ff', 'fe'] + parts[3:]
    # 翻转第七位
    eui_64[0] = "{:02x}".format(int(eui_64[0], 16) ^ 0x02)
    
    # 将 EUI-64 地址部分转换为 IPv6 格式
    ipv6_suffix = ':'.join(eui_64[i] + eui_64[i+1] for i in range(0, len(eui_64), 2))
    
    # 组合 IPv6 前缀和生成的后缀
    ipv6_address = ipv6_prefix + ":" + ipv6_suffix
    return ipv6_address

# 示例 MAC 地址列表
mac_addresses = ["A8:77:E5:71:25:21","F8:AF:05:29:29:67","EC:4D:3E:99:4D:2B","00:1D:53:00:65:E3","BA:B6:21:5D:E6:6A","72:83:0E:F0:67:A3"]
ipv6_prefix = "fe80:"  # 示例 IPv6 网络前缀

# 生成 IPv6 地址
ipv6_addresses = [mac_to_ipv6(mac, ipv6_prefix) for mac in mac_addresses]
for ipv6 in ipv6_addresses:
    print(ipv6)