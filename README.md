[README.md](https://github.com/user-attachments/files/26489790/README.md)
# wordsmith - Password Generator & Validation Tool

A powerful password wordlist generator with email/phone validation and "Have I Been Pwned?" integration.

## Disclaimer

**This project is strictly for educational and research purposes only.**

### What This Tool Does NOT Do:
-  Does NOT attempt unauthorized access to any system
-  Does NOT perform hacking or illegal activities
-  Does NOT scrape, crawl, or abuse third-party services
-  Does NOT store, sell, or misuse personal data
-  Does NOT validate credentials against live systems
-  Third-party API responses (like HIBP) may contain stale or inaccurate data

### What This Tool DOES Do:
- Generates password combinations based on personal information (for authorized penetration testing)
- Validates email format and phone number format locally
- Queries the public "Have I Been Pwned?" database (read-only, no authentication bypass)
- Helps security researchers understand password patterns

### Legal Requirements:
- You must have **explicit written authorization** before using this tool on any system or data you do not own
- Using this tool for unauthorized access, hacking, or illegal purposes is a criminal offense
- The authors are not responsible for misuse, damages, or legal consequences
- Comply with all local, state, and federal laws

### IMPORTANT:
This tool is provided "AS IS" without any warranty. Users are solely responsible for ensuring compliance with applicable laws and regulations. Unauthorized access to computer systems is illegal.

## Features

### Option 1: Password Generation
- Generate thousands of password combinations from personal data
- Uses transformations: leet speak, alternating caps, vowel removal
- Supports separators and numeric patterns
- Deduplication for unique passwords only

### Option 2: Email Generation
- Random email generation with custom domain
- Keyword-based email prefixes

### Option 3: Phone Number Generation
- Support for Greece (+30) and Turkey (+90)
- Random generation within valid ranges

### Option 4: Validation & HIBP Checking
**Sub-options:**
1. **Email Format Validation** — Local regex validation only
2. **Phone Number Validation** — Uses phonenumbers library
3. **Single Email HIBP Check** — Check if email was in known breaches
4. **Batch Email HIBP Checking** — Check multiple emails from file

#### Important Notes on HIBP:
- Queries the public "Have I Been Pwned?" API (with rate limiting)
- Does NOT attempt to bypass, hack, or login to HIBP
- Information is publicly available and read-only
- Respects API TOS with 2-second delays between requests

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Follow the interactive menu to choose your option.

## Requirements

See `requirements.txt`:
- requests >= 2.31.0
- phonenumbers >= 8.13.0
- tqdm >= 4.66.0
- pystyle >= 2.2.4

## Authors
- CodebindPyth 

## License
Educational Use Only - See Disclaimer

---

**Remember:** This tool is for authorized security testing and education only. Always obtain proper authorization before testing any systems you do not own.
