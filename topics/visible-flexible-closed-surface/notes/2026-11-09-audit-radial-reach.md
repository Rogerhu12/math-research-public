# Independent audit: radial normal-chord bounds and buffer inequality

Reviewer: Astra independent_audit, 2026-11-09. I did not write either candidate proof.

Reviewed files and SHA256:

- `notes/2026-11-09-closing-radial-reach.md`: `803d6f7e6d172cf637298cdf433e412fcc057ce243a75726136ea091fc8273b3`.
- `notes/2026-11-09-sharp-monotone-reach-candidate.md`: `2e12c6d2401dee2970a8d6aa26dd0393eb062f2e1a45a75208a064dc0447ed6c`.

## Verdict

**PASS for both pure geometric normal-chord proofs and the closing note's Section4 buffer sufficient condition.** The sharper proof yields the better constant1/K under tangent-cone width strictly below pi/2 and can be used for the same-sign radial profiles here. The old cos²(A/2)/K statement remains valid for the larger range A<pi. All parameter applications remain conditional: neither proof supplies a closed isometric family, a full-surface reach certificate, or the missing uniform bounds for the unchanged infinite source.

## Sharp planar bound

Choose the direction of traversal from p to q. Reversing an arc reverses every tangent together, preserving the width of the containing tangent arc. Rotating its starting tangent to the horizontal then gives a strictly positive horizontal component of every tangent on the subarc, because any two tangents differ by an angle smaller than pi/2. Hence the whole subarc, not merely a neighborhood of p, has a graph representation v(u) with increasing u.

The identity d(sin(phi))/du=kappa is exact: both numerator and denominator from the arclength derivatives contain cos(phi), which is positive. Starting with phi=0 yields |sin(phi)|<=Ku. For u<1/K, division by sqrt(1-K²u²) is legitimate and integration gives the lower circular-arc bound on |v|. That bound places the graph outside each open radius1/K disk tangent to the curve at p. For u>=1/K, the stated completion of the square proves the same exclusion without further information about the graph. The endpoint u=1/K is covered directly by that square. The absolute value in the normal component makes the proof independent of the choice of unit normal.

Thus for every ordered pair p,q the inequality |q-p|²>=2|(q-p) dot n_p|/K holds. It is sharp: a sufficiently short circular arc of radius1/K attains equality and has tangent-cone width below pi/2. No assumption that curvature has constant sign is used or needed.

For comparison, the old cone proof is also correct: projecting onto the cone bisector gives a chord length at least ell*cos(A/2), and the curvature bound controls the normal chord component by K*ell²/2. If the first point comes later in the parameter order, reverse the parameter on the subarc or integrate with absolute orientation; the same proof applies at that first point. The old sentence considering u<v should be read with this reversal when applying its conclusion to every ordered pair.

## Radial reduction

I expanded both Cartesian identities independently. With p=(r,0,h(r)) and q=(s cos(theta),s sin(theta),h(s)), the squared chord separates into the meridian chord and 2rs(1-cos(theta)). The normal component separates into

$$[h(s)-h(r)-w(r)(s-r)+w(r)s(1-\cos\theta)]/\sqrt{1+w(r)^2}.$$

The meridian term is controlled by the sharp planar inequality. The angular squared-chord term is exactly twice its absolute normal contribution times r*sqrt(1+w²)/|w|. Taking the smaller of the two constants and then applying the triangle inequality to the two normal contributions proves the sharp radial inequality. The weaker cone constant can be substituted by the same argument.

For w of one sign and bounded, the meridian tangent angles lie in an interval of width arctan(||w||_infinity)<pi/2; if w is nonpositive, reflect the height coordinate. Flat intervals add only the endpoint angle zero. At a point where w=0, the angular normal contribution is zero, so no division by zero is needed. A flat neighborhood of r=0 permits direct treatment at the center by the meridian bound. These observations justify the candidate's conventions at flat points and the central disk.

If every nonflat point has r>=r_c and |w|<=c, then r*sqrt(1+w²)/|w|>=r_c*sqrt(1+c²)/c, since sqrt(1+t²)/t decreases for t>0. Consequently K<=6, c<=.506, r_c=.25 would indeed give the ratio at least1/6 for all pairs within the indicated radial tail/disk block. It would not by itself give the reach of the complete surface: prefix pairs, cross-region pairs, and the actual nonaxisymmetric corrections still have to be covered. Both candidates state this restriction correctly.

## Cutoff-buffer sufficient condition

Let S be the cutoff value in[0,1], b=v/rx, and E=1+w². Starting from the displayed radial derivative, the exact inequality v<=K*r_x is equivalent to

$$S(b-Kj_0)\le K\alpha(1-S)/E.$$

Using b<=B, E<=Emax, alpha>0 makes the left side no larger and the right side no smaller than required by

$$K(c_r-1)S^2+(K-B-K\alpha/Emax)S+K\alpha/Emax\ge0.$$

The direction of every estimate is correct. To certify this condition, check the quadratic at both endpoints and at its vertex if that vertex lies in[0,1]. Lower bounds on c_r and alpha, an upper bound on B, and an upper bound on Emax all move the displayed quadratic in the conservative direction on[0,1]. A large raw buffer curvature bound does not itself invalidate the redistributed buffer, because the alpha term is retained here.

The same algebra also applies to the root cut-preserving constructor's final port once it is verified that this entire port is raw and uses the same cutoff. In the audited root implementation it does: the restored transition is segment7, while the final segment8 is exactly raw. This observation does not automatically verify numerical B/Emax/alpha enclosures, and it does not extend the buffer estimate to every modified transition without checking its own cutoff.

## Infinite source qualification

The deep-source Section5 bound has the correct exponents and direction under its stated alpha_n bracket and plateau assumptions: the peak w bound scales as delta_n^(a-1); dividing the logarithmic transition derivative by eta_n supplies the factor that changes this to delta_n^(a-1-etaPower), up to a logarithmic factor. It is essential to apply such a bound to all unchanged cells, not only the finite warped portion.

The independent audit has found an actual example of that distinction: root's original protectCell80, delta0=.006, wCut=.5, rCuff=.25 background has a raw n80 first-transition point with curvature above341, despite all80 warped cells having curvature below6. This is documented separately in `notes/2026-11-09-audit-cut-tail-deep-curvature.json`. It does not challenge either geometric lemma; it means their curvature hypothesis is false for that original full-tail extension.
