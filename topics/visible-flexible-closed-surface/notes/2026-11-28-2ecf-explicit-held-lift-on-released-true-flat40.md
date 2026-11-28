# 释放切圈场上的实际低模排球位移

**数值证据。**

在首个 675 控制的真实位置场上加 C² 端口夹持的多项式径窗，Y 方向叠加负的奇次正弦，Z 方向叠加偶次正弦。对每个原 G10 采样真点和两球中心解所需位移的实际二次式，再评估变动后的全部六 jets 和十四原行。12 个物理基均将 G10 held 推到 .6508；其中无一同时满足采样 κ<1/.097。按原完整行平方和选择的 (m,n,p,k)=[3, 4, 5, 0.8]，幅 0.03182458302016637。独立 G11 误差 / κ / held 为 0.2541240362 / 12.10901571 / 0.6509468117，故其局部曲率及度量较未变形的源恶化。选择操作自身没有迭代接受。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-low-mode-held-and-curvature.py" --mode select --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-true-flat40.json --field polar-released-cut-true-flat40.npz --output polar-released40-low-lift-select.json
python3 -u "$S/2ecf-polar-released-low-mode-held-and-curvature.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-true-flat40.json --field polar-released-cut-true-flat40.npz --output polar-released40-low-lift-observe.json --selection polar-released40-low-lift-select.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-low-mode-held-and-curvature.py | b88c0bf070cbe0456605bed927acdfc739a050f20f1098ecf6cf3353f2ca7abf |
| polar-released40-low-lift-select.json | b3553a0f5028c1a6b58e9817d17573e46f5cc6f86cf7eb4c7eaffba2ee9d1197 |
| polar-released40-low-lift-observe.json | ea6833880cf7b362980602833ff8dc1b13094048b42d39ef3ffe50dcd16f9408 |
| polar-released40-low-lift-select-exit.json | bcef211be6378c34431c3908b8cfd3d89f3742eadfada6152359992c762f2e88 |
| polar-released40-low-lift-select.log | 3f7de96c0181c5bb2e58162a09dfa5599023efc5f43560a61cb79fc2e66c09f1 |
| polar-released40-low-lift-observe-exit.json | e6f1c7b315e9bc80726378efabd76d4fb439daf8ed08a7cf9ff3968c1567bc4f |
| polar-released40-low-lift-observe.log | d6a327c0e4dce0a9e2d2c29ecb9e327f2176429b33faa2abfe1be65f8d8669b6 |
