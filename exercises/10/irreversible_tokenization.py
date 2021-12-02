import hashlib
import hmac

import util

def hash_token(s):
    '''Generates a new valid Luhn-checksummed number using a one-way hash function.

    Generation of a new number happens by means of the cycle-walking algorithm,
    with the SHA256 hash function.

    Input:
      s: String representation of base-10 number to use as starting point

    Raises:
      ValueError: If input was not a valid Luhn-checksummed number

    Returns:
      str: Base-10 representation of a new Luhn-checksummed sequence
    '''
    # Raise unless valid Luhn checksum
    if not util.luhn(s):
        raise ValueError(f"Input was not a valid Luhn-checksummed number: {s}")

    cycle = lambda b: hashlib.sha256(b).digest()
    return util.luhn_cycle_walk(cycle, s)

def mac_token(key, s):
    '''Generates a new valid Luhn-checksummed number using an HMAC construction.

    Generation of a new number happens by means of the cycle-walking algorithm,
    with the HMAC-SHA256 MAC.

    Input:
      key: String to use as key for HMAC. Will be encoded as ASCII to get key
           bytes.
      s: String representation of base-10 number to use as starting point

    Raises:
      ValueError: If input was not a valid Luhn-checksummed number

    Returns:
      str: Base-10 representation of a new Luhn-checksummed sequence
    '''
    # Raise unless valid Luhn checksum
    if not util.luhn(s):
        raise ValueError(f"Input was not a valid Luhn-checksummed number: {s}")

    # Input is numeric, so ASCII is a sane enough choice
    key_bytes = key.encode('ascii')

    cycle = lambda b: hmac.digest(key_bytes, b, "sha256")
    return util.luhn_cycle_walk(cycle, s)


if __name__ == '__main__':
    out = irreversible_tokenization("7992739871")
    print(out)
