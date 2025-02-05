# Regex Exercise 2 Sonnet Notes


## First I ran the three main find and replaces
1. find `&` replace `&amp;`
1. find `<` replace `&lt;`
1. find `>` replace `&gt;`

No results where found from these three find and replace

## First to remove the leading spaces:
1. Find `^ +  ` replace it with an empty string

### Explanation - 
1. `^` finds only the start of the line.
1.  `+` finds one or more spaces.
1. Replacing it with nothing removes unwanted indentation.

## Wrap Each Line in `<line>` Tags:
1. Find `^(.+)$` replace with `<line>\1</line>`

### Explanation
1. `^(.+)$` this gets all non empty lines while avoiding blank lines
1. `\1` re-inserts the found text within <line> tags

## Convert Roman Numerals to <sonnet number="X"> Format (I am having issues with this one)
1. Find `<line>([IVXLCDM]+)</line>` replace `</sonnet>\n<sonnet number="\1">`

### Explanation
1. I though the find would work but it does not.

## Remove Extra Blank Lines
1. Find `\n{2,}` replace `\n`

### Explanation
1. Finds two or more newlines that are blank and replaces them to just a single blank line.

## Lastly 
1. Manualing entering the root, author and title tags