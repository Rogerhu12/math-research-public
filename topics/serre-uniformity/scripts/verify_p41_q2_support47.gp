\\ Independent group-law CM action and direct all-column trace verification.
p41v_q2_support47(input,cert,path)={
  my(q=47^4,disc=cert[3],A=cert[1],B=cert[2],order=if(disc==-7,2,1),
    f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    phi=sum(k=1,80,input[2][k]*u^(k-1)),ew=sum(k=1,80,input[3][k]*u^(k-1)),
    ii=sum(k=1,80,input[4][k]*u^(k-1)),u2=Mod(Mod(1,q)*'s,'s^2+1),
    epsvar=varhigher("q2verify",'t),eps=Mod(Mod(1,q)*u^0*epsvar,epsvar^order),
    P=vector(2,j,sum(k=0,order-1,sum(l=1,80,cert[14][j][k+1][l]*u^(l-1))*eps^k)),
    Q=vector(2,j,sum(k=0,order-1,sum(l=1,80,cert[15][j][k+1][l]*u^(l-1))*eps^k)),
    P0=vector(2,j,polcoef(lift(P[j]),0,epsvar)),Q0=vector(2,j,polcoef(lift(Q[j]),0,epsvar)),
    Qold=vector(2,j,sum(k=1,80,cert[5][j][k]*u^(k-1))),
    ss=sum(k=1,80,cert[8][k]*u^(k-1)),rr,alpha,v,plus,V,expected,
    U=Mod(matrix(2,2,i,j,cert[9][i][j]),41),F=Mod(matrix(2,2,i,j,cert[10][i][j]),41),
    Ez=ellinit([A,B],z),Pz,Qz,ewz,fixed=List(),ns=input[8],R,T,ff=cert[11],tau=cert[12],
    vals,raw,gh,score,g,v1,v2,coef,C,Fmodel);
  if(P[2]^2!=P[1]^3+A*P[1]+B+eps||Q[2]^2!=Q[1]^3+A*Q[1]+B+eps,error("independent Q2 actual curve jets"));
  if(p41j_mul(P,41,A*eps^0,u,z,order)!=[0]||p41j_mul(Q,41,A*eps^0,u,z,order)!=[0],error("independent Q2 actual41-torsion"));
  if(p41l_mul(Qold,cert[7],A,u,z)!=Q0,error("independent Q2 Weil basis adjustment"));
  Pz=vector(2,j,z^0*subst(lift(lift(P0[j])),'t,z));Qz=vector(2,j,z^0*subst(lift(lift(Q0[j])),'t,z));
  ewz=z^0*subst(lift(lift(ew)),'t,z);
  if(ellweilpairing(Ez,Pz,Qz,41)!=ewz,error("independent Q2 primitive Weil pairing"));
  if(ss^2!=if(disc==-7,-7,-2)||subst(lift(ss),'t,phi)!=-ss,error("independent Q2 CM square root"));
  rr=if(disc==-7,(-7+ss)/2,4*u^0);alpha=if(disc==-7,(1+ss)/2,ss);v=3*rr^2+A;
  if(rr^3+A*rr+B!=0||A-5*v!=alpha^4*A||B-7*rr*v!=alpha^6*B,error("independent Q2 CM endomorphism model"));
  for(j=1,2,V=if(j==1,P0,Q0);plus=p41l_add(V,[rr,0],A,u,z);
    V=[(V[1]+plus[1]-rr)*p41l_inv(alpha^2,u,z),(V[2]+plus[2])*p41l_inv(alpha^3,u,z)];
    expected=p41l_add(p41l_mul(P0,lift(U[1,j]),A,u,z),p41l_mul(Q0,lift(U[2,j]),A,u,z),A,u,z);
    if(V!=expected,error("independent group-law Q2 CM action")));
  for(j=1,2,expected=p41j_add(p41j_mul(P,lift(F[1,j]),A*eps^0,u,z,order),p41j_mul(Q,lift(F[2,j]),A*eps^0,u,z,order),A*eps^0,u,z,order);
    if(expected!=vector(2,k,p41j_frob(if(j==1,P[k],Q[k]),phi,eps,epsvar,order)),error("independent Q2 actual Frobenius jets")));
  for(n=1,820,R=Mod([ns[n][1],ns[n][2]-ns[n][1]^2;1,-ns[n][1]],41);
    if(U*R==R*U||U*R==-R*U,listput(fixed,n)));
  if(Vec(fixed)!=ff,error("independent Q2 actual fixed necklaces"));
  for(n=1,#ff,R=Mod([ns[ff[n]][1],ns[ff[n]][2]-ns[ff[n]][1]^2;1,-ns[ff[n]][1]],41);
    T=F*R/F;T/=T[2,1];
    if([lift(T[1,1]),lift(T[1,1]^2+T[1,2])]!=ns[ff[tau[n]]],error("independent Q2 necklace Frobenius")));
  print("Independent Q2 CM",disc," group law, exact torsion, Weil root and fixed support PASS ",getwalltime());
  vals=p41j_eisenstein(P,Q,A*eps^0,u,z,order);
  C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2);
  Fmodel=matrix(73,73,i,j,input[7][i][j][1]+input[7][i][j][2]*u2);
  raw=vector(order,k,matrix(#ff,73));
  for(n=1,#ff,
    gh=vector(42,k,lift(Mod(matrix(2,2,i,j,input[9][ff[n]][i][j]),41)*Mod(matrix(2,2,i,j,input[10][k][i][j]),41)));
    for(k=1,73,score=0*eps;v1=input[5][k][1];v2=input[5][k][2];
      for(l=1,42,g=gh[l];score+=vals[p41m_idx(g[1,1]*v1[1]+g[1,2]*v1[2],g[2,1]*v1[1]+g[2,2]*v1[2])]*
        vals[p41m_idx(g[1,1]*v2[1]+g[1,2]*v2[2],g[2,1]*v2[1]+g[2,2]*v2[2])]);
      for(j=0,order-1,coef=polcoef(lift(score),j,epsvar);raw[j+1][n,k]=(trace(ew*coef)-trace(ii*ew*coef)*u2)/4));
  );
  for(k=1,order,raw[k]=raw[k]*C;
    if(p41m_encode(raw[k])!=cert[13][k],error("independent direct Q2 all73 coefficient values"));
    if(raw[k]*Fmodel!=matrix(#ff,73,n,j,subst(lift(raw[k][tau[n],j]),'s,-u2)),error("independent Q2 coefficient descent")));
  write(path,["PASS"]);
  print("Independent Q2 CM",disc," all",order*#ff,"x73 direct trace coefficients PASS ",getwalltime());
};

