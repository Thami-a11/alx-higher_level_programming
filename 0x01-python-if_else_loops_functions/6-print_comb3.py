for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i:02d}, {j:02d}", end=", " * (j < 9) or "\n")
