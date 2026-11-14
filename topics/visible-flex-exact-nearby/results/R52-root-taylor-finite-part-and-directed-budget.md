# R52：真实根 Taylor 有限部与完整有向误差预算

2026-11-12，visible-exact-astra-f6a2。

**状态：本篇算法与误差公式已证明；当前实际 beta 的完整区间尚未付齐。**
R50 已将首相位化成一阶主密度的有限部积分。本篇把根部积分化成在真根处
计算的普通幂级数，给出舍入、根位置、无限原函数、角均值和 Taylor 余项的
分别可计算预算。实际数值的一致性不替代这些预算。

这里始终使用同一个算子、同一个 R37 零阶项和同一个四重频率约定。
fourfold_phase_beta_taylor.py 的 mp 诊断及其两份报告另存 notes；
fourfold_phase_beta_interval.py 的球算术阶段逐项记录已付和未付的门。
本篇不宣称已经得到完整反馈逆、非线性精确族或 README 的完成标准。

## 1. 真根、普通 Taylor 系数与同一个零阶项

设正侧真根为 $t$，固定根内物理距离
$$
 \rho=t-r,\qquad
 -K_0(t-\rho)=\rho\,\kappa_0(\rho)^2,\qquad \kappa_0(0)>0.
 \tag{52.1}
$$
根附近的所有标量样条均取在一个共同开 knot span 内。其多项式 germ、
三角函数及 R33 的准确无限角原函数定义该邻域的实际解析函数。
仅为 Cauchy 估计，可以把这些多项式 germ 解析延拓出这个实 span；
这不声称原来的分段样条在 span 外等于该延拓。

在 $(r,\theta)$ 坐标中写完整 R37 主密度为
$$
 \widehat A=\begin{pmatrix}a&b\\ b&\widehat c\end{pmatrix},
 \qquad \widehat c=b^2/a+K_0/(\zeta^4a),\qquad
 \omega=(K_F-K_0)/(\zeta^4a).
$$
于是 $(\rho,\theta)$ 的混合分量是 $b_\rho=-b$，并且
$$
 \mu=\sqrt{-K_0}/\zeta^2=\sqrt\rho\,\kappa,\qquad
 \kappa=\kappa_0/\zeta^2,\qquad L=\log\kappa.
 \tag{52.2}
$$
保持 R37 同一个实函数 $\ell$ 及 $\chi=1$ 的核心口径：
$$
 \widehat d=d+(\omega\ell)_\theta+\omega\ell^2.
 \tag{52.3}
$$
当前实际对称对象采用
$$
 \ell=\partial_\theta\log(F_z/r)-\partial_\theta\log|F|.
$$
它需要真实的 $F_z/r>0$，不由形式写法自动授予。根部 $r=t>0$，
该表达式等于 $F_{z,\theta}/F_z-F\cdot F_\theta/|F|^2$。

定义三个光滑函数
$$
 A=-\frac{a}{16\kappa},\qquad
 B=-\frac{aL_\rho+b_\rho L_\theta}{4\kappa},
$$
$$
 C=\frac1\kappa\left[
 d+\omega(\ell^2+\ell L_\theta)
 -\frac14\{aL_\rho^2+2b_\rho L_\rho L_\theta+\widehat cL_\theta^2\}
 \right],
 \qquad \mathscr G=A+\rho B+\rho^2C.
 \tag{52.4}
$$
R50 的角积分分部给出准确恒等式
$$
 \langle J(t-\rho,\cdot)\rangle
       =\rho^{-5/2}G(\rho),\qquad G=\langle\mathscr G\rangle .
 \tag{52.5}
$$
这里 $\langle\cdot\rangle=(2\pi)^{-1}\int_0^{2\pi}\cdot\,d\theta$。
$(\omega\ell)_\theta/\mu$ 的角积分等于
$\omega\ell L_\theta/\mu$，所以(52.4)中的交叉项是**加号**。
此步骤是在角均值后成立，不能把未经积分的零阶项擅自删掉。

写普通 Taylor 展开 $G(\rho)=\sum_{n\ge0}g_n\rho^n$。由(52.1)，
$$
 \kappa_0(\rho)^2
 =\sum_{n\ge0}\frac{(-1)^nK_0^{(n+1)}(t)}{(n+1)!}\rho^n.
 \tag{52.6}
$$
这是真根处的除法，没有相减两个近乎相等的非零浮点数再除以 $\rho$。
若有向计算在根区间内包络所有导数，则(52.6)包络同一个真根的系数。
只有在无限原函数的误差已经加入 $K_0$ 后，才能用已证无限根的
$K_0(t)=0$ 将常数项设为零。

## 2. 有限部的准确多项式公式

取 $N\ge1$，定义
$$
 I_N(\eta)=\sum_{n=0}^N
             \frac{g_n\eta^{\,n-3/2}}{n-3/2}.
 \tag{52.7}
$$
则这是 $\rho^{-5/2}\sum_{n=0}^Ng_n\rho^n$ 在 $[0,\eta]$ 上的准确
Hadamard 有限部。证明是逐项积分：仅 $n=0,1$ 有发散幂，
减去它们后留下的常数恰为(52.7)，不存在对数项。

若 $G$ 在 $|\rho|\le R$ 解析且 $|G|\le M$，$0<\eta<R$，则
$$
 \left|\operatorname{FP}\int_0^\eta\rho^{-5/2}G(\rho)\,d\rho-I_N(\eta)\right|
 \le
 \boxed{\frac{M\eta^{N-1/2}}
 {(N-1/2)R^{N+1}(1-\eta/R)}}.
 \tag{52.8}
$$
事实上 $|g_n|\le M/R^n$。对 $n\ge N+1$ 有
$n-3/2\ge N-1/2>0$，故可积分、逐项取绝对值并求几何级数。

若 $|g_n-\widetilde g_n|\le e_n$，相应系数费用为
$$
 E_{\rm coeff}(\eta)=
 \sum_{n=0}^N\frac{e_n\eta^{n-3/2}}{|n-3/2|}.
 \tag{52.9}
$$
使用球区间直接计算(52.7)即自动计入这个费用及全部基本运算舍入。
缩放变量 $u=\rho/s$ 时，存储 $G(su)=\sum h_nu^n$，其中 $h_n=s^ng_n$；
准确积分改写为
$$
 I_N(\eta)=\eta^{-3/2}
      \sum_{n=0}^N\frac{h_n(\eta/s)^n}{n-3/2}.
 \tag{52.10}
$$
缩放减少系数量级，没有改变有限部或根的定义。

## 3. 固定物理切点处理根区间

设已经证明唯一真根 $t\in[t_-,t_+]$，选一个准确有理或 dyadic 切点
$b<t_-$。记 $\eta(t)=t-b$，并要求所有这些 collar 都留在实际共同 span 内。
则
$$
 \operatorname{FP}\int_0^t\langle J(r)\rangle\,dr
 =\int_0^b\langle J(r)\rangle\,dr+
      \operatorname{FP}\int_0^{\eta(t)}\rho^{-5/2}G_t(\rho)\,d\rho.
 \tag{52.11}
$$
右侧 bulk 的区间是固定的；在第二项同时包络 $t$、$G_t$ 系数和
$\eta(t)$ 即可。各球之间的相关性即使不利用也只会扩大包络，不会遗漏真值。
不需要再把根误差乘一个发散的端点 $J$ 后作人为相消。

实际四重约定是物理频率 $n=4j$，因此 R46/R50 的 $1/j$ 相位为
$$
 \beta=\tfrac14\operatorname{FP}\int_{-t}^{t}\langle J(r)\rangle\,dr.
$$
若对象及算子确实按所写方式径向显式对称，则
$$
 \boxed{\beta=\tfrac12\left[
       \int_0^b\langle J(r)\rangle\,dr+I(\eta(t))\right]} .
 \tag{52.12}
$$
这个 $1/2$ 同时含径向两侧和四重频率因子；不能额外再乘一次 $2\pi$。

## 4. 角平均的完整误差

用归一化角 $x=4\theta$，一周期长度为 $2\pi$。假设
$\mathscr G(\rho,x)$ 在
$$
 |\rho|\le R,\qquad |\operatorname{Im}x|\le\sigma
$$
解析且绝对值不超过 $M$。令 $G_A$ 是 $A$ 个等距点的准确角均值。
Fourier 系数的移线估计给
$$
 \sup_{|\rho|\le R}|G_A(\rho)-G(\rho)|
 \le E_A:=\frac{2M e^{-\sigma A}}{1-e^{-\sigma A}}.
 \tag{52.13}
$$
证明：均匀求和仅保留角频为 $A$ 的整数倍；每个系数由两条边界分别
得到 $M e^{-\sigma|k|}$，对非零倍数求和即得。
对径向再次使用 Cauchy，$n$ 阶普通系数的角误差至多 $E_A/R^n$。
所以有限多项式部分的完整角费用可取
$$
 E_{\rm angle,N}
 =E_A\sum_{n=0}^N
      \frac{\eta^{n-3/2}}{R^n|n-3/2|}
 \le \frac{2E_A\eta^{-3/2}}{1-\eta/R}.
 \tag{52.14}
$$
加上(52.8)便同时处理未求出的径向阶和全部未求出的角模。
这里的 $M,R,\sigma$ 必须来自同一个真实复杂域；有限角采样本身不供应它们。

## 5. 无限原函数与有限 DFT 的明确预算

设单位切向量的每个柱坐标分量 $T$ 在
$$
 |\rho|\le R_0,\qquad |\operatorname{Im}x|\le\sigma_0
$$
解析且 $|T|\le M_T$。偶数 $N_0$ 点 DFT 保留
$|k|<N_0/2$，丢去两个 Nyquist 端模。记
$$
 d_0=1,\qquad d_k=(4|k|-1)^{-1}\quad(k\ne0).
 \tag{52.15}
$$
R33 原函数的柱坐标水平二乘二矩阵，其每行绝对值之和恰为 $d_k$；
竖直非零模的因子 $1/(4|k|)$ 更小，竖直均值由所定义的高度单独处理。
第 $b$ 个物理 $\theta$ 导数再付 $(4|k|+1)^b$。
这些导数始终以旋转柱坐标基表示，故该行无穷范数因子已经包括基的微分，
不再乘复旋转的因子；若改报固定 Cartesian 分量的复管范数，则另乘
$e^{|\operatorname{Im}\theta|}$。本文的双线性点积、行列式及目标角均值可在
同一旋转基中准确计算。

准确 DFT 混叠满足
$$
 |\widetilde T_k-T_k|
 \le M_T a_{N_0,k},\qquad
 a_{N_0,k}=
 \frac{2e^{-\sigma_0N_0}\cosh(\sigma_0k)}
             {1-e^{-\sigma_0N_0}}.
 \tag{52.16}
$$
这是 $\sum_{m\ne0}e^{-\sigma_0|k+mN_0|}$ 的准确几何求和。
若半径函数在径向盘上的界为 $M_a$，对 $0\le\sigma_1<\sigma_0$ 有
$$
\begin{split}
 \epsilon_b=M_aM_T\bigg[
 &\sum_{|k|<N_0/2}d_k(4|k|+1)^b
           e^{\sigma_1|k|}a_{N_0,k}\\
 &+\sum_{|k|\ge N_0/2}d_k(4|k|+1)^b
           e^{-(\sigma_0-\sigma_1)|k|}
 \bigg]
\end{split}\tag{52.17}
$$
作为 $F-F_{N_0}$ 每个柱坐标分量的
$b$ 阶物理角导数界。有限 DFT 自身的舍入由球算术另外包住。
高度是同一个准确坡度积分，无角尾误差。

为免把无限和交给未解释的数值黑箱，令 $L=N_0/2$、
$z=e^{-(\sigma_0-\sigma_1)}$。对本篇所需 $b=0,1,2$，第二行可用
$$
 \frac{2z^L}{4L-1}
   \sum_{p=0}^b\binom bp4^p S_p
$$
替代，其中
$$
 S_0=\frac1{1-z},\quad
 S_1=\frac{L}{1-z}+\frac z{(1-z)^2},\quad
 S_2=\frac{L^2}{1-z}+\frac{2Lz}{(1-z)^2}
                    +\frac{z(1+z)}{(1-z)^3}.
 \tag{52.18}
$$
证明是 $d_k\le(4L-1)^{-1}$，再对 $(4k+1)^b$ 展开并求前三个
几何矩。因而(52.17)可以完全由有限次有向基本运算和指数求值完成。

这些费用对整个径向盘一致。故真实场的第 $n$ 个普通径向系数，
与有限原函数系数的差不超过 $\epsilon_b/R_0^n$；
在 $u=\rho/s$ 变量中只需给它加入半径
$\epsilon_b(s/R_0)^n$ 的零中心实球。此后实际径向微分自动产生准确的
阶乘比，不需要把逐点尾界免费当作高径向导数尾界。

## 6. 目标曲率必须使用无限角均值

目标度量是 $g_0=E\,dr^2+a^2d\theta^2$，其中
$E=\langle F_r\cdot F_r\rangle$。在复杂径向延拓上这里是双线性平方，
不是对变量取复共轭；Fourier 计算应配对 $k$ 与 $-k$。
只有常数系数的已知实 germ 才允许丢掉计算中包络出的虚部。

若在 $|\rho|\le R_0$ 已有有限场每分量的界 $M_F$ 和
$\|F-F_{N_0}\|_\infty\le\epsilon_0$，取 $R_E<R_0$、
$h=R_0-R_E$。Cauchy 给
$$
 \|F_r-(F_{N_0})_r\|_\infty\le\epsilon_0/h,\qquad
 \|(F_{N_0})_r\|_\infty\le M_F/h.
$$
因此
$$
 \|E-E_{N_0}\|_{|\rho|\le R_E}
 \le E_*:=3\frac{\epsilon_0}{h}
          \left(2\frac{M_F}{h}+\frac{\epsilon_0}{h}\right).
 \tag{52.19}
$$
三分量逐个展开 $2F_{N_0,r}\delta F_r+(\delta F_r)^2$，然后角平均，
即得该式。第 $n$ 个普通系数误差为 $E_*/R_E^n$。

把这个误差先加入 $E$，随后在球幂级数中计算
$$
 C_0=a'E'-2a''E,\qquad K_0=C_0/(2aE^2).
 \tag{52.20}
$$
真实 $E(0)>0,a(0)>0$ 使局部级数除法合法；复杂域的下界还须另付给
(52.8)、(52.13)，不能由局部系数除法推断整个盘无零点。
匹配同一个无限对象的根证书后，才用 $K_0(t)=0$ 做(52.6)。
与此同时，(52.17)必须加入实际点上使用的 $F,F_\theta,F_{\theta\theta}$；
径向导数再从这些完整级数求出。只修 $E$ 而不修实际 $d,\zeta,\omega$
也不足以包络同一个算子的相位。

有限原函数的 $M_F$ 可以不用未证的数值最大值：由
$$
 |\widetilde T_k|\le M_T(e^{-\sigma_0|k|}+a_{N_0,k})
$$
在所有保留模上乘 $M_a d_k$ 并求和，竖直均值再加准确高度界即可。
标量多项式 $p(\rho)=\sum p_n\rho^n$ 的盘界取
$\sum|p_n|R_0^n$；对于物理 phase 的有限正弦和，
$|\sin(kx)|\le\cosh(k\sigma_0)$。故
$$
 M_T=\exp\!\left(
 \sum_k\|\beta_k\|_{R_0}\cosh(k\sigma_0)
 +\sum_k\|\gamma_k\|_{R_0}\cosh(k\sigma_0)\right)
 \tag{52.21}
$$
是全部切向量分量的统一上界。这些都是实际储存标量输入的有限表达式。

## 7. 球幂级数运算为何给正确系数

每个 binary64 输入视为其准确二进制有理值。固定 span 后，先在一个准确
dyadic 中心求 de Boor 多项式的系数，再把“真根球加缩放变量”代入。
这是同一多项式的准确恒等变换，避免将同一个根区间在多个权中反复放大。

设 $f=\sum f_nu^n$。有限阶加法和乘法分别按分量相加与卷积。
若 $f_0\ne0$，倒数由
$$
 h_0=1/f_0,\qquad
 h_n=-f_0^{-1}\sum_{k=1}^nf_kh_{n-k}
$$
递推。选定平方根分支且 $g_0^2=f_0,\ g_0\ne0$ 后，
$$
 g_n=\frac{f_n-\sum_{k=1}^{n-1}g_kg_{n-k}}{2g_0}.
 \tag{52.22}
$$
指数满足
$$
 g_0=e^{f_0},\qquad
 g_n=\frac1n\sum_{k=1}^nk f_k g_{n-k}.
$$
三角函数可由指数或其微分递推得到。逐阶归纳证明：若输入球包住真系数，
且每个基本运算向外包络，则输出球包住对应的真系数；相关性丢失只会变宽。
微分前须保留足够高阶，不能把被截掉的未知高系数当成零。

实际代码用 python-flint 的 Arb/acb_series 执行这些有向球运算，官方说明见
[python-flint：arb](https://python-flint.readthedocs.io/en/latest/arb.html) 与
[FLINT Arb 文档](https://flintlib.org/doc/arb/index.html)。
本篇的数学预算独立于这些函数的具体名称；输出仍必须记录源码、输入及
根证书哈希、精度、保留阶和每个未付门。

## 8. 从各包络组成 beta 区间

设已经有同一无限对象的 bulk 包络 $B_-\le\int_0^b\langle J\rangle\le B_+$。
设(52.10)的球结果为 $[P_-,P_+]$，其中已包括舍入、根区间及第5–6节
的无限原函数修正。对同一个 $R,\sigma,M$ 付清第4节角费用 $E_A^*$
和(52.8)的余项 $E_T$。则
$$
 \boxed{\quad
 \beta\in\tfrac12\big[
 B_-+P_--E_A^*-E_T,\
 B_++P_++E_A^*+E_T
 \big].\quad}
 \tag{52.23}
$$
若多项式阶段尚未加入某个误差，其费用必须按(52.9)再加；
不应在已经加过的系数上重复收费。式(52.23)由(52.11)–(52.14)直接相加。
它明确列出了成为实际区间所需的全部部分，没有从若干浮点输出接近推出结论。

当前同一 sym step02 的两 collar、两精度/角网格诊断给
$\beta\simeq36.801611$，完整原始值及再现命令在
notes/2026-11-12-stable-root-taylor-beta.md。它们不是(52.23)中的区间。
原始 bulk 外推失败同样保留，没有择取稳定数字掩盖旧失败。
当前正在将第5–7节的实际有向节点系数接到复杂域和 bulk 包络。
本篇不把当前图的 beta 转授给后续 D5/D8 参数图，也不代付完整传播网络、
普通源、有限低块及固定握持的非线性闭合。
