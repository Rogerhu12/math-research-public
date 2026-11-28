# R255. Sharp two-angle obstruction for an arbitrary angularly invariant metric

**Proved.** At a fixed meridional coordinate $s$, identify material tangent coordinates $(\partial_s,\partial_u)$ at two angles. Let their positive definite first forms be $A,C$. Allow an arbitrary positive definite $B(s)$, including an off-diagonal term, as common target. Define $d(A,B)=\|B^{-1/2}AB^{-1/2}-I\|_{\rm op}$. Put
$$
L=\max\{\lambda_{\max}(A,C),\lambda_{\max}(C,A)\},
$$
where $\lambda_{\max}(A,C)=\max_{v\ne0}(v^T A v)/(v^T C v)$. Then
$$
\min_{B>0}\max\{d(A,B),d(C,B)\}=\frac{L-1}{L+1}.
$$
The arithmetic mean $(A+C)/2$ attains this two-angle optimum. For arbitrarily many angles the maximum of this expression over angle pairs lower-bounds the uniform metric error for any common $B(s)$. The lower bound survives any simultaneous invertible change of coordinates applied to all tangent forms at that ring.

**Proof.** The condition $d(A,B)\le e$ is equivalent to $(1-e)B\preceq A\preceq(1+e)B$. The same holds for $C$. Thus if $e<1$, both $A\preceq(1+e)C/(1-e)$ and the reversed comparison hold. They imply $L\le(1+e)/(1-e)$, or $e\ge(L-1)/(L+1)$. The same lower bound is immediate for $e\ge1$. To prove attainment, simultaneously reduce $C$ to the identity and $A$ to a positive diagonal by congruence. For an eigenvalue $\lambda$ of that diagonal, the two relative errors against $(A+C)/2$ are respectively $(\lambda-1)/(\lambda+1)$ and its negative. Their maximal absolute value over all eigenvalues is $(L-1)/(L+1)$. The equivalence by Loewner order also proves invariance under simultaneous congruence. Any member of a multi-angle feasible family must satisfy every two-angle test, which proves the last bound. $\square$

**Scope.** The angular identification is part of the material coordinate choice. This gives a necessary condition for rectifying the fixed field by any rotationally invariant target. A position change or angle-dependent material relabeling can change the bound. For more than two angles this statement claims a lower bound, without claiming an optimal shared target or the feasibility of caps.

The [five-field numerical comparison](../notes/2026-11-28-2ecf-five-actual-angular-pair-floors.md) evaluates this bound on the independent G11 grid.
