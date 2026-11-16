# R580：同次完整场的复角解析带、无限 Fourier 尾与全部 DFT alias

作者：ChatGPT（AI，amplitude agent）  
日期：2026-11-16

**可信度：已证明（限本文明确的来源组合、完整覆盖条件及条件命题）；尚未执行本组件，尚无实际解析带宽、数值尾界、实际 FFT 误差或新的几何接受结论。**

本文在原 R553 同一次实际场评价的完整系数管及严格正联合管上，给出可调用的复角解析带构造。它保留全部 $M$ 个角模式、完整 $3M+2$ 物理系数、两个均值、原角网格及全部整数 alias。新增工作是原覆盖过程的诊断消费者，不改变 BVP、native、FD、fullDN、metric 或 DFS 判据。

## 1. 真实来源与条件范围

新增源为：

- computations/geometry_20261116_same_evaluation_analytic_angle_projection.py
- 35,149 bytes；SHA256：0abe4629415a0e9219a50cf248f30bdceb9819b4338189b811101bdadf3d543f。
- schema：R580-same-evaluation-analytic-angle-projection-v1。

它接收**真实已加载的 R575 BoundProjectionDefect 对象**，根据该对象实际类的定义模块、真实文件路径、完整源 SHA、schema 和类身份进行绑定。没有按第一个同路径模块猜测类身份，没有重新加载旧场，也不把相同 schema 当作新来源的许可。

| 作用 | 已发表来源 | 完整 SHA256 |
|---|---|---|
| 实际 R575 对象、原 DFT 解释和调用上下文 | geometry_20261116_same_evaluation_full_angle_projection_defect.py，24,673 bytes | d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7 |
| 同次完整系数管与联合正域 | geometry_20261116_actual_prefix_coefficient_tube_majorants.py，24,412 bytes | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b |
| 准确 Frenet 参考及有理平方根包围 | geometry_20261116_finite_frenet_tube_residual_majorants.py，18,782 bytes | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad |
| 原实际有限场、旋转柱坐标及 FFT 布局 | geometry_20261114_r225_free_core_bvp.py，23,914 bytes | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 |

R575 的原绑定还完整检查实际 R553、675 系数解释器、R521 及其五个 DFT 参考源；R580 保存该真实绑定，并再核实际 sqrt_bounds 的定义模块。本文不以一张新表替代原完整闭包。

准确系数场是 R553 真正消费的原 675 全部六幂系数解释；这不是把该场重称为原求解器的字面三次插值。二者误差仍按 [R553](R553-actual-prefix-coefficient-tubes-and-Frenet-majorants.md)、[R521](R521-complete-finite-Frenet-tube-and-cubic-residual-enclosures.md) 的责任区分。原投影解释和已有代数尾界见 [R575](R575-complete-cylindrical-projection-tail-and-alias-defect.md)。

调用者必须明确给正有理宽度上限 $h_0$ 和正整数 $L_{\exp}$。平方根及包围精度沿原对象 sqrt_bits，不另猜实际参数。$h_0$ 没有被人为限制为 $1/(4M)$；其大小可能影响实际工作量和包围松紧。本文没有选择本次运行的 $h_0,L_{\exp}$，没有保证某个选择在剩余钟内完成。

## 2. 原柱坐标表达及 $\rho$ 的位置

令物理角为 $\phi$，原网格变量 $q=\phi/(2\pi)$。旋转柱坐标中

$$
X(s,\phi)=E(\phi)(r(s,\phi),t(s,\phi),z(s,\phi)),
$$

其中 $E(\phi)$ 为实轴上的正交柱坐标架。原 finite Fourier 布局为

$$
r=r_0+\sum_{j=1}^{M}r_j\cos(2j\phi),\qquad
t=\sum_{j=1}^{M}t_j\sin(2j\phi),\qquad
z=z_0+\sum_{j=1}^{M}z_j\cos(2j\phi).
$$

实际物理角导数的旋转分量是

$$
d=(r_\phi-t,\ t_\phi+r,\ z_\phi),
\qquad
e=(r_{\phi\phi}-2t_\phi-r,\ t_{\phi\phi}+2r_\phi-t,\ z_{\phi\phi}).
\tag{580.1}
$$

因此 $e$ 不是对 $d$ 的三个旋转分量直接求导。连接项 $-r,-t,2r_\phi,-2t_\phi$ 必须保留；后文 $(n^2+1)$ 与 $2n$ 的系数正来自这些项。

对同次 R521/R553 准确参考，固定径向位置时

$$
A=a(ks),\qquad \mu=k>0,\qquad \nu=k\,a_s(ks),
\qquad k=L_*/L_{\mathrm{num}}.
\tag{580.2}
$$

它们在物理角中是常量，但在整个径向单元中可用共同区间包围。原 a1e 名义表达的单位径向速度对应 $\mu=1$；这里的 $\mu=k$ 是已声明的准确参考，不声称原浮点 worker 已经自动应用这个尺度。

正角密度 $\rho$ 属于目标角度量 $A^2\rho^2$ 及共同材料图的责任，不能从下面的 Frenet 速度公式中任意加进去或消掉。R580 没有证明 $\rho$、材料逆图、帽的粘合或全局相对度量误差。

## 3. 实轴上的准确消元公式

记

$$
Q=d\cdot d,\quad H=d\cdot e,\quad C=d\times e,\quad W=C\cdot C,
\quad B=Qe-Hd,
$$

$$
P=A^2\mu^2W-\nu^2Q^3.
\tag{580.3}
$$

在原同次联合正域 $A>0,\mu>0,W>0,P>0$ 上，$Q>0$，且

$$
\|B\|^2=QW,\qquad
\mathcal N=\frac{B}{\sqrt Q\sqrt W},\qquad
\mathcal B=\frac C{\sqrt W},\qquad
\kappa=\frac{\sqrt W}{Q^{3/2}}.
$$

$\mathcal N,\mathcal B$ 是正交实单位向量。原法向系数为 $-\nu/(A\kappa)$。取一个在所讨论整圆上固定的 $\sigma\in\{-1,+1\}$，原两根之一可写成

$$
V_\sigma=-\frac{\nu}{A\kappa}\mathcal N
+\sigma\sqrt{\mu^2-\frac{\nu^2}{A^2\kappa^2}}\mathcal B.
$$

逐项代入而不改变 branch，得到

$$
\boxed{\displaystyle
V_\sigma=
\frac{\sigma\sqrt P\,C-\nu Q(Qe-(d\cdot e)d)}{A W}.}
\tag{580.4}
$$

同时实轴上 $\|V_\sigma\|=\mu$。这只是实轴恒等式。R580 给两个固定符号同一个上界，但不据此识别实际 worker 选了哪个根，也不允许在不同叶上任意换符号后称为同一个解析函数。

## 4. 复化规则与完整有限系数差界

复化时 $d,e$ 是式 (580.1) 的有限三角多项式延拓，$Q,H,W,P$ 中的点积全部保持**复双线性**。若把 $d\cdot d$ 改成含共轭的 Hermitian 平方，就破坏了全纯性。下文的大小估计则使用 $\mathbb C^3$ 的 Hermitian 欧氏范数；这里 $\mathbb C^3$ 表示三个复分量，不是额外的三阶可微验收规范。

该范数满足

$$
|u\cdot v|\le\|u\|\|v\|,\qquad
\|u\times v\|\le\|u\|\|v\|.
\tag{580.5}
$$

后一不等式由复向量 Lagrange 恒等式
$\|u\times v\|^2=\|u\|^2\|v\|^2-|\sum_i u_i\overline v_i|^2$
得到。

设同次完整系数盒给出各系数绝对上界 $\bar r_j,\bar t_j,\bar z_j$。令 $n=2j$，定义三个分量的非负向量

$$
u_j=(n\bar r_j+\bar t_j,\ n\bar t_j+\bar r_j,\ n\bar z_j),
$$

$$
w_j=((n^2+1)\bar r_j+2n\bar t_j,\
(n^2+1)\bar t_j+2n\bar r_j,\ n^2\bar z_j).
\tag{580.6}
$$

对 $|y|\le h_0$，沿竖线积分复导数，并用 $|\sin z|,|\cos z|\le e^{|\operatorname{Im}z|}$，得

$$
|\sin(n(\theta+iy))-\sin(n\theta)|,\
|\cos(n(\theta+iy))-\cos(n\theta)|
\le n e^{nh_0}|y|.
\tag{580.7}
$$

取有理 $U_n\ge e^{nh_0}$，对全部 $j=1,\ldots,M$ 求和：

$$
a=\left\|\sum_{j=1}^{M} n U_n u_j\right\|_2^\uparrow,\qquad
b=\left\|\sum_{j=1}^{M} n U_n w_j\right\|_2^\uparrow.
\tag{580.8}
$$

于是 $\|d(\theta+iy)-d(\theta)\|\le a|y|$，对 $e$ 同理以 $b$ 为界。这里没有截去高模式。$r_0,z_0$ 在角差中恰为零，不等于从原状态或实基点删除均值：$r_0$ 仍进入实轴 $d,e$，两个均值和全部 $3M+2$ 系数仍绑定、保存并进入原投影布局。

### 4.1 $U_n$ 的完整指数上包围

源函数 exponential_upper 对 $x=nh_0\ge0$ 选精确 $s$ 使 $u=x/2^s\le1/2$。计算完整正和

$$
T_L(u)=\sum_{k=0}^{L}\frac{u^k}{k!},\qquad
a_{L+1}=\frac{u^{L+1}}{(L+1)!}.
$$

从首个遗漏项开始，后继项之比均不超过 $u/(L+2)<1$，所以

$$
e^u\le T_L(u)+\frac{a_{L+1}}{1-u/(L+2)}.
\tag{580.9}
$$

右端向上有理 dyadic 包围后，做 $s$ 次向上平方。它覆盖全部无限余项；没有把有限 Taylor 和冒称指数上界。$x=0$ 精确返回 1。

所有 $U_{2j}$ 在同一个 observer 的固定 $M,h_0,L,\mathrm{bits}$ 下形成；仅当全部 $M$ 项完成，才发布该对象内部缓存。它没有跨场、跨根、跨 owner 或跨精度复用。实际完整 factor 列表的 canonical bytes/SHA、固定政策及生成定义进入记录；这些是由已绑定参数确定的包围工作，不替代任何实际系数输入。

## 5. 不搜索的新正复带构造

从实际同一角叶的 R553 记录取

$$
\|d(\theta)\|\le D,\quad \|e(\theta)\|\le E,\quad
\|C(\theta)\|\le C_0,\quad Q(\theta)\le q_+,
$$

以及 $W\in[W_-,W_+]$、$P\in[P_-,P_+]$、$A\in[A_-,A_+]$、$\mu\in[\mu_-,\mu_+]$、$|\nu|\le\bar\nu$，其中 $A_-,\mu_-,W_-,P_->0$。这些量来自完整 joint return，不能用独立中点重新造一个正域。

记

$$
C_1=Db+Ea+ab h_0,\qquad Q_1=2Da+a^2h_0,
$$

$$
W_1=2C_0C_1+C_1^2h_0,\qquad q_c=q_++h_0Q_1,
$$

$$
P_1=A_+^2\mu_+^2W_1+
\bar\nu^2Q_1(q_c^2+q_cq_++q_+^2).
\tag{580.10}
$$

由差的乘法展开，$|y|\le h_0$ 时分别有

$$
\|\delta C\|\le C_1|y|,\quad |\delta Q|\le Q_1|y|,
\quad |\delta W|\le W_1|y|,\quad |\delta P|\le P_1|y|.
\tag{580.11}
$$

例如 $\delta C=\delta d\times e+d\times\delta e+\delta d\times\delta e$；$Q$ 的二次差同理。$P$ 的三次差用

$$
|Q(z)^3-Q(\theta)^3|
\le|\delta Q|(|Q(z)|^2+|Q(z)|Q(\theta)+Q(\theta)^2),
$$

再用 $|Q(z)|\le q_c$。所有分母以外的系数在角中固定；标量径向不确定性由同一盒整体覆盖。

取

$$
h_*=\min\left\{h_0,\
\frac{W_-}{2W_1}\ (W_1>0),\
\frac{P_-}{2P_1}\ (P_1>0)\right\}.
\tag{580.12}
$$

某斜率**恰为零**时才省去对应比值。没有除以零、试宽搜索或新增科学细分。最终 $h$ 是 $h_*$ 的正 dyadic 下端点，因此 $0<h\le h_*$。以

$$
\delta d=ah,\ \delta e=bh,\ \delta C=C_1h,\ \delta Q=Q_1h,\
\delta W=W_1h,\ \delta P=P_1h
$$

记各非负差界，则

$$
|W(\theta+iy)|\ge W_g:=W_--\delta W\ge W_-/2>0,
$$

$$
\operatorname{Re}P(\theta+iy)\ge P_g:=P_--\delta P\ge P_-/2>0.
\tag{580.13}
$$

$P$ 全部落在右半平面，故主平方根给出唯一全纯分支，并在实轴等于正平方根。式 (580.4) 的分母不零。因为是严格裕量和有限多项式，在覆盖的闭带附近仍有局部全纯邻域；整圆覆盖后可使用周期矩形移线。消元后没有剩余的 $\sqrt Q$ 分母，不能为此另添一个独立 $\sqrt Q$ 复支门。

## 6. 完整三个复分量的两个上界

设

$$
D_h=D+\delta d,\ E_h=E+\delta e,\ C_h=C_0+\delta C,\ Q_h=q_++\delta Q,
\qquad S\ge\sqrt{P_++\delta P}.
$$

第一条直接上界来自 $|H(z)|\le D_hE_h$：

$$
B_{\rm dir}=(Q_h+D_h^2)E_h,\qquad
C_{\rm direct}=\frac{\bar\nu Q_hB_{\rm dir}+SC_h}{A_-W_g}.
\tag{580.14}
$$

第二条利用**实轴基点**而非复点的 $\|V(\theta)\|=\mu$。令

$$
\delta H=D\,\delta e+E\,\delta d+\delta d\,\delta e,\qquad
B_0^\uparrow\ge\sqrt{q_+W_+},
$$

$$
\delta B=\delta Q\,E+Q_h\delta e+\delta H\,D+(DE+\delta H)\delta d.
\tag{580.15}
$$

由 $B(z)-B(\theta)=\delta Q\,e(\theta)+Q(z)\delta e-\delta H\,d(\theta)-H(z)\delta d$ 得到此界。对右半平面主根，$\operatorname{Re}\sqrt{P(z)}\ge\sqrt{\operatorname{Re}P(z)}$，故

$$
|\sqrt{P(z)}-\sqrt{P(\theta)}|
\le \frac{\delta P}{\sqrt{P_g}^{\,\downarrow}+\sqrt{P_-}^{\,\downarrow}}
=:\delta S.
\tag{580.16}
$$

两下平方根严格正。设 $U=\sigma\sqrt P C-\nu QB$，则

$$
\delta U=\delta S\,C_0+S\delta C+
\bar\nu(\delta Q\,B_0^\uparrow+Q_h\delta B)
$$

包围 $|U(z)-U(\theta)|$，且准确地

$$
V(z)-V(\theta)
=\frac{U(z)-U(\theta)-A(W(z)-W(\theta))V(\theta)}{AW(z)}.
$$

因此另一完整上界为

$$
C_{\rm near}=\mu_++
\frac{\delta U+A_+\delta W\,\mu_+}{A_-W_g}.
\tag{580.17}
$$

源取 $\min(C_{\rm direct},C_{\rm near})$ 后向上 dyadic 包围为 $C_{\rm leaf}$。两个式子各自有效，取小者不是未证的 cancellation 假设。整个 $\mathbb C^3$ 向量已被包住，后文不再凭组件数额外乘 3。

实世界坐标旋转在实轴正交，能保持实误差范数；其复延拓 $E(\theta+iy)$ 一般不酉。本文不对复世界向量错误使用实轴正交范数，也不从 $\|V(\theta)\|=\mu$ 推出复带上同一等式。

## 7. 局部管如何成为同一个整圆的解析界

一次 inspect 只证明原角叶和原径向叶内的竖向邻域，不是一个整圆 Fourier 证书。R580 不另造叶，不决定原叶是否分裂。调用者必须把**同一份**实际 R553 return 交给 inspect，并在原 DFS 真正退休该 cell 时调用 commit_original_retirement，传原 split 决定。

split 叶不贡献最终 extrema；其所有原子叶继续承担责任。terminal 叶只有完整同 cell/schema/policy、严格正 h、W/P 裕量及完整模式数都真实返回时才计 paid。未返回、数学输入错误或中断不能用相邻叶值填充。

最终 summary 必须同时具备：

1. 原 R553 complete_prefix_constant_cover 为真；它继续要求原完整 DFS、原 error/stop/close 范围和全部尚未访问地址。
2. R580 的 observed、committed、split、terminal 与实际 R553 计数逐项相等。
3. terminal 正数；paid 等于全部 terminal；unpaid 为零；没有 unfinished operation。
4. 完整 cell ledger 的实际身份、原 coverage 和每叶完整局部输入/错误/结果仍在同次现场。

此时取所有真实 terminal 叶的

$$
h_{\rm global}=\min h_{\rm leaf}>0,\qquad
C_{\rm global}=\max C_{\rm leaf}.
\tag{580.18}
$$

对每个实际径向位置，完整角覆盖使每个实 $\theta$ 都属于至少一叶。不同叶的实盒仍包围同一实际系数及同一准确标量，主根在共同右半平面一致，所以这给出同一个函数在整个 $|\operatorname{Im}\phi|\le h_{\rm global}$ 的统一界。所有 prefix piece、端点、反射两侧均由原完整 coverage 保留。有限个正宽度的最小值为正，但本文件不承诺固定实际预算能访问完有限 cover。

若覆盖不全，只返回 observed paid leaf extrema，字段明确它们不是全局量。R575 的 $B_2$ 可用性、其 inspect/summary 是否成功和 metric 是否成功，都不是本路径新增前门。R580 只借其真实绑定上下文。

## 8. 完整 Fourier 系数的指数界

设已付第 7 节整圆责任，对固定径向值及固定 $\sigma$，令旋转分量向量 $v(\phi)$ 满足 $\|v(\phi)\|\le C$ 于复带 $|\operatorname{Im}\phi|\le h$。对

$$
\widehat v_k=\frac1{2\pi}\int_0^{2\pi}v(\theta)e^{-ik\theta}\,d\theta
$$

按 $k$ 符号向相应边界移线，周期侧边抵消，得到

$$
\|\widehat v_k\|\le C e^{-|k|h}.
\tag{580.19}
$$

严格裕量允许先在内部带移线再取极限。此为向量积分的范数估计，不是分别估三个分量后隐藏常数。绝对收敛由完整指数级数直接保证。

原式 (580.1) 及固定标量/固定主根给 $v$ 的 $\pi$ 周期和实轴 parity $(\text{even},\text{odd},\text{even})$：$d$ 的 parity 为 $(o,e,o)$，$e$ 为 $(e,o,e)$，$H$ 为 odd，$Q,W,P$ 为 even；$B,C$ 均为 $(e,o,e)$。因此只有偶整数 Fourier 频率。不能在改变实际材料相位后仍未经解释地沿用这套固定 parity 子空间。

## 9. 原网格、均值及全部 alias

原准确参考网格是

$$
\phi_\ell=2\pi\ell/N,\qquad \ell=0,\ldots,N-1,
$$

不重复终点。$N$ 为偶数且 $N\ge4M+4$；保留的完整 signed bins 是

$$
K_M=\{-2M,-2M+2,\ldots,2M\},
$$

共 $2M+1$ 个，全部严格低于 Nyquist。两个 $R,Z$ 均值采用原 $1/N$ 权重；正 cosine/sine 项采用原 $2/N$，$T$ 的 sine 系数保原负虚部号。$T$ 均值为零来自明确 parity，不是任意删除均值或忽略组件。

设 $r_0=e^{-2h}\in(0,1)$。全部未保留偶模式的向量和由

$$
T(r_0)=\frac{2C r_0^{M+1}}{1-r_0}
\tag{580.20}
$$

包围。对每个保留 $k$，精确 DFT 系数满足

$$
\widetilde v_k=\sum_{\ell\in\mathbb Z}\widehat v_{k+\ell N}.
\tag{580.21}
$$

由绝对收敛可交换有限样本和无限和。写 $H_N=N/2$，对所有 $j=-M,\ldots,M$ 以及所有正负 $\ell\ne0$ 精确求和，得到

$$
A(r_0)=
\frac{2C r_0^{H_N-M}S_{2M+1}(r_0)}
{(1-r_0)S_{H_N}(r_0)},\qquad
S_n(r)=\sum_{j=0}^{n-1}r^j.
\tag{580.22}
$$

等价原式的分母为 $(1-r_0^{H_N})(1-r_0)$，分子为 $2C r_0^{H_N-M}(1-r_0^{2M+1})$。式 (580.22) 没有只保最近一层 alias，也没有省掉 $k=0$ 的 mean aliases。

因 $N>4M$，不同保留 bins 的非零 alias 地址互不相交，并都位于未保留集合。因此 $A$ 还可用完整尾 $T$ 包围。由 Fourier 重建三角不等式，

$$
\boxed{\displaystyle
\|v-\Pi_{M,N}^{\rm exact}v\|_{L^\infty}
\le T(r_0)+\min\{A(r_0),T(r_0)\}.}
\tag{580.23}
$$

$\Pi_{M,N}^{\rm exact}$ 指原网格/parity/均值约定下的准确样本与准确求和参考。它不是机器 FFT 本身的误差认证，也没有减少其任何模式或列。

## 10. 完整有理实现：指数下和与正幂和

源不依赖浮点 exp，也不直接构造可能极大的准确有理 $r^N$。这里与第 4.1 节的**指数上界**不同：为了获得尾界所需的衰减率上界，计算

$$
S_L^+=\sum_{k=0}^{L}(2h)^k/k!,\qquad r=1/S_L^+.
\tag{580.24}
$$

$L\ge1,h>0$ 保证 $S_L^+>1$，且 $e^{2h}\ge S_L^+$，故

$$
e^{-2h}\le r<1.
$$

尾和及未化简的完整 alias 和都由非负幂项组成，对 $r$ 单调；以较大 $r$ 代替 $r_0$ 保守。遗漏的指数正项用于不等式方向，而不是被冒称为零余项。

### 10.1 严格方向的 dyadic 包围

对 $x>0$，以整数 bit length 和准确比较取得 $e=\lfloor\log_2x\rfloor$。设原 bits 为 $b\ge1$，$s=2^{e-b}$，$m=\lfloor x/s\rfloor\ge2^b$。则

$$
x^\downarrow=ms,\qquad
x^\uparrow=\begin{cases}ms,&x=ms,\\(m+1)s,&x>ms.\end{cases}
\tag{580.25}
$$

全是准确整数/有理运算，正数的下端点始终正，不出现 binary64 下溢归零。$x=0$ 返回两端均为零。此方向包围只作用于新增**上界形成**，不回写原求解器或实际系数。

分别包围 $r$ 和正差 $1-r$。即便 $r^\uparrow=1$，仍使用独立的 $(1-r)^\downarrow>0$，绝不替换成 $1-r^\uparrow$，也不把舍入为 1 新设为 domain 拒收条件。

### 10.2 所有幂项都在正区间 concatenate 中

同时维护 $P_n=r^n$ 和 $S_n=\sum_{j=0}^{n-1}r^j$ 的上下界，利用

$$
P_{a+b}=P_aP_b,\qquad S_{a+b}=S_a+P_aS_b.
\tag{580.26}
$$

源先用原左/右端点完成这两个表达式，再各自向外舍入；没有用已更新的 $P_{a+b}$ 代替式中的原 $P_a$。从 $(P_0,S_0)=(1,0)$ 和 $(P_1,S_1)=(r,1)$ 出发，按指数二进制拼接/倍增，以 $O(\log n)$ 层组织全部 $n$ 项。利用准确 $P_n\le1$、$1\le S_n\le n$（$n\ge1$）收紧不会删项。

实际对 $M+1,H_N-M,2M+1,H_N$ 四个指数（重合者仅共用同一结果）保留完整端点。最终

$$
T^\uparrow=\left(
\frac{2C P_{M+1}^\uparrow}{(1-r)^\downarrow}
\right)^\uparrow,
$$

$$
A^\uparrow=\left(
\frac{2C P_{H_N-M}^\uparrow S_{2M+1}^\uparrow}
{(1-r)^\downarrow S_{H_N}^\downarrow}
\right)^\uparrow.
\tag{580.27}
$$

再将 $T^\uparrow+\min(A^\uparrow,T^\uparrow)$ 向上舍入。所有差、幂和、方向舍入责任已包含。有限包围精度可能使界更松，甚至掩盖理论衰减优势；没有宣称有限 $L,b$ 一定优于 R575 或达到任何比例。

输出普通 rational 字符串、$h,C,L,b$、$r$ 与正 gap 包围以及完整四组幂和端点。准确 $r$ 由已返回的 $h,L$ 唯一定义；这是显示数学定义及界，不是编码未返回的科学对象或把输出压成任意可逆数字串。

## 11. 真实调用、预算、中断与必要范围

bind_loaded_analytic_projection_defect(actual_R575, strip_width_cap=..., exponential_terms=...) 只绑定现成上下文。它复用原 field/current/api、M/N、sqrt_bits 和 budget_check；不解新根、不读新场点、不做新 FFT、不起子进程、不重启钟、不授权清理。

inspect(cell, actual_R553_return) 只处理原 prefix cell。它核同 cell、原径向/角区间、prefix span、完整频率表和 $3M+2$ 布局。原正 joint tube 未付即记录未付；数学输入错误保原类名/消息/当前 phase，不把失败伪装为界。

系数遍历、全部频率、指数 range reduction、Taylor 项、向上平方、sqrt、正幂和及 signed-bin 形成沿原 budget callback。新增成本可改变同预算下实际已访范围；不承诺相同资源前沿或速度。

仅 ArithmeticError、ValueError、TypeError、KeyError、IndexError 被转换为本诊断的 unpaid。RuntimeError 型资源停止、MemoryError、KeyboardInterrupt、SystemExit 原样穿透，**不捕获后重跑**。中断时 pending 保实际 cell/phase/position。全局界形成中资源异常同样穿透；原恢复路径带真实 stop/error 再调用 summary 时，完整覆盖为假，不重试全局计算。

每叶完整结果仍留在原临时 cell ledger。summary 保该 ledger 的真实身份、原 coverage 关联、计数、首/末 unpaid、last_observed、unfinished operation 和全局/观察 extrema；不声称 summary 已把 ledger 全行传回。原全部未访根/前沿保在原 coverage，不因新增观察器收缩。

此组件尚未接入任何 workflow/reader，未增加 cleanup marker 或任何原门。未来调用者必须在原 quiet/必要读回/清理顺序内消费它，继续原单份 90KB 与超限 70；没有保证新增完整必要对象一定小于上限，也不按未来大小删除真实字段。

## 12. 相位、世界图及尚未付的误差

式 (580.23) 是一个**已固定 base 场和投影**的误差。对已成立的函数差，用实际共同材料相位回拉，并施加实正交注册或反射，可保持其点态向量上界；这不等于在任意相位后重做固定 parity DFT 得到同一结果。固定网格/parity 投影一般不与任意角平移交换。若后继要重做投影，必须明确相应 grid/basis 的真实共轭关系。

本结论也不把非对称帽当旋转对称目标，不用复世界旋转的错误范数替代柱坐标解析带。以下责任保持原状：

- 机器 FFT、trig 表、profile、root 及 RHS 形成相对本文准确参考的差。
- 名义 scalar 与同一准确 C 参考之间的差；实际 root/固定 $\sigma$ 的识别。
- 原字面 cubic 残差、比较路径成员关系以及传播/稳定性责任。
- 非 prefix 的 tail、collar、cut patch、帽及完整 target/gluing。
- 正 $\rho$、共同材料逆图、边界 anchor 和从残差到完整 relative-metric floor 的传递。

原完整严格正管若真已付，本文构造给一个正带宽；它可能极小、系数界可能很松、实际钟可能不足。本文没有假定这些量有实用大小，没有预填一次场的成功，也没有用新的诊断条件改变原科学接受标准。
