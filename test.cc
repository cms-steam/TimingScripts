#include <iostream>
#include <vector>
#include <string>
#include "TFile.h"
#include "TKey.h"
#include "TCollection.h"
#include <iostream>
#include <string>
#include "TROOT.h"
using namespace std;

void test(float time, std::string filename){


  vector<string> vNames;
  vector<float> vTimes;
  vector<float> vRates;


  ofstream outfile("HLT_Paths_Total_Time_CMSSW742_pu40bx25.csv");

  TFile* file = new TFile(filename.c_str());
  file->cd("DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths");

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
    if(name.find("total")!=string::npos && name.find("module_total")==string::npos){
      //handle special case with 'totalOR' in name
      if(name.find("totalOR")!=string::npos && !(name.find("total",name.find("total"+1))!=string::npos)) continue;
      if(name.find("DQMOutput")!=string::npos) continue;
      //      std::cout<<name<<" with mean: "<<h->GetMean()<<std::endl;
      mean = h->GetMean();
      vTimes.push_back(mean);
      std::cout<<" path in timing: "<<path<<std::endl;
    }
  }



  for(unsigned int j =0; j<vNames.size(); j++){
    outfile<<vNames.at(j)<<","<<vTimes.at(j)<<","<<vRates.at(j)<<std::endl;
  }


}



