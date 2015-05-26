#include <iostream>
#include <vector>
#include <string>
#include "TFile.h"
#include "TKey.h"
#include "TCollection.h"

using namespace std;

void test(){
  gStyle->SetOptStat(kFALSE);

  vector<string> vNames;
  vector<float> vTimes;
  vector<float> vRates;


  ofstream outfile("HLT_Paths_Total_Time_CMSSW742_pu40bx25.csv");

  TFile* file703 = new TFile("DQM_Timing_PU40bx25_CMSSW742_May2015FrozenMenu.root");
  file703->cd("DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths");

  TIter next703(gDirectory->GetListOfKeys());
  TKey *key703;


  
  while ((key703 = (TKey*)next703())) {
    TClass *cl = gROOT->GetClass(key703->GetClassName());
    if (!cl->InheritsFrom("TH1")) continue;
    TH1 *h = (TH1*)key703->ReadObj();
    //    names703.push_back(h->GetName());
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
	  rate = h->GetBinContent(i)/(1.621);
	  vRates.push_back(rate);
	  vNames.push_back(path);
	  std::cout<<"path in rates: "<<path;
	}
      }

    }

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

  std::cout<<vNames.size()<<" "<<vTimes.size()<<std::endl;

  for(unsigned int j =0; j<vNames.size(); j++){
    outfile<<vNames.at(j)<<","<<vTimes.at(j)<<","<<vRates.at(j)<<std::endl;
  }

  //  TH1F* hist = new TH1F("hist","Paths Total time",names703.size(),0,names703.size());
  /*  for(int i=0;i<names703.size();i++){
    hist->Fill(i,avgs[i]);
    hist->GetXaxis()->SetBinLabel(i+1,names703[i].c_str());   
    //cout<<"Hist: "<<names703[i]<<" Average: "<<avgs[i]<<endl;
  }
  TCanvas c1;
  hist->GetYaxis()->SetTitle("processing time (ms)");
  //hist->Draw();
  //  c1.Print("Paths_Total_Times.pdf");

  TCanvas c2;
  TH1F* aphist = file703->Get("DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process TEST/all_paths");
  aphist->SetTitle("all_paths Processing time for GRunV41");
    //cout<<histname703<<endl;
  //aphist->Draw();
  //c2.Print("GrunV41_allpaths.pdf");*/
}



