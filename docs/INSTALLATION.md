# Pi-hole Installation Guide

## Overview

This guide provides resources for installing and setting up Pi-hole on your network.

## Prerequisites

- Raspberry Pi (or Linux-based system)
- Network connection
- Basic command-line knowledge

## Official Installation

For the official installation guide, visit:
- [Pi-hole Official Installation](https://pi-hole.net/)

## Recommended Tutorials

We recommend the following comprehensive guides:

1. **Crosstalk Solutions - Pi-hole and Unbound Tutorial 2023**
   - https://www.crosstalksolutions.com/the-worlds-greatest-pi-hole-and-unbound-tutorial-2023/
   - Covers Pi-hole with DNS over HTTPS (DoH) setup

2. **Pi-hole GitHub Repository**
   - https://github.com/pi-hole
   - Official source code and latest updates

## Quick Installation Steps

```bash
# Update your system
sudo apt-get update
sudo apt-get upgrade -y

# Download and run Pi-hole installer
curl -sSL https://install.pi-hole.net | bash
```

## Post-Installation

After installation:

1. Access the admin dashboard at `http://<your-pi-hole-ip>/admin`
2. Configure your DNS settings
3. Add blocklists and allowlists from this repository
4. Set Pi-hole as your network's DNS server

## Configuration

See [CONFIGURATION.md](CONFIGURATION.md) for detailed configuration steps.

## Blocklists

See [LISTS.md](LISTS.md) for recommended blocklists and how to add them.

## Troubleshooting

- Check the official Pi-hole documentation
- Visit the [Pi-hole community on Reddit](https://www.reddit.com/r/pihole/)
- Review Pi-hole logs: `sudo tail -f /var/log/pihole/pihole.log`

## Updates

To keep Pi-hole updated, use the update script or Pi-hole's built-in update function.

See [RESOURCES.md](RESOURCES.md) for more information on updates.
