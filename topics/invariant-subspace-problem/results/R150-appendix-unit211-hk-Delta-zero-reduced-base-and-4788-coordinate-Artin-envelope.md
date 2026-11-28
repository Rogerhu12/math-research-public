# R150：h=k、Delta 零的约化权基与 4788 维比值坐标 Artin 包络

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

**状态：完整纸面证明，无新数学执行。** 在当前正确的 $h=k,\Delta=0$ 原图，两个剩余谱因子 $F_{99},F_{300}$ 上，原两曲线的必要权基代数是约化的，且严格同构于
$$
K_{99}\times K_{300},\qquad K_d=\mathbb Q[\lambda]/(F_d),
\tag{1}
$$
维数为 $399$。在此必要代数中，$u$ 是 $\lambda$ 的唯一代数函数；这不提供尚未算出的显式恢复系数，也不重跑已冻结的联合 gcd。

原 $\Delta$ 的 $Q^2$ 系数在两个整域上同时为单位。结合原 Loww 的倒 $z$ 首一三次和 $\rho$ 首一二次，得到以下**明确变量范围**的有限 Artin 包络：
$$
\boxed{\dim_{\mathbb Q}\mathcal E\le399\cdot2\cdot3\cdot2=4788.}
\tag{2}
$$
本次的长度包括这些坐标的全部可能重数，区别于此前只计不同点的上界。

$\mathcal E$ 只覆盖 $(\lambda,u,Q,z,\rho)$ 及其唯一恢复的原 Gram、比值 $w,h,k$ 坐标；**没有把独立尺度 $U_0$ 或未列出的物理矩阵轨道计入 (2)**。若另添原 $U_0^3=-P_0$，所构造包络的长度至多 $14364$。本稿不排空 $F_{99}/F_{300}$，不处理 $\Delta\ne0$，不完成普通 Hilbert ISP。

## 1. 已完成的准确原输入

[正确十七阶覆盖](R150-appendix-unit211-h-equals-k-corrected-fixed-seventeen-lambda-cover-and-5640-points.md)给出同一点的必要多项式
$$
P(\lambda,u),\quad M_{\rm true}(\lambda,u),
\qquad
\deg_{\lambda,u}P=(28,3),\quad
\deg_{\lambda,u}M_{\rm true}=(110,14).
\tag{3}
$$
固定 Sylvester 矩阵 $S(\lambda)$ 的行依次是十四个 $u^jP$ 和三个 $u^jM_{\rm true}$，列为 $1,u,\ldots,u^{16}$。其真实行列式 $R_{17}$ 已完整返回，且只剥已付谱因子后为
$$
R_{\rm rem}=\kappa C_1^{19}C_2^{14}C_4^6F_{99}F_{300}.
\tag{4}
$$
$F_{99},F_{300}$ 是不同的 $\mathbb Q$ 不可约因子，均只出现一次。[三个小因子的独立真原排除](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)已在整个当前原图支付 $C_1C_2C_4$。

设 $\Sigma(\lambda)$ 为此处所有已付纯谱支持的乘积，包括
$$
A,\ B,\ \lambda,\ 2\lambda-1,\ S_{\rm num},\ C_1,\ C_2,\ C_4,
$$
其中
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
S_{\rm num}=(2\lambda-1)(2\lambda^2-1).
$$
每个列出的非零因子次数均小于 $99$，故在两个 $K_d$ 中都可逆。所有被实际剥除的谱因子均由这些支持覆盖。

定义暂不加入其它原条件的必要基代数
$$
\mathcal A_0=
\mathbb Q[\lambda,\Sigma^{-1},u]/(P,M_{\rm true}).
\tag{5}
$$
原所有允许坐标都必须经由它。其它已付的纯权单位和完整原方程稍后再加。

## 2. 行列式给真实理想成员，不只给点集覆盖

由恒等式
$$
\operatorname{adj}(S)S=R_{17}I_{17},
$$
取常数单项式对应的第一行，得到
$$
R_{17}(\lambda)\in(P,M_{\rm true})
\subset\mathbb Q[\lambda,u].
\tag{6}
$$
这里使用固定多项式矩阵的形式伴随身份，不需要重新计算伴随系数，也不反演临时消元主元或任何 $u$ 首项。

(4)、(6) 和 $\Sigma$ 的局部化给
$$
F_{99}F_{300}=0\quad\hbox{于 }\mathcal A_0.
\tag{7}
$$
特征零及两个真实不可约因子的不同性保证它们互素且可分。因此
$$
\mathcal A_0\simeq
\prod_{d\in\{99,300\}}K_d[u]/(P_d,M_d),
\tag{8}
$$
$P_d,M_d$ 是 (3) 在整个 $K_d$ 中的像。尚未选取任何复嵌入。

## 3. 每个完整谱域的 u 商恰为该域

把 $P$ 写成 $\sum_{j=0}^3a_j(\lambda)u^j$。由 (3)，$a_3\ne0$ 且
$$
\deg_\lambda a_3\le28<99.
$$
所以 $a_3$ 不可能被 $F_{99}$ 或 $F_{300}$ 整除；它在两个整域中都是单位。故
$$
\deg_u P_d=3.
\tag{9}
$$

在离散赋值环 $\mathbb Q[\lambda]_{(F_d)}$ 上，(4) 给
$$
\operatorname{ord}_{F_d}\det S=1.
\tag{10}
$$
矩阵的 Smith 对角中，非单位项的赋值之和为一。因此恰有一个非单位项，模 $F_d$ 后
$$
\operatorname{nullity}_{K_d}S=1.
\tag{11}
$$

下面把该秩事实准确接到整个一元理想。令 $g_d=\gcd(P_d,M_d)$，次数为 $r_d$。固定 Sylvester 映射的核由
$$
AP_d+BM_d=0,\qquad \deg A<14,\quad\deg B<3
$$
组成。写 $P_d=g_dp$、$M_d=g_dm$，其中 $(p,m)=1$。全部解恰为
$$
A=-mH,\qquad B=pH,\qquad \deg H<r_d.
$$
后一次数限制来自 (9)；它同时自动满足 $\deg A<14$，即使 $M_d$ 的次数下降也成立。若 $M_d=0$，核维为三，也符合这项计算。故核维准确等于 $r_d$，(11) 强制
$$
\deg g_d=1.
\tag{12}
$$
因而 $g_d$ 的首一式为 $u-\eta_d$，$\eta_d\in K_d$，并有
$$
K_d[u]/(P_d,M_d)\simeq K_d.
\tag{13}
$$
这证明 (1)，包括基代数的约化性与准确维数 $399$。

本节没有输出 $\eta_d$ 的显式 $\lambda$ 系数。已冻结 ad00 的实际日志仍只包含原 $P$ 三次，没有联合 gcd 返回；(13) 是新的完整纸面结构证明，不能改写旧执行状态。

## 4. 剩余两个整域上 Q 的二次头实际为单位

原定义是
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad
J=-2u(u-1)+\ell Q,\quad T_0=-2u(u-1)-\ell Q,
$$
$$
\Phi=-2(u-1)(u-2)+(1-\ell)Q,\quad
P_f=T_0(J-Q),
$$
$$
N_F=(3-4\lambda)Q+J\xi(\xi+3-2\lambda),\quad
\Delta=\Phi N_F-(2\xi+3-2\lambda)\xi P_f .
$$
[完整原 Q 纤维证明](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Q-fibers-1444-cover.md)直接展开了
$$
[Q^2]\Delta
=(1-\ell)(3-4\lambda-A)
=-\frac{2(B^2-A^3)(\lambda^2+\lambda-1)}{B^2}
=:d_2(\lambda).
\tag{14}
$$
其非零分子的次数至多八；首项非零也可由 $B^2-A^3$ 的六次首项 $8\lambda^6$ 直接看出。因此 $d_2$ 在两个 $K_d$ 中均为单位，不需要运行新的 Bézout。

于是
$$
\mathcal B_0=\mathcal A_0[Q]/(\Delta/d_2)
\tag{15}
$$
是 $\mathcal A_0$ 上自由二生成代数，维数 $798$。该结论保留 $\Delta$ 的重根，未做平方自由化。

在 $\mathcal B_0$ 中再反演原物理已付权支持，例如
$u(u-1)Q(1-Q)bcP_{02}P_f$，得到 $\mathcal B$。
这些量由原权公式在 (15) 中定义；$bc=M/(4(1-Q))$ 可先反演 $1-Q$ 再定义。有限维交换代数的任意局部化只保留部分 Artin 局部分量，故
$$
\dim_{\mathbb Q}\mathcal B\le798.
\tag{16}
$$
没有把一个新权条件当成物理单位；若某个必要分量在这个真实开集中消失，它只会减少长度。

## 5. 倒 z 三次、rho 二次与完整比值恢复

沿[完整原 Loww 纤维](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Loww-fibers-8664-cover.md)，原 $P_1$ 及均值唯一给
$$
f=-\frac{P_c+bc\Phi z}{P_f},\quad
V=\frac{Jf-G+bcz}{Q},\quad t=z/Q,
$$
$$
G=\lambda P_{02}+(u-1)T_0,\qquad
P_c=QP_{02}(\ell+T)-GT_0,\quad T=A^2/B.
\tag{17}
$$
完整原 Loww 写成
$$
L_w(z)=c_0+c_1z+c_2z^2+c_3z^3,\qquad c_j\in\mathcal B,
$$
且
$$
c_0=-\frac{2P_{02}\lambda^2(2\lambda-1)^2}{B}
\tag{18}
$$
是已付单位。全部 $c_j$ 对 $\rho$ 共轭不变，因而确在 $\mathcal B$ 中；它们由前篇完整原式定义，不需展开大系数。

当前原图已由独立真原 $t=0$ 排除支付 $z\ne0$。取 $\zeta=z^{-1}$，原必要式为首一三次
$$
\zeta^3+(c_1/c_0)\zeta^2+(c_2/c_0)\zeta+c_3/c_0=0.
\tag{19}
$$
先在 $\mathcal B$ 上添 (19)，得到长度至多 $3\cdot798=2394$ 的有限代数，再反演 $\zeta$。局部化已经是 Artin 代数的局部化，不会增加长度。

最后添
$$
\rho^2=1-Q.
\tag{20}
$$
这是首一二次，所得包络 $\mathcal E$ 满足 (2)。原 $1-Q$ 已为单位，所以 $\rho^{-1}=\rho/(1-Q)$ 也是环内元素。两个有序符号和可能的其它坐标重数完整保留。

给定这些坐标，$b,c$、$X,Y$、$A_1,r,s$ 及比值 $w,h,k$ 均由已刊同一点的有理原公式唯一恢复。其分母均在前述已付支持中。再加入剩余原 $N/P$ 方程或取原 Gram 非退化开集，只是对这个有限代数取商或作局部化，故仍不增加长度。这里没有把必要包络说成原方程的充分解。

## 6. U0 尺度的单独范围

[原 U-value atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)明确保留
$$
V=U/U_0,\qquad P_0=-U_0^3\ne0.
\tag{21}
$$
原 Gram 的共同缩放归一不等于另外把 $U_0$ 设为一。因此本稿不把 (2) 解释为含未列尺度的全部对象计数。

如果在 $\mathcal E$ 中明确添入这个原尺度，取
$$
\widetilde{\mathcal E}=\mathcal E[U_0]/(U_0^3+P_0).
\tag{22}
$$
$P_0$ 是已恢复 Gram 的原最高值，且为单位。于是 (22) 自由三生成，$U_0$ 自动为单位，故
$$
\dim_{\mathbb Q}\widetilde{\mathcal E}\le14364.
\tag{23}
$$
原 $U$ 各值由 $U_0(1,w,h,k)$ 恢复；任何剩余原物理等式或开条件仍只减少这个指定坐标包络的长度。未列出的嵌入、基变换或矩阵轨道不在 (23) 的计数范围。

同样的范围区别适用于旧 W/b0 的 $23088$：其证明给的是已列比值与 Gram 坐标的 Artin 包络；另添独立 $U_0$ 三次时，仅可直接推出相应包络长度至多 $69264$。有限三次扩张不会改变此前的维数上界，但点数或长度不能省略它。

## 7. 来源与执行边界

本稿只使用已完成的原输入定义、准确次数、完整不可约分解及显示的代数证明。

- $P$ 参数 SHA256：8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c。
- $M_{\rm true}$ 参数 SHA256：65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663。
- 十七阶源 a12ac66b99fb8bc239cd303259c21a705dd02fab；唯一已成 run46124405008/job140915684956。
- $F_{99}$ 参数 SHA256：e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e。
- $F_{300}$ 参数 SHA256：5bfbc9ddc3b558dbef77fc19cd495175a1c8ad16461e6166c44cb982a1dca7ea。

没有重跑十七阶行列式、QQ 因式、ad00 联合 gcd、Q 纤维 Bézout 或冻结 Loww 结果式。两个剩余域的全部原值条件及整个 $\Delta\ne0$ 继续开放。
