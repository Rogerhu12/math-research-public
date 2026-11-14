\\ R89. Exact weight-two Jacobi coefficients on the actual new Fricke-plus space.
\\ Called in two fresh GP processes by p41_jacobi_cm_coordinates.py.
p41_require(c,label)={if(!c,error(Str("R89: ",label)));};
p41_path_matrix(v)={
  my(x=v[1],y=v[2],A,B,C,D,G);
  if(y==oo,A=1;C=0,A=numerator(y);C=denominator(y));
  if(x==oo,B=1;D=0,B=numerator(x);D=denominator(x));
  G=[A,B;C,D];
  if(matdet(G)==-1,G[,2]=-G[,2]);
  p41_require(matdet(G)==1,"nonadjacent generator path"); G;
};
p41_encode(f,m)={
  my(d=denominator(Vec(f)));
  [d,vector(m,j,d*polcoef(f,m-j))];
};
p41_jacobi_setup(dir)={
  my(M=msinit(1681,2,1),N,P,s,E,g,G,Hfull,H,cp);
  N=msnew(M); P=N[1]*matker(msatkinlehner(M,1681,N)-matid(117));
  p41_require(msdim(M)==144 && matsize(P)[2]==54,"actual new space");
  p41_require(msstar(M)==matid(144),"star plus");
  p41_require(msatkinlehner(M,1681,P)==matid(54),"Fricke plus");
  s=mseval(M,matid(144)); E=Mat(vector(#s,i,s[i]~));
  g=mspathgens(M)[1]; G=vector(#g,i,p41_path_matrix(g[i]));
  p41_require(matsize(E)==[287,144] && #g==289,"free and elliptic paths");
  for(i=288,289,p41_require(mseval(M,matid(144),g[i])==vector(144),"elliptic path value"));
  Hfull=mshecke(M,2)+2*mshecke(M,3);
  H=mshecke(M,2,P)+2*mshecke(M,3,P); cp=charpoly(H);
  p41_require(denominator(H)==2,"Hecke denominator");
  p41_require(gcd(cp,charpoly(Hfull)/cp)==1,"spectral complement");
  writebin(Str(dir,"/setup.bin"),[M,P,E,g,G,Hfull,H]);
  write(Str(dir,"/paths.json"),vector(#G,i,[G[i][1,1],G[i][1,2],G[i][2,1],G[i][2,2]]));
  print("R89: actual modular-symbol space and 289 paths constructed.");
};
p41_jacobi_project(dir)={
  my(a=read(Str(dir,"/setup.bin")),M,P,E,Hfull,H,rows,ref,J,w,cp,Q,B,L,Jnew,
     K,cc,co,fac,ji,jd,prime=0,detmod=0,out,f,m,kap,s8,r3,r7,xi,sgn,c8,c3,c7);
  M=a[1];P=a[2];E=a[3];Hfull=a[6];H=a[7];
  rows=read(Str(dir,"/rows.gp")); ref=read(Str(dir,"/reference.gp"));
  J=matrix(144,4);
  for(k=1,4,
    p41_require(rows[k][288]==0 && rows[k][289]==0,"raw elliptic relation");
    w=matinverseimage(E,rows[k][1..287]~);
    p41_require(#w==144 && E*w==rows[k][1..287]~,"exact relative cohomology class");
    J[,k]=w;
  );
  cp=charpoly(H);Q=matimage(subst(cp,'x,Hfull));
  p41_require(matsize(Q)==[144,90],"full complementary space");
  B=concat(P,Q); L=B^-1*J; Jnew=L[1..54,];
  p41_require(B*L==J,"actual Hecke projection");
  K=matrix(54,54);w=Jnew[,1];
  for(k=1,54,K[,k]=w;w=H*w);
  p41_require(matrank(K)==54,"nonzero reference on all 54 eigenlines");
  cc=K^-1*Jnew; co=vector(4,k,sum(i=1,54,cc[i,k]*'x^(i-1))); fac=factor(cp);
  p41_require(matsize(fac)[1]==8 && vecsum(vector(8,i,poldegree(fac[i,1])))==54,"eight actual fields");
  jd=denominator(Jnew);ji=jd*Jnew;
  forprime(l=1009,2000,
    w=ji[,1];K=matrix(54,54);
    for(k=1,54,K[,k]=w;w=lift(Mod(H,l)*w));
    detmod=lift(matdet(Mod(K,l)));
    if(detmod,prime=l;break);
  );
  p41_require(prime!=0,"small-prime cyclic certificate");
  out=vector(8);
  for(i=1,8,
    f=fac[i,1];m=poldegree(f);
    p41_require(Vec(f)==ref[i][1],"reference field identity");
    kap=Mod(ref[i][2],f);
    c8=Mod(co[2],f);c3=Mod(co[3],f);c7=Mod(co[4],f);
    s8=c8/2;r3=30*c3/kap;r7=10*c7/kap;
    p41_require(r3^2==Mod(ref[i][3]^2,f),"independent D=-3 square");
    p41_require(r7^2==Mod(ref[i][4]^2,f),"independent D=-7 square");
    p41_require(s8^2==Mod(ref[i][5]^2,f),"independent D=-8 square");
    sgn=[lift(r3/Mod(ref[i][3],f)),lift(r7/Mod(ref[i][4],f)),lift(s8/Mod(ref[i][5],f))];
    p41_require(vector(3,j,sgn[j]^2)==[1,1,1],"actual signs");
    xi=108*r7+1080*s8+80+16*r3/3;
    p41_require(xi!=0,"actual translation nonzero");
    out[i]=[Vec(f),p41_encode(lift(c8),m),p41_encode(lift(c3),m),p41_encode(lift(c7),m),
            p41_encode(lift(s8),m),p41_encode(lift(r3),m),p41_encode(lift(r7),m),p41_encode(lift(xi),m),sgn];
  );
  write(Str(dir,"/projection.json"),"{\"pari_version\":",version(),",");
  write(Str(dir,"/projection.json"),"\"full_dimension\":144,\"new_fricke_dimension\":54,\"complement_dimension\":90,");
  write(Str(dir,"/projection.json"),"\"two_times_hecke_matrix\":",vector(54,i,Vec(2*H[i,])),",");
  write(Str(dir,"/projection.json"),"\"projected_common_denominator\":",jd,",");
  write(Str(dir,"/projection.json"),"\"projected_integer_columns\":",vector(4,k,Vec(ji[,k])),",");
  write(Str(dir,"/projection.json"),"\"cyclic_prime\":",prime,",\"cyclic_determinant\":",detmod,",");
  write(Str(dir,"/projection.json"),"\"field_data\":",out,"}");
  print("R89: all signed coefficients and independent square checks passed; cyclic determinant mod ",prime," = ",detmod,".");
};
