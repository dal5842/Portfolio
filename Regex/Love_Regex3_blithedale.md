# Blithedale Regex Notes

## Reserved Charcters
First I looked for all the reserved characters which led to no results for all three.
1. Find `&` Replace `&amp;`
1. Find `<` Replace `&lt;`
1. Find `>` Replace `&gt;`

## Remove Extra Blank Lines
Next I looked for blank lines there was 48 results
1. Find `\n{3,}` Replace `\n\n`

## Mark Paragraphs
Third I looked to mark the paragraphs which gave 993 matches
1. Find `\n\n` Replace `</p>\n<p>`

## Identify and Mark Chapter Titles
Next I looked to mark the chapter titles and found 29 matches
1. Find `^<p>([IVXLC]+\. .+)</p>$` Replace `<title>\1</title>`

## Wrap Chapters in `<chapter>` Tags
Next I wrapped the chapter titles which gave me a 29 result match again
1. Find `(<title>.+?</title>)` Replace `</chapter>\n<chapter>\n\1`

## Auto-Tag Quoted Passages
Next I looked for the quoted sections and got a match of 913.
1. Find`"([^"]+)"` Replace `<quote>\1</quote>`

## Fixings
Last I just did some cleaning of the xml document
1. adding root
1. adding title
1. adding author
1. adding a TOC (table of contents)
1. removed the random start and end tags not used/closed or open.