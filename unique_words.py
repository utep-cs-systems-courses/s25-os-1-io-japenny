import os, sys
import re, string

if len(sys.argv) != 3:
  print("Usage: python unique_words.py")
  sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Get file directory
filename = input_file
fd = os.open(filename, os.O_RDONLY)  
all_bytes = b''

# Read all text from
while True:
  read_bytes = os.read(fd, 1024)

  if not read_bytes:
    break

  all_bytes += read_bytes

# Clean text
pattern = f"[{re.escape(string.punctuation)}\\n]"
clean_text = re.sub(pattern, " ", all_bytes.decode('utf-8')).lower()
word_lst = clean_text.lower().split()
co_unique_words = dict()

# Get unique count of words
for word in word_lst:
  if word not in co_unique_words:
    co_unique_words[word] = 0
  co_unique_words[word] += 1

# Close file directory
os.fsync(fd)
os.close(fd)

# Create new file directory
new_filename = output_file
new_fd = os.open(new_filename, os.O_RDWR | os.O_CREAT)

# write unique word count to file
for word, count in co_unique_words.items():
    line = f"{word}: {count}\n".encode('utf-8')
    os.write(new_fd, line)

# close new file directory
os.fsync(new_fd)
os.close(new_fd)

