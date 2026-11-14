\\ Actual first jets of the four normalized3-isogenies.
p41h3j_encode(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,lift(M[i,j])));
p41h3j_velu(P,root,tt,uu,eps,ev,u,z)={
  my(d=P[1]-root,b=p41l_inv(polcoef(lift(d),0,ev),u,z)*eps^0);
  b*=2-d*b;if(d*b!=1,error("Hecke jet denominator"));
  [P[1]+tt*b+uu*b^2,P[2]*(1-tt*b^2-2*uu*b^3)];
};
p41_hecke3_jets47(input,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    ii=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ev=varhigher("ep",'t),eps=Mod(u^0*ev,ev^2),P,Q,root0=Mod(input[6][1],q)+Mod(input[6][2],q)*ii,root,tt,uu,ww,A,B,
    vals,reps=List(),neg,Es,aa=vector(159),bb=vector(159),power=u^0,HA,HB);
  P=vector(2,j,sum(k=0,1,sum(h=1,80,input[4][j][k+1][h]*u^(h-1))*eps^k));
  Q=vector(2,j,sum(k=0,1,sum(h=1,80,input[5][j][k+1][h]*u^(h-1))*eps^k));
  root=root0-12*root0*p41l_inv(12*root0^3+12*root0+384,u,z)*eps;
  if(3*root^4+6*root^2+12*(32+eps)*root-1!=0,error("actual3-kernel jet equation"));
  tt=2*(3*root^2+1);uu=4*(root^3+root+32+eps);ww=uu+root*tt;A=1-5*tt;B=32+eps-7*ww;
  P=p41h3j_velu(P,root,tt,uu,eps,ev,u,z);Q=p41h3j_velu(Q,root,tt,uu,eps,ev,u,z);
  Q=p41j_mul(Q,14,A,u,z,2);
  if(P[2]^2!=P[1]^3+A*P[1]+B||Q[2]^2!=Q[1]^3+A*Q[1]+B,error("actual target jet curve"));
  if(p41j_mul(P,41,A,u,z,2)!=[0]||p41j_mul(Q,41,A,u,z,2)!=[0],error("actual target jet torsion"));
  vals=p41a_eisenstein(P,Q,A,u,z,2,ev);
  for(k=1,1680,neg=lift(Mod(-(k%41),41))+41*lift(Mod(-(k\41),41));if(k<neg,listput(reps,k+1)));
  reps=Vec(reps);if(#reps!=840,error("target jet odd representatives"));
  Es=vector(2,n,Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(vals[reps[j]]),n-1,ev)),i-1))),q));
  for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  write(path,[p41h3j_encode(HA),p41h3j_encode(HB),vector(2,n,p41h3j_encode(Es[n])),
    vector(2,j,vector(2,n,p41l_vec(polcoef(lift(P[j]),n-1,ev)))),
    vector(2,j,vector(2,n,p41l_vec(polcoef(lift(Q[j]),n-1,ev))))]);
  print("Actual normalized3-isogeny jet and1680 Eisenstein jets PASS ",getwalltime());
};
