#include <iostream>
#include <vector>
#include "TH1.h"
#include "TGraph.h"
#include "TF1.h"

void Fit_v_PU(){

  Double_t x[]={15,17,22,25,27};//enter pileup points
  Double_t y[]={70.56,76.96,99.93,124.37,128.99};//enter timing values

  TGraphErrors *g = new TGraphErrors((sizeof(x) / sizeof(Double_t)), x, y);
  TCanvas* c = new TCanvas();
  /*
  //set errors
  g->SetPointError(0,1,1);
  g->SetPointError(1,1,1);
  g->SetPointError(2,1,1);
  g->SetPointError(3,1,1);
  g->SetPointError(4,3,1);
  g->SetPointError(5,2,1);
  g->SetPointError(6,1,1);
  g->SetPointError(7,1,1);
  g->SetPointError(8,1.5,1);
  g->SetPointError(9,2.5,1);
  g->SetPointError(10,1,1);
  g->SetPointError(11,2,1);
  g->SetPointError(12,1,1);
  g->SetPointError(13,1,1);
  g->SetPointError(14,1,1);
  g->SetPointError(15,1,1);
  g->SetPointError(16,1,1);
*/

  //linear fit first
  TF1* lin = new TF1("lin","pol1",0,50);
  g->Fit(lin);
  lin->SetLineColor(kBlue);
  //quadratic
  TF1* quad  = new TF1("quad","pol2",0,50);
  g->Fit(quad,"+");
  quad->SetLineColor(kGreen);
  //quad->Draw();
  //exponential
  TF1* exp = new TF1("exp","expo",0,50);
  //g->Fit(exp,"+");
  //exp->SetLineColor(kBlue);
  //exp->Draw();
  TLine* line = new TLine(0,240,50,240);
  line->SetLineColor(kRed);
  g->SetPoint(g->GetN(),50,1000);
  g->SetMarkerStyle(20); 
  g->GetYaxis()->SetRangeUser(0,250);
  g->GetXaxis()->SetRangeUser(0,50);
  g->GetXaxis()->SetTitle("<PU>");
  g->GetYaxis()->SetTitle("Processing Time (ms)");
  g->SetTitle("Processing Time vs. Pileup");
  g->Draw("ap");
  c->Update();
  //exp->Draw("same");
  lin->Draw("same");
  line->Draw("same");
  quad->Draw("same");
  c->Print("Timing_Fit_v_PU.pdf");

  for(int i=0; i<g->GetN();i++){
    std::cout<<"Point: "<<i<<" pileup: "<<g->GetX()[i]<<" timing: "<<g->GetY()[i]<<std::endl;
  }

}
