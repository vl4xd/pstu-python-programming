def FindDivisors(n: int) -> list[int]:
    """Находит все делители числа n оптимизированным способом"""

    try:
        n = int(n)
    except ValueError:
        raise ValueError("Number must be an integer.")

    if n < 0:
        raise ValueError("Number must be > 0.")

    divisors = []
    i = 1
    # Идем до корня из n
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            # Добавляем парный делитель (кроме случая, когда i = n/i)
            if i != n // i:
                divisors.append(n // i)
        i += 1

    return sorted(divisors)


def IsNumberSimple(divisors: list[int]) -> bool:
    if len(divisors) == 2:
        return True
    return False


def IsNumberPerfect(number: int, divisors: list[int]) -> bool:
    check_number = sum(divisors) - number
    if number == check_number:
        return True
    return False


def GetStringSumDivisors(divisors: list[int]) -> str:
    divisors.pop()
    string = "+".join(map(str, divisors))
    sum_divisors = sum(divisors)
    string += f"={sum_divisors}"
    return string