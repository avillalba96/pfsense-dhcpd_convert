# dhcpd_to_pfsense

## HOW TO

Converts static address mappings from dhcpd.conf (isc-dhcp-server) to config.xml (pfSense)

1) Cut dhcpd.conf and leave only static mappings (remove DHCP config stuff) and save it in the same folder with name **dhcpd.conf**. Maybe you don't even need to do it but you never know.
My format for static mappings is "host namehere { hardware ethernet FF:FF:FF:FF:FF:FF; fixed-address 0.0.0.0; }" but every format should work.
2) Run **python3.10 dhcpd_to_pfsense.py**
3) Insert contents of **output.xml** in your config.xml under the dhcp section.
4) Import the updated config.xml in pfSense.

## DISCLAIMER

Please don't trust this with your life. It's just a simple tool I made for me and worked really well, I did not test further. If you use it please check some of the generated entries to make sure everything is ok.

If you don't know where to put the contents of **output.xml** insert a dummy static mapping using pfSense web interface, export the config and add everything after that dummy entry (of course you can remove the dummy later).
