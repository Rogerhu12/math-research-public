# R594：完整非线性径向加速度、准确线性化与有限角漏模

日期：2026-11-26。**以下是准确代数/微分恒等、条件主部可逆性和真实漏模误差界。** 没有执行新符号程序、ODE、优化或数值谱检验；没有声称完整有限等距解、同一固定度量精化或本题完成。

已核对 R574、R576、R587、R591、R593：R574 支付完整 Darboux 方程，R576 支付 turning 消元及实际重构，R587 支付固定度量的均值高度接口；本稿新增的是给定径向均值时**直接解全部非线性径向最高项**、其离解状态的准确导数，以及保旧完整高度的有限角方程和漏模估计。本文的 $\mathfrak a$ 不同于 R576 记作 $a=N/u$ 的正 turning 密度。

## 1. 准确背景和记号

在一个开径向带 $I\subset(0,\infty)$ 上，令 $Z(r,\theta)$ 足够光滑、关于 $\theta$ 偶且 $\pi$ 周期。尖括号是完整连续角平均。写

$$
p=Z_r,\quad q=Z_\theta,\quad t=Z_{\theta\theta},
\quad \ell=Z_{r\theta},\quad k=Z_{rr},\quad
B=\ell-q/r,
$$

$$
b=(r^2-q^2)^{1/2},\qquad
N=\frac rb+\frac{r^2pt}{b^3},\qquad
V=\frac{r^2p^2}{b^2}.                                           \tag{1}
$$

假设 $b>0,N>0$，由 R576 唯一选择

$$
E>\max_\theta V,\qquad
u=(E-V)^{1/2},\qquad
\left\langle \frac Nu\right\rangle=1.                           \tag{2}
$$

还记

$$
M=r+pt-q^2/r=\frac{b^3N}{r^2}>0,\qquad
\omega=\frac{r^2}{u^3b^3}>0,\qquad
\mathfrak a=Et+rp.                                              \tag{3}
$$

Darboux 分子及 R576 实际重构的标量残差是

$$
\mathscr D
=E(kt-B^2)+rpk-\frac{E'}2 M
=\mathfrak a k-EB^2-\frac{E'}2M,
\qquad \mathcal R=\omega\mathscr D.                              \tag{4}
$$

沿任意这样的准确高度，R576 的 turning 微分恒等给

$$
\langle\mathcal R\rangle=0,\qquad
E'=\frac{2\langle\omega[E(kt-B^2)+rpk]\rangle}
         {\langle\omega M\rangle},
\qquad \langle\omega M\rangle=\langle N/u^3\rangle>0.             \tag{5}
$$

式(5)在未解 Darboux 方程的高度上同样成立；没有先假设 $\mathscr D=0$。

本稿主结论暂在

$$
\boxed{\mathfrak a(r,\theta)<0}                                  \tag{6}
$$

的区域内。$N>0$ 或 $u>0$ **不推出**(6)。数值候选若未检查它，不能直接套用后面的普通径向方程；$\mathfrak a$ 失号也不表示整个几何机制不存在。

## 2. 给定径向均值时，直接解完整非线性加速度

设 $Z=h+f$，$\langle f\rangle=0$，$h'=-W$，其中 $W>0$ 是所选静态设计的径向均值。因此

$$
\langle p\rangle=-W,\qquad \langle k\rangle=-W'.                 \tag{7}
$$

由(4)，$\mathscr D=0$ 等价于

$$
k=\frac{EB^2+(E'/2)M}{\mathfrak a}.                              \tag{8}
$$

取平均并用(7)。因 $M>0,\mathfrak a<0$，

$$
\left\langle M/\mathfrak a\right\rangle<0,
$$

故得到唯一的完整非线性公式

$$
\boxed{
E'=
\frac{2[-W'-\langle EB^2/\mathfrak a\rangle]}
     {\langle M/\mathfrak a\rangle},
\qquad
f_{rr}=\frac{EB^2+(E'/2)M}{\mathfrak a}+W'.
}                                                               \tag{9}
$$

这里 $E$ 始终先由同一 turning 根(2)确定；没有新增一个独立的 $E$ 状态。确切地说，给定当前 $f,f_r$ 和角导数，先按(9)定义 $f_{rr}$，则它的角平均准确为0，(4)逐点为0。由(5)和 $\langle\omega M\rangle>0$，(9)中的 $E'$ 必等于(2)沿该轨迹的真实径向导数。因此这些公式在充分光滑的函数层面没有多加或少加方程。

反过来，每个满足 $\mathscr D=0$、(2)、(6)、(7)的高度都满足(9)。

轴对称核对：$f=0$ 时 $p=-W,t=B=0$，$E=1+W^2$、$M=r$、$\mathfrak a=-rW$；(9)给 $E'=2WW'$ 和 $f_{rr}=0$，没有额外几何常数。

(9)是一个含角导数和角平均的非线性偏微分方程的径向表示。它本身不证明完整无限角初值问题良定，也不证明两端边值匹配；有限角截断只产生后述有限系统。此处仍是径向度量的**静态设计**，不能将沿设计变化的 $E$ 称为固定度量精化。

## 3. 离解状态的准确二 jets Frechet 链

令扰动为 $\dot Z$，点上记

$$
\dot p=\dot Z_r,\quad \dot q=\dot Z_\theta,\quad
\dot t=\dot Z_{\theta\theta},\quad
\dot\ell=\dot Z_{r\theta},\quad \dot k=\dot Z_{rr}.
$$

下式全部用当前实际高度的至多二 jets：

$$
\dot b=-q\dot q/b,
$$

$$
\dot N=
\frac{rq\dot q}{b^3}
+\frac{r^2(t\dot p+p\dot t)}{b^3}
+\frac{3r^2ptq\dot q}{b^5},
$$

$$
\dot V=\frac{2r^2p\dot p}{b^2}
+\frac{2r^2p^2q\dot q}{b^4}.                                     \tag{10}
$$

微分(2)，其严格正分母给

$$
\boxed{
\dot E=
\frac{2\langle\dot N/u\rangle+
      \langle N\dot V/u^3\rangle}
     {\langle N/u^3\rangle},
\qquad
\dot u=\frac{\dot E-\dot V}{2u}.
}                                                               \tag{11}
$$

记 $Q=kt-B^2$，则

$$
\dot Q=t\dot k+k\dot t-2B(\dot\ell-\dot q/r),\qquad
\dot M=t\dot p+p\dot t-2q\dot q/r,                               \tag{12}
$$

$$
\dot\omega
=\omega\left[-\frac{3(\dot E-\dot V)}{2u^2}
+\frac{3q\dot q}{b^2}\right].
$$

令

$$
\mathscr B
=Q\dot E+E\dot Q+r(k\dot p+p\dot k)
-\frac{E'}2\dot M.
$$

由于(5)在当前未解状态已成立，必须微分完整 $\langle\omega\mathscr D\rangle=0$，得到

$$
\boxed{
\dot E'=
\frac{2\langle\omega\mathscr B+
                    \dot\omega\mathscr D\rangle}
     {\langle\omega M\rangle},
\qquad
\dot{\mathscr D}=\mathscr B-\frac M2\dot E',
\qquad
\dot{\mathcal R}=\omega\dot{\mathscr D}
                    +\dot\omega\mathscr D.
}                                                               \tag{13}
$$

这证明了完整当前算子的准确导数，不是轴对称主部近似。特别在 $\mathscr D\ne0$ 的迭代点，$\dot\omega\mathscr D$ 两项不能删除；仅在准确解上它们才消失。全部式(10)–(13)没有第三径向或第三角导数。

## 4. 最高径向项、显式逆和有限主矩阵

把 $\dot Z,\dot Z_r$ 及其角导数固定，只让 $\dot k=v(\theta)$ 变化。式(10)(11)(12)的 $\dot E,\dot\omega,\dot M$ 不含 $v$；(13)给准确最高项

$$
\boxed{
\mathcal T v
=\mathfrak a v-
 M\frac{\langle\omega\mathfrak a v\rangle}
        {\langle\omega M\rangle}.
}                                                               \tag{14}
$$

其像满足 $\langle\omega\mathcal T v\rangle=0$。对 $\langle v\rangle=0$，

$$
\left\langle \frac vM\,\mathcal T v\right\rangle
=\left\langle\frac{\mathfrak a}M v^2\right\rangle.                \tag{15}
$$

若固定径向截面上 $-\mathfrak a/M\ge\kappa>0$，则(15)严格负定。对于任意满足 $\langle\omega H\rangle=0$ 的目标 $H$，唯一零均值解是

$$
\boxed{
v=\frac H{\mathfrak a}
-\frac{\langle H/\mathfrak a\rangle}
       {\langle M/\mathfrak a\rangle}
 \frac M{\mathfrak a}.
}                                                               \tag{16}
$$

代回(14)直接验证：目标的加权平均为0，且所选常数恰使 $\langle v\rangle=0$。分母严格为负。由(15)和 Cauchy–Schwarz，还得

$$
\|v\|_{L^2_\theta}\le
\kappa^{-1}\|H/M\|_{L^2_\theta}.                                 \tag{17}
$$

这只是径向最高项的逆。它没有支付整个径向区间的两端匹配、小分母、无限角有界逆或全尾；尤其平端 $W\to0$ 时，$\kappa$ 不应被默认为全域正下界。

令 $\varphi_j(\theta)=\cos(2j\theta)$，$1\le j\le J$。以 $\varphi_i/M$ 测试(14)，其有限主矩阵为

$$
\boxed{
\mathsf A_{ij}
=\left\langle\frac{\mathfrak a}M
                 \varphi_i\varphi_j\right\rangle.
}                                                               \tag{18}
$$

均值项准确消失，因为 $\langle\varphi_i\rangle=0$。任意非零实向量 $c$ 满足

$$
c^\top\mathsf A c
=\left\langle\frac{\mathfrak a}M
        \left(\sum_jc_j\varphi_j\right)^2\right\rangle<0.
$$

若同上有 $\kappa$，余弦正交给 $-\mathsf A\ge(\kappa/2)I$。这是连续平均的证明，不是有限 FFT 采样自动授予的连续符号判定。

## 5. 原样保已付完整场的真实有限角非线性 ODE

给定已付的完整偶/π周期高度 $f_0(r,\theta)$，$\langle f_0\rangle=0$；它可以有无限角谱。无需将其投影成有限 Fourier 多项式。只增添

$$
f=f_0+\sum_{j=1}^J c_j(r)\varphi_j(\theta),\qquad
k_0=-W'+(f_0)_{rr}.                                             \tag{19}
$$

从当前 $c,c'$ 和 $f_0$ 的真实 jets 计算 $p,q,t,B,E,M,\mathfrak a$。采用完整低角条件

$$
\left\langle \frac{\varphi_i}{M}\mathscr D\right\rangle=0,
\quad 1\le i\le J.                                              \tag{20}
$$

把 $k=k_0+\sum_jc_j''\varphi_j$ 代入(4)。其 $E'$ 项再次准确消失，因此(20)等价于

$$
\boxed{
\sum_{j=1}^J\mathsf A_{ij}c_j''
=\left\langle\varphi_i
       \left[\frac{EB^2}{M}
       -\frac{\mathfrak a}{M}k_0\right]\right\rangle,
\quad 1\le i\le J.
}                                                               \tag{21}
$$

这是完整非线性方程的有限弱投影：所有当前 $f_0+c$ 的非线性项都在内，不是 $L_W$ 的预条件近似。$E$ 仍是原 turning 根，$E'$ 仍由同一实际高度和(5)恢复。

在任一固定有限径向带、满足 $b,N,u>0$ 与(6)的开集合内，(2)的隐函数分母严格正，(18)严格负定；右侧对有限状态光滑。因此(21)写成 $c'=v,\ v'=\mathsf A^{-1}b$ 后是通常的局部有限维 ODE。其局部解存在唯一不授全区间存在、两端匹配、全角解或几何门。

对原当前264q之类的高度取 $f_0=f_{\rm paid}$、初始 $c=0$，在增加有限修正前，整个旧场及其 jets 精确保留。后续完整 metric、非零高角残差与精确/数值端口误差仍要读；不能只保(20)的有限零数就宣称等距。

### 一个不改方程的核心状态坐标

写角频率 $m_j=2j$、$\nu_j=m_j^2-1$，对新增 $C_j=c_j$ 定义

$$
A_j=\frac{m_j^2WC_j-rWC_j'}{\nu_j}.
$$

这只是可逆的一阶坐标定义，不是假设 $C_j$ 已解齐次场。准确有

$$
C_j'=\frac{m_j^2C_j}{r}-\frac{\nu_jA_j}{rW},
$$

$$
C_j''=\nu_j\left(
 \frac{C_j'}r+\frac{W'A_j}{rW^2}
 -\frac{A_j'}{rW}\right).                                       \tag{22}
$$

在正规核心坐标 $x$ 中，$W=-z_x/r_x$。把(22)代入(20)，并乘 $r_x$，对未知 $(\nu_jA_j)_x$ 的主矩阵是

$$
\boxed{
\widetilde{\mathsf A}_{ij}
=\left\langle-\frac{\mathfrak a}{rWM}
                    \varphi_i\varphi_j\right\rangle>0.
}                                                               \tag{23}
$$

所有余项仍由完整(20)给出。若满足 R576 的核心渐近
$M\to R$、$\mathfrak a/(rW)\to-1$，则

$$
\widetilde{\mathsf A}_{ij}\longrightarrow
 \frac{\delta_{ij}}{2R}.
$$

所以这个状态坐标能移除最高项矩阵的 $W\to\infty$ 尺度；它不自动支付剩余非线性项的末端正则性或试步的核心 jets。实际 BVP 必须用真实核心口，不可仅凭这一有限主矩阵极限补造端点。

## 6. 低模已解后，真正连续高模尾如何付真实 metric

在准确有限弱条件(20)下，令

$$
H=\mathscr D/M.
$$

$H$ 是偶且π周期。假定其 Fourier 展开一致收敛，写

$$
H=h_0+H_{>J},\qquad
H_{>J}=\sum_{j>J}h_j\cos(2j\theta),
$$

因为(20)令所有 $1\le j\le J$ 系数准确为0。由(5)，

$$
0=\langle\omega M H\rangle,\qquad
h_0=-\frac{\langle\omega M H_{>J}\rangle}
          {\langle\omega M\rangle}.
$$

权 $\omega M=N/u^3$ 严格正，故

$$
\boxed{
|h_0|\le\|H_{>J}\|_\infty,\quad
\|H\|_\infty\le2\|H_{>J}\|_\infty,\quad
\|\mathcal R\|_\infty
\le2\max_\theta(N/u^3)\,\|H_{>J}\|_\infty.
}                                                               \tag{24}
$$

这里没有均值小分母，也没有将未经检验的 FFT 尾差当成右侧连续范数。

更一般地，若低模并非准确为0，可把
$\sum_{j=1}^J|h_j|+\|H_{>J}\|_\infty$ 替代(24)中的尾范数，证明完全相同。积分/离散误差须进入这些真实系数的误差界，不能先假设低模已经精确满足。

R576 的真实位置差是

$$
W_*=\Pi_{2\pi}\big[b(\Pi_\pi\mathcal R)JT\big].
$$

零均值周期原函数在周期 $P$ 上的 $L^\infty$ 算子范数至多 $P/4$：其卷积核可取周期锯齿，绝对积分正是 $P/4$，向量值也成立。此处 $\mathcal R$ π周期且均值为0；$b$ π周期，$JT$ π反周期。因此

$$
\|W_*\|_\infty
\le\frac{\pi^2}{8}\max_\theta b\,\|\mathcal R\|_\infty.           \tag{25}
$$

令 $\tau=\|H_{>J}\|_\infty$，在每个固定 $r$ 上于是有

$$
\boxed{
\delta:=\frac{\|W_*\|_\infty}{\sqrt E}
\le
\frac{\pi^2}{4}\frac{\max b}{\sqrt E}
       \max_\theta(N/u^3)\,\tau.
}                                                               \tag{26}
$$

R576 的准确实际 metric 式给

$$
\left|\frac{E_{\rm act}-E}{E}\right|\le2\delta+\delta^2,\qquad
\left|\frac{F_{\rm act}}{r\sqrt E}\right|\le\delta.
$$

将其代入二维自伴缺陷的谱范数公式，再用二维三角不等式，得到

$$
\boxed{\eta\le(1+\sqrt2)\delta+\delta^2.}                         \tag{27}
$$

(24)–(27)支付的是由**连续**高模尾和剩余低模误差导出的真实 metric 误差；它不支付曲率、单射或全对点 reach，也不会把正误差改称准确等距。

## 7. 一个明确可用而非 FFT 猜测的高模尾上界

若对某个整数 $s\ge2$，在给定径向截面有真正连续界

$$
\|\partial_\theta^s H\|_\infty\le C_s,
$$

则对 $j\ge1$ 作 $s$ 次周期分部积分，

$$
|h_j|=|2\langle H\cos(2j\theta)\rangle|
\le2^{1-s}C_s j^{-s}.
$$

求和并以积分界尾部，得到

$$
\boxed{
\|H_{>J}\|_\infty
\le\frac{2^{1-s}}{s-1}\,C_s J^{1-s}.
}                                                               \tag{28}
$$

因此能够实际证明的角导数界可直接接(26)(27)。本稿没有凭一次有限角数值结果授予 $C_s$；若用区间角包围、解析条带或其他方法，必须各自完成所需连续界。

## 8. 条件的范围和下一实际工作

在准确 R588 类平端，非径向各固定 jet 相对 $W$ 都趋零；故 $E\to1$，$\mathfrak a/(rW)\to-1$。在 R576 核心门中，$E/W^2\to1$、$f_r/W\to0$、$Wf_{\theta\theta}\to0$ 同样给 $\mathfrak a/(rW)\to-1$。这些端口条件若已准确成立，失号问题只需在余下紧致连接体继续处理；有限 seed/ODE 误差不能被这句端点渐近代付。

下一个可执行输入是保已付完整 $f_0$ 的(21)或等价(22)(23)有限角 BVP，先观察当前真实 $\mathfrak a$ 的符号和矩阵条件。原内 flat 口、核心 C²口、幅度归一和均值控制必须进入实际边界条件；不能用自由端值取消未经支付的历史。

有限弱系统或当前轴对称 Green 预条件的后端 success 都不是本题完成。完整非线性全角残差、无限尾和数值传递误差、固定最终度量、实际宏观核心、全相位嵌入/reach 仍须继续支付。

### 已登记依赖

- [R574](R574-exact-nonlinear-height-equation-and-core-flux-transversality.md)：准确 Darboux 分子和线性角模。
- [R576](R576-exact-turning-elimination-and-finite-nonlinear-height-interface.md)：唯一 turning 根、$\langle\omega\mathscr D\rangle=0$、真实重构及 metric 式。
- [R587](R587-fixed-metric-mean-height-elimination-at-flat-cap-and-core.md)：固定度量时的另一均值消元；本稿没有混淆两类设计。
- [R588](R588-quantitative-common-inner-tail-and-actual-metric-bound.md)：准确无限内尾的已付范围。
- [R591](R591-forced-flat-harmonics-and-third-order-shooting.md)、[R593](R593-exact-resonant-background-and-finite-nonresonance.md)：既有强迫与有限非共振接口，不代替本稿的完整当前导数。
