def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a1 = len(s1)
    a2 = len(s2)
    a3 = len(s3)
    
    if a1 % 2 != 0:
        result = "[" + s1
    else:
        result = "[" + ''
    
    if a2 % 2 != 0:
        result += ', ' + s2
    else:
        result += ''
        
    if a3 % 2 != 0:
        result += ', ' + s3 + "]"
    else:
        result += ']'
    return result