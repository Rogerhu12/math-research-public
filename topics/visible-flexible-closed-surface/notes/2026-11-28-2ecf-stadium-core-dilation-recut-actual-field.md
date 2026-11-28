# p32 单独相似放大、真实重裁与未随核缩放的帽

[R301](../results/R301-core-only-similarity-and-exact-flat-recut-with-unscaled-caps.md) 给出变换、核与全帽目标和每一同场条件。实际对象是 [2100 维的首个 48 步高领输入](2026-11-28-2ecf-raised-stadium-exhaustive-cuts-and-2100-positions.md)，其新领选择沿用 [十八种完整真实候选](2026-11-28-2ecf-stadium-eighteen-true-cuff-changes-with-r293.md)第 4 种。给定真实高领、尺度及平环后，归一 metric 峰在原材料处严格保留；每个实际曲率及全核闭图切球比由相似转移。帽本身的真实诱导度量另由 R293 固定。不能用原核心的绝对 $r$ 和新帽的整体直径任意拼接。

复用前引所有物理输入及 `--extra-state stadium-p32-minimax-b-ex10.json stadium-p32-direct-balls6-a-stage02.json stadium-p32-raised-dense12-b-stage01.json --elevation stadium-p32-six-cuffs18-corrected-elevation.json`。执行：

```bash
python "$SCRIPTS/2ecf-strong-stadium-core-only-homothety-budget.py" "${shared[@]}" --prefix stadium-p32-genuine-scaled1
python "$SCRIPTS/2ecf-strong-stadium-elevated-independent-closed-pairs.py" "${shared[@]}" --prefix stadium-p32-raise54-own48-shift
```

第一条从训练的 128、192 角选 $\lambda=1.1$ 并固定全部物理量。四个有富余的原训练比上限分别为球 1.10038286、宽 1.10911437、高 1.12257859、领 1.10925926。独立的 256 错相角完全未用于这一选择。首个直接程序的完整结果随附，SHA-256 `0fa4128956e7a4a79dd3add1bcda745bd0126e37e197e69e3f3c442c47f54b43`，包含新目标、领、平环及全部三组原行的数值回执。第二份独立点对数据的 SHA-256 为 `d6bd08cc53e1893c2f418ddc62a4c08ee55d95c6ecf05e6a3fc104a58f651b54`。后者的角径、球、法向与物理源可逐项复算；.10078938184 是这组点对的实测值。
