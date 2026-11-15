# R636 — 原两临界行的有理替代、真实 Cartier 返回与完整曲率缺陷

日期：2026-11-15。**状态：下述有理函数恒等式、原有限窗口比较及四条临界行及前五块的完整返回均已证明。**

本篇不把 R639 的整形式因子认作椭圆函数。另行构造一个完全指定的
$k(E_b)$ 中有理函数，它与原六次 sigma 来源在所需的整个窗口一致。
因此 R624 的两个首行及两个第二行确可交给同一椭圆函数域上的 Cartier
算子。全局连接仍有非零 $p$ 曲率；其缺陷、真实极点和来源成本均保留。
没有证明最后的二乘二行列式非零，也没有增加原中央零条件。

## 1. 同一曲线、同一 Gaussian 和整窗口

取
$$
p=6s-1>71,\qquad b=17,\qquad d=p+1,\qquad
L=\frac{p^2-1}{6},\qquad w=z^6,
$$
并在完美剩余域 $k$ 上使用
$$
E_b:y^2=x^3+b,\qquad \omega_E=\frac{dx}{2y},\qquad
Dx=2y,\quad Dy=3x^2.
\tag{1}
$$
原点展开为 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$。
令
$$
c=[w^s]\log(\sigma/z),\qquad
\sigma^\circ=\sigma\exp(-cz^d),\qquad
\zeta^\circ=D\log\sigma^\circ=\zeta-dcz^p.
\tag{2}
$$
这是 R356、R614、R624 的原规范，特别
$[z^p]\zeta^\circ=0$ 为特征零的准确等式。

R614 的原 addition 整性说明
$(\sigma^\circ/z)_n$ 在全部 $n<L$ 整。
同一范围中原 $x,y$ 及 $z=u\mathsf H(bu^6)$ 所需的系数亦整。
以下涉及 $z$ 的模 $p$ 计算均在这个已付有限窗口进行。
可取整的截断参数 $z_0(u)$ 到 $u^{p^2-2}$；其
$Dz_0=1+O(u^{p^2-1})$。本篇至多作 $p$ 次导数、读取 $7p$ 以下的
系数，故 $p>71$ 保证这些计算与原 $z$ 完全相同。
不把整个特征零形式对数直接约化成全局函数。

回顾 R356、R587 的实际有理函数
$$
\mathscr R_p(x)=\frac12\sum_{j=0}^{3s-1}
 \binom{3s-1}{j}b^{3s-1-j}\frac{x^{3j+1}}{3j+1},
\qquad Z=\frac{\mathscr R_p(x)}{y^p},
$$
$$
G=\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
\qquad r=\frac{x^2}{y},\qquad H_G=G+r.
\tag{3}
$$
所有显示分母均为单位。原完整等式为
$$
DZ=1,\quad D^p=0,\quad
Z=z+O(z^{5p}),\quad
DG=-x+c_pZ^{p-1},
$$
$$
c_p=\binom{3s-1}{2s-1}b^s\ne0,\qquad
D^{p-1}G=r^p,\qquad
H_G=\frac{3b}{5}z^5+O(z^{11}).
\tag{4}
$$
此外 $G$ 与 $\zeta^\circ$ 的 $z^p$ 系数都准确为零。
这些都是原有理来源；本篇没有另选一个有利的原函数。

## 2. 原有理对数比较的准确首缺陷

在比 R356 更长、但仍整的窗口内有
$$
\boxed{
\zeta^\circ-G=
\left(\frac{3b}{5}\right)^p z^{6p-1}+O(z^{6p}).
}
\tag{5}
$$
特别其第一个可能差异在 $6p-1$，而非用于本题两条临界行的较低次数。

先证差的阶数。由原 Gaussian 常数的准确约化，
$$
D\zeta^\circ=-x+c_pz^{p-1}.
$$
结合 (4)，
$$
D(\zeta^\circ-G)
=c_p(z^{p-1}-Z^{p-1})=O(z^{6p-2}).
\tag{6}
$$
差的主部相消。$G,\zeta^\circ$ 都是 $\mu_6$ 型 $-1$。
在 (6) 以下，导数看不见的项只能是 $z^{mp}$；
型条件要求 $m\equiv1\pmod6$。
唯一较低候选 $z^p$ 已由原规范准确消去，下一候选为 $z^{7p}$。
所以差至少为 $O(z^{6p-1})$。

写其首系数为 $a$。由于 $\zeta^\circ$ 是原整局部来源
$\sigma^\circ$ 的对数导数，所需有限窗口内有
$$
D^{p-1}\zeta^\circ+(\zeta^\circ)^p=0.
$$
这一局部等式可以先用一个具有同一有限 jet 的整 Laurent 级数延长证明，
不要求 $G$ 的全局连接平坦。
另一方面，(4) 给
$$
D^{p-1}G+G^p=H_G^p.
$$
在 $z^{5p}$ 处，差的 $p$ 次幂没有贡献，而
$$
D^{p-1}(a z^{6p-1})
=(p-1)!\,a z^{5p}=-a z^{5p}.
$$
故 $a=(3b/5)^p$，得 (5)。该系数是单位，但它仍不是
R624 的任一指定临界值。

## 3. 唯一的全局有理替代

在 $K=k(E_b)$ 上设
$$
\nabla=D-6G.
$$
R587 的完整曲率给
$$
\boxed{\nabla^p=-6H_G^p.}
\tag{7}
$$
右端是 $K^p$ 中非零乘法算子，因此 $\nabla$ 在这个
$p$ 维 $K^p$ 向量空间上可逆，且
$$
\nabla^{-1}=-\frac{\nabla^{p-1}}{6H_G^p}.
\tag{8}
$$

定义两个完全指定的有理函数
$$
\boxed{
Q_6=-\nabla^{p-1}(Z^5),\qquad
P_6=Z^pQ_6
=-\nabla^{p-1}(Z^{p+5}).
}
\tag{9}
$$
因 $D(Z^p)=0$，最后两式准确相同。Leibniz 公式及 Wilson 等式还给
$$
\boxed{
P_6=\sum_{j=0}^{p-1}\frac{(-Z)^j}{j!}\nabla^j(Z^6).
}
\tag{10}
$$
因此
$$
\boxed{
\nabla Q_6=6H_G^pZ^5,\qquad
\nabla P_6=6H_G^pZ^{p+5}.
}
\tag{11}
$$
(8) 说明 (11) 各自在整个 $K$ 内有唯一有理解。
这里没有添加任意水平函数，也没有把右边缺陷删掉。

在 $O$，$G=z^{-1}+O(z^5)$、$Z=z+\cdots$。
算子 $\nabla$ 保持 $z^6k[[z]]$，所以 (10) 显示
$$
P_6=z^6(1+\cdots),\qquad Q_6=z^{6-p}(1+\cdots).
\tag{12}
$$
$P_6$ 的型为 $0$，$Q_6$ 的型为 $+1$。

**原来源比较。** 有
$$
\boxed{
P_6\equiv(\sigma^\circ)^6\pmod{z^{6p+6}}.
}
\tag{13}
$$
证明：置 $F=(\sigma^\circ)^6$。由 (5)，
$\nabla F=6(\zeta^\circ-G)F=O(z^{6p+5})$；
(11) 的右边亦为 $O(z^{6p+5})$。
所以
$$
D(P_6/F)=O(z^{6p-1}).
$$
比值首项为一且型为 $0$。对 $1\le n<p$，
$D(z^{6n})=6n z^{6n-1}$ 的系数是单位。
因此比值的这些全部系数均为零，得到 (13)。
第一个可不被导数看见的型 $0$ 项在 $z^{6p}$，没有被宣称消失。

(13) 是完整的原有限窗口相等，不只是匹配四个采样值。

### 3.1 真实极点和成本

令 $\mathcal D_2$ 为三个非零二挠点之和。
$Z$ 只在 $\mathcal D_2$ 有极，单点极阶至多 $p$；
$G$ 只在 $O,\mathcal D_2$ 有极，在二挠点极阶至多 $p(p-1)$。
于是
$$
(Q_6)_\infty\le
(p-6)O+(p^3-2p^2+6p)\mathcal D_2,
$$
$$
(P_6)_\infty\le
(p^3-p^2+6p)\mathcal D_2.
\tag{14}
$$
在 $O$ 的准确阶数已由 (12) 支付。
这些是随 $p$ 增长的真实极帽，不能当成固定 degree6 theta 来源，
也不自动属于旧同预算的原 $M$ 列。

## 4. 四条原临界行的整个函数域返回

保持 R624 的原两来源
$$
f_4=x\sigma^6,\qquad f_1=-xy\sigma^6,
$$
并定义
$$
\mathfrak c_\ell=[w^{s-1}]\,z^{-\ell}e^{-6cz^d}f_\ell,\qquad
\mathfrak d_{\ell,2}=[w^{2s-1}]\,z^{-\ell}e^{-6cz^d}f_\ell.
\tag{15}
$$
它们在该窗口都整。这里的实际次数为
$$
\begin{array}{c|cc}
 &\mathfrak c_\ell&\mathfrak d_{\ell,2}\\ \hline
\ell=4&z^{p-1}&z^{2p}\\
\ell=1&z^{p-4}&z^{2p-3}.
\end{array}
$$

置
$$
A_4=xQ_6,\qquad A_1=-Z^3xyQ_6.
\tag{16}
$$
于是 $Z^pA_4=xP_6$，$Z^pA_1=-Z^3xyP_6$。
由 (13) 和 $Z=z+O(z^{5p})$，这些分别在全部所需次数内等于
$e^{-6cz^d}f_4$ 和 $z^3e^{-6cz^d}f_1$。
$Z$ 替换 $z$ 的误差高于两条第二行，不能在更长窗口中无条件忽略。

记 $\mathcal C$ 为同一曲线的 Cartier 算子，输出总以 $\omega_E$ 为基。
准确有
$$
\boxed{
\overline{\mathfrak c_\ell}
=\operatorname{Res}_O(A_\ell\omega_E),\qquad
\overline{\mathfrak d_{\ell,2}}
=\left(
 \frac{\mathcal C((A_\ell/Z)\omega_E)}{\omega_E}(O)
 \right)^p
=-D^{p-1}(A_\ell/Z)(O).
}
\tag{17}
$$

证明如下。$A_\ell$ 在 $O$ 的极阶至多 $p-4$，
而 $A_\ell/Z$ 的极阶至多 $p-3$。
Cartier 之后在 $O$ 至多有简单极。
又
$$
\mathcal C(Z^p A_\ell\omega_E)
=Z\,\mathcal C(A_\ell\omega_E),
$$
$$
\mathcal C(Z^{p-1} A_\ell\omega_E)
=Z\,\mathcal C((A_\ell/Z)\omega_E).
\tag{18}
$$
第一式在 $O$ 的值读出 $A_\ell\omega_E$ 的留数之 $p$ 次根，
其 $p$ 次方正是第一行。
第二式中 $A_\ell/Z$ 的函数型为 $4$，所以
$\mathcal C((A_\ell/Z)\omega_E)/\omega_E$ 的型为 $0$。
其至多简单的极被这个型排除，故它在 $O$ 正则。
利用 $Z(O)=0,DZ(O)=1$，第二式的首导数给第二行。

最后，因为 $DZ=1$，$Z$ 是 $K/K^p$ 的一个 $p$-基。
若 $B=\sum_{i=0}^{p-1}b_i^pZ^i$，则
$$
\mathcal C(B\omega_E)=b_{p-1}\omega_E,\qquad
D^{p-1}B=-b_{p-1}^p.
\tag{19}
$$
这给 (17) 的最后一个显示式，并说明该处的有理函数确实正则。

这里保留了原第二行的首 Frobenius jet。
它是通过 (9) 的准确 $Z^p$ 因子和 (18) 支付的；
没有从一次分部积分中删掉一个看不见的最高 Frobenius 常数。

### 4.1 首两行亦为同一个二挠点的实际留数

$A_4\omega_E,A_1\omega_E$ 都是 $\mu_6$ 不变有理微分，
除 $O$ 和三个非零二挠点外无极。
其三个二挠留数相等。
任取 $P_e=(e,0)$、$e^3=-b$，留数定理给
$$
\boxed{
\overline{\mathfrak c_4}
=-3\operatorname{Res}_{P_e}(xQ_6\omega_E),\qquad
\overline{\mathfrak c_1}
=3\operatorname{Res}_{P_e}(Z^3xyQ_6\omega_E).
}
\tag{20}
$$
可以在包含 $e$ 的有限剩余域扩张中读取，不改变原值。
对第二行，$A_4/Z$ 还可能在 $Z=0$ 的其他点有极；
这些点不能从全局 Cartier 计算中删除。

因此 R624 的准确目标为
$$
\boxed{
\mathfrak D_p=
\det\begin{pmatrix}
 \operatorname{Res}_O(xQ_6\omega_E)&
 -\operatorname{Res}_O(Z^3xyQ_6\omega_E)\\[2mm]
 -D^{p-1}(xQ_6/Z)(O)&
 D^{p-1}(Z^2xyQ_6)(O)
\end{pmatrix}.
}
\tag{21}
$$
这四个条目都来自同一 $Q_6$。公式没有把其中任何条目换成
R587 曲率单位、R630 的较高非线性单位或原 Hasse 常数。

### 4.2 完整伴随式

令 $\nabla_+=D+6G$。
Cartier 杀掉完整 exact 微分，故任意 $a,v\in K$ 满足
$$
\mathcal C(a\nabla v\,\omega_E)
=-\mathcal C((\nabla_+a)v\,\omega_E).
$$
反复 $p-1$ 次，结合 (9)，得到
$$
\boxed{
\mathcal C(aP_6\omega_E)
=-Z\,\mathcal C\!\left(
 Z^5\nabla_+^{p-1}a\,\omega_E
 \right).
}
\tag{22}
$$
此式可用于 (17) 的四个实际测试。
右边的全部有理极部和 $Z$ 因子均在，不将其拆成各自为零的项。

## 5. 第二个显式有理模型：一个 p-reduced 原函数和有限指数

还可将同一低窗口化为一个单变量有理函数的有限指数；
它不需要原 $\psi_p$ 的高精度整数提升作为额外输入。

由 $r=\tfrac13D\log y$ 及 $D^p=0$，
$$
D^{p-1}r=-r^p.
$$
结合 (4)，
$$
D^{p-1}H_G=0.
\tag{23}
$$
因此显示的有限和
$$
V_0=
\sum_{i=0}^{p-2}
 \frac{(-1)^i Z^{i+1}D^iH_G}{(i+1)!}
\tag{24}
$$
满足 $DV_0=H_G$。
它在 $O$ 正则、值为零、型为 $0$，并且只可能在非零二挠点有极。
令 $X=x^3$，于是
$$
V_0\in k(X),\qquad
V_0=\sum_{j\ge1}\frac{v_j}{(X+b)^j}
$$
为有限和。
删掉所有 $p\mid j$ 的项，得到唯一的 proper、$p$-reduced 原函数
$$
\boxed{
V_{\mathrm{red}}=
\sum_{\substack{j\ge1\\p\nmid j}}
 \frac{v_j}{(X+b)^j},\qquad
DV_{\mathrm{red}}=H_G.
}
\tag{25}
$$
删去的和是 $K^p$ 中的函数，其在 $O$ 从 $z^{6p}$ 起；
所以未改动本篇低窗口。
唯一性来自：两个这样的原函数之差在 $k(X)^p$ 中，
而 proper partial fractions 的 $p$ 次幂只有 $p$ 倍数指数。

这一表示有真实的度数帽：
$$
\boxed{
\deg_{(X+b)^{-1}}V_{\mathrm{red}}
\le \frac{p(p-1)}2-1,\qquad
V_{\mathrm{red}}=\frac b{10}z^6+O(z^{12}).
}
\tag{26}
$$
第一式由 $DV_{\mathrm{red}}=6x^2y\,\partial_XV_{\mathrm{red}}$ 证明。
若最高指数为 $j$，则 $p\nmid j$，在一个非零二挠点的极阶准确为
$2j+1$；而 $H_G$ 的极阶至多 $p(p-1)$。
第二式由 $H_G=(3b/5)z^5+\cdots$ 及原点值零得到。

定义真正有限的多项式，而非特征 $p$ 的无限指数：
$$
E_{p-1}(T)=\sum_{j=0}^{p-1}\frac{T^j}{j!},\qquad
\widehat P_6=\frac{E_{p-1}(6V_{\mathrm{red}})}{y^2}.
\tag{27}
$$
所有阶乘均为单位，$\widehat P_6$ 是完整有理函数。
准确求导给
$$
\boxed{
\nabla\widehat P_6
=\frac{6H_G(6V_{\mathrm{red}})^{p-1}}{y^2}.
}
\tag{28}
$$
右边在 $O$ 从 $z^{6p+5}$ 起，其首系数同样为
$6(3b/5)^p$。
又 $\widehat P_6=z^6(1+\cdots)$，故用第 3 节相同的局部比较得
$$
\boxed{
\widehat P_6\equiv P_6\equiv(\sigma^\circ)^6
 \pmod{z^{6p+6}}.
}
\tag{29}
$$
两个有理模型不被宣称全局相等。
(9) 的 $Z^pQ_6$ 分解及 (20) 的留数支持属于第一个模型；
若直接改用 (27)，须保持其自己的全部除子和 Cartier 测试。

(24)–(29) 给出一个完全在原 $k(E_b)$ 中执行的有限算法：
由原 $Z,G$ 算 $H_G$，作有限原函数，按 $X$ 作 proper partial fractions，
删去 $p$ 倍数极次，再取显示的有限指数。
它只恢复已说明的原模 $p$ 窗口，不把 R624 的四位除法数据要求
改成关于较浅除法数据的虚假结论。

## 6. 全 Gaussian 重标与完整中央规范

若 $c'=c+\eta$、$\eta\in\mathcal O$，取
$$
G_\eta=G-\bar\eta Z^p,\qquad
\nabla_\eta=D-6G_\eta.
\tag{30}
$$
R356 的原共振比较使第 2–4 节同样适用于
$\sigma\exp(-c'z^d)$。
这里保留整个有限算子
$$
Q_{6,\eta}
=-\sum_{j=0}^{p-1}
 \binom{p-1}{j}(6\bar\eta Z^p)^{p-1-j}\nabla^j(Z^5).
\tag{31}
$$
不能把全有理函数的变化只保留为一个局部剪切。
在指定两行上，准确变化则是
$$
\mathfrak c_\ell\longmapsto\mathfrak c_\ell,\qquad
\mathfrak d_{\ell,2}\longmapsto
\mathfrak d_{\ell,2}-6\bar\eta\,\mathfrak c_\ell,
\tag{32}
$$
所以 (21) 不变。
非零 $\eta$ 时 $G_\eta$ 在二挠点的极帽可升到 $p^2$；
例如 $P_{6,\eta}$ 的单点极帽应保为 $p^3+5p$，不继续套 (14) 的较小帽。

R639 的完整中央规范
$$
F_c=\Pi_0\log(\sigma/z),\qquad E_c=\exp F_c
$$
满足 $F_c-cz^d$ 从 $z^{2d}=w^{2s}$ 起。
所以 (15) 的两个窗口逐项不变，而不是仅行列式不变。
本篇的实际四行也因此适用于那个完整中央连接。
这不将 (13) 的全部 $n<p$ 比较范围扩给完整中央规范：
两种 gauge 在 $n=2s$ 起会不同。

## 7. 对原算术条件的准确意义

R624 已将原两个完整 Newton 导数同时为零时的条件写为
$$
\mathfrak c=-M^{-1}\mathfrak R_1,\qquad
\mathfrak d_2=-M^{-1}
 \left(\mathfrak R_2+C_s\operatorname{diag}(34,72)\,q\right),
\tag{33}
$$
其中 $M$ 是原固定单位矩阵，$\mathfrak R_1,\mathfrak R_2$
是原低卷积残差，$q$ 保留原第二位及形式对数项。
本篇把左边的同一四个数明确移到 (17)、(21) 的有理 Cartier 矩阵，
没有删除 (33) 的任何残差。

尤其：

- $\nabla$ 全局可逆不说明 (21) 在 $O$ 的二乘二块可逆。
- (5)、(26)、(28) 的单位首项都在明确的原次数上；
  它们不能代替 $\mathfrak c_4,\mathfrak c_1$ 或 $\mathfrak D_p$。
- 全部有理替代的极帽随 $p$ 增长；不能免费并入旧同 $R$ 的固定预算列。
- (17) 中的第二行确有全局 Cartier 意义，但尚需计算该指定值，
  而非从全局算子的非退化猜它非零。

新增输入是：唯一的曲率受控有理替代、全部 $n<p$ 的原六次 sigma 比较、
两条留数和两条真实 Cartier 值、整 Gaussian 重标的完整算子、
以及 proper $p$-reduced 有理原函数的第二种有限模型。
所有证明对允许的 $p$ 统一成立，没有新增目标素数扫描。


## 8. 原前五个中央块与第五块的准确坐标补项

仍使用 (2) 的首 Gaussian 规范，并将 (15) 扩为
$
\mathfrak d_{\ell,h}
=[w^{hs-1}]\,z^{-\ell}e^{-6cz^d}f_\ell,
\qquad 1\le h\le5,\qquad \mathfrak d_{\ell,1}=\mathfrak c_\ell.
\tag{34}
$
全部 $hs-1<p$，所以这些是 (13) 已付整窗口中的原实际系数。

(5)、(6) 还决定原有理参数的首个 Frobenius 差：
$
\boxed{
Z=z-\kappa_5z^{5p}+O(z^{5p+1}),\qquad
\kappa_5=\frac{(3b/5)^p}{c_p}\ne0.
}
\tag{35}
$
证明：若 $Z=z+A z^{5p}+\cdots$，则
$c_p(z^{p-1}-Z^{p-1})=c_p A z^{6p-2}+\cdots$；
(5) 的导数在该处是 $-(3b/5)^p z^{6p-2}$。
故 $A=-\kappa_5$。这个常数是原 $z,Z$ 的准确差，
不是可以通过重选原函数删除的自由量。

对 $2\le h\le5$ 定义
$
B_{\ell,h}
=\frac{\mathcal C(Z^{1-h}A_\ell\omega_E)}{\omega_E},
\qquad
T_{\ell,h}=
\left(\frac{D^{h-2}B_{\ell,h}(O)}{(h-2)!}\right)^p.
\tag{36}
$
这些求值全有定义。事实上 $Z^{1-h}A_\ell$ 在 $O$ 的极阶至多
$p+h-5\le p$，所以 Cartier 后至多有简单极。
其输出函数 $B_{\ell,h}$ 的 $\mu_6$ 型为 $h-2$。
$h-2=0,1,2,3$ 均排除 $z^{-1}$，因此 $B_{\ell,h}$ 正则，
且低于 $z^{h-2}$ 的项全零。

有完整的返回公式
$
\boxed{
\mathfrak d_{\ell,h}=T_{\ell,h}\quad(2\le h\le4),\qquad
\mathfrak d_{\ell,5}=T_{\ell,5}-\ell\kappa_5
\quad(\ell=4,1).
}
\tag{37}
$
所有式均在 $k$ 中；第一块继续由 (17) 的留数给出。

为核全部坐标和符号，设 $F_\ell^*=Z^pA_\ell$。
Cartier 的准确恒等式为
$
\mathcal C(Z^{1-h}F_\ell^*\omega_E)
=Z\,B_{\ell,h}\omega_E.
$
右边的 $z^{h-1}$ 系数为
$D^{h-2}B_{\ell,h}(O)/(h-2)!$。
因此 $T_{\ell,h}$ 正是左边原输入的
$z^{hp-1}$ 系数，即 $Z^{1-h}F_\ell^*$ 在该次数的系数。
对 $h\le4$，(35) 的差尚未进入目标，且 (13) 的误差也高于目标，
于是直接得到 (37) 的前式。

到 $h=5$ 必须同时保留两个真实变化：
$
Z^{-4}=z^{-4}+4\kappa_5z^{5p-5}+\cdots,\qquad
F_1^*=z^3e^{-6cz^d}f_1-3\kappa_5z^{5p+3}+\cdots.
\tag{38}
$
$F_4^*$ 与 $z^3e^{-6cz^d}f_1$ 的首项都是 $z^4$。
故 $T_{4,5}=\mathfrak d_{4,5}+4\kappa_5$，
而 $T_{1,5}=\mathfrak d_{1,5}+4\kappa_5-3\kappa_5$。
这就是 (37) 中两个不同的仿射项。
(13) 经 $x$ 或 $Z^3xy$ 乘后，其误差仍从 $z^{6p+4}$ 起，
严格高于这里的 $z^{5p+3}$，没有另一个未付误差。

### 8.1 完整中央 gauge 的三角变换仍须保留

第 6 节所说的逐项不变只涉及前两个块。
若使用 R639 的完整 $F_c$，写
$
\Gamma(X)
=\exp\!\left(-6\sum_{j\ge2}F_{js}X^j\right)
=\sum_{r\ge0}\gamma_rX^r,\qquad
\gamma_0=1,\quad\gamma_1=0,\quad X=w^s.
$
这里 $F_n=[w^n]\log(\sigma/z)$。
所需 $\gamma_2,\gamma_3,\gamma_4$ 均整：
$js<p$、$j=2,3,4$ 时，原
$F_{js}=-X_{js}/(6js(6js-1))$ 的两个分母都是单位，
而该范围的 $X_{js}$ 已整；指数展开用到的阶乘也为单位。

因此全中央规范的原系数准确为
$
\boxed{
\mathfrak d^{\,c}_{\ell,h}
=\sum_{r=0}^{h-1}\gamma_r\mathfrak d_{\ell,h-r}
\qquad(1\le h\le5).
}
\tag{39}
$
特别
$
\mathfrak d^{\,c}_{\ell,5}
=T_{\ell,5}-\ell\kappa_5
+\gamma_2T_{\ell,3}
+\gamma_3T_{\ell,2}
+\gamma_4\mathfrak c_\ell.
\tag{40}
$
不能把后三项或 (37) 的仿射项删除。
本节将前五个原块全部接回同一个 $Q_6$ 的实际 Cartier 行，
并精确支付首次进入窗口的 $z/Z$ 差；
它仍只是一组完整返回恒等式，没有给其中任一条新赋中央零。


依赖：
[R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)；
[R587](R587-inert-minimal-log-primitive-and-exact-gaussian-p-curvature.md)；
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R624](R624-original-paired-forcing-determinant-and-four-digit-division-return.md)；
[R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)。
