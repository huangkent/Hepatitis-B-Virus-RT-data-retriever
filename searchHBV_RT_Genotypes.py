def collectGenotypeData(datafileName):   # retrieve the genotypes of HBV RT   datafile = file(datafileName)      filename = 'HBV RT genotypes info.txt'   genotypeFile = open(filename, 'w')   IsolateID = 0   for line in datafile:      if 'PUBMED' in line:         IsolateID = IsolateID + 1                  Genotype = ''              # retrieve the genotype         for line in datafile:            if 'genotype' in line:               index = 0               while line[index] != 'g':                  index = index + 1               Genotype = line[index + 10]               break            elif '//' in line:               break    # the info of the HBV RT is fully gone over         # record the sequence         record = str(IsolateID) + '##' + Genotype + '\n'         genotypeFile.write(record)   genotypeFile.close()if __name__ == "__main__":       collectGenotypeData('HBV RT sequences.txt')