
from ROOT import TGraph

class fill(object):
    def __init__(self,number,runs,menu,cmssw):
        self.number = number
        self.runs = runs
        self.menu = menu
        self.cmssw = cmssw
        self.tHists = []
        self.lHists = []
        self.lFiles = []
        self.tFiles = []
        self.graph = TGraph()

    def addTimeHist(self,f):
        hist = f.Get("/HLT/TimerService/Running 4 processes/event_byls")
        print hist
        self.tHists.append(hist)

    def addLumiHist(self,f):
        hist = f.Get("/Scal/LumiScalers/Instant_Lumi")
        print hist
        self.lHists.append(hist)
        
    def SetGraph(self):
        self.graph = getGraph(self.tHists,self.lHists)
        self.graph.SetTitle("Processing Time vs. Luminosity; Luminosity (e30 cm^{-2}); Average Processing Time")

    def printFill(self):
        out = 'Fill: %i\n' % self.number
        out += 'Runs: '
        for run in self.runs:
            out+='%s,' % run
        out+="\n"
        out+="HLT Menu: %s\n" % self.menu
        out+="CMSSW: %s\n\n" %self.cmssw
        print out

def inGolden(jsonfile,run,lumi):
    #boolean to return
    golden=False

    if u'%i' % run in jsonfile:
        lumis=jsonfile[u'%i' % run]
        for lumirange in lumis:
            if lumi > lumirange[0] and lumi < lumirange[1]:
                golden=True
    return golden
