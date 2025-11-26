#!/usr/bin/env python3
"""Convert LaTeX-flavored resume markdown to Jekyll-compatible markdown."""

import re
import sys


def convert_resume(content: str) -> str:
    """Convert LaTeX commands to clean markdown."""

    # Remove the YAML front matter with LaTeX header-includes
    # Match from start to the closing --- after header-includes
    content = re.sub(
        r'^---\n.*?^---\n',
        '',
        content,
        count=1,
        flags=re.MULTILINE | re.DOTALL
    )

    # Remove \vspace commands
    content = re.sub(r'\\vspace\{[^}]*\}', '', content)

    # Convert \href{url}{text} to [text](url) - do this BEFORE mbox removal
    content = re.sub(r'\\href\{([^}]*)\}\{([^}]*)\}', r'[\2](\1)', content)

    # Remove \mbox{...} but keep content (handles nested content like links)
    content = re.sub(r'\\mbox\{([^}]*)\}', r'\1', content)

    # Remove LaTeX begin/end center and minipage blocks
    content = re.sub(r'\\begin\{center\}', '', content)
    content = re.sub(r'\\end\{center\}', '', content)
    content = re.sub(r'\\begin\{minipage\}[^}]*\}[^}]*\}', '', content)
    content = re.sub(r'\\end\{minipage\}', '', content)
    content = re.sub(r'\\centering', '', content)

    # Convert skill pills to simple text badges
    # \pillcore{X}, \pilllang{X}, etc. -> just X
    content = re.sub(r'\\pill\w+\{([^}]*)\}', r'`\1`', content)

    # Convert \role{Company}{Title}{Dates} to markdown format
    def convert_role(match):
        company = match.group(1)
        title = match.group(2)
        dates = match.group(3)
        return f'### {company} — *{title}*\n**{dates}**\n'

    content = re.sub(
        r'\\role\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}',
        convert_role,
        content
    )

    # Convert \tech{...} to italic tech stack line
    content = re.sub(r'\\tech\{([^}]*)\}', r'*\1*', content)

    # Convert \edu{University}{Department}{Dates} to markdown format
    def convert_edu(match):
        university = match.group(1)
        department = match.group(2)
        dates = match.group(3)
        return f'### {university} — *{department}*\n**{dates}**\n'

    content = re.sub(
        r'\\edu\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}',
        convert_edu,
        content
    )

    # Convert \begin{itemize}...\end{itemize} with \item to markdown lists
    def convert_itemize(match):
        items_block = match.group(1)
        items = re.findall(r'\\item\s*(.+?)(?=\\item|$)', items_block, re.DOTALL)
        return '\n'.join(f'- {item.strip()}' for item in items) + '\n'

    content = re.sub(
        r'\\begin\{itemize\}(.*?)\\end\{itemize\}',
        convert_itemize,
        content,
        flags=re.DOTALL
    )

    # Convert + list items to - (standard markdown)
    content = re.sub(r'^\+ ', '- ', content, flags=re.MULTILINE)

    # Clean up escaped characters
    content = content.replace(r'\&', '&')
    content = content.replace(r'\#', '#')
    content = content.replace(r'C\#', 'C#')

    # Remove any remaining backslash commands we might have missed
    content = re.sub(r'\\[a-zA-Z]+\{[^}]*\}', '', content)
    content = re.sub(r'\\[a-zA-Z]+', '', content)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Trim leading/trailing whitespace
    content = content.strip()

    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: convert_resume.py <input_file> [output_file]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    converted = convert_resume(content)

    # Add Jekyll front matter
    jekyll_content = f"""---
layout: page
title: Resume
permalink: /resume/
---

# Michał Michalski
## CTO & Lead AI Software Engineer

Poznań, Poland | [michal@buyuk-dev.com](mailto:michal@buyuk-dev.com) | [buyuk-dev.com](https://buyuk-dev.com) | [+48 514 954 985](tel:+48514954985)

---

{converted}
"""

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(jekyll_content)
    else:
        print(jekyll_content)


if __name__ == '__main__':
    main()
