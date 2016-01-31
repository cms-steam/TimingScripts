#include <iostream>
#include <vector>
#include "TH1.h"
#include "TGraph.h"
#include "TF1.h"

void Fit_v_PU(){

  Double_t x[]={8,10,12,15,16,20};//enter pileup points
  Double_t y[]={40,50,60,75,85,115};//enter timing values

  TGraph *g = new TGraph((sizeof(x) / sizeof(Double_t)), x, y);
  TCanvas* c = new TCanvas();
  //linear fit first
  TF1* lin = new TF1("lin","pol1",0,50);
  g->Fit(lin);
  lin->SetLineColor(kRed);
  //quadratic
  TF1* quad  = new TF1("quad","pol2",0,50);
  g->Fit(quad,"+");
  quad->SetLineColor(kGreen);
  quad->Draw();
  //exponential
  TF1* exp = new TF1("exp","expo",0,50);
  g->Fit(exp,"+");
  exp->SetLineColor(kBlue);
  //exp->Draw();
  g->SetMarkerStyle(20);
  g->GetYaxis()->SetRangeUser(0,250);
  g->GetXaxis()->SetRangeUser(0,60);
  g->Draw("psame");
  c->Update();
  exp->Draw("same");
  lin->Draw("same");
  //quad->Draw("same");
  c->Print("Timing_Fit_v_PU.pdf");


}
