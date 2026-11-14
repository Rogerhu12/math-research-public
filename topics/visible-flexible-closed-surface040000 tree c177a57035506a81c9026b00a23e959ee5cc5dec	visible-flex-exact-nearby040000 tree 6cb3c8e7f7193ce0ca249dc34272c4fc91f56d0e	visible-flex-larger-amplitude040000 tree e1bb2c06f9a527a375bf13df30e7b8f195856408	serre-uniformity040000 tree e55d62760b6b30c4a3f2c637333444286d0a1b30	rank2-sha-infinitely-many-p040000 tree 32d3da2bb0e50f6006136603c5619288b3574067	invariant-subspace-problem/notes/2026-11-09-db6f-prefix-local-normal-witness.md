# A short-meridian sufficient condition for an unaligned Hausdorff witness

Status: complete conditional elementary argument, awaiting independent review.
It is not a statement that a current numerical candidate satisfies its hypotheses.

Let a complete reference surface contain an upper patch
$F:[0,s_1]\times S^1\to\mathbb R^3$ and its lower reflection. Assume
$F(0,\theta)=(\gamma(\theta),0)$ and $F_s(0,\theta)=e_3$ in the physical
meridian coordinate, where the planar core has support at most $r$ in a fixed
horizontal unit direction $u$. Suppose some allowed phase of the core contains
$p=(r+\Delta)u$ in the plane $z=0$, with $\Delta>0$.

Assume there are positive constants $b,L$ such that, for all material angles and
$0\le s\le s_*=\Delta/b$,

$$F_{s,3}(s,\theta)\ge b,\qquad
  F_{ss}(s,\theta)\cdot u\le L,\qquad \Delta L\le b^2.$$

Assume $s_*\le s_1$ and every part of the upper reference surface outside this
short patch has height at least $\Delta$; the reflected lower part has height
at most $-\Delta$. These are all-domain assumptions, not sampled claims.
Then $\operatorname{dist}(p,F_0(M))\ge\Delta$, hence
$\delta_{\rm hold}\ge\Delta$ for the phase family.

Indeed, two integrations of the horizontal acceleration bound, and one of the
vertical velocity bound, give

$$F(s,\theta)\cdot u\le r+\tfrac12Ls^2,\qquad F_3(s,\theta)\ge bs.$$

For $s\le\Delta/b$, the horizontal deficit satisfies
$\Delta-Ls^2/2\ge\Delta/2>0$. Orthogonal projection onto the plane spanned by
$u,e_3$ therefore gives

$$|p-F(s,\theta)|^2\ge
 (\Delta-Ls^2/2)^2+b^2s^2
 =\Delta^2+(b^2-\Delta L)s^2+\tfrac14L^2s^4
 \ge\Delta^2.$$

The other surface points are separated by their vertical coordinate. The lower
reflection has the identical estimate. The argument does not require a central
cylinder or a global reach of size $\Delta$.

## Use for the pending flat-acceleration design

The new candidate has a first-order core support gap near .2, but its initial
outward meridian speed is only .17. Before height reaches .2, the background
vertical velocity is close to one and its horizontal acceleration is small.
This suggests that the margin $b^2-\Delta L$ may be much easier to validate than
an all-section support envelope. No such bounds have yet been certified for the
nonlinear candidate. Any use on a finite interpolant must account for its exact
inlet jets and any nonzero projection/inlet defects; it must not silently replace
near-equalities by the exact hypotheses above.
