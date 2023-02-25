def make_sandwiche(*items):
    """Summarize the sandwich we are about to make."""
    print(f"\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


make_sandwiche('plate', 'knief', 'bread', 'mayo', 'egg salad', 'lettuce')
make_sandwiche('plate', 'knief', 'french bread', 'mustard', 'deli meat')
make_sandwiche('plate', 'knief', 'bread', 'peanut butter', 'jelly')
