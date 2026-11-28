# HF64–M80 原位圈的九点有理秩见证

**准确有理证明。** [R269](../results/R269-actual-ringwise-similarity-and-angular-clock-obstruction.md) 给出全环随 s 刚动、正缩放和任意角重参后到达角不变度量所需的微分兼容式。存储物理内结点 7 的九个准确单位圆点上，8 列允许参数的秩为 8，增广后为 9。对任意参数，必要式所余的最大绝对值至少 1.7718527881。问题针对实际新定义的完整 HF64–M80 加原物理 W。
以下 F 是先按[明确物理场的完整重生配方](2026-11-28-2ecf-strong-accurate-hermite-fourier-position-with-literal-W.md)生成 HF64–M80 加物理 W 的产物目录。其中 field SHA256 为 eaa0835dc7ea5207f2a93cb0ba9b1d1634f2e00c5cb8964fe954b47601990d86，源报告 SHA256 为 6e9dc0acf08851725780e6b6998c7897750a3966cb39d100934d3fb3a5a8c036。脚本使用其中完整 knot、真实 Fourier 和 W，以 Fraction 逐点构成准确矩阵并对全部余子式作整数消元。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-hf-ring-similarity-witness.py" --field "$F/strong-physical-hf64m80-W.json.field.npz" --field-report "$F/strong-physical-hf64m80-W.json" --output polar-HF64-ring-similarity-witness.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-hf-ring-similarity-witness.py | e97791d7353bf95c269f2aef1605d884615bc1275638008483facd5cc50e48a0 |
| polar-HF64-ring-similarity-witness.json | 98c9138c7f78bc85f583a67e56d9caf98dc2151f588c43b4fad204095af64245 |
| polar-HF64-ring-similarity-witness-exit.json | 2283a8dc6c997b64fd1f391096eae65ffbf998d344b7d2b6b95a19623e69f79a |
| polar-HF64-ring-similarity-witness.log | 73955af3998a8bd2111f86ad05631574cf4e941f73f940b0aa368f699e24639d |
