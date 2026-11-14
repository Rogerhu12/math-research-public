\\ R94: actual source correspondence and all 53 trace-zero Hecke directions.
\\ Invoked by p41_full_chow_heegner.py with a 512 MB PARI stack.
p41c_require(c,s)={if(!c,error(Str("R94: ",s)));};
p41c_encode(f,m)={my(d=denominator(Vec(f)));[d,vector(m,j,d*polcoef(f,m-j))];};
p41c_mob(G,z)={
  if(z==oo,if(G[2,1]==0,oo,G[1,1]/G[2,1]),
    if(G[2,1]*z+G[2,2]==0,oo,(G[1,1]*z+G[1,2])/(G[2,1]*z+G[2,2])));
};
p41_chow_setup(dir)={
  my(M=msinit(1681,2,-1),N,P,H,v4,ns,tr,B,cache=Map(),C,ff,l,weights,vs,
     a,b,c,A,B0,C0,D,G,be,k,KM,w,cc,F,fac,kap,S,sig,tn,ref,source,Sfull,Sbasis,Sden);
  N=msnew(M);P=N[1]*matker(msatkinlehner(M,1681,N)-matid(117));
  p41c_require(msdim(M)==143 && matsize(P)[2]==54,"source space");
  p41c_require(msstar(M)==-matid(143) && msatkinlehner(M,1681,P)==matid(54),"source signs");
  H=mshecke(M,2,P)+2*mshecke(M,3,P);v4=mseval(M,P,[1/4,3/4]);
  ref=read(Str(dir,"/reference.gp"));
  p41c_require(6*H==matrix(54,54,i,j,ref[1][i][j]),"R79 actual Hecke basis");
  ns=read(Str(dir,"/indices.gp"));p41c_require(#ns==54 && ns[1]==1,"basis list");
  B=matrix(54,54);tr=vector(54);
  for(i=1,54,
    C=matid(54);ff=factor(ns[i]);
    for(j=1,matsize(ff)[1],
      l=ff[j,1];p41c_require(ff[j,2]==1 && l!=41,"squarefree and prime-to-level index");
      if(!mapisdefined(cache,l),mapput(cache,l,mshecke(M,l,P)));
      C=C*mapget(cache,l);
    );
    B[,i]=(v4*C)~;tr[i]=trace(C);
  );
  p41c_require(denominator(B)==1 && lift(matdet(Mod(B,1009)))==832,"complete Hecke basis");
  weights=read(Str(dir,"/Sweights.gp"));vs=vector(54);
  for(i=1,#weights,
    a=weights[i][1];b=weights[i][2];c=weights[i][3];
    if(b==41,A=1;B0=a;C0=0;D=1,
      C0=lift(1/Mod(a-b,41));A=lift(Mod(a*C0,41));
      while(gcd(A,C0)!=1,A+=41);
      be=bezout(A,C0);D=be[1];B0=-be[2];
      k=lift(Mod(1-D,41)/Mod(C0,41));D+=C0*k;B0+=A*k;
    );
    p41c_require(A*D-B0*C0==1,"SL2 lift of actual unordered pair");
    G=[41*D,-B0;-1681*C0,41*A];
    vs+=c*mseval(M,P,[p41c_mob(G,1/4),p41c_mob(G,3/4)]);
  );
  p41c_require(#weights==841 && denominator(vs)==1,"actual S correspondence row");
  KM=matrix(54,54);w=v4;
  for(j=1,54,KM[,j]=w~;w=w*H);
  cc=KM^-1*concat(Mat([ref[2]~,vs~]),B);F=charpoly(H);fac=factor(F);
  kap=sum(j=1,54,cc[j,1]*'x^(j-1));sig=sum(j=1,54,cc[j,2]*'x^(j-1));
  S=vector(8,i,lift(Mod(sig,fac[i,1])/Mod(kap,fac[i,1])));
  for(i=1,8,p41c_require((Mod(S[i],fac[i,1])-1)^2==41-Mod(kap,fac[i,1])/2,"actual commuting-involution identity"));
  tn=vector(54,i,sum(j=1,54,cc[j,i+2]*'x^(j-1)));
  Sfull=lift(chinese(vector(8,i,Mod(S[i],fac[i,1]))));
  Sbasis=B^-1*KM*vector(54,j,polcoef(Sfull,j-1))~;Sden=denominator(Sbasis);
  writebin(Str(dir,"/chow_source.bin"),[H,v4,B,ns,tr,vs,S,kap,tn,F]);
  source=Str(dir,"/source.json");
  write(source,"{\"source_star\":-1,\"source_dimension\":54,\"source_basis_determinant_mod1009\":832,");
  write(source,"\"source_hecke_basis_columns\":",vector(54,j,Vec(B[,j])),",");
  write(source,"\"source_S_row_exact\":",vs,",\"S_hecke_coefficients\":",[Sden,Vec(Sden*Sbasis)],",\"hecke_traces\":",tr,"}");
  print("R94: actual 54-element squarefree Hecke basis and S correspondence verified.");
};
p41_chow_project(dir)={
  my(a=read(Str(dir,"/setup.bin")),geom=read(Str(dir,"/chow_source.bin")),
     ref=read(Str(dir,"/reference.gp")),M,P,E,Hfull,H,rows,R,J,Q,L,V,blocks,block_basis,
     F,fac,W,offset=0,m,f,Hf,Lf,K,w,cc,co,kap,S,r3,nu,xi,tn,tr,den,
     rawratios,directions,out=vector(8),Xi=matrix(54,53),rankXi,left,leftenc,right,rightenc,
     v,pivot,prime=0,rankmod=0,fp);
  M=a[1];P=a[2];E=a[3];Hfull=a[6];H=a[7];F=charpoly(H);fac=factor(F);
  p41c_require(F==geom[10],"source and target Hecke eigenlabels");
  rows=read(Str(dir,"/chow_rows.gp"));p41c_require(#rows==161,"all translation inputs");
  for(j=1,#rows,p41c_require(#rows[j]==289 && rows[j][288]==0 && rows[j][289]==0,"all generator relations"));
  R=matrix(287,#rows,i,j,rows[j][i]);J=matinverseimage(E,R);
  p41c_require(matsize(J)==[144,#rows] && E*J==R,"actual relative cohomology functionals");
  p41c_require(gcd(F,charpoly(Hfull)/F)==1,"exact cuspidal spectral projection");
  Q=matimage(subst(F,'x,Hfull));L=concat(P,Q)^-1*J;L=L[1..54,];
  blocks=vector(8,i,matker(subst(fac[i,1],'x,H)));
  block_basis=blocks[1];for(i=2,8,block_basis=concat(block_basis,blocks[i]));
  W=block_basis^-1*L;
  for(i=1,8,
    f=fac[i,1];m=poldegree(f);V=blocks[i];Hf=matinverseimage(V,H*V);
    p41c_require(matsize(V)==[54,m] && V*Hf==H*V,"actual field block");
    Lf=W[(offset+1)..(offset+m),];K=matrix(m,m);w=Lf[,1];
    for(j=1,m,K[,j]=w;w=Hf*w);
    p41c_require(matrank(K)==m,"reference Jacobi coefficient in every field");
    cc=K^-1*Lf;
    co=vector(#rows,k,Mod(sum(j=1,m,cc[j,k]*'x^(j-1)),f));
    p41c_require(co[1]==1,"coefficient ratio normalization");
    kap=Mod(geom[8],f);S=Mod(geom[7][i],f);r3=30*co[2]/kap;
    p41c_require(r3==Mod(ref[4][i],f),"R89 actual r3");
    rawratios=vector(#rows,j,p41c_encode(lift(co[j]),m));directions=vector(53);
    for(k=1,53,
      tn=Mod(geom[9][k+1],f);tr=geom[5][k+1];den=gcd(54,tr);
      nu=10*((co[3*k]+S*co[3*k+1])/kap+co[3*k+2]);
      xi=(108*nu-20*tr-4*tr*r3/3)/den;
      if(k==1,p41c_require(xi==Mod(ref[3][i],f),"R89 actual T2 translation"));
      if(i==1 && k==2,p41c_require(xi==Mod((-45*'x-615)/2,f),"explicit T3 translation"));
      directions[k]=[p41c_encode(lift(tn),m),p41c_encode(lift(nu),m),p41c_encode(lift(xi),m)];
      for(j=1,m,Xi[offset+j,k]=polcoef(lift(xi),j-1));
    );
    out[i]=[Vec(f),p41c_encode(lift(S),m),rawratios,directions];offset+=m;
  );
  rankXi=if(denominator(Xi)%1009,matrank(Mod(Xi,1009)),0);
  if(rankXi<53,rankXi=matrank(Xi));
  leftenc=[];rightenc=[];
  if(rankXi<53,
    left=matker(Xi~);leftenc=vector(matsize(left)[2]);
    for(k=1,#leftenc,
      v=left[,k];pivot=1;while(v[pivot]==0,pivot++);v/=v[pivot];den=denominator(v);
      leftenc[k]=[den,Vec(den*v)];
    );
    p41c_require(Xi~*left==matrix(53,#leftenc),"exact left kernel");
    right=matker(Xi);rightenc=vector(matsize(right)[2]);
    for(k=1,#rightenc,
      v=right[,k];pivot=1;while(v[pivot]==0,pivot++);v/=v[pivot];den=denominator(v);
      rightenc[k]=[den,Vec(den*v)];
    );
    p41c_require(Xi*right==matrix(54,#rightenc),"exact zero-translation directions");
  );
  forprime(l=1009,2000,
    if(denominator(Xi)%l,
      rankmod=matrank(Mod(Xi,l));if(rankmod==rankXi,prime=l;break);
    );
  );
  p41c_require(prime!=0,"exact full translation rank");
  fp=Str(dir,"/chow_projection.json");den=denominator(L);
  write(fp,"{\"projected_common_denominator\":",den,",");
  write(fp,"\"projected_integer_columns\":",vector(#rows,j,Vec(den*L[,j])),",");
  write(fp,"\"xi_rank\":",rankXi,",\"xi_rank_prime\":",prime,",\"xi_rank_mod_prime\":",rankmod,",");
  write(fp,"\"xi_left_kernel\":",leftenc,",\"xi_right_kernel\":",rightenc,",\"field_data\":",out,"}");
  print("R94: every one of the 53 actual translations computed; rank = ",rankXi," (also mod ",prime,").");
};
