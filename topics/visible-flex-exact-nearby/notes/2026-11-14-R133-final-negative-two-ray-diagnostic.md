# Actual final negative two-ray return: floating diagnostic

**Numerical evidence only, not a certificate.** The complete final centre
with index SHA256
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`
was used with all 32 moving modes, the exact recorded floating-rational
amplitude and compact parameter, and the complete quadratic 64-mode
drift. No angular mean replaced that drift.

On the negative half-body write $a=-\gamma m\sqrt{-K}>0$ and solve

$$
 (H_\pm)_r=-d\circ H_\pm\pm a,\qquad H_\pm(0,\xi)=\xi.
$$

The diagnostic return is
$F=H_-(r_*)^{-1}\circ H_+(r_*)$ as an increasing circle lift of period
$\pi/2$. The regularizing coordinate $r=r_*-x^2$ keeps the true root
endpoint in the integration. The target uses the existing floating
512-primitive evaluator, 4,097 radial interpolation nodes and 512 labels.
These numerical approximations have not been interval-certified.

The actual completed run gives:

| Diagnostic | Value |
| --- | ---: |
| Floating root | $.23839687429986117$ |
| Mean lift displacement | $.4318624877427462$ |
| Half the displacement range | $.0042976116115760465$ |
| Sampled individual ray Jacobian minimum | $.9666941259396387$ |
| Sampled individual ray Jacobian maximum | $1.0195410815276809$ |
| Orbit rotation estimates after 100,000 iterations | $.27492242944$, $.27492244848$, $.27492245969$ |

The last line is not a rigorous rotation-number interval. In particular,
no Diophantine property follows from its decimal digits. The return is
not the old object's frozen rotation; its full nonconstant part is
visible in this actual computation. The root finite part, first scalar
phase, genuine nonlinear branch dependence, and a full high-frequency
return inverse are not supplied.

The result helps distinguish the missing negative-return condition from
the now completed propagation and positive-cap Green bounds. It supports
continuing with the actual two-ray map and a genuinely paid phase/twist
argument, rather than reusing the old object's arithmetic constants.

Reproduction from the topic directory:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/fourfold_codazzi_final_negative_ray_diagnostic.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --out /a-new-path/negative-two-ray-diagnostic.json
```

The source refuses to overwrite an attempt. The accompanying JSON keeps
the complete sampled return lift, source and input identities, precise
ODE/grid settings and explicit uncertified scope. The run exited
normally after about 69 seconds. It is not counted as a mathematical
inverse result.
