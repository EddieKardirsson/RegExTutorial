import re

print('\n')

# Demo data
data = 'Welcome to this course on Regular Expressions! Today\'s date is the 28th of August.'

print(re.search('Welcome', data), '\n')
print(re.search('Welcome', data).group(), '\n')

print(re.findall('e', data), '\n')

# . Period metacharacter is a wild card. Can match any character except new line
print(re.search('.', data).group(), '\n')
print(re.search('t.', data).group(), '\n')
print(re.findall('t.', data), '\n')

# * Asterisk metacharacter matches the preceding character zero or more times
print(re.findall('t*o', data), '\n')
print(re.findall('s*i', data), '\n')

# + Plus metacharacter is similar to the asterisk, but it matches the preceding character one or more times.
print(re.findall('t+o', data), '\n')

# ? Question mark metacharacter matches either zero or one of the preceding character.
print(re.findall('s?i', data), '\n')

# Escape metacharacters (backslash) is used if you for example want to match a literal period or other special characters
print(re.findall('\.', data), '\n')

# Character classes

# [abc] - Brackets, to match multiple characters
print(re.findall('[abc]', data), '\n')

# [0-9] - Brackets with hyphens to set a specific range of characters to match
print(re.findall('[0-9]', data), '\n')
print(re.findall('[a-z]', data), '\n')
print(re.findall('[A-Za-z]', data), '\n')

# \d \w \s - Character class shorthands
print(re.findall('\d', data), '\n') # \d = numerical digits
print(re.findall('\w', data), '\n') # \w = characters part of a word, alphabetical
print(re.findall('\s', data), '\n') # \s = match whitespace characters

print(re.findall('\d+\w+\s', data), '\n')

# Anchors

# ^ - Caret symbol represents beginning of the string
print(re.findall('^\w*', data), '\n')

# $ - Dollar sign represents end of the string
print(re.findall('\w*.$', data), '\n')

# Get the first sentence of the string:
print(re.findall('^.*!', data), '\n')

# Quantifiers

# {n} - Basic quantifier. Match exactly n preceding tokens
print(re.findall('\w{3}', data), '\n')

# {n,} - Match at least n preceding tokens.
print(re.findall('\w{3,}', data), '\n')

# {n, m} - Match between n and m tokens.
print(re.findall('\w{2,3}', data), '\n')

# Match at least one of a word
print(re.findall('\w{1,}', data))
print(re.findall('\w+', data), '\n')

# Groups

# () (?:) - Form group by surrounding part of regular expression with parentheses.

# Capturing Groups
print(re.search('(\d+)(th)', data).groups(), '\n')

# Non-Capturing Groups
print(re.search('(?:\w+ \w+)', data).group(), '\n')
print(re.search('(?:\w+ \w+){3}', data).group(), '\n')

# Applying Conditional Logic
print(re.findall('(?:\w{7}|\w{4})', data), '\n')

# Capture the phone numbers from a string
test = """
(999)999-9999 fdesoifdsiohf893u92kjnskoflom+13(999)999-9999 
fioj2ji39010-3  
+124(99999)99-999-9999999-9'
"""

print(re.findall('(?:\+\d+)?\(\d+\)(?:\d+-)+\d+', test), '\n')

# Data Parsing

# Split up text into sentences and find senteces with numerical data in them
content = """
The term bristlecone pine covers three species of pine tree (family Pinaceae, genus Pinus, subsection Balfourianae). All three species are long-lived and highly resilient to harsh weather and bad soils. One of the three species, Pinus longaeva, is among the longest-lived life forms on Earth. The oldest of this species is more than 4,800 years old, making it the oldest known individual of any species.
Despite their potential age and low reproductive rate, bristlecone pines, particularly Pinus longaeva, are usually a first-succession species, tending to occupy new open ground. They generally compete poorly in less-than-harsh environments, making them hard to cultivate. In gardens, they succumb quickly to root rot. They do very well, however, where most other plants cannot even grow, such as in rocky dolomitic soils in areas with virtually no rainfall.
Bristlecone pines grow in scattered subalpine groves at high altitude in arid regions of the Western United States. Bristlecones, along with all related species in class Pinopsida, are cone-bearing seed plants commonly known as conifers; the name comes from the prickles on the female cones.
There are three closely related species of bristlecone pines:
At least some of the three species can hybridize in cultivation, but the ranges of wild populations do not overlap. The Colorado River and Green River produce a 160-mile (260 km) gap between the ranges of P. longaeva and P. aristata and the northern Owens Valley provides a 20-mile (30 km) gap between the ranges of P. longaeva and P. balfouriana.
Bristlecone pines grow in isolated groves just below the tree line, between 5,600 and 11,200 ft (1,700 and 3,400 m) elevation on dolomitic soils. The trees grow in soils that are shallow lithosols, usually derived from dolomite and sometimes limestone, and occasionally sandstone or quartzite soils. Dolomitic soils are alkaline, high in calcium and magnesium, and low in phosphorus. Those factors tend to exclude other plant species, allowing bristlecones to thrive. Because of cold temperatures, dry soils, high winds, and short growing seasons, the trees grow very slowly. Even the tree's needles, which grow in bunches of five, can remain on the tree for forty years, which gives the tree's terminal branches the unique appearance of a long bottle brush.
The bristlecone pine's root system is mostly composed of highly branched, shallow roots, while a few large, branching roots provide structural support.
The bristlecone pine is extremely drought tolerant due to its branched shallow root system, its waxy needles, and thick needle cuticles that aid in water retention.
The wood is very dense and resinous, and thus resistant to invasion by insects, fungi, and other potential pests. The tree's longevity is due in part to the wood's extreme durability. While other species of trees that grow nearby suffer rot, bare bristlecone pines can endure, even after death, often still standing on their roots, for many centuries. Exposed wood on living and dead trees does not rot, but rather erodes like stone due to wind, rain, and freezing, which creates unusual forms and shapes.
The bristlecone pine has an intrinsically low rate of reproduction and regeneration, and it is thought that under present climatic and environmental conditions the rate of regeneration may be insufficient to sustain its population. The species are on the International Union for Conservation of Nature (IUCN) red list. The species are labeled under Least Concern (LC), the justification for this being that no subpopulations for Great Basin bristlecone pines are decreasing. Subpopulations seem to be increasing or remaining stable. Many bristlecone pine habitats have been protected, including the Inyo National Forest's Ancient Bristlecone Pine Forest in the White Mountains of California and the Great Basin National Park in Nevada, where cutting or gathering wood is prohibited.
The green pine needles give the twisted branches a bottle-brush appearance. The needles of the tree surround the branch to an extent of about one foot near the tip of the limb. The name bristlecone pine refers to the dark purple female cones that bear incurved prickles on their surface. The dark color of these cones helps to absorb heat. After maturity, which takes about two years, the cones will become brown in color. These ancient trees have a gnarled and stunted appearance, especially those found at high altitudes, and have reddish-brown bark with deep fissures. As the tree ages, much of its vascular cambium layer may die. In very old specimens, often only a narrow strip of living tissue connects the roots to a handful of live branches. Even though the trees' needles may age, they still remain functional in regulating water and by their ability to photosynthesize.
Bristlecone pines are known for attaining great ages. The oldest bristlecone pine in the White Mountains is Methuselah, which has a verified age of 4,855 years. It is located in the Inyo National Forest in Eastern California.[citation needed] However, the specific location of Methuselah is a closely guarded secret.
The other two species, Pinus balfouriana and Pinus aristata, are also long-lived, though not to the extreme extent of P. longaeva; specimens of both have been measured or estimated to be up to 3,000 years old. The longevity of the trees is believed to be related to the proportion of dead wood to live wood. This high ratio reduces respiration and water loss, thereby extending the life of the tree.
Trees that reproduce by cloning can be considered to be much older than bristlecone pines. A colony of 47,000 quaking aspen trees (nicknamed "Pando"), covering 106 acres (43 ha) in the Fishlake National Forest in Utah, United States, has been estimated to be 80,000 years old, although tree ring samples date individual, above-ground trees at an average of about 130 years.
Bristlecone pines are invaluable to dendroclimatologists, because they provide the longest continual climatically sensitive tree-ring chronologies on Earth. By cross-dating millennia-old bristlecone pine debris, some chronologies reach beyond 9,000 years before present. In addition, ratios of stable carbon isotopes from bristlecone pine tree rings are sensitive to past variations in moisture availability. This information can be used to reconstruct precipitation changes in the past.
The Rocky Mountain population is severely threatened by an introduced fungal disease known as white pine blister rust, and by mountain pine beetles. Climate change may also affect the species as temperatures increased 0.5–1 °C (0.90–1.80 °F) over a 30-year period throughout the southern Rocky Mountain range. These changes in climate would mostly affect trees in higher elevations. With these problems, the genetic diversity within the species has become a concern; old specimens of bristlecone pine, however, have survived previous warmer periods.
"""

# Lookbehind and Lookahead to filter out species names and decimal numbers
sentences = re.split('(?<![A-Z])\.(?!\d)', content)
for s in sentences: print('TOKEN: ', s.strip(), '\n')
print()

final_data = []
for s in sentences:
    if re.search('\d', s):
        final_data.append(s.strip())
        print('DATA: ', s.strip(), '\n')