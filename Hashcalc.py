import hashlib

def calculate_hash(file_path, algorithm="md5"):
    """
    Calculate the hash (MD5 or SHA256) of a file.
    """
    hash_function = hashlib.md5() if algorithm.lower() == "md5" else hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_function.update(chunk)

    return hash_function.hexdigest()

def compare_hashes(hash1, hash2):
    """
    Compare two hashes and determine if they are the same.
    """
    return hash1 == hash2

def main():
    print("File Comparison by Hash")

    # Get user input
    user_choice = input("Do you want to input hashes manually? (yes/no): ").lower()

    if user_choice == "yes":
        hash_algorithm = input("Enter the hash algorithm (md5/sha256): ")
        hash1 = input(f"Enter the first {hash_algorithm.upper()} hash: ")
        hash2 = input(f"Enter the second {hash_algorithm.upper()} hash: ")
    else:
        hash_algorithm = input("Enter the hash algorithm (md5/sha256): ")
        file_path1 = input("Enter the path of the first file: ")
        file_path2 = input("Enter the path of the second file: ")

        hash1 = calculate_hash(file_path1, hash_algorithm)
        hash2 = calculate_hash(file_path2, hash_algorithm)

    print(f"\n{hash_algorithm.upper()} Hash of File 1: {hash1}")
    print(f"{hash_algorithm.upper()} Hash of File 2: {hash2}")

    # Compare hashes
    if compare_hashes(hash1, hash2):
        print("\nHashes are identical.")
    else:
        print("\nHashes are different.")

if __name__ == "__main__":
    main()
