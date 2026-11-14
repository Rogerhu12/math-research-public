\\ R79: exact squared ratios of B_{-8} and B_{-4} on all eight Hecke fields.
\\ The factor 1/4 is proved from Cai--Shu--Tian and Gauss sums in R79.
\\ The square root exported below is algebraic, without choosing the actual
\\ sign of the Mordell--Weil point ratio.

default(parisizemax,536870912);
default(parisize,67108864);
require(condition,label) = {
  if(!condition, print("FAIL: ",label); quit(1));
};
json_matrix(A) = {
  my(n=matsize(A)[1], out="[");
  for(i=1,n,
    if(i>1,out=concat(out,","));
    out=concat(out,Str(Vec(A[i,])));
  );
  concat(out,"]");
};
twist_row(M,P,D) = {
  my(m=abs(D), out=vector(matsize(P)[2]));
  for(a=1,m-1,out+=kronecker(D,a)*mseval(M,P,[a/m,oo]));
  out;
};

gettime();
M=msinit(1681,2,-1);
N=msnew(M);
W=msatkinlehner(M,1681,N);
P=N[1]*matker(W-matid(117));
require(msdim(M)==143 && matsize(P)[2]==54,"actual space");
require(msstar(M)==-matid(143) && msatkinlehner(M,1681,P)==matid(54),"signs");
H=mshecke(M,2,P)+2*mshecke(M,3,P);
require(denominator(H)==6,"Hecke denominator");
v4=twist_row(M,P,-4);
v8=twist_row(M,P,-8);
cp=charpoly(H); fac=factor(cp);
require(matsize(fac)[1]==8,"eight Hecke fields");
out=vector(8);
{for(i=1,8,
  f=fac[i,1]; m=poldegree(f);
  V=matker(subst(f,'x,H));
  C=matinverseimage(V,H*V);
  require(matsize(V)[2]==m && V*C==H*V,"factor restriction");
  w4=v4*V; w8=v8*V;
  K=matrix(m,m); w=w4;
  for(j=1,m,K[j,]=w;w=w*C);
  coeff=((K~)^-1*(w8/4)~)~;
  rho=sum(j=1,m,coeff[j]*'x^(j-1));
  require(w4*subst(rho,'x,C)==w8/4,"exact ratio on this factor");
  fy=subst(f,'x,'y);
  roots=nfroots(fy,'x^2-Mod(subst(rho,'x,'y),fy));
  require(#roots==2,"a nonzero square in the actual coefficient field");
  root=lift(roots[1]);
  require(Mod(root,fy)^2==Mod(subst(rho,'x,'y),fy),"square identity");
  denrho=denominator(Vec(rho)); denroot=denominator(Vec(root));
  out[i]=[Vec(f),denrho,vector(m,j,denrho*polcoef(rho,m-j)),denroot,vector(m,j,denroot*polcoef(root,m-j))];
);}
print("All eight exact Hecke-field square identities passed; milliseconds: ",gettime());
print("CERTIFICATE_BEGIN");
print("{");
print("\"pari_version\":",version(),",");
print("\"level\":1681,\"weight\":2,\"star\":-1,\"fricke\":1,\"new\":true,");
print("\"dimension\":54,\"hecke_generator\":\"T2+2*T3\",\"hecke_denominator\":6,");
print("\"twist_reference\":\"p41_small_cm_certificate.json\",");
print("\"twist_reference_sha256\":\"717ca26634c9613a3d8677dda68895d7d945cca370563b76c299e820d24c5f51\",");
print("\"one_algebraic_square_root_no_point_sign\":true,");
print("\"six_times_hecke_matrix\":",json_matrix(6*H),",");
print("\"fields\":[");
{for(i=1,8,
  print("{\"factor_descending\":",out[i][1],",\"ratio_denominator\":",out[i][2],",\"ratio_numerator_descending\":",out[i][3],",\"root_denominator\":",out[i][4],",\"root_numerator_descending\":",out[i][5],"}",if(i<8,",",""));
);}
print("]");
print("}");
print("CERTIFICATE_END");
quit;
