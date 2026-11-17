# M320/N4096 从 .997 向 1.0：有限域失败、有效末态与高模定位

日期：2026-11-17。维护：`parallel-geometry-amplification`。

**状态：未到达请求终点的真实有限 IVP 失败记录。没有新可接续父，没有
全新段成功 C² 读出；不据一次未接受 stage 宣称数学上的不可延拓。**

## 1. 延续对象与共享 jets

从已成功且完成全短段读出的 M320/N4096 `.997` 真末节点继续，输入
`parallel-short-ivp-m320-cleanfield-n4096.json.gz`，SHA
`507cab03af49bf58305cd9e91421e2b91c0071cc4115dd8e1f6d1f047ad9389a`。

保持全部 962 条方程、同 M/N、同标量及原 core `rho`，没有重新零补。
DOP853 参数为 `rtol=1e−13`、`atol=1e−16`，首步及步长上限
`.000015625`，请求到达 `s=1.0`。Q/W/H 域不夹断。

新首节点直接共享输入已存储的 value/rhs/d2。
重新计算 RHS、二阶 jet 与存储值逐字相同，最大系数差均为 0。
因此这一个局部连接点的公共 jets 没有混用不同 M、N 或另一个初值。

## 2. 实际终态和失败 stage

运行接受了 50 个实际节点，719 次 RHS 调用；最后有效时刻为

\[
s_*=.9976192183160486.
\]

下一个未接受 stage 在 `.9976193423844432` 触发域错误。两者相隔约
`1.24068e−7`，不是在初始状态就用大步直接失败。保留了实际全部接受节点及
其 RHS/d2，但没有把它们作为新的接受父，也没有继续无限缩步。

令

\[
Q=|F_\phi|^2,\quad W=|F_\phi\times F_{\phi\phi}|^2,
\quad H=W-k^2Q^3,\quad k=a'/a,
\]

并在给定角网格上计算 `k_admissible=min sqrt(W/Q³)`。

| 数量 | 最后有效状态 | 未接受 stage |
|---|---:|---:|
| s | .997619218316 | .997619342384 |
| 实际 k | .292996277939 | .292996053878 |
| 采样 k_admissible | .293782908909 | .292298356347 |
| `k_admissible−|k|` | +.000786630970 | −.000697697531 |
| 最小采样 H | +8.31461108414e−8 | −7.29139639002e−8 |
| 最差角 | 2.70594210983 | .434116562972 |

这两列的 stage 判据使用原 N4096。对**同一最后有效曲线**再用 8192 角读，
上表的 k_admissible、最差角及 H 最小值均相同。此处 H 是 Frenet 域量，
不表示帽高度或握持集合。

有效末态已经接近该有限域边界，随后 stage 越界；这与域余量耗尽相容，
但未接受 stage 不是实际积分解值，不能据其负 H 证明真解必在同一时刻越界。
本次没有再进行更小步长扫描或新标量试验。

## 3. m>224 的角向贡献

在最后有效曲线上，仅提取旋转分量中的模 m=225,…,320，保留真实原系数。
最大单个高模系数为 `6.27901244991e−9`。8192 角的高模贡献为：

| 高模量 | 最大采样向量范数 | 系数三角求和值 |
|---|---:|---:|
| F | 3.97989286125e−8 | 6.30855226831e−8 |
| F_φ | 2.20917766819e−5 | 3.50907263925e−5 |
| F_φφ | .0123521807710 | .0195877476828 |

第 ℓ 阶系数三角和按

\[
\sum_{m>224}\bigl[(2m+1)^\ell(|R_m|+|T_m|)
 +(2m)^\ell|Z_m|\bigr],\qquad \ell=0,1,2,
\]

计算，已经包含 Cartesian 旋转基产生的额外一阶频率。表中数值仍为浮点
计算，未附有理外包认证。

作为一次**同一曲线的诊断性删模**，将 m>224 置零，保留实际 k，再用
8192 角读得 k_admissible 约 `.327450059804`，余量 `.0344537818650`，
最小 H 约 `3.83369187049e−6`。这说明这些位置幅度极小的高模在角二阶几何
中已有显著作用。删模曲线不是另一份真 IVP，更不是已解决的 M224 延续；
本次没有以删模结果作为新初值。

## 4. 来源及复现

源：`notes/2026-11-17-parallel-geometry-short-ivp-continue.py`，SHA
`2874954eeeb8121a0b63f3fc3fe869da62332b99663b3ddac19396e27bd32c17`。
复用冻结局部 quintic 读者 SHA
`ed0de0d513f28e1d227ba4f49a2ac2b2379107ca200c50f0d43f933e0edfd924`；
由于本次未到目标，成功场的全段读者没有执行。

在课题目录运行：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python \
  notes/2026-11-17-parallel-geometry-short-ivp-continue.py \
  --input "$SCRATCH/parallel-short-ivp-m320-cleanfield-n4096.json.gz" \
  --output-stem "$SCRATCH/parallel-short-ivp-m320-continue1000-final" \
  --end 1.0 --max-step .000015625 --rtol 1e-13 --atol 1e-16 \
  --read-angles 8192 --radial-subdivisions 4
```

最终失败 raw SHA：
`0ecf757b7958f739a3f1726075fe4312d81d2c030eebb419cd8ae113bf9cd1bf`。
最终诊断报告 SHA：
`cc2c233341f2550214f99de97ecfbbb9b2ca9ce1e82043ce132daabd745a11f2`。
raw 包含实际接受的完整节点 value/rhs/d2、共享起点 jets、失败 stage 定位及
域/高模诊断；标记 `ivp_reached_end=false`、`bvp_accepted=false`，只留 scratch。
