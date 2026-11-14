# R67 — 真实二维场的准确有限多项式与完整误差

## 结论与对象

对准确仿射点
\[
\delta_5=-7789843107295549/4611686018427387904
\]
及 frozen shared1032 网格的 segment 419，已构造并保存一个准确有限多项式
\[
P(u,\theta)=\sum_{j=0}^{52}\sum_{k=-1800}^{1800}
             c_{j,k}u^j e^{4ik\theta}.
\]
所有 \(c_{j,k}\) 均为准确 dyadic 复数，负角模由正模的准确共轭定义，零模准确为实。物理场为 \(f=d\theta/d\tau\)，\(\tau=\tau_c+hu\)，分支 \(\sigma=-1\)。

同一真实无穷场与 \(P\) 的完整误差在 \(|u|\le1\) 上已付；物理角带宽 \(s=81/10000\) 时，零、一、二阶物理角导数的加权 Fourier 范数误差分别严格小于
\[
1.269\,10^{-21},\qquad
9.147\,10^{-18},\qquad
6.710\,10^{-14}.
\tag{67.1}
\]
这些界含真实无穷原函数、目标 \(E\)、真根、全部节点及 DFT 舍入、完整角混叠、角尾和全部遗漏时间阶。

最初的宽径向球把该段列为三个可能 germ。新增的准确端点证书证明：**整个真实 segment 419 实际严格位于主 germ 内**。因此 (67.1) 对该准确点的整个本时间段真实场成立，无须在这一段补另外两个短 cap。这个加强没有改动原始三 germ 域报告或已保存 \(P\)；其他时间段及参数仍各需自己的位置门。

## 67.1 一般有限对象与节点误差引理

设 \(f(u,\theta)\) 在
\[
|u|\le R,\qquad|\operatorname{Im}\theta|\le S
\]
的邻域全纯，关于物理角 \(\theta\) 的周期是 \(\pi/2\)，且
\[
|f(u,\theta)|\le M,\qquad R>r\ge0.
\]
记
\[
f(u,\theta)=\sum_{j\ge0} b_j(\theta)u^j,\qquad
b_j(\theta)=\sum_{k\in\mathbb Z}a_{j,k}e^{4ik\theta}.
\]
Cauchy 估计给出
\[
|a_{j,k}|\le M R^{-j}e^{-4S|k|}.
\tag{67.2}
\]

在实角节点 \(\theta_\ell=\pi\ell/(2N)\) 上，有向计算给出包含真实
\(b_j(\theta_\ell)\) 的球。因为准确场在实 \(u,\theta\) 上为实，每个节点的真实时间系数也为实。选择球实部的准确 dyadic 中点 \(y_{j,\ell}\)，其误差不超过实部半径 \(\epsilon_{j,\ell}\)。令
\[
\bar\epsilon_j=N^{-1}\sum_{\ell=0}^{N-1}\epsilon_{j,\ell}.
\]
则每个准确 DFT 系数的节点误差不超过 \(\bar\epsilon_j\)。

对准确中点节点 DFT 作有向计算，得到球 \(A_{j,k}\)。保留 \(0\le k\le K<N/2\)：正模选择球的准确复中点 \(c_{j,k}\)，零模选择准确实中点，并付
\[
\eta_j=\max_{0\le k\le K}|A_{j,k}-c_{j,k}|,
\qquad e_j=\bar\epsilon_j+\eta_j.
\tag{67.3}
\]
零模的虚部置零费用包含在整个 \(|A-c|\) 内。准确实节点的 DFT、真实实场的 Fourier 系数都满足准确共轭对称；定义
\(c_{j,-k}=\overline{c_{j,k}}\) 后，同一 \(e_j\) 覆盖全部保留负模。没有要求浮点 FFT 的两个中点自动满足准确共轭。

本对象的任意精度整数／指数序列已写成 14 个 gzip 分片。每个实标量为 \(m2^e\)，整数 \(m\) 作为字符串保存；完整精确解码、形状、时间覆盖、SHA-256 和字节数均已重读。该有限 \(P\) 的准确身份独立于下面的真场误差界。

## 67.2 完整角混叠与矩形补集

对 \(|k|\le K\)，实轴 DFT 的全部非零混叠满足
\[
\left|
  a_{j,k}-\frac1N\sum_\ell b_j(\theta_\ell)e^{-4ik\theta_\ell}
\right|
\le
\frac{M}{R^j}
\frac{e^{-4S(N-|k|)}+e^{-4S(N+|k|)}}{1-e^{-4SN}}.
\tag{67.4}
\]
这是对全部正、负 \(\ell N\) 混叠的几何级数；没有只保留最近一对别名。

对物理角导数阶 \(q=0,1,2\)，设
\[
w_q(k,s)=(4|k|)^q e^{4s|k|},
\]
其中 \(q=0\) 时 \(k=0\) 的权重为一。有限时间阶 \(j<m\) 的误差由三项组成：

1. 保留模节点／舍入费
   \(\sum_{|k|\le K}w_q(k,s)e_j\)；
2. 将 (67.4) 乘同一权重后，对全部保留模求和；
3. 真角尾
   \[
   2MR^{-j}\sum_{k>K}(4k)^q e^{-4(S-s)k}.
   \]

再乘 \(r^j\) 并对 \(j<m\) 求和。全部遗漏时间阶，不论其角频是否保留，另付
\[
T_q=
M\,W_q(S-s)
\frac{(r/R)^m}{1-r/R},
\quad
W_q(d)=\sum_{k\in\mathbb Z}(4|k|)^q e^{-4d|k|}.
\tag{67.5}
\]
\(q=0,1,2\) 的这些级数均有源码所用的准确几何矩闭式。上述拆分覆盖整个时间／角频矩形补集，包括高时间阶与高角频的角落。

因此，对有限 \(P\)，所得总量 \(B_q\) 满足
\[
\sup_{|u|\le r}
\|\partial_\theta^q(f-P)(u,\cdot)\|_{\mathcal A_s}\le B_q,
\qquad 0\le s<S.
\tag{67.6}
\]
源码 `fourfold_boundary_fourier_budget.py` 实现这些有向算术；实际域假设由独立完整域报告提供，不由插值节点的“小残差”推断。

## 67.3 线性聚合的等价快捷预算

角重构预算对真实角带模数和节点误差两个输入均为非负线性。故可先计算
\[
M_{\mathrm{ret}}=
M\sum_{j=0}^{m-1}(r/R)^j
=M\frac{1-(r/R)^m}{1-r/R},
\qquad
e_{\mathrm{ret}}=\sum_{j=0}^{m-1}r^j e_j,
\tag{67.7}
\]
再以 \(M_{\mathrm{ret}},e_{\mathrm{ret}}\) 做一次角重构预算，最后加一次 (67.5)。此法与逐时间阶累加给出同一个数学上界，减少了重复指数计算。

新独立源码 `fourfold_saved_field_strip_budget.py` 只读取已完成的场报告和同一 \(P\) manifest，核对所有分片身份，再执行 (67.7)。它不改 \(P\)、不重新采样、不改变几何。已用三个时间内半径及三种导数阶与原逐阶算法交叉核对，差异仅在有向舍入级别。

同一保存对象在更窄**物理角**带的严格上界为：

| 物理角带 \(s\) | \(B_0\) | \(B_1\) | \(B_2\) |
|---:|---:|---:|---:|
| \(81/10000\) | \(1.269\,10^{-21}\) | \(9.147\,10^{-18}\) | \(6.710\,10^{-14}\) |
| \(1/256\) | \(1.422\,10^{-23}\) | \(1.213\,10^{-21}\) | \(2.070\,10^{-19}\) |
| \(1/512\) | \(1.219\,10^{-23}\) | \(8.907\,10^{-22}\) | \(1.304\,10^{-19}\) |

这些宽度不是初值 Fourier 标签 \(x\) 的带宽。把 \(P\) 复合到 \(Y(u,x)\) 前，仍须单独证明 \(Y\) 的复像落入相应物理角域。

## 67.4 准确 δ5／419 的实际单 germ 门

本段准确时间端点为
\[
\tau_a=4466727694628647/9007199254740992,\qquad
\tau_b=282639970307159/562949953421312.
\]
其整个时间区间严格位于 \((-\pi/2,\pi/2)\)，已证真根 \(t>0\)。故 \(r(\tau)=t\sin\tau\) 严格递增。若主 span 是 \([a,b]\)，只须分别证明
\[
\inf(t\sin\tau_a)>a,\qquad
\sup(t\sin\tau_b)<b.
\tag{67.8}
\]
这里两个端点分别计算，绝不先构造一个宽 Arb 球再取它的下端点。

`fourfold_phase_endpoint_germ_certificate.py` 检查准确仿射参数、根证书、实际 common knot adjacency 和所有标量合法域，然后给出
\[
[a,b]=[8173936700574847,\ 8286623314361713]/72057594037927936,
\]
以及严格余量
\[
\inf(t\sin\tau_a)-a>1.4279\,10^{-13},
\qquad
b-\sup(t\sin\tau_b)>2.7374\,10^{-4}.
\tag{67.9}
\]
因此，已有主 germ 的解析外延在整个本段实时间上就是实际场。外复时间盘中仍使用该 germ 的已证解析延拓，这正是 Cauchy 预算所需的对象。

此前三 germ 列表是一个安全但较宽的候选覆盖；它不是“实际必跨三段”的证明。新增 (67.8) 消除了本准确段的多余覆盖需求，没有向其他时间片或参数邻域推广。

## 67.5 实际执行、来源与再现

实际数值包使用 \(N=4096,K=1800,m=53\)，quarter primitive 节点 1024，320-bit Arb，外时间半径 \(R=3\)、外物理角带 \(S=1/64\)。主 germ 的真实外域模数 \(M<4.303428\)。运行 wall 274.1034 秒、进程 CPU 56.5652 秒。四个独立直接求值角点的全部保留时间系数与批量结果相容；所有准确系数分片完整重读通过。

关键身份：

- 实际场源 `fourfold_phase_actual_field_fourier_package.py`：
  `c5198dcc172d4c2ef271370d4fc9b1bf39c749f20e04835e4c39cccf7498734a`。
- 新全角／复时间域报告：
  `e1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90`。
- 已完成实际场报告：
  `b8990af160ac31055cd8afe9118706e297bdb2578398a069191b418df67744a7`。
- 准确 \(P\) manifest：
  `4b33966313c4fdde253ffca05d21a49692186d8263f9f7f069804632b22b6613`。
- 更窄物理角预算源：
  `7f733ee91cf554a22bded46bbebf294001ae06f72f511f4594306291ad8f4d7a`。
- 更窄物理角预算报告：
  `bb88e5be5a8058d0b32ff85e6907bd18f4605b8ea1cc7b1eee58bd74374a5e34`。

完整分片及来源清单见
`notes/2026-11-12-step5-exact-field-polynomial-frozen-manifest.json`。
准确保存证明、命令和详细误差分解见
`notes/2026-11-12-exact-field-polynomial-preservation.md` 与
`notes/2026-11-12-step5-reference419-actual-field-polynomial.md`。
独立审查见
`notes/2026-11-12-exact-field-polynomial-independent-audit.md`。
新增的 sharp endpoint 门独立保存为
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_sharp_single_germ.json`。

重付角带与实际 span 门的命令为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_saved_field_strip_budget.py \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_main_actual_field_narrow_strip_budget.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_endpoint_germ_certificate.py \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_sharp_single_germ.json
```

R67 提供一个实际时间段上可复用的准确二维有限场对象和完整误差。它没有支付 \(P(u,Y(u,x))\) 的有限复合误差、整条流误差、Wiener 返回映射残差或非线性 PDE 结论；这些仍由各自后续证书承担。

