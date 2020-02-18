def dna_counts(the_file_name, your_name = "user"):
    dna_file = open(the_file_name,"r")

    dna_data = [] 
    for line in dna_file: 
        line = line.rstrip() 
        dna_data += [line]
        
    dna_file.close()      
    
    print("Hello " + your_name)
    
    no_of_sequences = len(dna_data)   
    print("There are " + str(no_of_sequences) + " sequences in this file")  

    bp_count = []      
    for xyz in dna_data: 
        bp_count += [len(xyz)] 

    print("The average length is " + str(sum(bp_count)/no_of_sequences) + " basepairs")
    print("The longest sequence is " + str(max(bp_count)) + " basepairs")
    print("The shortest sequence is " + str(min(bp_count)) + " basepairs")    
    
    import matplotlib.pyplot as plt

    nuc_count = []
    for xyz in dna_data:
        nuc = {"a":xyz.count("a"),"t":xyz.count("t"),"c":xyz.count("c"),"g":xyz.count("g")}
        nuc_count += [nuc]

    x0 = [1.0,2.0,3.0,4.0]
    gene0 = nuc_count[0].values()
    plt.bar( x0,gene0 ,width=.25)

    x1 = [1.25,2.25,3.25,4.25]
    gene1 = nuc_count[1].values()
    plt.bar(x1, gene1,width=.25)

    x2 = [1.5,2.5,3.5,4.5]
    gene2 = nuc_count[2].values()
    plt.bar(x2,gene2,width=.25)

    plt.xticks(x1 , ('a', 't', 'c', 'g'))

    plt.ylabel('Nucleotide count')
    plt.title('Nucleotide per sequence')
    plt.legend(labels = ["gene1","gene2","gene3"],loc='best')   
        