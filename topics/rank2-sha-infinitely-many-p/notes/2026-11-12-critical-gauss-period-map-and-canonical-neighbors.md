# 临界 Gauss period map、边界分支与 canonical 曲线的真实同源邻点

日期：2026-11-12。状态：以下 Gauss 约化、所有分支数、Newton sums、
真实同源标记及 level-one quasi-canonical 邻点识别均已证明。
这给出实际 Hecke 对应的几何接口；没有证明中央导数非零或无穷素数结论。

固定 $p\ge7$、$p\equiv3\pmod4$，置 $d=p+1$、
$\rho=p^{-1/d}$。本文的 $t$ 始终是模参数
$\lambda_{\rm Leg}-1/2$，不是椭圆纤维的形式参数。

## 1. 指定整基、水平平凡化及初始 Frobenius

使用 [R68](../results/R68-integral-crystalline-frobenius-and-exact-critical-comparison.md)
的实际 Legendre 族

$$
\mathcal E_t:\quad y^2=x(x-1)(x-\tfrac12-t),\qquad s=1-4t^2,
$$

及整 de Rham 基
$e=(\omega,\eta)^t$，其中
$\omega=dx/(2y)$、$\eta=\nabla_{\partial_t}\omega$。准确有

$$
\nabla e=
\begin{pmatrix}0&1\\s^{-1}&8t/s\end{pmatrix}e,\qquad
Y=\begin{pmatrix}K&L\\K'&L'\end{pmatrix},\quad Y(0)=I,\quad
\det Y=s^{-1},
\tag{1.1}
$$

$$
K={}_2F_1(\tfrac14,\tfrac14;\tfrac12;4t^2),\qquad
L=t\,{}_2F_1(\tfrac34,\tfrac34;\tfrac32;4t^2),\qquad J=L/t.
$$

所有这些级数在 $|t|<1$ 收敛。令 $h=Y^{-1}e$，则
$\nabla h=0$ 且 $h(0)=e(0)$，故

$$
\omega(t)=K(t)h_1+L(t)h_2,\qquad \operatorname{Fil}^1_t=[K(t):L(t)].
\tag{1.2}
$$

这里的线坐标由本题的基直接计算，不借用不同基下的显式 period-ratio 公式。

实际晶体 Frobenius 使用行约定 $\Phi(e^\phi)=F_p(t)e$，
$\phi(t)=t^p$。其初值及整个矩阵为

$$
F_0=\begin{pmatrix}0&p\alpha_p\\\beta_p&0\end{pmatrix},\quad
\alpha_p,\beta_p\in\mathbb Z_p^\times,\quad\alpha_p\beta_p=-1,
\qquad
F_p(t)=Y(t^p)F_0Y(t)^{-1}.
\tag{1.3}
$$

$\alpha_p,\beta_p$ 是晶体矩阵常数，不是本题的 theta 系数。

(1.2) 也是 identity special-fiber marking 所给的晶体 period map。
所用原始事实是：quasi-isogeny marking 在解析 Dieudonné 丛上给函子性的
平凡化，且它是 Gauss–Manin 水平的。
见 Yves André，*Period mappings and differential equations. From
$\mathbb C$ to $\mathbb C_p$*，2002，II Lemmas 6.1.3、6.2.5，
印刷 pp.90–91；[原文](https://arxiv.org/pdf/math/0203194)。
在本盘上，水平平凡化在 $t=0$ 的值一经固定，由特征零微分方程唯一性
即为 $Y^{-1}$。后文只使用这个抽象、函子性的平凡化事实。

## 2. 临界圆盘上的准确约化

取 $\varpi^{p+1}=p$，写 $t=\varpi X$。定义

$$
\kappa_p=p[t^{p+1}]K\bmod p\in\mathbb F_p^\times.
$$

则在闭单位 $X$ 盘的 Tate 代数中

$$
\boxed{\quad
\overline{K(\varpi X)}=1+\kappa_pX^{p+1},\qquad
\overline{J(\varpi X)}=1,\qquad
\overline{\frac{u(\varpi X)}{\varpi}}
=\frac{X}{1+\kappa_pX^{p+1}},\quad u=L/K.
\quad}
\tag{2.1}
$$

最后一个式子在分母非零处成立；作为 $\mathbb P^1$ 值 period map，
它也记录了所有极点。

**系数证明。**
由固定递推，

$$
[t^{2n}]K=\frac{\prod_{j=1}^n(4j-3)^2}{(2n)!},\qquad
[t^{2n}]J=\frac{\prod_{j=1}^n(4j-1)^2}{(2n+1)!}.
\tag{2.2}
$$

[R77 的完整计数](2026-11-12-iterated-gm-frobenius-and-complete-inert-jets.md)
给出：每个 $p^h$ 层对 $K$ 的估值贡献至少为 $-1$；
负贡献只能在奇数 $h$ 出现，且要求 $2n\ge p^h+1$。
若共有 $a\ge1$ 个可能负层，则 $2n\ge p^{2a-1}+1$。
所以
$v_p([t^{2n}]K)+2n/(p+1)\ge0$；
等号只有 $n=0$ 或 $2n=p+1$。
后一处第一层贡献恰为 $-1$，其余层为零，故 $\kappa_p\ne0$。
对 $a\ge2$，不等式
$(p^{2a-1}+1)/(p+1)>a$ 排除等号。

$J$ 的负贡献只在偶数 $h$ 出现，并要求 $2n\ge p^h-1$。
同样计数给每个非恒定项的加权估值严格正；
更精确地 $\|J-1\|_\rho\le\rho^2$。
所有系数的负估值至多按 $\log_p(2n+1)$ 增长，
所以缩放后的系数趋于零。这证明 Tate 收敛及 (2.1)。

因此 $K$ 在 $|t|\le\rho$ 恰有 $p+1$ 个零点，全部满足 $|t|=\rho$，
全部简单。其缩放剩余值为

$$
\bar X^{p+1}=-\kappa_p^{-1}.
\tag{2.3}
$$

这 $p+1$ 个根全在 $\mathbb F_{p^2}$，形成一个非零 norm fiber。
每个剩余根唯一提升：导数
$(p+1)\kappa_pX^p=\kappa_pX^p$ 在这些根非零。
Weierstrass preparation 则保证没有额外零点。
因为 $J$ 在闭盘上为单位，$L=tJ$ 在这些零点不为零。

## 3. 一般临界值的全部局部分支及 Newton sums

令 $U\in\mathbb C_p^\times$ 满足 $|U|=1$。
方程 $u(t)=\varpi U$ 等价于

$$
F_U(X):=XJ(\varpi X)-UK(\varpi X)=0.
$$

其约化为 $X-U(1+\kappa_pX^{p+1})$，
恰有 $p+1$ 个不同的非零根；在根上约化导数为 $U/X\ne0$。
故存在准确 $p+1$ 个简单解 $|X|=1$，
并在每个 $U$ 的小邻域给解析分支。
原式导数还可不约化地核为

$$
F_U'(X)=L'(t)-\varpi U K'(t)
=\frac1{s(t)K(t)}
\quad\text{于 }F_U(X)=0.
\tag{3.1}
$$

约化根的 monic 多项式为

$$
X^{p+1}-(\kappa_pU)^{-1}X+\kappa_p^{-1}.
$$

若 $S_j$ 为这全部根的 $j$ 次幂和，则 Newton identities 准确给

$$
S_1=\cdots=S_p=0,\qquad S_{p+1}=-\kappa_p^{-1}.
\tag{3.2}
$$

例如实际 $M_e(t)=t^4+O(t^6)$ 的水平截面在这些点满足

$$
\overline{\varpi^{-4}K(t)M_e(t)}=X^5/U.
$$

其完整分支 trace 的最低剩余项为零，因为 $5\le p$。
这是 period-map 分支的准确约化，不独自构成完整 Hecke 恒等式；
真实同源的微分及 level 运输仍必须保留。

## 4. canonical 源曲线的商及统一 special-fiber marking

记 $E_0=\mathcal E_0$。它有 CM 自同构
$(x,y)\mapsto(1-x,iy)$，故形式群在当前惰性位是未分歧二次扩张
$\mathbb Q_{p^2}$ 的高度一 formal module，即高度二的 canonical lift。

先在一个有限未分歧基扩张 $B/\mathbb Q_p$ 上固定 $i$ 以及所需
prime-to-$p$ level 数据。所有这些挠点在好约化处未分歧。
对每个阶 $p$ 子群 $H\subset E_0[p]$，
取商同源 $q_H:E_0\to E_H$。

在形式群参数 $X$ 中，可使用 Serre 的商参数

$$
q_H(X)=\prod_{Q\in H}(X+_FQ).
\tag{4.1}
$$

它约化为 $X^p$；相应目标的特殊纤维标记因此是同一个
relative Frobenius $\bar E_0\to\bar E_0^{(p)}=\bar E_0$。
此构造及标记的唯一性见 Jiu-Kang Yu，
*On the moduli of quasi-canonical liftings*，
Compositio Math.96(1995),293–321，§3，pp.295–296，
[原文](https://www.numdam.org/article/CM_1995__96_3_293_0.pdf)。

把 ordered $2$-torsion 经 $q_H$ 运输到目标；因源 $2$-torsion 在
$\mathbb F_p$ 上，Frobenius 逐点固定其约化，
目标遂落在同一个 Legendre 形式邻域，参数记为 $t_H$。
对 Legendre 方程的 $y$ 坐标选择，规定约化同源为
$(x,y)\mapsto(x^p,y^p)$。这排除残余的 $y\mapsto-y$，
并与 (1.3) 的基规范一致；加入固定的满 prime-to-$p$ level
也可消去自同构。因而本处没有可任意补上的分支单位。

由 §1 的函子性水平晶体平凡化，$q_H$ 的水平矩阵是其约化
relative Frobenius 的矩阵，准确等于同一个 $F_0$：

$$
q_H^*\binom{h_{1,H}}{h_{2,H}}
=F_0\binom{\omega_0}{\eta_0}.
\tag{4.2}
$$

这里 $h_{i,H}=h_i(t_H)$，源的水平标记在 $0$ 即为 $e(0)$。
这个结论由真实同源及其约化推出，不是由零点数或两矩阵相似推出。

将 (1.2) 代入 (4.2) 得

$$
q_H^*\omega_H
=\beta_pL(t_H)\omega_0+p\alpha_pK(t_H)\eta_0.
\tag{4.3}
$$

代数同源的拉回保 Hodge 线，且其微分非零。因此

$$
\boxed{\quad K(t_H)=0,\qquad
q_H^*\omega_H=c_H\omega_0,\quad c_H=\beta_pL(t_H)\ne0.\quad}
\tag{4.4}
$$

为在使用边界零点计数前独立确定这些邻点的位置，
下一节直接算其形式群 Newton polygon。

## 5. 不借 degree 类比的准确邻点估值

给定任一整、首项单位的形式参数，源 $F$ 的非零 $p$-挠点全部满足

$$
v_p(X(Q))=w:=\frac1{p^2-1}.
\tag{5.1}
$$

证明如下：源定义在未分歧环上，特殊纤维高度二，
所以 $[p]_F(X)$ 的线性项为 $pX$，
次数 $2,\ldots,p^2-1$ 的系数被 $p$ 整除，
第 $p^2$ 次系数为单位。其非零根的 Newton polygon
为从 $(1,1)$ 到 $(p^2,0)$ 的单段。

由 (4.1)，商同源线性系数的估值为

$$
v_p(q_H'(0))=(p-1)w=\frac1{p+1}.
\tag{5.2}
$$

更完整地，目标 $F_H[p]\setminus\{0\}$ 的点分两组。

1. 来自 $F[p]/H$ 的 $p-1$ 个非零点为 $q_H(P)$、$P\notin H$。
   (4.1) 中所有 $p$ 个因子都是非零 $p$-挠点的参数，故其估值为
   $pw=p/(p^2-1)$。
2. 其余点可写 $q_H(P)$，其中 $[p]P\in H\setminus\{0\}$。
   对任一这样的非零 $Q=[p]P$，
   $[p]_F(X)-X(Q)$ 的 Newton polygon
   由 $(0,w)$ 连至 $(p^2,0)$，
   因而所有 $p^2$ 个解满足 $v_p(X(P))=w/p^2$。
   这比 $w$ 小，故每个 $X(P+Q')$、$Q'\in H$ 仍有此估值；
   (4.1) 给 $v_p(q_H(P))=w/p$。
   在除去 $H$ 的重复后，这组恰有 $p^2-p$ 个点。

于是目标乘 $p$ 级数的 Newton polygon 准确有顶点

$$
(1,1),\quad (p,\tfrac1{p+1}),\quad(p^2,0).
\tag{5.3}
$$

尤其其第 $X^p$ 次系数的估值恰为 $1/(p+1)$。
整的单位首项参数替换不改变点参数的估值，故此结论也适用于
标准 Legendre 形式参数。

标准参数的 $[p]$ 级数第 $X^p$ 系数模 $p$ 是 Hasse 系数。
在 $\lambda=1/2+t$，它有形式

$$
A_p(t)=t\,v(t)+p\,w(t),\qquad v(0)\in\mathcal O_B^\times,
\tag{5.4}
$$

因为 Legendre Hasse 多项式在此 supersingular 点有简单零点。
可直接用 $P_{(p-1)/2}(2t)$ 核定：
其次数为奇数，原点导数是
$p$-单位；改变不变微分只乘一单位。
现在 $v_p(t_H)>0$，而 (5.3) 给
$v_p(A_p(t_H))=1/(p+1)<1$。
若 $v_p(t_H)\ge1$，(5.4) 的值估值至少一，矛盾；
若 $0<v_p(t_H)<1$，(5.4) 的第一项严格支配第二项。
因此

$$
\boxed{\qquad v_p(t_H)=\frac1{p+1},\qquad |t_H|=\rho.\qquad}
\tag{5.5}
$$

这也与 (4.4) 中 $L=tJ$、$J$ 为单位及 (5.2) 完全一致。

## 6. 所有邻点互异、全部 $K$ 零点及 CM 阶

参数 $t_H$ 是代数数，构造对
$\operatorname{Gal}(\overline B/B)$ 等变；
其所有共轭仍来自 $E_0[p]$ 的 $p+1$ 个阶 $p$ 子群。
因为 $B$ 未分歧，(5.5) 的估值分母迫使
$B(t_H)/B$ 的 ramification index 至少 $p+1$，
从而 $t_H$ 至少有 $p+1$ 个不同的 $B$ 共轭。
所以这全部 $p+1$ 个目标参数确实互不相同。

结合 (4.4)、(5.5) 及 §2 的完整零点计数，得到

$$
\boxed{\quad
\{t_H:H\subset E_0[p],\ |H|=p\}
=\{t:|t|\le\rho,\ K(t)=0\}.
\quad}
\tag{6.1}
$$

这是带实际标记的等式；并非只说两边有相同的度数。
其缩放剩余点正好是 (2.3) 的 $p+1$ 个 norm fiber。

还有一个准确的域论加强。把未分歧基 $B$ 扩大到其剩余域包含
$\mathbb F_{p^2}$ 及上述 level 数据。此时 $\mu_{p+1}\subset B$，
$B(\varpi)/B$ 是次数 $p+1$ 的 tame cyclic 扩张。
(2.3) 的所有根都在 $B$ 的剩余域；对
$K(\varpi X)$ 逐根作 Hensel 提升，得到全部 $t_H\in B(\varpi)$。
另一方面 (5.5) 已给 $[B(t_H):B]\ge p+1$，所以

$$
\boxed{\quad B(t_H)=B(\varpi)\quad\text{对每个 }H.\quad}
\tag{6.2}
$$

因此全部邻点是同一个 tame cyclic Galois 轨道，
其带兼容运输数据的完整分支和可以写成真正的域 trace。
这里断言的是模参数及该标记下的商对象；
完整的源 $p$-挠点坐标本身可在更大的域中，未把两者混同。

目标的 CM 局部阶也能直接核定。
源 Tate 格是 $\mathcal O_{\mathbb Q_{p^2}}$ 的秩一格；
目标由指数 $p$ 的 $\mathbb Z_p$ 格给出。
一个 $\mathcal O_{\mathbb Q_{p^2}}$ 元素保持该格，
当且仅当其模 $p$ 标量保持指定的 $\mathbb F_p$ 直线，
即模 $p$ 属于 $\mathbb F_p$。
故乘子阶准确为

$$
\mathbb Z_p+p\mathcal O_{\mathbb Q_{p^2}}.
$$

其他有限位未改变；全局 CM 阶为 $\mathbb Z+p\mathbb Z[i]$。
这些正是 level-one quasi-canonical 商。
这里只在这句术语识别使用 Yu §4 的定义；所有参数估值与互异性
已经由 §5–6 直接证明。

## 7. 接入完整 Hecke 对应时仍要保留的权

(4.4) 给精确微分权 $c_H=\beta_pL(t_H)$，
而不是 $K(t_H)$。
例如 $K(t_H)M_e(t_H)=0$ 是在所选水平 Hodge 分量中为零；
它不表示代数模截面 $M_e$ 在这个 CM 邻点为零，
也不表示真实 Hecke summand 为零。

对于一条从附近源 $t$ 到目标 $t_j(t)$ 的真实同源分支，
只要保持同一 relative-Frobenius 标记，
同样的函子性直接给其 de Rham 行矩阵

$$
Y(t_j)F_0Y(t)^{-1}.
\tag{7.1}
$$

其 Hodge 条件与第一条目推出

$$
u(t_j)u(t)=p\alpha_p/\beta_p,\qquad
c_j=\beta_p L(t_j)/K(t),
\tag{7.2}
$$

其中第一式在可除处分母清去后处处成立。
源 $t=0$ 时恰恢复 (4.4)。
此外由 $u'=1/(sK^2)$ 可直接求导得

$$
t_j'(t)=\frac{s(t_j)}{s(t)}\,\frac{c_j^2}{p}.
\tag{7.3}
$$

(7.2) 的比例是 $p\alpha_p/\beta_p$；
不能把它改成 $1/p$ 倍。由 (5.5)，
$v_p(c_H)=1/(p+1)$，于是源零点处
$v_p(t_j'(0))=2/(p+1)-1$，
也明确显示该对应的临界尺度。

完整权一 Hecke trace 还需运送 $68$-level 上的点，
并保留惰性时 $M_e/M_o$ 的系数 Frobenius 交换。
这一步由同源/Hecke 后续笔记处理。
本篇已经付清的是：临界 $K$ 零点确是实际 canonical 邻点，
其晶体标记、参数尺度及微分权都准确确定。
