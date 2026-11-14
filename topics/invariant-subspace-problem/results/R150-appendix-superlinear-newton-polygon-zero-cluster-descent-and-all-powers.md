# R150 附录：全部超线性 Newton 边、真实零簇下降与原点态幂

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。固定分数逆根与单边排核采用 normal_resume_1cf 已核结果；通用支撑函数、零簇下降和有限终止由本稿完整支付。

状态：完整证明；根代理全文独核，normal_resume_1cf 独核 Newton 终止、全部归一式、Hensel 真整除和固定深域闭图链。

范围扣除：[单有理边稿](R150-appendix-actual-fractional-inverse-roots-and-rational-newton-edges.md)已经处理一个有理最高边上的全部非零根，含任意重复簇；既有不同次数平衡剪切乘积稿已经处理指定因子分解及其相应消失阶条件。本稿允许任意标量首一多项式，用全部 Newton 边的系数数据逐层处理真实零簇，不要求预给剪切因子，也不要求非零重根附近的局部消失阶。每层都使用同一个原规范核向量和同一个实际分数逆根。

## 1. 可直接检查的系数条件及主结论

保持已付的原两行
$$
u=u_*+\sum_j(a_j+d_j^0+e_j^0)\chi_j,\qquad
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d_j^1+e_j^1)\chi_j,
\tag{1.1}
$$
其中
$$
a_j\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,
$$
$$
d_j^\nu=0\ (a_j=0),\qquad
\sum_{a_j>0}|d_j^\nu|^2/a_j<\infty,\qquad
e^\nu\in\ell^1(\mathbb C),\quad \nu=0,1.
$$
所有常数、$\psi$ 及原复 $\ell^2$ first 指数权 $w$ 任意。

设
$$
F(x,y)=y^M+\sum_{j=0}^{M-1}f_j(x)y^j,\qquad M\ge1.
\tag{1.2}
$$
置 $f_M=1$、$d_j=\deg f_j$，零多项式的次数记为 $-\infty$。要求
$$
\boxed{
f_0\ne0,\qquad
d_0>\max_{1\le j\le M}(d_j+j).
}
\tag{1.3}
$$
这等价于：$F$ 的最高普通齐次项恰为一个非零标量乘 $x^{d_0}$。特别 $d_0>M$。这是一个有限的原标量系数检验。

**定理 1。** 在 (1.1)—(1.3) 下，对全部 $\lambda\in\mathbb C$、整数 $r\ge1$ 和原复指数权 $w$，
$$
\boxed{
[F(u,v)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.4}
$$

对正主行没有额外排序、增长或尾率条件。在下降重排满足
$$
\boxed{
\liminf_{n\to\infty}
\frac{n\sum_{j>n}(a_j^*)^2}
{\left(\sum_{j\le n}a_j^*\right)^2}=0
}
\tag{1.5}
$$
的全柱分支中，(1.1) 的 $e^{i\psi}b$ 还可换成任意复行 $c$，只需
$|c_j|\le C_0a_j$。

## 2. 条件 (1.3) 精确支付全部边及其终止

对实参数 $\tau$，定义原标量支撑函数
$$
m(\tau)=\max_{0\le j\le M,\ f_j\ne0}(d_j+\tau j).
\tag{2.1}
$$
这是一条有限条仿射直线的上包络。充分大 $\tau$ 时唯一最大指标为 $j=M$；由 (1.3)，$\tau=1$ 时唯一最大指标为 $j=0$。当 $\tau$ 下降时，活动指标只能下降。

因此在从 $+\infty$ 下降到 $1$ 的过程中，恰有有限个转折
$$
\tau_1>\tau_2>\cdots>\tau_s>1.
\tag{2.2}
$$
它们都是有理数，因为每个转折由两个整系数仿射式相等给出。每个转折至少降低一个活动指标，所以 $s\le M$。

令
$$
I_i=\{j:d_j+\tau_i j=m(\tau_i)\},\qquad
h_i=\max I_i,\quad \ell_i=\min I_i.
$$
则
$$
\boxed{
h_1=M,\quad h_i>\ell_i,\quad
h_{i+1}=\ell_i\ (i<s),\quad \ell_s=0.
}
\tag{2.3}
$$
两相邻转折之间的唯一活动指标正是 $\ell_i$。多条直线同点相交时，中间指标全部归在同一个 $I_i$，不增加虚构的层。

若 $c_j$ 是 $f_j$ 的最高 $x$ 系数，定义
$$
H_i(s)=\sum_{j\in I_i}c_j s^j.
\tag{2.4}
$$
则
$$
\deg H_i=h_i,\qquad
\operatorname{ord}_{s=0}H_i=\ell_i,
$$
而非零根连同重数共有 $h_i-\ell_i$ 个。
特别最终边 $H_s$ 的常数项非零。

选一个固定正整数 $Q$，使
$$
p_i:=Q\tau_i\in\mathbb N,\qquad p_i>Q
\tag{2.5}
$$
对全部 $i$ 成立。无需各 $p_i,Q$ 互素。置
$$
\mu_i=\max_j(Qd_j+p_i j)=Qm(\tau_i).
$$
由相邻边之间同一条活动直线，准确有
$$
\boxed{
\mu_i-\mu_{i+1}=(p_i-p_{i+1})\ell_i.
}
\tag{2.6}
$$
这是后面真实零簇缩放的指数恒等式。

反过来，如果从 $y^M$ 端到非零 $y^0$ 端的完整上包络全部转折都严格大于1，则在 $\tau=1$ 必由 $j=0$ 唯一取最大，恰得 (1.3)。因此本稿的“全部超线性 Newton 边”就是 (1.3)，并未省掉底边或留下一个未计的零根分支。

若 $f_0=0$，上包络不能到达 $j=0$；若在 $\tau=1$ 有并列或更大正指标，至少有一层的斜率等于1或小于1。这两种情形都不满足本定理。

## 3. 固定的真实分数逆根和非零完整部分排除接口

采用原复加权主行稿中已付的同一共享位移：
$$
Z=X_{a+d^0}+\omega,\qquad L=Z^{-1},\qquad
Y=e^{i\psi}X_b.
\tag{3.1}
$$
$Z$ 最大增生、空谱，全部预解属于 $\mathfrak C=A'$；对全部充分大的实 $c$，两个原 first
$cZ\pm e^{-i\psi}Y$ 都最大增生。

固定 §2 的 $Q$。单有理边稿 §2 用同一个真实半群构造
$$
B=\frac1{\Gamma(1/Q)}
\int_0^\infty t^{1/Q-1}e^{-tZ}\,dt
\quad(Q>1),
\qquad B=L\quad(Q=1).
\tag{3.2}
$$
这是有界增生、单射、稠密像、拟幂零算子，属于 $\mathfrak C$，并准确满足
$$
\boxed{B^Q=L.}
\tag{3.3}
$$
其同半群 Gamma 积分的 Beta 乘法律已付；本稿所有边始终使用这个 $B$，不逐边选择形式根。

自然算子
$$
X=B^{-1}
$$
最大增生、空谱，且
$$
\operatorname{Dom}X^Q=\operatorname{Dom}Z,\qquad X^Q=Z.
\tag{3.4}
$$
每个有界 $\mathfrak C$ 元素保持其各自然幂域。

对每个整数 $p>Q$ 定义自然闭算子
$$
S_p=YB^p,\qquad
\operatorname{Dom}S_p=\{h:B^ph\in\operatorname{Dom}Y\}.
\tag{3.5}
$$
闭性来自 $Y$ 闭及 $B^p$ 有界；共同正则器给稠密域。

**已付接口 3.1。** 在固定有限放大中，不存在非零闭空间 $\mathcal M$，满足全部对角 $\mathfrak C$ 不变、$\mathcal M\subseteq\operatorname{Dom}S_p$、
$S_p\mathcal M\subseteq\mathcal M$，并且其完整部分
$J=S_p|_\mathcal M$ 有界而
$$
\sigma(J)=\{\kappa\},\qquad\kappa\ne0.
\tag{3.6}
$$
在全柱条件 (1.5) 下，更一般的任意有界可逆完整部分也被排除，且允许一般复受控辅助。

为明确这个接口与本稿的共同分母兼容，简述其已付两支：

- [幂好时间/全柱二分稿](R150-appendix-power-good-times-column-dichotomy-and-good-circle-resolvents.md)保证每个正不可和 $\ell^2$ 行至少有幂次好时间或 (1.5)。
- 好时间支的真实整预解好圆从 $Z$ 经有限有界因式传给 $X$。在假想 (3.6) 上，自然定义给 $Y=JX^p$ 于全部 $\operatorname{Dom}X^p$；原两个最大增生 first 的限制与
  $cX^Q\pm e^{-i\psi}JX^p$ 由共同正则器及最高单位公式准确识别。单有理边稿 §§4、6 的窄扇形引理排除它。
- 全柱支在准确 $\operatorname{Dom}Z^p$ 上逐次得到 $Y^Q=J^QZ^p$，原伴随深域投影回传给测试
  $1-(Z^*/\overline{\sigma_n})^p+
  z(Y^*)^Q/\overline{\sigma_n}^{\,p}$。常数项因 $p>Q$ 趋零，全部实际混合头尾三组根界及 Cauchy 回传由该稿 §7 支付。

以上证明只用整数 $p>Q$，未用互素性。它也没有把通常伴随或原反射共轭限制到 $\mathcal M$。

## 4. 原完整 Bell 同时保留全部 Newton 边

固定 $\lambda,r,w$，令
$$
D=rM,\qquad M_i=r\mu_i,\qquad
D_i=rh_i,\qquad E_i=r\ell_i.
\tag{4.1}
$$
先用原 (1.1) 的行及原指数权形成
$[F(x,y)-\lambda]^r$ 的完整混合 Bell 最大实现。
之后才在同一共同深域上作已经付清的实际有界代换
$$
x_{\rm old}=Z+H_0,\qquad
y_{\rm old}=Y+R_0Z+K_0,\qquad
H_0,R_0,K_0\in\mathfrak C.
\tag{4.2}
$$
得到有限核心多项式 $P(Z,Y)$。它关于 $Y$ 首一，次数 $D$。

对每一个权 $(Q,p_i)$，正阶 Bell 微分都严格降权；有界 $x$ 平移严格降权，$y$ 中的 $R_0x+K_0$ 也因 $p_i>Q$ 严格降权。
原常数 $\lambda$ 只降权。因此同时对全部边有
$$
\boxed{
\widehat P_i(t,s)
=t^{M_i}P(t^{-Q},t^{-p_i}s)
\in\mathfrak C[t,s],\qquad
\widehat P_i(0,s)=H_i(s)^r I.
}
\tag{4.3}
$$
这里每个 $t$ 指数都是非负整数。没有重新选择 cumulant，原普通点态幂始终保留。

最高边有 $M_1=p_1D$，所以 $\widehat P_1$ 关于 $s$ 首一、次数 $D$。相邻边的完整有限式满足
$$
\boxed{
\widehat P_i(t,t^{q_i}s)
=t^{q_iE_i}\widehat P_{i+1}(t,s),
\qquad q_i=p_i-p_{i+1}>0.
}
\tag{4.4}
$$
这是把 (2.6) 代入定义得到的精确恒等式；它包含所有低权 Bell 项。

由 (1.3)，原 $F$ 的普通总次数为 $d_0$，所以 $P$ 的普通总次数不超过 $rd_0$。这给稍后固定一次的有限原词预算。

## 5. Banach 系数因子与实际 $B$ 代入

以下所有解析系数都只在 $t=0$ 的某个邻域定义。半径允许随有限层改变。

### 5.1 单变量 Banach Hensel 与有限 Bézout

设 $Q(t,s)$ 关于 $s$ 首一、次数 $d$，系数为交换 Banach 代数 $\mathfrak C$ 中的解析函数，且
$$
Q(0,s)=\prod_{\nu=0}^m q_\nu(s),
$$
其中 $q_\nu$ 是两两互素的首一标量多项式。则在缩小 $t$ 邻域后存在同次数首一解析因子
$$
Q(t,s)=\prod_\nu Q_\nu(t,s),\qquad Q_\nu(0,s)=q_\nu(s).
\tag{5.1}
$$
并有解析系数多项式 $a_\nu$，$\deg_sa_\nu<\deg q_\nu$，使
$$
\boxed{
\sum_\nu a_\nu(t,s)\prod_{\mu\ne\nu}Q_\mu(t,s)=1.
}
\tag{5.2}
$$

完整理由如下。乘积系数映射在标量因子点的导数为
$$
(v_\nu)_\nu\longmapsto
\sum_\nu v_\nu\prod_{\mu\ne\nu}q_\mu,
\qquad \deg v_\nu<\deg q_\nu.
$$
这是有限维标量 CRT 的可逆线性映射，扩张到 Banach 系数后仍有同一个有界逆。
把乘积的二次以上余项移到右侧，在一个足够小的系数球上用该逆作压缩迭代，得到 (5.1)；迭代对 $t$ 解析并一致收敛，故因子解析。
(5.2) 的有限系数矩阵在 $t=0$ 就是同一个可逆 CRT 矩阵；小邻域中的 Neumann 逆给解析的 $a_\nu$。
各求和项的次数最多 $d-1$，等式是准确多项式恒等式，不只模 $Q$ 成立。

这里仅使用不同标量根簇的互素性，没有把多元互素误当成单位。

### 5.2 只在有界拟幂零 $B$ 上作解析代入

若 $A(t)=\sum_{n\ge0}A_nt^n$ 在0附近解析，则
$$
A[B]:=\sum_{n\ge0}A_n B^n
\tag{5.3}
$$
按算子范数收敛。确实，系数至多按某个固定指数增长，而 $B$ 拟幂零给任意小指数的幂上界。
系数与 $B$ 交换，故 (5.3) 保持加法和乘法，所得有界算子仍属于 $\mathfrak C$。

所有自然 first 和有限词域由 $\mathfrak C$ 保持，所以这些系数也保持全部后续需要的域。
本稿从不在无界 $S_p$ 上代入一个解析幂级数；每次关于 $S_p$ 的运算都是一个有限多项式。

## 6. 一次固定深域上的原核向量

反设原规范最大 Bell 核含 $f\ne0$。
将原所有倾斜 first、$Z,Y$ 纳入同一个
[R186 共同正则族](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)，取其有界单射正则器 $\mathcal R$。固定一次
$$
N\ge rd_0+3D+2,\qquad g=\mathcal R^Nf\ne0.
\tag{6.1}
$$
于是 $g$ 在所有所需长度至多 $N$ 的真实自然词域中，且原最大图与正则器交换给
$$
P(Z,Y)g=0.
\tag{6.2}
$$

对全部边置
$$
S_i=YB^{p_i}.
$$
$B$ 的全部非负幂有界且属于 $\mathfrak C$，所以 $g\in\operatorname{Dom}S_i^j$ 对 $j\le N$ 成立，所有这些自然词可以准确交换。

最高边的有限多项式等式给
$$
\boxed{
\widehat P_1[B](S_1)g=B^{M_1}P(Z,Y)g=0.
}
\tag{6.3}
$$
逐项验证只用 $B^Q=Z^{-1}$：原项 $Z^aY^b$ 的归一系数是
$B^{M_1-Qa-p_1b}$，指数由 (4.3) 非负。
原 $Z,Y$ 词的长度由 $rd_0$ 支付。

后续每次 CRT 分核的投影多项式次数小于 $D_i\le D$；再作用一个因子时总 $Y$ 次数小于 $2D$。(6.1) 已同时支付它们。
每层排除非零簇后，剩余向量将严格等于这个同一个 $g$，所以这些固定词预算不会随层数累积。

## 7. 通用零簇下降的解析恒等式

我们递归构造关于 $s$ 的有限多项式
$$
\widehat P_i(t,s)=U_i(t,s)Q_i(t,s)
\tag{7.1}
$$
使系数在 $t=0$ 附近解析，并满足
$$
\boxed{
Q_i\text{ 首一，次数 }D_i,\qquad
U_i(0,s)=c_iI,\quad c_i\in\mathbb C\setminus\{0\},
\qquad
Q_i(0,s)=c_i^{-1}H_i(s)^rI.
}
\tag{7.2}
$$
初始 $U_1=I$、$Q_1=\widehat P_1$，所以成立。

假设第 $i$ 层成立。按 $H_i$ 的不同非零根分簇，§5.1 给
$$
Q_i(t,s)=R_i(t,s)\prod_{\kappa\ne0}P_{i,\kappa}(t,s),
\tag{7.3}
$$
其中
$$
R_i(0,s)=s^{E_i},\qquad
P_{i,\kappa}(0,s)=(s-\kappa)^{d_{i,\kappa}},
\qquad
\sum_{\kappa\ne0}d_{i,\kappa}=D_i-E_i.
$$
所有因子首一、系数解析。$E_i=0$ 时按 $R_i=1$ 解释。

若 $i<s$，令 $q_i=p_i-p_{i+1}$，并置
$$
A_i(t,s)=
U_i(t,t^{q_i}s)
\prod_{\kappa\ne0}P_{i,\kappa}(t,t^{q_i}s).
$$
由 (7.2)—(7.3)，
$$
A_i(0,s)=c_i\prod_{\kappa\ne0}(-\kappa)^{d_{i,\kappa}}I
=:c_{i+1}I
$$
是与 $s$ 无关的非零标量单位。
(4.4) 现在成为
$$
A_i(t,s)R_i(t,t^{q_i}s)
=t^{q_iE_i}\widehat P_{i+1}(t,s).
\tag{7.4}
$$

由于 $A_i(0,s)$ 为标量单位，$A_i$ 在形式 $t$ 级数环中可逆，其每个系数都是 $s$ 的有限多项式。也可在任意固定小 $s$ 圆盘上先取足够小的 $t$ 邻域，用通常解析逆逐项比较 Taylor 系数。
因此 (7.4) 强迫
$$
\boxed{
R_i(t,t^{q_i}s)\text{ 的全部 }t^{\,j}\text{ 系数在 }j<q_iE_i
\text{ 时为零。}
}
\tag{7.5}
$$
这是每个有限 $s$ 系数的实际整除。

定义
$$
\boxed{
Q_{i+1}(t,s)
=t^{-q_iE_i}R_i(t,t^{q_i}s),\qquad
U_{i+1}(t,s)=A_i(t,s).
}
\tag{7.6}
$$
由 (7.5)，$Q_{i+1}$ 的系数仍解析；关于 $s$ 首一、次数 $E_i=D_{i+1}$。
消去 (7.4) 两边的共同标量 $t^{q_iE_i}$，得到下一层 (7.1)。
令 $t=0$ 又得 (7.2)。

特别，这一步只在解析系数环中求 $A_i$ 的局部逆以证明 Taylor 整除；后面在实际未知闭图上从不求
$U_i[B](S_i)$ 或 $A_i[B](S_{i+1})$ 的逆。

## 8. 每一非零簇都排除，零簇仍保同一原向量

归纳假设
$$
\boxed{Q_i[B](S_i)g=0.}
\tag{8.1}
$$
初始由 (6.3) 成立。

对 (7.3) 的互素因子应用 (5.2)，记有限 CRT 多项式
$$
E_{i,\nu}(t,s)
=a_{i,\nu}(t,s)\prod_{\mu\ne\nu}P_{i,\mu}(t,s),
$$
其中 $\nu=0$ 表示零因子 $P_{i,0}=R_i$，只在 $E_i>0$ 时保留。
它们满足 $\deg_sE_{i,\nu}<D_i$ 和 $\sum_\nu E_{i,\nu}=1$。

在 (6.1) 的已付深域上定义
$$
g_{i,\nu}=E_{i,\nu}[B](S_i)g.
$$
有限乘法及 (8.1) 给准确的
$$
g=\sum_\nu g_{i,\nu},\qquad
P_{i,\nu}[B](S_i)g_{i,\nu}=0.
\tag{8.2}
$$
相关总次数小于 $2D$，每一步都在同一实际词域中。

### 8.1 非零簇的真实相伴图

固定 $\kappa\ne0$，令 $d=d_{i,\kappa}$。
若 $g_{i,\kappa}\ne0$，取自然核的真实相伴图
$$
\Gamma_{i,\kappa}
=
\{(h,S_ih,\ldots,S_i^{d-1}h):
h\in\operatorname{Dom}S_i^d,\
P_{i,\kappa}[B](S_i)h=0\}.
\tag{8.3}
$$
它非零且闭：前坐标逐次用 $S_i$ 闭性，最高坐标用首一核等式控制后再用 $S_i$ 闭性。该等式的系数保持 $\operatorname{Dom}S_i$，故核向量逐次进入更深自然幂域。

因此对角 $S_i$ 在这个图上的完整部分 $J$ 由有界相伴矩阵给出。
全部对角 $\mathfrak C$ 保持这个图并与 $J$ 交换。由
$$
P_{i,\kappa}(t,s)=(s-\kappa)^dI+tV_{i,\kappa}(t,s)
$$
得到
$$
(J-\kappa I)^d=-B_\Gamma V_{i,\kappa}[B_\Gamma](J).
\tag{8.4}
$$
右侧拟幂零，因为 $B_\Gamma$ 拟幂零并与另一有界因子交换。
谱映射遂给
$$
\sigma(J)=\{\kappa\}.
$$
现在 §3 的已付接口排除这个非零图。因此
$$
\boxed{g_{i,\kappa}=0\qquad(\kappa\ne0).}
\tag{8.5}
$$
这里没有对无界 $S_i$ 使用解析函数，也没有从因子分别循环推断乘积循环。

### 8.2 不损失原深域的零簇转移

若 $E_i>0$，(8.2)、(8.5) 精确给
$$
g_{i,0}=g,\qquad R_i[B](S_i)g=0.
\tag{8.6}
$$
剩下的不是另一个只知在较浅域中的投影向量；它就是固定的原正则核向量 $g$。

对于 $i<s$，在同一深域上
$$
S_i=B^{q_i}S_{i+1}.
$$
把 (7.6) 的有限多项式恒等式代入实际 $B$，得到
$$
0=R_i[B](S_i)g
=B^{q_iE_i}Q_{i+1}[B](S_{i+1})g.
\tag{8.7}
$$
每个解析系数仅在有界 $B$ 上按范数收敛；关于 $S_{i+1}$ 的次数为
$E_i\le D$，所以 (6.1) 已付域。
$B$ 单射，故 (8.7) 推出下一层 (8.1)。

只取消了已知单射的有界 $B$ 幂；没有在未知空间上取消一个未证明可逆的高边因子。

### 8.3 最后一层确实没有零簇

由精确包络计数 (2.3)，$E_s=r\ell_s=0$。
所以最后一次 (8.2) 只有非零簇，所有项都由 (8.5) 为零，得到 $g=0$。
这与 (6.1) 的单射正则器给 $g\ne0$ 矛盾。

过程至多 $M$ 层，所有斜率均严格大于1。既未假定无穷 Puiseux 过程终止，也未留下一个由记号掩盖的底部零根。

## 9. 原点态结论及新的多边实例

以上排除的是原指定普通点态多项式的规范最大 Bell 核。
原完整 $C$ 自伴性给其像稠密；R186 的原循环指数图核心给
$$
[\mathcal P e^w]_A=\overline{\operatorname{Ran}\mathcal P}=H.
$$
因此 $\mathcal Pe^w=[F(u,v)-\lambda]^r e^w$ 循环，定理 1 证毕。

一个同时含整数边、非整数边和重复簇的例子是
$$
F_m(x,y)=(y^2-x^3)^m(y-x^2)^m+x^{5m-1},
\qquad m\ge3.
\tag{9.1}
$$
它关于 $y$ 首一、次数 $3m$，最高普通齐次项为 $x^{5m}$，满足 (1.3)。
Newton 斜率为 $2$ 与 $3/2$，共同分母可取 $Q=2$。

最高边 $p=4$ 的归一式为
$$
t^{12m}F_m(t^{-2},t^{-4}s)
=(s^2-t^2)^m(s-1)^m+t^{2m+2},
$$
所以其最高符号含真正的零簇 $s^{2m}$，单边“全部根非零”定理不能直接处理。

下一边 $p=3$ 的原归一式为
$$
t^{10m}F_m(t^{-2},t^{-3}s)
=(ts-1)^m(s^2-1)^m+t^2.
$$
在任意 $\kappa^2=1$ 处再取 $s=\kappa+tz$，第一项含 $t^m$，第二项为 $t^2$。
当 $m>2$ 时，原平衡分簇所需的 $t^m$ 消失阶真实失败。
本稿仍给
$$
\boxed{
[F_m(u,v)-\lambda]^r e^w
\text{ 对全部 }m\ge3,\lambda,r,w\text{ 循环。}
}
$$
这依靠零簇下降后非零完整部分排除，无需构造形式无界 Puiseux 分支。

## 10. 条件的真实边界

本稿允许所有有限多个超线性有理边；不要求它们有相同分母的约分形式，也不要求原多项式先按剪切因子给出。先前单边、简单根、指定平衡乘积的交集只按原来源引用。

严格的斜率条件不能在本函数类中整体删除。例如取任意允许的正主行 $u$，令
$v=u+\chi_0$。这仍在 (1.1) 的实受控骨架加有限 $\ell^1$ 余项范围内，但
$$
F(x,y)=(y-x)^2-1
\quad\Longrightarrow\quad F(u,v)=0.
$$
这个 $F$ 的斜率为1，且不满足 (1.3)。
因此一般斜率1或以下不能由已闭超线性层的结果免费推出循环性。

更精细的零/低斜率排核条件、一般复辅助在非全柱分支中的预算、原正常见证的专属源上界和普通复 Hilbert ISP 仍需继续研究。本稿新增的是 (1.3) 所刻画的全部超线性 Newton 多边形及其原完整点态幂。

## 11. 去掉关于第二变量的首一要求

本节把定理 1 的标量多项式条件进一步放宽；根代理与 normal_resume_1cf 已全文独立核查该增强。原函数范围、全部 $\lambda,r,w$、全柱支的一般复辅助范围均不改变。

### 11.1 更一般的系数条件

现在允许
$$
F(x,y)=\sum_{j=0}^M f_j(x)y^j,\qquad
M\ge1,\qquad f_M\ne0
$$
而不要求 $f_M$ 为常数。仍记 $d_j=\deg f_j$，零多项式记为 $-\infty$，只要求
$$
\boxed{
f_0\ne0,\qquad
d_0>\max_{1\le j\le M}(d_j+j).
}
\tag{11.1}
$$
等价地，任意这个 $F$ 的最高普通齐次项为非零 $c x^{d_0}$。
则定理 1 的全部循环性结论仍成立。

旧[非首一 Sylvester 稿](R150-appendix-nonmonic-second-variable-fixed-sylvester-and-point-powers.md)已经处理某些单边简单根和横截条件。本节扣除其交集；新增允许本稿全部有限超线性边、重复簇及无局部消失阶的低项。下文只归一一个真实有界系数，绝不对原无界 $f_M(Z)$ 求逆。

### 11.2 首边的最高系数是一个真实有界单位

令 $c_M=[x^{d_M}]f_M\ne0$，仍取 $D=rM$。
完整 Bell 及原有界 first 代换后，有限核心 $P(Z,Y)$ 的 $Y^D$ 系数为一个 $Z$ 的有限多项式
$$
A(Z)=c_M^rZ^{rd_M}
+\sum_{\ell<rd_M}A_\ell Z^\ell,\qquad A_\ell\in\mathfrak C.
\tag{11.2}
$$
理由是正阶 $y$ 微分必降低 $y$ 次数，不能贡献到 $Y^D$；其余 $x$ 微分和有界 $x$ 平移只能降低 $x$ 次数。$y$ 的有界仿射代换也不改变最高 $Y^D$ 系数。

§2 的包络证明不变，只把原 $d_M=0$ 换成实际 $d_M$。
仍有 $h_1=M$、$\ell_s=0$ 及全部差式 (2.6)。
首边的宏观指数现在是
$$
M_1=rQd_M+p_1D.
$$
因此 $\widehat P_1(t,s)$ 的 $s^D$ 系数为
$$
\boxed{
a(t)=t^{Qrd_M}A(t^{-Q})
=c_M^rI+\sum_{\ell<rd_M}A_\ell t^{Q(rd_M-\ell)}.
}
\tag{11.3}
$$
它是一个有限 $\mathfrak C$ 系数多项式，并且在 $t=0$ 的 Banach 解析系数环中可逆。若 $d_M=0$，直接有 $a(t)=c_M^rI$。

在本稿实际有界拟幂零 $B$ 上，
$$
a[B]=c_M^rI+B^Q C[B]
$$
其中 $C[B]\in\mathfrak C$ 与 $B$ 交换。$B^Q C[B]$ 拟幂零，故
$$
\boxed{
a[B]\text{ 是真实有界单位},\qquad
a[B]^{-1}=(a^{-1})[B]\in\mathfrak C.
}
\tag{11.4}
$$
最后一个等式由 §5.2 的范数收敛解析代入及乘法恒等式得出。这个单位保持全部所需原 first 词域。

### 11.3 只修改递推的初值

原规范核仍可用 (6.1) 中同样的固定深度正则化，因为普通总次数仍为 $d_0$。
准确有
$$
\widehat P_1[B](S_1)g=B^{M_1}P(Z,Y)g=0.
$$
现在定义
$$
\boxed{
U_1(t,s)=a(t),\qquad
Q_1(t,s)=a(t)^{-1}\widehat P_1(t,s).
}
\tag{11.5}
$$
$Q_1$ 关于 $s$ 首一、次数 $D$，系数在0附近解析，并且
$$
U_1(0,s)=c_M^r I,\qquad
Q_1(0,s)=c_M^{-r}H_1(s)^rI.
$$
所以 §7 的全部初值条件成立。
由 (11.4) 的实际有界逆，原核等式还准确给
$$
Q_1[B](S_1)g=0.
$$

从这一点起，§§7—8 的每个 Hensel 因子、有限 CRT、零簇真实整除、原向量不变和最后 $\ell_s=0$ 的终止证明完全保持。
初始只取消了有界单位 $a[B]$；后续仍仅取消有界单射 $B$ 的非负整数幂。
没有在任何未知限制上把原 $A(Z)$ 或 $f_M(Z)$ 当作有界可逆算子。

例如对 $m\ge3$，
$$
F(x,y)=(x+1)(y^2-x^3)^m(y-x^2)^m+x^{5m}
$$
的 $y^{3m}$ 系数为真正的非恒定多项式 $x+1$，最高普通齐次项为 $x^{5m+1}$，满足 (11.1)。
全部
$$
[F(u,v)-\lambda]^r e^w
$$
仍循环。其低有理边在 $Q=2,p=3$ 归一后为
$$
(1+t^2)(ts-1)^m(s^2-1)^m+t^2,
$$
所以 $m>2$ 时原非零重簇的 $t^m$ 消失阶仍真实失败。
