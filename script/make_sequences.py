import random
random.seed(1)

sequences = [ ''.join(random.choices("ACGT", k=20)) for _ in range(0,1000) ]

sequences1 = [ s for s in sequences for _ in range(0, random.randint(1,101)) ]
random.shuffle(sequences1)

with open("sequences_1.csv", "w") as fh:
    fh.write("sequence,time\n")
    for s in sequences1:
        fh.write(f"{s},1\n")

sequences2 = random.sample(sequences1, k=len(sequences1)*3//4)

with open("sequences_2.csv", "w") as fh:
    fh.write("sequence,time\n")
    for s in sequences2:
        fh.write(f"{s},2\n")

bins = {1: [[], []], 2: [[], []], 3: [[], []], 4: [[], []]}
for sequence in sequences:
    val = random.uniform(1,4)
    for repl in [0,1]:
        for _ in range(0, random.randint(100,151)):
            binn = max(min(round(random.normalvariate(mu=val, sigma=1)),4),1)
            bins[binn][repl].append(sequence)

for binn, repls in bins.items():
    for repl, seqs in enumerate(repls,1):
        random.shuffle(seqs)
        with open(f"vampseq_{binn}_{repl}.fastq", "w") as fh:
            for n, s in enumerate(seqs):
                h = f"COUNTESS-TEST-DATA:{n}"
                q = ('ZZZZ' + 'XYZZY' * (len(s)//5))[:len(s)]
                fh.write(f"@{h}\n{s}\n+{h}\n{q}\n")

stop_codons = ['TAA','TAG','TGA']
reference = "ATG"
for _ in range(0,50):
    codon = ''.join(random.choices("ACGT", k=3))
    if codon not in stop_codons:
        reference += codon
reference += random.choice(stop_codons)

with open(f"barcodes.csv", "w") as fh:
    fh.write("barcode,sequence\n")
    for barcode in sequences:
        offset = random.randint(0,len(reference))
        sequence = reference[0:offset] + random.choice("ACGT") + reference[offset+1:]
        fh.write(f"{barcode},{sequence}\n")


