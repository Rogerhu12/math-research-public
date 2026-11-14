\\ Full actual source-fibre cubic jets, with trace evaluation left to exact Python matrices.
p41_source_cubic47(input,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    ii=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ev=varhigher("ep",'t),eps=Mod(u^0*ev,ev^4),P,Q,vals,reps=List(),neg,Es,
    aa=vector(159),bb=vector(159),power=u^0,HA,HB);
  P=vector(2,j,sum(k=0,3,sum(h=1,80,input[4][j][k+1][h]*u^(h-1))*eps^k));
  Q=vector(2,j,sum(k=0,3,sum(h=1,80,input[5][j][k+1][h]*u^(h-1))*eps^k));
  if(P[2]^2!=P[1]^3+P[1]+32+eps||Q[2]^2!=Q[1]^3+Q[1]+32+eps,error("source cubic curve"));
  if(p41j_mul(P,41,eps^0,u,z,4)!=[0]||p41j_mul(Q,41,eps^0,u,z,4)!=[0],error("source cubic torsion"));
  vals=p41a_eisenstein(P,Q,eps^0,u,z,4,ev);
  for(k=1,1680,neg=lift(Mod(-(k%41),41))+41*lift(Mod(-(k\41),41));if(k<neg,listput(reps,k+1)));
  reps=Vec(reps);Es=vector(4,n,Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(vals[reps[j]]),n-1,ev)),i-1))),q));
  for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  write(path,[p41h3j_encode(HA),p41h3j_encode(HB),vector(4,n,p41h3j_encode(Es[n]))]);
  print("Actual source cubic torsion and1680 Eisenstein jets PASS ",getwalltime());
};
