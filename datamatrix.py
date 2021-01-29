def datamatrix(data,name,i,month):
    A = []
    A.append(int(data['player'][i][name][month]['data']['R']))
    A.append(int(data['player'][i][name][month]['data']['AB']))
    A.append(int(data['player'][i][name][month]['data']['RBI']))
    A.append(int(data['player'][i][name][month]['data']['H']))
    A.append(int(data['player'][i][name][month]['data']['HR']))
    A.append(int(data['player'][i][name][month]['data']['BB']))
    A.append(int(data['player'][i][name][month]['data']['SB']))
    return(A)

def datamatrix1(data,name,i,month):
    A = []
    A.append(float(data['player'][i][name][month]['data']['IP']))
    A.append(int(data['player'][i][name][month]['data']['W']))
    A.append(int(data['player'][i][name][month]['data']['L']))
    A.append(int(data['player'][i][name][month]['data']['SV']))
    A.append(int(data['player'][i][name][month]['data']['SO']))
    A.append(int(data['player'][i][name][month]['data']['BB']))
    A.append(int(data['player'][i][name][month]['data']['HLD']))
    A.append(int(data['player'][i][name][month]['data']['R']))
    return(A)