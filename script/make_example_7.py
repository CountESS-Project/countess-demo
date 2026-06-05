import random
random.seed(1)

print("replicate,timepoint,barcode,sequence,count")

stop_codons = ['TAA','TAG','TGA']
reference = "ATG"
for _ in range(0,20):
    codon = ''.join(random.choices("ACGT", k=3))
    if codon not in stop_codons:
        reference += codon
reference += random.choice(stop_codons)

sequences = [
    reference[0:offset] + random.choice("ACGT") + reference[offset+1:]
    for offset in random.choices(range(0,len(reference)), k=500)
]

seqscores = {
    seq: random.uniform(0.9,1) if seq == reference else random.uniform(0,1)
    for seq in sequences
}

barcodes = {
    ''.join(random.choices("ACGT", k=20)): random.choice(sequences)
    for _ in range(0,5000)
}

for rep in range(1,5):
    barcounts = { bar: int(random.randint(500,5000)) for bar in barcodes.keys() }
    for time in range(0,6):
        for bar, count in barcounts.items():
            seq = barcodes[bar]
            print(f"{rep},{time},{bar},{seq},{count}")
            barcounts[bar] = int(count * random.uniform(seqscores[seq]*0.9, seqscores[seq]*1.1))
