# q122 has a direct pointwise metric-error witness

The earlier value 2.07058e-6 was a finite angular Fourier l1 metric diagnostic. An l1 value above a target is not by itself a lower bound for the actual pointwise maximum. A fresh read of the same accepted physical quintic supplies the missing direct check.

At physical s = 0.9720813654259819 and the original angular chart value psi = 0, the actual material metric components, normalized by the fixed background metric g = diag(1,a(s)^2), are

- E = |F_s|^2 - 1 = 2.0705611216698117e-6;
- F = <F_s,F_theta>/a = 0;
- G = |F_theta|^2/a^2 - 1 = 2.609457960822681e-8.

Thus the relative metric operator norm of this sampled 2-by-2 error matrix is 2.0705611216698117e-6. Its ss component alone exceeds 1e-6. The original node witness at s = 0.9721471856177173 similarly gives 2.0688963147108552e-6 at psi = 0; its finite Fourier l1 value reproduces the previous 2.068924291591986e-6. This confirms a physical pointwise numerical gap, rather than merely a conservative l1 upper diagnostic.

The calculation loaded the unchanged primary package SHA006eaa15e9b1416aa72140e616e1ecf75461033df8448ade0bbd812826d210a8 and all three original physical quintic chunks. It used the same profile, material chart, exact quintic derivatives and the original 1360-angle complete mean. Four declared radial rows were evaluated at 1360 angular samples. It did not solve or modify any field, open a tail worker or assemble a Jacobian. Owned exit code was zero, wall time 6.042775479 s, and peak RSS 107436 KiB.

These are direct floating-point samples, not interval enclosures, full-surface upper bounds, or any new existence certificate. The intended next numerical operation remains same-g M32 refinement after the unique eight-control response and disk maintenance finish.
