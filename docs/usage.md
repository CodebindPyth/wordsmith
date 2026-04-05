# Usage

## Option 1 — Generate a password wordlist

Use this option to build a password list from a target's personal details.

- First name
- Last name
- Keywords/interests
- Partner name
- Birthday
- Job
- Pet name
- Kids' names
- City or zipcode
- Lucky number
- Phone number

The generator applies transformations such as:

- leet speak
- alternating capitalization
- vowel removal
- reverse text
- separators and numeric suffixes
- birthday-based patterns
- multi-field combinations

## Option 2 — Generate random emails

Generate random email addresses with a custom domain and optional keyword prefix.

## Option 3 — Generate phone numbers

Generate random phone numbers for supported country codes.

## Option 4 — Validate and breach-check

- Validate email format locally
- Validate phone numbers with the `phonenumbers` library
- Check a single email against Have I Been Pwned
- Batch-check emails from a file against Have I Been Pwned

### HIBP rate limiting

The tool waits between requests to avoid abusing the public API and to keep usage respectful.
