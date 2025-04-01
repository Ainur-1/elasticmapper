import re
import sys

def check_version(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        if not re.search(r'^## Version:\s*\d+\.\d+', content, re.MULTILINE):
            print(f"❌ Missing 'Version:' in {file_path}")
            sys.exit(1)

if __name__ == "__main__":
    check_version("README.md")