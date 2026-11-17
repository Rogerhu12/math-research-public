# n4 raw λ=0.02：完整误差的径向与频带定位

维护：Astra-held10-7322d0de-20261118；2026-11-18（UTC+8）。

## 核对方法

对 [原 M16](2026-11-18-n4-raw-lambda002.md) 与 [同 g M20](2026-11-18-n4-raw-lambda002-fixed-m20.md) 的两个实际 checkpoint，重新加载其完整物理 profile、原 polynomial field、参数定义的完整核心，以及原 Cartesian chain-rule 公式。使用与各自最终审计相同的径向点、网格中点和角点。此诊断不重求 BVP，不改变核心或 $g$。

[`localize_raw_defect.py`](../scripts/resume_n4/localize_raw_defect.py) 精确重现两个原审计的完整 metric 最大值；Darboux 与 flow 最大值也在浮点舍入范围内一致。新增输出只有峰值位置和有限频带标量，不输出高维谱数组。

## 最大值位置改变

下表中的 $u$ 是实际弧长材料角。Fourier 频率则针对数值角图 $\psi$，不把两者混为同一个坐标。

| 量 | M16 | 同 g M20 |
|---|---:|---:|
| 完整 metric | $2.41704708461\times10^{-6}$ | $3.43422818407\times10^{-6}$ |
| metric 峰径向 $s$ | 1.17855410463 | 0.0668734245771 |
| metric 峰分量 | $g_{uu}/a^2-1$ | $g_{ss}-1$ |
| 峰处固有 Gauss 曲率 | 0 | $-5.16859064511$ |
| metric 最大 Fourier 系数的绝对频率 | 60 | 84 |
| metric 的 $|k|>4M$ 部分占 $\ell^1$ 比例 | 10.06% | 54.27% |
| 完整 Darboux 峰径向 $s$ | 0.0599096531327 | 0.0704018114415 |
| Darboux 最大 Fourier 系数的绝对频率 | 64 | 80 |
| flow defect 峰径向 $s$ | 0.0895494840992 | 0.0696920631172 |
| flow defect 最大 Fourier 向量系数的绝对频率 | 71 | 83 |

两个 profile 的所有物理分段点完全相同。M20 的 metric 峰已经从外侧 $K=0$ 区移到最初的负 $K$ 区，不能把它理解为同一处误差单纯增大。

M20 的 flow defect Fourier 向量 $\ell^1$ 中，超过 $4M+1=81$ 的部分占 $99.999888\%$。M16 的对应比例为 $99.999658\%$。这直接定位了当前有限表示外的流场误差。M20 metric 的主频 $84=4(M+1)$ 也处在相邻未表示的标量频带，但 nonlinear metric / Darboux 张量自身会产生更高频率；仅凭这些比例不能断言哪一个分辨率改动一定足以收敛。

## 排除一个具体的数值解释

该 profile 的 `prefix_end` 为 $0.375834192240$。完整核心 lift 从 $s=0.5\,\mathrm{prefix\_end}\simeq0.1879171$ 才开始额外的 quintic 衰减，至 $0.9\,\mathrm{prefix\_end}$ 结束。上述 M20 metric、flow 和 Darboux 三个峰都在此前，衰减窗坐标分别约为 $-0.805,-0.786,-0.782$。

因此，这三个峰不是该 quintic 衰减窗边缘产生的导数峰。完整高频核心 lift 在该区域仍存在，不能由这个定位推出 lift 本身无关，也不能删去它来降低误差。

目前证据支持进一步检查同 $g$、同 $J=16$ 的角向截断变化，尚未给出持续下降的精化序列。随后 M24 使用完整旧核心和材料图的嵌套初值；任何新终态继续按完整 metric 门判断。

具体 source/checkpoint hash、物理分段点以及所有峰值标量分别见 [`raw-lam002-m16-defect-location.json`](../scripts/resume_n4/raw-lam002-m16-defect-location.json) 与 [`raw-lam002-m20-defect-location.json`](../scripts/resume_n4/raw-lam002-m20-defect-location.json)。
