# Pi-hole Configuration Guide

## Overview

This guide covers configuring Pi-hole with the configurations and settings provided in this repository.

## Configuration Files

Configuration files are located in the `config/` directory.

### Main Configuration

The `config.yml` file contains basic settings:

```yaml
ip_address: 10.0.10.50
```

Adjust the IP address to match your Pi-hole installation.

## Adding Blocklists

Pi-hole allows you to add multiple blocklists for effective ad blocking.

### Using Lists from This Repository

1. Log into the Pi-hole Admin Dashboard
2. Navigate to **Adlists**
3. Add the lists from the `lists/` directory

#### Recommended Blocklists

Popular blocklists include:

- **StevenBlack/hosts**: https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
- **Firebog Lists**: https://v.firebog.net/
- **Disconnect.me**: https://s3.amazonaws.com/lists.disconnect.me/

For more information, see [LISTS.md](LISTS.md).

## Custom Allow/Block Lists

### Allowlist (Whitelist)

Edit `lists/allow-list.txt` to add domains that should NOT be blocked:

```
example.com
trusted-service.com
```

### Blocklist (Blacklist)

Edit `lists/block-list.txt` to add domains that should be blocked:

```
ads.example.com
tracker.example.com
```

## Admin Dashboard Configuration

### Basic Settings

1. **Settings** → **DNS Records**
   - Configure your DNS settings
   - Add upstream DNS servers (Cloudflare, Quad9, etc.)

2. **Settings** → **DHCP**
   - Enable/disable DHCP server
   - Set DHCP range

3. **Settings** → **Adlists**
   - Add or remove blocklists
   - Enable/disable lists

### Network Configuration

Set Pi-hole as your network's primary DNS:

- **Router Settings**: Set Pi-hole IP as the primary DNS
- **Individual Devices**: Manually set DNS to Pi-hole IP

## Upstream DNS Servers

Popular options:

- **Cloudflare**: `1.1.1.1` and `1.0.0.1`
- **Quad9**: `9.9.9.9` and `149.112.112.112`
- **OpenDNS**: `208.67.222.222` and `208.67.220.220`

## Performance Tuning

- Enable DNS caching
- Adjust blocklist refresh intervals
- Monitor query logs for insights

For more details, refer to the official Pi-hole documentation.

## Troubleshooting

### DNS Not Resolving

- Check upstream DNS configuration
- Verify Pi-hole is running: `sudo systemctl status pihole-FTL`

### Some Sites Blocked Unexpectedly

- Check allowlist (`lists/allow-list.txt`)
- Review active blocklists
- Check the query log in the admin dashboard

### Performance Issues

- Reduce number of active blocklists
- Check system resources (CPU, RAM)
- Verify DNS query response times

## Advanced Configuration

See the [Pi-hole documentation](https://docs.pi-hole.net/) for advanced configuration options.
