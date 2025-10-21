def gb2byte(n: float) -> int:
    """Преобразует гигабайты (GB) в байты (B)."""
    return int(n * 1024**3)


def tb2byte(n: float) -> int:
    """Преобразует терабайты (TB) в байты (B)."""
    return gb2byte(n * 1024)


def byte2gb(n: int) -> float:
    """Преобразует байты (B) в гигабайты (GB)."""
    return n / 1024**3


def byte2tb(n: int) -> float:
    """Преобразует байты (B) в терабайты (TB)."""
    return n / 1024**4
