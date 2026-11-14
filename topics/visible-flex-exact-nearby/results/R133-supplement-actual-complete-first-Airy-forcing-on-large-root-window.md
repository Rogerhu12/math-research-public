# R133 supplement: actual complete first Airy forcing on the radius-1/50 root window

## F.1. Actual result and precise scope

Public Actions run [43624260519](https://github.com/Rogerhu12/math-research-public/actions/runs/43624260519), attempt 1, completed the first-forcing computation with actual mathematical exit code 0 and all 14 gates true. The mathematical child took 39.161968501 seconds. Its complete native contains 1328 closed common cells: the one previously accepted cell was reused unchanged and precisely 1327 new cells were computed.

This is a bound for the complete actual degree-zero operator $L_0v_0$ and the two first forced Airy amplitudes in the explicit family $Q_\delta=Q_0+\delta Z$, $\nu_\delta=\nu_0+\delta$, at the fixed physical $\eta_0$, for real $|\delta|\le 10^{-8}$. It is not the complete residual of the reconstructed nonlocal system. The original primitive, inverse, projection and mean remainders, the reconstructed next-amplitude jumps, and the final strong return norm remain separate.

The derivation and conventions are those of [the first-forcing and radial-inverse-jet proof](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md), the nonsingular forced-amplitude construction, and [the exact first-forcing seam identity](R133-supplement-exact-first-forcing-seams-and-first-correction-jump.md). In particular, the component order of the two forcing equations is $(F_b,F_a)$. No local scalar potential is substituted for the degree-zero contribution of the old nonlocal inverse.

## F.2. Identity, coverage and actual process

The workflow event and actual scientific checkout both equal

    865b9b70b0cd12fc5ab48fcbc6c3cd38a9738584

The original radius-1/50 root native, its complete 1300 coefficient rows and all 1079 seam records were reused. The six original intrinsic parts supply 1144 selected original cells; common subdivision produces the 1328 accepted cells. No original target solve, root-row computation, candidate reconstruction or response solve was repeated.

The exact enclosing interval is

$$
\left[\frac{1091984371497}{5000000000000},
      \frac{2583968743003}{10000000000000}\right],
$$

and the true-root enclosure is

$$
\left[\frac{1191984371497}{5000000000000},
      \frac{2383968743003}{10000000000000}\right].
$$

The whole interval lies outside the compact intrinsic support of the $\nu$ perturbation. Thus the intrinsic jets at fixed $\eta_0$ apply to the same $\nu_\delta$ family here; the full 193-component direction, both exact repairs and the even mean remain in the polynomial and seam bounds.

The native has 6577892 bytes and is retained without splitting in artifact

    visible-exact-actual-first-Airy-forcing-43624260519-1
    consumers/actual-first-Airy-forcing.json.gz

Its complete process is [the 36229-byte process record](../notes/actual_first_Airy_forcing_ci/run-43624260519-1/consumers/process.json); publication provenance is [the 4334-byte worker record](../notes/actual_first_Airy_forcing_ci/run-43624260519-1/worker-process.json).

| Object | SHA-256 |
| --- | --- |
| Complete first-forcing native | 54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47 |
| Mathematical producer | ba25934f0f6e147f293644edc93b2adf1c33d5935f86596d96355cf063c95fa6 |
| CI driver | eb6ac89d60a378f9d9b66e5a32da4e52ab5655b79c8ae646ffad73df7fb88cff |
| Manifest, 24 fixed inputs | a7790a87932a22997e29dfa2085982ac7adbbef9fd36512918eec975dd3c5341 |
| Mathematical process | 0f4d1dd4b33bf80c40e5ef65a169e0012bfd4f47746a8b7fbe7134557af5b145 |
| Worker process | 9f0a156ecbb3f1a2f411b0d7b8ead0b0af531ebc76d098b2985cca8025315932 |
| Reused complete root native | dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212 |

Both actual worker pulls left the checkout at the stated commit; both root/topic README diffs were empty. The worker retains the reviewed-rule commit and reports topic completion as false.

## F.3. Strict bounds from the native

All decimal inequalities below are outward weakenings of the recorded Arb bounds. They are analytic supremum bounds, not same-width Wiener bounds.

The coefficient, leading-amplitude, forcing and output strips are respectively

$$
1/16,\qquad 3/64,\qquad 5/128,\qquad 1/64.
$$

The leading rays remain in an old-angle strip of width less than $0.058217876514865<1/16$; the forcing rays remain in width less than $0.038369173227740<5/128$. Both divided-phase and root-frame gaps pass their strict positivity gates.

| Complete quantity on the stated family and window | Strict upper bound |
| --- | ---: |
| $\|L_0v_0\|_\infty$ for the full pair | 268394.856049072 |
| First angular derivative of that pair, after the stated strip loss | 34354541.574282 |
| First forced amplitude $\|a_1\|_\infty$ | 7731800.525026 |
| First forced amplitude $\|b_1\|_\infty$ | 11178348.024174 |
| Matrix $H^{-1}$, recorded column-sum bound | 1.043052650849 |
| Matrix $H_D$, recorded column-sum bound | 16.257529915022 |
| Leading $\|a_0\|_\infty$ | 2.349330993382 |
| Leading $\|b_0\|_\infty$ | 0.032159149767 |
| Leading $\|\partial_r^2a_0\|_\infty$ | 601596.165774 |
| Leading $\|\partial_r^2b_0\|_\infty$ | 17046.505371 |

The full branch factors in the nonsingular forced formulas are retained. The common next-amplitude root trace is exactly zero. These amplitude bounds are finite but large; this computation does not establish smallness of the first correction at frequency 97.

The actual sum of absolute even-mean first-derivative jumps is less than $2.711255457450\cdot10^{-15}$. The actual sum of the corresponding first radial optical-amplitude jumps is less than $5.389567397748\cdot10^{-14}$. The resulting second-radial divided-phase seam fee is less than $7.135631736677\cdot10^{-9}$; its mixed angular fee is less than $2.522421238273\cdot10^{-13}$. Every seam is separated from the complete root enclosure; the recorded minimum separation is exactly

$$
\frac{125978004170690098219}{10995116277760000000000000}.
$$

These fees have already been included in the mixed-jet and first-forcing bounds. They do not replace the still separate reconstructed state-jump operator.

## F.4. Preserved failure evidence and exact one-cell reuse

Run 43622131835 produced one valid accepted cell before encountering an undefined Taylor evaluation on the next cell. Its native is retained with SHA-256

    ac235e9e0f9fb1880cc4adc83efc87b2653b0e02e53b0bdd70d20862a3798b0a

Run 43623626229 reused that cell and diagnosed the same issue: the original positive whole and midpoint gamma enclosures were finite, while general integer powers of a zero-centred interval produced NaN in this pinned runtime. Neither failure was a negative gamma certificate.

The successful run contains a direct runtime audit: powers 1, 2 and 3 through that general entry return NaN on the test interval, whereas bounded Horner evaluation of the identical cubic, intersected with its original whole jets, is finite and encloses all four midpoint derivatives. Taylor factorials and the original whole third derivative are unchanged. No absolute value or artificial positive replacement is used.

The one old cell was accepted under the explicitly pinned original source and manifest; its wider certified enclosure remains valid. The new code whitelists that exact historical prefix and checks all immutable input identities. It does not generally accept a prefix from an unrelated producer.

## F.5. Remaining quantitative boundary

This result supplies complete first-forcing data and real radial inverse jets for subsequent consumers. All original 1079 seams remain available with their exact identities. A consumer may aggregate these already proved rows on smaller root windows and evaluate the complete seam operator in the established negative source window.

The old $I/J$ remainders, independent mean source, complete reconstructed amplitude seams, positive affine-port conversion, and final $C_E,C_s$ still require their own complete estimates. The native explicitly leaves the strong return norm, numerical cutoff-97 inverse and true PDE branch claims false.
