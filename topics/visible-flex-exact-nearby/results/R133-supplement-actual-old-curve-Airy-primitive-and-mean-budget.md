# R133 supplement: actual old-curve Airy primitive, mean and commutator budget

2026-11-14. **Proved, with actual public directed-arithmetic bounds.**
Public [run 43605453793](https://github.com/Rogerhu12/math-research-public/actions/runs/43605453793)
completed all eleven gates, with child return zero and mathematical
wall time 0.214333714 seconds.

This instantiates
[the original primitive and exact mean theorem](R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md).
It applies to the actual moving analytic fold for the entire explicit
complex family $|\delta|\le10^{-8}$ at intrinsic $\eta_0$.
The primitive and mean follow the original closed $\rho$ curve.

## 1. Exact actual output

The directory is
`notes/actual_airy_primitive_ci/run-43605453793-1/consumers/`.

| Item | Exact SHA256 |
| --- | --- |
| `actual-airy-primitive.json.gz` | `4ebc5865a8427e67e003e0aa25d8f629353ed87efd67d1705e1cdac7d2fc5b39` |
| published `process.json` | `3d405529c83f9205baddbeb87113cc5e6c8c7735c3337cdc5fca97f2d52c9b4c` |
| mathematical producer | `602de801dddb38ae3cbd6e04a5c9de96ea1e3180b9ae4089bb30bcda3814dafc` |
| wrapper | `4ebf561a26f3d2abdaf5595de4df5f478a78e62af645f395eae6c4393babc9b5` |
| nine-file manifest | `ebe37ead772a4e998be65cc453b88b2e9af097d1abe31bcdaba58bf7a2b7beba` |
| original complete fold native | `9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd` |

The actual event commit was `feab9848e2bb79e0c6f97eeeffd8d02743f2a0a3`;
the immutable scientific checkout was `f5c3bd58ab7a558e401b40140d94432b3fd72390`.
The old fold flow, scalar germs and response calculations were not rerun.

## 2. Actual analytic domains and strict constants

The outer amplitude product is
$|T|\le81/4000000$, $|\Im X|\le1/128$.
The inner product is $|T|\le19/10^6$, $|\Im X|\le1/256$.
For the original mean, use $|\rho|\le4\,10^{-6}$
and the original angular contour $\Im\phi=\epsilon,3/1024$.

| Quantity | Certified strict bound |
| --- | ---: |
| both two-amplitude principal matrix inverses | $<1.000097093597$ |
| $|T|$ on the entire original mean contour | $<0.000018291698201$ |
| complete old-mean decay exponent $c_\Pi$ | $>0.002921264998045>1/512$ |
| complete $J$ on the paid same space | $<0.825332619571$ |
| $J$ with either angular derivative ordering | $<3.301330478284$ |
| complete $[D_0,J]$ | $<253957.400944014<254000$ |
| actual analytic transport displacement | $<6.075000001\,10^{-8}$ |

In particular, for either entire Airy column and either angular sign,
with physical frequency $n=4|j|$ and
$M_F=\max(|F(0)|,|F'(0)|)$, the original mean is bounded by

$$
20M_F(1+n^{2/3}T_c)e^{-n c_\Pi}\|v\|_{\rm in}.
$$

This includes the full original mean measure and the true Airy
profile. It is not a statement that an arbitrary independent mean
equation vanishes.

## 3. Finite expansions remain finite identities

The exact identity is

$$
I_\rho\mathcal U(v)
 =W_N-\Pi_\rho W_N-n^{-N}I_\rho\mathcal U(Yv_{N-1}).
$$

The final term has the genuine original $L^2$ primitive factor $1/4$.
All nested derivatives of the variable inverse matrix are included
in the coefficient recurrence.

The new native records the full coefficients for orders one through
four. For the complete last-amplitude coefficient $(H_*L_N)^N$,
outward bounds are:

| Order $N$ | Complete last-amplitude coefficient |
| ---: | ---: |
| 1 | $<512.073328149$ |
| 2 | $<589992.960153$ |
| 3 | $<1074203230.897$ |
| 4 | $<2685892693131$ |

These coefficients multiply the actual $n^{-N}$ and Airy amplitude
norms in the theorem. They are not claimed to be small at every
$n\ge388$, and the finite expansion is not asserted to converge
as an infinite Neumann series.

The exact inverse error remains $JPf=Pg-JE$, with the complete
original residual $E=APg-Pf$. Its radial derivative uses the paid
$[D_0,J]$ and the actual $D_0E$. The independent even-mean equation
remains a separate source row.

## 4. Remaining actual root obligations

The finite-order analytic transports are defined by genuine
characteristic integrals in $t=\sqrt T$, with the paid positive
angular margin. This certificate supplies the domains and constants
needed to control their true primitive and mean remainders.

It does not evaluate the full original two-row PDE parametrix
residual, correct that residual with the positive graph, identify
the actual finite reflection constant, or prove the complete strong
return remainder. The positive graph and root-to-negative energy
certificates must be used on the same background before those
conclusions can be drawn.
