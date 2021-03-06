def calculate_luhn_checksum(s):
    '''Calculates the Luhn checksum of the number encoded in s

    Input:
      s: String representation of base-10 number of which to calculate Luhn
         checksum

    Returns:
      int: Luhn checkdigit

    Raises:
      ArgumentError: If input is not a number
    '''

    try:
        int(s)
    except ValueError:
        raise ValueError(f"Passed value was not a valid base-10 number: {s}")

    digits = [int(c) for c in s]
    # We'll revert them here, then we can just iterate forward
    digits.reverse()

    sum = 0
    for idx, digit in enumerate(digits):
        if idx % 2 == 0:
            sum += 2 * digit
            if digit >= 5:
                # If digit * 2 >= 10, we actually wanted to add its cross sum
                # As 0 <= digit <= 9, we know that 0 <= 2 * digit <= 18
                # For a number x in [10, 18], its crosssum is equal to x - 9
                sum -= 9

        else:
            sum += digit

    return (10 - sum) % 10

def luhn(s):
    '''Validates a Luhn checksum

    The check digit is assumed to be in the last position.

    Input:
      s: String representation of base-10 number which to verify.

    Raises:
      ArgumentError: If input is not a number, or too short.

    Returns:
      bool: Indicating whether input's last digit was a valid Luhn checksum
    '''
    if len(s) < 2:
        raise ValueError(f"Passed value was too short: {s}")

    try:
        int(s)
    except ValueError:
        raise ValueError(f"Passed value was not a valid base-10 number: {s}")

    # We'll assume that the checksum digit is the last digit
    digit_str, checksum = s[0:-1], s[-1]
    actual_checksum = calculate_luhn_checksum(digit_str)

    return actual_checksum == int(checksum)

def luhn_cycle_walk(cycle, s):
    '''Cycle-walk algorithm to find Luhn-checksumed numbers.

    Input:
      cycle: Function which takes a bytes object, and outputs next element on cycle
      s: string representation of number to use as starting point

    Returns:
      bytes: Next element on cycle
    '''

    n = len(s)
    input_bytes = s.encode('ascii')

    while True:
        input_bytes = cycle(input_bytes)

        # Interpret digest bytes as big-endian integer, reduce to an appropriate length
        # This is safe as SHA256's output is (conjectured to be)
        # indistinguishable from uniform random.
        candidate = str(int.from_bytes(input_bytes, "big") % 10**n)

        # If we got a valid Luhn-checksumed number, return it. Else continue
        # trying.
        if luhn(candidate):
            return candidate
