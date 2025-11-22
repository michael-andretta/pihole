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

### Adding Lists from a Repository

1. Open Pi-hole Admin Dashboard
2. Navigate to **Adlists** (or **Gravity** → **Adlists** depending on your version)
3. Click **Add New Adlist**
4. Paste the raw URL to the list file, for example:
   - `https://raw.githubusercontent.com/your-repo/lists/main/allow-list.txt`
   - `https://raw.githubusercontent.com/your-repo/lists/main/block-list.txt`
5. (Optional) Add a description in the **Comment** field
6. Click **Add** to save
7. Pi-hole will automatically sync the list according to the update frequency

### Adding Local Lists

For lists stored locally on your Pi-hole system:

1. Open Pi-hole Admin Dashboard
2. Navigate to **Adlists**
3. For **local lists**, you can:
   - Upload files via the dashboard
   - Use local file paths (e.g., `/etc/pihole/allow-list.txt`)
   - Copy-paste contents directly

### List Update Frequency

- **Default Update Interval**: Pi-hole checks for list updates every **24 hours** (1 day)
- **Manual Update**: You can force an immediate update by running `pihole -g` in the terminal or via the dashboard
- **Custom Frequency**: To change the update frequency:
  1. SSH into your Pi-hole
  2. Edit `/etc/pihole/pihole-FTL.conf`
  3. Look for `GRAVITY_UPDATE_INTERVAL` and set your preferred interval (in hours)
  4. Restart Pi-hole: `sudo systemctl restart pihole-FTL`

**Note**: More frequent updates increase server load. 24 hours is recommended for most users.

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

## Recommended Public Blocklists

Below are tested and working blocklists that can be added to Pi-hole:

### Advertising & General Purpose

- **StevenBlack/hosts** (Comprehensive ad blocking)
  - URL: `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts`
  - Popular and widely used

- **AdAway** (Ad blocking)
  - URL: `https://adaway.org/hosts.txt`
  - Well-maintained and reliable

- **Firebog Easylist** (Advertising)
  - URL: `https://v.firebog.net/hosts/Easylist.txt`
  - Excellent coverage for ads

- **Firebog Admiral** (Ad blocking)
  - URL: `https://v.firebog.net/hosts/Admiral.txt`
  - Lightweight option

- **Sysctl.org Cameleon** (General purpose)
  - URL: `http://sysctl.org/cameleon/hosts`
  - Regular updates

### Tracking & Telemetry

- **Firebog Easyprivacy** (Tracking protection)
  - URL: `https://v.firebog.net/hosts/Easyprivacy.txt`
  - Prevents tracker connections

- **Firebog Prigent-Ads** (Tracking & ads)
  - URL: `https://v.firebog.net/hosts/Prigent-Ads.txt`
  - Combined protection

- **WindowsSpyBlocker** (Telemetry blocking)
  - URL: `https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt`
  - Blocks Windows telemetry

- **Perflyst PiHole Blocklist - Android Tracking**
  - URL: `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt`
  - Android device tracking

### Malware & Security

- **Firebog Prigent-Malware** (Malware blocking)
  - URL: `https://v.firebog.net/hosts/Prigent-Malware.txt`
  - Malicious domain blocking

- **Firebog RPiList-Malware** (Raspberry Pi list)
  - URL: `https://v.firebog.net/hosts/RPiList-Malware.txt`
  - Pi-hole optimized malware list

- **Phishing Army** (Phishing protection)
  - URL: `https://phishing.army/download/phishing_army_blocklist_extended.txt`
  - Extended phishing database

- **URLhaus Malware** (Malware URLs)
  - URL: `https://urlhaus.abuse.ch/downloads/hostfile/`
  - Tracks malware distribution sites

- **Firebog Prigent-Crypto** (Cryptominer blocking)
  - URL: `https://v.firebog.net/hosts/Prigent-Crypto.txt`
  - Blocks cryptocurrency miners

### Spam & Suspicious

- **KADhosts** (Spam & suspicious)
  - URL: `https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt`
  - Comprehensive spam blocking

- **Spam404** (Malicious content)
  - URL: `https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt`
  - Blacklist of malicious domains

- **NoTrack Blocklist** (General purpose)
  - URL: `https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt`
  - Well-maintained blocklist

- **NoTrack Malware** (Malware specific)
  - URL: `https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt`
  - Malware-focused list

### Specialized Lists

- **Social Media Blocking** (Facebook tracking)
  - URL: `https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt`
  - Blocks Facebook trackers

- **Chad Mayfield's Porn Blocklist** (Adult content)
  - URL: `https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_all.list`
  - Comprehensive adult content blocking

- **Perflyst SmartTV Blocklist** (Smart TV tracking)
  - URL: `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt`
  - Blocks Smart TV telemetry

- **Perflyst Amazon Fire TV Blocklist**
  - URL: `https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt`
  - Fire TV tracking blocking

### Whitelists (Allowlists)

- **anudeepND Whitelist** (Popular services)
  - URL: `https://github.com/anudeepND/whitelist`
  - Prevents false positives for common services

## Quick Addition Guide

To add any of these lists to your Pi-hole:

1. Copy the URL from above
2. Go to Pi-hole Admin Dashboard → **Adlists**
3. Click **Add New Adlist**
4. Paste the URL
5. Add a descriptive comment (optional)
6. Click **Add**

Pi-hole will automatically check and sync these lists based on your configured update frequency.

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
