# Dracula

Find and Replace

1. find`&` replace with `&amp;`

### Chapter headings
1. find `(?m)^CHAPTER ([IVXLC]+)` replace `<chapter num="\1">CHAPTER \1</chapter>`

### pargraphs
1. find `(\r?\n){2,}` replace `</p><p>`

### journal entries
1. find `(?m)^(.*?)’s Journal` replace `<journal author="\1">\1’s Journal</journal>`

### months
1. find `(?m)(\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th)?)` replace `<date>\1</date>`

### quotes
1. find `"([^"]+)"` replace `<quote>\1</quote>`
