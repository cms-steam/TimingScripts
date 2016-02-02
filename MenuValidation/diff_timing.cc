
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
      cout<<"histname: "<<h->GetName()<<" keyname: "<<key730->GetName()<<endl;
      outfile<<h->GetName()<<endl;
    }

  }
  outfile<<endl;
  outfile<<"******************NOW 740 NAMES****************"<<endl;
  outfile<<endl;

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
       outfile<<h->GetName()<<endl;
       }
  }

  int nmax;


  nmax=names730.size();


  cout<<"n740 is: "<<names740.size()<<endl;
  cout<<"n730 is: "<<names730.size()<<endl;
  //  outfile<<diff<<endl;


  vector<float> vres;
  vector<int> viter;

  outfile<<endl;
  outfile<<"********************Matched Names Now*************************"<<endl;

  for(int i=0; i<nmax; i++){

    string histname730 = "DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths/"+names730[i];
    //if(i>80) cout<<names730[i]<<endl;
    //cout<<histname730<<endl;
    for(int j =0; j < names740.size(); j++){

      //cout<<"730: "<<names730[i]<<" 740: "<<names740[j]<<endl;
      if(!(names730[i]==names740[j]) )continue;
      string histname740 = "DQMData/Run 1/HLT/Run summary/TimerService/Running 1 processes/process HLTX/Paths/"+names740[i];
      //cout<<histname740<<endl;
      outfile<<names740[j]<<endl;
      //cout<<histname730<<endl;
      TH1F* hist730 = (TH1F*)file730->Get(histname730.c_str());
      TH1F* hist740 = (TH1F*)file740->Get(histname740.c_str());
      float diff = hist730->GetMean() - hist740->GetMean();
      float percentdiff=0.0;
      if(hist730->GetMean()!=0){
	percentdiff = (diff/hist730->GetMean())*100.;
      }
      //outfile<<diff<<endl;
      if(percentdiff<100 && percentdiff>-200){
	vres.push_back(percentdiff);
	viter.push_back(i);
      }
    }
    //reshist->SetBinName(i,names730[i].c_str());
    if(i%10==0){
      cout<<"running hist: "<<i<<" out of "<<nmax<<endl;
    //cout<<histname740<<endl;
    }
  }

  std::vector<std::string> vJetNames;
  std::vector<float> vJetRes;
  std::vector<std::string> vMuNames;
  std::vector<float> vMuRes;
  std::vector<std::string> vElNames;
  std::vector<float> vElRes;
  std::vector<std::string> vPhotNames;
  std::vector<float> vPhotRes;
  std::vector<std::string> vHTNames;
  std::vector<float> vHTRes;

  for(int i=0;i<vres.size();i++){
    if(names730[viter[i]].find("Jet")!=string::npos){
      vJetNames.push_back(names730[viter[i]]);
      vJetRes.push_back(vres[i]);
    }
    else if(names730[viter[i]].find("HT")!=string::npos){
      vHTNames.push_back(names730[viter[i]]);
      vHTRes.push_back(vres[i]);
    }
    else if(names730[viter[i]].find("El")!=string::npos){
      vElNames.push_back(names730[viter[i]]);
      vElRes.push_back(vres[i]);
    }
    else if(names730[viter[i]].find("Mu")!=string::npos){
      vMuNames.push_back(names730[viter[i]]);
      vMuRes.push_back(vres[i]);
    }
    else if(names730[viter[i]].find("Photon")!=string::npos){
      vPhotNames.push_back(names730[viter[i]]);
      vPhotRes.push_back(vres[i]);
    }

  }



  //make a new histogram to plot results
  TH1F* JetResHist = new TH1F("JetReshist","Percentage change from 73X to 74X for Jet Paths",vJetRes.size(),0,vJetRes.size());
  TH1F* MuResHist = new TH1F("MuReshist","Percentage change from 73X to 74X for Muon Paths",vMuRes.size(),0,vMuRes.size());
  TH1F* ElResHist = new TH1F("ElReshist","Percentage change from 73X to 74X for Electron Paths",vElRes.size(),0,vElRes.size());
  TH1F* PhotResHist = new TH1F("PhotReshist","Percentage change from 73X to 74X for Photon Paths",vPhotRes.size(),0,vPhotRes.size());
  TH1F* HTResHist = new TH1F("HTReshist","Percentage change from 73X to 74X for HT Paths",vHTRes.size(),0,vHTRes.size());

  TCanvas c1;
  for(int j=0; j< vJetRes.size(); j++){
    JetReshist->Fill(j+1,vJetRes[j]);
    JetReshist->GetXaxis()->SetBinLabel(j+1,vJetNames[j].c_str());
    cout<<"bin number: "<<j<<" with label "<<vJetNames[j]<<" and difference: "<<vJetRes[j]<<endl;
  }

  JetReshist->Draw();
  c1.Print("TimingDifferencesForJetPaths.pdf");

  TCanvas c2;
  for(int j=0; j< vHTRes.size(); j++){
    HTReshist->Fill(j+1,vHTRes[j]);
    HTReshist->GetXaxis()->SetBinLabel(j+1,vHTNames[j].c_str());
    cout<<"bin number: "<<j<<" with label "<<vHTNames[j]<<" and difference: "<<vHTRes[j]<<endl;
  }

  HTReshist->Draw();
  c2.Print("TimingDifferencesForHTPaths.pdf");

  TCanvas c3;
  for(int j=0; j< vElRes.size(); j++){
    ElReshist->Fill(j+1,vElRes[j]);
    ElReshist->GetXaxis()->SetBinLabel(j+1,vElNames[j].c_str());
    cout<<"bin number: "<<j<<" with label "<<vElNames[j]<<" and difference: "<<vElRes[j]<<endl;
  }

  ElReshist->Draw();
  c3.Print("TimingDifferencesForElPaths.pdf");

  TCanvas c4;
  for(int j=0; j< vMuRes.size(); j++){
    MuReshist->Fill(j+1,vMuRes[j]);
    MuReshist->GetXaxis()->SetBinLabel(j+1,vMuNames[j].c_str());
    cout<<"bin number: "<<j<<" with label "<<vMuNames[j]<<" and difference: "<<vMuRes[j]<<endl;
  }

  MuReshist->Draw();
  c4.Print("TimingDifferencesForMuPaths.pdf");

  TCanvas c5;
  for(int j=0; j< vPhotRes.size(); j++){
    PhotReshist->Fill(j+1,vPhotRes[j]);
    PhotReshist->GetXaxis()->SetBinLabel(j+1,vPhotNames[j].c_str());
    cout<<"bin number: "<<j<<" with label "<<vPhotNames[j]<<" and difference: "<<vPhotRes[j]<<endl;
  }

  PhotReshist->Draw();
  c5.Print("TimingDifferencesForPhotonPaths.pdf");


}
