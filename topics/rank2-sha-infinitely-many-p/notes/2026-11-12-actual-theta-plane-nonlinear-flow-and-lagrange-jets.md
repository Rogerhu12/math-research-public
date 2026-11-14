# 两条真实 theta 行的固定非线性方程与全部逆参数 jet

日期：2026-11-12。**状态：所列固定方程、全次数系数递推和原饱和格
的逆参数／留数公式已证明。** 这些公式没有给出所需惰性预算的严格改善，
也不把高阶行的新分母当作已经消除。

## 1. 原截面的完整固定多项式

始终在 $E_0:y^2=x^3-x$ 上，令

$$
u=x^{-1/2},\quad v=u',\quad s=u^4,\quad
\vartheta=\sigma/u,\quad L=\vartheta'/\vartheta.
$$

这里 $u(0)=0,u'(0)=1,\vartheta(0)=1,L(0)=0$；准确整数流是

$$
u'=v,\quad v'=-2u^3,\quad v^2=1-u^4,
\qquad L'=u^2,\quad\vartheta'=L\vartheta.
\tag{1.1}
$$

所有撇号暂指 $z$ 导数。R117 的原同次数两行可写为

$$
A_2(z)=\vartheta(z)^{68}P(s),\qquad
B(z)=\vartheta(z)^{68}Q(s),
\tag{1.2}
$$

$$
\begin{aligned}
P(s)&=\frac{s}{5}(1-s)^2(1+s)(1-2s+5s^2)(5-2s+s^2)
                       H_1(s)H_2(s),\\
Q(s)&=\frac{s}{5}(1-s)(1+s)^2(1-2s+5s^2)(5-2s+s^2)Q_8(s),
\end{aligned}
\tag{1.3}
$$

其中 $H_1,H_2,Q_8$ 是 R117/R155 的同一整多项式。
两个多项式均为次数十六，首项均为 $s$。这由 R117 的
$\sigma^{68}$ 表达式代入 $x^2=s^{-1}$、$\sigma^{68}=s^{17}\vartheta^{68}$
直接得到；没有增加未知首项标量。

记

$$
p_0(s)=P(s)/s\in1+s\mathbb Z[1/5][s],\qquad
V(s)=Q(s)/P(s)-1=-22s+O(s^2).
\tag{1.4}
$$

$V$ 是固定有理函数，原点的可去因子已经消去。
仍有 $B=(1+V)A_2$。

## 2. 真正固定的二阶非线性方程

把 $\vartheta^{68}$ 看成 $s$ 的形式级数，置

$$
U(s)=\vartheta(z(s))^{68},\qquad W(s)=\log U(s),\qquad W(0)=0.
$$

由 (1.1)，$d_z^2\log U=68u^2$，而

$$
(s')^2=16u^6(1-s),\qquad s''=4u^2(3-5s).
$$

因此完整方程准确是

$$
\boxed{\quad
4s(1-s)W''(s)+(3-5s)W'(s)=17.
\quad}
\tag{2.1}
$$

本节撇号改指 $s$ 导数。它确定唯一原点正则解，
$W'(0)=17/3$。若 $W'(s)=\sum_{n\ge0}a_ns^n$，则

$$
a_0=17/3,\qquad
(4n+3)a_n=(4n+1)a_{n-1}\quad(n\ge1).
\tag{2.2}
$$

等价地，

$$
\boxed{\quad
[s^m]W(s)=\frac{17}{m}
                \prod_{j=0}^{m-1}\frac{4j+1}{4j+3}
\quad(m\ge1).
\quad}
\tag{2.3}
$$

所以原输入准确为 $A_2=P(s)e^{W(s)}$，而不是一个任意的
局部指数模型。原正次数 theta 连接全部保留在这个固定 $W$ 中。
最低项给一个有理数规范核对：

$$
W(s)=\frac{17}{3}s+\frac{85}{42}s^2+\cdots,\qquad
A_2=s+\frac{394}{15}s^2+\cdots,\quad
B=s+\frac{64}{15}s^2+\cdots.
$$

再用 $s=z^4-\tfrac25z^8+\cdots$，原 $z^8$ 系数分别是
$388/15$、$58/15$，与 R117 的独立两行校准一致。

例如惰性 $p=4r-1\ge7$ 时，$W$ 的前 $r-1$ 个系数均 $p$ 整，
$[s^r]W$ 的赋值恰为 $-1$：乘积中分母第一次出现 $p$
是在 $4(r-1)+3=p$，此前分子、分母及 $r$ 均为 $p$ 单位。
这仅校准已知首坏项，不代表更深层已经可忽略。

为直接得到 R155 的 $F(V)$ 方程，记
$\mathcal A(s)=P(s)e^{W(s)}=F(V(s))$，并设

$$
C(s)=68+4(3-5s)\frac{P'}P
           +16s(1-s)\left(\frac{P''}P-\left(\frac{P'}P\right)^2\right).
\tag{2.4}
$$

链式法则给

$$
\begin{aligned}
&16s(1-s)(V')^2\bigl(FF_{VV}-F_V^2\bigr)\\
&\quad+\bigl(16s(1-s)V''+4(3-5s)V'\bigr)FF_V
                         =C(s)F^2.
\end{aligned}
\tag{2.5}
$$

其中 $s$ 取固定关系 $V=V(s)$ 的原点支。所有系数属于一个固定
代数函数域，与 $p$ 无关。这是二阶**非线性**方程；没有把它叫作
有限阶标量线性微分方程，也没有由 (2.5) 擅自推出
$\Lambda_p(V^jF)$ 的有界阶线性递推。

## 3. 只改变输出参数，不改变原平面源格

采用 R158§7/R159§7 的实际平面 $(A_2,B)$。
源的整幺三角基是

$$
A_2^{j-c}(B-A_2)^c=A_2^jV^c,
\qquad 0\le c\le j\le D.
\tag{3.1}
$$

现在用第一个原坐标本身作为输出参数，写

$$
X=A_2(z)=w+O(w^2)=s+O(s^2).
\tag{3.2}
$$

逆级数 $s=s(X)$ 在 $\mathbb Q[[X]]$ 中唯一存在。
所有准确前缀核在 $w$ 与 $X$ 参数下完全相同；对消失至少 $k$ 阶的
输出，两个第 $k$ 系数相等，因为 (3.2) 的首系数是一。
这在每个 $p$ 处都是严格的饱和 jet 等距，**不要求**逆级数的其余
系数整，也没有把 $X$ 添加成第四个自由源变量。

所以可用以下同一个完整矩阵研究原范数：

$$
\mathcal B_{k;(j,c)}=[X^{k-j}]\,V(s(X))^c,
\qquad 0\le c\le j\le D.
\tag{3.3}
$$

负指标为零。$c=0$ 时它准确是 $\mathbf1_{k=j}$；
$c>0$ 且 $k\le j$ 时为零。下节处理全部其余条目。

## 4. 原全部深度的 Lagrange／留数公式

令 $n=k-j>0$、$c\ge1$。因为 $X=P(s)e^{W(s)}$，
Lagrange 反演严格给

$$
\boxed{\quad
\mathcal B_{k;(j,c)}
 =\frac c n [s^{n-1}]
       V(s)^{c-1}V'(s)\,p_0(s)^{-n}e^{-nW(s)}.
\quad}
\tag{4.1}
$$

证明也可直接用同一个留数核，避免任何逆级数精度猜测：

$$
\begin{aligned}
\mathcal B_{k;(j,c)}
 &=\operatorname{Res}_{s=0}
                  V(s)^c\mathcal A'(s)\mathcal A(s)^{-n-1}\,ds\\
 &=\frac c n\operatorname{Res}_{s=0}
                  V(s)^{c-1}V'(s)\mathcal A(s)^{-n}\,ds.
\end{aligned}
$$

第二步是 $d(V^c\mathcal A^{-n})$ 的留数为零；
$\mathcal A^{-n}=s^{-n}p_0^{-n}e^{-nW}$ 随即给 (4.1)。

所有输入都是固定有理系数，只需到 $s^{n-1}$ 的有限 jet。
然而显示的 $n$ 分母必须保留，指数中的真实整数也是
$n=k-j$，不是原源的 theta 次数 $j$。
不能在对 $j$ 逐列变化时把它们偷偷替换成同一个单位。

为使全部权的计算／比较有统一规范，定义固定级数

$$
G(s)=\log p_0(s)+W(s)=\sum_{m\ge1}g_ms^m,
\qquad
\mathcal U_n(s)=e^{-nG(s)}=\sum_{m\ge0}u_m(n)s^m.
$$

有精确递推及卷积

$$
u_0(n)=1,\qquad
m\,u_m(n)=-n\sum_{h=1}^m h g_h\,u_{m-h}(n),
\tag{4.2}
$$

$$
u_m(n+n')=\sum_{h=0}^m u_h(n)u_{m-h}(n').
\tag{4.3}
$$

对固定 $m$，$u_m(n)\in\mathbb Q[n]$，次数至多 $m$。
式 (2.3)、固定多项式 $p_0$、(4.2) 和 (4.1) 因而给出了
任意 $D,k$ 的实际有限矩阵，不涉及未定周期或另选局部测度。

## 5. 与尚未支付的预算之间的精确距离

(4.1) 把实际全部深度交给同一个固定 $G$，但没有省掉以下数据：

- 源范围仍是 $0\le c\le j\le D$，不包含任意自由 $V^a$ 列。
- 每一列的指数是 $-(k-j)G$，含完整正 theta 连接 $W$。
- 每一列都有真实的 $c/(k-j)$，并且要在原饱和前缀中共同消元。
- 两条原中央导数共同为零，只是 R155 的两个实际 Mellin 条件，
  不等于 (4.2) 的全部 $u_m(n)$ 被额外的 $p$ 除。

因此下一步可以在这个明确矩阵中尝试同一有限差分或同一微分行，
并以 R151 的最大子式之差核算净收益。不能仅由 (4.2) 的多项式
依赖或 (2.5) 的有限微分阶数，就宣称已经得到有界阶 Mellin 递推。
所需惰性预算仍是 R159 的真实平面门槛
$a_I+2b_I<2$；本文未证明这个严格不等式。

## 依赖

- [R117 的固定两行恒等式](2026-11-12-two-rank-two-theta-linear-convolution.md)
  给 (1.2)–(1.4) 的原始多项式与尺度。
- R57/R38 的原整数流给 (1.1)；(2.1)–(2.5) 由本文逐式推导。
- [R155](../results/R155-two-theta-rows-common-amice-lattice.md)、
  [R158](../results/R158-ordinary-saturated-jets-and-degree-sensitive-budget.md)
  固定了真实源、Mellin 行及普通成本；本篇未改变这些对象。
- [R159 的直接 slopes 命题](2026-11-12-degree-sensitive-jets-and-direct-slope-boundary.md)
  给最后所述严格惰性门槛。
