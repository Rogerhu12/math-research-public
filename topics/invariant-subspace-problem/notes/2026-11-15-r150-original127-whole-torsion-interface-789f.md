# Whole original F127 torsion with every free polynomial tail

Author: Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.  
Date: 2026-11-16. Status: frozen executable entry; no computation claimed yet.

## 1. Complete original parent

This entry consumes only the successfully completed graded-module basis
of all6188 original sources. Its3333 constant prebasis directions were
eliminated by actual127 unit operations. Every remaining2855 original row,
including zero normal forms and the two restored nonzero sources6046 and6063,
was passed to the complete new module computation.

The wrapper binds the actual new basis, its original source DAG and metadata.
All basis ranks, leading degrees and free components are measured.
It does not input the old716 leading-degree sum,820 state dimension or315
torsion length. The generic rank of the complete original matrix is3333
plus the actual module-basis rank.

Let $k=\mathbf F_{127}$ and let $M$ be the complete quotient over $k[s]$
after the3333 original unit directions. The graded basis has distinct
leading components. Its monic rows have leading degrees $d_c$ in the pivot
components. The other components are genuinely free in the standard
monomial dictionary. The original source DAG is retained throughout.

## 2. Why a finite window contains the entire torsion

Put $B=\max_c d_c$, taking $B=0$ when there are no positive leading degrees.
Let $V_B$ be the $k$-span of all standard monomials of parameter degree
strictly less than $B$. Its full dimension is

$$
n=\sum_{\text{pivot }c}d_c+B\,r_{\mathrm{free}}.
$$

In particular, the sum of the leading degrees alone is not the torsion length.

Every standard monomial in a pivot component has degree less than its pivot
degree, hence less than or equal to $B-1$. A standard form outside $V_B$
therefore has a nonzero free-component term of degree at least $B$.
Take its highest such degree. Multiplication by any nonzero scalar
polynomial preserves that highest free-component vector, shifted by the
degree of the polynomial. Terms from pivot components began below $B$;
their standard reductions do not increase the graded degree and cannot
cancel this higher term. Lower free terms cannot cancel it either.
Such an element is not torsion.

Thus every torsion element lies in $V_B$. If $B=0$, the window is zero and
the entire quotient is free: the algorithm explicitly permits $n=0$,
returns zero torsion and still retains all nine full target standard forms.

## 3. Actual state action and all leakage

For every original standard monomial of $V_B$, the native program multiplies
by $s$ and computes its complete standard form through the actual new basis.
Every subtraction is recorded as a constant times a nonnegative power of
$s$ times a numbered basis row. The basis row itself is linked to the
original6188-source DAG.

The result has the unique decomposition

$$
s v=A v+s^B C v.
$$

Here $A:V_B\to V_B$, and every component of $C$ is one of the actual free
components. The native program checks that no omitted higher-degree or
divisible monomial remains. It retains every free leakage coordinate.
There is no projection that silently discards the free directions.

The true torsion space is exactly

$$
T=\bigcap_{j\ge0}\ker(CA^j).
$$

Indeed, a torsion element and all of its $s$-multiples must remain in $V_B$
by the preceding argument, so all its leakage vanishes. Conversely, for a
vector in this intersection, all actual $s$-powers equal their finite state
powers. They span a finite-dimensional space, and a nonzero scalar
polynomial annihilates the vector.

## 4. Finite stopping certificate

The program constructs the full rows of

$$
C,\ CA,\ CA^2,\ldots
$$

by exact127 matrix multiplication. It inserts every row into one actual
echelon basis. It stops only when an entire new block is reduced to zero
against the saved earlier row span. Thus the assertion of stability is
an actual row-reduction certificate for the full $CA^k$ block, not a
plateau inferred from a selected subset.

Once a complete block lies in the preceding span, the accumulated span is
right-invariant under $A$, and no later block enlarges it. The ambient
dimension gives the finite stopping bound. The receipt records the complete
rank history and stopping power; the exact selected observation rows and
full echelon rows remain in the temporary certificate.

Let $K$ be the full kernel of this stable observation matrix. The program
constructs its normalized free-coordinate basis and checks

$$
C K=0,\qquad A K=K J,
$$

as well as every stored observation-row product with $K$ and the complete
free-coordinate identity. It checks all coordinates of these products.
Consequently the action $J$ is the action of $s$ on the entire original
torsion module, whose dimension is

$$
\dim_k T=n-\operatorname{rank}\mathcal O.
$$

The finite affine characteristic polynomial is $\det(sI-J)$, the product
of all invariant factors of the original torsion module. It is not merely
a common annihilator of the nine targets, nor the largest invariant factor.

## 5. The nine targets retain their full standard forms

Each of the nine original targets is reduced completely, with its original
source operations. The entire packed polynomial standard form is retained
in its own temporary file, including every free term of degree at least $B$.

A target outside $V_B$ is explicitly marked as such. A bounded target is
tested against the complete $K$ basis. A negative target test does not abort
or alter the computation of the whole torsion space. The small receipt
distinguishes boundedness from membership in that space.

## 6. Checkpoints and the one unsegmented construction

Two alternating state files retain the complete state matrices, completed
state columns, normalized targets, current observation block, exact
observation-row prefix and next-block multiplication-row prefix. They also
retain all echelon rows, selection indices and source-operation offsets.
The inactive slot is completed before the selector changes.

After observation stability, construction of the complete kernel and action
candidate is one unsegmented block. Its preceding stable checkpoint remains
valid if the process stops before the entire candidate has been saved.
That event does not claim a partly constructed candidate. Once the complete
candidate is saved, the program resumes verification by whole kernel columns
and target tests without repeating the completed state or observation work.

All completed candidate and verification states are bound to the original
basis and both source hashes. A finalized native result is reused before
the characteristic-polynomial worker is considered. If that small worker
times out, the complete original torsion state remains available and is not
computed again.

## 7. Budget and characteristic worker

The requested native budget is60 seconds, compilation30 seconds and the
characteristic worker30 seconds, with outer150 seconds and2048MiB.
The finite-window allocation is capped at8192 coordinates. Each byte
accumulation is bounded by $8192\cdot126^2<2^{32}$.
Failure of this resource gate is not a mathematical negative conclusion.

The characteristic worker is a separately bounded process. It first checks
the entire state-file hash and reads the exact action block. It uses the
public python-flint0.9.0-compatible methods
`nmod_mat(...,127).charpoly()` and `nmod_poly.factor()`, verifies the monic
degree and the full factor product, and records the actual installed
python-flint version. Its expanded action allocation is capped at2048
torsion coordinates; the native whole-state result survives any later gate.

The primary API reference is
[python-flint nmod_mat](https://python-flint.readthedocs.io/en/latest/nmod_mat.html).
No system FLINT development headers are required by these native programs.

## 8. Frozen entry and conclusion boundary

Pins and the complete argv array are in

~~~text
notes/2026-11-15-r150-original127-whole-torsion-inputs-789f.json
~~~

The native is ad6306ec33870f4c5325d8894d68a757b8215442,
SHA256 d92bcb7395f4d81c89b6a5d291951a6d7bf920862ea68c6bb6b3fe454e485528.

The wrapper is2e7390ed3cb7ce63f854ce707509c7c4e5e825d1,
SHA256 3bf32f1f48ebb8b1944562ee7186ff17748725d9023dd68c37d4dd3207234fe1.

~~~text
python {scripts}/2026-11-15-r150-original127-whole-torsion-runner-789f.py
  --gb-out {work}/original127-complete-graded-module
  --sources-root {scripts}
  --out {work}/original127-whole-torsion
  --seconds 60 --memory-mib 2048
  --compile-seconds 30 --characteristic-seconds 30
~~~

Success is an exact complete-field127 affine computation with original
sources and all free directions retained. The separate original infinity
qualification and generic-rank comparison are still required before using
the affine result for a characteristic-zero degree bound. This source does
not assume that qualification, infer global target membership, or close any
remaining root2 arithmetic page.

Only code, parameters and small actual receipts with hashes are permanent.
The basis, original DAG, full target forms, state, action and checkpoints
remain temporary. No local compilation or mathematical execution has been
claimed; the Actions invocation performs the first actual run.
