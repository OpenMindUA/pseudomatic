
from pseudomatic import pseudonym


def main():
    print("Testing 'retail' theme in English:")
    for i in range(20):
        print(pseudonym(f"test-{i}", 'en', 'retail'))

    print("\nTesting 'retail' theme in Ukrainian:")
    for i in range(20):
        print(pseudonym(f"test-{i}", 'ua', 'retail'))

if __name__ == "__main__":
    main()
