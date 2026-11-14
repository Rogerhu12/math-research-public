\\ Independent group-law verification of the nonself T2 CM targets.
p41v_t2_cm_targets47(input,cert,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    ew=sum(k=1,80,input[3][k]*u^(k-1)),ii=sum(k=1,80,input[4][k]*u^(k-1)),
    u2=Mod(Mod(1,q)*'s,'s^2+1),epsvar=varhigher("t2cmverify",'t),eps=Mod(Mod(1,q)*u^0*epsvar,epsvar),
    C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2),
    c,rec,A,B,rr,v,AA,BB,P,Q,PP,QQ,add,expected,vals,gh,raw,score,g,va,vb,coef,W);
  for(n=1,#cert,c=input[10][n];rec=cert[n];A=c[2];B=c[3];rr=Mod(c[7],q)*u^0;v=3*rr^2+A;
    AA=Mod(rec[2],q)*u^0;BB=Mod(rec[3],q)*u^0;
    if(A-5*v!=AA||B-7*rr*v!=BB,error("independent T2 CM target coefficients"));
    P=vector(2,j,sum(k=1,80,c[4][j][k]*u^(k-1)));Q=vector(2,j,sum(k=1,80,c[5][j][k]*u^(k-1)));
    PP=vector(2,j,sum(k=1,80,rec[6][j][k]*u^(k-1)));QQ=vector(2,j,sum(k=1,80,rec[7][j][k]*u^(k-1)));
    add=p41l_add(P,[rr,0],A,u,z);expected=[P[1]+add[1]-rr,P[2]+add[2]];
    if(PP!=expected,error("independent group-law T2 target P"));
    add=p41l_add(Q,[rr,0],A,u,z);expected=[Q[1]+add[1]-rr,Q[2]+add[2]];
    if(p41l_mul(QQ,2,AA,u,z)!=expected,error("independent group-law T2 target Q and Weil scale"));
    if(PP[2]^2!=PP[1]^3+AA*PP[1]+BB||QQ[2]^2!=QQ[1]^3+AA*QQ[1]+BB,error("independent actual target curve"));
    if(p41l_mul(PP,41,AA,u,z)!=[0]||p41l_mul(QQ,41,AA,u,z)!=[0],error("independent target41-torsion"));
    vals=p41j_eisenstein(vector(2,j,PP[j]*eps^0),vector(2,j,QQ[j]*eps^0),AA*eps^0,u,z,1);
    gh=vector(42,k,lift(Mod(matrix(2,2,i,j,input[8][c[8]][i][j]),41)*Mod(matrix(2,2,i,j,input[9][k][i][j]),41)));
    raw=matrix(1,73);
    for(k=1,73,score=0*eps;va=input[5][k][1];vb=input[5][k][2];
      for(l=1,42,g=gh[l];score+=vals[p41m_idx(g[1,1]*va[1]+g[1,2]*va[2],g[2,1]*va[1]+g[2,2]*va[2])]*
        vals[p41m_idx(g[1,1]*vb[1]+g[1,2]*vb[2],g[2,1]*vb[1]+g[2,2]*vb[2])]);
      coef=polcoef(lift(score),0,epsvar);raw[1,k]=(trace(ew*coef)-trace(ii*ew*coef)*u2)/4);
    W=raw*C;if(p41m_encode(W)!=rec[8],error("independent all73 T2 target values"));
    print("Independent T2 CM target",c[1]," group law and all73 direct trace values PASS ",getwalltime());
  );
  \\ The omitted ascending CM12 branch is the actual dual isogeny.
  c=input[10][1];A=c[2];B=c[3];rr=2*u^0;v=3*rr^2+A;
  P=vector(2,j,sum(k=1,80,c[4][j][k]*u^(k-1)));Q=vector(2,j,sum(k=1,80,c[5][j][k]*u^(k-1)));
  PP=vector(2,j,sum(k=1,80,input[11][1][j][k]*u^(k-1)));QQ=vector(2,j,sum(k=1,80,input[11][2][j][k]*u^(k-1)));
  for(j=1,2,
    expected=if(j==1,P,Q);add=p41l_add(expected,[rr,0],A,u,z);
    expected=[(expected[1]+add[1]-rr)/4,(expected[2]+add[2])/8];
    if(expected!=if(j==1,p41l_mul(PP,2,0,u,z),QQ),error("actual CM12 ascending branch dual composition")));
  write(path,["PASS"]);
  print("Actual ascending CM12 dual returns CM3 with basis (2P,21Q) after Weil calibration PASS ",getwalltime());
};

