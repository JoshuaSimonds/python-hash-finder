import hashlib

algorithms = {
    "1": ("SHA-256", hashlib.sha256),
    "2": ("SHA-512", hashlib.sha512),
    "3": ("MD5", hashlib.md5),
    "4": ("SHA-1", hashlib.sha1)
}

while True:
    print("\n----Select a hashing algorithm----")
    for key, (name, _) in algorithms.items():
        print(f"[{key}] {name}")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice in algorithms:
        break  
    else:
        print("\n Invalid selection! Please enter a number between 1 and 4.")

algo_name, algo_function = algorithms[choice]

user_input = input(f"\nEnter the text to hash using {algo_name}: ")

encoded_text = user_input.encode()
hash_object = algo_function(encoded_text)
hex_dig = hash_object.hexdigest()

print(f"\n {algo_name} Hash:\n{hex_dig}")