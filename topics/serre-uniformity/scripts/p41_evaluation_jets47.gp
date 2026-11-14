\\ Actual first-order jets at all820 R102 evaluation points.
p41e_lift(P,eps,ev,u,z)={
  my(x=P[1]*eps^0,y=P[2]*eps^0,dd,dx,dy);
  dd=polcoef(lift(p41c4_psi41(x+eps,1,32)),1,ev);
  dx=-polcoef(lift(p41c4_psi41(x,1,32+eps)),1,ev)*p41l_inv(dd,u,z);
  dy=((3*P[1]^2+1)*dx+1)*p41l_inv(2*P[2],u,z);
  x+=dx*eps;y+=dy*eps;
  if(y^2!=x^3+x+32+eps||p41c4_psi41(x,1,32+eps)!=0,error("evaluation jet lift"));
  if(p41j_mul([x,y],41,eps^0,u,z,2)!=[0],error("evaluation actual41-torsion"));[x,y];
};
p41_evaluation_jets47(input,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),P0=vector(2,j,sum(k=1,80,input[3][j][k]*u^(k-1))),
    Q0=vector(2,j,sum(k=1,80,input[4][j][k]*u^(k-1))),ew=sum(k=1,80,input[5][k]*u^(k-1)),
    ii=sum(k=1,80,input[6][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    epsvar=varhigher("eps",'t),eps=Mod(u^0*epsvar,epsvar^2),P,Q,ev,reps=List(),signed=vector(1681),
    neg,E0,E1,aa=vector(159),bb=vector(159),power=u^0,HA,HB,G0R,G0I,G1R,G1I,T,
    gg,H,gh,pairs=input[7],M0=matrix(820,73),M1=matrix(820,73),score0,score1,v,w,g,j1,j2,sgn,C,A,W,tau=input[12]);
  P=p41e_lift(P0,eps,epsvar,u,z);Q=p41e_lift(Q0,eps,epsvar,u,z);
  if(vector(2,j,p41j_frob(P[j],phi,eps,epsvar,2))!=Q,error("evaluation jet FrobP"));
  if(vector(2,j,p41j_frob(Q[j],phi,eps,epsvar,2))!=p41j_mul(P,35,eps^0,u,z,2),error("evaluation jet FrobQ"));
  print("Actual evaluation fibre41-torsion jets ",getwalltime());
  ev=p41j_eisenstein(P,Q,eps^0,u,z,2);
  for(j=1,1680,
    neg=lift(Mod(-(j%41),41))+41*lift(Mod(-(j\41),41));
    if(j<neg,listput(reps,j+1);signed[j+1]=#reps;signed[neg+1]=-#reps);
  );reps=Vec(reps);if(#reps!=840,error("evaluation signed torsion representatives"));
  E0=Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(ev[reps[j]]),0,epsvar)),i-1))),q);
  E1=Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(ev[reps[j]]),1,epsvar)),i-1))),q);
  for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  G0R=(E0~*HA)*E0;G0I=(E0~*HB)*E0;
  T=(E1~*HA)*E0;G1R=T+T~;T=(E1~*HB)*E0;G1I=T+T~;
  print("Actual derivative trace Gram matrices ",getwalltime());
  gg=vector(820,n,Mod(matrix(2,2,i,j,input[9][n][i][j]),41));
  H=vector(42,n,Mod(matrix(2,2,i,j,input[10][n][i][j]),41));
  gh=vector(820,n,vector(42,k,lift(gg[n]*H[k])));
  for(n=1,820,for(k=1,73,
    v=pairs[k][1];w=pairs[k][2];score0=0*u2;score1=0*u2;
    for(l=1,42,g=gh[n][l];
      j1=signed[p41m_idx(g[1,1]*v[1]+g[1,2]*v[2],g[2,1]*v[1]+g[2,2]*v[2])];
      j2=signed[p41m_idx(g[1,1]*w[1]+g[1,2]*w[2],g[2,1]*w[1]+g[2,2]*w[2])];
      sgn=sign(j1*j2);j1=abs(j1);j2=abs(j2);
      score0+=sgn*(G0R[j1,j2]+G0I[j1,j2]*u2);
      score1+=sgn*(G1R[j1,j2]+G1I[j1,j2]*u2);
    );M0[n,k]=score0;M1[n,k]=score1;
  ));
  C=matrix(73,73,i,j,input[8][i][j][1]+input[8][i][j][2]*u2);
  A=matrix(73,73,i,j,input[11][i][j][1]+input[11][i][j][2]*u2);
  W=matrix(820,73,i,j,input[13][i][j][1]+input[13][i][j][2]*u2);
  if(M0*C!=W,error("evaluation jet constant terms differ from actual model"));M1*=C;
  if(M1*A!=matrix(820,73,n,k,subst(lift(M1[tau[n],k]),'s,-u2)),error("evaluation jet actual Frobenius"));
  write(path,[vector(2,i,vector(2,j,p41l_vec(polcoef(lift(P[i]),j-1,epsvar)))),
    vector(2,i,vector(2,j,p41l_vec(polcoef(lift(Q[i]),j-1,epsvar)))),p41m_encode(M1)]);
  print("All820 actual first-order evaluation jets saved ",getwalltime());
};
