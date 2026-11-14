\\ Actual cusps and effective divisor ideals in the R102 level41 model.
p41d_act(M,ne,nsq)={
  my(a=ne[1],e=ne[2],R=Mod([a,e-a^2;1,-a],41),T);
  T=M*R/M;T/=T[2,1];a=lift(T[1,1]);e=lift(a^2+T[1,2]);20*a+setsearch(nsq,e);
};
p41d_qunit(v)={my(c=p41m_pair(v));(c[1]^2+c[2]^2)%47!=0;};
p41d_cusps(input)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z,u,phi,ew,ii,u2,ns=input[9],gg,H,pairs=input[5],
     nsq=select(e->kronecker(e,41)==-1,[1..40]),orb=vector(820),reps=List(),U=Mod([1,0;1,1],41),Fcusp=Mod([1,0;0,6],41),
     n,n1,rho,ecurve=vector(1681),e1=vector(1681),g,gh,v,w,iv,iw,score0,score1,aa,dd,ss,weights,scalars,
     B=matrix(20,73),B1=matrix(20,73),C,M,N,M0,inds,rows,cols,free,PV,C0,Pinv,K80,K2,W,A,AK,Acusp,
     vcm,c0,c,cform,cleading,cmvalue,attempt=0,ri);
  z=ffgen(Mod(1,47)*f);u=Mod(Mod(1,q)*'t,f);phi=sum(k=1,80,input[2][k]*u^(k-1));
  ew=sum(k=1,80,input[3][k]*u^(k-1));ii=sum(k=1,80,input[4][k]*u^(k-1));u2=Mod(Mod(1,q)*'s,'s^2+1);
  gg=vector(820,n,Mod(matrix(2,2,i,j,input[10][n][i][j]),41));
  H=vector(42,n,Mod(matrix(2,2,i,j,input[11][n][i][j]),41));
  for(n=1,820,if(!orb[n],listput(reps,n);n1=n;my(count=0);while(!orb[n1],orb[n1]=#reps;count++;n1=p41d_act(U,ns[n1],nsq));if(count!=41||n1!=n,error("cusp orbit"))));
  reps=Vec(reps);if(#reps!=20,error("cusp count"));rho=vector(20,n,orb[p41d_act(Fcusp,ns[reps[n]],nsq)]);
  ri=vector(20);for(n=1,20,ri[rho[n]]=n);
  for(a=0,40,for(d=0,40,
    if(a==0&&d==0,next);
    ecurve[p41m_idx(a,d)]=if(a,(41-2*a)*u^0/82,(1+ew^(41-d))*p41l_inv(2*(1-ew^(41-d)),u,z));
    e1[p41m_idx(a,d)]=if(a==1,ew^(41-d),if(a==40,-ew^d,0*u));
  ));
  scalars=vector(20,k,lift(Mod(35,41)^(k-1)));weights=vector(20,k,ew^lift(Mod(36,41)^(k-1)));
  for(n=1,20,
    gh=vector(42,l,lift(gg[reps[n]]*H[l]));
    for(k=1,73,
      v=pairs[k][1];w=pairs[k][2];score0=score1=0*u;
      for(l=1,42,
        g=gh[l];iv=g*v~;iw=g*w~;
        for(j=1,20,
          aa=p41m_idx(scalars[j]*iv[1],scalars[j]*iv[2]);dd=p41m_idx(scalars[j]*iw[1],scalars[j]*iw[2]);
          score0+=weights[j]*ecurve[aa]*ecurve[dd];
          score1+=weights[j]*(ecurve[aa]*e1[dd]+e1[aa]*ecurve[dd]);
        );
      );B[n,k]=score0;B1[n,k]=score1;
    );
  );
  print("Exact Tate constant and first coefficients complete ",getwalltime());
  C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*ii);M=B*C;N=B1*C;
  for(k=1,73,if(sum(n=1,20,M[n,k])!=0,error("exact residue sum")));
  A=matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*u2);
  if(M*matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*ii)!=matrix(20,73,n,k,subst(lift(M[ri[n],k]),'t,phi)),error("actual cusp Galois descent"));
  M0=matrix(20,73,n,k,z^0*subst(lift(lift(M[n,k])),'t,z));inds=matindexrank(M0);
  rows=Vec(inds[1]);cols=Vec(inds[2]);if(#rows!=19,error("actual cusp restriction rank"));
  free=select(k->!setsearch(Set(cols),k),[1..73]);PV=vecextract(M,rows,cols);C0=vecextract(M0,rows,cols)^-1;
  Pinv=matrix(19,19,i,j,subst(C0[i,j].pol,'t,u));for(k=1,2,Pinv=Pinv*(2*matid(19)-PV*Pinv));
  if(PV*Pinv!=matid(19),error("cusp unit minor inverse"));
  K80=matrix(73,54);for(k=1,54,K80[free[k],k]=u^0);
  my(block=-Pinv*vecextract(M,rows,free));for(i=1,19,for(k=1,54,K80[cols[i],k]=block[i,k]));
  if(M*K80!=matrix(20,54),error("actual cusp kernel"));
  K2=matrix(73,54,i,j,(trace(K80[i,j])-trace(ii*K80[i,j])*u2)/80);
  for(i=1,73,for(j=1,54,if(subst(lift(K2[i,j]),'s,ii)!=K80[i,j],error("kernel does not descend to quadratic ring"))));
  AK=A*matrix(73,54,i,j,subst(lift(K2[i,j]),'s,-u2));Acusp=vecextract(AK,free,"..");
  if(K2*Acusp!=AK,error("cusp basis Frobenius"));
  if(Acusp*matrix(54,54,i,j,subst(lift(Acusp[i,j]),'s,-u2))!=matid(54),error("cusp descent cocycle"));
  W=matrix(820,73,i,j,input[8][i][j][1]+input[8][i][j][2]*u2);
  vcm=vector(73,j,input[12][j][1]+input[12][j][2]*u2);setrand(41047);
  while(1,
    attempt++;c0=vector(54,j,random(47)+random(47)*u2)~;
    c=c0+Acusp*vector(54,j,subst(lift(c0[j]),'s,-u2))~;cform=W*K2*c;cmvalue=vcm*K2*c;
    if(!p41d_qunit(cmvalue),next);
    if(sum(n=1,820,!p41d_qunit(cform[n])),next);
    cleading=N*K80*vector(54,j,subst(lift(c[j]),'s,ii))~;
    if(sum(n=1,20,subst(lift(lift(cleading[n])),'t,z)==0),next);
    break;
  );
  print("Exact rank19 cusp restriction; rank54 full canonical space; canonical section after",attempt," tries ",getwalltime());
  [reps,orb,rho,M,N,rows,cols,free,K2,Acusp,c0,c,cform,cleading,cmvalue,matdet(vecextract(M0,rows,cols))];
};

p41d_kernel2(M,expected)={
  my(z=ffgen(Mod('s^2+1,47)),u=Mod(Mod(1,47^4)*'s,'s^2+1),nr=matsize(M)[1],nc=matsize(M)[2],
    M0=matrix(nr,nc,i,j,z^0*subst(lift(lift(M[i,j])),'s,z)),inds=matindexrank(M0),rows=Vec(inds[1]),cols=Vec(inds[2]),free,
    PV,C0,C,K,block);
  if(#rows!=expected,error(Str("unexpected kernel rank ",#rows," != ",expected)));
  free=select(k->!setsearch(Set(cols),k),[1..nc]);
  PV=vecextract(M,rows,cols);C0=vecextract(M0,rows,cols)^-1;
  C=matrix(expected,expected,i,j,subst(C0[i,j].pol,'s,u));
  for(k=1,2,C=C*(2*matid(expected)-PV*C));
  if(PV*C!=matid(expected),error("kernel unit inverse"));
  K=matrix(nc,#free);for(k=1,#free,K[free[k],k]=u^0);
  block=-C*vecextract(M,rows,free);for(i=1,expected,for(k=1,#free,K[cols[i],k]=block[i,k]));
  if(M*K!=matrix(nr,#free),error("exact kernel equality"));
  [rows,cols,free,K,matdet(vecextract(M0,rows,cols))];
};
p41d_divisors(input,cm)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
     u2=Mod(Mod(1,q)*'s,'s^2+1),z2=ffgen(Mod('s^2+1,47)),ii=sum(k=1,80,input[4][k]*u^(k-1)),
     W=matrix(820,73,i,j,input[8][i][j][1]+input[8][i][j][2]*u2),M=cm[4],K2=cm[9],Acusp=cm[10],fcoeff=cm[12],fvals=cm[13],
     pairs=List(),v,w,V20,inds,rows,cols,V,C0,C,V2,CM2,CM20,Dker,KD2,AK,fc,fg0,fg,gvals,
     ratio,scaled,R,R0,rank,Rker,IK,IP,cmrow,vcm,attempt=0,zeroSpace,checks);
  setrand(4104702);
  for(k=1,73,listput(pairs,[k,k]));
  while(#pairs<250,v=random(73)+1;w=random(73)+1;if(v==w,next);if(v>w,my(tmp=v);v=w;w=tmp);listput(pairs,[v,w]));pairs=Vec(pairs);
  V=matrix(820,250,n,k,W[n,pairs[k][1]]*W[n,pairs[k][2]]);
  V20=matrix(820,250,n,k,z2^0*subst(lift(lift(V[n,k])),'s,z2));inds=matindexrank(V20);rows=Vec(inds[1]);cols=Vec(inds[2]);
  if(#rows!=199,error(Str("actual L-square rank ",#rows)));
  pairs=vector(199,k,pairs[cols[k]]);V=vecextract(V,"..",cols);
  C0=vecextract(V20,rows,cols)^-1;C=matrix(199,199,i,j,subst(C0[i,j].pol,'s,u2));
  for(k=1,2,C=C*(2*matid(199)-vecextract(V,rows,"..")*C));
  V2=V*C;if(vecextract(V2,rows,"..")!=matid(199),error("L-square normalization"));
  print("Exact full L-square basis199 ",getwalltime());
  CM2=matrix(20,199,n,k,M[n,pairs[k][1]]*M[n,pairs[k][2]])*matrix(199,199,i,j,subst(lift(C[i,j]),'s,ii));
  CM20=matrix(20,199,n,k,z^0*subst(lift(lift(CM2[n,k])),'t,z));inds=matindexrank(CM20);
  my(dr=Vec(inds[1]),dc=Vec(inds[2]),df=select(k->!setsearch(Set(Vec(inds[2])),k),[1..199]),DP,D0,DI,DK,block);
  if(#dr!=20,error("D restriction rank"));DP=vecextract(CM2,dr,dc);D0=vecextract(CM20,dr,dc)^-1;
  DI=matrix(20,20,i,j,subst(D0[i,j].pol,'t,u));for(k=1,2,DI=DI*(2*matid(20)-DP*DI));
  DK=matrix(199,179);for(k=1,179,DK[df[k],k]=u^0);block=-DI*vecextract(CM2,dr,df);
  for(i=1,20,for(k=1,179,DK[dc[i],k]=block[i,k]));if(CM2*DK!=matrix(20,179),error("D exact kernel"));
  KD2=matrix(199,179,i,j,(trace(DK[i,j])-trace(ii*DK[i,j])*u2)/80);
  for(i=1,199,for(j=1,179,if(subst(lift(KD2[i,j]),'s,ii)!=DK[i,j],error("D kernel L2 descent"))));
  print("Exact D ideal dimension179 ",getwalltime());
  while(1,
    attempt++;fg0=vector(54,j,random(47)+random(47)*u2)~;
    fg=fg0+Acusp*vector(54,j,subst(lift(fg0[j]),'s,-u2))~;gvals=W*K2*fg;
    ratio=vector(820,n,my(a=p41m_pair(fvals[n]));gvals[n]*(a[1]-a[2]*u2)/Mod(a[1]^2+a[2]^2,q));
    scaled=matrix(820,199,n,k,ratio[n]*V2[n,k]);R=scaled-V2*vecextract(scaled,rows,"..");
    R0=matrix(820,199,n,k,z2^0*subst(lift(lift(R[n,k])),'s,z2));rank=matrank(R0);
    if(rank==106,break);if(attempt>20,error("no disjoint canonical pair"));
  );
  Rker=p41d_kernel2(R,106);IK=Rker[4];
  print("Exact K ideal dimension93; second canonical section after",attempt," tries ",getwalltime());
  vcm=vector(73,j,input[12][j][1]+input[12][j][2]*u2);
  cmrow=matrix(1,199,n,k,vcm[pairs[k][1]]*vcm[pairs[k][2]])*C;
  IP=p41d_kernel2(cmrow,1);
  zeroSpace=matrix(199,73,n,k,fvals[rows[n]]*W[rows[n],k]);
  if(V2*zeroSpace!=matrix(820,73,n,k,fvals[n]*W[n,k]),error("canonical zero representation"));
  if(CM2*matrix(199,73,n,k,subst(lift(zeroSpace[n,k]),'s,ii))!=matrix(20,73),error("zero representation at D"));
  if(R*zeroSpace!=matrix(820,73),error("zero representation at K"));
  print("Actual cusp/canonical/CM divisor spaces complete ",getwalltime());
  [pairs,rows,C,V2,[dr,dc,df,KD2],CM2,fg0,fg,gvals,Rker,cmrow,IP,zeroSpace];
};

p41d_qvec(v)=vector(#v,j,p41m_pair(v[j]));
p41d_vecmat(M)=vector(matsize(M)[1],i,vector(matsize(M)[2],j,p41l_vec(M[i,j])));
p41d_export(cm,dv,path)={
  my(K=cm[9],DK=dv[5],KK=dv[10]);
  write(path,[4,cm[1],cm[2],cm[3],p41d_vecmat(cm[4]),cm[6],cm[7],cm[8],
    p41m_encode(vecextract(K,cm[7],"..")),p41m_encode(cm[10]),p41d_qvec(cm[11]),p41d_qvec(cm[12]),
    vector(20,j,p41l_vec(cm[14][j])),p41m_pair(cm[15]),vector(80,j,lift(polcoef(cm[16].pol,j-1))),
    dv[1],dv[2],p41m_encode(dv[3]),DK[1],DK[2],DK[3],p41m_encode(vecextract(DK[4],DK[2],"..")),
    p41d_qvec(dv[7]),p41d_qvec(dv[8]),KK[1],KK[2],KK[3],p41m_encode(vecextract(KK[4],KK[2],"..")),
    [lift(polcoef(KK[5].pol,0)),lift(polcoef(KK[5].pol,1))],p41m_encode(dv[11])[1]]);
};
p41_cusp_divisors47(input,path)={
  my(cm=p41d_cusps(input),dv=p41d_divisors(input,cm));
  p41d_export(cm,dv,path);
  print("Complete actual cusp/canonical divisor certificate saved ",getwalltime());
};
