# Download latest resume in markdown format.
rm -f resume.md
wget -O resume.md https://raw.githubusercontent.com/buyuk-dev/resume/master/resume.md

echo "wget returned $?"

# Define the string to prepend
read -r -d '' STRING_TO_PREPEND << 'EOF'
---
layout: page
title: Resume
permalink: /resume/
---
EOF

echo "Prepared prefix variable."

# Prepend the string to the downloaded file
echo "$STRING_TO_PREPEND" | cat - resume.md > temp.md && mv temp.md resume.md
