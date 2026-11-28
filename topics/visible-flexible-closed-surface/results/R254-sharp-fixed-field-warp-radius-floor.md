# R254. Sharp fixed-position metric floor under arbitrary target-radius redesign

**Proved.** Fix a positive definite first fundamental form $A=\bigl(\begin{smallmatrix}E&F\\F&G\end{smallmatrix}\bigr)$ at a point, so $E>0$, $G>0$ and $EG-F^2>0$. The meridional coordinate and position field are fixed. For any angular target radius $a>0$ put $D_a=\operatorname{diag}(1,a^2)$ and $r(a)=\|D_a^{-1/2}A D_a^{-1/2}-I\|_{\rm op}$. Then
$$
\inf_{a>0}r(a)=
\begin{cases}
\sqrt{(E-1)^2+(2-E)F^2/G},&E<2,\\
E-1,&E\ge2.
\end{cases}
$$
For $E<2$ one minimizer has $a^2=G/(2-E)$. Consequently the right side at any material point lower-bounds the uniform metric error for **every** smooth target warp $a(s)$ on that same position field, regardless of its parametrization or number of radial coefficients.

**Proof.** Write $y=a^2$. The two extreme generalized eigenvalues of $(A,D_a)$ are the minimum and maximum over $v\ne0$ of $(v^TAv)/(v_1^2+yv_2^2)$. Both are nonincreasing functions of $y$ because each numerator is positive. Call them $\lambda_-(y),\lambda_+(y)$. We minimize the larger of the nonincreasing $\lambda_+-1$ and nondecreasing $1-\lambda_-$. They cross exactly when their sum of eigenvalues $E+G/y$ equals 2. If $E<2$, the two errors agree at $y=G/(2-E)$, so this is a global minimum. At that point the symmetric whitened error matrix is traceless and has first diagonal entry $E-1$ and off-diagonal entry $F/\sqrt y$. Its norm gives the formula. If $E\ge2$, the sum is greater than 2 at every finite $y$, and $r(a)=\lambda_+(y)-1$ decreases weakly to $E-1$ as $y\to\infty$. For $E\ge2$ and $F\ne0$ the largest eigenvalue is strictly larger than $E$ for every finite $y$, so only the limit attains the infimum in the extended domain. If $F=0$ and $E\ge2$, any sufficiently large finite $y$ has $\lambda_+=E$ and attains the same value. This proves the infimum in all cases. A single point lower-bounds a supremum, so allowing a separate radius at this point can only relax any smooth radial-warp optimization. $\square$

**Exact common-radius feasibility at one meridional coordinate.** For a prescribed $0\le\epsilon<1$, define $U=1+\epsilon$ and $L=1-\epsilon$. All material angles at this $s$ admit one radius with error at most $\epsilon$ if and only if some $y>0$ satisfies, at **every** angle,
$$
E\ge L,\quad E\le U,\quad G-Ly\ge0,\quad Uy-G\ge0,\quad
(E-L)(G-Ly)\ge F^2,\quad (U-E)(Uy-G)\ge F^2.
$$
Indeed these are exactly the diagonal and determinant conditions for $A-LD_a$ and $UD_a-A$ to be positive semidefinite. Each condition in $y$ is affine, including when $E$ equals an endpoint, so feasibility is the intersection of intervals with the positive half-line. No continuity across different $s$ is assumed by this relaxation.

**Scope.** This floor applies to the saved position field in its fixed meridional coordinate. A change of $X$, of that coordinate, or of the meridional component of the target can change the floor. The formula does not obstruct existence of a different isometric embedding. Numerical evaluations on the actual strong candidates are in the [companion numerical note](../notes/2026-11-28-2ecf-current-warp-radius-witness-floors.md).
