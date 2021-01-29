def hitterdata(n,a,b,data):
    PA = AB = RBI = R = H = B2 = B3 = HR = TB = SO = SB = CS = AVG = SAC = SF = BB = IBB = HBP = GIDP = TP = LOB = PO = A = DP = TP = E = CS = PB = 0
    if n == 0:
        return PA ,AB ,RBI ,R ,H ,B2 ,B3 ,HR ,TB ,SO ,SB ,CS ,AVG ,SAC ,SF ,BB ,IBB ,HBP ,GIDP ,TP ,LOB ,PO ,A ,DP ,TP ,E ,CS ,PB
    else:
        for i in range(a,b+1):
            PA = PA + int(data[i].select('td')[2].text)
            AB = AB + int(data[i].select('td')[3].text)
            RBI = RBI + int(data[i].select('td')[4].text)
            R = R + int(data[i].select('td')[5].text)
            H = H + int(data[i].select('td')[6].text)
            B2 = B2 + int(data[i].select('td')[7].text)
            B3 = B3 + int(data[i].select('td')[8].text)
            HR = HR + int(data[i].select('td')[9].text)
            TB = TB + int(data[i].select('td')[10].text)
            SO = SO + int(data[i].select('td')[11].text)
            SB = SB + int(data[i].select('td')[12].text)
            CS = CS + int(data[i].select('td')[13].text)
            AVG = AVG + float(data[i].select('td')[14].text)
            SAC = SAC + int(data[i].select('td')[15].text)
            SF = SF + int(data[i].select('td')[16].text)
            BB = BB + int(data[i].select('td')[17].text)
            IBB = IBB + int(data[i].select('td')[18].text)
            HBP = HBP + int(data[i].select('td')[19].text)
            GIDP = GIDP + int(data[i].select('td')[20].text)
            TP = TP + int(data[i].select('td')[21].text)
            LOB = LOB + int(data[i].select('td')[22].text)
            PO = PO + int(data[i].select('td')[23].text)
            A = A + int(data[i].select('td')[24].text)
            DP = DP + int(data[i].select('td')[25].text)
            TP = TP + int(data[i].select('td')[26].text)
            E = E + int(data[i].select('td')[27].text)
            CS = CS + int(data[i].select('td')[28].text)
            PB = PB + int(data[i].select('td')[29].text)
        return PA ,AB ,RBI ,R ,H ,B2 ,B3 ,HR ,TB ,SO ,SB ,CS ,AVG ,SAC ,SF ,BB ,IBB ,HBP ,GIDP ,TP ,LOB ,PO ,A ,DP ,TP ,E ,CS ,PB