# R133 supplement: complete correlated phase twist and its true defect corrections

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved.** For the explicit continuous family of the preceding direction
theorem, a complete interval calculation through the actual root gives
a strictly positive first phase functional. Both corrections needed to
turn that functional into the genuine weighted parameter row of R31
are paid explicitly. In physical angle units, that parameter row is
greater than $1/600$ whenever the **true** phase defect satisfies
$\|E\|_\infty\le10^{-6}$ and $\|E_\phi\|_\infty\le10^{-4}$.
After $x=4\phi$, the R31 row is greater than $1/150$.

The full transport run must still supply those two actual defect
bounds. The sampled fit is not used for them. This theorem concerns
the explicit approximate-centre family, not an already proved PDE
solution branch or a whole-body inverse.

## 1. Actual fields, complete products and signed scalar integration

Use the exact continuous background and direction from
[the explicit direction theorem](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md).
All scalar quantities are the true metric coefficients at the fixed
$\eta=\eta_0$, $\delta\eta=0$, $\nu=\nu_0$.
For $Q_\delta=\bar Q+\delta(\xi,\zeta)$ and
$\nu_\delta=\nu_0+\delta$, put $z=\langle\zeta\rangle$ and
$k=Tw'$. The complete derivatives at $\delta=0$ are

$$
 \dot d=\beta I_\phi
   \{2u\xi+(k-wK)v^2+2Kv\zeta\},
 \qquad
 \dot c=-\gamma qz+\frac{\gamma mk}{2q},
 \qquad \dot F_\pm=\dot d\pm\dot c.
 \tag{T.1}
$$

The quotient $k/q$ is used only on the true compact support. Outside
it, $k=0$ exactly, including the entire root remainder. The numerator
in (T.1) is evaluated as one complete Fourier polynomial before taking
its norm. In particular the $u\xi$, $Kv\zeta$, direct metric and true
mean terms are not independently replaced by absolute product bounds.

The actual base has 32 angular pairs and the explicit direction has
96. The complete output of every product in (T.1) has physical angular
index at most 128. The new consumer retains every such output, with
the exact sine/cosine sign convention, and sets only the primitive's
genuine zero Fourier multiplier to zero. It does not discard the even
state mean $z$ or an unretained product frequency.

All 626 true scalar cells are intersected with the actual radial
cubics, producing 3,095 complete intersections on $[0,r_b]$. The
original coefficient dyadics, complete continuous-repair envelopes
and full scalar Taylor errors are included. At the remaining root
interval $[r_b,r_*]$, the source uses the same actual analytic germ and
the exact identity

$$
 0\le q^2(r)\le K'_*\,(r_*^{\rm upper}-r).
 \tag{T.2}
$$

The complete scalar root contribution obeys

$$
 \left|\int_{r_b}^{r_*}\dot c\,dr\right|
 \le \frac23\gamma_*|z|_*\sqrt{K'_*}
               (r_*^{\rm upper}-r_b)^{3/2}.
 \tag{T.3}
$$

All finite direction and base coefficients are evaluated on that
whole remainder, including the exact repair allowances. No scalar
Taylor box is extrapolated beyond its accepted interval or across a
PPoly germ.

The actual complete integration gives

$$
 \begin{aligned}
 0.0087198199503
 &<\int_0^{r_*}\dot c\,dr<0.0120281321284,\\
 \int_0^{r_*}|\dot c|\,dr&<0.075420880,\\
 \int_0^{r_*}\|\dot d\|_{L^2_\phi}\,dr&<0.069404292,\\
 \int_0^{r_*}\|\dot d\|_{A_0}\,dr&<0.123021931.
 \end{aligned}
 \tag{T.4}
$$

The native also retains complete $A_{1/64},A_{1/32},A_{1/16}$ bounds
and the first two angular derivatives of $\dot d$. All signed and
absolute scalar integrals include the root remainder.

## 2. Actual inverse-ray labels and a positive first functional

Let $H_\pm(r)$ be the actual characteristic maps of $F_\pm$, and
$S_\pm(r)=H_\pm(r)^{-1}$. The true return is

$$
 P=S_-(r_*)\circ H_+(r_*).
 \tag{T.5}
$$

Let $H(\phi)=\phi+h(\phi)$ be the exact saved 24-mode trial coordinate,
and define

$$
 A_\pm(r,\theta)=H(S_\pm(r,\theta)),
 \qquad a_\pm=\partial_\theta A_\pm.
 \tag{T.6}
$$

The degree-one lift identity gives $\langle a_\pm\rangle=1$ exactly.
This is true without assuming that $H$ conjugates $P$ to a rotation.
The complete finite coefficients give

$$
 \|H'-1\|_{A_0}<0.015523220.
 \tag{T.7}
$$

The already proved actual real one-leg Jacobian estimate uses
$L_d<0.036374622$. Consequently

$$
 \|a_\pm-1\|_\infty
 \le(1+\|H'-1\|_{A_0})e^{L_d}-1
 <\varepsilon_a:=0.053142540.
 \tag{T.8}
$$

Define the complete first functional

$$
 \Gamma_0=\int_0^{r_*}
     \left\langle a_+^2\dot F_+-a_-^2\dot F_-\right\rangle dr.
 \tag{T.9}
$$

Since $a_\pm$ are real and have exact mean one,

$$
 \langle a_\pm^2\rangle=1+\|a_\pm-1\|_2^2.
 \tag{T.10}
$$

Thus the scalar-speed error around $2\int\dot c$ is at most
$2\varepsilon_a^2\int|\dot c|$. The mean-zero drift term is bounded
by $2(2\varepsilon_a+\varepsilon_a^2)\int\|\dot d\|_2$.
The complete unrounded native yields

$$
 \begin{aligned}
 E_c&<0.000425996655,\\
 E_d&<0.015145294626,\\
 \boxed{\quad 0.0018683485714<\Gamma_0<0.0396275555859.\quad}
 \end{aligned}
 \tag{T.11}
$$

In the first native this enclosure is named
`complete_zero_conjugacy_defect_twist_enclosure`: it is the complete
functional (T.9), which agrees with the uncorrected twist when the
conjugacy defect is zero. The actual defect is not assumed to vanish.

## 3. Exact nonzero-defect two-ray identity

For the specified target angle $\Omega$, let

$$
 E(\phi)=H(P(\phi))-H(\phi)-\Omega,
 \qquad e(\phi)=E'(\phi)/H'(\phi).
 \tag{T.12}
$$

Put

$$
 \overline\Gamma
   =\left\langle H'(P)\,\partial_\delta P\,H'\right\rangle.
 \tag{T.13}
$$

The complete two-leg parameter variation, followed by the actual
change of angular variable on each leg, gives

$$
 \overline\Gamma=\int_0^{r_*}
  \left\langle
   a_+^2(1+e_+)\dot F_+
    -a_-^2(1+e_-)^{-1}\dot F_-
  \right\rangle dr,
 \tag{T.14}
$$

where $e_+=e\circ S_+(r)$ and
$e_-=e\circ P^{-1}\circ S_-(r)$. To verify the factors, the plus-leg
variation contributes $P'/H_+'(r)$, while the change of variable adds
another $1/H_+'(r)$. The identity

$$
 H'(P)P'=H'(1+e)
 \tag{T.15}
$$

gives the first factor. On the minus leg one first changes from the
initial angle to the final angle by $P'$, so the same identity gives
the reciprocal factor in (T.14). Both signs and the order of the
actual forward/backward maps are retained.

Let $h_-=1-\|H'-1\|_{A_0}$ and
$\eta_E=\|E'\|_\infty/h_-<1$. Equations (T.9) and (T.14) give

$$
 |\overline\Gamma-\Gamma_0|
 \le 2(1+\varepsilon_a)^2\frac{\eta_E}{1-\eta_E}
        \int_0^{r_*}(\|\dot d\|_2+|\dot c|)\,dr.
 \tag{T.16}
$$

The full state mean is present in $\dot c$ and in this correction.
No pointwise sign for $\partial_\delta P$ is assumed.

## 4. The true R31 coordinate and its second correction

The R31 initial coordinate in physical angle units is $H_0=H^{-1}$.
Its weighted parameter row is

$$
 \sigma_{\rm phys}
 =\left\langle
     \frac{(\partial_\delta P)\circ H^{-1}}
          {(H^{-1})'\circ R_\Omega}
   \right\rangle.
 \tag{T.17}
$$

Let $P_0=H^{-1}\circ R_\Omega\circ H$. Changing variable $x=H(\phi)$
in (T.17) shows

$$
 \sigma_{\rm phys}
     =\langle(\partial_\delta P)H'(P_0)H'\rangle.
 \tag{T.18}
$$

This differs from (T.13) by the genuine output-coordinate defect.
The complete real flow variation gives

$$
 P_1:=\|\partial_\delta P\|_\infty
 \le2e^{2L_d}\int_0^{r_*}(\|\dot d\|_{A_0}+|\dot c|)\,dr.
 \tag{T.19}
$$

Since $\|P-P_0\|_\infty\le\|E\|_\infty/h_-$, one has

$$
 |\sigma_{\rm phys}-\overline\Gamma|
 \le P_1(1+\|H'-1\|_{A_0})\|H''\|_{A_0}
             \frac{\|E\|_\infty}{h_-}.
 \tag{T.20}
$$

For the two explicit **true** defect gates

$$
 \|E\|_\infty\le10^{-6},\qquad
 \|E'\|_\infty\le10^{-4},
 \tag{T.21}
$$

the second complete consumer gives

$$
 \begin{aligned}
 \text{right side of (T.16)}&<0.000032635254,\\
 \text{right side of (T.20)}&<0.000000035045,\\
 \boxed{\quad\sigma_{\rm phys}>0.0018356781856>1/600.\quad}
 \end{aligned}
 \tag{T.22}
$$

In the normalized circle $x=4\phi$, use
$H_{0,x}(x)=4H^{-1}(x/4)$ and $P_x(x)=4P(x/4)$.
The derivative denominator in (T.17) is unchanged while its numerator
has a factor four. Therefore

$$
 \boxed{\quad\sigma_x=4\sigma_{\rm phys}
      >0.0073427127427>1/150.\quad}
 \tag{T.23}
$$

This is the genuine row in R31, subject only to the still explicitly
required true gates (T.21). It is not an unweighted rotation-number
finite difference or a principal action derivative.

## 5. Actual reports and remaining gates

The correlated producer
`scripts/fourfold_codazzi_phase_correlated_first_parameter.py` completed
all six full-field gates in 97.346 seconds. Its report is
`notes/2026-11-14-R133-complete-correlated-first-phase-parameter-native.json.gz`.
The complete 3,095-row prefix and root remainder are retained. Its
intermediate checkpoint is only a retained prefix, never the complete
conclusion.

The correction consumer
`scripts/fourfold_codazzi_phase_parameter_transversality_budget.py`
completed seven gates and wrote
`notes/2026-11-14-R133-phase-parameter-transversality-defect-gates-native.json.gz`.
It consumes the exact complete first report and records (T.21) as
hypotheses. It explicitly records that the final full transport defect
has not yet been consumed.

The first command, from the topic directory, is

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_phase_correlated_first_parameter.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --trial /workspace/scratch/ac0d699811ad/regular-head-trials-20261114/response/work/2087c0f1ee3c7d28de47af8866438c34d4e7f9741918adc5b1c25547fcd1bde3/trials/response-full.json \
  --partial /workspace/scratch/ac0d699811ad/phase-next-20261114/correlated-first-parameter-partial.json.gz \
  --out notes/2026-11-14-R133-complete-correlated-first-phase-parameter-native.json.gz
```

The second command is

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps OPENBLAS_NUM_THREADS=1 \
python scripts/fourfold_codazzi_phase_parameter_transversality_budget.py \
  --out notes/2026-11-14-R133-phase-parameter-transversality-defect-gates-native.json.gz
```

The full transport must now supply (T.21), and the parameter KAM step
must still pay its analytic derivative bounds, smallness and actual
parameter domain. The true PDE and phase must ultimately be corrected
together at one final metric parameter. No true PDE solution branch,
full returned inverse or completed flex family is concluded here.
