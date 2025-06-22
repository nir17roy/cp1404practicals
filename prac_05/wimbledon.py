"""
CP1404/CP5632 Practical
Wimbledon data analysis
"""

FILENAME = "wimbledon.csv"


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        champions = {}
        countries = set()

        for line in in_file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            champions[champion] = champions.get(champion, 0) + 1
            countries.add(country)

    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
