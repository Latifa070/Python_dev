def sandwich_items(*items):
    print(f"Your sandwich contains: ")
    for item in items:
        print(f"- {item}")


sandwich_items("bread","protein", "cheeses", "fresh vegetables")
sandwich_items("bread","protein", "cheeses")
sandwich_items("bread","protein", "fresh vegetables")