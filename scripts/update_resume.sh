#!/usr/bin/env bash
set -euo pipefail

# Download latest resume in markdown format.
rm -f resume_raw.md
wget -O resume_raw.md https://raw.githubusercontent.com/buyuk-dev/resume/master/resume.md

echo "wget returned $?"

# Convert LaTeX-flavored markdown to Jekyll-compatible markdown
python3 scripts/convert_resume.py resume_raw.md resume.md

# Clean up
rm -f resume_raw.md

echo "Conversion complete."
