\\ R74: exact modular-symbol certificate, PARI/GP 2.19.0.
\\ Run: gp -q -f p41_twist_nonvanishing.gp
\\ The JSON block between CERTIFICATE_BEGIN and CERTIFICATE_END is the small
\\ finite-field certificate checked by verify_p41_twist_certificate.py.
\\ No floating-point L-values, modular-form database, or stored ms structure.

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

krylov_row_matrix(v,H) = {
  my(n=matsize(H)[1], out=matrix(n,n), row=v);
  for(i=1,n,out[i,]=row;row=row*H);
  out;
};

gettime();
M=msinit(1681,2,-1);
require(msdim(M)==143,"dimension of star-minus space");
require(msstar(M)==-matid(143),"star-minus sign");
N=msnew(M);
require(matsize(N[1])[2]==117,"new cuspidal dimension");
W=msatkinlehner(M,1681,N);
require(W^2==matid(117),"Fricke involution");
P=N[1]*matker(W-matid(117));
require(matsize(P)[2]==54,"new Fricke-plus dimension");
require(msatkinlehner(M,1681,P)==matid(54),"Fricke-plus restriction");
T2=mshecke(M,2,P);
T3=mshecke(M,3,P);
H=T2+2*T3;
require(T2*T3==T3*T2,"Hecke commutativity");
require(denominator(H)==6,"Hecke matrix denominator");
cp=charpoly(H);
require(poldegree(gcd(cp,deriv(cp)))==0,"54 distinct Hecke eigenvalues");
fac=factor(cp);
degrees=vector(matsize(fac)[1],i,poldegree(fac[i,1]));
require(degrees==[2,3,3,4,4,8,12,18],"Hecke field degrees");
require(vector(matsize(fac)[1],i,fac[i,2])==vector(8,i,1),"factor multiplicities");
factor_coefficients=vector(8,i,Vec(fac[i,1]));

{for(i=1,2,
  D=[-43,-163][i];
  require(qfbclassno(D)==1,Str("class number ",D));
  require(kronecker(D,41)==1,Str("41 split in K ",D));
  require(kronecker(D,47)==1,Str("47 split in K ",D));
);}
v43=twist_row(M,P,-43);
v163=twist_row(M,P,-163);
require(denominator(v43)==1 && denominator(v163)==1,"integral twist rows");
K43=krylov_row_matrix(v43,H);
K163=krylov_row_matrix(v163,H);
require(matrank(K43)==54 && matrank(K163)==54,"rational Krylov ranks");
d43=lift(matdet(Mod(K43,1009)));
d163=lift(matdet(Mod(K163,1009)));
require(d43==161 && d163==415,"finite-field Krylov determinants");
T47=mshecke(M,47,P);
require(gcd(denominator(T47),47)==1,"T47 denominator invertible at 47");
d47=lift(matdet(Mod(T47,47)));
require(d47==28,"all eigenforms ordinary at 47");
print("All exact checks passed; elapsed milliseconds: ",gettime());
print("Krylov determinants mod 1009: ",[d43,d163]);
print("det(T47) mod 47: ",d47);
print("Hecke factorization: ",fac);

print("CERTIFICATE_BEGIN");
print("{");
print("\"pari_version\":",version(),",");
print("\"level\":1681,\"weight\":2,\"star\":-1,\"fricke\":1,\"new\":true,");
print("\"dimension\":54,\"hecke_generator\":\"T2+2*T3\",\"hecke_denominator\":6,");
print("\"factor_coefficients_descending\":",factor_coefficients,",");
print("\"modulus\":1009,\"hecke_matrix_mod\":",json_matrix(lift(Mod(H,1009))),",");
print("\"twist43_exact\":",v43,",");
print("\"twist163_exact\":",v163,",");
print("\"krylov_determinants_mod\":[161,415],");
print("\"ordinary_prime\":47,\"ordinary_determinant_mod\":28,");
print("\"ordinary_matrix_mod\":",json_matrix(lift(Mod(T47,47))));
print("}");
print("CERTIFICATE_END");
