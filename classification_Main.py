import dataFetch as data
import createClassification as cc


if __name__ == '__main__':
    '''
    The main function that is called when the program is run.
    Prompts the user for the input of atoms. 
    It then displays the key : value pair of the atoms and the ref_flex numbers included
    with the atoms that were not asked for without their ref_flex values.
    
    Pre-required:   Atoms entered should be in CAPITAL. 
                    While entering the atoms, they should be separated with SPACE
                     
    '''
    labelList = input("Enter the needed atoms and separate it with a space:")
    #labelList = 'CA O N'
    atomLabel_withList, missingLabels = data.getData("CFTRdata\\atomflux_CFTRmutation\\DROIDSfluctuation_1.txt", labelList)

    # list to show the differentiation from atom to another atom
    diffLst = cc.makeDiff(labelList, atomLabel_withList)

    #######
    # calls the classification function.
    # Requires the X-coordinate list and the Y-coordinate list

    ##### LINE OF CODE COMMENTED OUT #####
    # cc.classification(X, Y, diffLst)

    # displays the dictionary of the atoms that are required.
    for key, val in atomLabel_withList.items():
        print(key, ':', val)

    print()
    print('The following atoms are missing from the dictionary:')
    if missingLabels.__len__() == 0:
        print('0')
    else:
        for labels in missingLabels:
            print(labels)



