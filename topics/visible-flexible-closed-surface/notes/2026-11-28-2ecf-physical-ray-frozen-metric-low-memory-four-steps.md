# 完整规定速率径线面上的低内存 5292 个真实位置步

**数值证据。**

输入是 R273 的低曲率正转全 65 射线面（A=.4,c=.56），固定其真实全帽度量、目标半径和所有几何参数。原有物理位置从全 Fourier–Hermite 场重算，新增后缀 5292 个 clamped Cartesian 自由度；新层从零开始。原完整正规带两次尝试在实际初值后均收到 SIGKILL，退出 −9，二者没有接受步。后续按每块八个实际径点流式直接求值 (J14 T)ᵀ(J14 T)，T 为全部同一物理 H² Sobolev 的带状逆因子。对每个新线性化执行 4 次阻尼正规方程 CG，所得方向按真实全 4291840 行目标回溯，均须通过 Armijo。这是有限 Krylov 内迭代的 Gauss–Newton；未将其称为原来的精确带状直接解。
本输入自己的首步另核全部 14 行的实际目标方向导数，以及每个实际内方向的 Hessian 二次型/jvp 平方一致性。新流程实际墙时 59.87743 秒、峰 296712 KiB、自然零。独立 observer 预先求一次全物理底，分别加入 4 个实际非零状态的直接角 Fourier 六 jets。

| 自身步 | G10 R² | G11 metric / κ / held |
|---:|---:|---|
| 1 | 1.56910685 | 0.50191968642 / 12.160290637 / 0.57317573047 |
| 2 | 0.4274065346 | 0.45879385403 / 11.689131636 / 0.57216694822 |
| 3 | 0.2395828633 | 0.36172066938 / 15.348544907 / 0.57346346938 |
| 4 | 0.1705018268 | 0.28257866283 / 16.178398641 / 0.5716836194 |

第 2 态独立曲率约11.68913，仍高于 1/.097，held 约 .57217。第 4 态独立 metric 约 .28258。下面用自然零的 --steps 0 命令重生原中断流程留下的初始字节，将其复制为原状态路径；二者 SHA256 均为 70d8fb7ca84ba50befbf800ab972275784f01612db7a8861639dc512bcfbff93。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raised-physical-ray-position-source.py" --mode prepare --scripts "$S" --parent polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --field polar-gap092-raised-rays-positive.npz --design polar-gap092-raised-rays-positive.json --observation polar-gap092-raised-rays-positive-full.json --output polar-gap092-physical-positive-prepared.json
python3 -u "$S/2ecf-polar-new-central-gap-suffix-solve.py" --scripts "$S" --prepare-entry "$S/2ecf-polar-raised-physical-ray-position-source.py" --prepared polar-gap092-physical-positive-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --zero --initial-damping .06 --steps 0 --prefix polar-gap092-physical-positive-zero
cp polar-gap092-physical-positive-zero-initial.json polar-gap092-physical-positive-xyz-own1-initial.json
python3 -u "$S/2ecf-polar-physical-ray-streamed-inner-gn.py" --scripts "$S" --prepared polar-gap092-physical-positive-prepared.json --state polar-gap092-physical-positive-xyz-own1-initial.json --steps 4 --iterations 4 --prefix polar-gap092-physical-positive-innerGN
python3 -u "$S/2ecf-polar-physical-ray-G11-states.py" --scripts "$S" --prepared polar-gap092-physical-positive-prepared.json --states polar-gap092-physical-positive-innerGN-step01-state.json polar-gap092-physical-positive-innerGN-step02-state.json polar-gap092-physical-positive-innerGN-step03-state.json polar-gap092-physical-positive-innerGN-step04-state.json --output polar-gap092-physical-positive-innerGN-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-raised-physical-ray-position-source.py | 19048cd5adf89aa94cd1476fc825b45a39bc2a767f804f2c34b186aa32ff217b |
| 2ecf-polar-physical-ray-streamed-inner-gn.py | 63a072fd3a27cd22a508f1e08e138010787c16cb5c844e40120de49f62703181 |
| 2ecf-polar-physical-ray-G11-states.py | 66f3d0c73aae6e95f4b502dc5ea36f8d71651b9e9c9eb32f2eba7017f10e28de |
| polar-gap092-physical-positive-prepared.json | f2a42b7e1ba6ed37de31c53b0fe0cf5938a1b1faa97c76c5fba01dfc8840ac1b |
| polar-gap092-physical-positive-zero-initial.json | 70d8fb7ca84ba50befbf800ab972275784f01612db7a8861639dc512bcfbff93 |
| polar-gap092-physical-positive-xyz-own1-initial.json | 70d8fb7ca84ba50befbf800ab972275784f01612db7a8861639dc512bcfbff93 |
| polar-gap092-physical-positive-xyz-own1-exit.json | f81a25e92477923b8d3766f391eacce34e74102a65431ab56b544be5b409be26 |
| polar-gap092-physical-positive-xyz-recover1-exit.json | 9745f35880eb56002a6b45caa4367e09b52a33aea7d7af5538c8d70ec4ec3542 |
| polar-gap092-physical-positive-innerGN-report.json | f32bf33a96281465b6b83061cef34a71b22113f0f4ce176c6ecb5442362e3aaa |
| polar-gap092-physical-positive-innerGN-G11.json | 45b64e4eb252ff0d68a26b85c59dc775c52400a1b394b745574c39265b6b139c |
| polar-gap092-physical-positive-innerGN-step01-state.json | c8b7fc94d952bf5b5a39f6da5de326101a50c306b050cd3139bf005adbc745e8 |
| polar-gap092-physical-positive-innerGN-step02-state.json | b5bd8b7f44e826854c62aad1dc1923f77681d13be0aead115cc8c7509ea4de3c |
| polar-gap092-physical-positive-innerGN-step03-state.json | 3e1020560db1c25eca4be8685ca4eb5ef171a8f05d83c7980dc271bfa15cc551 |
| polar-gap092-physical-positive-innerGN-step04-state.json | 6e2dfcd7d12c0d53134bf425f30bb3ed731508221f8eb3ad8963f8bc61945695 |
| polar-gap092-physical-positive-compose-exit.json | df65c7c06d0ccf24843d051a00078901a7b316599cee5b6e8f1ebaf6652a3db7 |
| polar-gap092-physical-positive-compose.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| polar-gap092-physical-positive-initial-only-exit.json | 15a78639aeb0ad51d54a25aca46c6ab0852312050028524b6a87081ecdf0336b |
| polar-gap092-physical-positive-initial-only.log | 800871316f66527764def0f3487b4940c614f09fd5889be9abed9213acd3217c |
| polar-gap092-physical-positive-innerGN-exit.json | bbc7f238bea374c07b40760c91bfb07f8b9c692c96c023ed76a4f3faa0188e90 |
| polar-gap092-physical-positive-innerGN.log | 3a98c585cf0c662e8a873a36dc80ee0cecc04d578afc867e54156f826e83b9ab |
| polar-gap092-physical-positive-innerGN-G11-exit.json | 0fb7a4eb43d593ca4351ee34212ce3effcbc410434a578475a753ceb7deede62 |
| polar-gap092-physical-positive-innerGN-G11.log | 934d0068bfd643b7fccd14ac6982937f18e186ab58fb7d0d04f3877c7d64859f |
