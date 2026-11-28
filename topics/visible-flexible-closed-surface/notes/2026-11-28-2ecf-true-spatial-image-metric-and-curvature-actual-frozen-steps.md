# 真强比例空间像的全指标及实际后映射目标优化

**数值证据。**

取前条冻结11半径、961球向位置的原物理图。将 R286 的两种变换逐点作用于实际 Cartesian 六 jets 并直接用相同 g 重算 G10/G11。平面/高度全 guides 场 G11 metric / κ / held 为 0.9730758002 / 1554.628119 / 0.6636642718；真实三维排球场为 0.5799639222 / 33.08943432 / 0.6647804377。前者原全部七几何行的最大违反均为零，代价是局部出现约 1555 的曲率。后者具真宽度及真实两球/d<1.6 证书，原高度 guide 单独观察。
随后在第二种真图中重新优化，原 g 及 11 个设计半径严格冻结。物理源选 24 径向 span、12 个偶角频率、575 个球向位置系数。对真实复合图的全六 jets 与原 point/area 全部行求导，包含空间映射至三阶以及三维闭合乘子的隐导。超额设计源的真正方向差分误差 6.052910164974616e-10。本输入自身 280 次 L-BFGS 接受，独立 G11 0.4578543861 / 18.09530296 / 0.6627342422。存档 NPZ 定义空间变换前的 Fourier–Hermite 场；成品位置必须逐点使用同一 SHA 的 R286 真三维球映射。变换后不能借变换前的 E=1。

## 可移植重生

W 含冻结11半径原始场及状态、R273 ridge 底、真实 G10/G11 及两个 master。S 为课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-material-global-spatial-guard-image.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-implicit-frozen11.json --field polar-gap092-material-implicit-frozen11.npz --eps .035 --output polar-material-spatialguard-frozen11.json
python3 -u "$S/2ecf-polar-material-spatial-guard-true-spheres.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-implicit-frozen11.json --field polar-gap092-material-implicit-frozen11.npz --eps .05 --output polar-material-spatial-spheres-frozen11.json
python3 -u "$S/2ecf-polar-unit-material-optimize-real-spatial-image.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --seed-field polar-gap092-raised-ridge-rays.npz --start polar-gap092-material-implicit-frozen11.json --frozen polar-gap092-material-implicit-radius11.json --iterations 280 --eps .05 --field polar-gap092-material-optimized-sphere-image.npz --output polar-gap092-material-optimized-sphere-image.json
python3 -u "$S/2ecf-polar-unit-material-optimize-real-spatial-image.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --design polar-gap092-material-optimized-sphere-image.json --field polar-gap092-material-optimized-sphere-image.npz --eps .05 --output polar-gap092-material-optimized-sphere-image-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-unit-material-optimize-real-spatial-image.py | 45deb390282d4dfbaab923e5c9fcc1972772eb47820da01926c65c89e2b7a6df |
| polar-material-spatialguard-frozen11.json | fbad63b5e989e64499ff368207f29d7c2b4b13ec2ec78dc5fdd946f28ea7d427 |
| polar-material-spatial-spheres-frozen11.json | 9070ba89b1c3b989d69bea02ee72bbdae40b41eedced92ef47aabace791c37b1 |
| polar-gap092-material-optimized-sphere-image.json | eb92b6077373a77260efe043fcde8813d537ac4deed487b2582e57f26a63f4e9 |
| polar-gap092-material-optimized-sphere-image.npz | 351856864d1f3c0a7476d989a7527f8883007b53f6d0df84cc0322372cb39194 |
| polar-gap092-material-optimized-sphere-image-full.json | f05ca36d6d0d5a243a72c303e786d510e381076946572507f283e9d9d545bc70 |
| polar-material-spatialguard-frozen11-exit.json | dfc8d53b3e4d1249d62062a99aca1be018233d343a7683610f8ad58ed48d1cd3 |
| polar-material-spatialguard-frozen11.log | 4fe21fb68efefea3bc37ff2de484eb8e831b977b6d957de7a2f276652fa5cb02 |
| polar-material-spatial-spheres-frozen11-exit.json | 50e2f3eebbb40ce793a850effeba15f574c15def65624134064425cfe27e30c8 |
| polar-material-spatial-spheres-frozen11.log | fb95521bb963ec2dfc84a0d6dc233bc7b5337b25967ad3485794ed6ff496aec6 |
| polar-gap092-material-optimized-sphere-image-exit.json | 69e78b9d3ecc36aad1be69b279621e7d2aa242d9d7ee64576f5ff754ae5537a3 |
| polar-gap092-material-optimized-sphere-image.log | 143b76fb5b90d3537ed34d41df71c0fae09d43c1d7e411831a90e0f1beff24de |
| polar-gap092-material-optimized-sphere-image-full-exit.json | 79cc30eb46efbd28a8830d7525c0da21c2d133dd9aabd886bbbd8c422ad6bbe9 |
| polar-gap092-material-optimized-sphere-image-full.log | 67b2032f5c282a5d95b92337becb6eb598fe74d8e57e8bdbf4c12da9042c06fe |
