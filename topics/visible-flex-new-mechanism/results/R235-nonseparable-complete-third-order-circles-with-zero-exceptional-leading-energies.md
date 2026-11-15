# R235：不可 GL(2) 分离、完整通过三阶且消掉例外端芽两个主能量的圆

日期：2026-11-15。完整纸面存在构造；没有运行新的 profile 积分、符号目标或几何计算。本稿将 [R233 四尺度圆](R233-four-scale-moment-circles-cancel-both-exceptional-leading-energies.md) 的可分离限制去掉，保留其准确三矩、全部第三阶和两个能量身份。

**结论。** 在任意给定的正活动区间 $I=[\ell,r]\Subset(0,\infty)$ 内，存在非退化、归一、$C^\infty$ 三矩圆 $(F,G)$，同时满足：

1. 任意常数 $GL(2,\mathbb R)$ 换基都不能将其变为两个支撑不交的 profiles；
2. 对真实第三 hook $\mathfrak H$，整个限制
   $\mathfrak H|_{\mathcal P\times\operatorname{Sym}^2\mathcal P}=0$，其中 $\mathcal P=\operatorname{span}\{F,G\}$；
3. R231 的两个完整领先能量 $L_c=L_s=0$；
4. 在任何已给定的真实 $M=0,T=\kappa\mathfrak H$ 几何上，只要 I 是其共同合法 profile 区间，两个二阶和四个第三阶完整 range 均成立。

这没有支付第四阶的其余层、完整 period、全部 ruling 或有限等距族。背景几何保持固定，但最终指定目标用本稿选定的第一 profile F 定义；不声称它与 R193 原目标是同一个度量。

来源：[R50 分离圆的旧常段障碍](R50-disjoint-profile-circle-fourth-order-positive-obstruction.md)、[R183 导数分包与四槽第三阶](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R229 真实能量边界项](R229-p2-energy-boundary-identity-for-exceptional-germs.md)、[R231 完整 leading 门](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、R233。以下 $\mathcal G$ 表示 R231 的 $G_0$ 二次算子，以免与最终第二 profile G 混淆。

## 1. 旧否定的范围与本稿新增内容

R50 的严格平方定理适用于含非空标准常状态 $(k,h,\omega)=(0,1,0)$ 段的几何，且 profile 平面可正交旋回不交支撑。它允许全部二、三阶齐次 gauge，并覆盖分离平面内任意固定混合目标。R216 可将相应标准障碍续到已指明的四阶 flat 状态点。

R50 本身明确不排除改变该常段几何。因此不能只因 R233 可分离，就宣布它在 $k_e\ne0$ 的新例外 germ 上已被全局排除。不过，R233 也不提供真正不可分离的圆。本稿用两个已经各自完成三阶及两能量的完整 block，准确得到后者；不把单个新相位或未付的第四项当成解。

## 2. 固定右锚的能量加法引理

沿用

$$
\mathcal G(u,v)=\frac18\left[
4xuv-2x^2(uv'+u'v)+2x^3u'v'
+x^2J(x^2u''v''+2u'v')
\right],
$$

$$
E(U,V)=\frac14\int_I(x^2U''V''+2U'V'),\qquad
Jq(x)=\int_x^r q.
\tag{1}
$$

对任何三矩圆 $(f,g)$，记

$$
A=\mathcal G(f,f),\qquad
D=\mathcal G(g,g)-\mathcal G(f,f),\qquad
X=\mathcal G(f,g).
$$

D、X 都在两个 collar 为零；A 则保留真实左二次尾。所需能量为 $L_c=E(A,D),L_s=E(A,X)$。

**引理。** 设两个完整三矩 pair $(f_1,g_1)$、$(f_2,g_2)$ 的全部 profile 支撑分别位于不交区间 $J_1<J_2$。则

$$
L_c(f_1+f_2,g_1+g_2)=L_c(f_1,g_1)+L_c(f_2,g_2),
$$

$$
L_s(f_1+f_2,g_1+g_2)=L_s(f_1,g_1)+L_s(f_2,g_2).
\tag{2}
$$

**证明。** 原 profile 及其导数支撑不交，故
$\mathcal G(f_1,f_2)=\mathcal G(f_1,g_2)=\mathcal G(f_2,g_1)=0$ 原式成立。因而 A、D、X 分别为两 block 的和。

在 $J_2$ 上 $A_1=0$，所以 $E(A_1,D_2)=E(A_1,X_2)=0$。在 $J_1$ 上 $A_2=cx^2$，其中 c 是它的真实右方累计尾。由同锚边界式

$$
E(x^2,Z)=0
\quad\text{当 }Z\text{ 在 }J_1\text{ 两端 collar 为零},
\tag{3}
$$

得另两交叉能量为零。这证明 (2)，没有将任一 $A_i$ 伪称紧支撑。$\square$

三矩也按两个不交 block 相加。因此任何两个已分别满足三矩和 $L_c=L_s=0$ 的 pair，均可在保留真实尾的条件下合并。

## 3. 一个任意小区间内的八包 block，且旋转参数非零

R233 四尺度基本 pair 取

$$
a_i=a+i\Delta,\quad i=1,2,3,4,\qquad a>0,\quad\Delta>0,
$$

$$
v_i=\frac1{\prod_{j\ne i}(a_i-a_j)},\qquad
s_i=\operatorname{sign}v_i,\qquad w_i=|v_i|a_i^3.
$$

用一个非零实 $\psi\in C_c^\infty((1-\delta,1+\delta))$，令
$\psi_i(x)=\psi(x/a_i)$，再置

$$
f_*=\sum_i\sqrt{w_i}\,\psi_i,\qquad
g_*=\sum_i s_i\sqrt{w_i}\,\psi_i.
\tag{4}
$$

四个活动区间互不交时，这是准确三矩圆。记
$A_i=\mathcal G(\psi_i,\psi_i)$，
$S_i=\frac14\int x^4((A_i/x)'')^2$。
R233 的完整边界推导给

$$
S_i=a_iS_*,\qquad S_*>0,
$$

$$
P_*:=E\{\mathcal G(f_*,f_*),\mathcal G(f_*,g_*)\}
=S_*\sum_i s_i v_i^2a_i^7.
\tag{5}
$$

本稿需要 $P_*\ne0$，而不只 $|P_*|<Q_*$。等差节点给

$$
(v_1,v_2,v_3,v_4)
=\frac1{6\Delta^3}(-1,3,-3,1).
$$

所以

$$
\frac{36\Delta^6}{S_*}P_*
=-(a+\Delta)^7+9(a+2\Delta)^7-9(a+3\Delta)^7+(a+4\Delta)^7
$$

$$
=-6\Delta\left[
7a^6+105a^5\Delta+630a^4\Delta^2+1925a^3\Delta^3
+3066a^2\Delta^4+2205a\Delta^5+358\Delta^6
\right]<0.
\tag{6}
$$

这是有限二项式恒等式，不评价 $\psi$ 的任何新积分。

### 3.1 平移的正 bulk 是有限多项式

R233 的原同锚式写作

$$
\mathcal G(u,u)=\frac{x^2}{8}J[x^4R^2],
\qquad R=(u/x)''.
$$

准确恒等式 $3R+xR'=u'''$ 给

$$
\left(\frac{\mathcal G(u,u)}x\right)''
=-\frac14(x^3u''-2x^2u'+2xu)u'''.
\tag{7}
$$

因此

$$
S(u)=\frac1{64}\int
x^6(x^2u''-2xu'+2u)^2(u''')^2.
\tag{8}
$$

对平移 $u_t(x)=u(x-t)$，换回固定变量后 (8) 是 t 的次数至多十的多项式。它在所有实际允许的正坐标平移上恰等于真实正 bulk。这里没有把带左尾的 $E(\mathcal G(u,u),\mathcal G(u,u))$ 当作 (8)。

### 3.2 八复制后避开有限个零点

取任意预定的小正开区间 J。先让 a 落在 J 的内部，再把 $\Delta,\delta$ 取得足够小，使基本支撑 $[\alpha,\beta]\Subset J$ 很窄。于是

$$
\mathcal L=
\{L>\beta-\alpha:\ [\alpha,\beta+7L]\Subset J\}
\tag{9}
$$

是非空开区间。对其中 L，令

$$
b_j=(-1)^j\binom7j^{1/3},\qquad
f_8=\sum_{j=0}^7b_j f_*(x-jL),\quad
g_8=\sum_{j=0}^7b_j g_*(x-jL).
\tag{10}
$$

每个基本 pair 单独三矩零差，故 (10) 是三矩圆，且在各微包上仍 $g_8=\pm f_8$。

R233 的全部边界项已付，其准确 $P_8=E(A_8,X_8)$ 在合法间距上等于

$$
P_8(L)=\sum_{j=0}^7b_j^4
\sum_{i=1}^4s_iw_i^2\,S(\psi_i(\,\cdot-jL)).
\tag{11}
$$

由 (8)，右边是 L 的有限多项式；其在 $L=0$ 的多项式值为

$$
P_8(0)=\left(\sum_{j=0}^7b_j^4\right)P_*<0.
\tag{12}
$$

**(12) 只是对角表达 (11) 的多项式延拓值。** 当 $L=0$ 时实际 profiles 重叠，不能把跨包正交或 (11) 解释成那个退化叠加 profile 的真实能量。本证明只用 (12) 说明这个多项式非零。

它只有有限个实根，因此可在非空合法开区间 $\mathcal L$ 选 L，使 $P_8(L)\ne0$。可同时选 L 为有理数；无需执行研究扫描或求积来证明这样的参数存在。

记

$$
A_8=\mathcal G(f_8,f_8)=\mathcal G(g_8,g_8),\qquad
X_8=\mathcal G(f_8,g_8),
$$

$$
Q_8=E(X_8,X_8)>0,\qquad
t=-P_8/Q_8.
$$

两种微包符号都有正 bulk 权重，故

$$
\boxed{0<|t|<1.}
\tag{13}
$$

### 3.3 完整第三阶已经在这个 block 内支付

使用 R183 §5／R233 §8 的全部四槽，八个三次幅度
$b_j^3=(-1)^j\binom7j$ 消去平移次数至多六的四条第三 ruling。两个二阶 forcing 的三矩逐基本包为零，所以其真实第二场，包括 s history，在各基本包之外为零；没有遗漏它与其他包第一输入的交叉项。

同时，各微包的 $(f_8',g_8')$ 都是某个固定实向量乘一个标量导数，R183 的完整 hook 引理给
$\mathfrak H|_{\mathcal P_8\times\operatorname{Sym}^2\mathcal P_8}=0$。
因此在已给定的 $M=0,T=\kappa\mathfrak H$ 几何上，这一个 block 的完整二、三阶 range 已经支付。

## 4. 同一个非零 t 的两种旋转根

取

$$
-\frac\pi4<\alpha<\frac\pi4,\qquad
\sin2\alpha=t,\quad \cos2\alpha>0,
$$

并令

$$
\beta=\frac\pi2-\alpha.
\tag{14}
$$

于是 $\sin2\beta=t$、$\cos2\beta=-\cos2\alpha$。分别按 R233 的旋转定义
$(f^\alpha,g^\alpha)$ 与 $(f^\beta,g^\beta)$。对两者均有

$$
\mathcal G(f^\gamma,f^\gamma)=A_8+tX_8,\qquad
\mathcal G(g^\gamma,g^\gamma)=A_8-tX_8,
$$

$$
\mathcal G(f^\gamma,g^\gamma)=\cos2\gamma\,X_8,
\qquad \gamma\in\{\alpha,\beta\}.
$$

所以

$$
L_c(f^\gamma,g^\gamma)=-2t(P_8+tQ_8)=0,\qquad
L_s(f^\gamma,g^\gamma)=\cos2\gamma(P_8+tQ_8)=0.
\tag{15}
$$

这是同一个真实 P、Q 的两根，不是用同一个常数角近似修复两个不同 block。共同 O(2) 旋转保持三矩，并在第一槽及差／交叉二次槽上作可逆的二维变换，故保留上一节已经支付的全部四条第三 ruling 和周期槽。

## 5. 任意给定正 I 内放置两个正尺度副本

选 $c_1<c_2$ 于 I 内，置 $H=c_2/c_1>1$。可取 c1 附近足够小的 J，使

$$
\overline J\subset I,\qquad
H\overline J\subset I,\qquad
\overline J\cap H\overline J=\varnothing,
\quad J<HJ.
\tag{16}
$$

第 3 节在这个 J 内完成全部构造。第一 block 取
$(f^\alpha,g^\alpha)$，第二 block 取其原未旋转 pair 的 H 正尺度副本再作 $\beta$ 旋转，即

$$
f_1=f^\alpha,\quad g_1=g^\alpha,\qquad
f_2(x)=f^\beta(x/H),\quad g_2(x)=g^\beta(x/H).
\tag{17}
$$

正尺度的原式协变给 $\mathcal G(u(\cdot/H),v(\cdot/H))(x)
=H\mathcal G(u,v)(x/H)$，从而两个能量均乘 H，t 的比值不变。三矩按 R233(16) 变换。因此第二 block 仍满足 (15)。

它也仍是完整八复制结构：基本 profiles 作同一个尺度变化，八个平移间隔变为 HL；第三 ruling 的同一七阶差分及 hook 不可见性原样成立。这不是将 profile 尺度变化当作真实几何变换。

最后置

$$
F=f_1+f_2,\qquad G=g_1+g_2.
\tag{18}
$$

两 block 三矩按支撑不交相加。第 2 节的准确能量加法给

$$
\boxed{L_c(F,G)=L_s(F,G)=0.}
\tag{19}
$$

最后统一乘一个正归一化系数，使 $m_0(F,F)=m_0(G,G)=1$。非退化性和 (19) 不变。

## 6. 至少四条取值方向，故不可 GL(2) 分离

写 $c=\cos\alpha,s=\sin\alpha$。由 $|\alpha|<\pi/4$，有 $c\pm s\ne0$。在第一 block 原正、负号微包上，最终比值 $G/F$ 分别是

$$
\rho=\frac{c-s}{c+s}>0,\qquad -\rho^{-1}.
$$

在第二 block 的 $\beta$ 分支上，比值分别是

$$
-\rho,\qquad \rho^{-1}.
\tag{20}
$$

$t\ne0$ 迫 $\alpha\ne0$，所以 $\rho\ne1$。四个数
$\rho,-\rho^{-1},-\rho,\rho^{-1}$ 彼此不同；每个比值都在一个真实非空活动子区间取得。

若存在常数可逆实矩阵把 (F,G) 变成支撑不交的两函数，则全部非零取值只能落在其逆像的两条固定直线上。它不能覆盖 (20) 的四条不同实射影方向。因此

$$
\boxed{\operatorname{span}\{F,G\}\text{ 不可由任何常数 }GL(2,\mathbb R)
\text{ 换基变为不交支撑。}}
\tag{21}
$$

这里判断使用 profile 的实际值，而不把不同微包的支撑不交误当成二维平面可分离。

## 7. 两个 block 合并后完整三阶仍成立

本节把“各 block 已付”落实为同一几何、同一右锚的全圆结论。

首先，任一微包上 $(F',G')$ 都是一个固定实向量乘一个标量导数；不同微包的导数支撑不交。R183 hook 引理因此直接给最终 $\mathcal P$ 的全部三次槽为零。

其次，两个完整二阶 forcing 是差槽和交叉槽：

$$
F^2-G^2=(f_1^2-g_1^2)+(f_2^2-g_2^2),\qquad
2FG=2f_1g_1+2f_2g_2.
$$

每个 block 的三矩零差保证其 canonical 二阶场在该 block 外为零，包括真实第二累计 profile。故四个第三 forcing 中，第一输入来自一个 block、第二场来自另一个 block 的所有交叉配对逐点为零。其 s 导数也不改变固定 xi 支撑。全四槽就是两个已完成四槽的和，因此全部第三 ruling 准确为零。

这里的二次槽等式按实际 forcing 理解：跨 block 的第一场及其完整导数支撑不交，故对应点态双线性 forcing 为零；并不是将抽象对称张量代数中的混合张量直接宣告为零。

在 $M=0$ 几何上完整二阶周期已付；在 $T=\kappa\mathfrak H$ 上最终 hook 不可见性又付全部第三周期。由 R56 完整 range，可得到同一右锚、同一周期、双 collar 的二、三阶解。所有实际 s histories 一直保留，没有按 block 重新选择累计零点。

这也说明该合并不需要给两个 block 分别选择不同几何：任意一个已满足上述 M/T 条件和共同 I 合法性的真实几何同时服务于两者。

## 8. 固定目标与未付的第四项

先冻结上述 F、G，再按原模型取

$$
Y_\theta=\cos\theta\,Y_F+\sin\theta\,Y_G,\qquad
g_\epsilon=g_X+\epsilon^2(dY_F)^2.
\tag{22}
$$

已经支付的二、三阶修正属于这个同一个 $g_\epsilon$ 的全圆，种子 $\theta=0,\pi$ 的高阶校正仍可取零。构造过程中重新选择了第一 profile，因此 (22) 一般不是 R193 原圆的旧目标；不能把新 profile 选择说成沿旧目标的 gauge。

对 R231 的例外端芽，另须保持其 $x>0$、$x+k_e/h_e>0$ 物理正支假设。在这样的共同 I 中，本稿确实消去完整 $h\beta^2$ 主层的两个相位系数，并且不再受“可换基不交”这一限制。它不证明原标准常段上的其他必要门已通过，也没有删掉较低的 second history、完整 third history、局部恢复或变化 profile 链式项。

没有继承 R193 的具体首包、R219 的八个非退化 flux 或 R225 的指定解析退化类；这些如需使用必须重新支付。完整第四 period、整个 ruling 商和有限等距仍未解决。下一层分析应针对这个新固定圆与同一选定几何的完整原式进行，而非由本稿的两个零数推断可解。

