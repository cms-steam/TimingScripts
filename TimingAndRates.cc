#include <iostream>
#include <vector>
#include <string>
#include "TFile.h"
#include "TKey.h"
#include "TCollection.h"
#include <iostream>
#include <sstream>
#include <string>
#include "TROOT.h"
using namespace std;

void TimingAndRates(float time, std::string filename,int run=1,std::string outname="HLT_Paths_TimingAndRates.csv",std::string process="HLTX"){
 
  std::cout<<"starting program"<<std::endl;
  std::vector<string> vNames;
  std::vector<float> vTimes;
  std::vector<float> vRates;
 

  ofstream outfile(outname.c_str());

  TFile* file = new TFile(filename.c_str());
  std::stringstream dirname;
  dirname<<"DQMData/Run "<<run<<"/HLT/Run summary/TimerService/Running 1 processes/process "<<process<<"/Paths";
  file->cd( (dirname.str()).c_str() );
  std::cout<<dirname.str()<<std::endl;
  TIter next(gDirectory->GetListOfKeys());
  TKey *key;
  
  while ((key = (TKey*)next())) {
    TClass *cl = gROOT->GetClass(key->GetClassName());
    if (!cl->InheritsFrom("TH1")) continue;
    TH1 *h = (TH1*)key->ReadObj();
    //    names.push_back(h->GetName());
    string title = h->GetTitle();
    string name = h->GetName();
    size_t pos;

    if(title.find("v2")!=string::npos){
      pos = title.find("v2");
    }
    else if(title.find("v1")!=string::npos){
      pos=title.find("v1");
    }
    string path(title,0,pos-1);
    float mean;
    float rate;

    if(title.find("module counter")!=string::npos){
 
      TAxis* axis = h->GetXaxis();
      int nbins = h->GetNbinsX();
      for(int i = 1; i<=nbins; i++){
	string label = axis->GetBinLabel(i);
	if(label.find("hltBoolEnd")!=string::npos){
       	  //push back rate to vector
	  rate = h->GetBinContent(i)/(time);
	  vRates.push_back(rate);
	  vNames.push_back(path);
	}
      }
      
    }

  }

  TIter next2(gDirectory->GetListOfKeys());
  TKey *key2;


  while ((key2 = (TKey*)next2())) {
    TClass *cl = gROOT->GetClass(key2->GetClassName());
    if (!cl->InheritsFrom("TH1")) continue;
    TH1 *h = (TH1*)key2->ReadObj();
    //    names.push_back(h->GetName());
    string title = h->GetTitle();
    string name = h->GetName();
    size_t pos;

    if(title.find("v2")!=string::npos){
      pos = title.find("v2");
    }
    else if(title.find("v1")!=string::npos){
      pos=title.find("v1");
    }
    string path(title,0,pos-1);

    //make sure path is in rates
    bool inRates=false;
    for(size_t j=0; j<vNames.size();j++){
      if(path==vNames.at(j)) inRates=true;
    }
    
    if(!inRates) continue;


    if(name.find("total")!=string::npos && name.find("module_total")==string::npos){
      //handle special case with 'totalOR' in name
      if(name.find("totalOR")!=string::npos && !(name.find("total",name.find("total"+1))!=string::npos)) continue;
      if(name.find("DQMOutput")!=string::npos) continue;
      //      std::cout<<name<<" with mean: "<<h->GetMean()<<std::endl;
      mean = h->GetMean();
      vTimes.push_back(mean);
     
    }
  }


  outfile<<"Path,TotalTime(ms),Rate(Hz)\n";
  for(unsigned int k =0; k<vNames.size(); k++){
    outfile<<vNames.at(k)<<","<<vTimes.at(k)<<","<<vRates.at(k)<<std::endl;
  }


}



