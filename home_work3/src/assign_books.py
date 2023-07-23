import json, csv, argparse;
from pathlib import Path;

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--source_directory",
    nargs="?",
    default = Path(__file__).parent.absolute() / 'data_source',
    required=False)
parsed_path = parser.parse_args()
sourcedata_directory_path = Path(parsed_path.source_directory)

users_file_name = 'users.json'
books_file_name = 'books.csv'
users_file_path = sourcedata_directory_path / users_file_name
books_file_path = sourcedata_directory_path / books_file_name

if not users_file_path.exists() or not books_file_path.exists():
    print(f"Source directory doesnt contain {users_file_path} and {books_file_name}")
    raise SystemExit(1)

result_file_name = 'result.json'
result_file_directory = Path(__file__).parent.absolute() / 'exported_data'
result_file_path = result_file_directory / result_file_name

# read users first
try:
    print(f"Now opening: {users_file_path.resolve()}")
    with open(users_file_path.resolve(), 'r') as read_file:
        users = json.load(read_file)
        print(f"{users_file_path.name} was loaded successfully!")
except OSError as e:
    print (f"Unable to open {users_file_path.resolve()}: {e}")

# read books

try:
    print(f"Now opening: {books_file_path.resolve()}")
    with open(books_file_path.resolve(), 'r') as books_file:
        books = list(csv.reader(books_file, delimiter=','))
        print(f"{books_file_path.name} was loaded successfully!")
except OSError as e:
    print (f"Unable to open {books_file_path.resolve()}: {e}")

# filter the user list just for specific keys, not all originally needed
user_reduced_keys = ('name', 'gender', 'address', 'age')
users_reduced_data = [{key: value for key, value in user.items() if key in user_reduced_keys} for user in users]
total_users = len(users_reduced_data)

# convert csv data to list of disctionaries
# make all keys lower, as original column name in CSV may contain uppercase
# create list of keys from first row in csv reader
books_keys = [k.lower() for k in books[0]]
# create list of values
books_list_values = [books[i] for i in range(1, len(books))]
# create list of dictionaries from 2 lists
books_list_dic = [{key: value for key, value in zip(books_keys, books_list_values[i])} for i in range(len(books_list_values))]

book_reduced_keys = ('title', 'author','genre','pages')
books_reduced_data = [{key: value for key, value in book.items() if key in book_reduced_keys} for book in books_list_dic]
total_books = len(books_reduced_data)
if(total_books < total_users):
    print (f"Books: {total_books} less then Users: {total_users}, \n"
           f" Cannot assign Books, so Exiting")
    raise SystemExit(1)

books_per_user_eq = total_books // total_users
# create new list to store dictionaries of books per user
books_per_user = []
# step1 - distribute books equally
book_index = 0
for user_index in range(total_users):
    books_per_user.append([books_reduced_data[i] for i in range(book_index, book_index + books_per_user_eq)])
    # shift index to the next chunk of books
    book_index = book_index + books_per_user_eq
# step2 - distibute left books
user_index = 0
for left_books_index in range (book_index, total_books):
    books_per_user[user_index].append(books_reduced_data[left_books_index])
    # shift user_index to the next user
    user_index = user_index + 1

# append books dictionary to users
final_data = [{**users_reduced_data[i], 'books' : books_per_user[i]} for i in range (total_users)]

result_file_directory.mkdir(parents=True, exist_ok=True)

with open(result_file_path.resolve(), "w") as result_file:
    json.dump(final_data, result_file)

print(f"The job is done! \n Result file: {result_file_path.resolve()}")
