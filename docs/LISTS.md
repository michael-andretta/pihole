# Pi-hole Blocklists Documentation

## Overview

Blocklists are curated lists of domains that Pi-hole will block at the DNS level. This provides network-wide ad blocking and threat protection.

## Available Lists

### Blocklists in This Repository

- **`block-list.txt`** - Custom domains to block
- **`allow-list.txt`** - Domains to whitelist (prevent blocking)

See [lists/README.md](../lists/README.md) for current contents.

## Recommended Public Blocklists

### General Ad/Tracker Blocking

1. **StevenBlack/hosts**
   - URL: https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
   - Combines multiple blocklists into one comprehensive list
   - Highly maintained and regularly updated

2. **Firebog Curated Lists**
   - Website: https://firebog.net/
   - Multiple categorized lists:
     - Ads: https://v.firebog.net/hosts/Prigent-Ads.txt
     - Malware: https://v.firebog.net/hosts/Prigent-Malware.txt

3. **Disconnect.me Lists**
   - Tracking: https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt
   - Ads: https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt

### Malware & Security

- **Phishing Lists**: Various blocklists specifically for phishing domains
- **Ransomware Lists**: Domains known to host ransomware

### Content Filtering

- **Adult Content**: Optional lists for family-friendly filtering
- **Gambling**: Lists for blocking gambling sites
- **Social Media**: Optional lists for blocking social platforms

## Finding More Lists

### List Aggregators

- **Firebog**: https://firebog.net/
- **Awesome Lists**: Various curated list collections on GitHub

### Reddit Community

- **r/pihole**: https://www.reddit.com/r/pihole/
- Community recommendations and discussions
- FAQ and troubleshooting help

## Best Practices

### Recommended Approach

1. **Start with proven lists**
   - StevenBlack/hosts is a solid foundation
   - Firebog's curated lists are well-maintained

2. **Add custom lists gradually**
   - Monitor your network for false positives
   - Adjust as needed

3. **Maintain an allowlist**
   - As you find legitimately blocked sites
   - Add them to `lists/allow-list.txt`

4. **Monitor performance**
   - Keep list count reasonable
   - Too many lists can impact performance
   - Watch DNS query response times

### Performance Considerations

- **Number of Lists**: Most setups use 5-15 lists effectively
- **List Size**: Larger lists take more memory and CPU
- **Refresh Frequency**: Adjust based on your needs
- **Cache Settings**: Enable DNS caching for speed

## Blocklist Maintenance

### Regular Updates

Enable automatic list updates in Pi-hole:
- **Settings** → **Adlists**
- Most lists update daily or weekly

### Monitoring

Use the admin dashboard to:
- View blocked queries
- Track which lists are blocking domains
- Identify false positives

### Custom Adjustments

1. **Whitelist (Allow-list)**
   - Add to `lists/allow-list.txt` in this repository
   - Or use Pi-hole's Whitelist feature

2. **Blacklist (Block-list)**
   - Add to `lists/block-list.txt` in this repository
   - Or use Pi-hole's Adlists feature

## Adding Lists to Pi-hole

### Step-by-Step

1. Open Pi-hole Admin Dashboard
2. Navigate to **Gravity** → **Adlists**
3. Paste the blocklist URL
4. Click **Add**
5. Click **Update Gravity**

### Bulk Import

For multiple lists, you can:
1. Copy list URLs
2. Add them one by one through the dashboard
3. Or import via configuration file

## Troubleshooting

### Lists Not Updating

- Check internet connectivity
- Verify blocklist URLs are valid
- Check Pi-hole logs for errors

### Too Many False Positives

- Reduce number of active lists
- Review which lists are overly aggressive
- Add frequently-needed sites to allowlist

### Performance Degradation

- Reduce number of lists
- Increase DNS cache TTL
- Monitor system resources

## Additional Resources

- [Official Pi-hole List Management](https://docs.pi-hole.net/ftldns/blockingmode/)
- [Firebog Safe Lists](https://firebog.net/)
- [Reddit Pi-hole Community](https://www.reddit.com/r/pihole/)
