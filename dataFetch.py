def getData(fileName, reqLabelList):
    '''
    Gets the data from the specific file by selecting the specified
    atoms entered by the user.
    :param fileName: Name of the file to look for the Data
    :param reqLabelList: Name of all the atoms that are required for the modelling
    :return: A tuple containing a dictionary of atoms, as the keys, and
            list of flux_ref as the values, and the labels missing from the model.
    '''

    file = open(fileName, "r")
    listLabels = reqLabelList.split()   # the seperate atoms
    numFlex_ref = list()
    missingLabel = list()
    atomLabel = dict()
    file.__next__()
    for line in file:
        words = line.split()
        if words[5] in listLabels:
            if words[5] not in atomLabel.keys():
                numFlex_ref = list()
                atomLabel[words[5]] = numFlex_ref
            numFlex_ref.append(words[6])
        else:
            if words[5] not in missingLabel:
                missingLabel.append(words[5])
    return atomLabel, missingLabel
