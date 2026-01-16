#!/usr/bin/env python3
"""
Fix blog post formatting in README files.
Ensures each blog post is on a separate line.
"""

import re
import sys

def fix_blog_format(filename):
    """Fix blog post formatting in a README file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find content between markers
        pattern = r'(<!-- BLOG-POST-LIST:START -->)(.*?)(<!-- BLOG-POST-LIST:END -->)'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print(f"Markers not found in {filename}")
            return False
        
        blog_content = match.group(2)
        
        # Check if posts are on the same line (missing newlines)
        # Pattern: "](...) - [" or "](...)- [" (with or without space before dash)
        if re.search(r'\]\([^\)]+\)\s*-\s*\[', blog_content):
            print(f"Found formatting issue in {filename}, fixing...")
            
            # Add newline before each "- [" that's not at the start of a line
            fixed_content = re.sub(r'(\]\([^\)]+\))\s*(-\s*\[)', r'\1\n\2', blog_content)
            
            # Ensure there's a newline after START marker
            if not fixed_content.startswith('\n'):
                fixed_content = '\n' + fixed_content
            
            # Ensure there's a newline before END marker
            if not fixed_content.endswith('\n'):
                fixed_content = fixed_content + '\n'
            
            # Reconstruct the file
            new_content = content[:match.start(2)] + fixed_content + content[match.end(2):]
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Fixed formatting in {filename}")
            return True
        else:
            print(f"✓ Format looks good in {filename}")
            return False
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False

if __name__ == "__main__":
    files = ["README.md", "README_CN.md"]
    fixed_any = False
    
    for filename in files:
        if fix_blog_format(filename):
            fixed_any = True
    
    if fixed_any:
        print("\n✓ Formatting fixes applied")
        sys.exit(0)
    else:
        print("\n✓ No formatting fixes needed")
        sys.exit(0)
