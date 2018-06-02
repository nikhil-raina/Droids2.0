import dataFetch as data

if __name__ == '__main__':
    labelList = 'CA'
    atomLabel_withList = data.getData("CFTRdata\\atomflux_CFTRmutation\\DROIDSfluctuation_1.txt", labelList)