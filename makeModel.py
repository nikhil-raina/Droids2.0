import dataFetch as data

if __name__ == '__main__':
    labelList = 'CA O N'
    atomLabel_withList, missingLabels = data.getData("CFTRdata\\atomflux_CFTRmutation\\DROIDSfluctuation_1.txt", labelList)

    for key, val in atomLabel_withList.items():
        print(key, ':', val)

    print()
    print('The following atoms are missing from the dictionary:')
    if missingLabels.__len__() == 0:
        print('0')
    else:
        for labels in missingLabels:
            print(labels)