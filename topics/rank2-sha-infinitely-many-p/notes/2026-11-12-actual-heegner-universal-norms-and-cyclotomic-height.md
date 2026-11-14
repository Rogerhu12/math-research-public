# 实际 Heegner 迹点的完整范数族与范数一块的 cyclotomic 高度

日期：2026-11-12。**已证明**，使用 R119 的实际非平凡角色
rank-one / Sha 有限性输入；本篇不重新证明该 Euler 系统输入。
下述范数族的构造本身不需要 R119。

固定 $E:y^2=x^3-17x$、$F=\mathbf Q(\sqrt{-15})$，以及
R116 得到的一个实际辅助素数 $\ell$。输入素数 $p\ge13$
在 $F$ 和 $K=\mathbf Q(i)$ 中分裂，$\ell$ 在两域中惰性，
$v_p(\ell+1)=1$。令
$$
L/F\subset F[\ell]/F,\qquad
\Gamma=\langle\tau\rangle\simeq C_p,
\qquad A=\ker\bigl(\operatorname{Res}_{L/F}E\longrightarrow E\bigr).
$$
实际点记为
$$
Q=\operatorname{Tr}_{F[\ell]/L}P[\ell]\in A(F)
 =\ker(N:E(L)\to E(F)).                              \tag{1}
$$
R116 给出 $Q$ 非挠且不可被 $p$ 除。R106 给出某个 $j$ 使
$cQ=-\tau^jQ$，其中 $c$ 是复共轭。R119 给出
$$
\operatorname{rank}_{\mathbf Z}A(F)=p-1,
\qquad \Sha(A/F)\text{ 有限}.                        \tag{2}
$$
本篇从这些实际对象得到：

1. 指定 $Q$ 是 $LF_\infty/F$ 中一条完整、整的 $p$ 进
   Mordell--Weil 范数兼容族的第零项；这里 $F_\infty/F$
   是反圆分 $\mathbf Z_p$ 扩张。
2. cyclotomic 高度在整个 $A(F)\otimes\mathbf Q_p$ 上非退化。
3. $F$-反圆分方向的普通高度在这个块上恒零；由第 1 项，
   其所有由增广提升定义的派生 Bockstein 配对也杀这个块。

第 2 项是高度的非零结论，没有断言一个高度或判别式为
$p$-单位。第 1 项是 $p$ 进完成中的实际范数族，没有把其
$\mathbf Z_p$ 系数称为整数系数。

## 1. 保留两个初层的环类点递推

以 $F_m$ 记 $F_\infty/F$ 的次数 $p^m$ 层，$F_0=F$。
因为 $h_F=2$ 且 $p$ 分裂，$F_m$ 是 $F[p^{m+1}]$ 的
唯一 $p$ 次幂子层。$L$ 只在 $\ell$ 分歧，故
$L\cap F_\infty=F$。环类群的中国剩余描述给
$$
L_m:=LF_m\subset F[\ell p^{m+1}].
$$
所有原始 CM 点使用与 (1) 相同的 $N$-方向和参数化
$\pi(\infty)=O$。设
$$
Q_0=Q,\qquad
Q_n=\operatorname{Tr}_{F[\ell p^n]/L_{n-1}}P[\ell p^n]
\quad(n\ge1).                                       \tag{3}
$$
这已经取了原类群、$\ell$ 的 prime-to-$p$ 部分和 $p$ 处
tame 部分的全部迹；没有删去原类群和。

令 $\sigma\in\Gamma$ 为 $F$ 中一个 $p$ 上素理想在 $L/F$
的 Artin 符号。共轭素理想的符号是 $\sigma^{-1}$。
标准 CM $p$-同源递推在这些准确迹上为
$$
\begin{aligned}
Q_1&=(a_p-\sigma-\sigma^{-1})Q_0,\\
\operatorname{Tr}_{L_1/L}Q_2&=a_pQ_1-(p-1)Q_0,\\
\operatorname{Tr}_{L_{n-1}/L_{n-2}}Q_n
 &=a_pQ_{n-1}-Q_{n-2}\qquad(n\ge3).
\end{aligned}                                       \tag{4}
$$
这里第二式的 $p-1$ 必须保留。第一层有两条水平同源，
分别由两个 $p$ 理想的 Artin 作用给出；其余 $p-1$ 条下降。
正导子层有一条上升和 $p$ 条下降。对第二层的上升点再取
tame 迹，就出现 $p-1$；以后 tame 群已稳定，系数为 $1$。
这是原始点递推而非只在模 $p$ 的 Kummer 类中成立。

更明确地，令 $K_n=F[\ell p^n]$、
$A_\ell=\operatorname{Gal}(K_0/L)$，其阶为 $2u$。
对 $n\ge1$，$K_n/L_{n-1}$ 的 prime-to-$p$ 群 $D_n$
阶为 $2u(p-1)$。$D_1\to A_\ell$ 的核阶为 $p-1$，
而 $D_n\to D_{n-1}$ 在 $n\ge2$ 时是同构。
因此第二式中 $D_1$ 对 $P[\ell]$ 的迹是
$(p-1)Q_0$；第三式中 $D_{n-1}$ 对 $P[\ell p^{n-2}]$
的迹是 $Q_{n-2}$。这个群指数核对也说明 (3) 没有误删
一层类群或 tame 迹。

这些同源图、迹和类群作用可见 Cornut（2002），
*Mazur's conjecture on higher Heegner points*，§§1、4.1；
本仓库 [固定 ordinary ST / 原始点接口](2026-11-12-fixed-ordinary-st-mellin-branch.md)
及 [保留初层的 Cornut 迹证明](2026-11-12-cornut-fixed-branch-and-nonzero-progression.md)
已经在同一参数化上使用并证明此递推。这里唯一改变是保留
未必平凡的 $\sigma$。

## 2. 第零项恰为 Q 的范数兼容族

令 $\alpha\in\mathbf Z_p^\times$ 为
$X^2-a_pX+p$ 的 ordinary 单位根，故
$a_p=\alpha+p\alpha^{-1}$。令
$$
z_n=\alpha^{-n}(Q_n-\alpha^{-1}Q_{n-1})
 \in E(L_{n-1})\widehat\otimes\mathbf Z_p\qquad(n\ge2).
                                                               \tag{5}
$$
对 $n\ge3$，(4) 以及
$\operatorname{Tr}_{L_{n-1}/L_{n-2}}Q_{n-1}=pQ_{n-1}$ 给
$$
\operatorname{Tr}z_n
 =\alpha^{-n}\bigl((a_p-p\alpha^{-1})Q_{n-1}-Q_{n-2}\bigr)
 =z_{n-1}.                                          \tag{6}
$$
第一个范数则准确为
$$
\begin{aligned}
\operatorname{Tr}_{L_1/L}z_2
 &=\alpha^{-1}Q_1-(p-1)\alpha^{-2}Q_0\\
 &=\bigl(1+\alpha^{-2}-\alpha^{-1}(\sigma+\sigma^{-1})\bigr)Q\\
 &=(1-\alpha^{-1}\sigma)(1-\alpha^{-1}\sigma^{-1})Q.
\end{aligned}                                       \tag{7}
$$
记 (7) 的群环因子为 $u$。它是 $\mathbf Z_p[\Gamma]$ 的
单位：该环是局部环，极大理想为 $(p,\tau-1)$，而
$$
u\equiv(1-\alpha^{-1})^2\ne0\pmod{(p,\tau-1)}.       \tag{8}
$$
最后一个非零也不需另加异常素数条件。$E$ 有有理二挠点，
所以每个奇好素数的 $a_p$ 为偶数。对 $p\ge13$，Hasse 界
排除 $a_p\equiv1\pmod p$ 除 $a_p=1$ 之外的可能，而后者
被偶性排除。因此 $\alpha\not\equiv1\pmod p$。

令
$$
\mathcal Q_0=Q,\qquad
\mathcal Q_m=u^{-1}z_{m+1}\quad(m\ge1).               \tag{9}
$$
$\Gamma$ 在所有 $L_m$ 上与反圆分塔作用交换，因此
$u^{-1}$ 与所有迹交换。(6)–(8) 证明
$$
\operatorname{Tr}_{L_{m+1}/L_m}\mathcal Q_{m+1}=\mathcal Q_m
\qquad(m\ge0).                                      \tag{10}
$$
各项均在全局 Mordell--Weil 群的 $p$ 进完成中；用到的
只有 $\mathbf Z_p$ 中的单位及群环单位。没有除 $p$，也没有
由局部正式群除法冒充全局整数点除法。

此外，(3) 的 $\Gamma$-范数为零。对 $p^n$ 导子点在
$\ell$ 加入导子的 Euler 关系给 $a_\ell P[p^n]$，而
$a_\ell=0$；故 (9) 还保持在相应的范数一块内。

取 Kummer 类即可得到 $\mathcal Q_0=Q$ 的完整紧 Selmer
范数兼容提升。因 $Q$ 生成下面的有理 $\mathbf Q_p[\Gamma]$
不可约块，整个 $A(F)\otimes\mathbf Q_p$ 都包含在该塔紧
Selmer 通用范数的 $\mathbf Q_p$ 张成中。

## 3. 实际 cyclotomic 高度不为零

令 $K=\mathbf Q(i)$，取 $p=\mathfrak p\bar{\mathfrak p}$。
在 $LK$ 上取标准 CM single-$\mathfrak p$ 高度
$h_{\mathfrak p}$，以及其共轭 $h_{\bar{\mathfrak p}}$。
规范化可选成 cyclotomic 高度是它们的和；不同的非零整体
有理规范不影响本篇的非零及非退化结论。

使用 Bertrand（1984）的非零定理时，可完全保留 Rubin
附录开头的根数 $-1$ 约定。先取已在 R103 证明根数为
$-1$ 的 CM 曲线 $E'=E^{(-15)}$。它与 $E$ 在
$F\subset L$ 上同构。将 $Q$ 经该同构拉回为非挠点
$Q'\in E'(L)$，再在 $LK$ 上应用 Rubin 附录
Theorem A.1。该定理明确允许任意数域中的非挠点。
CM 普通分解以及同一个 single-$\mathfrak p$ idèle
字符所定义的高度在同构下相容，故得到
$$
h_{\mathfrak p}(Q,Q)\ne0.                            \tag{11}
$$
参见 Agboola--Howard（2006），
*Anticyclotomic Iwasawa theory of CM elliptic curves*，
Rubin 的 Appendix A，Theorem A.1，正式发表版印刷第 1043 页：
[原文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
这里使用的是该定理的单点结论，没有由它直接断言一般高度
矩阵非退化，也不需要把附录的根数假设从 $-1$ 扩张为 $+1$。
因 $p$ 在 $F$ 中分裂且 $p\nmid15$，该同构在所用普通
$p$ 进域上定义，其微分比例是单位；非零性本身甚至不需
这一比例为单位。

$\tau$ 在 $LK/K$ 的延拓固定 $K$，single-prime 高度因而
对 $\tau$ 不变。复共轭交换两个 single-prime 字符，所以
实际关系 $cQ=-\tau^jQ$ 给
$$
h_{\bar{\mathfrak p}}(Q,Q)
 =h_{\mathfrak p}(cQ,cQ)
 =h_{\mathfrak p}(Q,Q).                              \tag{12}
$$
于是
$$
h_{\rm cyc}(Q,Q)=2h_{\mathfrak p}(Q,Q)\ne0.          \tag{13}
$$
从 $LK$ 降回 $L$ 只是高度的已知非零次数因子；采用绝对
高度规范时该因子已经除去。故 (13) 是 $E/L$ 上真实的
cyclotomic 高度非零。

## 4. exact rank-one 块把单点非零升级为全块非退化

令
$$
\mathcal K=\mathbf Q_p(\zeta_p),\qquad
W=A(F)\otimes\mathbf Q_p.
$$
因 $N$ 在 $A$ 上为零，$\mathbf Q_p[\Gamma]$ 在 $W$ 上
经 $\mathcal K$ 作用。由 (2)，$\dim_{\mathcal K}W=1$，
而非零 $Q$ 是其一组基。记 $x\mapsto\bar x$ 为
$\zeta_p\mapsto\zeta_p^{-1}$ 的 involution。

任何 $\Gamma$-不变的 $\mathbf Q_p$ 双线性配对 $h$ 都满足
$h(ax,y)=h(x,\bar a y)$。迹配对的非退化性给唯一
$c_h\in\mathcal K$，使
$$
h(xQ,yQ)=\operatorname{Tr}_{\mathcal K/\mathbf Q_p}
 (c_h x\bar y).                                     \tag{14}
$$
若 $h$ 对称，则 $c_h=\bar c_h$。若 $c_h\ne0$，乘以
$c_h$ 是 $\mathcal K$ 上的同构，所以 (14) 非退化。

将 (14) 用于 cyclotomic 高度，(13) 给
$\operatorname{Tr}(c_h)\ne0$，特别是 $c_h\ne0$。所以
$$
\boxed{\det(h_{\rm cyc}|_W)\ne0.}                    \tag{15}
$$
这是 (2) 的 exact rank 输入所给的新结论。若只有
$\operatorname{rank}A(F)\ge p-1$，(14) 不是秩一形式，
该推论就不成立。

## 5. 同一个块在反圆分方向中的真实行为

令 $h_-$ 是从 $F_\infty/F$ 拉到 $L$ 的反圆分高度。
它仍对 $\Gamma$ 不变且对称，但
$$
h_-(cx,cy)=-h_-(x,y).                                \tag{16}
$$
由于 $c(xQ)=-\bar x\tau^jQ$，$\tau^j$ 与其共轭的积为
$1$。将 (14) 代入 (16) 给 $\bar c_h=-c_h$；对称性同时
给 $\bar c_h=c_h$。因 $p$ 为奇数，
$$
\boxed{h_-|_{W\times W}=0.}                          \tag{17}
$$
这不是只凭一个反不变向量的自高度为零：整个真实秩
$p-1$ 块都被 (14)–(16) 控制。

更强地，(9)–(10) 已经给出每个 $xQ$ 的完整 Selmer
范数提升。其在任何有限增广商中都来自同一个完整上链，
所以每一级增广连接障碍为零。因而所有由这些连接障碍
定义的派生 Bockstein 高度都杀 $W$；无需猜测递归核是否
最终等于通用范数。

在 Bertolini--Darmon（1995），*Derived p-adic heights*，
Theorem 2.18 所定义的 $1\le k\le p-1$ 范围内，这正是通用范数包含于各阶根的
已证性质：[发表版全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/pub13.pdf)。
更高有限增广层的连接障碍为零由上面的完整提升直接得出，
没有把该文只构造到 $p-1$ 阶的配对外推为一个文献定理。
该文的局部范数条件在这里用于 $LF_\infty/L$，不是用于
原先在 $\ell$ 分歧的 $L/F$。$E$ 在 $p$ ordinary 且
non-anomalous；$L/F$ 在 $p$ 至多不分歧次数 $p$，不会改变
模 $p$ 的 non-anomalous 性；其他分歧位的组件群只有与
$p$ 互素的阶。因此不能把不适用的有限 $L/F$ 范数假设
偷换进来。

## 6. 尚须检测的确切方向

上述构造解决了“实际点是否能在反圆分 $p$ 塔中成为范数”
这一问题，答案是可以，且 (7) 给出了完整的可逆 Euler
因子。它并不解决另一个算子
$$
\delta=\tau^{(p-1)/2}(\tau-1)
$$
在固定 $L/F$ 范数一格上的原始性。

事实上，令 $\mathcal O=\mathbf Z_p[\zeta_p]$，以
$e$ 为 $A(F)\widehat\otimes\mathbf Z_p$ 的一组
$\mathcal O$-基，写 $Q=a e$。由 (14)，
$$
h_{\rm cyc}(Q,Q)
 =\operatorname{Tr}(c_e a\bar a).                    \tag{18}
$$
(15) 只证明 $c_e\ne0$；(13) 只证明 (18) 不为零。
它们均未证明 $a\in\mathcal O^\times$。目标仍是这个
实际 $a$ 的 $\delta$-赋值为零；已知 $Q$ 不可被 $p$
除只给 $v_\delta(a)<p-1$。

因此本篇新增的是实际范数族与非退化 cyclotomic regulator，
不是一个尚未给出的单位高度估计。要继续检测最低增广层，
应保留 $\delta$ 方向及有限 Sha 的整格信息，而不是把
(17) 中已经被完整范数提升消去的方向再当作非零证书。
