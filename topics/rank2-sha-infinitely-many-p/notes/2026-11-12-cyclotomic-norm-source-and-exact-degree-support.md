# 原 theta 源的圆分范数、准确齐次支撑与常数权除法

日期：2026-11-12。**状态：以下实际范数公式、有理整系数、原次数下降及同源除法支撑均已证明。**
本文使用 R180/R183 的真实 $a^{p^q}$ 截断构造，
不把这些对称性赋给任意选择的 R178 Cartan 修正。
所有结论仍在原来的 $(\mathcal A,B)=(A_2,B)$ 源中；
尚未证明原双中央导数的无穷非零或 R159 的严格预算。

## 1. 原对象和两种次数

固定惰性 $p\ge7$、$p\ne11$，沿用

$$
r=(p+1)/4,\quad R=r(p-1),\quad
\varpi^R=p,\quad\lambda=\varpi^r,\quad\gamma=\varpi^p.
$$

令 $m=p^q$、$q\ge1$，并取 R183 的允许 $n,N,J$。
特别 $J\le N<rm$。原曲线和原坐标是

$$
a(s)=e^{t(s)},\quad b(s)=s a(s),\qquad
\mathcal A=a^{17}P(s),\quad B=a^{17}Q(s),
$$
$$
P(s)=s+O(s^2),\quad Q(s)-P(s)=-22s^2+O(s^3).
$$

为避免把两个不同的差混用，记

$$
D_0=B-\mathcal A,\quad
\mathcal C=D_0+22\mathcal A^2,\quad
Z=\mathcal C/\mathcal A^2,\quad L=Z-22.
\tag{1}
$$

因此 $\mathcal A L=D_0/\mathcal A=Q/P-1$。
R178 已证明 $(\mathcal A,Z)$ 是原 $(a-1,b)$ 邻域的整形式坐标。
这里 $L$ 的常数为 $-22$；仅对已经准备成有限 $Z$ 多项式的对象
作 $Z=L+22$ 的代换，不向任意 $Z$ 形式级数代入这个单位常数。

写

$$
a(s)^m=\sum_{h\ge0}d_hs^h,\quad
D_N(s)=\sum_{h=0}^N d_hs^h,\qquad
\mathfrak J=a^N\{a^m-D_N(b/a)\}.
\tag{2}
$$

R183 给 $d_0,\ldots,d_N\in\mathbb Q\cap\mathbb Z_p$。
对 $374^m\mathfrak J$ 用实际整坐标和 Weierstrass 准备，记

$$
374^m\mathfrak J=S_N(\mathcal A,Z)W_N(\mathcal A,Z),\qquad
W_N=Z^m+\sum_{i<m}w_i(\mathcal A)Z^i.
\tag{3}
$$

准备单位 $S_N$ 与系数 $w_i$ 都在原整完成环中。
R183 的原多项式为

$$
\mathcal P_{q,n}
=\mathcal A^{2m}W_N^{[J]}
 \left(\mathcal A,\frac{D_0}{\mathcal A^2}+22\right),
\tag{4}
$$

上标表示截去系数中 $\mathcal A$ 次数大于 $J$ 的部分。
原已付次数是 $d=2m+J$，准确消失前缀是 $d+1$。
下文改善的是实际多项式次数，不撤销该已付前缀。

## 2. 径向圆分作用与准备的唯一性

取本原 $m$ 次根单位 $\zeta$，在
$\mathcal O_{\mathbb Q_p(\zeta)}[[\mathcal A]]$ 上准备。
其极大理想由 $\zeta-1,\mathcal A$ 生成。
径向变换 $(a,b)\mapsto(\zeta a,\zeta b)$ 保持 $s=b/a$，并满足

$$
\mathfrak J\longmapsto\zeta^N\mathfrak J,\qquad
(\mathcal A,B)\longmapsto(\zeta^{17}\mathcal A,\zeta^{17}B),
$$
$$
Z\longmapsto22+\zeta^{-17}(Z-22).
\tag{5}
$$

$22(1-\zeta^{-17})$ 在扩张环的极大理想中。
因此仿射代换在 $(\zeta-1,\mathcal A,Z)$ 完备拓扑中合法，
保留形式单位。代换后的 $W_N$ 仍关于 $Z$ 首一、次数为 $m$，
因为 $\zeta^{-17m}=1$；模极大理想仍为 $Z^m$。
比较 (3) 在 (5) 下的两种准备，唯一性给

$$
\boxed{\quad
W_N(\zeta^{17}\mathcal A,22+\zeta^{-17}(Z-22))
=W_N(\mathcal A,Z).
\quad}
\tag{6}
$$

这一步只将 $\mathfrak J$ 的半不变单位吸收到 $S_N$，
没有假定整个未准备表达式不变。

令 $\widetilde W_N(\mathcal A,L)=W_N(\mathcal A,L+22)$。
其 $\mathcal A^jL^i$ 系数在 (6) 下乘
$\zeta^{17(j-i)}$。因 $p\ne17$，扩张系数环无挠且为整环，得到

$$
\boxed{\quad
[\mathcal A^jL^i]\widetilde W_N\ne0
\quad\Longrightarrow\quad j\equiv i\pmod m.
\quad}
\tag{7}
$$

该作用不混合不同的 $\mathcal A$ 次数，所以 (7) 在截断 $[J]$
后仍准确成立。首一性还使 $L^m$ 的系数恒为一。

## 3. 原多项式的准确支撑与次数下降

由 (7)，存在整系数 $c_{i,t}$ 使

$$
\widetilde W_N^{[J]}
=L^m+\sum_{\substack{0\le i<m,\ t\ge0\\i+mt\le J}}
c_{i,t}\mathcal A^{i+mt}L^i.
\tag{8}
$$

代入 (4) 得到原源中的准确有限式

$$
\boxed{\quad
\mathcal P_{q,n}
=D_0^m+
\sum_{\substack{0\le i<m,\ t\ge0\\i+mt\le J}}
c_{i,t}\mathcal A^{(2+t)m-i}D_0^i.
\quad}
\tag{9}
$$

每个指数非负。因 $D_0=B-\mathcal A$ 是保持总次数的整线性换基，
第一块的原齐次次数准确为 $m$；其余各块的次数为 $(2+t)m$。
所以

$$
\boxed{\quad
\deg_{\mathcal A,B}\mathcal P_{q,n}
\le\Delta_{q,n}:=m\left(2+\left\lfloor J/m\right\rfloor\right)
=m\left\lfloor\frac{2m+J}{m}\right\rfloor.
\quad}
\tag{10}
$$

同时，R183 的同一个实际多项式仍满足

$$
\operatorname{ord}_s\mathcal P_{q,n}\ge2m+J+1,\qquad
\frac{\mathcal P_{q,n}(\gamma T)}
{p^{q-1}\lambda^p\gamma^{2m}}\in p^n\mathcal O'[[T]].
\tag{11}
$$

本文没有把前缀降为 $\Delta_{q,n}+1$ 后丢失原余量，
也没有说所有可能的最高齐次块必定非零。

## 4. 准备系数来自实际固定图的圆分范数

下面补出 (3) 的具体来源，也支付其有理性。
在特征零取常数项一的根

$$
a_N(s)=D_N(s)^{1/m}\in\mathbb Q[[s]],\quad
A_N=a_N^{17}P(s),\quad B_N=a_N^{17}Q(s).
$$

$A_N=s+O(s^2)$，故有形式逆 $s_N(A)$。令

$$
F_N(A)=B_N(s_N(A)),\qquad
G_N(A)=\frac{F_N(A)-A}{A^2},\qquad G_N(0)=-22.
\tag{12}
$$

对 $\epsilon^m=1$，写 $\epsilon=\zeta^{17}$。
未准备方程的对应分支为 $a=\zeta a_N(s)$，
从而在固定 $A$ 下的根准确为

$$
Z_\epsilon(A)=22+\epsilon^{-1}G_N(\epsilon^{-1}A).
\tag{13}
$$

这里不能假定 $G_N$ 的全部系数 $p$ 整。
为合法地代入准备单位，先在包含所有根单位的有限扩张中取足够小的
$A$ 盘：$D_N(0)=1$ 使 $a_N$ 在一个正半径盘解析，
$A_N'(0)=1$ 又给解析逆。有限个分支可共同缩盘，使
$|A|<1$、$|Z_\epsilon(A)|<1$；后者的常数
$22(1-\epsilon^{-1})$ 均在极大理想中。
原整形式级数 $S_N$ 在该盘收敛且为单位。
因此 (3) 与 $\mathfrak J=0$ 确实推出 $W_N(A,Z_\epsilon(A))=0$。
这些根的常数两两不同，而 $W_N$ 首一、次数为 $m$，故

$$
\boxed{\quad
W_N(A,Z)
=\prod_{\epsilon^m=1}
\left\{Z-22-\epsilon^{-1}G_N(\epsilon^{-1}A)\right\}.
\quad}
\tag{14}
$$

解析恒等式给同一形式恒等式。
$G_N$ 的系数有理，圆分 Galois 群只置换各因子，
所以 (14) 的全部系数有理。再结合原准备整性，得到

$$
W_N\in(\mathbb Q\cap\mathbb Z_p)[[A]][Z].
\tag{15}
$$

特别
$W_N(0,Z)=(Z-22)^m+22^m$，故 (8) 的 $c_{0,0}=22^m$。
这不是用模 $p$ 的根重复性代替特征零的准备。

现在取真正固定原图

$$
F(A)=B(s(A)),\qquad
G(A)=\frac{F(A)-A}{A^2}\in\mathbb Q[[A]],
\quad A=\mathcal A(s),\quad G(0)=-22.
\tag{16}
$$

由 $D_N-a^m=O(s^{N+1})$ 得
$a_N-a=O(s^{N+1})$、$A_N-\mathcal A=O(s^{N+2})$，
所以 $s_N(A)-s(A)=O(A^{N+2})$。
使用准确式
$F_N(A)=A(Q/P)(s_N(A))$ 和 $Q/P=1+O(s)$，进一步得到

$$
F_N-F=O(A^{N+3}),\qquad G_N-G=O(A^{N+1}).
\tag{17}
$$

因此在 (14) 中可以用固定 $G$ 代替 $G_N$，
而不改变任何 $A$ 次数至 $N$ 的系数。
原截断满足 $J\le N$，所以 (4) 的所有实际系数都来自

$$
\mathcal W_m(A,L)
=\prod_{\epsilon^m=1}
\{L-\epsilon^{-1}G(\epsilon^{-1}A)\}
\in\mathbb Q[[A]][L]
\tag{18}
$$

的同一个 $A$ 截断。对于固定 $p,q$，变化 $n$ 只改变已付截尾。
没有据此声称 (18) 超出已证窗口的全部系数 $p$ 整。

## 5. 固定原范数的准确首个分母

令 $j_0=rm$、$N=j_0-1$，这是 R183 已付的最大整系数窗口。
同文证明 $v_p(d_{j_0})=-1$。比较固定原函数与截断根，在特征零有

$$
a-a_N=\frac{d_{j_0}}m s^{j_0}+O(s^{j_0+1}),\qquad
\mathcal A-A_N=\frac{17d_{j_0}}m s^{j_0+1}+O(s^{j_0+2}).
$$

对固定 $A$ 反解并使用 $(Q/P)'(0)=-22$，得到

$$
G-G_N=\frac{374d_{j_0}}m A^{j_0}+O(A^{j_0+1}).
\tag{18a}
$$

因 $j_0\equiv0\pmod m$，(18) 每个根相对 (14) 的首变化都
等于其常数根 $-22\epsilon^{-1}$ 乘
$-17d_{j_0}A^{j_0}/m$。
在阶 $A^{j_0}$，只需对常数根多项式 $L^m+22^m$ 作这一共同缩放；
所以

$$
\mathcal W_m(A,L)-\widetilde W_N(A,L)
\equiv-17\,22^m d_{j_0} A^{j_0}\pmod{A^{j_0+1}}.
\tag{18b}
$$

首差与 $L$ 无关，也与 $Z$ 无关。
$W_N$ 的全部系数 $p$ 整，而 $p\nmid17\cdot22$；
故固定原范数 (18) 在所有 $A$ 次数小于 $rm$ 时整，
恰在 $A^{rm}$ 的常数 $Z$ 系数出现赋值 $-1$。
这里证明的是实际固定范数的首个分母，
没有将其当作任意原饱和 jet 的分母下界。

## 6. 第一层的完全明确有限系数

取 $q=n=1$，此时
$m=p$、$J=2r-1=(p-1)/2<p$。
由 (8)–(9)，原多项式只含次数 $p$ 和 $2p$ 两块；
因 $c_{0,0}=22^p\ne0$，第二块确非零，故实际次数准确为 $2p$。

还可免去未知准备系数，直接给出

$$
\boxed{\quad
\mathcal P_{p,1}
=(B-A)^p+\sum_{j=0}^{(p-1)/2}
c_j A^{2p-j}(B-A)^j,\qquad
c_j=-\frac{p}{p-j}[A^j]G(A)^{p-j}
\in\mathbb Q\cap\mathbb Z_p.
\quad}
\tag{19}
$$

证明如下。对 (18) 的根，Newton 幂和是

$$
S_h(A)=p\sum_{j+h\equiv0\ (p)}[A^j]G(A)^h A^j.
$$

对 $L^j$ 的 Newton 恒等式，幂和指标总和为 $p-j$。
若含至少两个幂和因子，且各指标为 $h<p$，
其最小 $A$ 阶至少为 $2p-(p-j)=p+j>j$；
更多因子的阶只会更高。故所需 $A^jL^j$ 系数只剩
线性项 $-S_{p-j}/(p-j)$，这给 (19)。
$j=0$ 的单独指标 $h=p$ 给 $c_0=22^p$。
这个论证实际识别了第一齐次块中全部 $0\le j<p$ 的系数；
本文的第一层源只取其中 $j\le J$ 的部分。
整性来自 (15)–(18) 的准确窗口，不是假定原 $G$ 全整。

另一个只用原 $s$ 系数的精确公式是

$$
c_j=-[s^{p-1}]
V(s)^{p-j-1}V'(s)
\left(\frac{s}{\mathcal A(s)}\right)^p,
\qquad V(s)=\frac{Q(s)}{P(s)}-1.
\tag{20}
$$

因为 $G(A)=V(s(A))/A$，先将 (19) 的系数写为
$[A^p]V(s(A))^{p-j}$，再用 Lagrange 反演，两个 $p/(p-j)$
准确抵消。这里 $V$ 只是计算参数，没有添加为原源的自由列。
事实上 (20) 的所需系数也直接整：$V$、$s/P$ 在这些素数处整，
而 R180 已付 $a^p$ 及其逆到次数 $p-1<pr$ 的整性。

同一个显式多项式保留

$$
\operatorname{ord}_s\mathcal P_{p,1}\ge(5p+1)/2,\qquad
\mathcal P_{p,1}(\gamma T)/(\lambda^p\gamma^{2p})\in p\mathcal O'[[T]].
\tag{21}
$$

## 7. 真正原源的常数权伴随矩阵

在 (19) 中给 $A,D_0,Z_0$ 权 $1,3,3p$，其中 $Z_0$ 表示
$\mathcal P_{p,1}$ 的形式值。每个修正单项的权为

$$
(2p-j)+3j=2p+2j\le3p-1.
$$

因此按首一 $D_0^p$ 的除法不增加这个权。
原 $B=D_0+A$ 的权至多三，所以 R181 的同一真实源像满足

$$
\boxed{\quad
A^\ell D_0^i Z_0^u:\qquad
0\le i<p,\quad \ell+3i+3pu\le3D.
\quad}
\tag{22}
$$

这将第一层原除法的环境次数成本从 $h=J+2$ 降为常数三，
但仍须保留 R181 的实际伴随矩阵像、其投影格和全部耦合前缀。
支撑容器不是一个免费更大的源。
以 (19) 作乘法格时，可使用真正次数 $2p$ 及仍较长的
$(5p+1)/2$ 消失延迟；完整旗标指数公式照常成立。
具体地，R181 在 $n=1$ 的同一规范权上支付九层，故

$$
\mathscr L_t^{\rm sharp}=E_D+
\sum_{u=1}^{t}p^{-9u}\mathcal P_{p,1}^{u}E_{D-2pu},\qquad
t\le\lfloor D/(2p)\rfloor,
$$
$$
\log_p[\mathscr L_t^{\rm sharp}:E_D]
=9\sum_{u=1}^{t}\binom{D-2pu+2}{2}.
\tag{23}
$$

新格仍满足 R181 的同一个全阶 $e_p(k)$ 输出基线，
该指数因此在完整真实旗标上准确扣除。
第 $u$ 块只影响阶至少为 $u(5p+1)/2$ 的跳跃。
这不要求商和余项分别保留前缀；此族的累计规模仍为 $O(D^3/p)$。
当前并未从这些次数改善推出严格全素数预算。

### 7.1. 任意圆分深度仍可取常数三权

对 $q\ge2$，在 R183 的允许下端取

$$
n=H_q-q,\qquad H_q=(p^q-1)/(p-1),\qquad
N=J=rp^{q-1}-1<m/2.
\tag{24}
$$

则 (9) 只有 $t=0$，同样给准确次数 $2m$、
消失前缀至少 $(2p+r)p^{q-1}$，且所有修正项的三权小于 $3m$。
因此 (22) 在任意该深度均可改写为
$\ell+3i+3mu\le3D$，仍使用同一真实源像。

这个选点还有精确的模 $p$ 主项。
R183 的系数界在 $0<h\le N<rp^{q-1}$ 给 $d_h\in p\mathbb Z_p$，
故 $D_N\equiv1\pmod p$。
在原整形式图中，$a=1$ 定义一条 $Z=Z_0(A)$ 的整截面，
$Z_0(0)=0$；隐函数导数由 $374$ 为单位支付。
所以模 $p$ 的准备因子为
$(Z-Z_0(A))^m=Z^m-Z_0(A)^m$。
因 $J<m$，截断后只余 $Z^m$，从而

$$
\mathcal P_{q,H_q-q}\equiv\mathcal C^{p^q}\pmod p.
\tag{25}
$$

这为全深度提供固定三权的实际伴随矩阵与明确 Frobenius 主项，
没有删掉相应高次余项或完整前缀条件。

## 依赖与核准

- [R180：原多层截断与准确前缀](2026-11-12-original-theta-multiple-precision-source-polynomials.md)。
- [R183：任意精度原源和两种尺度](../results/R183-arbitrary-precision-original-theta-source.md)。
- [R181：实际除法像与完整旗标指数](2026-11-12-actual-monic-source-division-and-saturated-flag-gain.md)。
- [R178：原整坐标及实际 Weierstrass 准备](2026-11-12-original-theta-as-source-and-integral-correction.md)。
- [R162：固定有理原源](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。

径向作用与唯一性、圆分根乘积及小盘代入由另一研究者独立复核；
准确齐次支撑和常数三权由第三位研究者独立复核。

[原系数有限校准](../scripts/check-cyclotomic-norm-source.py)
从实际有理 theta 图独立计算 (19)、(20)：$p=7,19$ 时两式逐系数相等，
真实消失阶分别为 $18,48$，且随后有限尾满足完整一层 $p$ 的规范界。
这些校准不替代本文的全素数证明。
