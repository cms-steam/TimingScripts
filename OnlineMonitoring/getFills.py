# Imports
import cx_Oracle
import socket
# For the parsing
import re


class DBQueryTool:

    def __init__(self) :
        # Connect to the Database
        hostname = socket.gethostname()
        if hostname.find('lxplus') > -1: self.dsn_ = 'cms_omds_adg' #offline
        else: self.dsn_ = 'cms_omds_lb' #online

        orcl = cx_Oracle.connect(user='cms_hlt_r',password='convertMe!',dsn=self.dsn_)
        orcl = cx_Oracle.connect(user='cms_trg_r',password='X3lmdvu4',dsn=self.dsn_)
        # Create a DB cursor
        self.curs = orcl.cursor()

    def getRunsFromFill(self,fill):

#        query="""SELECT MAX(A.RUNNUMBER), MAX(B.LIVELUMISECTION) FROM CMS_RUNINFO.RUNNUMBERTBL A, CMS_RUNTIME_LOGGER.LUMI_SECTIONS B WHERE B.RUNNUMBER=A.RUNNUMBER AND B.LUMISECTION > 0 """
#        query="""SELECT RUNNUMBER FROM CMS_RUNINFO.RUNNUMBERTBL A, CMS_RUNTIME_LOGGER.LUMI_SECTIONS B WHERE B.RUNNUMBER=A.RUNNUMBER AND B.LUMISECTION > 0 """
#        query="""SELECT column_name FROM all_tab_cols WHERE table_name = 'LUMI_SECTIONS' AND owner = 'CMS_RUNTIME_LOGGER'"""
#        query= """SELECT RUN_NUMBER FROM CMS_TCDS_MONITORING.TCDS_CPM_COUNTS_V WHERE FILL_NUMBER=%i""" % fill
        query= """SELECT RUNNUMBER FROM CMS_RUNTIME_LOGGER.LUMI_SECTIONS WHERE LHCFILL = (SELECT LHCFILL FROM CMS_RUNTIME_LOGGER.RUNTIME_SUMMARY WHERE BEGINTIME IS NOT NULL AND LHCFILL=%i) AND BEAM1_STABLE=1 AND BEAM2_STABLE=1""" % fill
        self.curs.execute(query)
        return self.curs.fetchall()
#        print self.curs.fetchone()



## ----------- End of class ------------ ##

#define list of fills
fills = [5027,5028,5029,5030,5038,5043,5045,5048,5052,5056,5060,5069,5071,5072,5073,5076,5078,5080,5083,5085,5091,5093,5095,5096,5097,5101,5105,5106,5107,5108,5109,5111,5112,5116,5117,5149,5151,5154,5161,5162,5163,5173,5179,5181,5183,5187,5197,5198,5199,5206,5210,5211]

if __name__ == "__main__":
    query_tool = DBQueryTool()

    for fill in fills:
        table = query_tool.getRunsFromFill(fill)
 #   print table
        runs = []
        for run in table:
            if not run in runs:
                runs.append(run)

        cleanedruns = []
        for run in runs:
            cleanedrun = str(run)
            cleanedrun = cleanedrun.replace('(','')
            cleanedrun = cleanedrun.replace(')','')
            cleanedrun = cleanedrun.replace(',','')
            cleanedruns.append(cleanedrun)
        print cleanedruns
    #now we have a list of the run numbers we want, so now check that stable beams were happening
#    for run in cleanedruns:
        
    
