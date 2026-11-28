# R325. An actual slower Prüfer tail with an exact finite-amplitude rotational mean correction and a C² flat-cuff limit

Use the R314 inverse-phase equations with the following new infinite sequence, distinct from R314 and R316. The physical flat cuff has radius r_c=.371 and height .5724. Put q=3/2, δₙ=.018 q^(−n), μₙ=k₀q^(−3n)δₙ, and use p values (q³δₙ,1/δₙ,δₙ) with the same two quintic log ramps of angular half-width δₙ about θ=arctan4 and π−γ, γ=arctan(1/4). Normalize the outgoing Prüfer amplitude at the largest radius to one. Define r_* from the exact sum of all packet lengths as in R314 and k₀=.00014 r_*⁷. Fix ε=2.8·10⁻⁹ once in the physical displacement. The target on this radial tail is exactly (1+w²)dr²+r²du² for this new infinite background.

Write the scaled R314 mode as (U cos2u,−(U/2) sin2u,F cos2u) in the cylindrical frame. Define e₀=5U′²/8+F′²/2, g₀=9U²/8+2F², x=g₀/r² and y=g₀′/(2r). The new physical axis radius and vertical derivative are

h=√(r²−g₀),    W²=w²−e₀+(2y−y²−x)/(1−x),   W>0.

Replace the radius and height of the base by h and .5724+∫[r_c,r] W(t)dt, and keep the actual nonzero mode. This changes true Cartesian positions at finite amplitude. Angular averaging gives ⟨G⟩=h²+g₀=r², ⟨E⟩=h′²+W²+e₀=1+w² and ⟨F_cross⟩=0 exactly. The m=2 and m=4 components of the full angular Gram generally survive. No accurate full metric, full nonlinear solution, or compact strong core is asserted here.

## Native gain, radial width and signed amplitude

On a constant phase section, the amplitude ratio between two endpoints a,b is s(a)/s(b) for s(φ)=√(cos²φ+p²sin²φ). Write R(φ) for positive amplitude, Q=R cosφ and Π=R sinφ with the packet's common sign. Both ramps satisfy |(log R)′|≤max(|tanφ|,|cotφ|). For a lower bound sharpen the sign. The first ramp is in the first quadrant and its negative derivative has magnitude ≤cotφ<.28. The second is in the second quadrant and its negative derivative has magnitude ≤|tanφ|<.28. These inequalities follow by bounding (1−p²)sinφ cosφ/(cos²φ+p²sin²φ) separately on each side of p=1.

For all n the first constant gain is at least [(1+4δ₀)²/17+(q³δ₀)²]^(−1/2). The middle gain is at least (4/√17)/√[(1/√17+δ₀)²+δ₀²]. The last gain is at least 4/√17. Multiplication with exp(−4·.28δ₀) gives gₙ>13>q⁶=11.390625. Thus |q_out,n|≤13^(−n).

For the backward bound from the exit through the last ramp, R is at most exp(2·.28δ₀)/(4/√17) times |q_out,n|, which is below 1.042. On the high-p constant piece R is maximized at its right endpoint. Also R|sinφ|≤R_end √[(1/√17+δ₀)²+δ₀²]<.274|q_out,n| there. Its value at the left end therefore has R<.283|q_out,n|, and the lower ramp gain gives R<.287|q_out,n| across the first ramp. On the first low-p part R increases with φ. On the last ramp |sinφ|≤1/√17+δ₀, and the last low-p part has |sinφ|≤1/√17. In particular |Q|≤1.06|q_out,n| and |Π|≤.30|q_out,n| everywhere.

For the phase-clock length the first low-p part contributes ≤4q³δₙ by its arctangent primitive, the central high-p part ≤4.25δₙ by integrating δₙ csc²φ, and the last low-p part ≤.25δₙ. On both ramps the phase density 1/(p sin²φ+cos²φ/p) is at most 1/(2|sinφ cosφ|)<2.4. Hence each full length is ≤27.6δₙ, the sum ≤27.6·.054, and r_*≤.371 exp(27.6·.054/√12)<.572.

## Positive real nonlinear branch at every phase of every actual layer

The native formulas are F=εr⁴Q, F′=εr³(4Q−√12 pΠ), U=−εμₙΠ/[(√3/2)r³], U′=−w F′ and w=μₙ/(r⁷p). Since p≤1/δₙ, the full infinite family satisfies the following estimates, with w_out=.00014 and δ₀=.018:

1. |F′|/w ≤ [ε(.572)³/(w_out δ₀³)] [4δ₀·1.06+√12·.30] (q⁶/13)^n < .7161 (q⁶/13)^n.
2. |F|/(rw) ≤ ε(.572)³·1.06/(w_out δ₀²) (q⁵/13)^n < .01225 (q⁵/13)^n.
3. |U|/(rw) ≤ ε(.572)³·.30/[(√3/2)δ₀] (q/13)^n < 1.01·10⁻⁸ (q/13)^n.
4. w≤w_out(.572/.371)⁷<.0029, and |U′|/w=|F′|<.00208.

It follows that x/w²<.000301, |y|/w²<.01756, and e₀/w²<.25642. Substitution into the stable radicand expression gives W²/w²>.70, in particular a uniform strictly positive margin. For example the deducted contribution from |2y−y²−x|/[(1−x)w²] is bounded by [2·.01756+.0029²·.01756²+.000301]/[1−.0029²·.000301]. The angular radius also stays positive. Thus the exact correction is defined throughout the accumulating open tail.

## Two derivatives at the cuff

Here and below constants in the estimates are independent of n. The native w tends uniformly to zero since μₙ/p≤k₀q^(−3n). The logarithmic ramp derivative is O((n+1)/δₙ). In w′ the term μₙ(1+δₙ^(−2)) times this logarithmic derivative is O((n+1)q^(−n)); hence w′→0 as well. The identities F″=−(w′/w)(F′−4F/r) and U″=−4w′F/r give |F″|≤C(n+1)(q³/13)^n and U″→0. The F″ estimate uses p/(d(native length)/dφ)=p²sin²φ+cos²φ≤1+δₙ^(−2). The adjacent flat endpoints have matching jets by μ/p matching across layers and vanishing ramp derivatives. The new background and mode therefore extend C² over the flat cuff.

Let A=h−r. The preceding ratios tend to zero, so W/w→1. Differentiate h²=r²−g₀ to get A,A′→0 and A″/w→0. Indeed g₀″/w is a sum of terms proportional to U′²/w, UU″/w, F′²/w and FF″/w; all tend to zero by the estimates above, as do g₀′/w and g₀/w. Similarly e₀′/w→0. Differentiating W²=w²−e₀−2A′−A′² yields W′−w′=(w/W−1)w′−[e₀′+2(1+A′)A″]/(2W)→0. Thus the new height and radius have exactly the flat limiting two-jets, as does the full finite-amplitude corrected immersion. Regularity follows throughout: the projected polar ring remains a small C¹ perturbation of the ordinary annulus since the displayed bounds control |U|/r, |U′|, |h/r−1| and |h′−1|. Equivalently the oriented horizontal Jacobian is positive by these bounds.

The source `2ecf-slow-prufer-exact-mean.mjs` implements the exact mean identities using the new slow-spacing source `2ecf-slow-prufer-packet-tail.mjs`. A finite physical 45-layer evaluation gives r_out≈.50015104, minimum sampled W²/w²≈.93811, and maximum sampled background |w′|≈6.70. The full infinite estimates use the exact r_* defined above. Finite truncations have their own outer radius and background target, and are not treated as same-g convergence evidence. The proof concerns the new shell through its outermost packet boundary. A subsequent compact core, macro buffer and full angular feedback require new same-input work.
