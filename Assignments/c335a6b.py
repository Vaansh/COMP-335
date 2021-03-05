import nltk
# defining Contex Free Grammar
grammar = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
  """)

sentence = 'the angry bear chased the frightened little squirrel'.split()


def parse(sent):
    # Returns nltk.Tree.Tree format output
    a = []
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(sent):
        a.append(tree)
    return(a[0])


# Gives output as structured tree
print(parse(sentence))

# Gives tree diagrem in tkinter window
parse(sentence).draw()
