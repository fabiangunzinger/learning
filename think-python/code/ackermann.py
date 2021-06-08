
def ack(m, n):
    """Computes the Ackermann function A(m,n).
    
    Args:
      m, n: non-negative integers.
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

print(ack(3, 4))
