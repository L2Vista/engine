import re


def parse(response):
    pattern = r"(?i)\(\s*(?:['\"])?([^,'\"]+)(?:['\"])?\s*,\s*(?:['\"])?([^,'\"]+)(?:['\"])?\s*,\s*(?:['\"])?([^,'\"]+)(?:['\"])?\s*,\s*(?:['\"])?([^,'\"]+)(?:['\"])?\s*,\s*(?:['\"])?([^,'\"]+)(?:['\"])?\s*\)"
    match = re.match(pattern, response)

    if match:
        from_chain = match.group(1).strip().lower() if match.group(1).strip().lower() != 'null' else 'null'
        to_chain = match.group(2).strip().lower() if match.group(2).strip().lower() != 'null' else 'null'
        category = match.group(3).strip().lower() if match.group(3).strip().lower() != 'null' else 'null'
        address = match.group(4) if match.group(4) != 'null' else 'null'
        tx_hash = match.group(5) if match.group(5) != 'null' else 'null'

        return from_chain, to_chain, category, address, tx_hash
    return 'null', 'null', 'null', 'null', 'null'


# Testing
if __name__ == "__main__":
    test_responses = [
        "('null', 'Base', 'CCIP', '0x993706A4fc0bBB2dDC10984562d174A51326bbcD', '0x23d57c2d9dcc618910ab5e918e7a8899c61c6b98095e1a4e48713ef755d67dd0')",
        "(Optimism, 'null', 'CCIP', 'null', '0x23d57c2d9dcc618910ab5e918e7a8899c61c6b98095e1a4e48713ef755d67dd0')",
        "(null, 'BASE', null, null, null)",
        "('OpTimism', 'basE', 'null', '0x993706A4fc0bBB2dDC10984562d174A51326bbcD', 0x23d57c2d9dcc618910ab5e918e7a8899c61c6b98095e1a4e48713ef755d67dd0)",
        "('OPTIMISM', 'BASE', 'CCIP', '0x993706A4fc0bBB2dDC10984562d174A51326bbcD', '0x23d57c2d9dcc618910ab5e918e7a8899c61c6b98095e1a4e48713ef755d67dd0')"
    ]

    for resp in test_responses:
        from_chain, to_chain, category, address, tx_hash = parse(resp)
        print(f"Response: {resp}")
        print(f"From: {from_chain}")
        print(f"To: {to_chain}")
        print(f"Category: {category}")
        print(f"Address: {address}")
        print(f"TX_HASH: {tx_hash}")
        print("-" * 60)
