\\ Partial research checkpoint: V3, -B4, and a principal-divisor Poincare scalar.
p41g_mat(v,u)=matrix(#v,#v[1],i,j,v[i][j][1]+v[i][j][2]*u);
p41g_conj(M,u)=matrix(matsize(M)[1],matsize(M)[2],i,j,subst(lift(M[i,j]),'s,-u));
p41g_reduction(M,z)=matrix(matsize(M)[1],matsize(M)[2],i,j,z^0*subst(lift(lift(M[i,j])),'s,z));
p41g_inv(v,u)={my(c=p41m_pair(v));(c[1]-c[2]*u)/Mod(c[1]^2+c[2]^2,47^4);};
p41g_trace(A,u)={my(n=matsize(A)[1],v=vector(n,k,random(47)+random(47)*u)~);[v,v+A*vector(n,k,subst(lift(v[k]),'s,-u))~];};
p41g_normalize(M,rank,u,z)={
  my(M0=p41g_reduction(M,z),inds=matindexrank(M0),rows=Vec(inds[1]),cols=Vec(inds[2]),V,PV,C0,C,W);
  if(#rows!=rank,error(Str("normalize rank ",#rows," expected ",rank)));
  V=vecextract(M,"..",cols);PV=vecextract(V,rows,"..");C0=vecextract(M0,rows,cols)^-1;
  C=matrix(rank,rank,i,j,subst(C0[i,j].pol,'s,u));for(k=1,2,C=C*(2*matid(rank)-PV*C));
  W=V*C;if(vecextract(W,rows,"..")!=matid(rank),error("normalized unit minor"));[W,rows,cols,C];
};
p41g_flip(S,AS,V2,P2,A2,u,z,label)={
  my(cf,cg,f,g,ratio,scaled,R,rank,K,Af,attempt=0);
  while(1,
    attempt++;cf=p41g_trace(AS,u);f=S*cf[2];
    if(sum(n=1,820,!p41d_qunit(f[n])),next);
    cg=p41g_trace(AS,u);g=S*cg[2];ratio=vector(820,n,g[n]*p41g_inv(f[n],u));
    scaled=matrix(820,199,n,k,ratio[n]*V2[n,k]);R=scaled-V2*vecextract(scaled,P2,"..");
    rank=matrank(p41g_reduction(R,z));if(rank==126,break);if(attempt>20,error("flip rank attempts"));
  );
  K=p41d_kernel2(R,126);Af=vecextract(A2*p41g_conj(K[4],u),K[3],"..");
  if(K[4]*Af!=A2*p41g_conj(K[4],u)||Af*p41g_conj(Af,u)!=matid(73),error("flip actual descent"));
  print(label," actual residual divisor after",attempt," tries ",getwalltime());
  [K,Af,cf,cg,f,g];
};
p41g_checkpoint(input)={
  my(q=47^4,u=Mod(Mod(1,q)*'s,'s^2+1),z=ffgen(Mod('s^2+1,47)),
    W=p41g_mat(input[1],u),A1=p41g_mat(input[2],u),tau=input[3],K1=p41g_mat(input[4],u),
    cf=vector(54,j,input[5][j][1]+input[5][j][2]*u)~,pairs2=input[6],C2=p41g_mat(input[7],u),P2=input[8],
    V2=matrix(820,199,n,k,W[n,pairs2[k][1]]*W[n,pairs2[k][2]])*C2,A2,
    KI=p41g_mat(input[9],u),KZ=p41g_mat(input[10],u),B=KI*KZ,AB=p41g_mat(input[11],u),WB,
    f=W*K1*cf,pairs=List(),a,b,residual,lambda,norm,added,V3a,V3,P3,A3,nB,U,pairsU=List(),UV,U0,vseed,v,R,rank,colker,AW,S,
    negB,neg2B,doubleB,attempt=0,normdata);
  if(vecextract(V2,P2,"..")!=matid(199),error("source V2"));
  A2=vecextract(p41g_conj(vecextract(V2,tau,".."),u),P2,"..");WB=V2*B;
  setrand(41047117);
  for(k=1,200,listput(pairs,[random(73)+1,random(199)+1]));pairs=Vec(pairs);
  lambda=vector(200,k,W[P2[pairs[k][2]],pairs[k][1]]*p41g_inv(f[P2[pairs[k][2]]],u));
  residual=matrix(820,200,n,k,V2[n,pairs[k][2]]*(W[n,pairs[k][1]]-lambda[k]*f[n]));
  norm=p41g_normalize(residual,126,u,z);added=norm[1];
  V3a=matrix(820,199,n,k,f[n]*V2[n,k]*p41g_inv(f[P2[k]],u));
  V3a-=added*vecextract(V3a,norm[2],"..");V3=matconcat([V3a,added]);P3=concat(P2,norm[2]);
  if(vecextract(V3,P3,"..")!=matid(325),error("actual V3 normalized basis"));
  A3=vecextract(p41g_conj(vecextract(V3,tau,".."),u),P3,"..");
  print("Actual complete V3 dimension325 ",getwalltime());
  negB=p41g_flip(WB,AB,V2,P2,A2,u,z,"MinusB4");
  [pairs,lambda,norm,V3,P3,A3,negB];
};

p41n_run(input)={
  my(q=47^4,u=Mod(Mod(1,q)*'s,'s^2+1),W=p41g_mat(input[1],u),A=p41g_mat(input[2],u),Z=p41g_mat(input[13],u),
    f=sum(k=1,81,input[14][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),t=Mod(Mod(1,q)*'t,f),
    ii=sum(k=1,80,input[16][k]*t^(k-1)),M=matrix(20,73,n,k,sum(j=1,80,input[12][n][k][j]*t^(j-1))),
    records=vector(2),seed,c,tv,dv,zv,attempt,nd,nz,normv,scalar,lt,logv);
  setrand(4104711702);
  for(side=1,2,
    attempt=0;while(1,
      attempt++;seed=p41g_trace(A,u);c=seed[2];tv=W*c;
      if(sum(n=1,820,!p41d_qunit(tv[n])),next);
      zv=Z*c;if(sum(n=1,20,!p41d_qunit(zv[n])),next);
      dv=M*vector(73,j,subst(lift(c[j]),'s,ii))~;
      if(sum(n=1,20,subst(lift(lift(dv[n])),'t,z)==0),next);
      break;
    );records[side]=[seed,tv,dv,zv];print("Actual moving section",side," after",attempt," tries ",getwalltime());
  );
  nd=prod(n=1,20,records[1][3][n])*p41l_inv(prod(n=1,20,records[2][3][n]),t,z);
  nz=prod(n=1,20,records[1][4][n])*p41g_inv(prod(n=1,20,records[2][4][n]),u);
  normv=subst(lift(nz),'s,ii)*p41l_inv(nd,t,z);
  for(j=1,79,if(polcoef(lift(normv),j)!=0,error("actual norm is not rational47")));
  scalar=polcoef(lift(normv),0);lt=scalar^46-1;
  if(lift(lt)%47,error("principal unit for logarithm"));logv=(lt-lt^2/2+lt^3/3)/46;
  print("Actual norm on B4=",lift(scalar),", log47 mod47^4=",lift(logv),", divided by47=",lift(logv)/47);
  [records,nd,nz,scalar,logv];
};
