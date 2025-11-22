# Contributing to This Pi-hole Repository

Thank you for your interest in contributing! This document provides guidelines for participating in this project.

## How to Contribute

### Reporting Issues

If you find a problem:

1. Check existing [GitHub Issues](https://github.com/michael-andretta/pihole/issues)
2. Provide:
   - Clear description of the issue
   - Steps to reproduce (if applicable)
   - Expected vs. actual behavior
   - Your Pi-hole version
   - Any relevant error messages

### Suggesting Improvements

Have an idea to improve this repository?

1. Open a [GitHub Issue](https://github.com/michael-andretta/pihole/issues) with the label `enhancement`
2. Describe:
   - What improvement you're suggesting
   - Why it would be beneficial
   - Any implementation ideas

### Submitting Changes

#### Pull Request Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/pihole.git
   cd pihole
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the style guide (see below)
   - Test your changes
   - Keep commits clear and concise

4. **Commit your changes**
   ```bash
   git commit -m "Brief description of changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Reference any related issues (#issue-number)
   - Describe what changes were made
   - Explain why these changes are beneficial

## Contribution Guidelines

### Code & Documentation Style

- **Markdown**: Clear headings, proper formatting
- **Scripts**: Include comments, error handling, and usage documentation
- **Lists**: One domain per line, sorted alphabetically (optional)
- **Configuration**: YAML format with comments

### Blocklist Contributions

When suggesting additions to blocklists:

1. **Provide source/justification**
   - Why should this domain be added?
   - Is it a known ad/tracking domain?
   - Do you have multiple sources confirming this?

2. **Check for duplicates**
   - Ensure the domain isn't already in the list
   - Check popular blocklists for consistency

3. **Consider false positives**
   - Is this a legitimate service that shouldn't be blocked?
   - Could it affect other users?

### Documentation Contributions

Improve our documentation by:

- Fixing typos or unclear sections
- Adding examples or clarifications
- Updating outdated information
- Adding troubleshooting tips

### Configuration Contributions

Share your configurations:

1. Ensure no sensitive data is included
   - Remove passwords or API keys
   - Use placeholder values
   - Document what needs to be customized

2. Add to `config/examples/` with descriptive filename

3. Include a README explaining:
   - What this configuration does
   - Why you created it
   - How to customize it

## Repository Structure

Understanding our structure helps with contributions:

```
.
├── docs/                  # Documentation
├── lists/                 # Blocklists & allowlists
├── config/                # Configuration files
├── scripts/               # Maintenance scripts
└── README.md              # Main overview
```

## Testing

Before submitting:

1. **Validate your changes**
   - If modifying lists: Check for syntax errors
   - If modifying scripts: Test execution
   - If modifying documentation: Review for clarity

2. **Test with Pi-hole**
   - Import/apply your changes
   - Verify expected behavior
   - Check for unexpected side effects

## Communication

- **Be respectful**: Treat others with courtesy
- **Be constructive**: Offer solutions, not just criticism
- **Be patient**: Maintainers are volunteers
- **Search first**: Check if your question has been answered

## License

By contributing, you agree that your contributions will be licensed under the same license as this project.

## Questions?

- Check [existing discussions](https://github.com/michael-andretta/pihole/discussions)
- Review [documentation](docs/)
- Ask in [issues](https://github.com/michael-andretta/pihole/issues)

## Recognition

Contributors will be recognized in:
- Git commit history
- GitHub contributors list
- Project documentation (if applicable)

Thank you for helping improve this project! 🎉
