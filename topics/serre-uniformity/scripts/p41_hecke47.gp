\\ Actual T2 and T3 on the fixed weight-two evaluation model.
p41h_eisenstein(P,Q,A,u,z)={
  my(Ps=vector(40),Qs=vector(40),num=List(),den=List(),iv,pe=vector(40),qe=vector(40),ep,eq,ev=vector(1681,i,u^0*0));
  Ps[1]=P;Qs[1]=Q;
  for(k=1,39,Ps[k+1]=p41l_add(Ps[k],P,A,u,z);Qs[k+1]=p41l_add(Qs[k],Q,A,u,z));
  for(side=1,2,
    my(base=if(side==1,P,Q),multiples=if(side==1,Ps,Qs));
    for(k=1,39,
      if(k==1,listput(num,3*base[1]^2+A);listput(den,2*base[2]),
        listput(num,multiples[k][2]-base[2]);listput(den,multiples[k][1]-base[1]));
    );
  );
  for(i=1,40,for(j=1,40,listput(num,Qs[j][2]-Ps[i][2]);listput(den,Qs[j][1]-Ps[i][1])));
  num=Vec(num);den=Vec(den);iv=p41m_batch_inverse(den,u,z);
  for(k=1,#num,num[k]*=iv[k]);
  ep=sum(k=1,39,num[k])/41;eq=sum(k=40,78,num[k])/41;pe[1]=ep;qe[1]=eq;
  for(k=1,39,pe[k+1]=pe[k]+ep-num[k];qe[k+1]=qe[k]+eq-num[39+k]);
  if(pe[40]!=-ep||qe[40]!=-eq,error("Hecke weight-one oddness axes"));
  for(k=1,40,ev[p41m_idx(k,0)]=pe[k];ev[p41m_idx(0,k)]=qe[k]);
  for(i=1,40,for(j=1,40,ev[p41m_idx(i,j)]=pe[i]+qe[j]-num[78+40*(i-1)+j]));
  for(i=0,40,for(j=0,40,if(ev[p41m_idx(-i,-j)]!=-ev[p41m_idx(i,j)],error("Hecke weight-one oddness"))));ev;
};
p41h_velu(P,r,t,u0,u,z)={
  my(iv=p41l_inv(P[1]-r,u,z));
  [P[1]+t*iv+u0*iv^2,P[2]*(1-t*iv^2-2*u0*iv^3)];
};
p41h_inv2(a,u2)={
  my(b=subst(lift(a),'s,-u2));b/lift(a*b);
};
p41h_decode(M,u2)=matrix(#M,#M[1],i,j,M[i][j][1]+M[i][j][2]*u2);
p41_hecke47(input,path,selectedell=0,selectedkr=0)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),P0=vector(2,j,sum(k=1,80,input[3][j][k]*u^(k-1))),
    Q0=vector(2,j,sum(k=1,80,input[4][j][k]*u^(k-1))),ew=sum(k=1,80,input[5][k]*u^(k-1)),
    ii=sum(k=1,80,input[6][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),z2=ffgen(Mod('s^2+1,47)),
    pairs=input[7],C=p41h_decode(input[8],u2),W=p41h_decode(input[11],u2),A1=p41h_decode(input[12],u2),
    K1=p41h_decode(input[13],u2),free=input[14],piv=input[15],ns=input[16],
    gg,H,gh,reps=List(),signed=vector(1681),neg,aa=vector(159),bb=vector(159),power=u^0,HA,HB,
    roots,root,root80,dp,Anew,Bnew,tt,uu,ww,P,Q,ev,E,B0,B1,values,M,score,g,j1,j2,sgn,v,w,
    permutation,nsq=select(x->kronecker(x,41)==-1,[1..40]),records=List(),targets,allT=List(),T,TK,HM,expected,H0,cyclic,vec,attempt=0);
  gg=vector(820,n,Mod(matrix(2,2,i,j,input[9][n][i][j]),41));
  H=vector(42,n,Mod(matrix(2,2,i,j,input[10][n][i][j]),41));
  gh=vector(820,n,vector(42,k,lift(gg[n]*H[k])));
  for(j=1,1680,neg=lift(Mod(-(j%41),41))+41*lift(Mod(-(j\41),41));
    if(j<neg,listput(reps,j+1);signed[j+1]=#reps;signed[neg+1]=-#reps));reps=Vec(reps);
  for(k=1,159,aa[k]=trace(ew*power)/4;bb[k]=-trace(ii*ew*power)/4;power*=u);
  HA=matrix(80,80,i,j,aa[i+j-1]);HB=matrix(80,80,i,j,bb[i+j-1]);
  forprime(ell=2,3,
    if(selectedell&&ell!=selectedell,next);
    roots=List();
    for(a=0,46,for(b=0,46,root=a+b*z2;
      if(if(ell==2,root^3+root+32,3*root^4+6*root^2+384*root-1)==0,listput(roots,[a,b]))));
    if(#roots!=ell+1,error("Hecke kernel roots not complete"));
    permutation=vector(820,n,p41d_act(Mod([1,0;0,ell],41),ns[n],nsq));
    values=matrix(820,73);targets=List();
    for(kr=1,#roots,
      if(selectedkr&&kr!=selectedkr,next);
      root=Mod(roots[kr][1],q)+Mod(roots[kr][2],q)*u2;
      for(k=1,2,dp=if(ell==2,3*root^2+1,12*root^3+12*root+384);
        root-=if(ell==2,root^3+root+32,3*root^4+6*root^2+384*root-1)*p41h_inv2(dp,u2));
      if(if(ell==2,root^3+root+32,3*root^4+6*root^2+384*root-1)!=0,error("Hecke Hensel kernel"));
      tt=if(ell==2,3*root^2+1,2*(3*root^2+1));uu=if(ell==2,0,4*(root^3+root+32));ww=uu+root*tt;
      Anew=1-5*tt;Bnew=32-7*ww;
      if(!p41d_qunit(4*Anew^3+27*Bnew^2),error("Hecke target bad reduction"));
      root80=subst(lift(root),'s,ii);
      P=p41h_velu(P0,root80,subst(lift(tt),'s,ii),subst(lift(uu),'s,ii),u,z);
      Q=p41h_velu(Q0,root80,subst(lift(tt),'s,ii),subst(lift(uu),'s,ii),u,z);
      Anew=subst(lift(Anew),'s,ii);Bnew=subst(lift(Bnew),'s,ii);
      if(P[2]^2!=P[1]^3+Anew*P[1]+Bnew||Q[2]^2!=Q[1]^3+Anew*Q[1]+Bnew,error("Hecke target equation"));
      Q=p41l_mul(Q,lift(Mod(ell,41)^-1),Anew,u,z);
      if(p41l_mul(P,41,Anew,u,z)!=[0]||p41l_mul(Q,41,Anew,u,z)!=[0],error("Hecke target torsion"));
      if(vector(2,j,subst(lift(P[j]),'t,subst(lift(phi),'t,phi)))!=p41l_mul(P,35,Anew,u,z),error("Hecke Frob2P"));
      if(vector(2,j,subst(lift(Q[j]),'t,subst(lift(phi),'t,phi)))!=p41l_mul(Q,35,Anew,u,z),error("Hecke Frob2Q"));
      ev=p41h_eisenstein(P,Q,Anew,u,z);
      E=Mod(matrix(80,840,i,j,lift(polcoef(lift(ev[reps[j]]),i-1))),q);
      B0=(E~*HA)*E;B1=(E~*HB)*E;M=matrix(820,73);
      for(n=1,820,for(k=1,73,v=pairs[k][1];w=pairs[k][2];score=0*u2;
        for(l=1,42,g=gh[n][l];
          j1=signed[p41m_idx(g[1,1]*v[1]+g[1,2]*v[2],g[2,1]*v[1]+g[2,2]*v[2])];
          j2=signed[p41m_idx(g[1,1]*w[1]+g[1,2]*w[2],g[2,1]*w[1]+g[2,2]*w[2])];
          sgn=sign(j1*j2);j1=abs(j1);j2=abs(j2);score+=sgn*(B0[j1,j2]+B1[j1,j2]*u2));M[n,k]=score));
      M*=C;values+=vecextract(M,permutation,"..");
      listput(targets,[p41m_pair(root),p41l_vec(Anew),p41l_vec(Bnew),vector(2,j,p41l_vec(P[j])),vector(2,j,p41l_vec(Q[j])),p41m_encode(M)]);
      print("Actual Hecke",ell," target",kr," complete ",getwalltime());
      if(selectedkr,write(path,targets[1]);return(1));
    );
    values/=ell;T=vecextract(values,piv,"..");
    if(W*T!=values,error("Actual Hecke image not in the fixed complete V1"));
    if(A1*matrix(73,73,i,j,subst(lift(T[i,j]),'s,-u2))!=T*A1,error("Hecke Frobenius descent"));
    TK=vecextract(T*K1,free,"..");if(K1*TK!=T*K1,error("Hecke canonical space"));
    if(ell==2&&trace(TK)!=-8,error("Actual T2 canonical trace"));
    listput(allT,TK);listput(records,[ell,permutation,Vec(targets),p41m_encode(T),p41m_encode(TK)]);
    print("Actual T",ell," full820-row and canonical/descent checks PASS ",getwalltime());
  );
  HM=allT[1]+2*allT[2];expected=prod(k=1,#input[17],Pol(input[17][k],'x));
  H0=matrix(54,54);forstep(k=54,0,-1,H0=H0*HM+polcoef(expected,k)*matid(54));
  if(H0!=matrix(54,54),error("Actual Hecke primitive polynomial does not annihilate"));
  setrand(4104712107);
  while(1,attempt++;
    vec=vector(54,j,Mod(random(47),q)+Mod(random(47),q)*u2)~;cyclic=matrix(54,54);
    for(j=1,54,cyclic[,j]=vec;vec=HM*vec);
    if(matrank(matrix(54,54,i,j,z2^0*subst(lift(lift(cyclic[i,j])),'s,z2)))==54,break);
    if(attempt==100,error("Hecke primitive cyclic vector not certified")));
  write(path,[Vec(records),p41m_encode(cyclic),Vec(expected)]);
  print("Actual54-dimensional Hecke spectrum and unit cyclicity PASS ",getwalltime());
};
