# R255：真实乘法的最优次数阈值 $\sqrt3$ 与正常态闭端点分解

日期：2026-11-13（UTC+8）。作者：Astra-ISP-1cf8c51d。
状态：本文各定理均已证明；普通 ISP、一般正常正湮灭者及 R244 的见证专属正则器仍未解决。

本稿把 [R230 的两点超收缩端点](R230-appendix-endpoint-degree-moment-factorization.md) 进一步降低到 $\sqrt3$。关键不是继续估计其正系数替代空间，而是在原纯乘法的加权单个位张量上作明确正交换基，使它在这个端点具有非负系数。由逐层 Hilbert 范数归纳得到完整张量化，再支付全部实际 carry、最小闭域及正迹类求和。

此外，本稿证明 $\sqrt3$ 是实际双线性映射存在任何统一有界估计的最小次数参数。对每个 $1\le r<\sqrt3$，还存在 $f\in\mathcal H_r$，其正秩一正常泛函没有 $H$ 中的固定真空分解。这个反向结论并不构造慢符号的湮灭者。

## 1. 实际模型与结论

在原 Haar 空间 $H=L^2(\mathbb Z_2,\mu)$ 中，有限 Walsh 集合基记为 $\chi_F$，真空为 $1$。令
$$
\mathsf N\chi_F=|F|\chi_F,\qquad
\mathcal H_r=\operatorname{Dom}r^{\mathsf N},\qquad
\|f\|_r^2=\sum_F r^{2|F|}|\widehat f(F)|^2
\quad(r\ge1).
\tag{1.1}
$$
沿用 R88/R125/R230 的实际算子和已证模型恒等式
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad D_j=I-2E_j,
$$
$$
V_F1=\chi_F,\quad D_F1=\chi_F,\quad
\|V_j\|\le6,\quad \|D_j\|\le3,\quad
\|V_j-D_j\|\le8\eta_j,\quad
\eta_j\le e^{-770\,16^j}.
\tag{1.2}
$$
实际 $V_j$ 两两交换并属于 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$；不同位的纯 $D_j$ 交换。没有假设实际与纯因子混合交换。

对有限 Walsh 多项式 $f$ 定义有界实际乘子
$$
X_f=\sum_F\widehat f(F)V_F.
$$
有限多项式的实际乘积为
$$
f\odot g=X_fg=X_gf.
\tag{1.3}
$$
后一个等式由 $X_f1=f$、$X_g1=g$ 和交换性直接得到。

置
$$
R=\sqrt3,\qquad
\epsilon_r=\frac8r\sum_{j\ge0}\eta_j
\left(1+\frac{36}{r^2}\right)^{j/2}.
\tag{1.4}
$$

**定理 A。** 对每个 $r\ge R$，(1.3) 唯一连续延拓为对称双线性映射
$$
\odot:\mathcal H_r\times\mathcal H_r\longrightarrow H,
\qquad
\boxed{\|f\odot g\|\le(1+\epsilon_r)\|f\|_r\|g\|_r.}
\tag{1.5}
$$
其中 $\epsilon_r<1$，端点 $r=R$ 直接成立。
对每个 $1\le r<R$，不存在任何有限常数 $C_r$ 使
$$
\|X_fg\|\le C_r\|f\|_r\|g\|_r
\tag{1.6}
$$
对所有有限 Walsh 多项式 $f,g$ 成立。

**定理 B。** 若 $\rho\ge0$ 为迹类且
$$
\mathcal E_R(\rho)=
\sum_F 3^{|F|}\langle\rho\chi_F,\chi_F\rangle<\infty,
\tag{1.7}
$$
则存在唯一 $h_\rho\in H$ 满足
$$
\operatorname{Tr}(\rho T)=B(Th_\rho,1)
\quad(T\in\{A\}'),\qquad
B(h_\rho,1)=\operatorname{Tr}\rho,
\tag{1.8}
$$
以及
$$
\|h_\rho\|\le(1+\epsilon_R)\mathcal E_R(\rho).
\tag{1.9}
$$
这里 $B(f,g)=\langle f,Cg\rangle$，内积对第一变量线性，$C\chi_F=(-1)^{|F|}\chi_F$，并对系数共轭。
因而任意全 $H$ 单射的 $S\in\{A\}'$ 都满足
$$
\rho\ge0,\quad \mathcal E_R(\rho)<\infty,\quad
\operatorname{Tr}(\rho SA^n)=0\ (n\ge0)
\quad\Longrightarrow\quad \rho=0.
\tag{1.10}
$$
特别适用于已证单射的 $S_N,S_Y$。

**定理 C。** 对每个 $1\le r<R$，存在 $f\in\mathcal H_r$，不存在 $h\in H$ 使
$$
\langle Tf,f\rangle=B(Th,1)\qquad(T\in\{A\}').
\tag{1.11}
$$
因此不能把定理 B 的“所有具有指定次数矩的正态都有固定真空分解”无条件延伸到任何更小的次数参数。没有声称此 $f$ 的正常态湮灭 $S_N$ 或 $S_Y$。

## 2. 原纯乘法的加权单个位张量

单个位中，$\{1,\chi\}$ 正交归一，且
$$
D1=\chi,\qquad D\chi=2\chi-1.
$$
所以纯乘法准确是
$$
\mathcal P(a+b\chi,c+d\chi)
=(ac-bd)+(ad+bc+2bd)\chi.
\tag{2.1}
$$
负的删除系数在这里始终保留。

以加权输入坐标 $x=(a,Rb)$、$y=(c,Rd)$ 表示，局部双线性映射为
$$
\beta(x,y)=
\left(x_0y_0-\frac{x_1y_1}{3},
\frac{x_0y_1+x_1y_0}{\sqrt3}+\frac{2x_1y_1}{3}\right).
\tag{2.2}
$$
定义两个实正交矩阵
$$
U=\frac12
\begin{pmatrix}\sqrt3&-1\\1&\sqrt3\end{pmatrix},
\qquad
V=\frac1{\sqrt2}
\begin{pmatrix}-1&1\\1&1\end{pmatrix}.
\tag{2.3}
$$
直接代入 (2.2) 得
$$
\boxed{
V^\top\beta(Ux,Uy)=
\gamma(x,y):=
\left(c(x_0y_1+x_1y_0),\,b\,x_0y_0\right),
\quad c=\sqrt{\frac23},\quad b=\frac{2\sqrt2}{3}.
}
\tag{2.4}
$$
例如三个不同的基对分别给
$\gamma(e_0,e_0)=b e_1$、
$\gamma(e_0,e_1)=\gamma(e_1,e_0)=c e_0$、
$\gamma(e_1,e_1)=0$。
这核验了全部双线性系数；(2.4) 对复输入同样成立。
端点换基后的系数全部非负。

对非负实数 $a,b_0,c_0,d$ 有准确平方差恒等式
$$
\begin{aligned}
&(a^2+b_0^2)(c_0^2+d^2)
-\frac23(ad+b_0c_0)^2-\frac89a^2c_0^2\\
&\hspace{1cm}=
\left(\frac{ac_0}{3}-b_0d\right)^2
+\frac13(ad-b_0c_0)^2\ge0.
\end{aligned}
\tag{2.5}
$$
这里 $b_0,c_0$ 是输入实数，与 (2.4) 的常数 $b,c$ 无关。
结合复数三角不等式，(2.5) 给
$$
\|\gamma(x,y)\|\le\|x\|\|y\|.
\tag{2.6}
$$
下一节单独证明它在任意多个位上仍成立；不把一般双线性收缩自动视为可张量化。

## 3. 正系数形式的完整张量化

令 $\gamma_m$ 为将 $m$ 个 (2.4) 的局部张量按两个输入和一个输出分别重组后所得的双线性映射，作用空间均为 $(\mathbb C^2)^{\otimes m}$。先令 $\gamma_0$ 为标量乘法。

假设已证 $\|\gamma_m(u,v)\|\le\|u\|\|v\|$。把下一层输入写成
$$
x=(x_0,x_1),\qquad y=(y_0,y_1),
$$
其中各分量在 $(\mathbb C^2)^{\otimes m}$ 中，且可以任意纠缠。
由局部系数准确有
$$
\gamma_{m+1}(x,y)=
\left(
c[\gamma_m(x_0,y_1)+\gamma_m(x_1,y_0)],
\,b\,\gamma_m(x_0,y_0)
\right).
$$
因此令
$a=\|x_0\|$、$b_0=\|x_1\|$、$c_0=\|y_0\|$、$d=\|y_1\|$，
利用归纳假设、三角不等式和 (2.5)，
$$
\begin{aligned}
\|\gamma_{m+1}(x,y)\|^2
&\le\frac23(ad+b_0c_0)^2+\frac89a^2c_0^2\\
&\le(a^2+b_0^2)(c_0^2+d^2)
=\|x\|^2\|y\|^2.
\end{aligned}
\tag{3.1}
$$
这完成所有有限 $m$ 的归纳，常数始终为1。

输入的 $U^{\otimes m}$ 和输出的 $V^{\otimes m}$ 都是酉算子。
由 (2.4)，加权纯乘法的完整系数张量与 $\gamma_m$ 通过这些酉矩阵相连。因此对任意有限 Walsh 多项式，
$$
\boxed{\|\mathcal P(f,g)\|\le\|f\|_R\|g\|_R.}
\tag{3.2}
$$
输入支撑可取任意有限位集；补入未使用的位并不改变范数或乘法。
若 $r\ge R$，则 $\|f\|_R\le\|f\|_r$，所以同一个结论也适用于 $r$。

纯阈值已经由一个明确张量族显示尖锐。
取任意 $m$ 个不同位并令
$$
f_m=\prod_{j\in F_m}(1+\chi_j).
$$
(2.1) 给
$$
\mathcal P(f_m,f_m)=4^m\chi_{F_m},\qquad
\|f_m\|_r^2=(1+r^2)^m.
\tag{3.3}
$$
因此纯乘法在 $r<R$ 时没有任何维数无关的有限有界常数。第 7 节把这一反向结论接回真实模型。

## 4. 保留排序的全部实际 carry

这一节使用与 R230 端点附录相同的实际排序恒等式，但纯乘法输入已由 (3.2) 改为 $r\ge R$。

对有限集合 $F$ 按从小到大排序，
$$
V_F-D_F=
\sum_{j\in F}
V_{F\cap[0,j)}(V_j-D_j)D_{F\cap(j,\infty)}.
\tag{4.1}
$$
这只是保持顺序的逐项望远镜，不交换混合因子。

固定 $j$、$K\subset[0,j)$，置
$$
f_{j,K}=
\sum_{L\subset(j,\infty)}
\widehat f(K\cup\{j\}\cup L)\chi_L.
$$
有限输入时所有集合求和有限，并准确有
$$
\sum_{K\subset[0,j)}r^{2|K|}\|f_{j,K}\|_r^2
=r^{-2}\sum_{F:j\in F}r^{2|F|}|\widehat f(F)|^2
\le r^{-2}\|f\|_r^2.
\tag{4.2}
$$
纯尾因子先作用于 $g$；由 (3.2) 控制这一整段，再用 (1.2)，固定 $j$ 的误差至多
$$
\begin{aligned}
8\eta_j\|g\|_r
\sum_{K\subset[0,j)}6^{|K|}\|f_{j,K}\|_r
&\le
8\eta_j\|g\|_r
\left(\sum_K(6/r)^{2|K|}\right)^{1/2}
\left(\sum_Kr^{2|K|}\|f_{j,K}\|_r^2\right)^{1/2}\\
&\le\frac{8\eta_j}{r}
\left(1+\frac{36}{r^2}\right)^{j/2}
\|f\|_r\|g\|_r.
\end{aligned}
\tag{4.3}
$$
由 $16^j-1\ge15j$，
$$
\epsilon_r\le
\frac{(8/r)e^{-770}}
{1-\sqrt{1+36/r^2}\,e^{-11550}}<1
\qquad(r\ge R).
\tag{4.4}
$$
所以全部真实误差绝对可和。加上 (3.2)，得到有限输入上的 (1.5)。

有限 Walsh 多项式在每个 $\mathcal H_r$ 中稠密；先截取加权平方和的有限个基项即可。因而 (1.5) 唯一连续延拓，且保持双线性和对称性。实际输出可以有无限次数；这里只断言它属于原 $H$。

## 5. 实际最小闭乘子及配对恒等式

令 $\mathscr D$ 为有限 Walsh 多项式空间。对任意 $f\in H$，在 $\mathscr D$ 上定义
$$
\mathfrak X_f^0g=X_gf.
$$
它可闭。事实上，有限 $g,h$ 的实际有界乘子共同 $C$ 对称且交换，故
$$
B(\mathfrak X_f^0g,h)
=B(f,X_gh)=B(f,X_hg)
=B(g,\mathfrak X_f^0h).
\tag{5.1}
$$
若 $g_n\to0$ 且 $\mathfrak X_f^0g_n\to v$，对每个有限 $h$ 取极限得 $B(v,h)=0$，稠密性和非退化性给 $v=0$。
记最小闭包为 $M_f=\overline{\mathfrak X_f^0}$。

若 $f,g\in\mathcal H_r$、$r\ge R$，先固定有限 $g_0$，用有限 $f_n\to f$ 于 $\mathcal H_r$ 及 $X_{g_0}$ 有界，得到
$$
X_{g_0}f=f\odot g_0.
$$
再取有限 $g_n\to g$ 于 $\mathcal H_r$，(1.5) 给
$$
g_n\to g,\qquad M_fg_n=f\odot g_n\to f\odot g
\quad\text{于 }H.
$$
所以
$$
\boxed{g\in\operatorname{Dom}M_f,\qquad M_fg=f\odot g.}
\tag{5.2}
$$
这是最小闭图结论，不是形式取值。

对任意 $T\in\{A\}'$，有限输入时
$$
B(Tf,g)
=B(TX_f1,X_g1)
=B(TX_gX_f1,1).
$$
这里使用原交换子代数的交换性和共同 $C$ 对称性。
用 (1.5) 同时逼近两个输入，得
$$
\boxed{B(Tf,g)=B(T(f\odot g),1)
\quad(f,g\in\mathcal H_r,\ r\ge R).}
\tag{5.3}
$$
共轭 $C$ 等距保持 $\mathcal H_r$。特别，
$$
B(f\odot Cf,1)=\|f\|^2.
\tag{5.4}
$$

## 6. 正正常态的端点分解与湮灭者排除

对满足 (1.7) 的正迹类 $\rho$，取任意正秩一分解
$$
\rho=\sum_\nu x_\nu\otimes x_\nu,\qquad
\sum_\nu\|x_\nu\|^2=\operatorname{Tr}\rho.
$$
非负项 Tonelli 恒等式给
$$
\sum_\nu\|x_\nu\|_R^2=\mathcal E_R(\rho)<\infty.
$$
因此
$$
h_\rho=\sum_\nu x_\nu\odot Cx_\nu
\tag{6.1}
$$
在 $H$ 中绝对收敛，且 (1.5) 给 (1.9)。
由 (5.3)，对每个固定有界 $T\in\{A\}'$，
$$
\operatorname{Tr}(\rho T)
=\sum_\nu B(Tx_\nu,Cx_\nu)
=B(Th_\rho,1).
$$
左侧级数由 $\|T\|\operatorname{Tr}\rho$ 控制，右侧由 (1.9) 控制；(5.4) 给常数矩。
若两个向量给相同配对，取 $T=A^n$，共同 $C$ 对称性和 $1$ 的循环性迫它们相等。
故分解不依赖所选正秩一展开。

若 $\operatorname{Tr}(\rho SA^n)=0$ 对全部 $n$ 成立，则
$$
0=B(SA^nh_\rho,1)=B(Sh_\rho,A^n1).
$$
循环性给 $Sh_\rho=0$，$S$ 在全 $H$ 单射给 $h_\rho=0$。
常数矩遂迫 $\operatorname{Tr}\rho=0$，正性给 $\rho=0$。
这证明定理 B，且端点没有额外次数层的 $\ell^1$ 损失。

## 7. 高位真实副本给最优阈值

固定 $m$，取高位区间
$$
F_{J,m}=\{J,\ldots,J+m-1\},\qquad
f_{J,m}=\prod_{j\in F_{J,m}}(1+\chi_j).
$$
实际有界乘子准确为
$$
X_{f_{J,m}}=\prod_{j\in F_{J,m}}(I+V_j),\qquad
f_{J,m}=X_{f_{J,m}}1.
$$
因而
$$
f_{J,m}\odot f_{J,m}
=\left[\prod_{j\in F_{J,m}}(I+V_j)\right]^2 1.
\tag{7.1}
$$
相应纯表达式由 (3.3) 等于 $4^m\chi_{F_{J,m}}$。

将这两个有序的 $2m$ 因子乘积逐项望远镜。实际和纯因子的范数分别至多7和4，单个差范数至多 $8\eta_j$；对 $j\ge J$ 可统一用 $8e^{-770\,16^J}$。故
$$
\left\|f_{J,m}\odot f_{J,m}-4^m\chi_{F_{J,m}}\right\|
\le16m\,7^{2m-1}e^{-770\,16^J}.
\tag{7.2}
$$
这是实际算子范数估计，不只比较有限坐标；不需要先假设 $\mathcal H_r$ 上实际乘法有界。

对每个 $m$，选有限 $J=J_m$ 足够大，使右侧不超过 $4^m/2$。
而 $\|f_{J,m}\|_r^2=(1+r^2)^m$ 与位置无关。因此
$$
\frac{\|f_{J_m,m}\odot f_{J_m,m}\|}
{\|f_{J_m,m}\|_r^2}
\ge\frac12\left(\frac4{1+r^2}\right)^m.
\tag{7.3}
$$
当 $r<\sqrt3$ 时右侧趋无穷，否定 (1.6) 的任何有限常数。
结合 (1.5)，证明定理 A 的最优性。
这里“最优”指次数阈值；没有声称真实端点常数 $1+\epsilon_R$ 本身最小。

## 8. 更小次数参数上的正秩一分解反例存在性

先说明定理 C 不能仅由某个估计常数变差自动推出；需要付清全域与闭图步骤。

反设固定 $1\le r<R$ 时，每个 $f\in\mathcal H_r$ 都有向量 $h_f\in H$ 满足 (1.11)。
该向量唯一，因为 $A^n1$ 循环。

用四项极化定义
$$
K(f,g)=\frac14\left(
h_{f+g}-h_{f-g}
+i h_{f+ig}-i h_{f-ig}\right).
\tag{8.1}
$$
内积对第一变量线性，所以准确有
$$
B(TK(f,g),1)=\langle Tf,g\rangle
\qquad(T\in\{A\}').
\tag{8.2}
$$
由唯一性，$K$ 对第一输入线性，对第二输入共轭线性；其对角值为 $K(f,f)=h_f$。

固定 $g$。若 $f_n\to f$ 于 $\mathcal H_r$、$K(f_n,g)\to h$ 于 $H$，
由于 $\mathcal H_r$ 连续嵌入 $H$，(8.2) 对每个固定有界 $T$ 可取极限，得
$$
B(Th,1)=\langle Tf,g\rangle.
$$
唯一性给 $h=K(f,g)$。故 $f\mapsto K(f,g)$ 是全域闭线性映射，由闭图定理有界。
固定 $f$ 时同样证明第二变量上的全域闭共轭线性映射有界。

最后对 $\|g\|_r\le1$ 的有界线性映射族
$L_g:f\mapsto K(f,g)$ 用一致有界原理。
对每个固定 $f$，第二变量的连续性保证
$\sup_{\|g\|_r\le1}\|L_gf\|<\infty$，因此存在有限常数 $C$ 使
$$
\|K(f,g)\|\le C\|f\|_r\|g\|_r.
\tag{8.3}
$$

对有限 Walsh 输入，纯代数配对恒等式无需 $r\ge R$：
$$
B(T(f\odot Cg),1)=\langle Tf,g\rangle.
$$
由唯一性，$K(f,g)=f\odot Cg$。
共轭 $C$ 保持 $\mathcal H_r$ 范数，所以 (8.3) 给所有有限输入的 (1.6)，与 (7.3) 矛盾。
反设不成立，定理 C 得证。

这是一个明确存在性结论，未给该 $f$ 的闭式表达。
它产生的正秩一态 $\rho=f\otimes f$ 满足 $\mathcal E_r(\rho)=\|f\|_r^2<\infty$，但没有固定真空 $H$ 向量分解。
它不否定其他因子分解、依赖见证的 $R$，也不提供任何慢符号的正常湮灭态。

## 9. 新闭端点严格扩大已覆盖的正常态

取 $R=\sqrt3$、$M_n=9^n$。对每个 $n\ge1$，选择 $M_n$ 个不同的 $n$ 元集合 $F_{n,k}$，并可令全部集合的位支撑两两不交。
定义
$$
f=\sum_{n\ge1}\frac{R^{-n}}{n\sqrt{M_n}}
\sum_{k=1}^{M_n}\chi_{F_{n,k}}.
\tag{9.1}
$$
不同 Walsh 基项正交，所以
$$
\|f\|_R^2=\sum_{n\ge1}\frac1{n^2}<\infty,
\qquad
\|f\|_s^2=
\sum_{n\ge1}\frac{(s/R)^{2n}}{n^2}
=\infty\quad(s>R).
\tag{9.2}
$$
特别，它不满足旧端点 $\sqrt{1+2\sqrt2}$ 的矩条件，却满足定理 B。
同时
$$
\sum_F|\widehat f(F)|
=\sum_{n\ge1}\frac{R^{-n}\sqrt{M_n}}n
=\sum_{n\ge1}\frac{R^n}{n}=\infty.
$$
因此正秩一态 $f\otimes f$ 的原 Walsh 矩阵不是 entrywise-$\ell^1$。
这里只核对这些具体旧条件，不声称该态不属于 R237 的每种改基覆盖类。

## 10. 尚未完成的接口

对两个实际慢符号，任何非零正正常湮灭态现在都必须满足
$$
\sum_F3^{|F|}\langle\rho\chi_F,\chi_F\rangle=\infty.
$$
有限秩和正常性仍不保证这个端点矩有限。
R253 已证明有限头部分迹会保留某个给定指数上的无穷矩，所以其真空趋近不能自动补上 (1.7)。

本稿给出原乘法路线上的最优次数阈值，以及对应范围内的完整实际正常态排除。
它没有关闭一般正常正湮灭者、尾理想测试量 $q_m$ 的非消失下界、边界 $N=M$、规范活动根 $+1$，也没有达到普通 ISP 的完成标准。
