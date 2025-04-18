
from pseudomatic import pseudonym


def main():
    print("Testing 'market' theme in English:")
    for i in range(20):
        print(pseudonym(f"test-{i}", 'en', 'market'))

    print("\nTesting 'market' theme in Ukrainian:")
    for i in range(20):
        print(pseudonym(f"test-{i}", 'ua', 'market'))

if __name__ == "__main__":
    main()