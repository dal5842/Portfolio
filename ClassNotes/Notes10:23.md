# In class notes 10/23

1. `//list[@sortKey="plants"]/item[position()=6]` gets the plant in the 6th position
1. `//list[@sortKey="plants"]/item[position() =< 6]` gets the first 5 planets
1. `//list[@sortKey="plants"]/item[position() >= last() -6 ]` gets the last 5 plants

# From homework exercise 4

1. `//div/count()`
1. `//div/*`
1. `//div/* ! name() => distinct-values()`
1. `//div/count(*)`
1. `//div/*/count(*)` this steps down and counts all the children in that level.
1. `min(//div/*/count(*))` gets the min
1. `//div/*/count(*) => max()` gets the max
1. `//div[/*count(*) = //div/*/count(*) => max()]` gets where the max is true if you did not know the max
1. `//occupation/@type => distinct-values()` 
1. `count(distinct-values(//occupation/@type))` or `//occupation/@type => distinct-values() => count()`
1. `//person[occupation[@type="artist"]]`
1. `//person[@sex="f" and occupation[@type="artist"]]`
1. `//person[occupation[@type="artist" and @subtype="engraver"]]`
1. `//