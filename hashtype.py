import re

HASH_TYPES = {
    "MD5": re.compile(r"^[a-fA-F0-9]{32}$"),
    "SHA-1": re.compile(r"^[a-fA-F0-9]{40}$"),
    "SHA-256": re.compile(r"^[a-fA-F0-9]{64}$"),
    "SHA-512": re.compile(r"^[a-fA-F0-9]{128}$"),
}

def hash_type(hash_string):
    clean_hash = hash_string.strip()
    possible_types = []
    
    for hash_name, pattern in HASH_TYPES.items():
        if pattern.match(clean_hash):
            possible_types.append(hash_name)
            
    return possible_types

def main():
    print("====================================")
    print("     Python Hash Type Identifier     ")
    print("====================================")

    while True:
        user_input = input("Enter your hash: ")
        
        matches = hash_type(user_input)
        
        if matches:
            print(f"Possible Type(s): {', '.join(matches)}\n")
        else:
            print("Unknown Type (doesn't match MD5, SHA-1, SHA-256, or SHA-512)\n")

if __name__ == "__main__":
    main()
