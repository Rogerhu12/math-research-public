# A rounder exact compact center and a longer original-metric Cauchy prefix (V52)

Change the real central curve to R281’s p=2, r=1/5, at physical scale λ=1.06. Its support function is 1+(16/45)cos(2θ)−(4/225)cos(4θ). Its unscaled axial supports are 301/225 and 141/225. Its physical curvature lies between 1/[1.06(1+.8(8/3−1))] and 1/(1.06·.2), or approximately .4043 and 4.7170. Use its true arclength argument, the original fixed V40 Q,S (V49 modulation factor exactly one), unchanged physical cylinder half-length 1.06·13/128, and the R314 exterior of V47. In the upper annulus integrate the nonlinear Gauss–Codazzi/frame and positions on 0≤t≤.24 from this new actual center. The left-interface material mark for global held distances is now 301/225 before scaling.

The 256 and 512 angle integrations take 768 and 1536 radial RK4 steps, 48 genuine radial quintic spans, and 48 and 96 angular indices per Cartesian coordinate on that prefix. Both complete physical maps use the exact central replacement (Γ₂−Γ₃₂) times 1−S₅(t/.70), plus the numerical Cauchy residual and a quintic matching all endpoint two-jets at .24 and .70. The old V48 changes turn on by the same two-jet cutoff on [.24,.70]. All actual R314 exterior values survive from .8 outwards.

| Original metric observation | 256 true angles | 512 true angles |
|---|---:|---:|
| Prefix prescribed G10a | 3.2936466e−5 | 6.7595239e−7 |
| Prefix prescribed G10b | 3.3513047e−5 | 6.5315729e−7 |
| Prefix independent G11 | 4.9969325e−5 | 8.9122804e−7 |
| Prefix G11 max physical curvature | 6.753286 | 6.753287 |
| Full G11 metric | .981193472 | .981193466 |
| Full G11 max physical curvature | 229.927404 | 229.927305 |

The new 512 prefix exits on its long axis at (1.431985891,0,.401165396), with unit direction (.08914,0,.99602). The short axis exits at (0,.817481789,.326841919), with unit direction (0,.92929,.36935). The full 512 join has G11 held .554264233 and half-width .994645601. Its pronounced near-fold around t=.45 prevents a geometry claim. All full material row counts are 958·(128+192)·14 and 668·256·14. These are finite field comparisons; global Cauchy continuation, continuous metric, reach and strong ratios remain open on this input.

Use `2ecf-compact-p2-original-cauchy-field.mjs make256 STATE192 STATE540 F256`, `make512 STATE192 STATE540 F512` and `observe STATE192 STATE540 FIELD` with the V40 and V48 genuine states. Regenerated field JSON SHA256 with final LF is adb44080468be089076e99bb090e785d75f7ca1ebd656c6129dfd9b01d812a45 and 53fc8d4bc057a4e0568b26e7e4c4b84150dee75af04948bff9c14bee5428b87f respectively.
