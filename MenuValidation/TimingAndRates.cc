#include <iostream>
#include <vector>
#include <string>
#include "TFile.h"
#include "TKey.h"
#include "TCollection.h"
#include <sstream>
#include <fstream>
#include <string>
#include "TROOT.h"
#include "TClass.h"
#include "TH1.h"
using namespace std;

void TimingAndRates(float time, std::string filename,int run=1,std::string outname="HLT_Paths_TimingAndRates.csv",std::string process="HLTX"){
 
  std::cout<<"starting program"<<std::endl;
  std::vector<string> vNames;
  std::vector<float> vTimes;
  std::vector<float> vRates;
 
  std::cout<<outname<<std::endl;
  std::cout<<filename<<std::endl;
  ofstream outfile(outname.c_str());

  TFile* file = new TFile(filename.c_str());
  std::stringstream dirname;
  dirname<<"DQMData/Run "<<run<<"/HLT/Run summary/TimerService/process "<<process<<" paths";
  //std::cout<<"dirname = "<<(dirname.str()).c_str()<<endl;
  file->cd( (dirname.str()).c_str() );
  std::cout<<dirname.str()<<std::endl;
  TIter next(gDirectory->GetListOfKeys());
  TKey *key;
  
  while ((key = (TKey*)next())) {
    TClass *cl = gROOT->GetClass(key->GetClassName());
//    if (!cl->InheritsFrom("TH1")) continue;
    if (!cl->InheritsFrom("TDirectory")) continue;
//    TH1 *h = (TH1*)key->ReadObj();
    TDirectory *pathTDir = (TDirectory*)key->ReadObj();
    //    names.push_back(h->GetName());
//    string title = h->GetTitle();
    string pathdirname = pathTDir->GetName();
    string fullpathdir = dirname.str()+"/"+pathdirname;
    string path;

//    string name = h->GetName();
    //Get rid of "endpath " and "path " in names
    size_t pos;

    if(pathdirname.find("endpath ")!=string::npos){
        path = pathdirname.erase(0,8);
    }
    else if(pathdirname.find("path ")!=string::npos){
        path=pathdirname.erase(0,5);
    }

    //cd into paths directory and get the right histograma
    file->cd(fullpathdir.c_str());
//    string path(title,0,pos-1);
    //Do rates
    float rate;
    TH1* hcounts =(TH1*)(gDirectory->GetKey("module_counter"))->ReadObj();
        //if(title.find("module counter")!=string::npos){
    TAxis* axis = hcounts->GetXaxis();
    int nbins = hcounts->GetNbinsX();
    for(int i = 1; i<=nbins; i++){
        string label = axis->GetBinLabel(i);
        if(label.find("hltBoolEnd")!=string::npos){
            //push back rate to vector
            rate = hcounts->GetBinContent(i)/(time);
            vRates.push_back(rate);
            vNames.push_back(path);
        }
    }

    //Do time
    //make sure path is in rates
    bool inRates=false;
    for(size_t j=0; j<vNames.size();j++){
      if(path==vNames.at(j)) inRates=true;
    }
    
    if(!inRates) continue;
    //std::cout<<"Checking path "<<path<<endl;
    
    float mean;
    TH1* htime =(TH1*)(gDirectory->GetKey("path time_real"))->ReadObj();
    mean = htime->GetMean();
    vTimes.push_back(mean);
      
    

  }

  outfile<<"Path,TotalTime(ms),Rate(Hz)\n";
  for(unsigned int k =0; k<vNames.size(); k++){
    outfile<<vNames.at(k)<<","<<vTimes.at(k)<<","<<vRates.at(k)<<std::endl;
  }


}



