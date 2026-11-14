\\ Actual j1728 elliptic divisor and B_minus4 in the R102/R110 model.
p41c4_psi41(x,A,B)={
  my(out=vector(42),q=4*(x^3+A*x+B),m);
  out[1]=0;out[2]=x^0;out[3]=x^0;
  out[4]=3*x^4+6*A*x^2+12*B*x-A^2;
  out[5]=2*(x^6+5*A*x^4+20*B*x^3-5*A^2*x^2-4*A*B*x-8*B^2-A^3);
  for(n=5,41,m=n\2;
    if(n%2,
      if(m%2==0,out[n+1]=q^2*out[m+3]*out[m+1]^3-out[m]*out[m+2]^3,
        out[n+1]=out[m+3]*out[m+1]^3-q^2*out[m]*out[m+2]^3),
      out[n+1]=out[m+1]*(out[m+3]*out[m]^2-out[m-1]*out[m+2]^2)
    );
  );out[42];
};
p41c4_lift(P,eps,ev,u,z)={
  my(x=P[1]*eps^0,y=P[2]*eps^0,dx,dy,dd);
  dd=polcoef(lift(p41c4_psi41(x+eps,1,0)),1,ev);
  dx=-polcoef(lift(p41c4_psi41(x,1,eps)),1,ev)*p41l_inv(dd,u,z);
  dy=((3*P[1]^2+1)*dx+1)*p41l_inv(2*P[2],u,z);
  x+=dx*eps;y+=dy*eps;
  if(y^2!=x^3+x+eps||p41c4_psi41(x,1,eps)!=0,error("CM4 lift equations"));
  if(p41j_mul([x,y],41,eps^0,u,z,2)!=[0],error("CM4 actual41-torsion"));[x,y];
};
p41_cm4_divisor47(input,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),ii=sum(k=1,80,input[4][k]*u^(k-1)),
    u2=Mod(Mod(1,q)*'s,'s^2+1),epsvar=varhigher("eps",'t),eps,record,P0,Qold,Q0,P,Q,wold,adjustment=0,
    Ez=ellinit([1,0],z),Pz,Qz,ewz,iiz,U,Fnew,ns=input[8],nsq=select(e->kronecker(e,41)==-1,[1..40]),fixed=List(),
    tau,gg,H,gh,ecurve,pairs=input[5],raw0=matrix(20,73),raw1=matrix(20,73),g,v,w,h,score,cc,C,A,ct1,ct2,expected,
    coarse,K1,C2,KI,W2,W,pairs2=input[13],Kfree=input[16],S=input[17],fcoeff,fvals,cm2,restriction,Zker,Bcoords,A2,BF,free,piv);
  eps=Mod(u^0*epsvar,epsvar^2);setrand(4104704);
  record=p41l_curve(1,0,f,u,z,phi,0);P0=vector(2,j,sum(k=1,80,record[5][j][k]*u^(k-1)));
  Qold=vector(2,j,sum(k=1,80,record[6][j][k]*u^(k-1)));wold=sum(k=1,80,record[7][k]*u^(k-1));
  for(k=1,40,if(wold^k==ew,adjustment=k;break));if(!adjustment,error("CM4 Weil adjustment"));
  Q0=p41l_mul(Qold,adjustment,1,u,z);
  Pz=vector(2,j,z^0*subst(lift(lift(P0[j])),'t,z));Qz=vector(2,j,z^0*subst(lift(lift(Q0[j])),'t,z));
  ewz=z^0*subst(lift(lift(ew)),'t,z);iiz=z^0*subst(lift(lift(ii)),'t,z);
  U=Mod(Mat([p41l_pointcoords(Ez,Pz,Qz,ewz,[-Pz[1],iiz*Pz[2]])~,p41l_pointcoords(Ez,Pz,Qz,ewz,[-Qz[1],iiz*Qz[2]])~]),41);
  Fnew=Mod([1,0;0,adjustment],41)^-1*Mod([0,35;1,0],41)*Mod([1,0;0,adjustment],41);
  if(U^2!=-matid(2)||matdet(U)!=1||Fnew*U!=-U*Fnew,error("CM4 matrices"));
  P=p41c4_lift(P0,eps,epsvar,u,z);Q=p41c4_lift(Q0,eps,epsvar,u,z);
  if(p41j_mul(vector(2,j,p41j_frob(P[j],phi,eps,epsvar,2)),adjustment,eps^0,u,z,2)!=Q,error("CM4 FrobP"));
  if(vector(2,j,p41j_frob(Q[j],phi,eps,epsvar,2))!=p41j_mul(P,35*adjustment,eps^0,u,z,2),error("CM4 FrobQ"));
  ct1=vector(2,j,subst(lift(P[j]),epsvar,-eps));ct2=vector(2,j,subst(lift(Q[j]),epsvar,-eps));
  for(j=1,2,
    expected=p41j_add(p41j_mul(ct1,lift(U[1,j]),eps^0,u,z,2),p41j_mul(ct2,lift(U[2,j]),eps^0,u,z,2),eps^0,u,z,2);
    if(expected!=if(j==1,[-P[1],ii*P[2]],[-Q[1],ii*Q[2]]),error("CM4 family unit action"));
  );
  for(n=1,820,if(p41d_act(U,ns[n],nsq)==n,listput(fixed,n)));fixed=Vec(fixed);
  if(#fixed!=20,error("CM4 elliptic point count"));
  tau=vector(20,n,setsearch(fixed,p41d_act(Fnew,ns[fixed[n]],nsq)));
  if(sum(n=1,20,tau[n]==n)!=2,error("CM4 rational residue points"));
  for(n=1,20,if(!tau[n]||tau[tau[n]]!=n,error("CM4 Frob permutation")));
  print("Actual CM4 Weil adjustment",adjustment," and20 elliptic points ",getwalltime());
  ecurve=p41j_eisenstein(P,Q,eps^0,u,z,2);
  gg=vector(820,n,Mod(matrix(2,2,i,j,input[9][n][i][j]),41));
  H=vector(42,n,Mod(matrix(2,2,i,j,input[10][n][i][j]),41));
  for(n=1,20,gh=vector(42,k,lift(gg[fixed[n]]*H[k]));
    for(k=1,73,score=0*eps;v=pairs[k][1];w=pairs[k][2];
      for(l=1,42,h=gh[l];score+=ecurve[p41m_idx(h[1,1]*v[1]+h[1,2]*v[2],h[2,1]*v[1]+h[2,2]*v[2])]*
        ecurve[p41m_idx(h[1,1]*w[1]+h[1,2]*w[2],h[2,1]*w[1]+h[2,2]*w[2])]);
      cc=polcoef(lift(score),0,epsvar);raw0[n,k]=(trace(ew*cc)-trace(ii*ew*cc)*u2)/4;
      cc=polcoef(lift(score),1,epsvar);raw1[n,k]=(trace(ew*cc)-trace(ii*ew*cc)*u2)/4;
    );
  );
  C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2);
  A=matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*u2);
  if(raw0!=matrix(20,73),error("CM4 raw weight2 value should vanish"));coarse=raw1*C;
  if(coarse*A!=matrix(20,73,n,k,subst(lift(coarse[tau[n],k]),'s,-u2)),error("CM4 actual coarse Frobenius"));
  print("All20 actual coarse CM4 values ",getwalltime());
  K1=matrix(73,54,n,k,input[11][n][k][1]+input[11][n][k][2]*u2);
  fcoeff=K1*vector(54,k,input[12][k][1]+input[12][k][2]*u2)~;fvals=coarse*fcoeff;
  if(sum(n=1,20,!p41d_qunit(fvals[n])),error("canonical divisor meets CM4"));
  C2=matrix(199,199,n,k,input[14][n][k][1]+input[14][n][k][2]*u2);
  KI=matrix(199,93,n,k,input[15][n][k][1]+input[15][n][k][2]*u2);
  cm2=matrix(20,199,n,k,coarse[n,pairs2[k][1]]*coarse[n,pairs2[k][2]])*C2;
  restriction=cm2*KI;Zker=p41d_kernel2(restriction,20);Bcoords=KI*Zker[4];
  if(cm2*Bcoords!=matrix(20,73),error("CM4 effective divisor kernel"));
  free=vector(73,k,Kfree[Zker[3][k]]);
  if(vecextract(Bcoords,free,"..")!=matid(73),error("CM4 basis normalized free coordinates"));
  W=matrix(820,73,n,k,input[18][n][k][1]+input[18][n][k][2]*u2);
  W2=matrix(820,199,n,k,W[n,pairs2[k][1]]*W[n,pairs2[k][2]])*C2;
  A2=vecextract(matrix(820,199,n,k,subst(lift(W2[input[19][n],k]),'s,-u2)),S,"..");
  expected=A2*matrix(199,73,n,k,subst(lift(Bcoords[n,k]),'s,-u2));BF=vecextract(expected,free,"..");
  if(Bcoords*BF!=expected||BF*matrix(73,73,n,k,subst(lift(BF[n,k]),'s,-u2))!=matid(73),error("CM4 point subspace actual descent"));
  write(path,[4,record[5],record[6],record[7],adjustment,
    vector(2,i,vector(2,j,lift(U[i,j]))),vector(2,i,vector(2,j,lift(Fnew[i,j]))),
    vector(2,i,vector(2,j,p41l_vec(polcoef(lift(P[i]),j-1,epsvar)))),
    vector(2,i,vector(2,j,p41l_vec(polcoef(lift(Q[i]),j-1,epsvar)))),
    fixed,tau,p41m_encode(coarse),p41d_qvec(fvals),Zker[1],Zker[2],Zker[3],
    p41m_encode(vecextract(Zker[4],Zker[2],"..")),
    [lift(polcoef(Zker[5].pol,0)),lift(polcoef(Zker[5].pol,1))],free,p41m_encode(BF)]);
  print("Actual B_minus4 point represented, effective divisor degree126 ",getwalltime());
};
