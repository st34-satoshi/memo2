# copy from https://en.wikipedia.org/wiki/Performance_rating_(chess)

def expected_score(opponent_ratings: list[float], own_rating: float) -> float:
    """How many points we expect to score in a tourney with these opponents"""
    return sum(
        1 / (1 + 10**((opponent_rating - own_rating) / 400))
        for opponent_rating in opponent_ratings
    )


def performance_rating(opponent_ratings: list[float], score: float) -> int:
    """Calculate mathematically perfect performance rating with binary search"""
    lo, hi = 0, 4000

    while hi - lo > 0.001:
        mid = (lo + hi) / 2

        if expected_score(opponent_ratings, mid) < score:
            lo = mid
        else:
            hi = mid

    return round(mid)

if __name__ == "__main__":
    print(performance_rating([1851, 2457, 1989, 2379, 2407], 4))  # should be 2551
    # print(performance_rating([1173, 1466, 1656, 1539, 1804], 4))
    print(performance_rating([1334, 1466, 1656, 1539, 1804], 4))