import hashlib
from . import names

LANGUAGES = {
    'default': {
        "en": (names.EN_ADJECTIVES, names.EN_NOUNS, names.EN_GENDER),
        "ua": (names.UA_ADJECTIVES, names.UA_NOUNS, names.UA_GENDER)
    },
    'business': {
        "en": (names.EN_ADJECTIVES_BUSINESS, names.EN_NOUNS_BUSINESS, names.EN_GENDER_BUSINESS),
        "ua": (names.UA_ADJECTIVES_BUSINESS, names.UA_NOUNS_BUSINESS, names.UA_GENDER_BUSINESS)
    },
    'market': {
        "en": (names.EN_ADJECTIVES_MARKET, names.EN_NOUNS_MARKET, names.EN_GENDER_MARKET),
        "ua": (names.UA_ADJECTIVES_MARKET, names.UA_NOUNS_MARKET, names.UA_GENDER_MARKET)
    }
}

def pseudonym(seed: str, language: str = "en", theme: str = 'default') -> str:
    """
    Generate a pseudonym based on a seed string and language.

    Args:
        seed (str): The input seed string.
        language (str): The language code ("en" for English, "ua" for Ukrainian).
        theme (str): The theme for the pseudonym ("default", "business", or "market").

    Returns:
        str: A pseudonym in the format "Adjective Noun".
    """
    if language not in LANGUAGES[theme]:
        raise ValueError(f"Unsupported language: {language}")

    adjectives, nouns, gender = LANGUAGES[theme][language]

    # Hash the seed using SHA-256
    hash_bytes = hashlib.sha256(seed.encode('utf-8')).digest()
    number = int.from_bytes(hash_bytes, byteorder="big")

    # Convert the first two bytes of the hash to indices
    adjective_index = number % len(adjectives['M'])
    noun_index = (number // len(adjectives['M'])) % len(nouns)
    gender_index = gender[noun_index]

    # Select the adjective and noun
    adjective = adjectives[gender_index][adjective_index]
    noun = nouns[noun_index]

    # Combine into a pseudonym
    return f"{adjective} {noun}"

# Example usage
if __name__ == "__main__":

    print("Testing 'market' theme in English:")
    for i in range(20):
        print(pseudonym(f"test-{i}", 'en', 'market'))

    print("\nTesting 'market' theme in Ukrainian:")
    for i in range(20):
        print(pseudonym(f"test-{i}", 'ua', 'market'))
