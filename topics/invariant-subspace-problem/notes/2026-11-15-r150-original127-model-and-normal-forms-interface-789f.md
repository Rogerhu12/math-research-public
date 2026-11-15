# Independent F127 original model and complete normal forms

Author: Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.  
Date: 2026-11-15. Status: corrected complete6188 entry; new native not yet compiled or run.

## 1. Exact original input and limited conclusion

This entry creates the fixed-prime127 model from the complete primitive
integer seventeen equations. It checks all4433 coefficients against the
paid original31 model before any reduction modulo127. The old model supplies
only the original source dictionary. In that dictionary

$$
\mathrm{rawSource}=17\,\mathrm{multiplierIndex}
 +\mathrm{equationIndex}+1.
$$

The first actual model run stopped at its complete-source assertion: the old
input lists3333 proposed prebasis sources and2195 other sources, only5528.
Its failed receipt is preserved; the native NF never started. This correction
does not reinterpret that incomplete dictionary as the full original source.

The generator now enumerates all364 multiplier monomials and all17 equations,
then takes the exact complement of the3333 original prebasis IDs. There are
2855 remaining sources. The old2195 are checked distinct and disjoint from
the prebasis and included as a strict subset; the other660 labels are restored
directly from the original dictionary. No claim about their127 normal forms
is assumed. Four17-by4 equation/multiplier-degree histograms distinguish the
prebasis, old subset, restored660, and complete complement. The native
independently checks all6188 original labels again.
All normalization constants must be127 units. A failed unit check is a
failed qualification of this fixed-prime entry, not a characteristic-zero
nonmembership result.

No old31 numerical prebasis operation, normal-form coefficient, module basis
or torsion state is transported to127. The exact primitive coefficients are
reduced again. Success of this stage proves only a complete original127
normal-form presentation with replayable sources. The full affine torsion
and independent infinity qualification remain later stages.

## 2. Independent seven-plane arithmetic

The field arithmetic is specific to127. Its nonzero scalars are partitioned
as

$$
c\,2^r(-1)^\epsilon,\qquad
c\in\{1,3,5,7,9,11,13,19,21\},\qquad
0\le r<7,\ 0\le\epsilon<2.
$$

The constructor checks all126 scalars, uniqueness and inverses. Addition
uses seven bit planes and end-around carry modulo $2^7-1$, including
normalization of the all-one representation of zero. Nine cached multiples
belong to the current127 row.

Before matrix work, the native program compares packed arithmetic with
independent scalar modular arithmetic over every field value, all rotations
and both signs. It exercises distinct source/destination strides, word
offsets and untouched guard words, and checks all scalar multiplications and
cached multiples. This is a new necessary arithmetic check, not a replay of
the31 tests.

## 3. Original constant block and all polynomial tails

The native program groups the proposed original3333 $N$ sources by multiplier
degree and performs actual127 constant-head elimination. It permits different
pivot positions from31. It rejects any failure of independence rather than
silently dropping a proposed source. Every forward normalization and
elimination, and every same-degree backward operation, records its original
source index and field coefficient.

Only the constant leading block is row-reduced at this stage. The complete
parameter-dependent lower-moment-degree tails accompany the same operations.
The script checks every same-degree pivot-block entry and requires3333
distinct actual unit pivots.

It then reduces all2855 remaining original rows and all nine saved original
targets through these bases, carrying each lower-degree tail. Every reduced
pivot coordinate is checked zero. The new1034-component dictionary is stored
in original moment monomials. Parameter degree remains at most45 by the paid
univariate degree bound and is also checked in the actual output.

## 4. Continuation and original sources

The complete constant prebasis, its original forward/backward DAG and the
new component dictionary are retained only inside the current job. The
native program saves a completed-row checkpoint after each original source
and target. The checkpoint includes exact committed byte offsets of the
normal-form data, source-reduction DAG and readable polynomial output.

A resumed run verifies the immutable binding. The wrapper hashes every
retained file against the prior actual receipt. Native recovery truncates
only the uncommitted appended tail of its own temporary output to the saved
offsets, restores the complete constant basis, and starts at the next
original row. A fully completed stage is reused without arithmetic.
Time and memory limits are excluded from the mathematical binding.

The constant basis is checkpointed after its entire construction; this
version does not claim a resumable partially completed backward constant
elimination. A hard stop before that first checkpoint has no completed
prebasis conclusion.

All2855 rows must finish before the GB stage may consume the presentation.
An exit75 prefix proves only the explicitly committed row prefix. At complete
exit the wrapper reads every2855-source and9-target binary record against
the exact dictionary, including polynomial bounds and field representatives.
It reports how many of the newly restored660 rows actually have zero or
nonzero normal form. Every record, including zero rows, goes to the later
GB consumer; no old-field zero source is silently omitted.

## 5. Memory and budget

This route does not load the old T96 graph. For a complete1021-row module
basis, the later GB cache upper bound is

$$
1021\cdot46\cdot\lceil1034/32\rceil\cdot7\cdot4\cdot9
 =390569256\ \text{bytes}.
$$

The more conservative constant-prebasis cache bound is
$3333\cdot446\cdot7\cdot4\cdot9=374602536$ bytes.
Only one current original row is processed at a time; source DAG files are
streamed to temporary disk. These bounds leave room within a2GiB process.
The later torsion stage must derive its actual degree profile and state
dimension instead of assuming the old716/820/315 values, and will gate its
allocation before construction.

The initial request is model outer60s, nativeNF180s, compilation30s, outer240s,
memory2048MiB. The later proposed stages are GB900s and torsion60s, each
using the newly completed127 data; those source pins are separate.

## 6. Exact frozen files and invocation

The complete source/input pins and CLI are in

~~~text
notes/2026-11-15-r150-original127-model-and-normal-forms-inputs-789f.json
~~~

The model source is d563d45f7060297a576a25a41ba30ec620202a0d,
SHA256 a0eec7261177a8806e6761e3bee98d6740e5cbf1d225a9da107c27c47a82d349.

The native normal-form source is03cfbf6882fd19aed3e32b6883654691dd0ff63f,
SHA256 46ef43c439aadb77a7458c97a0bce120846e6aa57d79bc9aed78d211242f81f8.

The arithmetic header is796c0d4c790b3f2294bc203f057e78c0fb16d4ed,
SHA256 03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3.

The runner ise9bdb251ad30a96b1ea12efe46f6d416ae8b8bdb,
SHA256 050ef5d714726e1e5f19be46f96a690188db809357ffbd40b2371558bd12f46a.

Restore the pinned primitive gzip using the existing small historical-input
script. The existing global197 raw model supplies the paid prebasis and a checked subset; the generator itself creates all6188 original labels.
Run the model generator, then:

~~~text
python {scripts}/2026-11-15-r150-original127-normal-form-runner-789f.py
  --model-out {work}/original127-model-all6188
  --sources-root {scripts}
  --out {work}/original127-normal-forms-all6188
  --seconds 180 --memory-mib 2048 --compile-seconds 30
~~~

The full argv arrays in the manifest are executable without relying on shell
line continuation. A repeated bounded run uses exactly the same output path.

No local compiler or AST check has run: the local execution process is
unavailable. Actions must perform the first actual parse, compile, arithmetic
tests and matrix computation. Only source, parameters and small receipts are
permanent; the binary input, basis, DAG and recovery data are temporary.
