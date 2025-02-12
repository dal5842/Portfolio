# Mulan Regex Notes

## Reserved Charcters
First I looked for all the reserved characters which led to no results for all three.
1. Find `&` Replace `&amp;`
1. Find `<` Replace `&lt;`
1. Find `>` Replace `&gt;`

## Finding Chunks of Text
Next I looked for all the chunks of text broken up by blank lines which gave me 727 matches
1. Find `(?s)(?<=\n|\A)([^ \n][\s\S]*?)(?=\n\s*\n|\Z)` Replace `<sp>\1</sp>\n;`


### class notes:
`//sp[matches(.,'^.+?:')]` finds the speakers
`//sp[matches(.,'^[^:].+?$')]` finds speakers
'