/*
A very simple upwind program because my Python skill's sucks
 */

#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<sstream>

using namespace std;

int sign(float c){
return ( 0.0 < c) - (c < 0.0);
}

/*File output*/
void output(int steps, vector<float> x, vector<float> fx)
{
  ofstream fp;
  stringstream buf;
  string filenumber;

  buf<<setfill('0');
  filenumber = to_string(steps);
  buf<<setw(5)<<filenumber;

  string filename="./data/f"+buf.str()+".csv";
  fp.open(filename, ios::out);
  fp<<"x, fx\n";
  for(int i=0; i<x.size(); ++i){
    fp<<x[i]<<", "
      <<fx[i]<<"\n";
  }
  fp.close();
  buf.str(string()); //clear buffer
}

int main()
{
  int imax = 1001;
  float length = 10.0;
  float dx = length / (imax-1);
  float dt;
  
  cout<<"Enter dt (dx ="<<dx<<")"<<endl;
  cin>>dt;
  
  vector<float> u, un, xg;
  u.resize(imax);
  un.resize(imax);
  xg.resize(imax);

  int i;
  //Initial condition
  for(i = 0; i<imax; ++i){
    xg[i] = i*dx;
    u[i] = 0.0;
    un[i] = 0.0;
    if( xg[i] >= 0.2*length and xg[i] <= 0.4*length){
      u[i] = 1.0;
      un[i] = 1.0;
    }
  }

  //start advection
  int itermax = 2.0/(dt) + 1;
  int iter;
  int iup;
  float c = 1.0;
  int steps = itermax/10;

  cout<<"Maximum iteration: "<<itermax<<endl;
  
  do{

    for(i=1; i<imax-1; ++i){
      iup = i - sign(c);
      un[i] = u[i] - c*(dt/dx)*( u[i] - u[iup] );
    }
    swap(u,un);

    if(iter%steps == 0) output(iter, xg, u);
    
    iter +=1;
  }while(iter<itermax);
  
  
  
}
