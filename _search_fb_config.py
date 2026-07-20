with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r"\bFB_CONFIG\b", content)]
for m in matches:
    # Print the line number and the line
    line_num = content[:m].count("\n") + 1
    line = content.split("\n")[line_num - 1]
    print(f"Line {line_num}: {line}")
