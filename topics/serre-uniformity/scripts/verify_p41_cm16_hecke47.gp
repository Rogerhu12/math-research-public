\\ Independent verification uses the negative vertical kernel and direct traces.
p41v_cm16_hecke47(input,cert,path)={
  my(q=47^4,f=sum(k=1,81,input[1][k]*'t^(k-1)),z=ffgen(Mod(1,47)*f),u=Mod(Mod(1,q)*'t,f),
    ew=sum(k=1,80,input[3][k]*u^(k-1)),ii=sum(k=1,80,input[4][k]*u^(k-1)),
    P=vector(2,j,sum(k=1,80,input[10][j][k]*u^(k-1))),
    Q=vector(2,j,sum(k=1,80,input[11][j][k]*u^(k-1))),
    PP=vector(2,j,sum(k=1,80,cert[1][j][k]*u^(k-1))),
    QQ=vector(2,j,sum(k=1,80,cert[2][j][k]*u^(k-1))),
    PM=vector(2,j,sum(k=1,80,cert[3][j][k]*u^(k-1))),
    QM=vector(2,j,sum(k=1,80,cert[4][j][k]*u^(k-1))),
    delta=Mod(input[17],q)*u^0,root,scale,original,expected,add,actual,
    epsvar=varhigher("vcm16ep",'t),eps,vals,u2=Mod(Mod(1,q)*'s,'s^2+1),
    C=matrix(73,73,i,j,input[6][i][j][1]+input[6][i][j][2]*u2),
    gh,raw=matrix(20,73),W,score,g,va,vb,coef);
  for(branch=1,2,
    root=if(branch==1,ii,-ii);scale=(1+root)/delta;
    for(j=1,2,original=if(j==1,P,Q);add=p41l_add(original,[root,0],1,u,z);
      expected=[(original[1]+add[1]-root)*p41l_inv(scale^2,u,z),(original[2]+add[2])*p41l_inv(scale^3,u,z)];
      actual=if(branch==1,if(j==1,PP,QQ),if(j==1,PM,QM));
      if(j==2,actual=p41l_mul(actual,2,-11,u,z));
      if(actual!=expected,error("independent group-law CM16 vertical map and Weil scale")));
  );
  for(j=1,2,original=if(j==1,P,Q);
    expected=p41l_add(original,[-original[1],ii*original[2]],1,u,z);
    add=p41l_add(original,[0*u,0],1,u,z);scale=1+ii;
    actual=[(original[1]+add[1])*p41l_inv(scale^2,u,z),(original[2]+add[2])*p41l_inv(scale^3,u,z)];
    if(actual!=expected,error("independent CM16 horizontal1+i")));
  eps=Mod(Mod(1,q)*u^0*epsvar,epsvar);
  vals=p41j_eisenstein(vector(2,j,PM[j]*eps^0),vector(2,j,QM[j]*eps^0),-11*eps^0,u,z,1);
  for(n=1,20,
    gh=vector(42,k,lift(Mod(matrix(2,2,i,j,input[8][input[15][n]][i][j]),41)*
      Mod(matrix(2,2,i,j,input[9][k][i][j]),41)));
    for(k=1,73,score=0*eps;va=input[5][k][1];vb=input[5][k][2];
      for(l=1,42,g=gh[l];
        score+=vals[p41m_idx(g[1,1]*va[1]+g[1,2]*va[2],g[2,1]*va[1]+g[2,2]*va[2])]*
          vals[p41m_idx(g[1,1]*vb[1]+g[1,2]*vb[2],g[2,1]*vb[1]+g[2,2]*vb[2])]);
      coef=polcoef(lift(score),0,epsvar);raw[n,k]=(trace(ew*coef)-trace(ii*ew*coef)*u2)/4));
  W=raw*C;
  if(p41m_encode(W)!=cert[6],error("independent negative-vertical CM16 full20x73 values"));
  write(path,["PASS"]);print("Independent CM16 group law, negative vertical kernel and full20x73 direct trace PASS ",getwalltime());
};

