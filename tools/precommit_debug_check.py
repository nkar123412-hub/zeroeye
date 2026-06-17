import os
import re
import sys

# Patterns that indicate debug prints should be removed before committing
DEBUG_PATTERNS = {
    "python": [r"print\(.*DEBUG.*\)", r"import pdb", r"breakpoint\(\)"],
    "rust": [r"println!\(\s*.*DEBUG.*\)", r"dbg!\("],
    "go": [r"fmt\.Printf\(.*DEBUG.*\)", r"log\.Printf\(.*DEBUG.*\)"],
    "typescript": [r"console\.log\(.*DEBUG.*\)", r"console\.debug\(.*\)"],
    "cpp": [r"std::cout\s*<<\s*.*DEBUG.*", r"printf\(.*DEBUG.*\)"],
}

FILE_EXTENSIONS = {
    ".py": "python",
    ".rs": "rust",
    ".go": "go",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".h": "cpp",
    ".c": "cpp",
}

def check_file(filepath):
    ext = os.path.splitext(filepath)[1]
    if ext not in FILE_EXTENSIONS:
        return []

    lang = FILE_EXTENSIONS[ext]
    patterns = DEBUG_PATTERNS.get(lang, [])
    findings = []

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    findings.append(f"Line {line_num}: {line.strip()}")
    
    return findings

def main():
    files_to_check = sys.argv[1:]
    all_findings = {}

    for filepath in files_to_check:
        if os.path.isfile(filepath):
            findings = check_file(filepath)
            if findings:
                all_findings[filepath] = findings

    if all_findings:
        print("\n❌ Pre-commit check failed: Debug prints detected!\n")
        for filepath, findings in all_findings.items():
            print(f"File: {filepath}")
            for finding in findings:
                print(f"  {finding}")
        print("\nPlease remove debug prints or mark them as intentional before committing.\n")
        sys.exit(1)
    
    print("✅ No debug prints found. Ready to commit!")
    sys.exit(0)

if __name__ == "__main__":
    main()
