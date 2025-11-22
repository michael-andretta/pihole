# Configuration Files

Configuration files and templates for Pi-hole setup.

## Files

### `config.yml`

Main configuration file containing basic Pi-hole settings.

**Current settings:**
```yaml
ip_address: 10.0.10.50
```

Modify the IP address to match your Pi-hole installation.

## Examples Directory

The `examples/` directory contains template configurations for different scenarios:

- **Basic setup**: Standard Pi-hole configuration
- **Advanced setup**: With DNS over HTTPS and additional features
- **High-performance**: Optimized for larger networks

## Using Configuration Files

### Manual Configuration

1. Edit `config.yml` with your specific settings
2. Save the configuration
3. Apply settings through Pi-hole admin dashboard or configuration files

### Command Line Configuration

```bash
# Copy configuration to Pi-hole directory
sudo cp config.yml /etc/pihole/

# Apply configuration
pihole updateGravity
```

## Configuration Options

### Network Settings

```yaml
ip_address: 10.0.10.50          # Pi-hole IP address
dns_port: 53                     # DNS listening port
```

### Upstream DNS

```yaml
upstream_dns:
  - 1.1.1.1                      # Cloudflare DNS
  - 8.8.8.8                      # Google DNS
```

### DHCP Settings (if enabled)

```yaml
dhcp_enabled: true
dhcp_start: 10.0.10.100
dhcp_end: 10.0.10.200
dhcp_gateway: 10.0.10.1
```

## Best Practices

1. **Backup before changes**: Always backup your configuration
2. **Test incrementally**: Make one change at a time
3. **Monitor logs**: Check logs after configuration changes
4. **Document customizations**: Note why you made specific changes

## Advanced Configuration

For advanced options, refer to:
- [Official Pi-hole Documentation](https://docs.pi-hole.net/)
- [dnsmasq Configuration](http://www.thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html)

## Troubleshooting

### Configuration Not Applied

1. Check file permissions
2. Verify file format (YAML syntax)
3. Restart Pi-hole: `sudo systemctl restart pihole-FTL`

### DNS Issues

1. Verify upstream DNS is reachable
2. Check port 53 is not in use
3. Review Pi-hole logs

## Support

See [../docs/CONFIGURATION.md](../docs/CONFIGURATION.md) for detailed configuration guidance.
