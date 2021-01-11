from py7zip import *

# compress_files/folders
file = compress()
file.archive_file("example.txt", "example_compressed")

file = compress()
file.archive_folder("example_folder", "example_folder_compressed")

#extract
file = extract()
file.extract("example_compressed")

file = extract()
file.extract_folder("example_folder_compressed", "example_out")