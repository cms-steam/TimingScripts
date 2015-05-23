
#include <iostream>
#include <vector>
#include <string>
#include "TFile.h"
#include "TKey.h"
#include "TH1.h"
#include "TCollection.h"

using namespace std;

void diff_timing(){

  vector<string> names730;
  vector<string> names740;

  TFile* file730 = new TFile("DQM_Timing_PU40bx25_GRunV56_extRange.root");
  file730->cd("DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths");
  
  TIter next730(gDirectory->GetListOfKeys());
  TKey *key730;

  ofstream outfile("diff.txt");


  while ((key730 = (TKey*)next730())) {
    TClass *cl = gROOT->GetClass(key730->GetClassName());
    if (!cl->InheritsFrom("TH1")) continue;
    TH1 *h = (TH1*)key730->ReadObj();
    string title = h->GetName();
    
    if(title.find("module_total")!=string::npos){
      names730.push_back(key730->GetName());


    }

  }


  TFile* file740 = new TFile("DQM_Timing_CMSSW740patch1_frozenMenu_PU40bx25.root");
  file740->cd("DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths");

  TIter next740(gDirectory->GetListOfKeys());
  TKey *key740;
  
  while ((key740 = (TKey*)next740())) {

    TClass *cl = gROOT->GetClass(key740->GetClassName());
    if (!cl->InheritsFrom("TH1")) continue;
    TH1 *h = (TH1*)key740->ReadObj();
    string title = h->GetName();
    if(title.find("module_total")!=string::npos){
       names740.push_back(h->GetName());
       }
  }

  int nmax;


  nmax=names730.size();


  cout<<"n740 is: "<<names740.size()<<endl;
  cout<<"n730 is: "<<names730.size()<<endl;
  //  outfile<<diff<<endl;


  vector<float> vres;
  vector<int> viter;

  for(int i=0; i<nmax; i++){

    string histname730 = "DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths/"+names730[i];
    //cout<<histname730<<endl;
    for(int j =0; j < 100; j++){
      //cout<<"730: "<<names730[i]<<" 740: "<<names740[j]<<endl;
      if(!(names730[i]==names740[j]) )continue;
      string histname740 = "DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths/"+names740[i];
      //cout<<histname740<<endl;
      
      cout<<histname730<<endl;
      TH1F* hist730 = (TH1F*)file730->Get(histname730.c_str());
      TH1F* hist740 = (TH1F*)file740->Get(histname740.c_str());
      float diff = hist730->GetMean() - hist740->GetMean();
      float percentdiff=0.0;
      if(hist730->GetMean()!=0){
	percentdiff = (diff/hist730->GetMean())*100.;
      }
      outfile<<diff<<endl;
      if(percentdiff<100 && percentdiff>-200){
	vres.push_back(percentdiff);
	viter.push_back(i);
      }
    }
    //reshist->SetBinName(i,names730[i].c_str());
    cout<<"running hist: "<<i<<" out of "<<nmax<<endl;
    //cout<<histname740<<endl;
  }

  int jjet =0;

  for(int i=0;i<vres.size();i++){
    if(names730[viter[i]].find("Jet")!=string::npos){
      jjet++;
      vJetRes.push_back(vres[i]);
    }

  }



  //make a new histogram to plot results
  TH1F* JetResHist = new TH1F("reshist","Percentage change from 73X to 74X for Jet Paths",vres.size(),0,vres.size());
  TH1F* MuResHist = new TH1F("reshist","Percentage change from 73X to 74X for Muon Paths",vres.size(),0,vres.size());
  TH1F* ElResHist = new TH1F("reshist","Percentage change from 73X to 74X for Electron Paths",vres.size(),0,vres.size());
  TH1F* PhotonResHist = new TH1F("reshist","Percentage change from 73X to 74X for Photon Paths",vres.size(),0,vres.size());


      reshist->Fill(j,vres[i]);
      reshist->GetXaxis()->SetBinLabel(j,names730[viter[i]].c_str());
      cout<<"bin number: "<<j<<" with label "<<names730[viter[i]]<<" and difference: "<<vres[i]<<endl;

  reshist->Draw();

}
