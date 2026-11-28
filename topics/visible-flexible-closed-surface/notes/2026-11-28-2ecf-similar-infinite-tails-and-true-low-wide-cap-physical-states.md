# 原无限尾的准确相似变换与低宽帽高度窗口内的真实大幅状态

取原 R262 真实 cuff 半径 $a_0$（manifest 所存 `0.14999999999999997` 的准确二进数），保留一直到已证平斜率 $r=1/4$ 的全部无穷线与原物理母线。相似变换 $X\mapsto\lambda X,s\mapsto\lambda s,V\mapsto\lambda V$ 使 $r,z,f,h$ 扩大 $\lambda$ 倍，$w,f_s,h_s$ 不变，$w_r,f_{ss},h_{ss}$ 除以 $\lambda$。每单位端口高度的线性形状算子量按 $\lambda^{-2}$ 转移。原深线的完整零二阶 cuff 迹与[真实平台证明](2026-11-28-2ecf-r262-oscillating-tail-second-mode-physical-meridian-and-shape-steps.md)同时转移。以下都重求外部传递与新固定度量。

| 新物理输入 | 实际位置和曲率观察 |
|---|---|
| $\lambda=8/5$，.4→.6 外缓段 | 65536 个缓段和 32768 个前缀设计；单位线性组合量约 173.24，中心 .71326、cut 高 1.345。$\epsilon=1/32$、32 段 6 通道，独立移位峰 .0153381、曲率 9.8181，原生深部曲率 5.1924。 |
| 同一 $\lambda$，.4→.8 新缓段 | 两次各 65536 个设计；中心 1.40695、cut 高 1.11197、组合量 60.3723。$\epsilon=1/16$ 移位峰 .00124735、曲率 8.8961；$\epsilon=1/8$ 真实位置步达 .00653938、曲率 9.6812，原生深部曲率 6.4065。 |
| $\lambda=(8/25)/a_0$，准确平领 $8/25$，新 cut 约 .85 | 65536 个六段缓段。初次两转的短前缀虽在 16384 例中找到 2412 个低高度根，最小单位线性组合量仍约 12505。 |
| 同一准确平领/缓段的折返前缀 | 角速度首、末 $1/16$ 线性制动、主体常速，母线位置 $C^2$。32768 例中有 3021 个低高度根。第一项 cuff 高约 .617932，其 $\epsilon=1/32$ 完整场单存。第二项中心 1.18234415、cut 高 .56494721、实际 cuff 高 .57507874、材料半核总长 1.48971463。 |

最后一行第二项位于 R215 帽给定的高度窗口。$\epsilon=1/16$ 纯二次真实中央、32 段每坐标八通道给独立峰 .01374322、曲率 12.63493。同一度量上另取 $p=32,\epsilon=.34$ 的真材料中央，基线水平、垂直线性振幅分别乘 .75、.25 后用实际中央二阶 Hermite 提升。其真实周长不变、半宽差为准确的两倍二进 .34。[平滑支撑及曲率的定义](2026-11-28-2ecf-short-m2-curvature-updates-and-full-amplitude-centers.md)

| 同一大幅中央 | 935×225 移位峰 | 移位曲率 | 原生深区曲率 | 核球半径采样 | 核 y 绝对值峰采样 |
|---|---:|---:|---:|---:|---:|
| 32 段，每坐标 8 通道 | .11724801 | 12.21570 | 11.01872 | 1.452988 | 1.026908 |
| Boehm 嵌套加至 64 段，每坐标 10 通道；同时求 slab 及球的实际位置导数 | .11656764 | 13.65673 | 10.12506 | 1.452988 | .948124 |

两行均另测独立网格，以及 17046 原生径行和 120 错角。64 段全域采样曲率回升，两个实际 slab 均超过 .895。32 段态的固定极角高度导数最低约 −.45416；8、18、32 段样条搜索 $z+F(\rho)$ 也仅取得约 −.283 的最小径向导数，尚无全域单射证书。

令 `S` 为课题 scripts 目录，`W` 为已经再生[原完整深表与平台](2026-11-28-2ecf-r262-oscillating-tail-second-mode-physical-meridian-and-shape-steps.md)的新工作目录。使用 NumPy、SciPy，集中入口运行上述相似法、全部尾/前缀、新物理态、深曲率与球板观测。输出文件应不存在。

```bash
python "$S/2ecf-r262-m2-low-cap-reproduce.py" --scripts "$S" --work "$W"
```

| 源码或产物 | SHA-256 |
|---|---|
| `2ecf-r262-m2-similar-infinite-tail.py` | `bb8614a4636dedb4d1c11ca442d99375cfc7d9f7a4284976d99e8ddb06c697a1` |
| `2ecf-r262-m2-scaled-radius-physical-meridians.py` | `3b6e28db8395b4027ed209370d4b5db62972eb5e785969237e675cd939faff04` |
| `2ecf-r262-m2-low-cap-window-physical-meridians.py` | `d5a62e45e7094f61e59b8ecf7ba0cdf77bd4952ae999c0627921f923d5401ae8` |
| `2ecf-r262-m2-low-cap-double-return.py` | `72129cfb22928cdc1898ec09ef0d4fe3700449ad9c8ad6f17c19d2bd7e460a3d` |
| `2ecf-r262-m2-low-cap-physical-continuation.py` | `65647f9a490e69bcd66e2e158bc15e89f8f0131675ad23f3b2f18c401b4fe01c` |
| `2ecf-r262-m2-low-cap-stadium-active.py` | `af678b3fb4cb4a8236e35804497960e07dbd4b2e9edfa1fd9029da94ba8c0f54` |
| `2ecf-r262-m2-low-cap-slab-active.py` | `bf78bd670fef4c31b1feda63306f693a3f58a04e6648459dcf444434d080b4d3` |
| `2ecf-r262-m2-low-cap-geometry-observer.py` | `7e132fafb2605731e0056fcc1cc698210466cd660d2e36c1febe99f632dba92b` |
| `2ecf-r262-m2-low-cap-reproduce.py` | `0b27fd89bfd386bbf6273061df0057b3adcd5b9ad0def54d69a9405026a5c9f5` |
| `g12-m2-lambda8over5-buffer-cut8.json` | `4243c83145bfa5218a1e983c8f464188fb410d8cc9f37329bb8ef152ecbbb7f0` |
| `g12-m2-lambda8over5-buffer.json` | `cbbc4aed9da427227a4b4a9df232c78600b36f81069b556a35aac29754da20a4` |
| `g12-m2-lambda8over5-cut6-eps1over32.json` | `3b40d4fef235c0831b49c25f0354b15c45dd293c187786f4627fb12ea714c730` |
| `g12-m2-lambda8over5-cut8-curved-eps1over8.json` | `135c751bcb02c6c2e1849c8c48b94c26891782110aee48bb6f6ce0caac8fcb4d` |
| `g12-m2-lambda8over5-cut8-eps1over16.json` | `34981214aa9371c61ed63b0e2b7da67565badedff5f88b9254cdca022a5520aa` |
| `g12-m2-lambda8over5-short-cut8.json` | `55ebf84f3a3bee3adbb0a56a7d9d2d6590e3790f914f68142b74e171af50e329` |
| `g12-m2-lambda8over5-short.json` | `fc16f0db165a973364fe8e41241a6b0977240cdcbe5628ff1516afd986f811a1` |
| `g12-m2-lambda8over5-tail.json` | `d09ab9e7928ed5af624ae4e8ee89ed9bb30e5368b4fb14eb77c6e1642467cd44` |
| `g12-m2-exact-cuff32-tail.json` | `19ca111b7679c799504f75831116a5d8bcf66bcadcf5eba4d6da1d45730df785` |
| `g12-m2-exact-cuff32-cut85-buffer.json` | `9dcdfbac41ff8c5b5c971a8f750e22d880602d88948f53b3da3a306cb9407d8a` |
| `g12-m2-exact-cuff32-lowcap-cut85.json` | `767468a1f39e01fb901cc5e4c9749ccb40110c59a186c2889ef63159e479ad28` |
| `g12-m2-exact-cuff32-low-double-cut85.json` | `db4e7587bc9fa9938a0c299bdeff3f96d97d5573052853d9505dc1a409f42911` |
| `g12-m2-exact-cuff32-low-double-eps1over32.json` | `9acab7fa4fad2add1700335d072490521162a20bd7039e5729ff1650f6239457` |
| `g12-m2-true32-low575-small-eps1over16.json` | `a5b38c2c9e7ccfdfb50455a9984b0c6eb5e0ed2e83657fb36a8eada6aeccf772` |
| `g12-m2-true32-low575-stadium-eps034.json` | `c473d69429afab745d6ccd71763f3eea11ea925dd26ad64396452d6c00035cab` |
| `g12-m2-true32-low575-stadium-geometric.json` | `8a86cb4a542eec96f89e6bd05a35c4083f574d63b23e1495c4c42a1d87fb1cf8` |
| `g12-m2-true32-low575-stadium-slab64.json` | `9eb9eebe3442cca1695dbbdb0da0d2eed5fa887d339a10c0b1aec2e7dfecfae6` |
