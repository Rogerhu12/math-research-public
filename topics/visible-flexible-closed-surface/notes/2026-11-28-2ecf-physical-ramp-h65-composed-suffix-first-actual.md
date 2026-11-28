# 固定同一度量的新 H33/H65 源与真实 5292 后缀

**数值证据。**

原 5292 第 9 态 suffix 系数固定抄入两个新物理源。分别以真实全目标观察建立独立 own0，两条新链不继承旧 9 次接受。H33 在此仅为 baseline；H65 对自己的 4291840 行做一次完成的原物理正规步及自己的独立 G11。所有原 13 行、面积、几何和曲率 guides 全数保留。修改只在整个位置修正恒为零的 ramp 内，未改变沿 b..S 的任一原空间函数；原缓存的审计只作父来源，H65 对实际 J、JT 及完整法方程另有检查。

| 源及自身接受 | G10 R14² | G10 metric / κ / held | G11 metric / κ / held |
|---|---:|---|---|
| H33 own0 | 0.06814645201212 | 0.25357882768 / 20.996640574 / 0.70624240288 | 0.25439324792 / 21.127509036 / 0.70637567537 |
| H65 own0 | 0.06814645201258 | 0.25357882768 / 20.996640574 / 0.70624240288 | 0.25439324792 / 21.127509036 / 0.70637567537 |
| H65 own1 | 0.06773158997712 | 0.25347342131 / 21.025976773 / 0.70583945497 | 0.25429571527 / 21.156407069 / 0.7059725611 |

H65 实际全导数误差 [{'epsilon': 1e-06, 'relativeL2': 5.084745636676459e-10}]，adjoint 9.992007221626409e-16，完整物理 normal 相对残差 1.3856164980748249e-14。H65 第一步实际步长 0.25，外部总 driver 自然 0，166.219707 s、450808 KiB。独立最坏 metric 仍在后部 s=.2043122962。准确新前缀能进一步压低固定段误差，但未将后缀的约 .25 峰消去。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raw-ramp-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H33-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --warm-state polar-fixed-prefix-original16-step09-step01-state.json --initial-damping 0.0035555555555555553 --prefix polar-physical-H33-coarse9 --steps 0
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H33-prepared.json --observer polar-physical-H33-independent.json --state polar-physical-H33-coarse9-initial.json --output polar-physical-H33-coarse9-baseline-G11.json
python3 -u "$S/2ecf-polar-raw-ramp-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --warm-state polar-fixed-prefix-original16-step09-step01-state.json --initial-damping 0.0035555555555555553 --prefix polar-physical-H65-coarse9 --steps 1
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-physical-H65-coarse9-initial.json --output polar-physical-H65-coarse9-baseline-G11.json
python3 -u "$S/2ecf-polar-raw-ramp-suffix-observe.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raw-ramp-source-compose.py" --prepared polar-physical-H65-prepared.json --observer polar-physical-H65-independent.json --state polar-physical-H65-coarse9-step01-state.json --output polar-physical-H65-coarse9-step01-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-raw-ramp-suffix-solve.py | d894b12fe449b452d759511fe61fb37569e0b21864c3568ec31cc9df68267890 |
| 2ecf-polar-raw-ramp-suffix-observe.py | 6a5466a54587153ba07feb42e33feec7a959b589f6596ac045c97524773bdfea |
| polar-physical-H33-coarse9-initial.json | 76ab2d91884fe09a6f9f55e7d0672701b839b6e08e7c17f26632e70101ab9d3a |
| polar-physical-H33-coarse9-report.json | 84d8dc619514ed341a114a04871c6719e3939114e69d890e8af5c9b7b48a2d32 |
| polar-physical-H33-coarse9-baseline-G11.json | 0a3fb7eb6d3ae2e5fb745d2d6f293fb263637a8dee53b3c8b14c35def81a5924 |
| polar-physical-H65-coarse9-initial.json | 73c15007ad23ce7c04e71557d6d7f1483b02327a05be5d21a8aee554bcbbf5ce |
| polar-physical-H65-coarse9-report.json | f1ed6d3ad16ac63ff5b5633964dd279b5ce00a262354386b99a2b1510e0781b6 |
| polar-physical-H65-coarse9-baseline-G11.json | 8e7b7a37e3d9c53c9fdf14d9be05c6cba85e701f152e32b7057b43e567482903 |
| polar-physical-H65-coarse9-step01-state.json | bcff3588b43ee2d1271b3666008f15af2c1b9a088617177feb3433d69b3251dc |
| polar-physical-H65-coarse9-step01-G11.json | 403cdbd461d52506e5f9e109822b41f3044579cfd9bcd9baee20d015f34bef78 |
| polar-physical-H65-coarse9-actual-derivative-check.json | 382ebb55aa3d13eae61ce3fbbe40802595c2241fbb1a6698f6e2f9e42912c961 |
| polar-composed-H33-H65-driver-exit.json | 1d4ccffc6bcfa3b08c77d16a19ce9efcffa0d9d31bf424baa9f3a867bd0d52a2 |
| polar-physical-H33-coarse9-exit.json | 2e8bc4abfd49a2ad42504f7c67778e93ddfeeb497517e95505a9236c80e879bb |
| polar-physical-H33-coarse9.log | ed070bdac6347c1973fb16a222beda1ac5d79424cce9a849a86eb24dd245c74b |
| polar-physical-H33-coarse9-baseline-G11-exit.json | 0424a6211dc745c5ff531a9874dcc079516ee8957aff1d01cadba4b220ac952b |
| polar-physical-H33-coarse9-baseline-G11.log | 53a3ea7c95049e3429411219a4b618088e215a815d289f4b038853f7ec5b39b3 |
| polar-physical-H65-coarse9-exit.json | 0f5f2f8713f5d57d147383885ad7427bc1e1b0f437d481903bbfa07f19797af2 |
| polar-physical-H65-coarse9.log | 3ddea92b4f15c639f1aad6bc4e2b36583ad43fa76f6a3790d03404b2322719bb |
| polar-physical-H65-coarse9-baseline-G11-exit.json | 58a7648320c5f824dbffa8c42573e1793c4d3cb3ed8bec56e61131e33163c6e3 |
| polar-physical-H65-coarse9-baseline-G11.log | dbfef7ce47038b1193484516d5449bf1a18deced08107366034ea70bd42630c5 |
| polar-physical-H65-coarse9-step01-G11-exit.json | a74e2f15d4c3accc45fa2d0b0c5fd6c39bc742df551be05c7aa42f0c4aae1b31 |
| polar-physical-H65-coarse9-step01-G11.log | ac48e986543f7aa58f2c2d9fd386f56d5c4fc0ea3c28115bc7fd46a9986f9aec |
