# 相位 Schur 的近缩放方向与外负曲率环来源

状态：**同一实际函数的浮点诊断；未改变任何已保存候选。**

基准为 phase M24/n201/Q256，SHA256
`63b5513befcf44ce907b047dbeb41a7e143431211d20e3cbb103a081cbef0a0e`。
其三个有限 Schur 方向来自
`data/fourfold_phase_m24n201_schur_directions.npz`，SHA256
`2c6e5eb5c17578baf08f43a3d6b39e1699b5fd7dd0c17aae02047f0ba2fd158a`。
本节所有方向都使用完整相位变分
$V=\delta a\,\mathcal PT+a\mathcal P(\delta T)+\delta Z e_z$，
没有把旧位置图的裸 mean 列迁移到新图。

## 1. 小 Schur 谱不等于固定目标 metric 的齐次核

对每个径向位置定义角平均最小二乘投影

\[
\xi=\frac{\langle V\cdot F_x\rangle}{E},\qquad
E=\langle |F_x|^2\rangle.
\]

其导数由同一实际变分的 $V_x$ 与 $F_{xx}$ 按商法则计算，未对采样
曲线做数值微分。若 $V=\xi F_x$，对应 mean metric 输出满足

\[
\delta a=\xi a',\qquad \delta E=\xi E'+2E\xi'.
\]

原数值方程只消去 metric 的非均值部分，允许这些均值变化。
对于固定目标 $E,a$，还必须检查 $\delta E=\delta a=0$。
“是重参数方向”本身也不能自动推出“是固定目标方程的齐次核”。

最软 Schur 组合为
`(-.994734076190,.003528309200,.102428847011)`。
在 $x\in[0,.35]$ 核心，纯 $\xi F_x$ 投影后的相对 L2 余量为
`.86161666`，最大法向分量`.11444783`，并不接近纯径向重参数。
这个方向的最大 $|\delta E/E|=.37640$、$|\delta a/a|=.09871$，
而 $|\delta E-\xi E'-2E\xi'|/E$ 的最大样本约`.33039`。
因此不能称它为固定目标 metric 的零方向。

作为辅助诊断，再拟合一个**常数空间缩放** $\lambda F$。
对径向投影的余量求最佳常数 $\lambda$，得到核心
$\lambda\approx-.09506757$；此时
$V-\lambda F-\xi F_x$ 的相对L2余量降至`.03213`。
对应公式还需在上面的 metric 变化中加入 $\lambda a$ 与 $2\lambda E$。
这解释了该方向可能对同步改变 mean metric 后的核心返回数较软。
在整个有限体 $[0,3]$ 上，即使重新拟合缩放，余量仍为`.25116`；
不能将它认作全身的精确缩放/重参数。

脚本同时报告全部三个原列及三个 Schur 特征组合、四个径向窗口、
法向分量与 mean metric 变化。范数约定是坐标 $dx$ 乘角平均的 L2，
最大值是点上向量 Euclidean 范数，均为样本，不是统一上界。
对 soft 方向的独立对称差分核查，在 $x=.1,.23,.445$、参数步长1e-4时，
$V,V_x$ 最大差均小于3e-12；$\xi'$ 的径向差分步长从1e-4减到1e-5后，
误差由1.16e-6降至1.16e-8。这个核查支持实现一致性，不替代误差认证。

## 2. 外负曲率环在 phase 表示之前已经出现

独立特征扫描发现当前 phase 图在中央负曲率核心以外又有一条
全角负曲率环。本节追溯三份已保存位置图，使用它们的实际二jet。
旧位置图的 target radius 是
$a=\sqrt{\langle|F_\theta|^2\rangle}$；其一二阶径向导数由
$F_{x\theta},F_{xx\theta}$ 求得，后者直接来自同一个样条的二阶径向
系数再求角导。没有用旧平均径向位置替代该 target radius。

令 $E=\langle|F_x|^2\rangle$，则该径向 target metric 的曲率为

\[
K_0=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}.
\]

同时检查实际 immersion 的 $\det II/\det I$，不是只看 $K_0$。
以下窗口为 $x\in[.30,.60]$，径向步长.001；旧位置图512全圈角点，
phase 图256 quarter角点。

| 保存状态 | $K_0(.445)$ | 窗口内实际 Gaussian 最小样本 |
| --- | ---: | ---: |
| position M16/n101 | +1.963296 | +.744957 |
| position M16/n151 graded | +.734644 | +.697498 |
| position M24/n151 graded | −.428304 | −.431198 |
| phase M24/n201/Q256 | −.504096 | −.504407 |

前两份位置图在这个窗口没有发现负环；M24位置图已经有全角负区间，
样本约 $[.430,.455]$，target零点插值约`.429113,.455913`。
phase图的区间约 $[.428,.456]$，target零点插值约
`.427728,.456708`。phase图在 $x=.445$ 的实际 Gaussian 范围是
`[-.504407,-.503887]`，因此该现象不是只存在于径向拟合 metric。

三 mean 系数沿保存序列从
`(.36731,-.00003985,-.01684)`，到
`(.56898,-.001276,-.03696)`，再到
`(.78517,-.002128,-.05932)`；当前phase为
`(.799535,-.002083,-.060915)`。
外环在 unrestricted mean 的这一段漂移过程中出现；不能把它归因于
单位切向转换或角FFT的后验误差。

## 3. 半径 .5 的 mean bump 是主要来源

在当前 phase mean 上作以下**剖面对照**，这些对照不是新的等距解：

| mean/profile 对照 | $K(.445)$ |
| --- | ---: |
| 当前 mean 与保存 circumference shift，去掉phase场 | −.504856 |
| 当前三mean，去掉circumference shift | −.479081 |
| 保留当前第0/1 mean及shift，只把半径.5的第2系数设0 | +2.522270 |
| 原始零mean背景 | +3.324907 |

第三个对照在整个 $[.3,.6]$ 的最小曲率仍为+.32913。
因此宽 mean bump 的实际二阶几何是外环的主要来源。
将系数设零并不满足原非线性 metric 方程，不能把这个对照当成完成的
修复。后续需要在同一真实 Schur 兼容方向上同时支付残差、可见性和
外区曲率条件。

当前图尚不能直接套用“一个中央双曲核心加两个正曲率端块”的分解。
额外负环要么经真实兼容修正消去，要么需要另外建立多转折区域的
全局分析。此前腰圈 $N,\det II$ 为负并不能保证全体只有一对转折。

## 4. 文件与精确重做入口

- `scripts/fourfold_phase_gauge_diagnostic.py`
- `data/fourfold_phase_m24n201_gauge_diagnostic.json`
- `scripts/fourfold_outer_ring_diagnostic.py`
- `data/fourfold_outer_ring_origin.json`

两个 JSON 记录对应脚本 SHA256；gauge 记录输入图与完整方向的哈希，
外环记录四份输入图的哈希。所有输入向量已经另存入仓库。

```bash
mkdir -p /tmp/visible-exact-diagnostics
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_gauge_diagnostic.py \
  topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_q256_checkpoint.npz \
  topics/visible-flex-exact-nearby/data/fourfold_phase_m24n201_schur_directions.npz \
  --angles 256 --out /tmp/visible-exact-diagnostics/gauge.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_outer_ring_diagnostic.py \
  --out /tmp/visible-exact-diagnostics/outer-ring.json
```

全部结论保持浮点/采样限定。代码没有变更 canonical phase24 候选，
也没有把剖面试调或有限 Schur 方向升级为精确存在结果。
