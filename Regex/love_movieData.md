# MovieData Regex Notes


## Step 1: Handling Special XML Characters

Before applying any transformations, we need to replace special XML-reserved characters to ensure well-formedness.

### Find and Replace Operations:

1. Find: `&` Replace with: `&amp;`
2. Look for `<` and `>` if found replace.

### Transformation Find and Replaces

1. Find: `^.+` Replace with: `<movie>\0</movie>`
2. Find: `(<movie>)(.+?)(\t)` Replace with: `\1<title>\2</title>\3`


Lastly add a root element around the entire document