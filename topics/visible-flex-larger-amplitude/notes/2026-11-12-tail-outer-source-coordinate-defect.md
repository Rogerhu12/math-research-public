# 外 0–11 胞元：真实 source 坐标的一阶系统、连续残差与两点接口

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**状态。** 第 1–4 节是完整恒等式与残差接口推导；第 5–6 节列出当前实际证书仍须支付的输入。未运行新的径向求解，未把 109 个端点当成连续径向证明。

## 1. 使用同一个真实 source 参数

在一个原 segment 上，以 R26 的真实参数 $x$ 写背景

$$
r=r(x)>0,\qquad r_x>0,\qquad w=w(x)>0,\qquad
s=\frac{r_x}{r},\qquad \ell=(\log w)_x,\qquad E=1+w^2.
\tag{X.1}
$$

R26 同时提供 $r,r_x,\log w,\ell$ 的同函数区间；不能把不同端点/不同候选的独立数值混成一个未定义的径向函数。内部经典计算可先要求 $r,w$ 为 $C^2$、高度为 $C^3$，分段光滑时逐段处理公共迹，终端 $C^2$ 的论证另行保留。

设

$$
p=\frac{h_\theta}{r}=wP,\qquad
k=h_r=w(1+K),\qquad
T=P_\theta,\quad U=K_\theta-P,\quad
L=1+K+ET.
\tag{X.2}
$$

$K$ 包括其 mean。真实水平正分支条件为

$$
S=1-w^2P^2>0,\qquad
D=E(1-w^2P^2)-w^2(1+K)^2>0,\qquad
L>0.
\tag{X.3}
$$

R41 可在给定点或已经有同函数径向包络的面板上支付完整连接根及这些正号；它本身不提供面板的径向误差。

## 2. 完整 source-$x$ 方程

高度兼容 $\partial_r(rp)=k_\theta$ 给出

$$
\boxed{P_x=sK_\theta-(s+\ell)P.}
\tag{X.4}
$$

Darboux 方程按 $h_{rr}$ 解开为 R41.33：

$$
k_r=
\frac{E(k_\theta-p)^2/r+w w_r(1-p^2+kp_\theta)}
{k+Ep_\theta}.
\tag{X.5}
$$

将 (X.2) 代入，使用
$w_x=w\ell$、$w_r=w\ell/r_x$，再从
$k_x=w\ell(1+K)+wK_x$ 中解出 $K_x$，得到

$$
\boxed{
K_x=
\frac{E s (K_\theta-P)^2
-\ell[2K+K^2+w^2P^2+(1+K)P_\theta]}
{1+K+EP_\theta}.}
\tag{X.6}
$$

核对分子时，关键消项是

$$
1-w^2P^2+w^2(1+K)T
-(1+K)(1+K+ET)
=-2K-K^2-w^2P^2-(1+K)T.
\tag{X.7}
$$

因此 (X.4)、(X.6) 是保全部角频率和 mean 的真实一阶系统。系数直接使用 $s,\ell$，在流公式中不再除以很小的 $w$，也不先计算可能很大的 physical $w_r/w$。输入归一 $P=p/w$、$K=k/w-1$ 本身是否有界仍须实际支付。

在正分支及上述正则性下，反向满足 (X.4)、(X.6) 的场给局部 Darboux 高度；全局高度/水平 development 的周期和 cuff 条件仍由 R30/R32/R41 处理。

## 3. 旋转背景线性部分与完整二材料非线性

将 (X.6) 写为

$$
K_x=-\ell(2K+P_\theta)+\mathcal N(P,K),
\tag{X.8}
$$

则完整余项恰为

$$
\boxed{
\mathcal N=
\frac{
E s(K_\theta-P)^2+
\ell\left[(K+P_\theta)^2+
w^2(2KP_\theta+P_\theta^2-P^2)\right]}
{1+K+EP_\theta}.}
\tag{X.9}
$$

证明只需将 $-\ell(2K+T)$ 乘以公共分母，和 (X.6) 相减；所得二次项为
$K^2+2EKT+ET^2-w^2P^2$，即 (X.9) 的括号。
所以它与 R33 的两种真实材料、完整 mean 和点态逆是一致的方程，不是新的截断模型。

若 real parity 使用
$P=P_m\sin(m\theta)$、$K=K_m\cos(m\theta)$，则旋转背景的第 $m$ 模线性矩阵为

$$
\frac d{dx}
\begin{pmatrix}P_m\\K_m\end{pmatrix}
=
\begin{pmatrix}
-s-\ell&-ms\\
-m\ell&-2\ell
\end{pmatrix}
\begin{pmatrix}P_m\\K_m\end{pmatrix}.
\tag{X.10}
$$

特别是不能在 $\ell$ 变号时只保留一种稳定性图景。均值的线性部分是
$(K_0)_x=-2\ell K_0$，完整流还含 $(\mathcal N)_0$。

若采用物理扰动 $\kappa=wK$，对应第二方程的物理非线性源为

$$
f_\kappa=\frac w{r_x}\mathcal N,\qquad
\int|f_\kappa|\,dr=\int w|\mathcal N|\,dx.
\tag{X.11}
$$

真正接 R33 的缩放 $V,B$ 时，必须按其定义再做同一函数的范数变换；(X.11) 没有免费把两个不同的范数空间等同。

## 4. 连续候选的残差必须保留两行

对明确给定的径向候选 $\widehat P(x,\theta),\widehat K(x,\theta)$，定义

$$
\begin{aligned}
\mathcal R_P
&=\widehat P_x-s\widehat K_\theta+(s+\ell)\widehat P,\\
\mathcal R_K
&=\widehat K_x+\ell(2\widehat K+\widehat P_\theta)
-\mathcal N(\widehat P,\widehat K).
\end{aligned}
\tag{X.12}
$$

这是实际连续残差；仅有节点 shooting mismatch 小，或者仅在节点给 $\widehat K_x$ 换成 ODE 右端，不会自动支付 (X.12)。

若从
$\widehat h_\theta=rw\widehat P$
重建候选高度，并选择 mean 满足
$(\widehat h_0)_x=r_xw(1+\widehat K_0)$，
则对非零模有精确关系

$$
(\widehat h_\perp)_x-r_xw\widehat K_\perp
=rw\,\partial_\theta^{-1}\mathcal R_P.
\tag{X.13}
$$

这里要求 $\widehat P$ 的 mean 为零，$\partial_\theta^{-1}$ 只作用于非零模。证明为对两边取 $\theta$ 导数并使用 (X.12)，双方 mean 都为零。

把 $\widehat k=w(1+\widehat K)$ 看成独立候选径向 slope 时，另有

$$
\widehat k_r-
q(\widehat p,\widehat k,\widehat k_\theta)
=\frac w{r_x}\mathcal R_K,
\tag{X.14}
$$

其中 $q$ 是 (X.5) 的完整有理式。但若 $\mathcal R_P\ne0$，$\widehat k$ 不是重建高度的真实 $\widehat h_r$；因此 (X.14) 不能直接冒充该插值曲面的 Darboux 缺陷。其真实二阶误差还涉及 (X.13) 的径向导数，或由完整流修正的存在及正则性重新获得。

有两种合法的证书入口：

- 同时保留 $\mathcal R_P,\mathcal R_K$，给两点 Green 的**两个源列**分别付界；
- 用一个明确的高度插值及其真实径向导数定义 $P,K_\perp$，使第一行兼容恒等成立，再对完整 mean 与第二行残差付界。

当前 R29/R33 已支付的特定源列不能未经证明直接同时覆盖新出现的第一行残差。

### 角导数的量词

R41 的根误差在 $W_{\tau,1}$ 中。若后续残差需要更多角导数，必须在更高阶同一 Banach 代数里重付，或为**已知候选/已知误差**使用一个明示的条带差。例如 $0\leq\sigma<\tau$，

$$
\|\partial_\theta^2 f\|_{\sigma,1}
\leq\frac4{e^2(\tau-\sigma)^2}\|f\|_{\tau,1}.
\tag{X.15}
$$

它来自 $\sup_{t\geq0}t^2e^{-(\tau-\sigma)t}=4/[e^2(\tau-\sigma)^2]$。对已知残差付一次固定角宽损失是合法的；对每次未知函数的固定点迭代不断免费丢 strip 不是同一个 Banach 收缩。未知流仍需 R33 式连续 strip 或等价的实际算子门。

## 5. 外头两点 Green 需要补哪些真实数据

现有真列/Green 只覆盖 cell $12,\ldots,224$。R42 的幅度重标不增加外 $0,\ldots,11$ 的传递矩阵、源积分、位置顺序或边界分母。

对旋转背景预条件子，可用 (X.10) 在同一 R26 实源上补各低模真实两列。若 $T_m$ 表示 node 12 到外 cut 的完整 $2\times2$ 传递，深端的真实线性图为 $K_{12,m}=S_mP_{12,m}$，则简单 height chart 的边界分母含

$$
(T_m)_{11}+(T_m)_{12}S_m.
\tag{X.16}
$$

这个式子只是说明要核销的实际 Schur 项；它不表明当前 $S_m$ 已是非线性强中心的完整导数。实际中心非轴对称时 Fréchet 导数还会耦合频率，需要有限耦合块或一个严格的卷积扰动界。

深头当前固定 node 12 Dirichlet 的存在盒，也不自动提供对全部边界数据的统一导数。若采用同一收缩算子，须另外给边界 lift 列、域不变余量和导数界，方可用
$(I-D\mathcal T)^{-1}$ 合成真实 deep-DN 导数。

高模在深图上有由同一低参数共同决定的**两分量 trace**。不能任意固定其 cut 高度又固定完整深端两分量，得到超定的外头问题。真实强前缀与外传后产生的全高模必须共同匹配；node 12 很小的 trace 经外头可能放大，其增长要由同函数/同条带的传递与源核实际支付。

## 6. 当前执行顺序与缺口

先恢复 R26/strong M20 全部输入并真实重算丢失的 13port 包；随后 109 点只用于定位预算最紧的原 segment。下一数值对象应是该真实 $x$ 上的连续候选与 (X.12) 的包络，并据其来源补实际外头边界核。禁止以端点通过、有限 root 内部 residual 或单向深尾小量替代这些步骤。

本笔记没有放宽固定 $g$、固定完整 cut 数据的身份，也没有把有限的单时刻尾片升级为完整闭嵌入族。根 README 的幅度、reach、全时检查和同问题加密标准仍全部保留。
