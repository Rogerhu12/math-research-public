# R630 — 固定物理角的动态均值尾与深边界换角

作者：parallel-model / GPT-6 Astra Pro，AI-assisted；接口方向由 root 提出。日期：2026-11-17。

**已证明的有限模型换元与字面均值微分。** 本文将 [R626](../results/R626-finite-mean-dynamic-zero-mode-tail-bvp.md) 的动态零模直接放在固定物理角 $\phi$ 中，服务当前大幅前缀的浅端数据。它不把材料角 Fourier 尾补零，不降低角求积或原 PDE 缺陷责任。实际运行由 `parallel-numerical` 的独立尾链提供；本文没有新 BVP 输出。

## 1. 固定角图及有限状态

给定固定、严格正、$2\pi$ 周期的 $\rho(\phi)$，满足

$$
\vartheta_\phi=\rho(\phi),\qquad
\frac1{2\pi}\int_0^{2\pi}\rho\,d\phi=1.
$$

$\rho$ 与径向变量和族参数的当前求解方向无关。它定义同一材料度量

$$
g=E(r)dr^2+r^2d\vartheta^2
 =E(r)dr^2+r^2\rho(\phi)^2d\phi^2,
\qquad E=1+w^2.
\tag{1.1}
$$

取

$$
\widetilde P=\rho P=\frac{h_\phi}{rw},\qquad
K=\frac{h_r}{w}-1.
\tag{1.2}
$$

在当前反射/半周对称中，固定 $\rho$ 是偶、$\pi$ 周期函数，保留

$$
\widetilde P=\sum_{j=1}^M\widetilde p_j\sin(2j\phi),\quad
K=c_\phi+\sum_{j=1}^M k_j\cos(2j\phi).
\tag{1.3}
$$

这里 $c_\phi$ 是普通物理角 Fourier 第0模，不是材料角加权均值。状态仍是 $2M+1$ 维。原物理角高度多项式在该表示中不需先重新展开成可能很长的材料角 Fourier 级数。

准确链式法则给

$$
P=\frac{\widetilde P}{\rho},\qquad
T=\partial_\vartheta P
 =\frac{\partial_\phi\widetilde P}{\rho^2}
  -\frac{\widetilde P\rho_\phi}{\rho^3},
$$
$$
U=\partial_\vartheta K-P
  =\frac{\partial_\phi K-\widetilde P}{\rho}.
\tag{1.4}
$$

这些有理角函数按同一个固定 $\rho$ 求值；没有把它们称为仍只含 $M$ 个模。

## 2. 第一行准确留在有限物理角空间

原 R69 高度兼容式等价于

$$
\boxed{
\widetilde P_x=s\partial_\phi K-(s+\ell)\widetilde P,}
\qquad s=r_x/r,\ \ell=w_x/w.
\tag{2.1}
$$

**证明。** 原式 $P_x=s\partial_\vartheta K-(s+\ell)P$ 乘上与 $x$ 无关的 $\rho$，再用 $\rho\partial_\vartheta=\partial_\phi$。证毕。

右端准确保留 (1.3) 的奇三角空间。因此无需把 $\rho^{-1}$ 的长 Fourier 尾放进动态第一行的状态。

第二行仍为

$$
F_K^{\rm full}=-\ell(2K+T)+\mathcal N(P,K,T,U),
$$
$$
\mathcal N=
\frac{EsU^2+\ell\{(K+T)^2+z(2KT+T^2-P^2)\}}{1+K+ET},
\qquad z=w^2.
\tag{2.2}
$$

由于 $T$ 本身已有 $\rho^{-1}$ 因子，有限物理角模型须投影**整条**第二行：

$$
F_K^0=\Pi_{M,n}^{\phi}F_K^{\rm full},\qquad
\bar F_K=F_K^0-Q_nF_K^0.
\tag{2.3}
$$

只投影 $\mathcal N$ 而保留一个未经表示的 $-\ell T$，不是声明的 $2M+1$ 维系统。$\Pi_{M,n}^{\phi}$ 和 $Q_n$ 采用 R626 的普通物理角等距求积与 Fourier 投影，$n>4M$；还须用足够角分辨率求值固定 $\rho$ 及 (1.4)。

## 3. 加权字面均值和完整速度式

使用 R626 的同一个无相减函数

$$
B(P,K,T,z)=\frac{A}{q(1+q)}+\frac{(1+K)T}{Sq},
$$
$$
A=2K+K^2+(1+z)P^2,\quad S=1-zP^2,
\quad D=1-zA,\quad q=\sqrt D.
\tag{3.1}
$$

完整材料角均值是

$$
\mathcal M=\frac1{2\pi}\int_0^{2\pi}\rho(\phi)B(\phi)\,d\phi.
\tag{3.2}
$$

定义一个明确的有限求积

$$
Q_{\rho,n}f=Q_n(\rho f),\qquad
m_{\rho,n}=Q_{\rho,n}B.
\tag{3.3}
$$

若 $\rho$ 是已解析到的有限三角多项式，取节点数使 $Q_n\rho=1$ 准确；否则记录实际 $Q_n\rho-1$。也可统一把 $Q_{\rho,n}$ 除以正数 $Q_n\rho$，这不改变 $m_{\rho,n}=0$ 的根或下面零模速度，因为分子分母同乘该常数；它不改变物理 $\rho$ 或材料度量。

令 $F_{\widetilde P}$ 为 (2.1) 右端，并按字面链式计算

$$
V_P=\frac{F_{\widetilde P}}\rho,\qquad
V_T=\frac{\partial_\phi F_{\widetilde P}}{\rho^2}
     -\frac{F_{\widetilde P}\rho_\phi}{\rho^3}.
\tag{3.4}
$$

其中 $\partial_\phi F_{\widetilde P}$ 对其有限系数准确求导，不调用非线性有限差分链式法则。R626 的四个稳定偏导 $B_P,B_K,B_T,B_z$ 直接复用，且

$$
\mu_{\rho,n}=Q_{\rho,n}B_K
=Q_n\!\left(\rho\frac{1+K+ET}{D^{3/2}}\right)>0
\tag{3.5}
$$

只要每个节点 $\rho,L,D>0$。定义

$$
\boxed{
(c_\phi)_x=-\frac{
 2\ell zQ_{\rho,n}B_z+
 Q_{\rho,n}(B_PV_P+B_K\bar F_K+B_TV_T)
 +\chi m_{\rho,n}}{\mu_{\rho,n}}.}
\tag{3.6}
$$

连同 $\widetilde P_x=F_{\widetilde P}$、$\bar K_x=\bar F_K$，得到显式完整状态 ODE。

**定理。** 该有限系统准确满足

$$
(m_{\rho,n})_x+\chi m_{\rho,n}=0.
\tag{3.7}
$$

**证明。** $\rho$ 固定，故 $P_x=V_P$、$T_x=V_T$、
$K_x=\bar F_K+(c_\phi)_x$、$z_x=2\ell z$。对有限和 (3.3) 普通求导，代入 (3.6) 即得。证毕。

推荐仍取 $\chi=0$，并在一个端点施加一次 $m_{\rho,n}=0$。与同一有限加权均值隐式根模型的等价、零模积分常数以及均值误差的无 $z^{-1}$ 传播，逐字沿用 R626 的证明。

**不能照抄 R626 的两个去1步骤。** 当前只有 $Q_n\bar F_K=0$，一般 $Q_{\rho,n}\bar F_K\ne0$；同样，有限求积通常不能保证 $Q_{\rho,n}V_T=0$。所以 (3.6) 保留这两个完整项。它仍未用任何 $(\langle\Omega\rangle-1)/z$ 的不稳定相减。

## 4. 几何高度、边界与实际连续残差

普通物理角高度系数 $H_j$ 对应

$$
\widetilde p_j=-\frac{2jH_j}{rw},\qquad
k_j=\frac{(H_j)_r}{w}.
\tag{4.1}
$$

因此大幅前缀在其固定物理角中的实际高度、径向一阶 jet 可直接输入，无需先对材料角做高阶 Fourier 重投影。全部分母和 PDE 的物理角尾仍须通过增加角求积节点、状态阶数及实际缺陷读出控制。

兼容时，令 $I_\phi=\partial_\phi^{-1}$ 为普通零均值周期原函数，

$$
h_\perp=rw I_\phi\widetilde P,
\qquad (h_0)_x=r_xw(1+c_\phi).
\tag{4.2}
$$

则 $h=h_0+h_\perp$ 具有 (1.2) 的实际两导数。这一高度均值规范是普通 $\phi$ 均值；若以后改用材料加权均值作状态变量，必须相应转换常数，不能仍直接套 (4.2)。

对任一实际候选定义

$$
\widetilde f_P=\widetilde P_x-sK_\phi+(s+\ell)\widetilde P.
$$

其由 (4.2) 重建的实际非均值斜率满足

$$
\frac{(h_\perp)_r}{w}
=\bar K+\frac r{r_x}I_\phi\widetilde f_P.
\tag{4.3}
$$

因此事后把有限解转几何时，要使用这个实际导数并按需要重解同一均值分支；不能把不完全兼容的 $K$ 直接当作该重建高度的导数。

对准确修正 ODE 解，原完整方程残差为

$$
\widetilde f_P=0,\qquad
f_K=\Pi_{M,n}^{\phi}F_K^{\rm full}-F_K^{\rm full}
      +\eta_{\rho,n},
$$
$$
\eta_{\rho,n}=(c_\phi)_x-Q_nF_K^0.
\tag{4.4}
$$

它包含 $-\ell T$ 的真实物理角投影尾，不只有有理源 $\mathcal N$ 的尾。径向数值候选的实际求解残差还须另加。若用有限 $m_{\rho,n}=0$，真实均值差由完整角函数 $\rho B$ 的求积误差控制，不能假设它为零。

## 5. 后续可选的稳定重排，暂不改变直接实现

下面是两个可独立声明的优化，不是直接式 (3.6) 的隐藏步骤。

第一，可用 $\psi_j=\cos(2j\phi)-\langle\rho\cos(2j\phi)\rangle$ 作非均值基，将 $c$ 改为材料加权均值。它只给每个基加常数，状态维数和 $K_\phi$ 不变；投影后减去实际加权均值可使相应 $Q_{\rho,n}\bar F_K=0$。但普通 Fourier 第0系数及 (4.2) 的高度规范必须一起换算。

第二，连续角恒等式

$$
\int_0^{2\pi}\rho T\,d\phi
=\int_0^{2\pi}\partial_\phi P\,d\phi=0
$$

允许把同一完整均值写成 $\langle\rho(B-T)\rangle$。若明确选择**另一个有限求积定义** $\widetilde m_n=Q_{\rho,n}(B-T)$，其 $T$ 偏导为 $B_T-1$，可复用 R626 的稳定差值。它与直接 $Q_{\rho,n}B$ 的差恰是 $Q_{\rho,n}T$，有限节点时一般不为零；不能未经声明替换已接受的有限模型。

当前独立实现优先采用完整 (3.6)，并以同一个固定 $\rho$ 保持加密身份。两种优化只有实际选择后才进入相应计算链。

## 6. 深端线性关系也必须换角，不能照抄物理模的对角 Robin

原轴对称尾的稳定列按**材料角** $\vartheta$ 的频率对角。$\rho$ 非恒定时，物理角 $\cos(2j\phi)$ 不是该角算子的本征函数。因此把原第 $2j$ 模的 Robin 数直接放到物理第 $j$ 行，一般是错误的边界条件。只把内部 PDE 换成 (1.4)，不能自动修正这个边界。

一个直接、可加密的选择是：对每个物理高度/斜率基，先计算其材料角 Fourier 系数，在材料角上施加真实已传播的齐次稳定行，再拉回并投影到声明的物理测试空间。变换是稠密矩阵；角求积和材料频率 cutoff 必须作为独立精度参数。若某个材料稳定列的高度分量含零，保留两分量齐次行，不除高度形成 DN 商。此选择与第3节的物理状态阶数独立，不要求把整个径向解扩大成同样长的材料谱。

另一种适合小型独立 solver 的明确线性 Galerkin 入口是有限角广义谱。令物理偶基 $b_0=1,b_j=\cos(2j\phi)$，形成同一个正求积下的矩阵

$$
G_{ij}=Q_n(\rho b_i b_j),\qquad
A_{ij}=Q_n(b'_i b'_j/\rho).
\tag{6.1}
$$

节点上 $\rho>0$ 且基采样满秩时，$G>0$，$A\ge0$，常数方向是其核。解

$$
A v_\alpha=\lambda_\alpha Gv_\alpha,
\qquad v_\alpha^TGv_\beta=\delta_{\alpha\beta},
\quad \alpha=0,\ldots,M.
\tag{6.2}
$$

取 $\lambda_0=0$ 为高度平移规范，其余 $M$ 个本征值严格正。相应有限角函数 $\psi_\alpha=\sum_i(v_\alpha)_i b_i$ 是加权 Galerkin 角 Laplace 本征函数；$\alpha\ge1$ 时 $Q_n(\rho\psi_\alpha)=0$。

**准确有限弱式的来源。** 在轴对称高度 $h_r=w$ 处，线性化高度满足

$$
(w v_r)_r+\frac{w_r}{r}\partial_\vartheta^2v=0.
$$

对物理基作材料权弱投影，得到

$$
G(w\mathbf H_r)_r-\frac{w_r}{r}A\mathbf H=0.
\tag{6.3}
$$

用 (6.2) 展开，恰为 $M$ 个标量方程

$$
(w a_{\alpha,r})_r-\lambda_\alpha\frac{w_r}{r}a_\alpha=0.
\tag{6.4}
$$

所以可以对每个**实际 $m_\alpha=\sqrt{\lambda_\alpha}$** 沿同一径向 source 传播稳定列；这些值一般不再恰等于 $2\alpha$。不能把它们偷偷取整后仍称同一个有限弱式。

设在当前深 cut，列 $(u_\alpha,v_\alpha^{\rm mom})$ 使用同一动量尺度 $\mu$，对应

$$
\frac{H_r}{H}=\frac{m_\alpha^2}{r}
 +\frac{\sqrt{12}\mu}{r^8w}
                  \frac{v_\alpha^{\rm mom}}{u_\alpha}
$$

的关系。实际实现保留无除法的行。若 $\mathbf H$ 是物理高度系数，$\mathbf K$ 是完整物理 $K$ 系数，则令

$$
a_\alpha=v_\alpha^TG\mathbf H,\qquad
d_\alpha=w v_\alpha^TG\mathbf K,
$$

施加 $M$ 个边界式

$$
\boxed{
u_\alpha d_\alpha-
\left(\frac{m_\alpha^2}{r}u_\alpha
 +\frac{\sqrt{12}\mu}{r^8w}v_\alpha^{\rm mom}\right)a_\alpha=0,
\quad 1\le\alpha\le M.}
\tag{6.5}
$$

因 $v_\alpha^TGe_0=0$，这些行不把高度常数或背景径向斜率 $w$ 误放进非均值线性条件。第3节的一个均值边界行仍另行保留。跨胞元改变 $\mu$ 时，动量分量必须按原连续 $\mu v^{\rm mom}$ 换算；不能重复乘端口倍率。

式 (6.1)–(6.5) 是一个明确、方正的**有限弱线性深边界**，不是已证明的非线性真实稳定图。加密可同时提高物理基阶数和角求积；在本征函数足够解析的低频窗，标准加权变分近似可与实际材料模/稠密拉回独立比较。若要把某次有限行宣称为完整尾的边界，仍须保留原 source 稳定列误差、此角 Galerkin 差、非线性深图余项，以及完整未表示频率。新的内部动态均值没有支付这些差额。

## 7. 当前真实物理端口的直接复现

`../scripts/parallel_20261117_prefix_physical_trace.py` 从实际接受的M112 `.992` field逐模读取ρ、P̃、K、height，不作材料谱重展开。输入SHA `b677632099a08a33f94792a06dcc37d4e0f029131069b6ff94b1cb586ebaff25`，完整输出SHA `36688dcba2bacef79d497b92a118b58141447f2630a9c735e75a63cf4aab719b`，源SHA `f596c6b062a27af85e68c2d4c3bd4544500295a7de8926407ccec0d6846ebd4a`。普通φ高度均值为 `.9703876955889461`、K第0模为 `.023119658917963193`；此前材料角均值 `.9196724087226285`、`−.09208764312352026` 不可代替它们。

调用例：

```sh
python topics/visible-flex-larger-amplitude/scripts/parallel_20261117_prefix_physical_trace.py \
  --input /workspace/scratch/16f63c8bce6b/parallel-refine0992-m112-t8.json.gz \
  --out /workspace/scratch/16f63c8bce6b/parallel-trace0992-physical-m112.json
```

raw只在仓库外。该转换保留的是实际有限前缀字段；其本身不证明前缀等距误差为零，也不签署深tail接合。
