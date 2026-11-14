# Current ac1 fold/Airy: actual restored native run

2026-11-14, phase_inverse. **Executed, exit 0, 27 gates passed.**

The earlier successful current-centre fold/Airy native file was lost with
the transient runtime and had not been pushed. This run uses the unchanged
published source and the two recovered small native inputs. It writes a
new report and does not overwrite or fabricate the unavailable old bytes.

From `topics/visible-flex-exact-nearby` the actual command was

```sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python3 scripts/fourfold_codazzi_current_moving_fold_Airy.py --out notes/2026-11-14-R133-current-moving-fold-Airy-restored-native.json.gz
```

Python 3.12.14 and python-flint 0.9.0 were used, with the source's 320-bit
Arb precision. The run returned normally. It reports 27 gates, no failed
gate, `complete=true`, `proved=true`, and no failure.

| File | SHA256 |
|---|---|
| `scripts/fourfold_codazzi_current_moving_fold_Airy.py` | `1bd118841981689d6e947fe4234e62d4ecca2a942b008746d469c4fe495a6a0b` |
| `notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz` | `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864` |
| `notes/2026-11-13-R133-universal-two-port-Airy-v2-native.json.gz` | `1e5b5436f35c46e1c760c7385754867db6a28e7bd89d1a66700a069908608921` |
| `notes/2026-11-14-R133-current-moving-fold-Airy-restored-native.json.gz` | `0eaef7a19a6d0b0ed49ee759321062eedd734057f46e7ef18deefe7893b647c4` |

The output is 14,325 bytes. It preserves its source/dependency hashes,
upstream input hashes, whole original affine parameter interval, original
object SHA and current candidate SHA
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.

The scales are unchanged: blown-up radius $1/512$, fold radius $2^{-26}$,
canonical complex radius $2^{-34}$, real Airy half-width $2^{-36}$ and
fixed physical radial offset $2^{-37}$; the actual physical angular strip
is $1/8192$. Outward readable consequences of the new balls are

$$
 J_{\min}>1.1804352935,\qquad
 \operatorname{Lip}(\text{true inverse})<.03336772183,
$$
$$
 \text{balanced feedback}<.028684968258,
$$
$$
 \text{physical fixed-r H1 to complete Airy port}<32.817995814,
 \qquad
 \text{canonical H1 to physical fixed-r L2}<4.528366133.
$$

The mathematical scope is exactly the published
`results/R133-supplement-current-moving-body-complete-Airy-collar.md`:
the actual two-dimensional fold, ordinary physical H1 source including
its radial derivative, both full Airy port columns, all modes and both
original mean states. The physical fixed circle is
$r=r_*(\eta)-2^{-37}$ and is its actual nonconstant canonical graph.
No inverse-curvature conversion was added. No outer PPoly seam,
positive regular graph or whole-body feedback inverse is certified by
this recovered local report.

The separate current-centre consumer
`scripts/fourfold_codazzi_current_moving_root_piece_ports.py` still
requires the complete exact ac1 candidate and the actual root/target
inputs. The centre is being reconstructed through the already recorded
six-step chain; until it is supplied, this note does not mark that
common-root-piece run complete.
