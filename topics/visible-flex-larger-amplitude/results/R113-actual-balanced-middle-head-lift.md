# R113: Actual balanced head mass through both middle columns

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Proved and exactly evaluated.** For the original R74 complex twenty-axis parameter polydisc, the homogeneous outer propagation of the true head's modes $94,96$ has constant-strip local-$V$ norm strictly less than $283/1000$. The previous valid bound for this same two-mode lift was approximately $173.8218$. Both genuine initial columns, the complete R78 head mass, all eighteen outer source segments and all 10793 original leaves remain present.

This is a bound on one linear lift term in the outer equation. It is not a complete middle-frequency inverse, nonlinear self-map, all-46 cut solution, R100 parameter extension, or closed surface.

## 1. The actual input norm

The high bands in R61 §4–5 and R78 §3 originate in the strong norm R33 (33.4), whose two component suprema are separate. At the true cut $b$, R61 (61.22)–(61.23) identifies the relative physical input as $(B_bP,\overline K)$. In particular, the R78 near-band mass $H_N$ pays

$$
\sum_{94\le |m|\le184}(1+|m|)e^{\tau_b|m|}
\bigl(B_b|P_m(b)|+|\overline K_m(b)|\bigr)\le H_N.
\tag{1}
$$

The signed-frequency sum includes both positive and negative modes. It is one shared mass, not a separate complete budget assigned to each mode or each component. The paid constants satisfy

$$
B_b\ge B_->592,\qquad
\tau_b\ge\tau_->18/125=:\tau_*,
\qquad \delta:=\tau_- -\tau_*>0.
\tag{2}
$$

The exact saved lower endpoints are consumed directly. Their decimal displays are $B_-=592.4007651609996\ldots$ and $\delta=0.0004358307482676697\ldots$. No new shallow high-frequency Dirichlet condition or high DN slope is imposed.

## 2. The two true column operator

Let $T_m(t,b)$ be the true physical homogeneous transfer of R104 on the same cell11/cell10 background. The recovered R104 producer propagated both columns from physical unit inputs. Internally the initial $Y=F(P,K)^T$ columns are $F(b)e_1,F(b)e_2$, so the saved readouts already include the initial $F(b)$ factor and divide by the actual target $F(t)V_I$.

Write

$$
L_{m,P}=\sum_{\nu=1}^2\sup_t
\frac{|T_{m,\nu P}(t,b)|}{V_I(t)},\qquad
L_{m,K}=\sum_{\nu=1}^2\sup_t
\frac{|T_{m,\nu K}(t,b)|}{V_I(t)}.
\tag{3}
$$

The completed checkpoint supplies outward upper endpoints for each of the four suprema, with the actual whole-leaf target enclosure. Taking their exact rational sums is valid even if summing separately rounded components is one last bit larger than a separately rounded old scalar row.

For the homogeneous lift $Z_m(t)=T_m(t,b)(P_m(b),K_m(b))^T$, the triangle inequality in each separate radial component gives

$$
\begin{aligned}
\|Z\|_{X_V,\{94,96\}}
&\le \sum_{m=\pm94,\pm96}(1+|m|)e^{\tau_*|m|}
\bigl(L_{|m|,P}|P_m(b)|+L_{|m|,K}|K_m(b)|\bigr)\\
&\le H_N\max_{m\in\{94,96\}}
e^{-m\delta}\max\{L_{m,P}/B_-,L_{m,K}\}.
\end{aligned}
\tag{4}
$$

The second line uses (1), restriction to the two actual modes, and the norm of a two-column map from the weighted input $\ell^1$ norm. The output $(1+m)$ weight cancels the same input factor. There is no additional factor two, no common location assumed for the two output suprema, and no division of the $K$ input by $B_b$.

To evaluate the strip factor without any transcendental numerical call, for $z\ge0$ use

$$
e^{-z}\le \left(\sum_{k=0}^{6}\frac{z^k}{k!}\right)^{-1}.
\tag{5}
$$

Every term in the exponential's omitted Taylor series is nonnegative. Thus (5) is an exact rational upper bound when $z=m\delta$ is the saved dyadic/rational quantity.

## 3. Actual exact consumption

The recovered completed R104 packet uses its unchanged producer SHA `3bbbecae0b3df6927b157d56d0d11add096a6fe979e0d222339383a90d31f2b2`, precision 256, Taylor order 24, root bits 160 and remainder gate $2^{-100}$. It covers 18 source segments, 10793 original leaves, 10872 Taylor subpanels and 8 root brackets. The final checkpoint's entire causal tensor and coverage counts were compared exactly with the completed primary.

The relevant column sums, shown only for readability, are:

| Mode | $L_{m,P}$ | $L_{m,K}$ | Strip-paid balanced column norm |
| --- | ---: | ---: | ---: |
| 94 | $6.414901361564491\cdot10^{52}$ | $1.0817869960365772\cdot10^{48}$ | $1.0393986693285772\cdot10^{50}$ |
| 96 | $8.543498316596777\cdot10^{52}$ | $1.4713926616090655\cdot10^{48}$ | $1.3830865374559294\cdot10^{50}$ |

The same R78 near-band mass is approximately $2.0345509353021388\cdot10^{-51}$. Applying (4) first without strip improvement and then with (5) gives valid bounds with displays

$$
0.29341931194265386\ldots,\qquad
0.2813960008384758\ldots <\frac{283}{1000}.
\tag{6}
$$

The exact integer inequalities, all input endpoints and source hashes are in `2026-11-13-exact-resume-balanced-head-r1.json`. The final upper bound improves the earlier valid scalar lift by a factor greater than $617$. The numerical displays in this note do not define any input or gate.

Files required for the computation are the recovered primary, the final recovered checkpoint, the unchanged R78 head ledger and its unchanged R61 trace. The standard-library Fraction consumer is `2026-11-13-exact-resume-balanced-head-consumer.py`; it performed no ODE solve, radial quadrature, source integral or Arb computation. Its successful run took approximately $0.117$ seconds and peaked at 18052 KiB.

## 4. Scope of the improvement

Formula (4) applies to any set of modes for which the true columns and the matching balanced head mass have been paid. The actual numerical packet here contains exactly modes $94,96$; no values for modes $98$ through $5758$ are inferred from them. The unchanged complete mean and nonlinear source terms still enter the R98 coupled equation. In particular, replacing the former lift term by (6) alone does not prove the R98 radius $r_M=1/8$ is invariant, nor does a bound above that radius prove the true solution leaves it.

The next linear data packet adds true target-leaf local-$V$ readouts to all signed source origins, allowing the same two-mode source budget to be assessed without repeatedly transporting positive endpoint boxes. That independent calculation must finish and be consumed before any additional nonlinear claim.
