# phase24 的三根网络与兼容外环消除预测步

2026-11-12，constructive-route。**本条是普通浮点探索和完整输入记录，
不是精确等距面、连续区间型别或 reach 的证明。**

## 1. 输入与两个型别对象

原输入 data/fourfold_phase_m24n201_q256_checkpoint.npz 的 SHA256：
63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e。
方向为同一候选的 data/fourfold_phase_m24n201_schur_directions.npz；
其内容与首次运行使用的 scratch schur-phase-m24n201.npz 相同。

使用 scripts/fourfold_phase_geometry.py 对同一个 Q256 有限原函数求
真实二、三 jet，区分：

- 实际曲面 $K=(ln-m^2)/|F_\theta\times F_x|^4$；
- 同步径向目标 $g_0(p)=E(p)dx^2+a(p)^2d\theta^2$ 的 $K_0$，
  其中 $E=\langle|F_x|^2\rangle$、$a$ 为保存的周长半径；
- R37 modified 主符号的未归一化判别式
  $\widehat\Delta=(-K_0)G_{\rm actual}^2$。

不能把实际 $G_{\rm actual}$ 预设成 $G_0=Ea^2$。
方向变化包括同步 $\delta g_0$；选定候选后才能把相应 $g_0$ 固定给
modified Newton。Schur 方向保持 $\delta\beta_4(0)=0$，只最小化有限
加权线性残差，未给出精确 PDE 的解族。

## 2. 原图正侧三根

128 个逐角点的实际根每次都从真正有限原函数的判别式求解，
不把一个径向平均根当作实际根。表中的 $K_0'$ 是目标根处的径向导数；
$N$ 和非特征因子在各角自己的实际根上计算。

| 根 | 目标位置 | $K_0'$ | 实际逐角根范围 | 实际 $N$ 范围 | $1-(-M/N)t_\theta$ 范围 |
|---|---:|---:|---:|---:|---:|
| 中央出口 | .235457107261 | 45.22280668 | [.234529866926,.236116366669] | [−3.03046197,−.53692916] | [.97023816,1.02809379] |
| 外环入口 | .427726979478 | −44.31442432 | [.427724455868,.427728821603] | [−1.37410990,−.94863947] | [.99997995,1.00002415] |
| 外环出口 | .456717928810 | 91.84619057 | [.456716307819,.456720185970] | [−1.31398037,−.97840492] | [.99999153,1.00000417] |

实际 $K_x$ 在三组实际根上的范围分别为
$[36.61459,53.38717]$、$[-44.32396,-44.30705]$、
$[91.62406,92.02264]$。原始判别式求根最大残差分别约
$1.74\,10^{-10},1.49\,10^{-10},8.63\,10^{-11}$。
以上是浮点残差及有限样本，尚未做向外舍入或连续包络。

在已扫窗口 $[-.6,.6]$，目标负曲率分量为中央
$(-.235457107261,.235457107261)$，以及正、负侧两条外环。
实际曲面有对应的三个负曲率分量；例如 $x=.445$ 的全角实际 $K$
约为 $-.504$。所以原图的中央返回映射只能用于中央散射块，
不能宣称覆盖整个半面或直接套用只有两根的全域接口。
完整根数组、支撑区间、目标根参数列及正负样本见
2026-11-12-phase24-three-root-mean-control.json。

## 3. 三个真实均值列的兼容控制

令 $d_i$ 为保存的三个完整 Schur 方向，$S$ 为实际剩余的 Gram 矩阵。
以 $v_{\max}$ 为 $S$ 的最大特征向量，约束
$v_{\max}\cdot\delta\alpha=0$，删除最主要的有限线性不相容行。
这只是有实测来源的方向筛选，**不是无限 PDE 的充分兼容条件**。

在 $x\in[.3,.6]$ 的181径向点上求线性规划：

$$
\min\|\delta\alpha\|_\infty,\qquad
K_0(x)+\sum_i\delta K_{0,i}(x)\delta\alpha_i\ge\kappa,
\qquad v_{\max}\cdot\delta\alpha=0.
$$

先取 $\kappa=.02$，得到
$(.01072358979,-.00677668091,.01072358979)$。
完整非线性重算使目标 $K_0$ 最小值变成 $.02092597$，
实际曲率的采样最小值仍为 $-.00379979$，故这一试步尚未消掉真实外环。
若忽略兼容行而把三个 mean 同号增加，虽然目标曲率为正，
实际曲面却出现 $N$ 翻号和巨大曲率；这个失败对照也完整保留。

再取 $\kappa=.05$，得到

$$
\boxed{\delta\alpha=
(.011343751648855448,-.007168586888997951,
 .011343751648855448).}
$$

该增量的有限线性 metric 加权 $L^2$ 范数为
$2.5826202\,10^{-5}$，完整控制向量的最大变化为 $.01134375165$。
它近似沿 $\delta\alpha_1\approx-.632\,\delta\alpha_2$，
与删除主兼容行的方向一致。

直接重算 $v_{\rm trial}=v+\sum_i\delta\alpha_i d_i$，**没有做 Newton**：

- 目标 $K_0$ 在上述181点上的最小值为 $.05100340$；
- 实际 $K$ 在61径向点、每点64角点上位于
  $[.02356754,3.31466110]$，实际 $N$ 位于 $[-2.08587181,-.74060082]$；
- 中央 $[0,.2]$ 的目标 $K_0$ 样本仍为负；
- 全有限 body 的1798径向点、每点256角点诊断给出 metric operator
  残差 $.00388876$，故必须继续修正，不能视为已解；
- 腰圈实际径向差 $.1321159745$，两倍采样原点半径 $2R=2.5774082895$，
  比值 $.05125923$；这里只是当前有限 body 的可见比代理，
  不是闭合后的 $D$ 或 held 证书；
- 采样支撑函数最小 $.88676465$，最大主曲率绝对值 $7.74836386$，
  $\beta_4(0)=.20747484022400084$ 保持；
  这些也不是 reach 的连续严格下界。

该完整预测步保存为
data/fourfold_phase_m24n201_ring_removed_predictor.npz，
SHA256 为 0491c4a735e59e2631e8bc8646d4b6590ec699b74c4c4885dc981be6b7aedbaf。
它包含原始 radius shift 及独立 metadata，绝不覆盖 canonical。
新 mean 为
$(.810878909698159,-.00925125048406027,-.04957108612196493)$。
全部原输入哈希、方向哈希、线性规划、非线性重算和全 body 诊断见
2026-11-12-phase24-compatible-ring-removal-trial.json。

**必须连同保存的 trial 一起读取的失败项：** 随后的1201径向点、
每点256角点全 body 型别扫描发现，上述预测步损坏了中央真实二型。
目标 $K_0$ 只有一根 $.2398132250$，且实际曲面在
$x\ge.2525$ 的全部样本都椭圆；但中央 $[.115,.2525]$ 内出现54条
正负曲率混合的径向采样行，实际 $N$ 最大值为 $+.74932570$。
一个逐角根算法所选的根落在 $[.15077495,.25194930]$，
非特征因子跨零。这些逐角根不能再解释为唯一、光滑、横截的同一转折图。
所以该 predictor 只证明了一个外环控制方向的数值可行性，
**不是可直接接 R37 的新好候选**。不能对它运行要求 $N<0$ 的主返回
程序或宣称已经恢复全域两根结构。完整数据位于同一 JSON 的
trial_finite_body_type 字段。下次控制必须同时约束中央实际 $N$
和型别，或由受约束 Newton 恢复它们。

## 4. 精确重做入口与下一道已明确的门

在仓库根运行（只输出浮点诊断）：

    OPENBLAS_NUM_THREADS=1 python -u topics/visible-flex-exact-nearby/scripts/fourfold_phase_type_control.py \
      --checkpoint topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
      --directions topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_schur_directions.npz \
      --out topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-three-root-mean-control.json \
      --control

    OPENBLAS_NUM_THREADS=1 python -u topics/visible-flex-exact-nearby/scripts/fourfold_phase_type_control.py \
      --checkpoint topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
      --directions topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_schur_directions.npz \
      --out topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-compatible-ring-removal-trial.json \
      --control --margin .05 --compatibility-only \
      --reuse-root-report topics/visible-flex-exact-nearby/notes/2026-11-12-phase24-three-root-mean-control.json \
      --trial-checkpoint topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_ring_removed_predictor.npz \
      --trial-type-scan

当前最具体的正向接口是：保住 $\alpha_2$ 的外环可行区间，
让其它 mean 和相位变量修正新的 metric 残差，再从同一修正图的真实
R37 主算子重新计算返回及参数导数。不能把原图的返回、旧 n101
径向作用量、或此预测步的线性 $K_0$ 控制直接移交为 KAM/PDE 逆。
全频误差、转折幅度、次主相位、完整散射、两端固定开帽、闭嵌入和
reach 等原欠账仍必须分别完成。
