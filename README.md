# Pi-hole Configuration Repository

A curated collection of configurations, blocklists, and resources for Pi-hole DNS filtering and ad-blocking.

## ⚠️ Disclaimer

**Use at your own risk.** This repository is provided as-is without any warranty or guarantee. While these configurations and lists are intended to improve privacy and security:

- **False Positives**: Aggressive blocklists may block legitimate services
- **Service Disruption**: Incorrect configurations may disrupt network services
- **No Support Guarantee**: Use and modification are entirely at your own discretion
- **Test Changes**: Always test new lists and settings in a controlled environment
- **Whitelist as Needed**: Be prepared to whitelist services if they become blocked

**Before deploying to production**, thoroughly test all configurations and blocklists on a test system or Pi-hole installation.

## Quick Start

### Installation & Setup

1. **Official Pi-hole Installation**: https://pi-hole.net/
2. **Comprehensive Setup Guide**: https://www.crosstalksolutions.com/the-worlds-greatest-pi-hole-and-unbound-tutorial-2023/
3. **Official GitHub**: https://github.com/pi-hole

### Repository Contents

- **`/config/`** - Configuration files and settings
- **`/lists/`** - Custom blocklists and allowlists
- **`/docs/`** - Detailed documentation and guides

## Documentation

For more detailed information, see:

- **[CONFIGURATION.md](docs/CONFIGURATION.md)** - Detailed setup and configuration guide
- **[LISTS.md](docs/LISTS.md)** - Information about blocklists
- **[RESOURCES.md](docs/RESOURCES.md)** - Additional resources and links

## Community & Support

### Reddit
- **r/pihole**: https://www.reddit.com/r/pihole/ - Active community for questions and discussion

### Official Resources
- **Pi-hole Discussions**: https://github.com/orgs/pi-hole/discussions
- **Pi-hole Issues**: https://github.com/pi-hole/pi-hole/issues

## Recommended Blocklists

### List Aggregators & Tools
- **Firebog**: https://firebog.net/ - Curated blocklist collection
- **anudeepND Whitelist**: https://github.com/anudeepND/whitelist - Popular service whitelist
- **Pi-hole Update Lists**: https://github.com/jacklul/pihole-updatelists - Automated list management

### Popular Blocklists

**Advertising:**
- https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
- https://v.firebog.net/hosts/Prigent-Ads.txt
- https://adaway.org/hosts.txt

**Malware & Threats:**
- https://v.firebog.net/hosts/Prigent-Malware.txt
- https://urlhaus.abuse.ch/downloads/hostfile/

**Tracking & Telemetry:**
- https://v.firebog.net/hosts/Easyprivacy.txt

**General Purpose:**
- http://sysctl.org/cameleon/hosts

## Learning Resources

### Security & Privacy
- **Privacy Best Practices**: https://beaconsandwich.co.uk/2020/05/03/shut-your-pi-hole/
- **Blocklist Strategy (2023)**: https://arstech.net/pi-hole-blocking-lists-2023/

### Maintenance
- **Automated Updates**: https://github.com/jacklul/pihole-updatelists

## Best Practices

1. **Start Small**: Begin with a few trusted blocklists before adding more
2. **Monitor Performance**: Check query logs and whitelist as needed
3. **Regular Updates**: Keep Pi-hole and blocklists current
4. **Backup Configuration**: Save your settings before major changes
5. **Document Changes**: Keep track of what you've modified for troubleshooting

## Contributing

Found an issue or have improvements? Feel free to contribute to this repository or share feedback with the Pi-hole community.

---

**Last Updated**: November 2025
