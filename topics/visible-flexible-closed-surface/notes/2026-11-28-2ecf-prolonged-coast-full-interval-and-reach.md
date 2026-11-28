# 准确 Γ95 延长 coast 与全前缀法球的计算记录

**已证明的计算包含。**

R263 对整个 0≤σ≤.24 与完整角域作准确仿射母线包含；对 .07 与 .08 两种长度作整个中央+两半 ramp+coast 的双侧点对证明。后者各自作为有边界闭集的 reach 至少 1/9.867915 和 .099。全域整数程序对每个长度验整段而不是只验端点，另在末圈取 z 的有向下界。法球推导见正式 R263。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径。W 内的 ramp/coast master 由 R232/R233 原命令生成。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-prolonged-affine-coast-certificate.py" --scripts "$S" --ramp gap105-prefix-ramp-master.npz --coast gap105-prefix-coast-master.npz --cells 2048 --lengths .06 .07 .08 .09 .10 .12 .15 .18 .24 --output polar-prolonged-affine-coast-cert.json
python3 -u "$S/2ecf-polar-prolonged-coast-secant-budget.py" --ramp gap105-prefix-ramp-master.npz --interval polar-prolonged-affine-coast-cert.json --rows-sha 4807513a6212ba0dfb7e50622e04ca2ff5cd38cf7c6aab9205b0a1474a7149e4 --output polar-prolonged-coast-secant.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-prolonged-affine-coast-certificate.py | bfe10d2c2bd77577db8ec5c868ffd908de9ff238f4661407f8297d197e833e37 |
| 2ecf-polar-prolonged-coast-secant-budget.py | cb0201d389ae7fd45c61f2e799c2e09502e14b760317d24cea5d6bc3d9c406fb |
| polar-prolonged-affine-coast-cert.json | 415752a80b276af30dcb129afc805c116e2566babfd599390e956311c2d2d893 |
| polar-prolonged-coast-secant.json | e65ef4b41ac99e145b55e66230c7a4a47c9004f275153602e74f788d95eb4dc7 |
| polar-prolonged-affine-coast-cert-exit.json | 782a1bf7c75e8d997707b33932c19f422615cab72474314a84a9993a4b210fdd |
| polar-prolonged-affine-coast-cert.log | 3238430d278fbdea24125d624bb2cebf5678e3df8a51cbfdd1e12829ba04aede |
| polar-prolonged-coast-secant-exit.json | dbc886b447372d2dc36bc3f5b6eb0954be6bde0acb580828af347269a94a12a6 |
| polar-prolonged-coast-secant.log | 8a2ad14668fdcd4693ce9875192ff7d767f5b8dcefb5e0963ffe28ea80fe2535 |
