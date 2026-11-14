# R722 — The actual unit at $p=137147$ and its complete deep Abel consequence

Date: 2026-11-14. Status: **proved, with a complete public exact certificate**.
At the genuine exceptional prime $p=137147$, the original full coefficient
$M_2$ has valuation zero. This settles the unit hypothesis left open in
R711/R721 at this prime. It does not identify an Abel function with the
actual quadratic height and does not exclude a Serre-uniformity candidate
by itself.

## 1. The original value, with no change of character or period

Throughout this result set $p=137147$, $n=p+1=137148$, and normalize
$v_p(p)=1$. Retain R588/R595's original curve, differential, tame marking,
primitive character and selected $p$-adic embedding:

$$
E_0:y^2=x^3-1,\qquad dz=\frac{dx}{2y},\qquad
\alpha^3=4,\quad\beta^2=3,\quad
C_0=\frac{72\beta}{\alpha},\quad C_0^2=\frac{15552}{\alpha^2}.
\tag{722.1}
$$

The chosen reduction of $\alpha$ is the unique cube root of $4$ in
$\mathbf F_p$. For the same eighteen labeled mixed six-torsion points,

$$
Q_{\delta ij}=(\alpha\zeta^i,\delta\beta)+(\zeta^j,0),\qquad
\chi_6(Q_{\delta ij})=\delta\zeta^{j-i}.
$$

Write $T_r=e^*_{r,r+1}/(r!\mathcal A^r)$ and
$H_r(P)=\sum_Q\chi_6(Q)^{-1}T_r(P+Q)$. The sums are exactly

$$
S_2=-\sum_{b\in(\mathcal O_K/p)^\times}\theta(b)H_2(\Omega b/p),
\qquad
S_3=-\sum_b\theta(b)^{-1}H_3(\Omega b/p),
\qquad \theta=\theta_{-1}.
\tag{722.2}
$$

Put $P=S_2S_3/C_0^2$. The certified result is

$$
\boxed{
v_p(P)=0,\qquad P\equiv105522\pmod p,\qquad
v_p(M_2)=0,\qquad
\frac{M_2^2}{\zeta^2}\equiv53970\pmod p.
}
\tag{722.3}
$$

The last congruence determines the squared leading value; it does not
choose an unsupported sign for $M_2$. In particular $M_2\ne0$ in
characteristic zero. The actual scalar Abel primitive therefore has a
simple zero at its center in the coarse parameter $s=a-1$.

This is a computation of the full original $S_2S_3$, not a $p$-adic
lift of the single fixed-CM residue $C_{p-3}$. It includes all original
Fourier blocks and the inverse-sigma contributions through the exact
Kronecker/complex comparison of R717.

## 2. Exact complex comparison and certified trace recovery

R717 uses the original real period and area

$$
\Omega=\frac{\Gamma(1/6)\Gamma(1/2)}{3\Gamma(2/3)},\qquad
\mathcal A=\frac{\sqrt3\,\Omega^2}{2\pi},
$$

and the two original Hecke characters

$$
\xi_5((a))=a^5\chi_6(a)\theta(a)^{-1},\qquad
\xi_7((a))=a^7\chi_6(a)\theta(a).
$$

The exact R588 period identities, including both factorials, are

$$
L(\xi_5,3)=\frac{\Omega\,2!\mathcal A^2}{36p}S_2,\qquad
L(\xi_7,4)=\frac{\Omega\,3!\mathcal A^3}{36p}S_3.
$$

Consequently

$$
P=\frac{\alpha^2p^2}{144\Omega^2\mathcal A^5}
       L(\xi_5,3)L(\xi_7,4).
\tag{722.4}
$$

All tame labels, the CRT minus signs, the completed-zeta convention,
and the direction of the selected Teichmueller embedding are those proved
in R717. In particular these are the weight-five and weight-seven
characters with conductor divisible by $p$, not the fixed-conductor
characters used to define $C_p$ and $C_{p-3}$.

R717 proves, before any numerical rounding,

$$
P\in\mathbf Q(\zeta_n)^+,\qquad
DP\in\mathbf Z[\zeta_n],\qquad D=2^{37}3^{26}p^5.
\tag{722.5}
$$

Its complete approximate functional equations, with certified complex
balls and proved full lattice tails, recover the integers

$$
t_j=\operatorname{Tr}_{\mathbf Q(\zeta_n)/\mathbf Q}
          (DP\zeta_n^{-j}),\qquad
T(X)=\sum_{j=0}^{n-1}t_jX^j,\qquad
T(\zeta_n)=nDP.
\tag{722.6}
$$

At this prime the public calculation used 384-bit working precision,
tail allowance $2^{-256}$, and norm cutoff $360p=49372920$.
All $8113$ assigned lattice rows and $14925440$ retained terms were
covered. The four completed bins from the earlier public run were reused
without enumerating any row again.

Every one of the $137148$ trace balls passed the unchanged original
conditions: a unique integer, an imaginary interval containing zero,
and real radius strictly below $1/4$. The largest real radius was
exactly

$$
597851749\cdot2^{-82}<2^{-52}<1/4.
\tag{722.7}
$$

The analytic tail error is already included in those balls. Thus the
integers in (722.6) are certified by integrality and unique containment;
they were not selected from floating-point midpoints.

The three DFTs used independently enclosed phases

$$
\exp\!\left(\pi i\,\frac{j^2\bmod2n}{n}\right)
 =\exp(\pi i j^2/n).
$$

This is the exact same Bluestein phase as in R717. It avoids the severe
rectangular-ball wrapping diagnosed in the original recursive phase
implementation. The source-prefix and fixed-bin compatibility checks
prove that the four original bin producers and all numerical parameters
are unchanged. No failed old embedding or trace ball was reused.
The diagnostic and the repair are recorded separately in
[the independent-phase note](../notes/R717-independent-chirp-recovery.md).

## 3. The selected $p$-adic value and original norm scalar

The norm-one generator is the original

$$
\gamma=131992+75276\zeta\in\mathbf F_{p^2},\qquad
\operatorname{ord}(\gamma)=n,\qquad\gamma^{n/3}=\zeta.
$$

The exact Teichmueller lift modulo $p^6$, in the basis $1,\zeta$ with
$\zeta^2+\zeta+1=0$, is recorded as

$$
\widehat\gamma=
291966755832990292172716689527
+5169731443431895126669136480072\,\zeta
\pmod{6654537439844969533983720123529}.
\tag{722.8}
$$

The modulus displayed is $p^6$. Exact polynomial evaluation gives

$$
T(\widehat\gamma)
\equiv5777613736444106705138118150518+0\zeta\pmod{p^6},
\qquad
v_p\bigl(T(\widehat\gamma)\bigr)=5.
\tag{722.9}
$$

The zero second coordinate is the required real descent at this inert
prime. Since $v_p(nD)=5$, (722.6) and (722.9) prove $v_p(P)=0$.
Dividing by the known unit denominator
$n2^{37}3^{26}$ after removing $p^5$ gives the residue $105522$
in (722.3). Six digits suffice because the numerator has already been
shown nonzero after division by $p^5$.

The original toric norm and anti-linear relation from R588 are

$$
M_2\overline{M_2}
 =\frac{8N_\theta}{(p+1)^2}S_2S_3,\qquad
\overline{M_2}=-\zeta M_2,\qquad N_\theta\equiv-1\pmod p.
$$

These imply, with the original finite norm retained,

$$
\frac{M_2^2}{\zeta^2}
 =-\frac{8N_\theta}{(p+1)^2}C_0^2P.
\tag{722.10}
$$

All factors outside $P$ are units. Hence $v_p(M_2)=v_p(P)/2=0$;
reducing (722.10) gives

$$
\frac{M_2^2}{\zeta^2}\equiv8C_0^2P\equiv53970\pmod p.
$$

This use of complex conjugation is the exact algebraic relation above.
It does not assume that complex conjugation fixes the chosen
$p$-adic place. Also, the returned
$p^2S_2S_3\equiv0\pmod{p^2}$ is consistent with $S_2S_3$ being a
unit; it is not evidence that the unscaled product vanishes.

## 4. Complete deep-disc original Abel isometry

Use the same actual positive cubic quotient, Hodge basis, flat variable
$z_{\rm f}$, and coarse parameter $s=a-1$ as R705/R710/R711.
The primitive is

$$
\mathcal I(z_{\rm f})
 =\sum_{j\ge1}\frac{M_{3j-1}}{(3j)!}z_{\rm f}^{3j}.
$$

Set

$$
V=z_{\rm f}^3/p^3,\quad
P_p(V)=p^{-2}\mathcal I(z_{\rm f}),\quad
b_*=\frac{p^{p-4}M_{p-3}}{(p-2)!},\quad v_p(b_*)=0.
$$

R710/R711 prove the complete, not merely truncated, statement

$$
\widetilde P_p(V)=P_p(V)/b_*=\sum_{j\ge1}a_jV^j
 \in\mathbf Z_p\langle V\rangle.
\tag{722.11}
$$

The endpoint $b_*$ and all factorials remain in this normalization.
The original fixed-CM values already certified independently in R706 are

$$
C_p\equiv80155\ne0,\qquad C_{p-3}\equiv0\pmod p.
\tag{722.12}
$$

Thus the hypotheses of R721 hold with $h=v_p(M_2)=0$.
For completeness, the first two coefficients are

$$
a_1=\frac{pM_2}{6b_*},\qquad
a_2=\frac{p^4M_5}{720b_*}.
\tag{722.13}
$$

The shared zero $C_{p-3}$ makes the leading square for the original
$M_5$ vanish. R705 gives $v_p(M_5)\ge-7/2$, and R711's integer
valuation theorem improves this to $v_p(M_5)\ge-3$. Therefore

$$
v_p(a_1)=1,\qquad v_p(a_2)\ge1,\qquad v_p(a_j)\ge0\ (j\ge3).
\tag{722.14}
$$

For $t=v_p(V)>1/2$, the linear term has valuation $1+t$, the
quadratic term has valuation at least $1+2t$, and all terms of degree
at least three have valuation at least $3t>1+t$. The full tail
converges by (722.11), so the linear term is strictly dominant.

The complete coarse change is

$$
V=\Psi(v),\qquad v=s/p^3,\qquad
\Psi(v)=\frac38v+\sum_{r\ge2}\psi_rv^r,\qquad
\psi_r\in p\mathbf Z_p,\qquad \Psi\in\mathbf Z_p\langle v\rangle.
\tag{722.15}
$$

It is an integral analytic automorphism and preserves valuations on
the unit disc. Its exact linear coefficient, together with
$M_2z_{\rm f}^3/6$, gives the original coarse linear term $M_2s/16$.
Consequently

$$
\boxed{
v_p(\mathcal I(s))=v_p(s),\qquad
v_p\!\left(\frac{\mathcal I(s)}{M_2s/16}-1\right)
 \ge\min\{t,\,2t-1\}>0,
\quad t=v_p(s)-3>1/2.
}
\tag{722.16}
$$

In particular the primitive has no noncentral zero on
$v_p(a-1)>7/2$, over any complete extension.

On the actual closed candidate disc there is the stronger whole-series
identity

$$
\boxed{
\frac{\mathcal I(p^4u)}{p^4b_*}
 =\frac{M_2}{16b_*}u+pH(u),\qquad
H\in u^2\mathbf Z_p\langle u\rangle,\qquad
\frac{M_2}{16b_*}\in\mathbf Z_p^\times.
}
\tag{722.17}
$$

It gives an analytic automorphism of the closed unit disc. Integral
Tate-series differences and the unit linear term yield

$$
v_p\bigl(\mathcal I(s_1)-\mathcal I(s_2)\bigr)
 =v_p(s_1-s_2)\qquad(s_1,s_2\in p^4\mathcal O).
\tag{722.18}
$$

For the actual Abel component of the original quotient, R711 gives one
nonzero, parameter-independent constant $c_\sigma$ such that

$$
J_\sigma(s)=c_\sigma\mathcal I(s).
\tag{722.19}
$$

Its difference valuation is (722.18) plus $v_p(c_\sigma)$.
No unit assertion for this Kodaira-Spencer comparison scalar is needed
or made.

## 5. The two remaining geometric scalar zeros are ramified

R710's separately published extraction from the original $z$-coordinate
certificate gave

$$
C_{p-6}\equiv117309,\qquad C_{p-9}\equiv122674\pmod p,
\qquad v_p(M_8)=-7.
$$

Thus $a_3=p^7M_8/(9!b_*)$ is a unit. Combined with (722.14), the
integral series

$$
Q(V)=\widetilde P_p(V)/V
 =a_1+a_2V+a_3V^2+\sum_{j\ge4}a_jV^{j-1}
$$

has its first unit coefficient in degree two. Formal Weierstrass
preparation over $\mathbf Z_p$ gives

$$
Q(V)=U(V)(V^2+AV+B),\qquad
U\in\mathbf Z_p[[V]]^\times,\quad A,B\in p\mathbf Z_p.
$$

At $V=0$, $a_1=U(0)B$, so $v_p(B)=1$.
The quadratic is therefore Eisenstein. Its discriminant has valuation
one: $v_p(A^2)\ge2$ and $v_p(4B)=1$. It has two distinct roots,
both of valuation $1/2$, in a ramified quadratic extension of
$\mathbf Q_p$.

The unit $U$ converges and does not vanish at any $v_p(V)>0$.
The complete change (722.15) has an inverse on this disc and preserves
valuations and multiplicities. Hence the original scalar primitive has
exactly three zeros in the geometric open disc $v_p(a-1)>3$:
the simple center and two simple noncentral zeros satisfying

$$
\boxed{v_p(a-1)=7/2.}
\tag{722.20}
$$

In particular neither noncentral zero is a $\mathbf Q_p$ point.
The earlier residual lowest degree three in R710 is unchanged, while
the actual characteristic-zero order at the center is now proved to be
one. No statement is made that either noncentral scalar zero is a zero
of the full Abel vector.

## 6. Consequence for the already completed finite window

The R706 window contains exactly $5992$ primes
$41\le p\le200000$ in the actual classes $p\equiv2,5\pmod9$.
For its $5991$ primes other than $137147$, the independently certified
$C_pC_{p-3}\ne0$ gives $v_p(M_2)=-1$; R710 then gives only the center
as a scalar Abel zero in $v_p(a-1)>3$.
At $137147$, Sections 4–5 give the same conclusion for
$\mathbf Q_p$ points, since their positive valuations are integers.

Thus, for every prime in that exact finite window, the original scalar
Abel increment cannot vanish at a noncentral $\mathbf Q_p$ point in
the actual candidate range $v_p(a-1)\ge4$. This corollary combines
already completed certificates and the new target certificate; it does
not rerun or extend the prime window, and it is not an all-prime claim.

## 7. Public evidence and remaining boundary

The successful calculation ran in the public repository's
[Actions 43602664971](https://github.com/Rogerhu12/math-research-public/actions/runs/43602664971),
source commit `f63e0498a9d599342ee5af0f66f3a425edfd9fd2`.
Its bounded receipts are under

`computations/R717-original-CM-norm-p137147-direct-chirps/43602664971-1/`.

| Artifact | SHA-256 |
|---|---|
| `R717-exact-original-CM-norm.json` | `41940fcf1fde383e723c1b5c0265f23b04ed441cb86d8f1e946223ec721b1c2c` |
| `run-receipt.json` | `1e1db4e86616b955ec478ef1309f91bac3d78ab99ec8fa2fbd4b8e225aac6b49` |
| `files-manifest.json` | `b9fb211fbdbab138a17d76cfe0bb219403bc95b891122a4ce4e7e9962161e09f` |
| `R717-complex-embeddings.json.gz` | `46257ffeb21d3b47f67511b922a0235713668c95e5c42367afb9dc59d7600697` |
| `R717-integral-trace-balls.json.gz` | `f2bfd1c46cde0e9c5e772f7c15392a66db146d4602ad8dfe2201d1e11b645fbe` |
| `R717-exact-integer-polynomial.json.gz` | `1bc59fb2e944a02e9cb6fdb9f5344f2858daee20544387f06978e9b3c435de14` |

The full large artifacts, including all four completed bins, are preserved
in `serre-cartier-R717-original-CM-norm-p137147-direct-chirps-43602664971-1`.
The mathematical source SHA-256 is
`c437d880dcea112f4e5b3f7d44cdfd37ad221b7f41a4d14d1359f11f010aa835`.
The source-prefix comparison and the hashes of all four reused bins are
included in the final core receipt.

The preceding $C_p,C_{p-3}$ values come from
[R706](R706-exact-window-through-200000-and-original-sigma-zero.md),
with an independent original-coordinate confirmation. The next pair
and the full infinite tail come from
[R710](R710-unramified-squared-jets-and-complete-coarse-Abel-reduction.md).
The rational coefficient line and original quotient comparison are
[R711](R711-rational-CM-Abel-line-and-integral-jet-valuations.md);
the precise isometry theorem is
[R721](R721-uniform-conditional-deep-Abel-isometry.md).
The original complex and integer-trace proof is
[R717](R717-exact-original-CM-norm-from-certified-complex-traces.md).

None of the unnormalized scalar Abel statements above uses the
Mordell-Weil or weight-two L-value nonvanishing hypothesis in R616.
Using the normalized $t_i$, the common-order assertion of R682, or the
actual height exterior product continues to require its original
$L'(g_{-1,+},1)L(g_{-1,-},1)\ne0$ hypothesis.
At this prime the R616 premise is already established by
[R719](R719-p137147-original-primitive-visible-enumeration-certificate.md);
its closed status is retained here.
The true height still contains the actual $\Lambda$, Coleman-Gross
constants and $\ell_h$. They have not been identified with or removed
by this scalar primitive. Consequently this result does not exclude a
height zero, prove a Serre bound, or complete the topic.
