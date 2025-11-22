# Pi-hole Resources

A collection of helpful links and resources for Pi-hole users.

## Official Resources

### Pi-hole Project

- **Official Website**: https://pi-hole.net/
- **GitHub Repository**: https://github.com/pi-hole
- **Official Documentation**: https://docs.pi-hole.net/
- **GitHub Discussions**: https://github.com/orgs/pi-hole/discussions

## Tutorials & Guides

### Comprehensive Setup Guides

1. **Crosstalk Solutions - Pi-hole & Unbound 2023**
   - URL: https://www.crosstalksolutions.com/the-worlds-greatest-pi-hole-and-unbound-tutorial-2023/
   - Covers Pi-hole with DNS over HTTPS (DoH) and encrypted DNS

2. **Beacon Sandwich - "Shut Your Pi-hole"**
   - URL: https://beaconsandwich.co.uk/2020/05/03/shut-your-pi-hole/
   - Security and privacy considerations

3. **ARS Technica - Pi-hole Blocking Lists 2023**
   - URL: https://arstech.net/pi-hole-blocking-lists-2023/
   - List recommendations and strategies

## Blocklist Resources

### List Aggregators

- **Firebog**: https://firebog.net/
  - Curated, categorized blocklists
  - Community-maintained
  - Recommended for beginners

- **anudeepND's Whitelist**: https://github.com/anudeepND/whitelist
  - Comprehensive whitelist for popular services

### Popular Blocklists

- **StevenBlack/hosts**: https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
- **Sysctl.org Cameleon**: http://sysctl.org/cameleon/hosts
- **Firebog Ads List**: https://v.firebog.net/hosts/Prigent-Ads.txt
- **Firebog Malware List**: https://v.firebog.net/hosts/Prigent-Malware.txt
- **Disconnect.me Tracking**: https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
- **Disconnect.me Ads**: https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt

### Content-Specific Lists

- **Chad Mayfield's Porn Blocklist**: https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_all.list

## Updates & Maintenance

### Update Management

- **Pi-hole Update Lists Project**: https://github.com/jacklul/pihole-updatelists
  - Automated blocklist updates with advanced features
  - Improved list management capabilities

### Keeping Pi-hole Current

- Enable automatic updates in Pi-hole settings
- Follow official GitHub releases
- Monitor community discussions for new recommendations

## Community & Support

### Reddit

- **r/pihole**: https://www.reddit.com/r/pihole/
  - Active community
  - Q&A and troubleshooting
  - Configuration sharing
  - Weekly discussion threads

### GitHub

- **Pi-hole Issues**: https://github.com/pi-hole/pi-hole/issues
- **Pi-hole Discussions**: https://github.com/orgs/pi-hole/discussions

### Useful Related Projects

- **Unbound DNS**: Encrypted DNS resolver (often paired with Pi-hole)
- **Wireguard**: VPN tunnel to access Pi-hole remotely
- **PiVPN**: VPN configuration for Pi-hole networks

## Security & Privacy

### DNS Security

- Consider using encrypted DNS (DoH, DoT)
- Enable DNSSEC if supported
- Regular security updates

### Privacy Considerations

- Review which blocklists align with your privacy needs
- Consider upstream DNS provider privacy policies
- Monitor your Pi-hole's own security

## Hardware & Networking

### Recommended Hardware

- Raspberry Pi 4 (4GB+ RAM recommended)
- Proper power supply
- Adequate cooling (optional, but recommended for 24/7 operation)

### Network Configuration

- Static IP assignment for Pi-hole
- DNS server configuration on router or devices
- DHCP settings if using Pi-hole's DHCP server

## Troubleshooting Resources

### Common Issues

- Pi-hole Documentation: https://docs.pi-hole.net/
- GitHub Issues: https://github.com/pi-hole/pi-hole/issues
- Reddit: https://www.reddit.com/r/pihole/

### Query Logs

- Monitor query logs in admin dashboard
- Identify problematic domains
- Refine blocklists accordingly

## Contributing to Pi-hole

### How to Contribute

- Report bugs on GitHub
- Suggest improvements
- Share configurations and setups
- Help community members

## Additional Reading

### Articles & Blogs

- Network security basics
- DNS filtering explained
- Privacy-focused networking
- Home lab setup guides

## Related Technologies

- **DNS over HTTPS (DoH)**
- **DNS over TLS (DoT)**
- **DNSSEC**
- **Network segmentation**
- **VPN configurations**

---

For the latest information, always refer to the official Pi-hole documentation and community resources.
