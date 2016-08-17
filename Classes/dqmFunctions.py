

def inGolden(jsonfile,run,lumi):
    #boolean to return
    golden=False

    if u'%i' % run in jsonfile:
        lumis=jsonfile[u'%i' % run]
        for lumirange in lumis:
            if lumi > lumirange[0] and lumi < lumirange[1]:
                golden=True
    return golden
