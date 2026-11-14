# Exact scalar input budget for all 175 paid core leaves

**Proved and actually executed with BigInt rational arithmetic.** This is an
additive local-error budget, not a global transfer or DN certificate.

The nine complete native manifests from run 43307149760 contain all 174 exact
positive common scalar spans. Their accepted leaves form an exact adjacent
175-piece partition of [0,1/4], with one rejected outer box replaced by two
accepted children. All manifests have the same complete object, dependency,
source and parameter identity. In particular the actual real family is
delta5 plus [-1/1000000000,1/1000000000].

The helper parses the midpoint and decimal printing radius of each recorded
Arb upper string as exact integers divided by powers of ten. It adds that
printing radius before using the value. The 175 upper bounds are then added
as exact rational numbers; the displayed decimal is rounded upward by integer
ceiling. The actual result is

- Sum of local scaled transfer errors: less than
  0.000002294642251876562467.
- Maximum local scaled transfer error: less than
  0.000000036020340463550504.

The norm is the same physical Cauchy state (w,p/8) used by the native leaf
proofs. These numbers do not include amplification by intervening matrix
products. They must enter the ordered prefix-inverse formula in the complete
core composition note; they are not substituted for its final error.

The compact report binds each original manifest by SHA256 and keeps the exact
rational sum. It references the original leaf/error records instead of
duplicating regenerable data. No NPZ or binary matrix was accessed by the
integration-only calculation.

Reproduction from the topic directory:

    node scripts/fourfold_core_local_transfer_budget.cjs \
      data/core_uniform_flow_ci/43307149760 \
      notes/native_core_20261112/local_error_sum.json

The helper may include all original row identities in its fresh full output.
The checked-in compact summary omits only this duplicate list and records that
omission explicitly; its arithmetic values and input identities are unchanged.

Source SHA256:
1761c20dea16a51e640a298c374f5d6ddd732f34076e5252a5bca2d0dfcccbe4

Compact report SHA256:
41a6804e8e3956559581c356a1ff7bd30ef9b4001c01bbc523c7f89a66e5dd48

A separate scalar-product helper was written, but its input-loading attempt
was manually stopped before completion, and no scalar-product numeric
certificate resulted. The native matrix collector is still the next required
step for a useful full-core bound. The later correction that sigma is even
in r (though odd in theta) does not affect these 175 positive-half leaf
certificates or their exact sum.
