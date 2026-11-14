# R139 后续：自然母线标签角的实际谱比较与 U-map 接口

## 1. 同一物理场、两个明确计算角

固定 R139 的新34基准 $g$、保存的入口 $n_c,m_c$ 和完整解析 native 场。本次没有生成另一物理度量，也没有求解新的 ODE 或 BVP。

原表在固定 seed-normal $\phi$ 上取样，材料角为 $u=U_{\rm seed}(\phi)$。本次把计算角改为入口母线标签 $\xi$；它同样以入口 seed-normal 角计量，但对 $\sigma>0$，所对应的实际材料角变为

$$
t=U_0(\xi)=U_{\rm seed}(\xi),
\qquad
U(\sigma,\xi)=t-\frac1v\arctan\frac{w(\sigma,t)k(t)}{\rho_c+w(\sigma,t)}.
$$

因此本次比较的是同一 native 正交分量 $l,m,n$ 在两种角图中的函数表示，而非把计算角的二形式分量与物理正交分量混为一谈。

## 2. 全部二阶标量 map 与冻结约定

[fd2d_k0_ruling_chart.py](../scripts/fd2d_k0_ruling_chart.py) 提供

`FrozenRulingChart(inlet_path).jet(sigma,xi,include_native=False)`。

返回 $U,U_\sigma,U_\xi,U_{\sigma\sigma},U_{\sigma\xi},U_{\xi\xi}$。若 $h=U_0'$、$h'=U_0''$，由 R137 的入口材料导数直接得到

$$
U_\xi=U_t h,\qquad U_{\sigma\xi}=U_{\sigma t}h,
\qquad U_{\xi\xi}=U_{tt}h^2+U_t h'.
$$

严格 $D>0$ 的区间包保证 $U_t>0$，准确 balanced 材料图有 $h>0$，所以此图全角可逆。入口和出口的径向导数按各自 coast 单侧值返回，不假装和外片的计算图具有相同径向 jet。

本次实际最大单侧 $|U_\sigma|$ 为入口 $1.8855467605935923$、出口 $1.3592013195379453$。这是计算 atlas 接口应明确处理的量。不能只因 $U$ 与角向 jets 接上，就把分片计算图说成全局 $C^1$。原固定材料几何的接合须按物理状态及其正确导数完成。

图中的 $k=m_c/n_c$ 永远来自冻结的基准入口，不是待求 BVP 场。改变径向外设计 $a\mapsto a_\delta$ 时，此图可以作为固定参考坐标；其值和正性不因求解中的未知 $n$ 经过零而失效。但 R139 的原 native 场仍只在原 $\delta=0$ 度量上准确，不能借给改 $g$ 的方程。

对任意正 $a_\delta(s)$，接口 `pulled_metric(a,U_s,U_xi)` 给

$$
g=d\sigma^2+a_\delta^2(U_\sigma d\sigma+U_\xi d\xi)^2,
\qquad \det g=a_\delta^2 U_\xi^2>0.
$$

入口图是 $U_0(\xi)$。atlas 在出口后可选择一个明确定义的正目标 $V(\xi)$，再以径向系数对 $U_{\rm end}$ 与 $V$ 作凸组合；如果原 tail reader 使用 $u=\xi$，应明确选 $V=\xi$，如果保留 seed 图则选 $V=U_0$。本次文件只交付 coast 图，不替外部 atlas 隐式选择目标或覆盖旧 reader。

## 3. 物理与计算径向导数

`include_native=True` 时，native 中的 $n_\sigma,m_\sigma$ 仍是在固定物理 $u$ 下的导数。另返回计算图上的导数

$$
\partial_\sigma n|_\xi=\partial_\sigma n|_u+U_\sigma n_u,
\qquad n_\xi=U_\xi n_u,
$$

以及 $m,l$ 的对应分量。因此在各片内部，Codazzi 的消费式为

$$
\partial_\sigma m|_\xi-\frac{U_\sigma}{U_\xi}m_\xi
=\frac{l_\xi}{aU_\xi}-2cm,
$$

$$
\partial_\sigma n|_\xi-\frac{U_\sigma}{U_\xi}n_\xi
=\frac{m_\xi}{aU_\xi}+c(l-n).
$$

这只是同一个物理方程的链式变换。实际报告也核对了此表达式；没有把计算图的径向导数直接塞回原 fixed-$u$ 方程。

## 4. 真实运行和有限谱表

运行 `99731 / a4a6f9` 自然退出 $0$，耗时 $3.290532445000281$ 秒，仍用相同的 $9$ 个 coast 位置和 $768$ 个均匀入口标签。源和全部依赖 SHA 见 [报告](2026-11-12-fd2d-k0-ruling-chart-01-report.json)，SHA256

`16880b16ae5881b286f530d862ed6689fd8c860db52c4de1513605044d2801f4`。

[chart.npz](2026-11-12-fd2d-k0-ruling-chart-01-chart.npz) 保存各点的全部二阶标量 map 与 native $l,m,n$。两镜面对称及 $\pi$ 周期误差均不超过 $8.89\times10^{-16}$。

下表的 $M$ 是对应计算角的最高整数 Fourier 波数，等价于 D2 基 $\cos(2k\cdot)$ 的 $k\le\lfloor M/2\rfloor$。误差是同一有限节点集上删去更高波数后的字段值最大误差，不是连续无限尾界。

| $M$ | 最大 $k$ | 原 fixed-seed $\phi$ | 新母线标签 $\xi$ | 改善倍数 |
| --- | --- | --- | --- | --- |
| $15$ | $7$ | $.9797199796$ | $.5802457847$ | $1.69$ |
| $31$ | $15$ | $.7000300863$ | $.2958328970$ | $2.37$ |
| $63$ | $31$ | $.5398318081$ | $.06414500175$ | $8.42$ |
| $95$ | $47$ | $.3966050370$ | $.01408959333$ | $28.15$ |
| $191$ | $95$ | $.1731387058$ | $.0001454271466$ | $1190.55$ |

这说明原材料重映射造成的角压缩确实占据了高阶表示困难的很大一部分。它也如实说明低阶 $k\le15$ 的误差仍约 $.296$，不能仅凭换图宣称低阶初猜已经满足方程。当前结果供主线在实际角向残差需要时使用，不启动第二个重复求解，也不把坐标谱改善写成强目标完成。

