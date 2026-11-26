# R144 continuation contract: preserve 6,791 completed cells and finish the suffix

2026-11-26. This is a repair and continuation of the one unfinished
forward mean-retraction target. It is not another copy of a completed
target, and it does not change the raw centre, nu0, original affine
parameter interval or the mean retraction being enclosed.

## Actual failed execution and complete saved prefix

Public run 45770488571/1 ran the original scientific source with
SHA256 cdac407570960062945c6d846d7a14d04bcbb50945b03e5fd4ef3c745f82538f.
It completed 6,791 of the required 7,721 rows, then returned one at
the finite-scalar check for the mean-shift lower record on the next
row. Its complete saved scientific output has 4,806 bytes and
SHA256 478a807d1caf93fd441949eca6565c1188b34ab44ba007c37b2221ffbe21782f.
The execution receipt has 11,625 bytes and SHA256
773e2e5eb43017e77a0a7460a697ebad30e55172a4f88c5cd01600cf3a326f1d.

The successful prefix ends at the exact radius
5731986528263291/4503599627370496. The complete D, forward multiplier
G, signed bulk term B, propagated interface term A, original D(0),
whole-prefix Y lower and whole-prefix v-change upper were saved.
They are full decimal balls, not rounded display values.

The new source requires those exact public bytes and the actual
failed execution. It restores every saved ball with outward bounds,
intersects D with G*D(0)+B+A, and advances only original row indices
6791 through 7720. No successful prefix row or old producer is rerun.

## The denominator repair and diagnostic

For positive n and Y the mean difference is
$$
 m_{\rm flat}-m
 =(-mD)\,\frac1{\sqrt Y(\sqrt n+\sqrt Y)}.
$$
A centered-ball product of two wide positive factors can contain
zero even though its mathematical factors are positive. Directly
inverting that product can produce an indeterminate Arb result.
The original source used that direct product. The continuation
evaluates the original expression once on the first unfinished row
to record whether the denominator contains zero and whether the
old quotient is finite. This diagnostic is on a failed, uncompleted
row, and is not a recomputation of the successful prefix.

The actual new reciprocal enclosure uses monotonicity. With complete
positive endpoint enclosures nL<=n<=nU and YL<=Y<=YU,
$$
 \frac1{\sqrt{YU}(\sqrt{nU}+\sqrt{YU})}
 \ \le\
 \frac1{\sqrt Y(\sqrt n+\sqrt Y)}
 \ \le\
 \frac1{\sqrt{YL}(\sqrt{nL}+\sqrt{YL})}.
$$
Every square root and denominator is rounded in the direction needed
for its endpoint bound. In particular the upper reciprocal uses an
explicit strictly positive lower-denominator endpoint. No wide
positive centered-ball denominator is inverted.

The complete signed mean difference multiplies this reciprocal
enclosure by -mD. The C0 upper uses only the reciprocal upper endpoint
times |D| and the whole raw v upper. This avoids the same defect in
both the signed mean witness and the C0 comparison.

The linear D propagation, its signed forcing, full parameter interval
and all mean-interface fees remain the same. Positivity uncertainty
does not stop the linear flow. An unresolved Y produces an unknown
physical gate unless an actual directed failure witness is proved.

## Prefix interface-count reconciliation

The old output reports 5,731 interfaces. The original code incremented
that counter immediately after applying a row's possible mean jump,
before writing the row's new scalar state. The failed row may therefore
have incremented the counter while the saved D/G/B/A state still
belongs to the preceding completed endpoint.

The continuation obtains the number of completed prefix interfaces
from the immutable native keys strictly less than 6791. It verifies
that the old reported count differs by either zero or the possible
single interface at row 6791. That uncompleted partial-row increment,
if present, is recorded and is not consumed as completed work.
The interface at 6791 is then applied exactly once to the saved
left-endpoint state. The preceding a, m and candidate-piece identity
are read from native row 6790, without advancing that row.

The complete final interface count must still be 6,143.

## Honest gate history and full-domain conclusions

The old successful-prefix Y lower is strictly positive. Reading that
complete lower outward proves that every original prefix cell has
positive Y. Consequently its saved maximum v-change upper covers
the entire prefix and can be carried into the final global maximum.
A large upper is never treated as a lower bound or as an actual
violation.

The original partial output did not save the old first-violation
history. Absence of a witness field is not evidence that no earlier
violation occurred. The continuation explicitly marks that history
unavailable. A final false C0 gate requires a newly saved directed
witness from the unfinished suffix. A final true gate still requires
the complete prefix-plus-suffix positive Y lower and complete global
v-change upper. Otherwise the gate remains unknown.

All whole signed scalar enclosures are written to the actual output
file and parsed back before the final gates. The same true/false/
unknown semantics of the original contract apply.

## Trace and publication identity

The old private trace metadata is retained exactly:
6,791 records, 19,064,094 bytes,
SHA256 361ed5fcedde835356c885aea5951e63818e90a271b9fc2d3616f9fa7be6c763.
Its numerical row contents are not regenerated or published.

The new 930-row suffix trace stays private temporary data. The output
contains two trace metadata records and a hash of their canonical
metadata. It explicitly does not claim that two separate trace hashes
determine the SHA256 of concatenated trace contents. Whole record and
byte counts are sums of the two actual segments.

The continuation has a separate consumed marker and workflow so that
the original failed attempt and all its public bytes remain unchanged.
There is one explicit continuation child, no automatic science retry,
no artifacts, Releases or new published arrays. The existing actual
pull/README checks, AST-before-science rule, topic capacity accounting
and non-fast-forward push loop are retained. A successful whole
unknown is a completed numerical outcome for the original target,
not an assertion about geometric existence, an inverse or completion
of the research topic.
