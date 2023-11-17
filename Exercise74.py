print("    ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
for i in range(1, 11):
    print(f"{i:4}", end="")
    for j in range(1, 11):
        result = i * j
        print(f"{result:4}", end="")
    print()