import random

sequences = [ ''.join(random.choices("ACGT", k=20)) for _ in range(0,10000) ]

sequences1 = [ s for s in sequences for _ in range(0, random.randint(1,21)) ]
random.shuffle(sequences1)

with open("sequences1.csv", "w") as fh:
    fh.write("sequence,time\n")
    for s in sequences1:
        fh.write(f"{s},1\n")

sequences2 = random.sample(sequences1, k=len(sequences1)*3//4)

with open("sequences2.csv", "w") as fh:
    fh.write("sequence,time\n")
    for s in sequences2:
        fh.write(f"{s},2\n")
