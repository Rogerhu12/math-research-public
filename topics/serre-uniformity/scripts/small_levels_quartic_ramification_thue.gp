\\ R98: exact complete Thue computations, unconditional flag 1.
small_levels_quartic_ramification_thue(input_path, output_path) =
{
  my(V=read(input_path),co,P,T,S);
  for(i=1,#V,
    co=V[i][1];
    P=co[1]*'x^3+co[2]*'x^2+co[3]*'x+co[4];
    if(!polisirreducible(P),error("Expected an irreducible cubic at row ",i));
    T=thueinit(P,1);
    S=thue(T,V[i][2]);
    write(output_path,[i,S]);
  );
  print("R98: all ",#V," Thue equations solved with flag 1.");
};
