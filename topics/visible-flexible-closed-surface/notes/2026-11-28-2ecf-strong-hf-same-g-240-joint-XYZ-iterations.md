# 同一 HF 新度量的 240 次完整联合谱位置迭代

从[前 75 次的真实全部 6615 个坐标](2026-11-28-2ecf-strong-hf-true-XYZ-joint-spectral-solve.md)继续。按原实际角和物理 $s$ 导数重构两张 G10 与独立错移 G11，再打开同一完整系数空间求增量。旧系数和新增量都明确存储，累计系数仍定义同一 $g$ 下的真实位置。合并后核母场原成本、独立峰、度量定义、全部参数、材料时钟与实际物理基。将用于数值平衡的 metric、曲率尺度改为 .080、19，原 14 行项系数仍为 1。三阶段的平滑系数 35、80、160 各完成 80 次限额 L-BFGS-B，三个阶段都没有宣称驻点。

| 新阶段 | G10 metric | G10 曲率 | G10 原成本 | G11 metric | G11 曲率 | G11 held |
|---|---:|---:|---:|---:|---:|---:|
| 母场 | .087118369 | 22.257194 | .061258081 | .090945443 | 22.034318 | .65946514 |
| 35 | .087741296 | 20.360784 | .069077367 | .090229771 | 20.070069 | .66130351 |
| 80 | .083394133 | 19.544273 | .070891851 | .091186991 | 19.607630 | .66135232 |
| 160 | .081946831 | 19.313158 | .071768420 | .099258853 | 19.471687 | .66138078 |

在第一阶段，独立 G11 的三个报告量都改善。末态的两个训练峰下降，G11 曲率也继续下降，G11 metric 峰则回升至 .099258853，最坏在未用于训练的径点 $x=.1968676881$；不能把 G10 峰 .081946831 代为全域或独立峰。各阶段原 14 行成本上升；原七个几何 guide 和面积行在独立网格仍为零。没有全闭 reach、全域容差或同输入数值加密的完成结论。本次总用时约 183.99 秒。

```bash
python "$SCRIPTS/2ecf-strong-hf-fixed-metric-spectral-resume.py" "${hfargs[@]}" --diagonal clock-hf-diagonal-d006.json --warp clock-hf-two-material-spectral.json --warm clock-hf-full-joint-spectrum-03.json --prefix clock-hf-full-joint-240 --metric-scale .080 --curvature-scale 19 --original-weight 1 --coordinate-scale .035 --betas 35 80 160 --iterations 80 --ridge 1e-6 --block 54
```

三份实际状态 SHA-256 依序为：

- `aa4031209f7ab5fcaa1f94b3cfec47caad7d48e8b16fd62e727627ced96d3a0b`
- `ac9d625118f4a536d12bea123c5a772a6eae36ca72ce90409e93792be756dcd4`
- `49e19dcd0b92549b7aae1848e2fcfcb53249d7cf66840ca9460b7680772c727e`
