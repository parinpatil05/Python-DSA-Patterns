def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for _ in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second


steps = 5

print("Ways to Climb Stairs:",
      climb_stairs(steps))
