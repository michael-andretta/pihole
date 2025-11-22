# Blocklists & Allowlists

Custom DNS lists for Pi-hole filtering.

## Files

### `allow-list.txt`

Domains that should **NOT** be blocked (whitelist). Add domains here that are being incorrectly blocked by your active blocklists.

**Format**: One domain per line

```
example.com
trusted-service.com
```

### `block-list.txt`

Domains that should be blocked (blacklist). Add domains here that you want to block network-wide.

**Format**: One domain per line

```
ads.example.com
tracker.example.com
```

## Adding Lists to Pi-hole

1. Open Pi-hole Admin Dashboard
2. Navigate to **Gravity** → **Adlists**
3. For **local lists**, you can:
   - Upload files via the dashboard
   - Use local file paths
   - Copy-paste contents

## Best Practices

- **Keep lists organized**: One domain per line
- **Use comments sparingly**: Add `# comment` for clarity
- **Test changes**: Monitor your network for issues
- **Regular maintenance**: Review and update periodically

## Examples

### Allow-list Example

```
# Trusted services
discord.com
reddit.com
github.com
```

### Block-list Example

```
# Known ad servers
ads.example.com
tracker.example.com
analytics.example.com
```

## Syncing with Pi-hole

### Using Pi-hole's Web Interface

1. Create lists in this directory
2. Import via dashboard or command line
3. Enable/disable as needed

### Command Line (Advanced)

```bash
# Copy lists to Pi-hole
sudo cp allow-list.txt /etc/pihole/
sudo cp block-list.txt /etc/pihole/

# Update Gravity
pihole -g
```

## Sharing Custom Lists

If you want to share your lists publicly:

1. Ensure no sensitive information is included
2. Add descriptions via comments
3. Consider hosting online for others to use

## Related Documentation

See [../docs/LISTS.md](../docs/LISTS.md) for information about public blocklists and recommendations.
