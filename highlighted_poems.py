highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# 
print(highlighted_poems)
# highlighted_poems_list = highlighted_poems.replace(",", " ")
# highlighted_poems_list = highlighted_poems_list.strip(" ")
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip(" "))

print(highlighted_poems_stripped)

highlighted_poems_details = []
for split_poem in highlighted_poems_stripped:
    highlighted_poems_details.append(split_poem.split(":"))

print(highlighted_poems_details)

titles = []
poets = []
dates = []

for detailed_item in highlighted_poems_details:
    titles.append(detailed_item[0])
    poets.append(detailed_item[1])
    dates.append(detailed_item[2])

for detailed_item in highlighted_poems_details:
    txt = "The poem {} was published by {} in {}."
    print(txt.format(detailed_item[0], detailed_item[1], detailed_item[2]))








