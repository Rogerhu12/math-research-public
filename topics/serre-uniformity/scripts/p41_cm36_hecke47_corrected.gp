\\ Actual four cyclic3-isogenies from y^2=x^3+x; two CM(-36) branches.
p41c36_velu(P,rr,scale,u,z)={
  my(v=3*rr^2+1,w=rr^3+rr,iv=p41l_inv(P[1]-rr,u,z),si=p41l_inv(scale,u,z));
  [(P[1]+2*v*iv+4*w*iv^2)*si^2,P[2]*(1-2*v*iv^2-8*w*iv^3)*si^3];
};

p41_cm36_hecke47(input,branch,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ii=sum(k=1,80,input[4][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    P=vector(2,j,sum(k=1,80,input[10][j][k]*u^(k-1))),
    Q=vector(2,j,sum(k=1,80,input[11][j][k]*u^(k-1))),
    U=Mod(matrix(2,2,i,j,input[12][i][j]),41),F=Mod(matrix(2,2,i,j,input[13][i][j]),41),
    D=Mod([1,0;0,14],41),delta=Mod(input[18],q)*u^0,delta3=Mod(input[19],q)*u^0,
    ar=Mod(input[20],q)*u^0,br=Mod(input[21],q)*u^0,
    rr,scale,scalem,A,B,jinv,PP,QQ,PM,QM,expected,Ft,Um,
    epsvar=varhigher("cm36e",'t),eps,vals,reps=List(),signed=vector(1681),neg,Es,
    power,aa=vector(159),bb=vector(159),HA,HB,gh,GR,GI,W,C,Fmodel);
  if(branch!=1&&branch!=2,error("CM36 branch index"));
  if(delta^2!=2||delta3^2!=3||ar^2!=-1+2*delta3/3||br^2!=1+2*delta3/3||ar*br*delta3!=1,
    error("CM36 exact root lifts"));
  if(branch==1,rr=ar;scale=u^0;scalem=ii,rr=ii*br;scale=(1+ii)/delta;scalem=(1-ii)/delta);
  if(3*rr^4+6*rr^2-1,error("CM36 exact three-division root"));
  A=if(branch==1,-9-30*ar^2,9-30*br^2);
  B=if(branch==1,-70*ar^3-42*ar,-70*br^3+42*br);
  if(A*scale^4!=-9-30*rr^2||B*scale^6!=-70*rr^3-42*rr,error("CM36 normalized actual target model"));
  if(A*scalem^4!=-9-30*rr^2||B*scalem^6!=70*rr^3+42*rr,error("CM36 opposite target model"));
  jinv=1728*4*A^3*p41l_inv(4*A^3+27*B^2,u,z);
  if(jinv^2-153542016*jinv-1790957481984,error("CM36 exact j polynomial"));
  PP=p41c36_velu(P,rr,scale,u,z);QQ=p41l_mul(p41c36_velu(Q,rr,scale,u,z),14,A,u,z);
  PM=p41c36_velu(P,-rr,scalem,u,z);QM=p41l_mul(p41c36_velu(Q,-rr,scalem,u,z),14,A,u,z);
  for(j=1,4,
    expected=if(j==1,PP,if(j==2,QQ,if(j==3,PM,QM)));
    if(expected[2]^2!=expected[1]^3+A*expected[1]+B,error("CM36 actual target curve"));
    if(p41l_mul(expected,41,A,u,z)!=[0],error("CM36 target41-torsion")));
  Um=D^-1*U*D;if(branch==2,Um=-Um);
  for(j=1,2,
    expected=p41l_add(p41l_mul(PP,lift(Um[1,j]),A,u,z),p41l_mul(QQ,lift(Um[2,j]),A,u,z),A,u,z);
    if(expected!=if(j==1,PM,QM),error("CM36 opposite maps and source i")));
  Ft=D^-1*if(branch==1,matid(2),-U)*F*D;
  for(j=1,2,
    expected=p41l_add(p41l_mul(PP,lift(Ft[1,j]),A,u,z),p41l_mul(QQ,lift(Ft[2,j]),A,u,z),A,u,z);
    if(expected!=vector(2,k,subst(lift(if(j==1,PP[k],QQ[k])),'t,phi)),error("CM36 actual Frobenius")));
  print("Actual CM36 cyclic kernels branch ",branch," and complete torsion/Frobenius PASS ",getwalltime());
  eps=Mod(Mod(1,q)*u^0*epsvar,epsvar);
  vals=p41a_eisenstein(vector(2,j,PP[j]*eps^0),vector(2,j,QQ[j]*eps^0),A*eps^0,u,z,1,epsvar);
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
  if(W*Fmodel!=matrix(20,73,n,k,subst(lift(W[input[15+branch][n],k]),'s,-u2)),
    error("CM36 complete model Frobenius descent"));
  write(path,[p41l_vec(A),p41l_vec(B),p41l_vec(jinv),
    vector(2,j,p41l_vec(PP[j])),vector(2,j,p41l_vec(QQ[j])),
    vector(2,j,p41l_vec(PM[j])),vector(2,j,p41l_vec(QM[j])),
    vector(2,i,vector(2,j,lift(Ft[i,j]))),p41m_encode(W)]);
  print("Actual CM36 branch ",branch," full20x73 values PASS ",getwalltime());
};
