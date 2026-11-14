# R315：原单极中央核的首一多项式、单位导数及真实迹轨道

日期：2026-11-13。**状态：以下原 $H_3$ 中央核的准确首多项式、同时为单位的核值和导数、全单极族不存在标量交织、原非挠迹轨道不在有限来源空间闭合，以及每个好惰性处的真实 exact 微分被原中央行非零检测，均已证明。这里没有排除四个指定原轨道在中央观察后出现新的实际关系。**

本文接 R313 的实际同源迹，不另换一个 Frobenius 算子。关键是先算原中央核的首层，然后在真正的 $(p+1)$ 挠点处检验；不将原 $S$ 的未知中央非零当成输入。

## 1. 原单极来源和同一参考投影

固定 R310–313 的
$$
E_b:y^2=x^3+b,\quad b=17,\quad dz=dx/(2y),\quad
H=H_3,\quad d=p+1=6s,
$$
其中 $p>7$、$p\equiv5\pmod6$、$p\ne17$。取
$$
\kappa=34[z^d]\log(\sigma/z),\qquad v_p(\kappa)=-1.
$$
R308 已付真实参考
$$
\mathcal J_H(0)=1,\qquad
\mathcal J_H\in1+p\mathbb Z_p\langle u\rangle.
$$
所以 R312 的中央投影为
$$
\mathcal L_H(T)=\mathcal J_T'(0)-\mathcal J_T(0)\mathcal J_H'(0).
$$

对 $P=(a,y_P)$，定义真正的单极核
$$
\boxed{
\mathfrak F_p(P)=
\mathcal L_H\left(H(z)\frac{2y_P}{x(z)-a}\right).}          \tag{1}
$$
这里 $H(z)/(x(z)-a)$ 一般是亚纯来源；(1) 只用其真实原点展开，保原 $H$ 及同一 Newton Gaussian。以下先在
$$
\mathscr U=\{P:\ |x(P)|=|y(P)|=1\}
$$
上研究它，故源的原点范数统一有界。

$H$ 只含 $z^{6j}$，原观察只读 $z^{dh}$。在变量 $z$ 上作实际 $\mu_3$ 平均，准确有
$$
\frac13\sum_{j=0}^2\frac{2y_P}{x(\omega^jz)-a}
=\frac{2y_Pa^2}{x(z)^3-a^3}.
$$
因此
$$
\boxed{
\mathfrak F_p(P)=
\mathcal J_{\,2y_Pa^2H/(X-a^3)}'(0),\qquad X=x(z)^3.}     \tag{2}
$$
右边的来源从六次项开始，中心质量为零。所有高阶估计因而是 R301 的六阶来源估计，而不是错误地对一个二阶来源省掉第二个 Newton 项。

写
$$
B_{j,p}=\mathcal L_H(Hx^{-3j}),\qquad
\mathfrak A_p(R)=\sum_{j\ge1}B_{j,p}R^{j-1}.
$$
一致收敛给出完整核
$$
\boxed{\mathfrak F_p(P)=2y_Pa^2\mathfrak A_p(a^3).}        \tag{3}
$$
这里 $\mathfrak A_p$ 是同一原 $H_3$ 的完整解析行，不被当作代数多项式。

## 2. 首层是真实首一多项式

定义一个有限、完全来自原来源的多项式
$$
\boxed{
K_p(R)=\sum_{j=1}^{s}
       [z^{p+1}](H(z)x(z)^{-3j})\,R^{j-1}.}              \tag{4}
$$
这些系数全部 $p$ 整：$x^{-3j}$ 从 $z^{6j}$ 开始，故只读取 $H$ 在首共振 $z^{p+1}$ 之前的系数。R301 中唯一可能影响这一窗口的 sigma 分母恰在被避开的首共振处。

最后一个系数准确为
$$
[z^{p+1}](Hx^{-3s})=1,
$$
所以
$$
\boxed{K_p\in\mathbb Z_p[R]\text{ 首一，且 }\deg K_p=s-1.} \tag{5}
$$

R301 的完整尾界对 (2) 一致适用：所有 $h\ge2$ 的 Newton 项属于 $p^2$。若置
$$
c_p=\kappa^{-1}/p\in\mathbb Z_p^\times,
$$
则
$$
\boxed{
\frac{\mathfrak F_p(P)}p
\equiv2c_p\,y_Pa^2\,\overline K_p(a^3)\pmod p.}            \tag{6}
$$
这个等式在 $\mathscr U$ 的整解析函数环中成立，不只在个别点成立。对该整环，原向量场
$$
\partial_P=2y\,\partial_x+3x^2\,\partial_y
$$
保持整性，故 (6) 也可以准确求导。

具体地，完整核 (3) 的导数为
$$
\boxed{
\partial_P\mathfrak F_p(P)
=2a\left((7r+4b)\mathfrak A_p(r)
       +6r(r+b)\mathfrak A_p'(r)\right),\qquad r=a^3.}    \tag{7}
$$
而它的首层是
$$
\boxed{
\frac{\partial_P\mathfrak F_p(P)}p
\equiv2c_pa\left((7r+4b)\overline K_p(r)
       +6r(r+b)\overline K_p'(r)\right)\pmod p.}          \tag{8}
$$
所以连导数的实际有限首层也已支付，不需假设一个未知核“应当不恒定”。

## 3. 同一个挠点上的两个单位

令
$$
R_p(P)=2\bar c_p\,y(P)x(P)^2\overline K_p(x(P)^3)
$$
为约化曲线上的实际有理函数。由 (5)，它唯一的极在 $O$，极阶为
$$
3+4+6(s-1)=p+2.
$$
因此它非零，且至多有 $p+2$ 个零点，按重数计。

其导数也非零。(8) 括号内的首项系数为
$$
7+6(s-1)=p+2,
$$
故 $\partial_PR_p$ 在 $O$ 的极阶是 $p+3$，首项系数为
$2\bar c_p(p+2)\equiv4\bar c_p\ne0$。它至多有 $p+3$ 个零点。

超奇异曲线的实际 Frobenius 满足 $\operatorname{Frob}_p^2=[-p]$，所以
$$
E_b(\mathbb F_{p^2})=E_b[p+1](\overline{\mathbb F}_p),
\qquad \#E_b(\mathbb F_{p^2})=(p+1)^2.
$$
排除 $R_p$ 和 $\partial_PR_p$ 的零点，再排除 $O$、$x=0$ 的两点及 $y=0$ 的三点，至多排掉 $2p+11$ 点。对 $p>7$，
$$
(p+1)^2>2p+11.
$$
因此存在一个实际剩余点 $\bar T\in\mathscr U(\mathbb F_{p^2})$，使
$$
R_p(\bar T)\ne0,\qquad \partial_PR_p(\bar T)\ne0.
$$
令 $T$ 为其唯一的 $(p+1)$ 挠点提升。由 (6)、(8)，
$$
\boxed{
v_p(\mathfrak F_p(T))=1,\qquad
v_p(\partial_P\mathfrak F_p(T))=1,\qquad [-p]T=T.}         \tag{9}
$$
这对每个上述好惰性 $p$ 成立；不需要原 $S$ 的首权已经非零。

## 4. 全实际单极族不可能只乘一个标量

仍用 R313 的真实算子
$$
\mathscr T_{p,H}T(z)
=-\frac{H(z)}p\sum_{R\in E[p]}
                    \frac{T(-z/p+R)}{H(-z/p+R)}.
$$
R313 的完整第三类迹及 $\mathcal L_H(H)=0$ 准确给
$$
\boxed{
\mathcal L_H\left(\mathscr T_{p,H}
           \left(H\frac{2y(P)}{x-x(P)}\right)\right)
=\mathfrak F_p([-p]P).}                                  \tag{10}
$$
全部 theta 比值仍是这个同源算子的一部分。

假设存在某个 $\alpha\in\mathbb C_p$，对整个实际单极输入族满足
$$
\mathfrak F_p([-p]P)=\alpha\mathfrak F_p(P).               \tag{11}
$$
在 (9) 的固定挠点 $T$ 取值，立即得到 $\alpha=1$。

再令 $P$ 在 $T$ 的剩余盘内。R313 的实际形式群收缩给
$$
[-p]^nP\longrightarrow T.
$$
由 (11)、连续性，
$$
\mathfrak F_p(P)=\mathfrak F_p([-p]^nP)
\longrightarrow\mathfrak F_p(T).
$$
于是 $\mathfrak F_p$ 在这个盘内恒定，与 (9) 的单位导数矛盾。即使 (11) 只先对代数点断言，该盘内的代数点稠密，同一结论仍成立。

因此
$$
\boxed{
\text{全实际单极来源族上不存在任何 }
\mathcal L_H\mathscr T_{p,H}=\alpha\mathcal L_H
\text{ 的标量交织。}}                                    \tag{12}
$$
这里排除所有标量，包括 $1$、$-p$ 和 $p^2$，不是仅检查一个猜测特征值。

(12) 的量词是整个单极族。它并不排除四个指定原 CM 轨道的留数加权和另有真实关系；该关系必须由这四轨道自身及其完整行给出。

## 5. 原十八个非挠极的完整迹轨道不能在有限来源空间闭合

现在回到 R310 的固定二十四极及 R313 的正密度素数族。记十八个非挠极的集合为 $\mathcal D_{\mathrm{nt}}$，用原曲线的 Néron–Tate 高度定义
$$
m=\min_{P\in\mathcal D_{\mathrm{nt}}}\widehat h(P)>0,\qquad
M=\max_{P\in\mathcal D_{\mathrm{nt}}}\widehat h(P)<\infty.
$$
正性来自 R310 已证明这些点全部非挠；这里用的是固定有限点集的高度，未假设一个随 $p$ 变化的统一高度猜想。

当
$$
p^2m>M,                                                   \tag{13}
$$
每一层的高度区间
$$
\widehat h([-p]^n\mathcal D_{\mathrm{nt}})
\subset[p^{2n}m,p^{2n}M]
$$
与其余层互不相交。因此所有非挠支撑在不同层之间严格分离。在同一层内，R313 的好约化及 $\operatorname{Frob}_p^2$ 固定所有原极又保证这些点仍互异，所有原留数非零。

设
$$
\eta_n=g_n\,dz=\sum_a\varrho_a\xi_{[-p]^nP_a}.
$$
原六个三挠极在 $[-p]$ 下固定，因为 $p\equiv-1\pmod3$；其重复不会影响非挠支撑的分离。

还需核 $H$ 是否会消掉新极。原 $H$ 的全部非挠零点恰为 $\mathcal D_{\mathrm{nt}}$。其余零点是 $x=0$、$x^3=-4b$、$x^3=8b$ 的点：前两种是三挠，最后一种由
$$
x([2]P)=\frac{x(P)(x(P)^3-8b)}{4(x(P)^3+b)}
$$
得 $[2]P$ 为非零三挠，故为六挠。$H(0)=1$，原点也不添零。

所以在 (13) 下，每个 $n\ge1$ 的 $Hg_n$ 都在
$[-p]^n\mathcal D_{\mathrm{nt}}$ 有真实非零简单极；这些极既不被 $H$ 消去，也不在任何另一层出现。若有有限关系
$$
c_HH+\sum_{n=0}^Nc_nHg_n=0,
$$
取最大的 $N\ge1$ 并看其一个非挠极，立即得 $c_N=0$；逐层向下得所有 $c_n=0$（$n\ge1$）。最后 $Hg_0=S$、$S(0)=0$、$H(0)=1$ 且 $S\ne0$，也迫 $c_H=c_0=0$。

由 R313 的实际迹公式，
$$
\mathscr T_{p,H}^{\,n}S=Hg_n+A_{p,n}H
$$
且 $A_{p,n}$ 是完整的代数常数项。故
$$
\boxed{
H,\ S,\ \mathscr T_{p,H}S,\ \mathscr T_{p,H}^{\,2}S,\ldots
\text{ 在全局亚纯来源空间中线性无关。}}                  \tag{14}
$$
特别，不存在一个包含原 $S$、并在这个实际同源迹下稳定的有限维全局亚纯来源空间。

这是完整支撑的论证，不会因为一个观测泛函可能杀掉某些来源而失效。它也不排除先证明一个有意义的观察商，再在该商上获得有限矩阵；这样的商及其全中央相容性仍须真实构造，不能从同次数或同一 CM 角色直接推定。

## 6. 原中央行确实不杀 exact 微分

R312 证明的是杀掉 $H$ 方向，即对微分 $f\,dz$ 加全纯常数不改变归一中央斜率。这不能扩充成杀掉任意 exact 微分。

事实上，对每个上述好惰性素数，取曲线上的实际有理函数
$$
R_p=\frac{y}{x^{(p+5)/2}}.
$$
原向量场直接给
$$
\boxed{
R_p'=-(p+2)x^{-(p+1)/2}-(p+5)b\,x^{-(p+7)/2}.}           \tag{15}
$$
两个负幂都是 $x^{-3j}$；其原点展开准确从
$-(p+2)z^{p+1}$ 开始。因此这是合法的同一局部 Newton 来源，且
$$
\|e^{-\kappa z^d}HR_p'\|_R\le R^d.
$$
同一 Newton 界使全部 $h\ge2$ 项属于 $p^2$，得到
$$
\boxed{
\frac{\mathcal L_H(HR_p')}{p}
\equiv-\frac2{34pc}\not\equiv0\pmod p,
\qquad R_p'\,dz=dR_p.}                                  \tag{16}
$$
所以对每一个这些惰性素数，原泛函都不通过全局 de Rham 的 exact 商。

还可用一个不随 $p$ 变化的来源精确核定：取 $R=y/x^5$。原微分和参考给
$$
R'=-7/X-10b/X^2,\quad
[z^6]H=-3154b/15,\quad
x^{-3}=z^6+3bz^{12}/7+\cdots.
$$
所以
$$
\boxed{[z^{12}](HR')=21883b/15.}                          \tag{17}
$$
在 $p=11$、$b=17$，这个系数模 $11$ 为 $b\ne0$，而实际
$pc\equiv3\pmod{11}$。于是
$$
\mathcal L_H(HR')/11\equiv2\pmod{11}.
$$
$HR'$ 一般不是全局全纯 theta 截面，但其局部来源和完整导数都合法。这个固定例与 (16) 一同表明：从 Cartier 或 Frobenius 的 de Rham 关系进入原中央观察时，exact 部分必须保留。不能把原泛函任意解释为一个有限 $H^1_{\mathrm{dR}}$ 的 period。

## 7. 一个原 $H_3$ 的精确有限证书

生产文件：
[check-jzero-actual-pole-kernel-no-scalar.py](../scripts/check-jzero-actual-pole-kernel-no-scalar.py)
及其 JSON；**25 项精确检查全部 PASS**。

脚本在固定 $p=59$ 上，从实际 Weierstrass 递推重建 $H$ 的整个共振前窗口，而不使用一个任意首一多项式。得到
$$
\begin{aligned}
\overline K_{59}(R)={}&
8+31R+27R^2+19R^3+39R^4+57R^5\\
&+29R^6+19R^7+8R^8+R^9.
\end{aligned}
$$
同一原规范给 $pc\equiv39$、$c_p\equiv19\pmod{59}$。

在剩余点 $x=1$、$y^2=18$ 及其唯一六十挠提升 $T$，
$$
\overline K_{59}(1)=2,\qquad
(7+4b)\overline K_{59}(1)
 +6(1+b)\overline K_{59}'(1)=19.
$$
因此
$$
\mathfrak F_{59}(T)/59\equiv17\,y(T),\qquad
\partial_P\mathfrak F_{59}(T)/59\equiv14\pmod{59}.
$$
这同时核定实际来源、归一尺度和单位导数。对所有惰性素数的结论由 §§2–4 的首一性及点数证明，不由这个有限例外推。

直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)、
[R310](R310-jzero-actual-rankzero-frame-third-kind-and-central-transpose.md)、
[R312](R312-original-central-projection-fixed-poles-and-complete-kernels.md)、
[R313](R313-jzero-frobenius-square-actual-trace-and-central-first-layer.md)。

