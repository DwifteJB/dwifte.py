from py7zip import *

# compress_files/folders
file = compress()
file.archive_file("example.txt", "example_compressed")

file = compress()
file.archive_folder("example_folder", "example_folder_compressed")

# compress with password
file = compress()
file.archive_file("example.txt", "example_pass", "example")

# extract
file = extract()
file.extract("example_compressed")

file = extract()
file.extract_folder("example_folder_compressed", "example_out")

# extracting with password
file = extract()
file.extract("example_pass", "example")

# creat sfx archive
file = sfx()
file.creat("example", "example_sfx")