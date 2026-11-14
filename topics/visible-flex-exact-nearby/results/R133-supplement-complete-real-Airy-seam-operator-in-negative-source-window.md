# R133 supplement: complete real Airy seam operators in the negative source window

2026-11-14, phase_inverse.

**Proved quantitative operator bounds.** This gives an explicit full-frequency
norm for the first corrected state jump in
[the exact first-forcing seam identities](R133-supplement-exact-first-forcing-seams-and-first-correction-jump.md).
It includes every output mode, the old mean projection, the genuine inverse
$J$, and the density input normalization $n^{7/6}$. It uses no finite Fourier
fit or assumption that different high columns are orthogonal.

The result is a recipe to evaluate on the actual saved seams. No numerical
value of their accumulated norm, no whole return remainder, and no cutoff-97
inverse follows until that recipe has been run with the actual inputs.
The positive side has the same raw mixed Sobolev jump bound, but its conversion
to the separate positive weighted affine ports remains an additional step.

## 1. A complete two-derivative symbol bound

Use fourfold Fourier frequencies $4j$ and $\Lambda_j=(1+16j^2)^{1/2}$,
including $j=0$ in every output norm. Let $J_0\ge1$ be an integer input
cutoff, distinct from the inverse operator $J$. Suppose
$$
 Qe_j=b_j(\phi)e^{4ij\phi},\qquad
 \sup_j\|b_j\|_\infty\le B_0,\qquad
 \sup_j\|\partial_\phi^2b_j\|_\infty\le B_2,\quad |j|\ge J_0 .
 \tag{A.1}
$$
A bounded weak second derivative suffices. The coefficients can depend
arbitrarily on $j$; no frequency derivative is assumed. Then
$$
 \boxed{\;
 \|Q P_{\ge J_0}\|_{H^{-4/3}\to H^{-5/3}}
 \le {\cal S}_{J_0}(B_0,B_2)
 :=2^{5/3}\Lambda_{J_0}^{-1/3}
       (B_0+\pi^2B_2/48)
       +8B_2(J_0^{-4/3}+3J_0^{-1/3})^{1/2} .\;}
 \tag{A.2}
$$

Indeed the matrix coefficient at lag $\ell=m-j$ is bounded by
$\min(B_0,B_2/(16\ell^2))$, with the zero lag bounded by $B_0$.
Its unweighted row and column sums are at most
$B_0+\pi^2B_2/48$. On $|m|\ge|j|/2$ the Sobolev ratio is at most
$2^{5/3}\Lambda_{J_0}^{-1/3}$, so the ordinary Schur test proves the
first term. On $|m|<|j|/2$ use
$$
 |\widehat b_j(m-j)|\le4B_2/(4|j|)^2,\quad
 \Lambda_j<2(4|j|),\quad
 \sum_{m\in\mathbb Z}\Lambda_m^{-10/3}<2 .
$$
The squared Hilbert--Schmidt norm of that entire complementary matrix
is at most
$64B_2^2(J_0^{-4/3}+3J_0^{-1/3})$ by the integral comparison
for $\sum_{j\ge J_0}j^{-4/3}$. This proves (A.2). In particular the
low output and the mean have not been deleted from the argument.

## 2. Genuine circle maps and their complete Sobolev cost

Let $\Phi$ be an orientation-preserving fourfold circle lift and suppose
$$
 0<m\le\Phi'\le M,\qquad |\Phi''|\le F_2,\qquad
 |\Phi'''|\le F_3 .
$$
For $\psi=\Phi^{-1}$ put
$$
 P_2=F_2/m^3,\qquad P_3=F_3/m^4+3F_2^2/m^5,
$$
$$
 C_0=m^{-1/2},\quad
 C_2=M^{1/2}
 \{m^{-2}+2P_2^2+m^{-4}+P_3^2+
                       9P_2^2/(2m^2)+m^{-6}\}^{1/2},
 \quad C_\Phi=C_0^{1/6}C_2^{5/6}.
 \tag{A.3}
$$
Then $\|C_\Phi^{\rm op}\|_{H^{-5/3}\to H^{-5/3}}\le C_\Phi$,
where $C_\Phi^{\rm op}f=f\circ\Phi$.
For clarity the scalar bound $C_\Phi$ and this operator are different
objects.

To verify this, the adjoint is $\psi' C_\psi$.
Its first and second derivatives are
$\psi'' C_\psi+\psi'^2C_\psi\partial$ and
$\psi'''C_\psi+3\psi'\psi''C_\psi\partial+\psi'^3C_\psi\partial^2$.
The Frobenius bound on their three-row matrix, in the norm
$\|f\|_{H^2}^2=\|f\|^2+2\|f'\|^2+\|f''\|^2$, is $C_2$.
Duality and Hilbert-scale interpolation with the $L^2$ bound $C_0$
give (A.3).

If the columns instead have phase $\Phi$ and amplitude bounds
$(B_0,B_1,B_2)$ in the old angle, factor the operator as
$C_\Phi^{\rm op}Q$ with symbol $b_j\circ\psi$. Its second derivative
is bounded by
$$
 \widetilde B_2=B_2/m^2+B_1F_2/m^3 .
$$
Consequently its full norm in (A.2) is at most
$$
                C_\Phi\,{\cal S}_{J_0}(B_0,\widetilde B_2).
 \tag{A.4}
$$

## 3. Uniform real Airy decompositions, including the low Airy argument

Let $h(\phi)>0$ on the real circle, with
$$
 h_-\le h\le h_+,\qquad
 |(\log h)'|\le L_1,\qquad |(\log h)''|\le L_2,
 \qquad N=4J_0 .
$$
The following triples bound a function and its first two old-angle
derivatives. Each entry is an absolute bound, not a formal symbol order.
For $T=-h$ the two normalized profiles
$n^{1/6}\operatorname{Ai}(-n^{2/3}h)$ and
$n^{-1/6}\operatorname{Ai}'(-n^{2/3}h)$ have an exact decomposition
into a central phase $X$ and the two real phases
$X\pm\omega$, $\omega=2h^{3/2}/3$:

| Piece | First normalized profile | Second normalized profile |
|---|---|---|
| Central phase | $h_-^{-1/4}(16,\ 94L_1,\ 1208L_1^2+94L_2)$ | $N^{-1/6}(8,\ 51L_1,\ 650L_1^2+51L_2)$ |
| Each real branch | $h_-^{-1/4}(3,\ 16L_1,\ 209L_1^2+16L_2)$ | $h_+^{1/4}(4,\ 22L_1,\ 290L_1^2+22L_2)$ |

The exact phase decomposition is understood after multiplication by
$e^{i\epsilon nX}$, where $n=4|j|$ and $\epsilon=\operatorname{sgn}j$.
For negative input frequencies the labels of the two real branches
are exchanged; the same bounds apply.

Here is an elementary proof with all constants. Write
$u(z)=\operatorname{Ai}(-z)$, $t=2z^{3/2}/3$ and
$w=z^{1/4}u$. Then
$$
 w_{tt}+\{1+5/(36t^2)\}w=0,\qquad
 a_\sigma(t)=\tfrac12(w-\sigma i w_t)e^{-\sigma it}.
 \tag{A.5}
$$
The initial inequality
$|\operatorname{Ai}(0)|+|\operatorname{Ai}'(0)|<1$
can be checked directly from the exact gamma formulas
in [DLMF 9.2.3--4](https://dlmf.nist.gov/9.2#E3), as in the
already used actual root-interface consumer.
On $0\le z\le1$, $|u|+|u_z|<3$ follows from the first-order ODE
and $e<3$. At $t=1/2$, $3/4<z<1$, so $|w|<3$, $|w_t|<4$.
For $t\ge1/2$,
$$
 |(w^2+w_t^2)'|\le {5\over36t^2}(w^2+w_t^2),
 \qquad w^2+w_t^2<25e^{5/18}<36 .
$$
Direct differentiation of (A.5) gives
$$
 |a_\sigma|<3,\quad |t a_\sigma'|\le5/6,\quad
                  |t^2a_\sigma''|\le5/2 .
 \tag{A.6}
$$
Use the real cutoff $\chi=0$ for $t\le1/2$, $\chi=1$ for
$t\ge1$, and $\chi=3v^2-2v^3$, $v=2t-1$, in between.
It has $|\chi'|\le3$, $|\chi''|\le24$ and a bounded weak second
derivative. The exact high-argument formulas, where $t=n\omega$, are
$$
 n^{1/6}\operatorname{Ai}(-n^{2/3}h)
 =h^{-1/4}\sum_\sigma a_\sigma e^{\sigma it},
$$
$$
 n^{-1/6}\operatorname{Ai}'(-n^{2/3}h)
 =\sum_\sigma
   \{-i\sigma h^{1/4}+(4n)^{-1}h^{-5/4}\}
                                  a_\sigma e^{\sigma it}.
 \tag{A.7}
$$
Multiply each branch amplitude by $\chi(t)$; retain the complementary
profiles multiplied by $1-\chi(t)$ as the central phase.

For example
$|\partial_\phi(\chi a_\sigma)|\le(59/4)L_1$ and
$|\partial_\phi^2(\chi a_\sigma)|\le201L_1^2+(59/4)L_2$,
because $(\log t)'=(3/2)(\log h)'$.
Multiplication by $h^{-1/4}$ or by the second prefactor in (A.7)
gives the two branch triples in the table.
On the support of $1-\chi$, $z<(3/2)^{2/3}<4/3$.
There $|u|+|u_z|<8$ follows from the same first-order ODE and
$e^2<8$. Also $n^{1/6}<2h_-^{-1/4}$.
Twice differentiating $z=n^{2/3}h$ and using
$u_{zz}=-zu$ gives before the cutoff the triples
$$
 h_-^{-1/4}(16,\ 22L_1,\ 38L_1^2+22L_2),\qquad
 N^{-1/6}(8,\ 15L_1,\ 29L_1^2+15L_2).
$$
The stated central triples follow from
$|\chi_\phi|\le(9/2)L_1$ and
$|\chi_{\phi\phi}|\le(243/4)L_1^2+(9/2)L_2$.
Thus even small $n h^{3/2}$ is covered; no large-argument expansion
is applied there.

For $T=+h$ there is only the phase $X$, and valid corresponding triples are
$$
 h_-^{-1/4}(3,\ 3L_1,\ 5L_1^2+3L_2),\qquad
 N^{-1/6}(3,\ 3L_1,\ 6L_1^2+3L_2).
 \tag{A.8}
$$
For $z\le1$ use the initial ODE estimate above. For $z\ge1$,
shift the actual contour
[DLMF 9.5.4](https://dlmf.nist.gov/9.5#E4)
to $\sqrt z+i\mathbb R$. Gaussian integration gives
$$
 |\operatorname{Ai}(z)|\le
 {e^{-2z^{3/2}/3}\over2\sqrt\pi\,z^{1/4}},\qquad
 |\operatorname{Ai}'(z)|\le e^{-2z^{3/2}/3}
       \left\{{z^{1/4}\over2\sqrt\pi}+{1\over2\pi\sqrt z}\right\}.
 \tag{A.9}
$$
The derivative identity $\operatorname{Ai}''(z)=z\operatorname{Ai}(z)$
and $\sup_{t>0}t^p e^{-t}=(p/e)^p$ give (A.8).
These are bounds for the real scalar Airy functions only.
They neither change the original angular primitive nor solve the
actual moving equation.

## 4. Apply the exact triples to each true state jump

At one strict original seam let $(q_a,q_b)=([a_{1,r}],[b_{1,r}])$
be the actual amplitudes (J.15)--(J.16), including the complete
one-gain contribution (J.14). Suppose their derivatives have
bounds $A_k,B_k$, $k=0,1,2$. An analytic sup bound on a declared
strip of width $\sigma>0$ suffices, with
$A_k\le k!A_0/\sigma^k$ and $B_k\le k!B_0/\sigma^k$.
A narrower real-angle bound can be substituted when actually proved.

For each row of the table, let $p_k,q_k$ be its two profile triples.
The corresponding complete scalar symbol has bounds
$$
 D_k=\sum_{\ell=0}^k {k\choose\ell}
                      (p_\ell A_{k-\ell}+q_\ell B_{k-\ell}),
       \qquad k=0,1,2 .
 \tag{A.10}
$$
Apply (A.4) to each of the one or three genuine phases and add
the resulting norms. Call the sum $\mathcal A_s$.
This bounds, with both signs and all output modes,
$$
 {\cal V}_s e_j=
 n^{1/6}e^{i\epsilon nX}
 \{q_a\operatorname{Ai}(n^{2/3}T)
          +q_b n^{-1/3}\operatorname{Ai}'(n^{2/3}T)\}:
 H^{-4/3}_{|j|\ge J_0}\longrightarrow H^{-5/3}.
 \tag{A.11}
$$

The density input normalization is $n^{7/6}$, while the first
amplitude correction is multiplied by $n^{-1}$.
Therefore (J.19) is exactly
$$
                 {\cal J}_{s,1}=JP{\cal V}_s,\qquad
                 {\cal J}_{s,2}=0 .
$$
Take the actual reflected parity columns before applying $J$.
The even/odd projections are orthogonal contractions on every stated
Sobolev space; the scalar estimate above holds before those projections.
Thus $J$ is used only on its certified nonmean parity domain, not on
an unproved complementary parity block.
Using the actual original whole-circle inverse bound
$C_{J,s}:H^{-5/3}\to H^{-2/3}$ from the completed root native,
$$
 \boxed{\quad
 \|{\cal J}_s\|_{H^{-4/3}\to H^{-2/3}\times H^{-1}}
                  \le C_{J,s}{\cal A}_s .
 \quad}                                                     \tag{A.12}
$$
The old $P$ has norm one on the scalar Sobolev space. Projection
of this entire output to the genuine high block is also a contraction.
Neither projection has been commuted through $J$.
The complementary finite row is retained as its separate head source.

For the real negative root maps the complete variational equations give
one convenient common choice
$$
 m=e^{-D_1R},\quad M=e^{D_1R},\quad
 F_2=R C_2^{\rm flow},\quad F_3=R C_3^{\rm flow}.
 \tag{A.13}
$$
These cover $X$ and both actual root ray maps, since $X$ is their
average and their radial principal speed is angle independent.
At a fixed seam $h=|\rho|A^{2/3}$, hence
$$
 L_1\le {2\|A_\phi\|\over3A_-},\qquad
 L_2\le{2\over3}
       \left({\|A_{\phi\phi}\|\over A_-}
                          +{\|A_\phi\|^2\over A_-^2}\right).
 \tag{A.14}
$$
On the positive side $X$ remains a real circle lift. Its own
actual derivative bounds are used in (A.3); the two nonreal ray
maps are not inserted as real composition operators.

All seam distances use the certified root interval. All factors
$h_-^{-1/4}$ and the exact $T^{-1}$ in (J.16) are charged at that
seam. The input cutoff can be exactly $J_0=97$ in (A.2)--(A.14);
this is a full operator estimate on that input window, not a
claim that its resulting norm is small.

## 5. Propagation and limits of this conclusion

After the actual negative Cauchy map has been paid in the same
mixed source window, its complete jump column applied to (A.12)
bounds this part of the true correction. Sum the individually
weighted seam contributions in their actual radial order.
There is no source factor $\sqrt{\Delta r}$ on an affine jump.

A positive seam needs the actual conversion of (A.12) to the
weighted positive affine port before that positive Green map
is used. The ordinary volume residual, full old mean, finite
$I/J$ remainders, all later amplitude seams, root stable-port
normalization and strict return endpoint transformations remain
separate terms. In particular this theorem supplies a rigorous
and directly evaluable missing seam-operator fee; it does not
identify that fee with the complete strong return norm.
