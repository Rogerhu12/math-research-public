# 正常泛函分解的两点超收缩端点及全部真实 carry

日期：2026-11-12（UTC）。独占作者：normal_next。

状态：以下端点双线性估计、最小闭域结论及正正常湮灭者排除都有完整证明。本稿把 [R230](../results/R230-normal-positive-chaos-factorization-and-annihilator-exclusion.md) 的充分次数参数 $r>9$ 降为闭端点
$$
r_*=\sqrt{1+2\sqrt2}.
$$
这仍是一个正则性条件；没有证明任意正常态具有该次数矩，也没有构造一般 R244 指定输入正则器。

## 1. 结论与实际模型输入

在原 Haar 空间 $H$ 中，$\{\chi_F\}$ 是有限集合 $F\subset\mathbb N_0$ 编号的 Walsh 正交基，$\mathsf N\chi_F=|F|\chi_F$。对 $r\ge r_*$，记
$$
\mathcal H_r=\operatorname{Dom}r^{\mathsf N},\qquad
\|f\|_r^2=\sum_F r^{2|F|}|\widehat f(F)|^2.
\tag{1.1}
$$
沿用实际有界交换子
$$
N_j=A^{2^j}/d_j,\qquad V_j=(I-N_j)(I+N_j)^{-1},
$$
以及纯局部因子 $D_j=I-2E_j$、$E_j=e_{10}^{(j)}$。R230 已核验的实际输入为
$$
V_F1=\chi_F,\quad \|V_j\|\le6,\quad
\|V_j-D_j\|\le8\eta_j,\quad
0<\eta_j\le e^{-770\,16^j}.
\tag{1.2}
$$
所有 $V_j$ 都在原 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$ 中并彼此交换；纯 $D_j$ 在不同位交换。以下不要求实际 $V_j$ 与任意纯 $D_k$ 交换。

对有限 Walsh 多项式 $f$，定义
$$
X_f=\sum_F\widehat f(F)V_F,
\qquad
\epsilon_r=\frac8r\sum_{j\ge0}\eta_j
\left(1+\frac{36}{r^2}\right)^{j/2}.
\tag{1.3}
$$
由 $16^j-1\ge15j$，
$$
0<\epsilon_r\le
\frac{(8/r)e^{-770}}
{1-\sqrt{1+36/r^2}\,e^{-11550}}<1.
\tag{1.4}
$$

**主定理。** 对全部 $r\ge r_*$，实际乘法唯一连续延拓为对称双线性映射
$$
\odot:\mathcal H_r\times\mathcal H_r\longrightarrow H,
\qquad
\boxed{\|f\odot g\|\le(1+\epsilon_r)\|f\|_r\|g\|_r.}
\tag{1.5}
$$
其有限多项式取值为 $f\odot g=X_fg=X_gf$。对任意 $f,g\in\mathcal H_r$，$g$ 属于 R230/R244 的最小闭乘子 $\overline{\mathfrak X_f^0}$ 的定义域，且该算子在 $g$ 的值准确为 $f\odot g$。

若 $\rho\ge0$ 为迹类且
$$
\mathcal E_r(\rho):=\sum_F r^{2|F|}\langle\rho\chi_F,\chi_F\rangle<\infty,
\tag{1.6}
$$
则有唯一 $h_\rho\in H$ 满足
$$
\boxed{
\operatorname{Tr}(\rho T)=B(Th_\rho,1)\quad(T\in\{A\}'),\qquad
B(h_\rho,1)=\operatorname{Tr}\rho,
}
\tag{1.7}
$$
$$
\boxed{\|h_\rho\|\le(1+\epsilon_r)\mathcal E_r(\rho).}
\tag{1.8}
$$
这里 $B(f,g)=\langle f,Cg\rangle$，内积对第一变量线性；原共轭满足 $C\chi_F=(-1)^{|F|}\chi_F$，所有实际有界交换子都为 $C$ 对称，$1$ 对 $A$ 循环。

因而对任意全 $H$ 单射的 $S\in\{A\}'$，
$$
\rho\ge0,\quad \mathcal E_r(\rho)<\infty,\quad
\operatorname{Tr}(\rho SA^n)=0\ (n\ge0)
\quad\Longrightarrow\quad \rho=0.
\tag{1.9}
$$
特别同时适用于两个实际慢符号 $S_N,S_Y$，并允许 $r=r_*$。

## 2. 一个带偏置的两点概率空间

令实随机变量 $Z$ 取值
$$
z_+=1+\sqrt2,\qquad z_-=1-\sqrt2,
$$
概率分别为
$$
p_+=\frac{\sqrt2-1}{2\sqrt2},\qquad
p_-=\frac{\sqrt2+1}{2\sqrt2}.
$$
直接得到
$$
\mathbb EZ=0,\quad \mathbb EZ^2=1,\quad
Z^2=1+2Z,\quad \mathbb EZ^3=2,\quad \mathbb EZ^4=5.
\tag{2.1}
$$
因此 $\{1,Z\}$ 是这个二维 $L^2$ 的正交归一基。定义线性噪声算子
$$
Q_t(a+bZ)=a+tbZ,\qquad 0\le t\le1.
$$

**单点引理。** 若 $0\le t\le r_*^{-1}$，则
$$
\|Q_tu\|_{L^4}\le\|u\|_{L^2}
\quad(u=a+bZ,\ a,b\in\mathbb C).
\tag{2.2}
$$

**证明。** 置 $R=\operatorname{Re}(a\overline b)$。由 (2.1) 准确展开，
$$
\mathbb E|a+tbZ|^4
=|a|^4+2t^2|a|^2|b|^2+4t^2R^2
+8t^3R|b|^2+5t^4|b|^4.
$$
用 $|R|\le|a||b|$，上式至多
$$
|a|^4+6t^2|a|^2|b|^2+8t^3|a||b|^3+5t^4|b|^4.
\tag{2.3}
$$
要将其控制在 $(|a|^2+|b|^2)^2$ 内，只需二次型
$$
(2-6t^2)x^2-8t^3xy+(1-5t^4)y^2
\tag{2.4}
$$
非负，其中 $x=|a|,y=|b|$。令 $u=t^2$。对应实对称矩阵的行列式为
$$
(2-6u)(1-5u^2)-16u^3
=2(1-3u-5u^2+7u^3)
=2(u-1)(7u^2+2u-1).
\tag{2.5}
$$
对于
$$
0\le u\le u_*:=\frac{2\sqrt2-1}{7}
=\frac1{1+2\sqrt2},
$$
两个对角元均正，(2.5) 非负，所以矩阵半正定，包括 $u=u_*$。结合 (2.3) 得 (2.2)。这个计算完整覆盖复系数。

单点条件本身在此端点尖锐：稍大于 $u_*$ 时两个对角元仍正而行列式负，(2.4) 在某个 $x,y>0$ 为负，取实同相 $a=x,b=y$ 就违反 (2.2)。这只说明此正系数控制方法中的单点常数尖锐，未宣称原实际双线性映射的最优阈值。证毕。

## 3. 明确的张量化及纯乘法控制

先付清张量化。设 $T:L^2(X)\to L^4(X)$ 和 $U:L^2(Y)\to L^4(Y)$ 均为收缩，其中 $X,Y$ 是有限概率空间。逐个 $y$ 应用 $T$ 的收缩性，再使用 $2\le4$ 的 Minkowski 混合范数不等式，得到
$$
\begin{aligned}
\|(T_xU_y)F\|_{L^4_y(L^4_x)}
&\le\|U_yF\|_{L^4_y(L^2_x)}\\
&\le\|U_yF\|_{L^2_x(L^4_y)}\\
&\le\|F\|_{L^2_x(L^2_y)}.
\end{aligned}
\tag{3.1}
$$
中间一步也可把左侧平方写为 $\|\sum_x\mu(x)|U_yF(x,y)|^2\|_{L^2_y}$，再直接用三角不等式。因此递归应用 (3.1) 证明
$$
\|Q_t^{\otimes m}F\|_{L^4}\le\|F\|_{L^2}
\qquad(t\le r_*^{-1})
\tag{3.2}
$$
对任意有限维数 $m$ 成立，常数与 $m$ 无关。

取 $m$ 个独立同分布的 $Z_j$，记 $Z_F=\prod_{j\in F}Z_j$。这些 $Z_F$ 是乘积 $L^2$ 的正交归一基。对有限 Walsh 多项式 $f$ 定义非负系数多项式
$$
f^{\#}(Z)=\sum_F|\widehat f(F)|Z_F.
$$
以 $t=r^{-1}$ 在 (3.2) 中输入 $\sum_Fr^{|F|}|\widehat f(F)|Z_F$，得到
$$
\boxed{\|f^{\#}\|_{L^4}\le\|f\|_r.}
\tag{3.3}
$$

纯局部乘法满足
$$
D_j\chi_G=
\begin{cases}
\chi_{G\cup\{j\}},&j\notin G,\\
2\chi_G-\chi_{G\setminus\{j\}},&j\in G.
\end{cases}
\tag{3.4}
$$
所以纯双线性乘积
$$
\mathcal P(f,g)=\left(\sum_F\widehat f(F)D_F\right)g
$$
在共同位的两个系数分别为保留的 $2$ 与删除的 $-1$。另一方面，$Z_j^2=1+2Z_j$ 给 $f^{\#}g^{\#}$ 的相同保留系数 $2$ 和非负删除系数 $1$。逐个输出集合比较，前者系数的绝对值至多后者系数。以两边各自的正交归一基计算平方和，再用 Hölder 和 (3.3)，得
$$
\boxed{
\|\mathcal P(f,g)\|_H
\le\|f^{\#}g^{\#}\|_{L^2}
\le\|f^{\#}\|_{L^4}\|g^{\#}\|_{L^4}
\le\|f\|_r\|g\|_r.
}
\tag{3.5}
$$
这里仅以另一个两点概率空间估计系数，未把原实际算子解释成该空间的点乘，也未把 $D_j$ 的负删除项丢在恒等式里。

## 4. 全部实际 carry 的加权排序预算

对任意有限集合 $F$，按从小到大的位顺序准确展开
$$
V_F-D_F
=\sum_{j\in F}
V_{F\cap[0,j)}(V_j-D_j)D_{F\cap(j,\infty)}.
\tag{4.1}
$$
该恒等式不交换任何实际与纯混合因子。

固定 $j$ 与 $K\subset[0,j)$，置
$$
f_{j,K}=\sum_{L\subset(j,\infty)}
\widehat f(K\cup\{j\}\cup L)\chi_L.
\tag{4.2}
$$
有限多项式情形全部求和有限，并有准确加权恒等式
$$
\sum_{K\subset[0,j)}r^{2|K|}\|f_{j,K}\|_r^2
=r^{-2}\sum_{F:j\in F}r^{2|F|}|\widehat f(F)|^2
\le r^{-2}\|f\|_r^2.
\tag{4.3}
$$
把 (4.1) 按 (4.2) 合并，尾纯因子先作用于 $g$。由 (3.5)，
$$
\left\|\sum_L\widehat f(K\cup\{j\}\cup L)D_Lg\right\|
\le\|f_{j,K}\|_r\|g\|_r.
$$
再用 (1.2) 和加权 Cauchy–Schwarz，固定 $j$ 的总误差至多
$$
\begin{aligned}
8\eta_j\|g\|_r\sum_{K\subset[0,j)}6^{|K|}\|f_{j,K}\|_r
&\le8\eta_j\|g\|_r
\left(\sum_K(6/r)^{2|K|}\right)^{1/2}
\left(\sum_Kr^{2|K|}\|f_{j,K}\|_r^2\right)^{1/2}\\
&\le\frac{8\eta_j}{r}
\left(1+\frac{36}{r^2}\right)^{j/2}\|f\|_r\|g\|_r.
\end{aligned}
\tag{4.4}
$$
对 $j$ 求和由 (1.3)—(1.4) 绝对控制。加上 (3.5)，得到有限输入上的 (1.5)。注意 carry 输出可以有无限次数；证明只要求它落在原 $H$，没有声称次数保持。

有限 Walsh 多项式在 $\mathcal H_r$ 中稠密：先对加权平方和截取有限多个基项即可。因此该实际双线性映射唯一连续延拓为 (1.5)。有限输入时 $X_f,X_g$ 交换并满足 $X_f1=f$、$X_g1=g$，所以 $X_fg=X_gf$；连续延拓保持对称性。

## 5. 最小闭域与有界交换子的配对

令 $\mathscr D$ 为有限 Walsh 多项式空间，对任意 $f\in H$ 定义
$$
\mathfrak X_f^0g=X_gf,\qquad g\in\mathscr D.
\tag{5.1}
$$
它稠密定义且可闭。为完整核验，若 $g,h\in\mathscr D$，有界交换子的 $C$ 对称性与 $X_gh=X_hg$ 给
$$
B(\mathfrak X_f^0g,h)=B(f,X_gh)
=B(f,X_hg)=B(g,\mathfrak X_f^0h).
\tag{5.2}
$$
若 $g_n\to0$ 且 $\mathfrak X_f^0g_n\to v$，对任意 $h\in\mathscr D$ 在 (5.2) 取极限得 $B(v,h)=0$。稠密性迫 $v=0$，故最小闭包 $\overline{\mathfrak X_f^0}$ 确实存在。

现在取 $f,g\in\mathcal H_r$。对固定 $g_0\in\mathscr D$，有限多项式 $f_n\to f$ 于 $\mathcal H_r$ 时，$X_{g_0}f_n\to X_{g_0}f$ 于 $H$，而 (1.5) 又给 $f_n\odot g_0\to f\odot g_0$。因此
$$
\mathfrak X_f^0g_0=f\odot g_0.
$$
再取 $g_n\in\mathscr D$ 在 $\mathcal H_r$ 中趋 $g$，(1.5) 给
$$
g_n\to g,\qquad \mathfrak X_f^0g_n\to f\odot g
\quad\text{于 }H.
$$
于是
$$
\boxed{g\in\operatorname{Dom}\overline{\mathfrak X_f^0},\qquad
\overline{\mathfrak X_f^0}g=f\odot g.}
\tag{5.3}
$$
这是实际最小闭图的结论，不是对一个未付清定义域的形式乘积取值。

对 $T\in\{A\}'$，有限输入上可用有界 $X_f,X_g$ 交换和 $C$ 对称性得到
$$
B(Tf,g)=B(TX_f1,X_g1)=B(TX_gX_f1,1).
$$
同时在 $\mathcal H_r$ 中逼近两个输入，并由 (1.5) 取极限，得
$$
\boxed{B(Tf,g)=B(T(f\odot g),1)\quad(f,g\in\mathcal H_r).}
\tag{5.4}
$$
$C$ 等距保持 $\mathcal H_r$。取 $g=Cf$、$T=I$ 得
$$
B(f\odot Cf,1)=\|f\|^2.
\tag{5.5}
$$

## 6. 正迹类端点分解与排除

设 $\rho\ge0$、$\mathcal E_r(\rho)<\infty$。选任意正秩一分解
$$
\rho=\sum_\nu x_\nu\otimes x_\nu,\qquad
\sum_\nu\|x_\nu\|^2=\operatorname{Tr}\rho.
$$
非负项 Tonelli 给
$$
\sum_\nu\|x_\nu\|_r^2=\mathcal E_r(\rho)<\infty.
\tag{6.1}
$$
所以每个 $x_\nu\in\mathcal H_r$，并且
$$
h_\rho=\sum_\nu x_\nu\odot Cx_\nu
\tag{6.2}
$$
在 $H$ 中绝对收敛，范数满足 (1.8)。由 (5.4)，对每个固定有界交换子 $T$，
$$
\begin{aligned}
\operatorname{Tr}(\rho T)
&=\sum_\nu B(Tx_\nu,Cx_\nu)\\
&=B\left(T\sum_\nu x_\nu\odot Cx_\nu,1\right)
=B(Th_\rho,1).
\end{aligned}
$$
左侧级数由 $\|T\|\operatorname{Tr}\rho$ 控制，右侧由 (1.8) 控制。由 (5.5) 得常数矩 (1.7)。若两个 $H$ 向量都有同一配对式，取 $T=A^n$ 并用 $1$ 的循环性，立即得到它们相等；因此 (6.2) 不依赖正分解。

若满足 (1.9) 的湮灭条件，则
$$
0=B(SA^nh_\rho,1)=B(Sh_\rho,A^n1)
\qquad(n\ge0).
$$
循环性给 $Sh_\rho=0$，全空间单射性给 $h_\rho=0$，常数矩给 $\operatorname{Tr}\rho=0$，正性给 $\rho=0$。这完成主定理。

没有在端点引入次数层的额外 $\ell^1$ 求和，所以无需 R230 的 $r>9$ 与 $(1-81/r^2)^{-1}$ 损失。整个论证对 $r=r_*$ 直接成立。

## 7. 新端点范围严格大于旧次数条件

取 $R=r_*$，令 $M_n=\lceil R^{4n}\rceil$。对每个 $n\ge1$，选 $M_n$ 个不同的 $n$ 元集合 $F_{n,k}$，并可要求全部这些集合的位支撑两两不交。定义
$$
f=\sum_{n\ge1}\frac{R^{-n}}{n\sqrt{M_n}}
\sum_{k=1}^{M_n}\chi_{F_{n,k}}.
\tag{7.1}
$$
各项是不同 Walsh 基向量，所以
$$
\|f\|_R^2=\sum_{n\ge1}\frac1{n^2}<\infty,
$$
而每个 $r>R$ 都满足
$$
\|f\|_r^2=\sum_{n\ge1}\frac{(r/R)^{2n}}{n^2}=\infty.
\tag{7.2}
$$
特别，正秩一态 $f\otimes f$ 不满足任何旧的 $r>9$ 条件，却被本稿排除。

此外
$$
\sum_F|\widehat f(F)|
=\sum_{n\ge1}\frac{R^{-n}\sqrt{M_n}}n
\ge\sum_{n\ge1}\frac{R^n}{n}=\infty.
$$
故这个正秩一密度的原 Walsh 矩阵也不是 entrywise-$\ell^1$。这里不声称它不属于 R237 的每一种改基覆盖类；只明确核验旧次数条件与原 Walsh 矩阵绝对和条件都不足以覆盖本例。

## 8. 未完成的量词

非零正正常湮灭者若存在，现在必须满足
$$
\mathcal E_{r_*}(\rho)=\infty,
$$
比原来仅知全部 $r>9$ 的次数矩发散更强。有限秩并不保证这个端点矩有限：任一向量的次数平方尾仍可任意慢。

本稿在这个明确范围内让 R244 的指定输入正则器直接取 $R=I$；一般正常见证的支撑向量未因此进入所需配对闭域。R250 的逆阻尼域障碍仍存在，不能由端点次数估计或正常范数逼近取消。普通 ISP 的完成标准未达成。
