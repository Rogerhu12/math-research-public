\\ R97: solve every irreducible binary cubic equation with certification flag 1.
\\ thueinit(P,1) is unconditional, including the unit-group certification.
certified_thue_jobs(jobs) = {
  for(i=1,#jobs,
    my(P=Pol(jobs[i][1]));
    if(poldegree(P)!=3 || !polisirreducible(P), error("Non-irreducible cubic"));
    my(T=thueinit(P,1), V=thue(T,jobs[i][2]));
    print([i,V]);
  );
};
