\\ R1119. Actual star-plus modular-symbol input, new Fricke-plus subspace.
\\ Only called by the public-CI Python consumer in the same pinned Sage image.
p47j_require(c,label)={if(!c,error(Str("Jacobi47: ",label)));};
p47j_path_matrix(v)={
  my(x=v[1],y=v[2],A,B,C,D,G);
  if(y==oo,A=1;C=0,A=numerator(y);C=denominator(y));
  if(x==oo,B=1;D=0,B=numerator(x);D=denominator(x));
  G=[A,B;C,D];
  if(matdet(G)==-1,G[,2]=-G[,2]);
  p47j_require(matdet(G)==1,"nonadjacent generator path"); G;
};
p47j_encode(M)={
  my(d=denominator(M));
  [d,vector(matsize(M)[1],i,Vec(d*M[i,]))];
};
p47j_setup(dir)={
  my(M=msinit(2209,2,1),N,P,s,E,g,G,free,T2,T3,T5,A2,A3,A5,Aq);
  N=msnew(M);
  p47j_require(msdim(M)==189 && matsize(N[1])[2]==157,"full and new dimensions");
  P=N[1]*matker(msatkinlehner(M,2209,N)-matid(157));
  p47j_require(matsize(P)==[189,73],"new Fricke plus dimension");
  p47j_require(msstar(M)==matid(189),"actual star plus");
  p47j_require(msatkinlehner(M,2209,P)==matid(73),"actual Fricke plus");
  s=mseval(M,matid(189)); E=Mat(vector(#s,i,s[i]~));
  g=mspathgens(M)[1]; G=vector(#g,i,p47j_path_matrix(g[i]));
  free=matsize(E)[1];
  p47j_require(matsize(E)[2]==189 && free<=#g,"free path dimensions");
  for(i=free+1,#g,
    p47j_require(mseval(M,matid(189),g[i])==vector(189),"elliptic path value")
  );
  print("Jacobi47: actual new/Fricke subspace and all generator paths ready.");
  T2=mshecke(M,2); T3=mshecke(M,3); T5=mshecke(M,5);
  A2=mshecke(M,2,P); A3=mshecke(M,3,P); A5=mshecke(M,5,P);
  p47j_require(T2*P==P*A2 && T3*P==P*A3 && T5*P==P*A5,"exact Hecke restrictions");
  print("Jacobi47: reconstructing only the consumed T4513 input for its new Bq coordinate.");
  Aq=mshecke(M,4513,P);
  write(Str(dir,"/input.json"),"{");
  write(Str(dir,"/input.json"),"\"pari_version\":",version(),",");
  write(Str(dir,"/input.json"),"\"full_dimension\":189,\"new_dimension\":157,\"plus_dimension\":73,");
  write(Str(dir,"/input.json"),"\"free_path_count\":",free,",\"path_count\":",#g,",");
  write(Str(dir,"/input.json"),"\"paths\":",vector(#G,i,[G[i][1,1],G[i][1,2],G[i][2,1],G[i][2,2]]),",");
  write(Str(dir,"/input.json"),"\"E\":",p47j_encode(E),",\"P\":",p47j_encode(P),",");
  write(Str(dir,"/input.json"),"\"T2\":",p47j_encode(T2),",\"T3\":",p47j_encode(T3),",\"T5\":",p47j_encode(T5),",");
  write(Str(dir,"/input.json"),"\"A2\":",p47j_encode(A2),",\"A3\":",p47j_encode(A3),",\"A5\":",p47j_encode(A5),",");
  write(Str(dir,"/input.json"),"\"Aq\":",p47j_encode(Aq),"}");
  print("Jacobi47: exact input exported inside the temporary runner directory.");
};
