# R323. The finite-amplitude R314 second mode cannot be repaired on all deep layers using any axisymmetric mean correction

Take R314's exact infinite shell background (r cos u,r sin u,Z(r)), w=Z′>0 on every open packet. Fix any nonzero coefficient ε multiplying its genuine infinitesimal second mode. In the cylindrical basis, write its actual displacement as

D=(U cos(2u),−U sin(2u)/2,F cos(2u)),

where U,F now include ε. Keep this displacement and the original radial rotation metric (1+w²)dr²+r²du² fixed. Allow an arbitrary continuously differentiable axisymmetric correction to the actual Cartesian positions. This correction may change the radial radius, the phase of the axisymmetric ring, and its height.

## Exact finite-amplitude necessary test

Write the new axisymmetric base as (A(r)e_r+B(r)e_u)+C(r)e_z and h=√(A²+B²). An angular average of the actual metric, with no expansion in ε, gives

⟨G⟩=h²+g₀,   ⟨E⟩=A′²+B′²+C′²+e₀,

where g₀=9U²/8+2F² and e₀=5U′²/8+F′²/2. Cross terms with the base average to zero because the displacement has azimuthal order two in the moving cylindrical frame. Hence h²=r²−g₀; if this number is nonpositive the angular equation already fails at positive radius (the zero case can be tested separately). Where h>0, A′²+B′²≥h′² and necessarily

C′² ≤ w²−e₀ + (2y−y²−x)/(1−x),    x=g₀/r², y=g₀′/(2r).

With zero axis phase this right side is exactly the square of the required height derivative. A nonconstant axis phase only adds radial cost.

In each packet take the actual phase φ=π/2, interior to the high-p constant piece. R314 gives F=0, U=rwF′/3 and U′=−wF′ (here √12·√3/2=3). Thus x=w²F′²/8, y=−3w²F′²/8. If x=1 then (h²)′=2r−g₀′>0 although any differentiable squared norm vanishes to first order at a zero. If x>1 the angular equation is impossible. For x<1 the required squared height derivative is at most w²−F′²/2. Consequently |F′|>√2w rules out exact angular-average matching, even allowing an axis twist.

## Deep amplification at every nonzero amplitude

Write d=max(n−2,0), δ_n=.011·2^(−d), μ_n=k₀·8^(−d)δ_n and k₀=w_out r_out⁷>0, as in R314. On the tested high section p=1/δ_n. With Π the signed native amplitude at φ=π/2 and r≥r_c=.371,

|F′|/w=|ε|√12 r¹⁰ |Π| p²/μ_n.

A direct bound on the exact one-packet gain g_n, uniform in n, is g_n<21. On a constant section the amplitude gain is the quotient of √(cos²φ+p²sin²φ) at its endpoints. The first low-p section contributes at most √17. The middle high-p section contributes at most 1/sin(arctan(1/4))=√17. The last low-p section contributes at most one. On the two ramps |d log(amplitude)/dφ|≤max(|tanφ|,|cotφ|)<4.25 throughout their total angular length 4δ_n≤.044 (use the tangent addition formula at arctan4 and arctan(1/4)). Hence g_n≤17 exp(4.25·.044)<21. From the start of a packet to φ=π/2 the first low-p gain is at least one, the first ramp contributes at least exp(−2·4.25·.011), and the partial middle gain is at least sin(arctan4)=4/√17. Their product exceeds .85. Since |q_in,n|=1/(g₀⋯g_n) with unit outgoing normalization, |Π|≥.85/21^(n+1).

It follows that |F′|/w ≥ |ε|√12 r_c¹⁰·.85·64^d / [k₀(.011)³·21^(n+1)], diverging as n→∞. Every fixed nonzero ε therefore violates the exact mean test at all sufficiently deep sampled phases in the true infinite input. This uses the exact defining gains and phases. It requires no equality between finite 37-layer and infinite r_out.

For orientation, the accompanying `2ecf-prufer-axis-mean-obstruction.mjs` regenerates R314's 37-layer physical evaluator and checks all phase-midpoint ratios exceed √2 at ε=4e−6. The finite ratios at n=0,2,36 are about 34911.0, 74.999 and 2.80249e21 respectively. The full proof is the preceding infinite estimate.

This obstruction concerns the fixed original second-mode amplitudes plus axisymmetric positional corrections for the fixed rotation background. It supplies no lower bound against general true non-axisymmetric corrections, changes in the packets or a different target. It explains why the previously bounded tiny deep defect does not automatically yield a nonlinear exact tail.
