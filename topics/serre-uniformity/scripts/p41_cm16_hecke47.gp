\\ Actual T2 image of the full CM(-4) elliptic divisor, including both vertical kernels.
p41c16_velu(P,rr,scale,u,z)={
  my(v=3*rr^2+1,iv=p41l_inv(P[1]-rr,u,z),si=p41l_inv(scale,u,z));
  [(P[1]+v*iv)*si^2,P[2]*(1-v*iv^2)*si^3];
};
p41_cm16_hecke47(input,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ii=sum(k=1,80,input[4][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    P=vector(2,j,sum(k=1,80,input[10][j][k]*u^(k-1))),
    Q=vector(2,j,sum(k=1,80,input[11][j][k]*u^(k-1))),
    U=Mod(matrix(2,2,i,j,input[12][i][j]),41),
    F=Mod(matrix(2,2,i,j,input[13][i][j]),41),D=Mod([1,0;0,21],41),
    delta=Mod(input[17],q)*u^0,scale=(1+ii)/delta,scalem=(1-ii)/delta,
    PP,QQ,PM,QM,PH,QH,expected,Ft,Um,epsvar=varhigher("cm16e",'t),eps,vals,reps=List(),
    signed=vector(1681),neg,Es,power,aa=vector(159),bb=vector(159),HA,HB,gh,GR,GI,W,C,Fmodel);
  if(delta^2!=2||scale^2!=ii||scalem^2!=-ii,error("CM16 actual scale"));
  PP=p41c16_velu(P,ii,scale,u,z);QQ=p41l_mul(p41c16_velu(Q,ii,scale,u,z),21,-11,u,z);
  PM=p41c16_velu(P,-ii,scalem,u,z);QM=p41l_mul(p41c16_velu(Q,-ii,scalem,u,z),21,-11,u,z);
  for(j=1,4,
    expected=if(j==1,PP,if(j==2,QQ,if(j==3,PM,QM)));
    if(expected[2]^2!=expected[1]^3-11*expected[1]-14,error("CM16 actual target curve"));
    if(p41l_mul(expected,41,-11,u,z)!=[0],error("CM16 actual target41-torsion")));
  Um=D^-1*U*D;
  for(j=1,2,
    expected=p41l_add(p41l_mul(PM,lift(Um[1,j]),-11,u,z),p41l_mul(QM,lift(Um[2,j]),-11,u,z),-11,u,z);
    if(expected!=if(j==1,PP,QQ),error("CM16 vertical maps differ by actual source i")));
  PH=p41c16_velu(P,0*u,1+ii,u,z);QH=p41c16_velu(Q,0*u,1+ii,u,z);
  for(j=1,2,
    expected=p41l_add(p41l_mul(P,lift((matid(2)+U)[1,j]),1,u,z),
      p41l_mul(Q,lift((matid(2)+U)[2,j]),1,u,z),1,u,z);
    if(expected!=if(j==1,PH,QH),error("CM16 horizontal map is not actual1+i")));
  Ft=D^-1*(-U)*F*D;
  for(j=1,2,
    expected=p41l_add(p41l_mul(PP,lift(Ft[1,j]),-11,u,z),p41l_mul(QQ,lift(Ft[2,j]),-11,u,z),-11,u,z);
    if(expected!=vector(2,k,subst(lift(if(j==1,PP[k],QQ[k])),'t,phi)),error("CM16 target Frobenius")));
  print("Actual three2-isogenies and both vertical identifications PASS ",getwalltime());
  eps=Mod(Mod(1,q)*u^0*epsvar,epsvar);
  vals=p41a_eisenstein(vector(2,j,PP[j]*eps^0),vector(2,j,QQ[j]*eps^0),-11*eps^0,u,z,1,epsvar);
  for(j=1,1680,neg=lift(Mod(-(j%41),41))+41*lift(Mod(-(j\41),41));
    if(j<neg,listput(reps,j+1);signed[j+1]=#reps;signed[neg+1]=-#reps));
  reps=Vec(reps);Es=[Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(vals[reps[j]]),0,epsvar)),i-1))),q)];
  power=u^0;for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  gh=vector(20,n,vector(42,k,lift(Mod(matrix(2,2,i,j,input[8][input[15][n]][i][j]),41)*
    Mod(matrix(2,2,i,j,input[9][k][i][j]),41))));
  GR=p41a_trace_coefficient(Es,HA,0,gh,input[5],signed);
  GI=p41a_trace_coefficient(Es,HB,0,gh,input[5],signed);
  C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2);
  Fmodel=matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*u2);W=(GR+u2*GI)*C;
  if(W*Fmodel!=matrix(20,73,n,k,subst(lift(W[input[16][n],k]),'s,-u2)),error("CM16 complete model descent"));
  write(path,[vector(2,j,p41l_vec(PP[j])),vector(2,j,p41l_vec(QQ[j])),
    vector(2,j,p41l_vec(PM[j])),vector(2,j,p41l_vec(QM[j])),
    vector(2,i,vector(2,j,lift(Ft[i,j]))),p41m_encode(W)]);
  print("Actual CM16 full20x73 values PASS ",getwalltime());
};

