# 过滤整格、sequential periods 与原始对数图形的代数化边界

**可信度：§1、§2、§4、§5 的矩阵与系数计算已证明；§3 为所列原文的适用范围核查。** 日期：2026-11-12。本文续接 [固定上同调与移动端点笔记](2026-11-12-fixed-cohomology-moving-endpoint.md)。这里未得到无穷多个素数的 Sha 有限性，也不把后述 period conjecture 当作已证输入。

## 1. 固定过滤基会把丢失的对数移入 Frobenius 非对角项

沿用前一笔记的反变二维 Kummer 晶体基 $e_1,e_p$：
$$
\varphi(e_1)=e_1,\qquad
\varphi(e_p)=p e_p,\qquad
\operatorname{Fil}^1=L(e_p-\ell e_1),
\qquad \ell=\log_p\eta.
$$
因本处最大不分歧子域为 $\mathbb Q_p$，$\varphi$ 在系数上恒等。改取
$$
f_1=e_1,\qquad f_2=e_p-\ell e_1,
$$
使第一层过滤变成固定的第二条坐标轴，直接得到
$$
\varphi(f_2)=p f_2+(p-1)\ell f_1.
$$
因此
$$
\boxed{\quad
[\varphi]_{f_1,f_2}
=\begin{pmatrix}
1&(p-1)\log_p\eta\\
0&p
\end{pmatrix},\qquad
\operatorname{Fil}^1=L f_2.
\quad}
\tag{1}
$$
这里没有把过滤参数消去，而是将它移入 Frobenius 矩阵。对于实际字符 Kummer 类，$\ell=\rho_\chi\mathcal Q_p$，所以新矩阵仍含有原来需要控制的数。

一般而言，$e_p-\ell e_1$ 只是一个局部基；不能不经证明称它来自固定数域上的共同 de Rham 基。对于固定代数数的 Kummer motive，确有适当固定基给出 (1) 型矩阵；下一节的 Rosen 原文正是这个情形。

## 2. 可容许性与强整除条件允许任意高的非零深度

在 $\mathbb Q_p$ 上取任意 $c\in p\mathbb Z_p$。设
$$
M=\mathbb Z_p f_1\oplus\mathbb Z_p f_2,\qquad
\operatorname{Fil}^1M=\mathbb Z_p f_2,\qquad
\operatorname{Fil}^2M=0,
$$
并定义
$$
\varphi(f_1)=f_1,\qquad
\varphi(f_2)=p f_2+c f_1.
\tag{2}
$$
逐项检查得到
$$
\varphi(\operatorname{Fil}^1M)\subset pM,\qquad
\varphi(f_1)=f_1,\qquad
p^{-1}\varphi(f_2)=f_2+(c/p)f_1.
$$
最后两向量的行列式为 $1$，因而生成整个 $M$。所以通常权重 $0,1$ 的整性、过滤整除及生成条件，对每个这样的 $c$ 都成立。

若 $c\ne0$，它也确实来自单位 Kummer 类：对奇数 $p$ 令
$$
\eta=\exp_p\bigl(c/(p-1)\bigr)\in1+p\mathbb Z_p.
$$
则 $(p-1)\log_p\eta=c$，而单位 Kummer 类的 crystalline 性已在前一笔记按 Brinon–Conrad 核对。

特别地，可以取 $c=p^N$，其中 $N$ 任意大。维数、过滤秩、Frobenius 特征值、上述整除与生成条件都不变。这是对“这些局部公理本身迫使浅深度”的反证；它**不是**原始椭圆单位生成元的反例，也没有把这些随 $p$ 选取的局部单位冒充一个固定全局 motive。

## 3. 原文中准确对应的跨素数问题

### 3.1 Rosen 的强 sequential period conjecture

Julian Rosen 的 *Sequential periods of the crystalline Frobenius*，arXiv:1805.01885v1，定义
$$
\mathcal R=
\left(\prod_p\mathbb Q_p\right)\Big/\left(\bigoplus_p\mathbb Q_p\right),
\qquad
\operatorname{Fil}^n\mathcal R
=\{(a_p)_p:\liminf_p v_p(a_p)\ge n\}.
$$
其 §4、Conjecture 2 主张 sequential period map 严格保持 Hodge 过滤：若一个固定 motivic period 对所有充分大 $p$ 有额外 $p^n$ 整除，则这种整除应来自相应 Hodge 层。这正是“固定几何对象是否能反向控制无穷多个 $p$ 的深度”的额外输入，原文将它列为猜想。

在 §5.1、Theorem 5.1，原文对固定 $r\in\mathbb Q\setminus\{0,\pm1\}$ 的 Kummer motive 写出
$$
\begin{pmatrix}
1&\log_p(r^{p-1})\\0&p
\end{pmatrix}
\tag{3}
$$
并证明：上述强猜想蕴含无穷多个满足
$r^{p-1}\not\equiv1\pmod{p^2}$ 的素数。对好素数，(3) 的非对角项非零且属于 $p\mathbb Z_p$；其是否多被一个 $p$ 整除，恰是该 Fermat 商问题。

这一引用只说明一般“sharp Hodge 深度必在无穷多 $p$ 达到”的断言并非本文可以使用的已证通则。它没有证明本课题等价于非 Wieferich 问题，也没有把本题的阈值 $4$ 偷换成 Kummer 例子的阈值 $2$。

来源：[Rosen 原文](https://arxiv.org/pdf/1805.01885)，§4 Conjecture 2、§5.1 Theorem 5.1，印刷第8–10页。

### 3.2 Ogus 的全忠实性并不等于 Frobenius 元素本身稠密

Andreatta–Barbieri-Viale–Bertapelle 的 *Ogus realization of 1-motives*，Theorem 3.3.5，证明数域上 $1$-motives（至同源）的 Ogus 实现全忠实。这里 FOg 中所加的过滤是**权过滤**，不能仅由这个名称认作本题需要的整 Hodge 深度控制。

全忠实性控制的是固定有理线性映射与几乎所有 Frobenius 的相容性。Rosen §5.3、Remark 5.7 又明确区分：

- Frobenius 元素所**生成的子群** Zariski 稠密；
- Frobenius 元素组成的**集合本身** Zariski 稠密。

后者才是 weak sequential period conjecture 的密度要求；前者本身不足以令某个非零多项式在无穷多个 Frobenius 元素处非零。

这个逻辑差别有一个初等模型。在加法群 $\mathbb G_a^2$ 中取两坐标轴的并 $S$。$S$ 生成整个群，但非零多项式 $xy$ 在 $S$ 上恒为零。故仅有生成子群稠密，不能排除一个行列式型的多项式在所有选定元素上消失。这里也不把该模型当作实际算术 Frobenius 的构造。

来源：

- [Andreatta–Barbieri-Viale–Bertapelle 原文](https://arxiv.org/pdf/1610.04341)，Theorem 3.3.5、Example 3.3.6，印刷第17–18页；定义 FOg 的权过滤见引言及 §1。
- [Rosen 原文](https://arxiv.org/pdf/1805.01885)，Theorem 5.5、Corollary 5.6、Remark 5.7，印刷第11–12页。

## 4. 实际 chi 对象尚未放入一个固定数域上的固定 motive

原始局部对象是
$$
e_\chi\Phi(P_\pi),\qquad
P_\pi\in E[\mathfrak p]\setminus\{O\},\qquad
|\Delta_p|=p-1.
$$
函数 $\Phi$ 固定，但点 $P_\pi$、分裂域 $K(E[\mathfrak p])$ 和角色投影都随 $p$ 改变。逐 $p$ 构造二维 Kummer 扩张，并不自动给出 Rosen 定义所要求的一个固定数域上的固定对象及固定 de Rham 向量。

若保留全部端点，相对上同调维数为 $p+512$；若逐 $p$ 取两个端点，维数虽为 $514$，定义域与端点下降数据仍变。前一笔记已给出这两个准确计数。角色投影后维数变小，也不能抹去投影本身随 $p$ 变化的事实。

固定 norm-one 单位 $u$ 或辅助单位 $w$ 确实给固定 Kummer motive，但
$$
D_p(\alpha)
=\operatorname N_{M K(E[\mathfrak p])/M}(1+\alpha t(P_\pi))
$$
是 tame 普通范数。它属于平凡角色，并已在 [固定范数丢失临界角色笔记](2026-11-12-fixed-norm-loses-critical-character.md) 中证明不能替代 $e_\chi\Phi(P_\pi)$。

所以即使假定某个 sequential period conjecture，仍需先给出原目标的固定 motive 表示；本笔记没有建立这个表示。

## 5. 原始 log Phi 图形的 adelic size 可以精确计算

这里可以直接检验 Bost–Chambert-Loir 的代数化条件，而不只说其适用性未知。

### 5.1 一般系数引理

令
$$
F(t)=1+a_m t^m+a_{m+1}t^{m+1}+\cdots\in1+t^m\mathbb Z_p[[t]],
\qquad a_m\in\mathbb Z_p^\times,\quad m\ge2,
$$
并写 $I(t)=\log F(t)=\sum_{n\ge m}b_n t^n$。对 $p$ 为奇素数，有
$$
v_p(b_n)\ge-\left\lfloor\log_p(n/m)\right\rfloor
\quad(n\ge m).
\tag{4}
$$
证明：在
$$
I(t)=\sum_{k\ge1}\frac{(-1)^{k+1}}k(F(t)-1)^k
$$
中，次数 $n$ 只涉及 $k\le n/m$，每个分子系数为整数。各项分母至多损失
$\max_{k\le n/m}v_p(k)=\lfloor\log_p(n/m)\rfloor$ 位。

在 $n=mp$ 处，只有 $k=p$ 项的分母含 $p$，该项的分子系数恰为 $a_m^p$。因此
$$
b_{mp}\equiv\frac{a_m^p}{p}\pmod{\mathbb Z_p},
\qquad v_p(b_{mp})=-1.
\tag{5}
$$
设 $r=\lfloor\log_p(n/m)\rfloor\ge1$。因为 $n\ge mp^r$ 且
$$
mp^r-1\ge r(mp-1),
$$
式 (4) 给
$$
\frac{v_p(b_n)}{n-1}\ge-\frac1{mp-1}.
$$
式 (5) 达到等号。因此 $t+I(t)$ 除以 $t$ 的 Newton polygon 首斜率准确为
$$
-\frac{\log p}{mp-1}.
\tag{6}
$$

### 5.2 对本题原函数的应用

R19 给 $\lambda_1=0$、所有偶阶矩为零，以及
$$
\lambda_3=\delta^3\log\Phi(O)
=-2\cdot2!\,f^3\Omega_\infty^{-3}
L_{\mathfrak f}(\overline\psi^{\,3},3)\ne0.
$$
非零性来自该 Hecke $L$ 值的绝对收敛 Euler product：局部商的绝对值为
$(N\mathfrak q)^{-3/2}$。又 $t=z+O(z^5)$，故
$$
\Phi(t)-1=a_3t^3+O(t^4),
\qquad a_3=\lambda_3/6\ne0.
\tag{7}
$$
函数与首系数均固定在数域上，所以除有限个素位外，$\Phi(t)$ 的展开整且 $a_3$ 为单位。

令 $\widehat C$ 为 $I(t)=\log\Phi(t)$ 的形式图形。整剪切
$(t,y)\mapsto(t,y+t)$ 将它变成 $t+I(t)$ 的图形，不改变局部 size。后者在原点的导数为 $1$。Bost–Chambert-Loir Proposition 3.5(2) 将图形 size 识别为上述 Newton 首斜率的指数；在椭圆曲线上使用 $t$ 只是一个 étale 局部坐标。结合 (6)–(7)，得到对所有充分大的 split $p$：
$$
\boxed{\quad
S_p(\widehat C)=p^{-1/(3p-1)}.
\quad}
\tag{8}
$$
因此
$$
\sum_{\substack{p\equiv1\ (4)\\p\ \mathrm{large}}}
\log S_p(\widehat C)^{-1}
=
\sum_{\substack{p\equiv1\ (4)\\p\ \mathrm{large}}}
\frac{\log p}{3p-1}
=\infty.
\tag{9}
$$
最后的发散可由算术级数中素数定理经分部求和得到；只使用 split 素数已经足够。于是该固定图形**不是 A-analytic**。这排除了直接把原始 $\log\Phi$ 图形代入 Bost–Chambert-Loir Theorem 6.1 或 Theorem 7.9 的做法，因为其 A-analyticity 假设不成立。

这里的结论不排除先构造不同的、满足新整性条件的派生形式图形；也不声称某些端点值额外可被 $p$ 整除会改变 (8)。式 (8) 来自固定函数的全部系数，而原任务只约束一个移动端点的特定字符值。

外部输入仅为 size 的 étale/整坐标不变性、Newton polygon 公式及 A-analyticity 定义：
[Bost–Chambert-Loir 原文](https://arxiv.org/pdf/math/0702593)，Proposition 3.1、Proposition 3.5(2)、Definition 3.7；一般代数化结论见 Theorem 6.1、Theorem 7.9。本文的 (4)–(9) 是针对原函数另行给出的系数证明。

## 6. 此路线留下的准确任务

已确认：局部固定维数、强整除晶体公理、Ogus 全忠实性，以及原始对数图形的直接代数化，都没有给出所需的跨 $p$ 浅深度或中心非零。

仍可继续检验一种更具体的固定对象：由固定 Mordell–Weil 点构造的 Poincaré biextension 或 universal vectorial extension。要使这条路线实际闭合，必须同时证明目标的表示公式，以及相应的非零定理；不能仅因为这些对象被称为 $1$-motivic，就把二阶行列式或随 $p$ 改变的核线当成一个固定代数态射。
