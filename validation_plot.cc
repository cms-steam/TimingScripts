#include <iostream>
#include <stringstream>
#include <vector>
#include "TTree.h"
#include "TFile.h"
#include "TH1.h"
#include "TLegend.h"

void validation_plot(int run, std::string process="HLTX",std::string f1='dummy', std::string f2='dummy', std::string f3='dummy',std::string f4='dummy',std::string f5='dummy'){
  
  gStyle->SetOptStat(kFALSE);

  TCanvas c1;

  std::vector<TFile*> vFile;
  if(f1!='dummy'){
    TFile* file1 = new TFile(f1.c_str()); 
    vFile.push_back(file1);
  }
  if(f2!='dummy'){
    TFile* file2 = new TFile(f2.c_str()); 
    vFile.push_back(file2);
  }
  if(f3!='dummy'){
    TFile* file3 = new TFile(f3.c_str()); 
    vFile.push_back(file3);
  }
  if(f4!='dummy'){
    TFile* file4 = new TFile(f4.c_str()); 
    vFile.push_back(file4);
  }
  if(f5!='dummy'){
    TFile* file5 = new TFile(f5.c_str()); 
    vFile.push_back(file5);
  }

  std::stringstream histstring;
  histstring<<"DQMData/Run "<<run<<"/HLT/Run summary/TimerService/Running 1 processes/process "<<process<<"/all_paths";
  std::string histname = histstring.str();

  std::vector<TH1F> vHist;

  for(size_t i =0; i<vFile.size();i++){
    vHist.push_back( (TH1F*) vFile.at(i)->Get(histname.c_str()) );
  }

  for(size_t i=0; i<vHist.size(); i++){

    vHist.at(i)->SetLineWidth(2);
    vHist.at(i)->GetXaxis()->SetRangeUser(0,2000);
    vHist.at(i)->SetLineColor(kBlue+2*i);
    if(i=0) vHist.at(i)->Draw();
    else vHist.at(i)->Draw("same");
    leg->AddEntry(vHist.at(i),Form("hist %i",i),"l");
  }

  leg->Draw("same");

  c1.Print("HLT_Validation.pdf");

  
}
