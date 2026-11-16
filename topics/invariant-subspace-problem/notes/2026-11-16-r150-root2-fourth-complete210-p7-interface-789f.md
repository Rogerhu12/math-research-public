# R150: complete210 fourth page with the original arithmetic modulo 31^7

Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.  
Status: executable interface and proof of scope. The new complete fourth page has not been executed.

## 1. Exact question after the two zero probes

Use the original 17 primitive equations, all 6188 multiplier sources of
degree at most 3, and all 4367 target monomials. Put $p=31$,
$D=\mathbb Z_{(31)}$, $t=s-2$, $L=\operatorname{im}A$,
$N=V\cap\operatorname{im}_{\mathbb Q(s)}A$, and $C=N/L$.
The complete colon identity is $\operatorname{im}B=L:p^2$, with actual
original sources satisfying $AS=p^2B$.

The [sixteen-summand theorem](../results/R150-appendix-coefficient31-sixteen-cyclic-summands-and-one-remaining-exponent.md)
leaves just one coefficient-$31$ cyclic exponent $E\ge6$, supported at
root2. The complete incoming space
$I_5=\operatorname{im}(C[p^5]\longrightarrow C/pC)$ has dimension 15.
Its original 315-coordinate basis and parameter action are the
'futureCompleteIncoming15Full315' and 'futureCompleteIncoming15SAction'
arrays of the paid complete210 preparation.

Run 43798780106, job 133073660023, completed the two selected recipes at
indices 208 and 209. Their full 315 classes have SHA256
'f1a0d314fe738a42b8d72313fe11b3f89b870b5a196e3cd27886371a331c33c6';
their 300 by 2 quotient has SHA256
'bd50e12c55dda3ee443c1cb6d71c7bcf6351c4ec96f7bc8d6adec015d1192eea'
and rank zero. The completed raw output was 26380 bytes, SHA256
'1ac76082fa32eecf1e8f0939515909efceb712056abf2f7acc059ee33eb397d4'.
This is a two-source result only; it leaves $E\ge6$.

The present entry computes all 210 recipes, including all six recipes
that vanish only in the field description. It checks their full
polynomial image under the original parameter action. After every
original-source and completeness gate succeeds, the two possible
conclusions are

$$
\begin{array}{c|c|c}
\dim(I_6/I_5)&E&\dim I_4(B)\\
\hline
1&6&9\\
0&\ge7&8.
\end{array}
$$

The fourth successive increment is $\dim(I_4(B)/I_3(B))$; it is not
$\dim I_4(B)$, since the paid $\dim I_3(B)$ is 8.

## 2. Full source coverage

The complete old source family consists of 197 corrected original
$K_2,\ldots,K_{198}$. Its next complete kernel has 204 generators:
six actual original $p^4$ sources and 198 corrected relations. The 198
relations are the 196 omega relations followed by the two exact
$t$-relations. The alpha and beta arrays therefore each have length 196;
they do not include the two final relations.

The six original $p^4$ sources come from the seven-column
'currentK4.bin' family with labels $7001,\ldots,7007$, using zero-based
indices

$$
(0,1,4,5,6,3).
$$

Thus the complete 204 labels begin
$(7001,7002,7005,7006,7007,7004)$ and continue with
$15001,\ldots,15198$. These columns are multiplied by the exact original
equations anew modulo $p^7$. The old modulo-$p^5$ product is used only
to authenticate the original source and its $p^4$ divisibility.

The paid next two polynomial kernels are

$$
F_2=[I-T_2C_2,\ T_2(sI-J_2)],\qquad
F_3=[I-T_3C_3,\ T_3(sI-J_3)].
$$

Here $C_2$ is the complete four-dimensional second image, $T_2$ selects
the actual indices $6,\ldots,9$, and $F_2$ is 204 by 208.
Likewise $C_3$ is the complete two-dimensional third image, $T_3$ selects
the actual indices 10 and 11, and $F_3$ is 208 by 210.
Both generation statements use the complete paid source families.

For clarity, the polynomial generation formula follows directly from a
section. If $CT=I$ and multiplication by $s$ on the image is $J$, then
every polynomial source vector is, modulo
$[I-TC,\ T(sI-J)]$, represented by $T v$ for a constant image vector
$v$. Such a vector is in the kernel exactly when $v=0$.
Consequently these columns generate the whole polynomial kernel,
including all polynomial multiples. This is the full kernel statement,
not a search among a list of constant vectors.

The current driver retains every column of these two matrices. It does
not omit inherited field-zero indices $6,7,8,9$, direct field-zero
indices 10 and 11, or their original integer carries.
The final result records the actual 315 classes of all six indices.

## 3. Canonical lifts and complete original stages

Every source below is written in the original 6188-coordinate order.
The original field representatives and correction coordinates are
unchanged. In particular the two final canonical $F_3$ polynomials are
$s+29$, whose exact Taylor lift at $s=2+t$ is

$$
s+29=31+t.
$$

The integer constant 31 is retained. In contrast, the two final
relations of the earlier 198-family are the exact prescribed
$t$-relations. These distinct source choices are not interchanged.

The true correction basis has divisor exponents

$$
(1,1,2,2,2,2,2,3,3,4,4,4,4).
$$

The first seven are the original $U_7$ sources. The next two are the
actual eighth divided source and the original $L_{3,K_2}$ source.
The last four are the actual $D_4$ sections, now at indices $6,\ldots,9$
of the full 204-column $L_4$ family.

| Stage | Full count | Exact original source numerator | Computed terms | Stable formal terms |
|---|---:|---|---:|---:|
| $T_2$ | 197 | $K-pq_1-\sum p^{2-e_i}\kappa_i C_i$ | 25 | 25 |
| $L_3$ | 197 | $T_2-p^2q_2$ | 25 | 20 |
| $M_3$ | 198 | All 196 omega and two $t$ relations, with seven original corrections | 20 | 20 |
| $L_4$ | 204 | Six original $p^4$ sources, followed by $M_3-p^3q_3$ | 20 | 15 |
| $M_4$ | 208 | All canonical $F_2$ combinations, with all nine corrections | 15 | 15 |
| $L_5$ | 208 | $M_4-p^4q_4$ | 15 | 10 |
| $M_5$ | 210 | All canonical $F_3$ combinations, with all thirteen corrections | 10 | 10 |
| $L_6$ | 210 | $M_5-p^5q_5$ | 10 | 5 |

Each of these eight integer stages computes all 4367 output rows using
the original 17 equations and checks the required divisibility by
$p^2,\ldots,p^6$ coefficient by coefficient modulo $p^7$.
There is no deletion of a zero field recipe before this calculation.

The global $q_1$ source polynomial is evaluated to 25 actual Taylor
coefficients. All four subsequent field solves use all 1034 quotient
rows, all 1021 original $G$ columns, and all 13 free conditions.
The normal-form graph, source transport, forward DAG and backward DAG
are all the pinned original objects.

Before proceeding, the computed $D_3,D_4,D_5$ classes must equal the
complete paid matrices, respectively all 197, 204 and 208 columns.
At the final stage, columns 208 and 209 must reproduce both exact
hashes from the actual two-probe run. A changed representative is a
verification failure; it is not silently admitted as an equivalent
source.

## 4. Finite precision, completion, and the meaning of a zero full page

The [original nested-precision lemma](2026-11-15-r150-saturated-pages-integer-carry-and-nested-jet-precision-789f.md)
applies to the complete original matrix over $k[[t]]$,
$k=\mathbb F_{31}$, whose nonzero root2 Smith exponents are at most 5.
If an actual formal right hand side $r$ belongs to its image and a
finite source satisfies $\bar A q_N=r\bmod t^N$, an exact formal
solution can be chosen to agree with $q_N$ through degree $N-6$.
Indeed, in active Smith coordinates the difference is divisible by
$t^{N-a_i}$, and kernel coordinates are free.

At each stage, the formal-image hypothesis is verified, not assumed.
The right hand side is an original divided integer source, so its
augmented rank identities and the common generic rank 4354 exclude a
generic free obstruction. The paid complete 315 class or the completed
original field solve removes the root2 torsion obstruction. Five
Taylor coefficients detect that obstruction. Equal source prefixes
can then be lifted as equal canonical integers before the next carry.
This gives the exact precision chain

$$
25\longrightarrow20\longrightarrow15\longrightarrow10
\longrightarrow5.
$$

The final CRT8 representation is a representation of the local class:
three root1 slots are zero, and five root2 slots are retained.
It is not asserted to be a global original polynomial divided source.
The consumer verifies all 104 local free conditions, reconstructs all
39 local torsion coordinates, embeds them in all 315 original torsion
coordinates, and checks all 505 original global free observations.
It also checks the actual multiplication-by-$s$ action.

Complete the finite $D$-module $C$ at $p$. Its monic parameter
annihilator gives a Hensel/CRT decomposition into the root2 part and
the complementary primary parts. On the root2 part $t$ is
topologically nilpotent, and the $(p,t)$ completion is that same finite
$\mathbb Z_{31}$ summand. This exact completion preserves the
coefficient-$p$ elementary divisors. Thus the finite calculation
represents the corresponding genuine formal coefficient-torsion
classes.

Because all 210 polynomial kernel generators have been retained,
a completed zero quotient, together with the parameter-action closure,
proves that the entire fourth successive image of $B$ is zero.
It therefore proves $E\ge7$. This inference was unavailable from the
two-probe result. Conversely any nonzero quotient class proves
$E=6$. Both branches require every lower-page comparison and original
multiplication gate; a resource stop or failed gate proves neither.

## 5. Sources, recovery, and exact input identity

The new driver is
'2026-11-16-r150-root2-fourth-complete210-p7-runner-789f.py',
36750 bytes, SHA256
'ad18b9749976bbc2c011575c29960709e0b954d54f3ef0cda75c8f4d126fc60d'.

All thirteen mathematical helper hashes are unchanged from the actual
two-probe job. They include the p7 integer consumer, genuine 25-term
$G/V$ source transport, complete unit solver, original model builder,
complete210 preparation and original quotient readers.

The independent job uses the same original ten inputs, the six paid
small B2/B3 files, the four original true-source members, the exact
primitive JSON and the two local quotient-map files as the successful
two-probe job. The new manifest repeats every byte count, historical
ref and SHA. It does not require a surviving temporary session.

One additional original family is restored by
'2026-11-16-r150-root2-fourth-current-k4-input-recovery-789f.py',
6563 bytes, SHA256
'6c8940b37e5f843717e15f9e5feb2e6e153665884e0200fbdadacf29644c1787'.
It reads only the two pinned compressed parts at immutable commit
'8c6304e273e64b0544d3dd58bc0e48a672a87c36'. Together they are 6399260
bytes; their decompressed original source is 7645286 bytes, SHA256
'a5e16cfe2f6c6665c0806c488ea0ba3db11516e81be259c1f213126d9339566a'.
The accompanying paid product receipt authenticates the entire
seven-column family and its original $p^4$ divisibility. The new p7
products are computed independently.

The four-source extra-input restore is unchanged and pins the previous
positive-two input manifest, blob
'51317ff4432dbab4707c31413454d540a80506a7'. Supply that previous manifest
to the unchanged restore script, not the new full210 manifest. This is
an explicit input dependency; it does not reuse an unverified old
mathematical result.

Suggested currentK4 recovery:

~~~text
python SCRIPTS/2026-11-16-r150-root2-fourth-current-k4-input-recovery-789f.py
 --repo REPO
 --out WORK/root2-fourth-true-source-inputs
 --seconds 180
~~~

Suggested full mathematical invocation:

~~~text
python SCRIPTS/2026-11-16-r150-root2-fourth-complete210-p7-runner-789f.py
 --notes-root SCRIPTS
 --original-input-dir WORK/global197-original-inputs
 --small-input-dir WORK/root2-fourth-small-inputs
 --true-source-dir WORK/root2-fourth-true-source-inputs
 --exact-gzip WORK/original127-inputs/original-primitive-integer-equations.json.gz
 --jet-map-dir WORK/root2-fourth-jet-map
 --recipe WORK/root2-fourth-complete210-preparation/complete210-fourth-source-recipes.json.gz
 --out WORK/root2-fourth-complete210-p7
 --seconds 1800
 --memory-mib 6144
 --through final
~~~

If the recipe is absent, the runner reconstructs it from the six small
paid inputs and verifies the exact 709918-byte payload SHA and original
binding. No NF or GB elimination is rerun.

## 6. Resource and continuation contract

Use one shared 1800-second attempt and 6 GiB address-space limit, with
same-binding continuation on exit 75. The unchanged native code accepts
all these widths. The largest p7 output cell array has
$4367\cdot197\cdot25$ entries; one eight-byte copy is 172059800 bytes.
The source rows, accumulated product, original transport, field
matrices and Python objects add to this. The 6 GiB allowance is a
conservative execution budget, not a measured peak claim for the new
full-width calculation.

The previous two-probe run took 219.28 seconds with much narrower
right-hand sides. That time is not used as a claim that full210 will
finish in a single attempt. Every native stage and complete field
solve saves its own exact checkpoint. A retry uses the same driver,
inputs, output directory and mathematical binding. Paths, wall-clock
budgets and requested stopping phase do not alter that binding.

Exit 0 means a verified requested prefix or the completed full result;
exit 75 means a resumable resource checkpoint; exit 1 means an input,
source, arithmetic or verification failure. The independent job uses
'--through final'. It may continue a bounded exit 75 without restarting
verified stages. It must not repeatedly continue a verification failure.

All arrays, original source files and detailed continuation data remain
temporary. The compact final JSON is printed to the completed job log.
The repository may record source, parameters, run identity and output
SHA; no new mathematical calculation-output JSON, matrix archive,
certificate archive or Release asset is created in the repository.

## 7. Verification status at freeze

The new driver was independently compared with the original full
second-page source construction and the successful two-probe driver.
Its syntax was checked with Python's AST parser in an isolated temporary
directory. The changed driver has not executed mathematics.
All unchanged native helpers were already compiled and used in the
successful p7 job. The complete full-width calculation and every
asserted numerical gate remain the responsibility of the new actual run.
