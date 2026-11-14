# 迹曲线的复增长阶数与 Herblot 的准确阈值

日期：2026-11-12。**状态：迹曲线、非代数性与增长界已证明；所需算术上界未证明。**

本篇把加法 CM 逆像变成一个定义在 $\mathbb Q$ 上的固定图像，
并核对弱于 A-analytic 的算术代数化接口。
其目的不是把逐项高度估计当成整个 jet 映射的估计。

## 1. 所用原始定理及归一化

Herblot，*Algebraic points on meromorphic curves*（2012），Definition 2.4–2.5
要求一个 $K$-有理光滑形式曲线的评价映射满足：对任意有限位集合 $S$，
对每个 $\alpha'>\alpha$，存在 $C>0$，使全部 $k,D\ge0$ 都有
$$
\frac1{[K:\mathbb Q]}
\sum_{v\notin S}h_v(\varphi^k_D)
\le\alpha' k\log k+C(k+D),
\tag{1.1}
$$
并且每个固定 $v$ 有单独的线性界 $h_v(\varphi^k_D)\le C_v(k+D)$。
这里
$$
\varphi_D^k:
\{s\in H^0(X,L^D):s|_{\widehat V}\text{ 消失到 }k-1\text{ 阶}}
\longrightarrow
\operatorname{Sym}^k\Omega^1_{\widehat V,O}\otimes L_O^D
$$
是真正的 $k$ 阶 jet 评价，不是一个预先指定级数的单独第 $k$ 个系数。
Lemma 2.6 说明该性质在数域基变换下不变。

Theorem 6.1 的陈述以 $\mathbb Q$ 上的射影簇 $X$ 为基底。
设闭点的次数为 $d_j=[\mathbb Q(x_j):\mathbb Q]$，相应曲线为
$\alpha_j$-arithmetic，并由**同一个连通仿射曲线**上的解析映射共同一致化，
其总增长阶数至多 $\rho$。若各 germ 的 Zariski 闭包维数为 $r>1$，则
$$
\boxed{\sum_j\frac1{\alpha_jd_j}\le\frac r{r-1}\rho.}
\tag{1.2}
$$
否则 $r=1$，各 germ 都代数。

因此，对一个 $\mathbb Q$-有理点上的曲面图像，$d=1,r=2$，
若 $\rho=2$，严格的充分代数化范围是 $\alpha<1/4$。
若直接把 $K=\mathbb Q(i)$ 上的曲面视为 $\mathbb Q$-簇，原点的剩余域是 $K$，
则 $d=2$，同一条定理只给 $\alpha<1/8$。
不能用 Lemma 2.6 自动删除 Theorem 6.1 中闭点次数的因子。

## 2. 一个固定的 $\mathbb Q$ 系数迹图像

取前篇中的
$$
b=35+34i,\quad f=34(1+i),\quad
\ell=\delta\log\Phi,\qquad
(\sigma_b-1)^m F_b=\ell,\quad F_b(O)=0.
$$
在系数上施加 $K/\mathbb Q$ 的共轭，记其像为 $\overline F_b$。
于是
$$
(\sigma_{\bar b}-1)^m\overline F_b=\bar\ell.
$$
定义
$$
\boxed{H_m(t)=F_b(t)+\overline F_b(t)\in\mathbb Q[[t]].}
\tag{2.1}
$$
有 $H_m(0)=H_m'(0)=0$，因此它在
$$
X=E\times\mathbb P^1\quad/\mathbb Q
$$
的有理点 $(O,0)$ 处给出光滑形式图像。

注意这里使用的是一个固定函数的共轭迹，已经形成同一个 $\mathbb Q$-germ；
不是把若干不同函数的局部好素数集合合并。

## 3. 共轭项不能消去留数：迹仍然超越

有 $(b,\bar b)=1$：任何公共 Gaussian 素因子都整除
$b+\bar b=70$ 和 $b-\bar b=68i$，从而整除 $2$；但 $N(b)=2381$ 为奇数。
另外 $(bf,\bar b)=1$。

选择 $\ell$ 的一个极点 $s\in E[f]$。
写周期格为 $\Lambda=\Omega\mathbb Z[i]$，用中国剩余定理选择其复对数
$$
z_s=\frac{\Omega\eta}{f},\qquad
\eta\equiv1\pmod{b\bar b}.
$$
在
$$
z_n=b^{m+n}z_s
$$
处，前篇的亚纯和给
$$
\operatorname{Res}_{z=z_n}\widetilde F_b(z)\,dz
=r_s b^m\sum_{j=0}^n\binom{m+j-1}{j}b^j=:A_n,
\qquad |A_n|\longrightarrow\infty,
\tag{3.1}
$$
其中 $r_s=\operatorname{ord}_s\Phi\ne0$。

另一方面，$\bar\ell$ 的极点仍在 $E[f]$ 中，因为 $(\bar f)=(f)$。
若 $\overline F_b$ 的第 $j$ 项在 $z_n$ 有极点，就必须有
$$
\frac{\Omega b^{m+n}\eta}{\bar b^{m+j}}\in\Lambda,
$$
即 $\bar b^{m+j}\mid b^{m+n}\eta$，与互素性和 $\eta\equiv1\pmod{\bar b}$ 矛盾。
故共轭和在 $z_n$ 正则，迹的留数仍是 $A_n$。

所有 $z_n$ 都投影到同一 $s$。
如果迹代数于 $\mathbb C(E)$，把其多项式关系在这些点用同一局部变量展开，
只能得到有限多个 Laurent 分支，留数也只有有限多个值。
这与 (3.1) 矛盾。因此
$$
\boxed{H_m\text{ 不代数于 }\overline{\mathbb Q}(E).}
\tag{3.2}
$$
其图像在曲面 $X$ 中 Zariski 稠密，所以 (1.2) 中的维数准确为 $r=2$。

## 4. 亚纯和的增长确实至多为二阶

本节不仅使用“全平面亚纯”这一性质，还给 Definition 5.1 所需的增长界。
在复嵌入下，令
$$
h(z)=\ell(\operatorname{Exp}_Ez),\qquad
\widetilde F_b(z)=\sum_{n\ge0}C_n h(z/b^{m+n}),\quad
C_n=\binom{m+n-1}{n}.
\tag{4.1}
$$
固定椭圆函数 $h$ 的 Nevanlinna 特征满足
$T(R,h)\le C(1+R^2)$。
这一标准界也可直接由 Weierstrass $\sigma$ 函数得到：
把一个基本格中的极点用有限个 $\sigma(z-z_s)$ 消去；
$\sigma$ 的准周期公式给 $\log^+|\sigma(z)|=O(|z|^2)$，
而椭圆函数在远离固定极点邻域处有界。
在这些邻域内对消去极点后的整函数使用最大值原理，仍得同样的二次指数界。

对给定 $R\ge2$，选择 $N=O(\log R)$，使 $R/|b|^{m+N}$ 落入
$h$ 在原点正则且 $h(z)=O(z^2)$ 的固定小圆盘。
前 $N+1$ 项的特征之和至多为
$$
\begin{aligned}
\sum_{n=0}^N T(R,C_n h(z/b^{m+n}))
&\le C\sum_{n=0}^N\left(1+\frac{R^2}{|b|^{2(m+n)}}\right)
  +\sum_{n=0}^N\log^+ C_n\\
&=O(R^2)+O(\log R\log\log R).
\end{aligned}
\tag{4.2}
$$
使用 $T(R,f+g)\le T(R,f)+T(R,g)+O(1)$ 的有限和版本即可控制这一部分。
尾项在 $|z|\le R$ 全纯，且
$$
\sup_{|z|\le R}\left|\sum_{n>N}C_nh(z/b^{m+n})\right|
\le C R^2\sum_{n>N}(n+1)^{m-1}|b|^{-2(m+n)}
=O((\log R+1)^{m-1}).
\tag{4.3}
$$
所以其特征只有 $O(\log\log R+1)$。
因此
$$
T(R,\widetilde F_b)=O(R^2),\qquad
T(R,\widetilde H_m)=O(R^2),
\tag{4.4}
$$
后一式对两个固定共轭和相加即可。

### 4.1 将特征界转成原定理要求的全局截面

$\widetilde H_m$ 的所有极点都是简单极点，并投影到固定有限集合
$S_0\cup\overline S_0\subset E[f]$。
令 $D(z)$ 为在这些格陪集上各取一次零点的有限 $\sigma$ 乘积。
则 $D$ 为整函数，$\log^+|D(z)|\le C(1+|z|^2)$，且
$$
G(z)=D(z)\widetilde H_m(z)
$$
也是整函数。由 (4.4)，$T(R,G)=O(R^2)$。
整函数的圆盘 Poisson 估计给
$\log M(R,G)\le 3T(2R,G)+O(1)=O(R^2)$。

于是 $\eta_H(z)=(D(z),G(z))$ 是映射
$\widetilde H_m:\mathbb C\to\mathbb P^1$ 的拉回 $\mathcal O(-1)$ 的一个全局截面，
范数至多为 $C_1\exp(C_2|z|^2)$。
$D,G$ 可能有公共零点并无妨碍：截面允许在那里为零；它不恒为零且在 $z=0$ 不为零。

椭圆曲线的标准一致化也可用
$\sigma^3\wp,\sigma^3\wp'/2,\sigma^3$
给出增长为 $\exp(O(|z|^2))$ 的全局齐次截面。
将它与 $\eta_H$ 张量，对 $X=E\times\mathbb P^1$ 上一个积型 ample 丛，
得到 Definition 5.1 要求的截面。
因此整个映射
$$
z\longmapsto(\operatorname{Exp}_Ez,\widetilde H_m(z))
$$
在 $M=\mathbb P^1$、删去点 $T=\{\infty\}$ 的意义下，增长阶数准确满足
$$
\boxed{\rho\le2.}
\tag{4.5}
$$
这里没有把一个未知增长的亚纯延拓直接称作二阶一致化。

## 5. 得到的准确算术门槛

结合 (3.2)、(4.5) 与 Herblot Theorem 6.1：
$$
\boxed{\widehat{\operatorname{graph}}(H_m)
\text{ 不可能是任何 }\alpha<\tfrac14\text{ 的 }\alpha\text{-arithmetic germ}.}
\tag{5.1}
$$
等价地，若某个额外算术假设能推出这个固定图像满足
$\alpha<1/4$ 的 jet 高度界，就与已证明的非代数性矛盾。
本篇没有得到这样的上界。

## 6. 可核的截断系数充分条件，与仍缺的估计

把 $H_m(t)=\sum_{j\ge2}a_jt^j$，$a_j\in\mathbb Q$。
除去有限个模型坏素数后，定义
$$
s_p(k)=\max_{2\le j\le k}
\left\{0,\frac{-v_p(a_j)}{j-1}\right\},
\qquad
\mathcal B(k)=\sum_p s_p(k)\log p.
\tag{6.1}
$$
每个固定 $k$ 的和有限。
如果能证明对每个 $\alpha'>\alpha$ 有
$$
\mathcal B(k)\le\alpha'\log k+C,
\tag{6.2}
$$
并保持每个固定素数的解析收敛，那么图像为 $\alpha$-arithmetic。

**充分性的证明。** 在好素数处，把 $t,y$ 同时缩放为赋值 $s_p(k)$ 的变量。
由 (6.1)，图像的 $k$ 阶截断在这些坐标中整。
一个积分截面在图像上消失到 $k-1$ 阶时，其第 $k$ 阶评价的局部范数
至多为 $p^{k s_p(k)}$。积分模型中线丛的局部平凡化在原点是单位；
因此该界对所有 $D$ 成立。
对固定有限坏素数及无穷处，固定解析半径和固定模型给 $O(k+D)$ 界。
相加即得 (1.1)；删除任意有限 $S$ 也只改变线性常数。证毕。

前篇的真实图像大小界可以用于 (6.1)，但尚未给出 (6.2)。
在惰性处，令
$$
d_p=\operatorname{ord}_{\mathbb F_{p^2}^{\times}}(b),\quad
D_p=\operatorname{lcm}(d_p,2),\quad c_p=v_p(b^{d_p}-1).
$$
共轭保持 $d_p,c_p$，所以对迹可以使用同样的局部估计。
若 $D_p>k$，其 $k$ 阶截断其实整：在整的 tame 线性化坐标中，
所有小于 $D_p$ 的非零权都属于已处理的非共振块。
若 $D_p\le k$，前篇给
$$
s_p(k)\le\frac1{p^2-1}+\frac{m c_p}{D_p-1}.
\tag{6.3}
$$
从而惰性位的贡献至多为
$$
O(1)+m\sum_{\substack{p\ \mathrm{inert}\\D_p\le k}}
\frac{c_p\log p}{D_p-1}.
\tag{6.4}
$$
这比要求全和收敛弱：只需该截断和的对数增长常数，加上普通位的实际贡献，
足够小，才可能达到 $1/4$ 门槛。

但既有 $S$-unit 小公因子界只产生某些逐阶的 $o(d)$ 估计，
直接对 $d\le k$ 求和再除以 $d$ 仍只能给 $o(k)$，不是 $O(\log k)$。
对单独系数给 $o(k)$ 或 $O(k)$ 的高度上界，也不能替代 (1.1) 或 (6.2)：
同时截断的分母会涉及许多不同阶数的 $b^j-1$。
Stewart 的统一深度界已经控制近满阶数素数子集；
小阶数例外及普通处额外共振块仍需新的输入。

## 7. 偶性商给 $\rho=1$，但 jet 阶数也必须同步改变

这里还有一个准确的等价几何表述。
$H_m$ 是偶函数；令 $u=1/x$ 为 $E/\{\pm1\}\simeq\mathbb P^1$ 在原点像处的参数。
由曲线方程和 $t=-x/y$，有
$$
t^2=\frac{u}{1-17u^2}.
\tag{7.1}
$$
这是 $t^2$ 与 $u$ 之间的整严格形式坐标变换。
因此存在唯一 $J_m(u)\in\mathbb Q[[u]]$，使 $H_m(t)=J_m(1/x)$。
它仍不代数于 $\mathbb Q(u)$，否则 $H_m$ 会代数于 $\mathbb Q(E)$。

复一致化中的 $x(z)$ 和 $\widetilde H_m(z)$ 都为偶亚纯函数，
故在 $w=z^2$ 下下降为整个 $w$ 平面上的亚纯函数。
第 4 节的极点集合关于 $z\mapsto-z$ 对称。
可成对选择 $\sigma(z-z_s)\sigma(z+z_s)$，得到偶的清分母函数 $D(z)$；
$G(z)=D(z)\widetilde H_m(z)$ 也偶。
它们下降为整函数 $\widehat D(w),\widehat G(w)$，增长界由
$\exp(O(|z|^2))$ 变为 $\exp(O(|w|))$。
$x(z)$ 则可用偶的整对 $\sigma(z)^2\wp(z),\sigma(z)^2$ 作同样下降。
于是 $J_m$ 的图像在 $\mathbb P^1\times\mathbb P^1/\mathbb Q$ 的有理点处，
具有 Definition 5.1 意义下 $\rho\le1$ 的一致化。

Herblot 的相应门槛因此是
$$
\boxed{\widehat{\operatorname{graph}}(J_m)
\text{ 不可能是任何 }\alpha<\tfrac12\text{ 的 }\alpha\text{-arithmetic germ}.}
\tag{7.2}
$$

但这不是对原系数估计的免费加倍。
先在 $s=t^2$ 坐标写 $H_m=\sum_{j\ge1}a_{2j}s^j$。
同一个负赋值现在要除以 $j-1$，而原来除以 $2j-1$；其比值为
$$
\frac{2j-1}{j-1}=2+\frac1{j-1}.
$$
有限个低阶系数只涉及有限个坏素数；这些固定素数的解析性给有界的局部大小损失。
因此，对任意 $\varepsilon>0$，用第 6 节的充分量可得
$$
\mathcal B_{J_m}(k)
\le(2+\varepsilon)\mathcal B_{H_m}(2k)+O_\varepsilon(1).
\tag{7.3}
$$
式 (7.1) 及其逆均整，故不另增加好素数的截断大小损失；
固定线性项也可通过一个整的线性坐标变换去掉。
所以如果仅把同一批估计机械改写到偶性商上，算术常数也约乘二，
与 $1/4$ 变为 $1/2$ 同步。新的局部相消仍须另行证明。

## 8. 一个系数高度线性、但没有任何有限算术常数的反例

以下例子具体说明，不能以单个 Taylor 系数的高度代替 §1 的评价映射高度。
固定整数 $q\ge2$，定义
$$
F(z)=\sum_{n\ge1}\frac{z^n}{q^n-1},\qquad
D(z)=\prod_{j\ge1}(1-z/q^j).
\tag{8.1}
$$
在 $|z|<q$ 内交换绝对收敛的和，得到
$$
F(z)=\sum_{j\ge1}\frac{z}{q^j-z}
=-\frac{zD'(z)}{D(z)}.
\tag{8.2}
$$
乘积在紧集上一致收敛。因此 $F$ 在整个复平面亚纯，在每个 $q^j$ 有简单极点，留数 $-q^j$ 非零。它不代数于 $\mathbb C(z)$：一个代数函数在有限 $z$ 平面上的极点只能位于其多项式关系最高次系数的有限个零点，不能有这些无穷互异的极点。

同时，若 $R\ge2$，分开 $q^j\le R$ 与 $q^j>R$ 两段可得
$$
\log M(R,D)
\le\sum_{j\ge1}\log(1+R/q^j)
=O_q((\log(R+2))^2).
$$
Cauchy 估计给 $D'$ 同样的增长阶数。因此对任意 $\rho>0$，$D$ 与 $zD'$ 都满足 $\exp(O_{q,\rho}(|z|^\rho))$ 的整函数增长界。用齐次截面 $(D,-zD')$ 及 $z$ 的标准齐次坐标，图像在 $\mathbb P^1\times\mathbb P^1/\mathbb Q$ 上具有**任意正阶数** $\rho$ 的一致化。

这个固定 $\mathbb Q$-有理 germ 在每个有限位都有正收敛半径。若 $p\mid q$，分母是 $p$-单位。若 $p\nmid q$，提升指数公式给 $v_p(q^n-1)=O_{p,q}(1)+O(\log n)$；$p=2$ 使用通常的奇数底数版本，结论相同。因此其 $p$-进收敛半径至少为一。

若该图像对某个有限 $\alpha\ge0$ 是 $\alpha$-arithmetic，则先把 $\alpha$ 增大到某个正有限 $\alpha'$。Herblot Theorem 6.1 对任意 $\rho>0$ 给
$$
\frac1{\alpha'}\le2\rho,
$$
取 $\rho<1/(2\alpha')$ 即矛盾。所以它不是任何有限 $\alpha$ 的 $\alpha$-arithmetic germ。

但每个单独系数却满足
$$
h\left(\frac1{q^n-1}\right)=\log(q^n-1)\le n\log q.
\tag{8.3}
$$
这给出了所需逻辑区别的明确反例：所有单系数高度甚至只有线性增长、各有限位也都解析，仍不能推出实际 jet 评价有任何有限的 $\alpha k\log k+O(k+D)$ 上界。本例没有被当作本题实际 $F_b$ 的模型同构；它只排除这种推理捷径。

## 来源和适用范围

- M. Herblot，*Algebraic points on meromorphic curves*（2012），
  Definition 2.4–2.5、Lemma 2.6、Definition 5.1、5.4–5.5、Theorem 6.1；
  [作者原文](https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf)，
  [arXiv](https://arxiv.org/abs/1204.6336)。本文逐项使用的是此原始定理的陈述；
  不把对代数叶的 Proposition 3.6 自动用于本差分 germ。
- `2026-11-12-additive-cm-difference-inverse.md`：固定逆像、留数、完整 tame 群、
  图像大小的缩放证明及 Stewart Theorem 1.2。
- `2026-11-12-additive-multidifference-obstruction.md`：CRT 选复对数及唯一极点的论证。

没有把几个不同函数的局部条件当成共同一致化条件；
也没有假定极点处取值为 $\infty$ 就使该处的整个形式 germ 定义在数域上。
