# From in class 10/21: 

Notes from the los ago xml file: 

1. goes up the parent line : `floatingText/parent::*` or `floatingText/..`
1. goes through the parent line but finds the names of those parents : `floatingText/parent::* | name()`
1. going through descendents : `descendents::cbml:panel/child::floatingText`
1. text is a node, imedeant child `floatingText/text()`
1. gets all the text : `floatingText ! string()`
1. gets all the text like the string but removes the extra spaces : `floatingText ! normalized-space`
1. gets all the string lengths without the spaces : `floatingText ! normalized-space() ! string-length()`
1. gets you all values : `//cbml:panel/@characters =>distinct-values()`


Notes from the going over XPath Exercise 3 - Mitford Project:
1. always start with the div and slowly look through the xml document
1. `//div[@type="historical_people"]`
1. `//div[@type="historical_people"]/*`
1. `//div/* ! name()` and to get no duplicates `/div/* ! name() => distinct-values()`
1. and to get into more specifics add count or sort to the end `//div/* ! name() => distinct-values() => count()` or `//div/* ! name() => distinct-values() => sort()`
1. can use the wild card or the item tags interchangable
1. `//div/list[@sortKey="animals"]/* => count()` or `//div/list[@sortKey="animals"]/item => count()`
1. last finds the last element wrapped `//div/list[@sortKey="animals"]/item[last()]`
1. `//div/list[@sortKey="planets"]/*[5]`
1. gets the frist 6 items in the planets list `//div/list[@sortKey="planets"]/*position() le 6` or `//div/list[@sortKey="planets"]/*position() => [6]` or `//div/list[@sortKey="planets"]/*position() < 7` 
1. gets the fourth item in the planets list `//div/list[@sortKey="planets"]/*position() = 4` or `//div/list[@sortKey="planets"]/*position() [4]`
1. gets you all the occupations `//person/occupation[1]`
1. gets the first occupation in the xml document `(//person/occupation[1])`