\\ Actual CM(-7) point and CM(-8) fixed support for Q2, in the R102 model.
p41q_endo(P,rr,v,alpha,u,z)={
  my(iv=p41l_inv(P[1]-rr,u,z),ai=p41l_inv(alpha,u,z));
  [(P[1]+v*iv)*ai^2,P[2]*(1-v*iv^2)*ai^3];
};
p41q_lift(P0,A,B,eps,ev,u,z,order)={
  my(x=P0[1]*eps^0,y=P0[2]*eps^0,dx,dy,dd);
  if(order==1,return([x,y]));
  dd=polcoef(lift(p41c4_psi41(x+eps,A,B)),1,ev);
  dx=-polcoef(lift(p41c4_psi41(x,A,B+eps)),1,ev)*p41l_inv(dd,u,z);
  dy=((3*P0[1]^2+A)*dx+1)*p41l_inv(2*P0[2],u,z);
  x+=dx*eps;y+=dy*eps;
  if(y^2!=x^3+A*x+B+eps||p41c4_psi41(x,A,B+eps)!=0,error("Q2 CM actual Hensel lift"));
  if(p41j_mul([x,y],41,A*eps^0,u,z,order)!=[0],error("Q2 CM actual torsion jet"));[x,y];
};
p41_q2_support47(input,path)={
  my(q=47^4,disc=input[11],A=if(disc==-7,-35,-30),B=if(disc==-7,-98,56),
    order=if(disc==-7,2,1),ns=input[8],f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),
    u=Mod(Mod(1,q)*'t,f),phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ii=sum(k=1,80,input[4][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),record,P0,Qold,Q0,wold,adjustment=0,
    Ez=ellinit([A,B],z),Pz,Qz,ewz,ss0,ss,rr,alpha,v,UP,UQ,U,Fnew,expected,nsq=select(e->kronecker(e,41)==-1,[1..40]),
    fixed=List(),tau,epsvar=varhigher("q2ep",'t),eps,P,Q,vals,reps=List(),signed=vector(1681),neg,Es,
    aa=vector(159),bb=vector(159),power,HA,HB,gh,C,Fmodel,GR,GI,W,coeffs=vector(order));
  if(disc!=-7&&disc!=-8,error("Q2 support discriminant"));
  setrand(if(disc==-7,410471507,410471508));
  record=p41l_curve(A,B,f,u,z,phi,0);
  P0=vector(2,j,sum(k=1,80,record[5][j][k]*u^(k-1)));
  Qold=vector(2,j,sum(k=1,80,record[6][j][k]*u^(k-1)));wold=sum(k=1,80,record[7][k]*u^(k-1));
  for(k=1,40,if(wold^k==ew,adjustment=k;break));if(!adjustment,error("Q2 CM Weil calibration"));
  Q0=p41l_mul(Qold,adjustment,A,u,z);
  ss0=sqrt(if(disc==-7,-7,-2)*z^0);ss=subst(ss0.pol,'t,u);
  for(k=1,3,ss-=(ss^2-if(disc==-7,-7,-2))*p41l_inv(2*ss,u,z));
  rr=if(disc==-7,(-7+ss)/2,4*u^0);alpha=if(disc==-7,(1+ss)/2,ss);v=3*rr^2+A;
  if(rr^3+A*rr+B!=0||A-5*v!=alpha^4*A||B-7*rr*v!=alpha^6*B,error("Q2 actual self-isogeny model"));
  UP=p41q_endo(P0,rr,v,alpha,u,z);UQ=p41q_endo(Q0,rr,v,alpha,u,z);
  if(UP[2]^2!=UP[1]^3+A*UP[1]+B||UQ[2]^2!=UQ[1]^3+A*UQ[1]+B,error("Q2 actual self-isogeny target"));
  Pz=vector(2,j,z^0*subst(lift(lift(P0[j])),'t,z));Qz=vector(2,j,z^0*subst(lift(lift(Q0[j])),'t,z));
  ewz=z^0*subst(lift(lift(ew)),'t,z);
  U=Mod(Mat([p41l_pointcoords(Ez,Pz,Qz,ewz,vector(2,j,z^0*subst(lift(lift(UP[j])),'t,z)))~,
    p41l_pointcoords(Ez,Pz,Qz,ewz,vector(2,j,z^0*subst(lift(lift(UQ[j])),'t,z)))~]),41);
  if(matdet(U)!=2||U^2-if(disc==-7,U,0)+2*matid(2)!=matrix(2,2),error("Q2 CM characteristic polynomial"));
  for(j=1,2,expected=p41l_add(p41l_mul(P0,lift(U[1,j]),A,u,z),p41l_mul(Q0,lift(U[2,j]),A,u,z),A,u,z);
    if(expected!=if(j==1,UP,UQ),error("Q2 actual lifted CM matrix")));
  Fnew=Mod([1,0;0,adjustment],41)^-1*Mod([0,35;1,0],41)*Mod([1,0;0,adjustment],41);
  if(Fnew*U!=(if(disc==-7,matid(2),matrix(2,2))-U)*Fnew,error("Q2 CM Frobenius conjugation"));
  for(n=1,820,if(p41d_act(U,ns[n],nsq)==n,listput(fixed,n)));fixed=Vec(fixed);
  if(#fixed!=if(disc==-7,1,20),error("Q2 actual fixed support cardinality"));
  tau=vector(#fixed,n,setsearch(fixed,p41d_act(Fnew,ns[fixed[n]],nsq)));
  for(n=1,#fixed,if(!tau[n]||tau[tau[n]]!=n,error("Q2 support Frobenius")));
  print("Actual CM",disc," calibrated torsion and fixed support ",fixed," ",getwalltime());
  eps=Mod(Mod(1,q)*u^0*epsvar,epsvar^order);
  P=p41q_lift(P0,A,B,eps,epsvar,u,z,order);Q=p41q_lift(Q0,A,B,eps,epsvar,u,z,order);
  if(p41j_mul(vector(2,j,p41j_frob(P[j],phi,eps,epsvar,order)),adjustment,A*eps^0,u,z,order)!=Q,error("Q2 CM jet FrobP"));
  if(vector(2,j,p41j_frob(Q[j],phi,eps,epsvar,order))!=p41j_mul(P,35*adjustment,A*eps^0,u,z,order),error("Q2 CM jet FrobQ"));
  vals=p41a_eisenstein(P,Q,A*eps^0,u,z,order,epsvar);
  for(j=1,1680,neg=lift(Mod(-(j%41),41))+41*lift(Mod(-(j\41),41));
    if(j<neg,listput(reps,j+1);signed[j+1]=#reps;signed[neg+1]=-#reps));
  reps=Vec(reps);
  Es=vector(order,k,Mod(matrix(80,840,i,j,lift(polcoef(lift(polcoef(lift(vals[reps[j]]),k-1,epsvar)),i-1))),q));vals=0;
  power=u^0;for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  gh=vector(#fixed,n,vector(42,k,lift(Mod(matrix(2,2,i,j,input[9][fixed[n]][i][j]),41)*Mod(matrix(2,2,i,j,input[10][k][i][j]),41))));
  C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2);
  Fmodel=matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*u2);
  for(degree=0,order-1,
    GR=p41a_trace_coefficient(Es,HA,degree,gh,input[5],signed);
    GI=p41a_trace_coefficient(Es,HB,degree,gh,input[5],signed);W=(GR+u2*GI)*C;
    if(W*Fmodel!=matrix(#fixed,73,n,k,subst(lift(W[tau[n],k]),'s,-u2)),error("Q2 actual support jet descent"));
    coeffs[degree+1]=p41m_encode(W);
    print("Actual CM",disc," coefficient",degree," full",#fixed,"x73 PASS ",getwalltime()));
  write(path,[A,B,disc,record[5],record[6],record[7],adjustment,p41l_vec(ss),
    vector(2,i,vector(2,j,lift(U[i,j]))),vector(2,i,vector(2,j,lift(Fnew[i,j]))),fixed,tau,coeffs,
    vector(2,i,vector(order,j,p41l_vec(polcoef(lift(P[i]),j-1,epsvar)))),
    vector(2,i,vector(order,j,p41l_vec(polcoef(lift(Q[i]),j-1,epsvar))))]);
};

