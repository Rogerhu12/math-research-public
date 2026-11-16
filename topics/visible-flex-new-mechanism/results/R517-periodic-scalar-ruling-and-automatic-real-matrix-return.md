# R517：同规范周期 scalar 的真实矩阵返回与两次重复判据

日期：2026-11-16。**完整纸面定理；没有执行 profile、几何、Jacobian、ODE、秩、求积、符号程序或开发检查。**

本稿接 [R512](R512-fixed-compact-second-mother-and-complete-linear-path-gauge-obstruction.md) 的同一固定第一母库、有限秩二阶规则和第三规范。新的结论把周期 scalar 的一个真实总端点条件严格接到完整 ruling：

- 对同一个光滑 scalar 周期作两次实际重复，若整个 ruling 都为零，则原八矩增量必须准确为零；
- 已付一次完整 ruling 且原八矩增量为零时，整个 ruling 随同一 scalar 周期准确重复；
- 若 scalar 本身是全圆实解析且合法，则一周期的完整 ruling 零已经强迫原八矩返回。固定 profile 只须 $C^\infty$，不需解析。

这不是周期轨道存在证明，也不是 frame、位置、第三或第四 period 返回。它给出的正向接口是：一个未来真正构造出来的实解析周期 scalar 解，不必再独立支付八条矩阵终值；这些终值由完整能量与实际尾的忠实性自动强制。不能把 R507 仅有三个 scalar 端值返回的短路当成这样的周期解。

## 1. 同一点数据和实际重复

固定 R512 的真实库
$$
\Delta=f^2-g^2=\sum_iR_i u_i^2,\qquad
u_i(x)=u(x-y_i),
\tag{1}
$$
以及一个共同右锚。各包严格不交，之间有开放 gap；所有 $R_i\ne0$，原 $\Delta$ 的三矩为零。

所有真实复制幅度已在 $R_i$ 中，不能把它们改成自由权。原 R280 的 low/high 值分别为 $-B/2,8B$，$B>0$；非零共同幅的复制乘平方，故 R512 的非零事实在这里保持。

取 R512 的固定二阶规范 $w_\theta$，并令
$$
q=w_{\pi/2},\qquad
\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu
\tag{2}
$$
为同一个第三 Gram。若沿用该稿的记号，则
$\nu=\nu_*-\mathbf I(q,q)/2$。$q,\chi,\nu$ 不随实际时间或重复次数改变。

设
$$
S(s)=(h(s),k(s),\omega(s))
\tag{3}
$$
是一个真正光滑的 $L$ 周期 scalar 函数，$L>0$，满足
$$
\omega_s=\frac{k_s}{2h}.
\tag{4}
$$
要求整个周期物理合法：存在固定 $\underline h,\underline z>0$，
使
$$
h(s)\ge\underline h,\qquad
x+\omega(s)\ge\underline z
\tag{5}
$$
对整个 profile 区间和所有 $s$ 成立。它们由一个合法紧周期上的连续性取得，不是假定各段分别有不相容的窗口。

这里“周期”包含各阶端 germ 的实际匹配，保证重复后仍是一条原允许的光滑路径。下面的代数在检查点只使用 scalar 一阶 jet 相同；这不允许仅凭一阶端值匹配就宣告整个重复词已经光滑。

沿原实际时间恢复全部 frame、位置及二阶 history：
$$
\mathsf m_s=M_{\rm raw}(S,S_s),\qquad
\mathsf m(0)=\mathsf m_* .
\tag{6}
$$
$\mathsf m_*$ 是同一个真实传入值；不会在 $L$ 或 $2L$ 重置。定义一个周期的原八矩增量
$$
M=\int_0^L M_{\rm raw}(S(s),S_s(s))\,ds .
\tag{7}
$$
原 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 给 $M_{\rm raw}$ 逐点属于同一 $\mathfrak{sl}_3$；它只依赖 scalar 一阶 jet，不依赖已累计的 $\mathsf m$。因此准确有
$$
\boxed{\mathsf m(s+nL)=\mathsf m(s)+nM}
\tag{8}
$$
对每个整数 $n$ 成立。正时长重复只用 $n\ge0$，不需要负时间路径。

## 2. 固定 $\Delta$ 上原八维输出的忠实性

记
$$
q_E=\Phi_E(\Delta),\qquad E\in\mathcal E_8.
$$
原三矩使每个 $q_E$ 双 collar 紧。这里需要的是
$$
\boxed{q_E\equiv0\quad\Longrightarrow\quad E=0.}
\tag{9}
$$
为避免把原表示的维数冒作忠实性，完整证明如下。

原 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的真实左尾为
$$
p_E(n)=
(r_0+r_1x-p_0x^2/4)n_0+
(s_0+s_1x-p_1x^2/4)n_1+
(t_0+t_1x-p_2x^2/4)n_2,
$$
$$
t_0=p_0/4+s_1/2.
\tag{10}
$$
在第 $i$ 个实际 gap 上，$\Phi_E(\Delta)$ 恰为右方微包的
$p_E(\sum_{j>i}R_j\mu_j)$，其中
$\mu_j=\mathbf I(u_j,u_j)$。若 $q_E\equiv0$，此二次多项式在开放 gap 为零，故作为多项式恒零。相邻两个 gap 的零多项式相减给
$$
R_i\,p_E(\mu_i)=0 .
\tag{11}
$$
全体两端 collar 也给最左和最右的相同边界论证，没有遗漏末包。
因为 $R_i\ne0$，每个 $p_E(\mu_i)=0$。

共同母的三矩在真实中心 $c$ 上为
$$
\mu(c)=
(m_0,\ m_1+cm_0,\ m_2+2cm_1+c^2m_0),\qquad m_0=\int u''{}^2>0 .
\tag{12}
$$
$m_2$ 包含原 $2u'^2$ 项。三个不同实际中心的矩向量行列式，
按取行的次序等于
$$
m_0^3\prod_{i<j}(c_j-c_i)\ne0.
$$
因此这些 $\mu_i$ 张成 $\mathbb R^3$。由(11)及 $p_E$ 对 $n$ 的线性性，
$p_E(n)\equiv0$ 对所有 $n$ 成立。逐个读取(10)的 $x$ 系数，
原八坐标全部为零，得到(9)。

这正是 [R503](R503-nonzero-prefix-reflection-and-one-gauge-for-complete-secant-patches.md) §5 的尾忠实性在固定 $\Delta$ 上的版本。该稿使用全部相位以产生非零包系数；这里每个固定 $R_i$ 已非零，故无需另假所有相位输出为零。

若改用别的母库，真正需要保的是：非零差幅对应的实际三矩向量张成三维，并且相邻开放 gap 可读取原尾。本文不把(9)授给任意少量 profile 或不存在间隙的重叠族。

## 3. 整个 ruling 在周期次数上是准确二次式

令 $Z^w_\Delta$ 表示已经包含固定二阶规范的完整 second 场。
由原恢复
$$
Z^w_\Delta=K_{\rm loc,\Delta}-Y_{\Phi_{\mathsf m}\Delta+q},
\tag{13}
$$
其中 $K_{\rm loc}$ 使用原完整局部恢复，依赖当前 scalar 一阶 jet。
在适应 frame 的原分子记号下，周期性与(8)给
$$
\boxed{
V_{Z^w_\Delta}'(s+nL)
=V_{Z^w_\Delta}'(s)-nV_{Y_{q_M}}'(s),
\qquad q_M=\Phi_M(\Delta).
}
\tag{14}
$$
即使实际 frame 在每周期相差一个非平凡正交转动，原分子内积仍相同。
原中心线位置不进入此内积。式(14)不要求 frame 或中心线返回。

记
$$
e_s(M)=\frac1{h(s)}\int|V_{Y_{q_M}}'(s,x)|^2\,dx,\qquad
b_s(M)=\frac1{h(s)}
\int V_{Z^w_\Delta}'(s,x)\cdot V_{Y_{q_M}}'(s,x)\,dx .
\tag{15}
$$
R512 已完整支付同一 $(u,v)$ 的 $Y$–third 配对和原相位能量身份，
故整个 ruling 为
$$
\mathscr K(s,\theta)=
-\sin^2\theta\left\{
\frac1h\int|V_{Z^w_\Delta}'|^2
+2\mathbf w_{\rm geom}(S(s))\cdot\nu
\right\}.
\tag{16}
$$
所有 canonical、有序尾和传入量都在(13)中；没有从 third 场本身删掉一个累计项。

把(14)直接代入(16)：
$$
\boxed{
\mathscr K(s+nL,\theta)
=\mathscr K(s,\theta)
+2n\sin^2\theta\,b_s(M)
-n^2\sin^2\theta\,e_s(M).
}
\tag{17}
$$
尤其有准确的二阶差分
$$
\boxed{
\mathscr K(s+2L,\theta)-2\mathscr K(s+L,\theta)+\mathscr K(s,\theta)
=-2\sin^2\theta\,e_s(M).
}
\tag{18}
$$
同一个 $\chi$ 的 Gram、固定 $q$ 的交叉项及全部 incoming 只影响常数或一次项，不影响这个严格平方系数。

## 4. 两次真实重复与原 $M=0$ 的准确等价

取 $\theta=\pi/2$。若在同一实际词的两个连续周期 $[0,2L]$ 上完整 $\mathscr K$ 都为零，连续性也给三个真实检查点
$$
0,\quad L,\quad 2L
$$
的零值。式(18)在 $s=0$ 得 $e_0(M)=0$。

原 $Y_{q_M}$ 分子的第一分量是 $-q_M'/2$，所以其导数平方为零迫
$q_M''=0$。同一个右 collar 已给 $q_M=q_M'=0$，故
$q_M\equiv0$。再由(9)得
$$
\boxed{M=0.}
\tag{19}
$$
因此“两次重复”指两条长度 $L$ 的连续实际段，提供三个端点；
不是把仅有 $0,L$ 两个值当成足够的二次多项式判据。

反过来，若 $M=0$，则(8)使完整 second history 周期，
(14)及原几何权使(16)周期。若第一次 $[0,L]$ 已有全
$s,\theta$ 的 $\mathscr K=0$，则同一 scalar、同一规范的所有正时长重复都保持该结论。

**定理 1。** 在第1节的同一点假设下，已经支付一次完整 ruling 的周期 scalar 模板，其第二次实际重复也支付完整 ruling，当且仅当原八矩增量 $M$ 为零。

这给一种真实重复性判据。它不声称任一已付一次的 scalar 模板能够再次保持 ruling；若其 $M\ne0$，(18)已经严格说明不能。

## 5. 实解析周期 scalar 的自动矩阵返回

现在额外假设 $S$ 是实解析的周期函数，即它本身定义在一个实解析圆上，且(4)(5)在全圆成立。不能只把一个局部实解析段的两端值对上就使用本节。

原 $M_{\rm raw}(S,S_s)$ 是实解析的周期函数。它的真实积分
$\mathsf m(s)$ 在整条实轴实解析，尽管尚未知道它是否周期；
(8)已给出其可能的线性漂移，不存在因此造成的有限时间定义域缺口。

固定 profile 只须光滑，不须实解析。理由可从 R56/R73 的原分子直接读出：
$K_{\rm loc}$、$Y_{\Phi_{\mathsf m}\Delta+q}$ 及(16)由有限个固定 profile 函数、原固定 Volterra 积分和几何的有限 Laurent–多项式系数组成。对 $s$ 的解析性在这些几何系数中，不要求把 $x$ 的光滑函数延拓到复平面。

等价地，在每个周期紧参数域上，(5)提供统一正下界，
原分母远离零；几何系数在一个足够小的复时间邻域有统一解析延拓。
所有所需固定 profile jets 与其右原函数在共同紧区间有界，
故原 $x$ 配对积分也对 $s$ 实解析。此说明保留全部右锚项，
不先删任何左尾或用形式级数替换真实积分。

于是固定相位的 $\mathscr K(s,\theta)$ 在整个 $\mathbb R$ 实解析。
若一周期内整个 ruling 为零，实解析恒等定理使它在所有实际
$s$ 上为零。特别两个连续周期都为零，定理1给 $M=0$。

**定理 2。** 同一固定母库及同一规范上，一个合法、实解析周期
scalar 的完整 ruling 若在一个周期成立，则其原八矩增量自动为零，
并且 ruling 随全部正时长重复成立。

实际上非空开放时间段的完整 ruling 零就足以触发这一解析延拓；
但前提仍是已经有整圆的同一个实解析 scalar。不能把 R508 的局部
secant germ 在外部随意周期化后继续宣称解析。一个实解析函数在开放
germ 上已经被固定，外部拼接没有这种自由。

若 scalar 只有 $C^\infty$，本节的延拓论证不适用。
此时仍可使用第4节的两次真实重复判据，不能把一次重复自动算成两次。

## 6. 正定性还给一个不含新数值的稳定形式

固定原八基和其欧氏系数范数。式(15)给一个真实对称八维 Gram。
由(9)与第4节的正能量论证，它严格正定。沿一个合法紧周期连续依赖，
故有某个严格正的常数 $c$，满足
$$
e_s(M)\ge c\|M\|^2
$$
对整个周期成立。这是固定数据上的有限维紧性结论，未给一个未经计算的数值特征值。

例如若同一实际重复词在 $0,L,2L$、相位 $\pi/2$ 的 ruling 绝对值均不超过 $\varepsilon$，
则(18)严格给
$$
2e_0(M)\le4\varepsilon,\qquad
\|M\|\le\sqrt{2\varepsilon/c}.
$$
它只说明代数身份的稳定方向；不是当前任何数值路径已验证这些条件，
也不以有限小残差代替本文的准确零定理。

## 7. 尚需实际构造的对象与未删全词成本

本稿没有构造第5节的周期轨道。R507/R508/R509 的局部端点结果没有
同时支付周期 scalar 的全部 germ，更没有支付一个整圆实解析函数；
R515 的正二次矩阵边界继续有效。以后若找到这样的真正周期
$K=0$ 轨道，(19)才把原八矩返回作为结论给出。

即使 $M=0$，仍必须另付：

- 实际 frame 的周期旋转与中心线位置；
- 完整第三增量 $T$、第四增量 $V$ 及全部倒行／prototype／Klein 基准；
- 原两个 period 与同一个十三规范；
- 原几何主目标的固定度量、闭嵌入和厚度条件。

第4节只证明完整 ruling 随周期重复，并未说第三场或第四场自身周期。
这些场的全部原传递照常累计；R512 包装只在明确的 pairing 中消掉其贡献，
不能将其算子值或成本删去。所有重复仍是正时长实际路径，
没有把一个负矩阵替成负时间块。

因此本稿把真正未付的问题准确收紧为：构造同一固定规范下的合法实解析
周期 scalar 完整解，或直接构造两次都成立的光滑周期模板。
这是一个真实闭轨道问题；一旦它实际完成，原八矩端点便由本稿自动闭合，
但其余全词和主完成门仍须继续处理。
