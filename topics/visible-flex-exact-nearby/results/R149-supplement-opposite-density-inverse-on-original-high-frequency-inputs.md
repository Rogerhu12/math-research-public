# R149 ASQ13. Exceptional original labels in the true signed waist operator

Let $E$ be any set of original positive frequencies above the ordinary reference head, with $P_E$ its orthogonal projection. This includes the exceptional set of ASQ11 or a full high tail. Let $m=\min E$ if it is nonempty, and let $g_1=\max_{n\in E}g_n$, $g_2=\max_{n\in E}g_n/(4n)$ and $t=\max_{n\in E}g_n/(4n)^{1/3}$, or any certified larger values. The original directions are unit vectors in the real reflection lines, not coordinate masses with two independent signs.

## An exact opposite-sign transfer to the original input

Decompose the full inverse density $S^{-1}$ as $C'+D'$ with its original same-sign and opposite-sign projections. The off-diagonal and diagonal parts of $S^{-1}S=Id$ are $C'D+D'C=0$ and $C'C+D'D=Id$. Thus
$$
       DC^{-1}=-(C')^{-1}D',\qquad
       C^{-1}=C'-D'(C')^{-1}D'.                             \tag{ASQ13.1}
$$
These identities hold first on $L^2$. Apply them below to a finite Fourier sum, then use the uniform bounds and density for an infinite $E$. Both inverses are actual same-sign density inverses. For the inverse lift $\psi=p^{-1}$ on the real axis one has $\inf\psi'>1/1.0251>.975$, $|\psi''|<(1/6)/.9749^3<.181$. The once integrated kernel and the two Schur sums in ASQ12 show $\|D'\|_{0\to0}<.088$ and hence $\|(C')^{-1}\|_{0\to0}<1.12$. Also $\|D\|_{0\to0}<.08$ by ASQ12.

On $S_\sigma$ for $\sigma=1/256$, $|p'-1|<1/10$ by the complete complex derivative estimate in ASQ12. Write $p(z)=z+h(z)$; for $w$ in $S_{.9\sigma}$, $z\mapsto w-h(z)$ maps the closed strip of height $h_0<\sigma$ into itself if $|\operatorname{Im} w|\le.9 h_0$, because $h$ is real on the real axis and $|\operatorname{Im}h(z)|\le.1|\operatorname{Im}z|$. This map contracts by $1/10$ on the closed strip in the ordinary complex metric. Its unique fixed point defines the analytic inverse $\psi$. Throughout $S_{.9\sigma}$ one has $|\psi'-1|\le1/9$; thus $8/9\le\operatorname{Re}\psi'\le10/9$. Set $a=4(.9)\sigma=9/640$.

For $j,n>0$ the opposite-sign entries of $D'$ are bounded by $\exp[-a(n+8j/9)]$ by downward contour shift. For equal signs the entries of $Q_{97}C'$ are bounded by $\exp[-a(n-10j/9)]$, $1\le j\le96$, by an upward shift in the original phase $ny-j\psi(y)$. There is no Jacobian in either integral after the genuine density change of variables. Put
$$
 d_E=\left(\sum_{n\in E}(4n g_n)^2 e^{-2a n}\right)^{1/2}.
$$
The normalized real-line estimates follow from the two conjugate blocks by orthogonality. The sums in the output coordinate give
$$
 \|D'\bar G P_E\|_0<6.4d_E,\qquad
 \|Q_{97}C'\bar G P_E\|_0<44d_E,
$$
since $(e^{2a(8/9)}-1)^{-1/2}<6.4$ and $\sqrt{96}\exp(a(10/9)96)<44$. In (ASQ13.1) keep the mandatory middle $P_{97}$ by subtracting the genuine $DQ_{97}C^{-1}$, getting
$$
             \|D P_{97}C^{-1}\bar G P_E\|_0<10.8\,d_E .
$$
In fact $1.12(6.4)(1+.08\cdot.088)+.08(44)<10.8$. For an arbitrary output $z$ the same low-to-high split used in ASQ12 bounds $\|P_{97}Q_aT_i z\|_0<1.11\|z\|_0$. The $\mathcal T_\alpha I$ term is smoother before $C^{-1}$, so its complete contribution after the true input projection and both multipliers uses ASQ12.2,12.4. Altogether the entire exceptional-to-high opposite-sign part is
$$
 \|P_{97} Q_a T_i D P_{97} C^{-1} A\bar G P_E\|
       <12d_E+.00132g_1 .                                  \tag{ASQ13.2}
$$
This moves the true inverse only via the two exact block identities; it does not assert that opposite signs commute with composition or with the original low projection.

For its physical companion, the original complete $C^{-1}$ has the $H^{-4/3}$ bound $5/2$ (SDI). Apply it to $\bar G P_E$ directly in this window and use the $L^2$ inverse followed by $P_{97}$ to estimate its primitive input error. The two independent full estimates are
$$
 \|S P_{97}C^{-1} A\bar G P_E\|_{2\to H^{-4/3}}
 \le \min\{1.1\cdot388^{-1/3}(1.11)(1+1.43/388)g_1,\ 
      1.1[(5/2)t+388^{-4/3}(1.11)(1.43)g_1]\}.             \tag{ASQ13.3}
$$
The same estimate passes to an infinite set by density, provided its displayed right-hand side is finite. Thus the original signed vectors pass to each actual physical receiver with their frequency weights and without a cardinality factor.
