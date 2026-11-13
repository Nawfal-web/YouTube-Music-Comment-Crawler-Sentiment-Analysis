from dataset_analysis import analyze_dataset


def compare_datasets(file1, file2):

    print("\n=== Comparing Datasets ===")

    result1 = analyze_dataset(file1)
    result2 = analyze_dataset(file2)

    print("\n=== FINAL COMPARISON ===")

    print("\nDataset 1:")
    print(result1)

    print("\nDataset 2:")
    print(result2)

    pos1 = result1.get("Positive", 0)
    pos2 = result2.get("Positive", 0)

    if pos1 > pos2:
        print("\nDataset 1 is more positively received.")
    elif pos1 < pos2:
        print("\nDataset 2 is more positively received.")
    else:
        print("\nBoth datasets have similar sentiment.")


if __name__ == "__main__":

    compare_datasets(
        "dataset/billie_jean.csv",
    )