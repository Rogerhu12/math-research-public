# R133 supplement: physical reflection, mean rank, and the complete scalar-row ledger

The two stored strict-density mean coordinates have rank one on a single physically reflected state. Their relation makes only the average of the raw odd waist condition automatic. It does not remove the even moving mean, its ordinary source and metric-parameter coupling, the actual outer mean equation, or the physical amplitude row. The amplitude and even-mean functionals are independent local boundary coordinates on the already admitted amplitude-chart domain.

This note supplies an exact rank and domain audit. It performs no scientific arithmetic, changes no successful receipt, and proves no complete incoming or finite Schur inverse. The distinction between a stored coordinate, a physical unknown function, an independently supplied port, and a matching equation is maintained throughout.

## WPM1. Fixed original objects

Use the physical circle of period $\pi/2$, its normalized mean $\Pi$, reflection $Rf(\phi)=f(-\phi)$, $P=1-\Pi$, and $I=\partial_\phi^{-1}P$. Thus
$$
 R\Pi=\Pi R=\Pi,\qquad RI=-IR,\qquad \Pi I=0.
 \tag{WPM.1}
$$
All reflections below are on this original moving circle until an explicit density map is written.

The complete raw variation is $h=(h_1,h_2)$ of the physical moving variables $(u,v)$. On the original reflection class,
$$
 Ru=-u,\quad Rv=v,\qquad Rh_1=-h_1,\quad Rh_2=h_2.
 \tag{WPM.2}
$$
These are N.3's domain conditions, not conclusions obtained from a Fourier cutoff. Write
$$
 z_{\rm raw}(r)=\Pi h_2(r),\qquad f=Ph_2,\qquad m=\Pi v.
 \tag{WPM.3}
$$
The symbol $z_{\rm raw}$ is used here to distinguish the scalar in moving N.3--9 from the two strict-density means, denoted $\zeta_\pm$ below.

At any admitted strict negative circle put
$$
 q=\sqrt{-K}>0,\qquad n_g=\frac{a_{\rm phys}^2}{m^2}>0,\qquad
 T(q)=\frac1{\sqrt{2q}}
       \begin{pmatrix}1&q\\1&-q\end{pmatrix}.
 \tag{WPM.4}
$$
These are exactly strict-cut N.4. The complete primitive and mean state is
$$
 w=n_gTh,\qquad y=Iw,\qquad \zeta=\Pi w,\qquad
 \mathcal Y=L^2_0(\mathbb T;\mathbb C^2)\oplus\mathbb C^2.
 \tag{WPM.5}
$$
The original raw $H^{-1}$ to $\mathcal Y$ map includes both mean columns. It is not a raw $L^2$ identification. The scalar multipliers in (WPM.4) are radial at the circle in question.

The algebraic reflection statements apply to every background on which the original objects and their stated domains are admitted. Displays involving the KAM-selected $\mathcal H,\mathcal S_*,T_i$ or common incoming/outgoing factorization refer only to the original selected member $\delta_*$. The full-family frozen-coordinate theorem does not extend those selected identities to a family of principal conjugacies.

## WPM2. The actual rank of the two stored mean entries

On (WPM.2) one has
$$
 \Pi h=(0,z_{\rm raw}).
$$
Consequently the exact map and its inverse on its range are
$$
 \begin{split}
 \zeta&=\iota_m z_{\rm raw},\qquad
 \iota_m z=n_g\sqrt{q/2}\binom z{-z},\\
 z_{\rm raw}&=\pi_m\zeta,\qquad
 \pi_m(\zeta_+,\zeta_-)
     =\frac{\zeta_+-\zeta_-}{n_g\sqrt{2q}},\\
 \pi_m\iota_m&=1,\qquad
 \iota_m\pi_m=\frac12
                \begin{pmatrix}1&-1\\-1&1\end{pmatrix}
       \quad\hbox{on the complete mean coordinate space}.
 \end{split}
 \tag{WPM.6}
$$
Thus $\zeta_-=-\zeta_+$ and the reflected mean image has rank one. This is real rank one for the real physical class and complex rank one after complexification of that same class; complex coordinates do not add a physical degree of freedom. Equivalently,
$$
 z_{\rm raw}=\frac{\sqrt{2/q}}{n_g}\,\zeta_+.
 \tag{WPM.7}
$$
The ambient map $n_gT:\mathbb C^2\to\mathbb C^2$ still has rank two. Formula (WPM.6) describes its restriction to the one-dimensional reflected raw mean subspace. It does not change the complete two-column maps used in old estimates.

There are two distinct levels of freedom.

1. At one endpoint, a reflected state has one independent even-mean value, stored as two dependent density entries.
2. Along a radial interval, $z_{\rm raw}(r)$ is an unknown function. In N's concrete graph domain it belongs to $H^1_r$. It becomes one endpoint constant plus a known integral only after its full coupled mean equation has actually been used.

A pair of stored numbers therefore does not produce two independent mean unknowns on this reflection subclass. Conversely, an endpoint rank-one identity does not turn the whole radial mean function into an already eliminated scalar.

When independent source, head, exterior, jump or reference ports are supplied, their original input spaces must be retained. If a particular port is restricted to physically compatible reflection data, its corresponding mean image satisfies the appropriate reflected relation. Different independently prescribed ports are still different inputs. The relation for one resulting state does not identify their data with one another.

## WPM3. Paired receivers and the one redundant waist average

Let $E$ exchange the two wave components. Directly from (WPM.2)--(WPM.5),
$$
 Rw=-Ew,\qquad Ry=Ey,\qquad \zeta=-E\zeta.
 \tag{WPM.8}
$$
The sign change in $RI=-IR$ is necessary in the second identity.

Use the same ordered strict waist normalizer $\mathscr T_{J_s}$ and its actual inverse as in WY/WPR, with the fixed $J_s=268435456$. WPR.7--9 derives its commutation with $ER$ from the original strict coefficients. Its two high-compressed factors preserve nonmeans and act as the identity on the mean block. Set
$$
 F_\sigma=(\mathscr T_{J_s}^{-1}y)_\sigma+\zeta_\sigma,
 \qquad K_0=R-2\Pi.
 \tag{WPM.9}
$$
Then the complete pair obeys
$$
 F_-=K_0F_+,\qquad \Pi F_+=\zeta_+,\qquad
 \Pi F_-=-\zeta_+.
 \tag{WPM.10}
$$
Here $K_0$ is reflection on nonmeans and minus identity on the mean. Its mean action cannot be replaced by ordinary reflection alone.

Put $\kappa_0=\sqrt{q/2}/n_g$ and $\mathbf e^T=(1,1)$. Exact reconstruction gives the raw value, its primitive, and its mean:
$$
 \begin{split}
 h_1&=\kappa_0\mathbf e^T
       \{\partial_\phi\mathscr T_{J_s}P F+\Pi F\},\\
 Ih_1&=\kappa_0\mathbf e^T\mathscr T_{J_s}PF,\\
 \Pi h_1&=\kappa_0\mathbf e^T\Pi F.
 \end{split}
 \tag{WPM.11}
$$
The derivative in the first line acts on the complete output of $\mathscr T_{J_s}$; it is not commuted through the variable coefficients. The primitive formula uses that this output has zero mean.

On (WPM.10), the last line is exactly zero. This is the sole redundant waist-average row under discussion. The complete condition $h_1(0,\phi)=0$ still requires
$$
 \mathbf e^T\mathscr T_{J_s}(0)P
        \binom{F_+}{K_0F_+}=0.
 \tag{WPM.12}
$$
Its raw target is the complete even meanzero primitive space, since $h_1$ is odd and $Ih_1$ is even. All its nonzero Fourier modes remain. Reflection does not solve this function-valued condition.

For a prescribed waist datum $b_1$, physical reflection requires $b_1$ odd and hence $\Pi b_1=0$. A nonzero prescribed first mean is incompatible with this restricted problem; it is not a new scalar condition that can be repaired by the independent even mean.

The paired endpoint reconstruction is an algebraic description of reflected endpoint states. It does not show that every such endpoint is attained by the regular given-head Poisson graph.

At the selected member, write the complete incoming and outgoing values as
$$
 i=U_{\mathcal H^{-1}}F_+,\qquad
 o=U_{\mathcal H^{-1}}F_-.
$$
True density pullback preserves the integral, so
$$
 o=K_{\mathcal H}i,\qquad
 K_{\mathcal H}
 =U_{\mathcal H^{-1}}R U_{\mathcal H}
       -2(U_{\mathcal H^{-1}}1)\otimes\Pi,
 \qquad \Pi o=-\Pi i.
 \tag{WPM.13}
$$
The last rank is a full-density mean column and stays in the operator. It generally has a nonconstant angular output. An auxiliary scalar constant in this selected angle cannot be substituted for the physical even-mean column without this exact change of coordinates.

There is also an exact endpoint separation of this mean direction. Define
$$
 h_{\mathcal H}=U_{\mathcal H^{-1}}1,\qquad
 i_0=i-h_{\mathcal H}\Pi i,\qquad
 \mathscr B_{\rm prim}(i)=
 \kappa_0\mathbf e^T\mathscr T_{J_s}P
       \operatorname{diag}(U_{\mathcal H},U_{\mathcal H})
                       \binom i{K_{\mathcal H}i}.
$$
Then $\Pi h_{\mathcal H}=1$, $\Pi i_0=0$ and
$K_{\mathcal H}h_{\mathcal H}=-h_{\mathcal H}$. In particular
$$
 \boxed{\quad
 \mathscr B_{\rm prim}(i)
      =\mathscr B_{\rm prim}(i_0).
 \quad}
 \tag{WPM.13a}
$$
Indeed $U_{\mathcal H}h_{\mathcal H}=1$, so the two raw encoded pairs differ by
$(\Pi i)(1,-1)$, which the displayed $P$ annihilates exactly. This is an identity for the endpoint parameterization. The even physical mean is still stored by $\Pi i$ and (WPM.7). The regular given-head Poisson graph need not contain the free direction $h_{\mathcal H}$, and $i_0$ need not be in its actual incoming image. Thus (WPM.13a) supplies neither a kernel of the PDE boundary map nor an independent free variation within that graph.

## WPM4. The even mean remains an independent coupled equation

Moving N.6--9 splits $h_2=f+z_{\rm raw}$ and inverts only the complete meanzero angular block. Its missing equation is
$$
 \begin{split}
 (z_{\rm raw})_r
 ={}&\{b(1-\langle S\rangle)-2bKm^2\}z_{\rm raw}\\
 &-2bm\langle uh_1+K(v-m)f\rangle+\langle g_2\rangle,
 \qquad S=u^2+Kv^2,\quad b=a_{\rm phys}'/a_{\rm phys}.
 \end{split}
 \tag{WPM.14}
$$
The reconstruction $h_1=J\{(D_0-B)f-z_{\rm raw}b_2-Pg_2\}$ retains the same $z_{\rm raw}$ and the same ordinary source. Inverting $J$ on meanzero functions does not invert or remove (WPM.14). For ordinary radial $L^2$ data the scalarized equation has its original divergence interpretation; no radial derivative of $g_2$ is assumed.

If $g_1$ is the physically compatible odd first source, $\Pi g_1=0$. The even second source has no such conclusion. The statement is about source admission, not a convention for deleting a mean from an arbitrary source.

This distinction is visible in PC's actual trial. PC.6 defines its second component using the old meanzero projector, but PC.7 retains
$$
 (g_n)_2=2bm\langle u h_{1,n}+K(v-m)h_{2,n}\rangle.
 \tag{WPM.15}
$$
This scalar is the physical even-mean residual of that trial. It need not vanish because the trial second component has zero mean. Means of amplitudes in the transformed $(T,X)$ variables are not substituted for this row.

PC.35 supplies its particular correction with zero stable root input, zero supplied head, and zero other exterior/affine inputs, together with its specified ordinary source. The resulting corrected columns solve the homogeneous high equation and retain their actual stable trace. PC explicitly keeps their finite-head equations and mean residuals as independent rows. Accordingly:

- a particular supplied head being zero is an input condition for that correction;
- a trial being meanzero is a property of the trial;
- a complete bound on its mean residual or on the corrected state's mean is an estimate;
- none of these is the assertion that the original mean matching equation has been solved.

The complete PC/AW/SW state discrepancies include both stored output means. A later complete bound for a restricted incoming value can therefore include their values while the mean matching equations remain unsolved. Those statements concern different maps and are consistent.

## WPM5. The amplitude coordinate does not absorb the even mean

Work only on the complete even boundary neighborhood admitted in A.2, including its unknown high tail and its independent mean. Put
$$
 \ell_v=D\mathcal A(v),\qquad e(\phi)=\cos(4\phi).
$$
A.12 proves $\ell_v[e]\ne0$ on that domain, and $\Pi e=0$. The map
$$
 h\longmapsto(\Pi h,\ell_v[h])
 \tag{WPM.16}
$$
has rank two on the complete even boundary space. Indeed, for arbitrary real $z,a$,
$$
 h=z\,1+\frac{a-z\,\ell_v[1]}{\ell_v[e]}\,e
 \quad\Longrightarrow\quad
 (\Pi h,\ell_v[h])=(z,a).
 \tag{WPM.17}
$$
This construction only uses the already bounded functionals and A's nonzero amplitude direction. It requires no new scalar enclosure.

The existing projection
$$
 P_vh=h-\frac{\ell_v[h]}{\ell_v[e]}e
 \tag{WPM.18}
$$
therefore satisfies
$$
 \Pi P_v=\Pi,\qquad \ell_vP_v=0.
 \tag{WPM.19}
$$
Keeping the mean unchanged is not the assertion that $\ell_v[1]=0$, or that $P_v$ is diagonal with respect to the mean/nonmean splitting. A mean input can produce a compensating $e$ component. Its mean remains the same.

The true amplitude row is
$$
 \ell_v[h_2(0)]+\delta\alpha=f_{\rm amp}
 \tag{WPM.20}
$$
in the unnormalized convention of A.17--24. It is not the automatically zero first mean in (WPM.11). If $\alpha$ is fixed, set only its prescribed variation $\delta\alpha$ to zero; the amplitude equation remains.

The rank-two statement is local to the complete boundary space at one admitted background. It does not prove independence of a propagated outer mean row and the waist amplitude row after the whole PDE and all other boundary conditions have been imposed. It does not prove the square complement inverse $\overline A^{-1}$, a finite Schur inverse, or a bound for a radial lift of (WPM.18).

## WPM6. The actual metric parameter and outer mean remain

The exact unnormalized metric-parameter column of A.17 is $-\partial_\nu F$ in the body. In normalized variables the complete column is instead
$$
 (0,s_\nu)_r-DF(0,s_\nu)-\partial_\nu F.
 \tag{WPM.21}
$$
The original $\alpha$ and normalization factors cannot be dropped when comparing these coordinates.

A.19--21 gives, with $h=(\xi,\zeta_{\rm raw})$ and $z_{\rm raw}=\langle\zeta_{\rm raw}\rangle$,
$$
 \begin{split}
 (z_{\rm raw})_r
 ={}&\beta(1-\langle S\rangle)z_{\rm raw}
       -2\beta m\langle u\xi+Kv\zeta_{\rm raw}\rangle\\
 &-\beta mK_\nu\langle v^2\rangle\,\delta\nu
       +\langle f_2\rangle,\\
 K_\nu={}&-wK+\frac{\beta w'}{2E_\nu}.
 \end{split}
 \tag{WPM.22}
$$
The bump $w$ here is the original metric bump, not the density state in (WPM.5). Compact support makes the explicit endpoint metric column zero; it does not make the body term or the propagated even mean zero.

Writing $\zeta_{\rm raw}=z_{\rm raw}+\zeta_0$ gives
$$
 (z_{\rm raw})_r=c_m z_{\rm raw}+g_m,\qquad
 c_m=\beta(1-\langle S\rangle-2Km^2),
$$
$$
 g_m=-2\beta m\langle u\xi+K(v-m)\zeta_0\rangle
       -\beta mK_\nu\langle v^2\rangle\,\delta\nu
       +\langle f_2\rangle.
 \tag{WPM.23}
$$
The exact endpoint representation is
$$
 z_{\rm raw}(r)=
 e^{\int_R^r c_m}z_{\rm raw}(R)
       -\int_r^R e^{\int_t^r c_m}g_m(t)\,dt.
 \tag{WPM.24}
$$
This retains the endpoint constant, the nonmean coupling, the parameter source and the ordinary mean source. It is a legitimate scalar elimination only with all these terms retained in the remaining system. It is not a free choice $z_{\rm raw}(0)=0$ or $z_{\rm raw}(R)=0$.

The physical outer curvature mean has the exact derivative
$$
 D C_0[h]=-\frac{z_{\rm raw}(R)}{m(R)^2}.
 \tag{WPM.25}
$$
The true outer-cap mean function and its complete derivative must also enter its matching row. This scalar is not the average of the odd waist condition, nor is it the mean of an Airy amplitude or of a selected first-coefficient function.

The actual $\nu$ Schur interface remains A.22--26. If the complete $\overline A^{-1}$ has been established, then
$$
 h_0=\overline A^{-1}f_{\rm bar},\qquad
 h_\nu=-\overline A^{-1}g_\nu,\qquad
 \mathscr S_\nu=b[h_\nu],
$$
$$
 \delta\nu=\frac{f_4-b[h_0]}{\mathscr S_\nu},
 \qquad h=h_0+h_\nu\delta\nu.
 \tag{WPM.26}
$$
The first line defines the true full columns, including (WPM.22). The second requires the separate nonzero scalar gate. Reflection, local amplitude rank, and the removal of a redundant odd mean row prove none of those gates.

## WPM7. High graph coordinates and independent physical rows

The original homogeneous high identity is
$$
 \Psi_A=\mathcal P_{\rm hom}S_{\rm tr}^{Y},
 \qquad
 \Psi_A N_i=\mathcal P_{\rm hom}C_s^{\rm fr}.
 \tag{WPM.27}
$$
It is the same given-head graph, with its specified other inputs zero. The independent terms $\mathcal P_{\rm rest}p$ remain when their data are supplied. This is the scope of PC.35, IN.28 and the corrected SE/FC/NIF factorization; it is not a representation of every reflected endpoint state as regular positive data.

The actual root97 gate removes the artificial FC kernel/cokernel completion columns on the admitted natural high space. Its completion rank zero is unrelated to $m=\Pi v$ or to the physical even-mean equation. A high coordinate isomorphism transports the other rows with $Id_{\rm rest}$; it does not solve them.

The corrected high input space is
$$
 X_s^{\rm fr}=\mathcal S_*D_+\mathcal H_{\rm nat}^s.
 \tag{WPM.28}
$$
Every such input has zero scalar integral because the root high space does, $D_+$ preserves it, and the full density map preserves the integral. This is an input statement. It does not imply that the complete incoming output has zero integral. In (WPM.13), $\Pi i=\zeta_+$ is the actual even-mean information generated by the entire column.

Likewise, the fixed numbers $\langle c_i\rangle$ and $\langle c_o\rangle$ of scalar first-coefficient functions are coefficients of an auxiliary operator. They are not unknown values of $z_{\rm raw}$, and they are not the two stored mean entries of $\mathcal Y$.

The whole radial supplied head remains in its original function space. Finite angular support does not make a radial function into a finite-dimensional datum. The original low/head equations, the true finite output rows in a different angle, the high/low cross maps and independent second-reference inputs cannot be counted or removed by the two mean storage slots.

## WPM8. Rank and domain ledger

| Object | Exact domain or realization | Actual freedom or row | Permitted conclusion |
|---|---|---|---|
| Raw first mean $\Pi h_1$ | Physical odd $h_1$ | Identically zero on that domain | Its waist average row is redundant for compatible odd waist data |
| Raw even mean $z_{\rm raw}(r)$ | $H^1_r$ in N's graph domain | One coupled radial function | Retain N.7 / A.19--21 and its endpoint/source terms |
| Two density means $(\zeta_+,\zeta_-)$ | Complete ambient $\mathbb C^2$ storage; anti-diagonal on a reflected state | Rank one on that state, with (WPM.6) | Retain both stored entries or substitute the exact injection/extraction on the restricted problem |
| Means of the encoded pair $(F_+,F_-)$ | Complete primitive-plus-mean readout | $(\zeta_+,-\zeta_+)$ | Keep the $-2\Pi$ in $K_0$ |
| Selected incoming scalar mean | Mean of the actual output $i$ | $\Pi i=\zeta_+$, possibly nonzero for high input | Keep the full transported mean vector in (WPM.13) |
| Physical amplitude | Complete even boundary domain of A.2 | One scalar functional independent of $\Pi$ locally | Use A's mean-preserving rank-one coordinate; retain the true amplitude equation |
| Physical outer curvature mean | True outer endpoint and cap map | Full derivative (WPM.25) plus cap derivative/data | Retain the actual outer matching row |
| Metric variation $\delta\nu$ | True fixed-point linearized parameter | Scalar with complete ordinary body and even-mean column | Retain (WPM.21)--(WPM.26), including $w'$ |
| Prescribed positive/root/head/source/outer/jump means | Each original independent port domain | Input variables or functions specific to that port | Apply reflection compatibility per port; do not identify distinct supplied data |
| Stable high root coordinates | Original natural high space | No physical Fourier-zero coordinate in their frequency powers | Their isomorphism removes only the specified FC completion, not physical mean matching |
| Airy/ray or first-coefficient scalar means | Their original transformed amplitude/coefficient spaces | Coefficients or integrals of known functions | Do not use them as substitutes for a physical mean unknown or row |

The table distinguishes the number of entries in a representation from the rank of a restricted map and from the number of independent equations of a coupled boundary problem.

## WPM9. The exact reduction that is available

On the already admitted physical reflection domain, the original waist residual can be written as its primitive and its mean. The second component is identically zero. For compatible data, deleting that zero residual component and replacing the two stored means by $z_{\rm raw}$ using (WPM.6) gives an equivalent restricted system.

This reduction has three conditions:

1. The physical odd/even restrictions are imposed on the state and on every independently supplied datum to which the relation is applied.
2. All other appearances of the density means use the exact injection/extraction, the true density maps and the full mean-rank columns.
3. The even mean ODE, true outer mean/cap row, physical amplitude equation, metric-parameter column and all independent rest/head equations remain.

The result is equivalence of two representations of the same restricted problem. It is not a proof that the resulting block is square, onto, nonsingular or suitably small. Those conclusions require the original physical source and target, the complete graph constraints and the full finite/mean Schur analysis. In particular one must not create a square system by treating two dependent density means as two free unknowns and then using an automatically zero odd mean row as an independent equation.

## WPM10. Immutable primary identities

All file paths in this table are relative to the topic's results directory. The WPR entry is the exact paired-row text reviewed with this ledger; its formulas are also derived from the original strict coordinates used above.

| Primary | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| Moving N.3--9: physical reflection, scalarization and complete mean | R133-supplement-complete-moving-root-scalarization.md | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| Strict N.4--13: actual density, two mean slots and ordered normalizers | R133-supplement-complete-negative-source-to-strict-density-cut-readout.md | da51581b623d4167ae9278af6892bc9a0591fb3f | 13892 | 4d44bbe7082d4ee967ebf9d02284b3510624624ab98adb087b8d0499eb030376 |
| A.12--26: complete amplitude coordinate and true mean/parameter Schur | R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md | 511c9ca83972003796c4c4fa456236f32095e3e3 | 13237 | 825113583ae91127e6b99fc839a7b5fd32bdaa660befcce5c7d5728c253f0538 |
| PC.6--7, PC.35--37: trial mean residual and actual correction domains | R133-supplement-genuine-positive-Airy-cutoff-and-complete-strong-correction-columns.md | 35f3ddaec691c2d7c636ec43da3f52605ed6b329 | 37079 | 5368abae4c66f73800c16d5f2b906ddaa0f1d62d07e9bd9a3ca539061bdf5d68 |
| IN.28--30: homogeneous high factor and independent rest rows | R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md | f13509b4d0afc691cfc95d86c0f8e5562f919129 | 33894 | d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75 |
| Corrected NIF: actual reflected inverse-image domain | R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md | d606faa1ffd30c34d3487985a57dbc62a18890bc | 32942 | 8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640 |
| FC.18--26: same graph and independent complete columns | R133-supplement-finite-Fredholm-completion-of-the-actual-regular-Ai-graph.md | 8b7ff6fe74fa4ce914c8bc0c2192deae85ce0768 | 20794 | 46ccc206c86afef16ee3d3221162f0e5c373ad8420283bc9fbe40e52fe3e24bd |
| WPR.3--21: complete physical pair and exact raw waist rows | Exact reviewed paired-row text | 226272031762c5fcace679dd7f940a35040401dc | 22571 | 707b8269e454cab738fe70d84097087a0cf5c74026916a2f8bdc151435eca9cb |

No new scientific quantity was evaluated in this proof. The only new conclusions are the explicit reflected mean rank, the complete row/domain ledger, and the local rank-two separation of even mean and physical amplitude on A's already admitted domain.
