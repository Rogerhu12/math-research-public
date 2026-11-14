# R486 — 分级整连接、十三权清极与原齐次第三核的准确边界

日期：2026-11-14。**状态：已证明。** 在 R473 的真实三来源规范化上，
保留按权确定的对数零阶项，可得零增权整连接；乘最小正权来源后，
得到十三权的全局多项式系数形式。本篇给其真实核、全部好特征核、
加一版本的精确饱和范围、乘积缺陷和原三块物理公式，并计算单一
齐次权的实际 Smith 因子。一般混权原核仍受两个额外电荷观察约束；
来源次数减少不等于 R418 的严格算术预算已经改善。主目标未完成。

## 1. 原规范化上的完整分级连接

使用 R473 同一个
$$
R=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)],\qquad
a=t(t-1)(7+4t+16t^2),
$$
$$
c_m=\lceil m/68\rceil,\quad
\ell_m=\lfloor11m/34\rfloor,\quad e_m=\ell_m-4c_m,
$$
$$
\mathcal B_m=\vartheta^ma^{c_m}R[t]_{\le e_m},\qquad
\mathcal B=\bigoplus_{m\ge0}\mathcal B_m.
\tag{1}
$$
$e_m<0$ 时分量为零。原 $\mathcal A=R[S,T,U]\subset\mathcal B$，
且 R473 给固定 conductor
$$
\mathfrak c\mathcal B_m\subset\mathcal A_{m+C},\qquad
C=10980,\quad \mathfrak c=\vartheta^Cq_{\mathfrak c}(t).
\tag{2}
$$

令 $\partial_{\rm ang}=t\partial_t$ 保 $\vartheta$ 不动，
$L_a=t a'/a$。对每个非空权定义
$$
\boxed{\nabla_m=\partial_{\rm ang}-c_mL_a,\qquad
\nabla_m^{(\alpha)}=\nabla_m+\alpha.}
\tag{3}
$$
在整个实际来源上，有
$$
\boxed{
\nabla_m^{(\alpha)}(\vartheta^ma^{c_m}f)
=\vartheta^ma^{c_m}(t f'+\alpha f).}
\tag{4}
$$
故对 $\alpha\in R$，这是零增权整算子。其有理系数的极点在 (4)
中全部抵消，不能将两项拆开后分别认成目标格内的算子。

在标准基 $b_{m,j}=\vartheta^ma^{c_m}t^j$ 上，
$$
\nabla_m^{(\alpha)}b_{m,j}=(j+\alpha)b_{m,j}.
\tag{5}
$$
特征零中，$\nabla_m$ 的核为一条 $R\vartheta^ma^{c_m}$；
每个非空权都有自己的水平核，不能统一称为“只有全局常数”。
$m>0$ 时其物理 germ 通常非恒定。加一连接 $\nabla_m^{(1)}$
在特征零无核。

若 $F\in\mathcal B_m,G\in\mathcal B_n$，准确的乘积缺陷为
$$
\boxed{
\nabla_{m+n}(FG)-(\nabla_mF)G-F(\nabla_nG)
=(c_m+c_n-c_{m+n})L_aFG.}
\tag{6}
$$
显示整数是 $0$ 或 $1$，但所乘角函数不能删除。
仅在 $68$ 次 Veronese 上，令 $\rho=\vartheta^{68}a$，有
$$
\mathcal B_{68n}=\rho^nR[t]_{\le18n},\qquad
\nabla_{68n}=\left.t\partial_t\right|_\rho.
\tag{7}
$$
这时才是真正导子，其常量域含 $R[\rho]$。
它与 R485 固定 $\vartheta$ 的纯角导子不同。

## 2. 全部模 p 核与准确饱和门

在 $R$ 的好特征 $p$ 中，(5) 直接给
$$
\ker\bar\nabla_m
=\vartheta^ma^{c_m}k[t^p]_{\le e_m},
\tag{8}
$$
$$
\boxed{
\ker\bar\nabla_m^{(1)}
=\vartheta^ma^{c_m}t^{p-1}
 k[t^p]_{\le e_m-(p-1)}.}
\tag{9}
$$
负次数上界表示零。故除去特征零的一条水平核后，
$\nabla_m$ 的像 $p$-饱和恰当且仅当 $e_m<p$；
加一连接是 $\mathcal B_m\otimes\mathbf Z_p$ 的整自同构
恰当且仅当
$$
\boxed{e_m\le p-2.}
\tag{10}
$$
达到边界时 (9) 给实际新核。

这些门可以对所有权准确读取。写
$$
m=68q+r,\quad0\le r<68,\qquad
e_m=18q+\lfloor11r/34\rfloor-4\mathbf1_{r>0}.
\tag{11}
$$
对整数 $K>0$，若 $K=18q+s$、$0\le s<18$，首次出现
$e_m\ge K$ 的权为
$$
\boxed{
\mathfrak n(K)=
\begin{cases}
68q,&s=0,\\
68q+\lceil34(s+4)/11\rceil,&1\le s\le17.
\end{cases}}
\tag{12}
$$
上一周期最大值为 $18q-1$；当前非零余类解
$\lfloor11r/34\rfloor-4\ge s$ 即得 (12)，故没有遗漏 ceiling 跳跃。

因此在全部 $m\le M$ 上，加一连接整可逆的准确范围是
$M<\mathfrak n(p-1)$；未加一版本除去每权一条水平核后的
饱和范围是 $M<\mathfrak n(p)$。本题惰性 $p\equiv5\pmod6$ 时：

| $p\bmod18$ | $\mathfrak n(p-1)$ | $\mathfrak n(p)$ |
|---|---|---|
| $5$ | $68\lfloor(p-1)/18\rfloor+25$ | $68\lfloor p/18\rfloor+28$ |
| $11$ | $68\lfloor(p-1)/18\rfloor+44$ | $68\lfloor p/18\rfloor+47$ |
| $17$ | $68\lfloor(p-1)/18\rfloor+62$ | $68\lfloor p/18\rfloor+65$ |

这不是 R485 纯角导子的 $4p$ 门：两者的常量域及实际核不同。

## 3. 十三权清极与全部来源成本

最小非零正权为 $13$，其中
$$
W_{13}=\vartheta^{13}a\in\mathcal B_{13}.
\tag{13}
$$
定义
$$
\boxed{
\mathscr D_m^{(\alpha)}=W_{13}\nabla_m^{(\alpha)}
=\vartheta^{13}\{a\partial_{\rm ang}-c_mt a'+\alpha a\}.}
\tag{14}
$$
其完整输出为
$$
\boxed{
\mathscr D_m^{(\alpha)}(\vartheta^ma^{c_m}f)
=\vartheta^{m+13}a^{c_m+1}(t f'+\alpha f)
\in\mathcal B_{m+13}.}
\tag{15}
$$
证明：令 $d_m=c_m+1-c_{m+13}\in\{0,1\}$，目标基中的多项式
为 $a^{d_m}(tf'+\alpha f)$，其次数至多 $e_m+4d_m$。准确余量为
$$
e_{m+13}-(e_m+4d_m)
=\ell_{m+13}-\ell_m-4\in\{0,1\}.
\tag{16}
$$
这支付全部六十八类。乘 $a^{d_m}$ 在有限多项式格中像饱和，
因为 $a$ 模好 $p$ 不为零；所以 (8)–(10) 的核及饱和判据
原样适用于 (15)。

真实整函数也有显示表达。因 $t=-\sigma^6/\Theta^3$，
$$
\boxed{
W_{13}
=7\sigma^6\Theta^{10}
 +3\sigma^{12}\Theta^7
 +12\sigma^{18}\Theta^4
 +16\sigma^{24}\Theta.}
\tag{17}
$$
每项都是 degree26 的完整 theta，首项为 $7z^6$。
十三只是非零正权乘子在 $\mathcal B$ 中的最小权；
裸连接 (3) 已零增权，故不能把十三说成所有连接的绝对最小成本。

反复 $k$ 次 (15) 的总权为 $m+13k$。若所有所经权满足 (10)，
复合保持单射及来源像 $p$-饱和。对于加一版本，canonical
多项式系数的范数至多
$$
38^k\prod_{i=0}^{k-1}(e_{m+13i}+1)\|f\|_1,
\qquad \|a\|_1=38.
\tag{18}
$$
此导数增长必须计入预算；它不是一个统一于 $k,m$ 的常数。

## 4. 原 regularized 三块中的完整物理式

保留
$$
p=6s-1>83,\quad L=2s+\ell,\quad1\le\ell<s-13,
$$
$$
w^s=p\epsilon,\qquad \epsilon^3=0,\qquad
w^\ell\epsilon^2=0.
\tag{19}
$$
原实际变量为
$$
X=\vartheta_{\rm reg}(w)e^{a_0\epsilon/17},\qquad
\vartheta_{\rm reg}=(g/d)^{1/17},\quad d=1+8t,\quad a_0=p\kappa.
$$
$a_0$ 是原 Gaussian 单位，与角多项式 $a(t)$ 区分。
原 $g,t$ 及全部高尾保持 R468、R481 的定义。置
$$
\mathsf D=w\partial_w+s\epsilon\partial_\epsilon,\qquad
B=\mathsf D\log\vartheta_{\rm reg}+s a_0\epsilon/17,\qquad
\nu=(\mathsf D\log t)^{-1}.
\tag{20}
$$
这是原整 regularized 窗口内的量，$t=-w+\cdots$，
$\nu(0,0)=1$；不把普通 Amice 的整性转用为 raw 惰性 Taylor 整性。
$\mathsf D$ 保持 (19) 的所有关系。

令 $J_m$ 为原齐次来源在 $\vartheta=X,t=t(w)$ 的三块评价。
链式法则给
$$
J_m\partial_{\rm ang}=\nu(\mathsf D-mB)J_m,
$$
故
$$
\boxed{
J_m\nabla_m^{(\alpha)}
=\{\nu(\mathsf D-mB)+\alpha-c_mL_a(t(w))\}J_m.}
\tag{21}
$$
$L_a(t)$ 在原点值为一，是该局部窗口中的整级数；其他角根的
对数极由 (4) 整体支付。十三权版本再乘
$$
W_{13,\rm phys}=X^{13}a(t),\qquad
\nu W_{13,\rm phys}=7w\cdot(\text{原整单位}).
\tag{22}
$$

恢复整个原 $M_m=c_*U_0m_{13}J_m$，得到
$$
\boxed{
M_m\nabla_m^{(\alpha)}
=\{\nu(\mathsf D-13-\mathsf D\log U_0-mB)
       +\alpha-c_mL_a\}M_m.}
\tag{23}
$$
这里 $U_0$ 是含原 $P_{134}$、charge40 和全部 Gaussian 的完整单位。
对 (15)，右边再乘 $W_{13,\rm phys}$，并使用多一条物理行的
完整目标；第一、第二块进位继续按 (19) 保留。

### 4.1 一般混权的两个真实电荷观察

在直接和上定义
$$
\mathcal E_\vartheta|_{\mathcal B_m}=m,\qquad
\mathcal C|_{\mathcal B_m}=c_m.
$$
则 (23) 对一般 $F$ 的完整形式是
$$
\boxed{
M\nabla^{(\alpha)}F
=\{\nu(\mathsf D-13-\mathsf D\log U_0)+\alpha\}MF
-\nu B\,M\mathcal E_\vartheta F
-L_a\,M\mathcal CF.}
\tag{24}
$$
所以 $MF\equiv0$ 不使后两项自动消失。
$\mathcal C-\mathcal E_\vartheta/68$ 是真实六十八类角项；
即使用零增权连接，仍须证明混权原核与这些电荷观察相容。
这正是目前没有由连接成本改善付出的条件。

## 5. 固定 conductor 的整返回与全部补项

在 (2) 的实际子格上定义
$$
\mathcal Q_{\mathfrak c,m}^{(\alpha)}(\mathfrak cF)
=\mathfrak c\nabla_m^{(\alpha)}F.
\tag{25}
$$
输出仍在 $\mathcal A_{m+C}$；十三权版本则在
$\mathcal A_{m+C+13}$。函数域中的完整表达为
$$
\mathcal Q_{\mathfrak c,m}^{(\alpha)}
=\partial_{\rm ang}
-\frac{\partial_{\rm ang}\mathfrak c}{\mathfrak c}
-c_mL_a+\alpha.
\tag{26}
$$
它始终作用于显示的 $\mathfrak c\mathcal B_m$，不在任意原来源上
自由除 conductor。反复操作只需最后乘一次 $\mathfrak c$；
总权为 $m+C$ 或 $m+13k+C$。

在 (23) 仍按返回前来源的权 $m$ 读取时，物理式外还必须保
$-\nu\mathsf D\log\mathfrak c_{\rm phys}$，因为
$$
\mathsf D\log\mathfrak c_{\rm phys}
=CB+\nu^{-1}tq_{\mathfrak c}'/q_{\mathfrak c}.
\tag{27}
$$
此式同时保固定角项及 conductor 自身的 Gaussian 电荷。
返回后总 charge 为 $40+(m+C)/17$；十三权第 $k$ 步为
$40+(m+C+13k)/17$。原高轴差和第三精度不能省掉这些项。

令 $r=\operatorname{ord}_0q_{\mathfrak c}$，R473 给
$162\le r\le3552$。原 regularized $X,t/w$ 为整单位；
另删固定首系数的有限坏集后，直接由代入得到
$$
\mathfrak c_{\rm phys}=w^r u,\qquad u\text{ 为原整单位}.
\tag{28}
$$
这不是从普通 Amice 结论转用。若 $L+13+r<3s$，乘 (28)
有 $L-2r$ 个单位 Smith 因子、$2r$ 个 $p$ 因子和
$r$ 条自由目标行；连同原 $m_{13}$，必须保两条长度
$13+r$ 的真实进位带。再用 (22) 时，每步多一条物理行及相应
两条进位。抽象来源饱和不删除这些真实目标条件。

## 6. 单一齐次权的实际 Smith 因子

设 $\mathcal B_m\ne0$，且
$$
c_m+e_m<L,\qquad L+13<3s.
\tag{29}
$$
其第 $j$ 列在原 $M$ 中完整为
$c_*U_0w^{13}X^ma(t)^{c_m}t^j$。
所有列共享一个整单位，因为
$a(t)=tA(t)$、$A(0)=-7$，并且原 $X,U_0,c_*$ 均为单位。
取 $t=t(w)$ 为整目标坐标，相应
$\epsilon_t=t^s/p=\epsilon(t/w)^s$ 给 (19) 的整自同构。
去掉共同单位后，所有列准确为 $t^{13+c_m+j}$。

由 (29)，这些列位于不同的原整行。因此非零 Smith 因子准确为
$$
\boxed{
\{p^{\lfloor(13+c_m+j)/s\rfloor}:0\le j\le e_m\}.}
\tag{30}
$$
指数只有 $0,1,2$；其余目标行是自由余核。
在这个规范化来源格中 primitive 的齐次向量，不可能给原
$M$ 的模 $p^3$ 零向量。若经 (2) 返回且
$L+13+r<3s$，同一个证明将 (30) 的 $13$ 换成 $13+r$，
并保全部新的自由行及进位。

该结论要求 (29) 及明确的 primitive 来源格。一般
$F=\sum_mF_m$ 的各权可以互相抵消，不能从和中提出同一个
$X^m$，也不能逐权读取 (30)。式 (24) 正好显示这个区别。
当前真正困难的混权首核、同一首次修正和相对第二余核，
仍须按 R479、R481 处理。

### 6.1 同预算的真实左右提升配对

在同一个累计来源 $\mathcal B_{\le N}$ 上，裸连接不增加来源
或目标。若 $P_2$ 是其实际 $M$ 的模 $p^2$ 右核提升，
$\xi_2$ 是同一个 $M$ 的完整模 $p^2$ 左核提升，(24) 直接给
$$
\boxed{
\left\langle\xi_2,\,
 \nu B\,M\mathcal E_\vartheta P_2
 +L_a\,M\mathcal CP_2\right\rangle=0\pmod{p^2}.}
\tag{31}
$$
证明是左核消去同来源的 $M\nabla^{(\alpha)}P_2$，右核
消去 (24) 的第一项。沿 (25) 返回后，conductor 的全部
目标零阶修正同样作用于该右核，故 (31) 原样在真实
$M^{\mathfrak c}$ 上成立；两条 $13+r$ 进位仍属该完整矩阵。
在 (10) 的累计范围，可用加一连接保持来源 primitive 性。

式 (31) 不要求两条电荷观察各自保持右核，也不能把和中的
两项各自认作零。若来源另已限定于一个固定的 $m\bmod68$
类，才可用 $\mathcal C=\mathcal E_\vartheta/68+\eta_r$
将其化为单项
$(\nu B+L_a/68)M\mathcal E_\vartheta P_2$ 的配对；
一般实际混权向量没有这项额外前提。
这给同预算的完整接触关系，仍不证明某个真实余核类非零。

## 7. 后续可用范围

本篇支付了分级整连接、全特征核、固定返回和原物理三块身份；
没有改变三源函数域的超越次数二。真实系数增长 (18)、
conductor、Gaussian、两个电荷观察及全部进位仍在。
不能从“零增权”或“十三权”直接填入新的 $a_I,b_I$。
跨过 R418 的严格门，仍须由 (24) 的同一混权 jet 像或其真实
余核证明新的全量词算术估计。

依赖：

- [R473：三来源规范化及整 conductor](R473-three-source-function-field-normalization-and-integral-conductor.md)。
- [R453：原物理连接和固定返回进位](R453-single-integral-return-and-degree-two-two-source-connection.md)。
- [R468：第三中央行及实际 Gaussian 电荷](R468-third-original-central-row-three-axis-hensel-and-six-carry-interface.md)。
- [R479：原 M 两条进位及同一修正](R479-original-carry-graph-and-two-normal-jets.md)。
- [R481：完整第三精度和真正第二障碍](R481-full-third-precision-normal-form-and-common-correction.md)。
- [R485：固定 Theta 纯角导子与另一准确核门](R485-weight22-pure-connection-sharp-kernel-and-actual-return.md)。

