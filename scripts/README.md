# Management Scripts

Useful scripts for Pi-hole setup, maintenance, and updates.

## Available Scripts

### `upgrade.sh`

Updates and upgrades your Pi-hole system and the Pi-hole application.

**Usage:**
```bash
chmod +x upgrade.sh
./upgrade.sh
```

**What it does:**
- Updates system packages
- Upgrades existing packages
- Updates Pi-hole application
- Cleans up unnecessary packages

**Note**: Requires `sudo` privileges

## Running Scripts

### Prerequisites

1. Scripts must be executable:
   ```bash
   chmod +x <script-name>.sh
   ```

2. Sufficient permissions (usually requires `sudo`)

### From Repository

```bash
# Navigate to scripts directory
cd scripts/

# Make script executable
chmod +x upgrade.sh

# Run with sudo
sudo ./upgrade.sh
```

## Script Details

### upgrade.sh - System Updates

This script handles:

1. **System Package Updates**
   ```bash
   sudo apt-get update
   ```

2. **System Package Upgrades**
   ```bash
   sudo apt-get upgrade -y
   ```

3. **Pi-hole Updates** (if applicable)

4. **Cleanup**
   ```bash
   sudo apt-get autoremove -y
   ```

**Recommended frequency**: Monthly or as needed

## Safety Considerations

- Always backup your configuration before major updates
- Review update notes from Pi-hole
- Test in a non-critical environment first if possible
- Keep system backups

## Scheduling Regular Updates

### Using Crontab

To run updates on a schedule:

```bash
# Edit crontab
sudo crontab -e

# Add this line to run upgrade weekly on Sundays at 2 AM
0 2 * * 0 /path/to/pihole/scripts/upgrade.sh
```

### Common Crontab Schedules

```cron
# Daily at 3 AM
0 3 * * * /path/to/upgrade.sh

# Weekly on Sunday at 2 AM
0 2 * * 0 /path/to/upgrade.sh

# Monthly on the 1st at 4 AM
0 4 1 * * /path/to/upgrade.sh
```

## Creating Custom Scripts

To create additional maintenance scripts:

1. Create new `.sh` file in this directory
2. Add appropriate permissions:
   ```bash
   chmod +x your-script.sh
   ```
3. Document script purpose and usage
4. Add to this README

## Troubleshooting

### Script Won't Run

- Check execute permissions: `ls -l script.sh`
- Verify you have sudo access
- Check script syntax: `bash -n script.sh`

### Updates Fail

- Check internet connectivity
- Verify system disk space: `df -h`
- Review system logs: `sudo journalctl -xe`

## Related Documentation

- [Installation Guide](../docs/INSTALLATION.md)
- [Configuration Guide](../docs/CONFIGURATION.md)
- System documentation: `man apt-get`

## Best Practices

1. **Schedule updates**: Use cron for regular maintenance
2. **Monitor logs**: Check Pi-hole logs after updates
3. **Backup data**: Before major updates
4. **Test changes**: Verify DNS still works after updates
5. **Document changes**: Keep notes of what was updated

## Support

For issues:
- Check Pi-hole logs: `sudo journalctl -u pihole-FTL.service -f`
- Visit [r/pihole](https://www.reddit.com/r/pihole/)
- Check [Pi-hole GitHub Issues](https://github.com/pi-hole/pi-hole/issues)
