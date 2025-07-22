import hashlib
import strings_utils


def get_file():
    file_paths = input('File path: ').strip().lower().split(',')

    files = []
    
    for file_path in file_paths:
        with open (file_path, 'rb') as file:
            files.append(file.read())
        
    return files, file_paths


# Function for user's algorithm choice
def get_hash_algorithm():
    hash_algorithms = list(hashlib.algorithms_available)
    hash_algorithms.sort()
    
    while True:
        try:
            print(f'\n{strings_utils.separator}\n')
            for hash_algorithm in hash_algorithms:

                print(f'{(hash_algorithms.index(hash_algorithm)) + 1}. {hash_algorithm} ')

            input_hash_algorithm_choice = int(input(f'Choose a hashing algorithm (1-{len(hash_algorithms)}): '))

            hash_algorithm = hash_algorithms[input_hash_algorithm_choice-1]

        except IndexError:
            print(f"\n{strings_utils.error_message} Invalid choice.\n")
            continue

        return hash_algorithm
#####


def calculate_file_hash():

    files, file_paths = get_file()
    hash_algorithm = get_hash_algorithm()

    for file_path, file in zip(file_paths, files):
        calculated_file_hash = getattr(hashlib, hash_algorithm)(file).hexdigest()


        print(f'{file_path}: {calculated_file_hash}')

calculate_file_hash()

# TO DO: print file hex.
def get_file_hex():
    pass

