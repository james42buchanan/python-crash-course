from pathlib import Path

contents = (
Path('learning_python.txt')
 .read_text()
 .rstrip()
)

[print(line) for line in contents.splitlines()]