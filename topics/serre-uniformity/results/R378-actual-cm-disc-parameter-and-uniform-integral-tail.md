# R378：实际 CM 小圆盘的整参数与商映射的统一尾项

**现行范围更正（R575）**：实际参数与局部 Taylor 整性、尾项估计按文中假设保留。R348 的实际秩零商出现性及由此取得的有理点零像撤回，因而本文局部估计不能再以该全局零像为已证输入。完整证明见 [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)。

## 更正前正文（保留供复核，受上述范围更正约束）

**状态：已证明。** 本篇把 R376 的同一 Drinfeld 点进一步变成定义于未分歧底域的实际小圆盘，给出 R348 任意实际 CM 商在该盘上的整函数及逐系数统一下界。由此得到有限精度截断和严格零点证书。所选商的首个非零系数尚未得到统一单位性；本篇没有以尾项控制代替这一全局输入。

## 1. 结论

沿用 R348、R374、R376 的 $p\ge41$、$p\equiv2\pmod3$、
$Z_p$、$c_1$，以及实际非零商
$q:J_{Z_p}\to B$，其中 $B$ 是 R348 的 CM 因子的同源商。记

$$
e=p^2-1,\qquad
\varpi^e=p,\qquad
s=p(p-1),\qquad
D=3p(p-1),\qquad
h=3(p-1).
\tag{378.1}
$$

可在 R376 的同一 tame 扩张上改用 $\varpi$ 为 uniformizer；
$\varpi$ 与该文的 $\pi$ 相差单位。令 $R_0=W(\overline{\mathbb F}_p)$、
$R=R_0[\varpi]$，分式域分别为 $K_0,L$。

在 $c_1$ 的半稳定光滑点的形式完成中，

$$
z=\frac{a-1}{\varpi^D}
\quad\text{是整形式参数，}\qquad
\widehat{\mathcal O}_{\mathcal Z,\overline{c_1}}=R[[z]].
\tag{378.2}
$$

取以 $c_1$ 为原点的参数

$$
w=\frac{a-1}{p^3},\qquad
z=\varpi^h w.
\tag{378.3}
$$

闭圆盘 $|w|\le1$ 在 $Z_p$ 上有一个定义于 $\mathbb Q_p$ 的实际解析提升，且具有光滑整形式模型
$\operatorname{Spf}\mathbb Z_p\langle w\rangle$。这里描述的是这个明确小圆盘的整模型；不需要将它未经证明地识别为某个指定全局最小正则模型的开集。

R315 的实际整数分支具有

$$
r=1-a^3,\qquad v_p(r)=m+3k,\qquad
m\in\{1,2\},\quad k\ge1.
\tag{378.4}
$$

由 R376，它在 (378.2) 的圆盘内，并满足准确深度

$$
v_p(w)=m+3k-3\ge m,\qquad
v_p(z)=m+3k-\frac{3p}{p+1}>1.
\tag{378.5}
$$

令 $b=\dim B$。存在 $b$ 个实际整限制幂级数

$$
G_i(w)=\sum_{n\ge1}b_{i,n}w^n
\in R_0\langle w\rangle,\qquad 1\le i\le b,
\tag{378.6}
$$

以及整数

$$
1\le k_i\le p,\qquad 3\nmid k_i,
\tag{378.7}
$$

使

$$
v_p(b_{i,n})
\ge
\left\lceil\frac{3n-k_i}{p+1}\right\rceil
\ge0\qquad(n\ge1).
\tag{378.8}
$$

这些函数从同一个实际商映射产生，并且

$$
q([P-c_1])=0
\quad\Longleftrightarrow\quad
G_i(w(P))=0\ \text{对所有 }i
\tag{378.9}
$$

对这个圆盘内的点成立。至少一个 $G_i$ 不恒为零。

定义有限整数

$$
M=\min_{\substack{i,n\ge1\\b_{i,n}\ne0}}v_p(b_{i,n})\ge0,
\qquad G_i^\circ=p^{-M}G_i.
\tag{378.10}
$$

那么全部 $G_i^\circ$ 整，且至少一个系数为单位。对任意整数 $H\ge1$，置

$$
N_H=\left\lfloor
\frac{p+(M+H-1)(p+1)}3
\right\rfloor.
\tag{378.11}
$$

有统一且严格的截断界

$$
G_i^\circ(w)
\equiv\sum_{1\le n\le N_H}p^{-M}b_{i,n}w^n
\pmod{p^H R_0\langle w\rangle}.
\tag{378.12}
$$

特别地，若有一个 $G_i^\circ$ 的首个非零系数就是单位，则
$w=0$ 是该圆盘内 $v_p(w)>0$ 的唯一公共零点。
一般情形仍有有限的严格证书，见 §7；不能自动假设这个单位条件成立。

## 2. 从 $p$ 挠点多项式读出变形参数的整尺度

在全级六及完整 $p$ 水平的 Drinfeld 模型上，固定一个提升
$c_1$ 的 CM 点。将其好约化椭圆通用变形写为

$$
\mathcal E_t:\quad Y^2=X^3+tX-1,\qquad T=-X/Y.
\tag{378.13}
$$

这可由将常数项用唯一的、模极大理想等于一的六次根规范化得到。
$p>3$ 保证变换整，且 $t$ 是椭圆模叠的一个通用变形参数。

在这个全层 Drinfeld 点附近，令 $\mathcal A$ 为相应完成的光滑局部环。
完整 $p$ 水平给出所有 $p^2$ 个挠点的形式坐标 $T(S)\in\varpi\mathcal A$。
若 $P,Q$ 是所选完整基，则

$$
\overline{T(aP+bQ)/\varpi}=a\alpha+b\beta
\quad(a,b\in\mathbb F_p).
\tag{378.14}
$$

这是整形式群加法的一次项，R376 已识别其 Drinfeld 坐标。
$\alpha,\beta$ 在 $\mathbb F_p$ 上独立。

写乘 $p$ 幂级数的 Weierstrass 分解为

$$
[p](T)=U(T)W(T),\qquad
W(T)=\prod_{S\in\mathcal E[p]}(T-T(S))
 =T^{p^2}+\sum_{j=1}^{p^2-1}w_jT^j,
\quad U(T)\in\mathcal A[[T]]^\times.
\tag{378.15}
$$

恒等式可先在泛纤维的分裂挠点上验证，再由平坦性下降。
各根属于 $\varpi\mathcal A$，故

$$
w_j\in\varpi^{p^2-j}\mathcal A.
\tag{378.16}
$$

设 $c_p(t)$ 是 $[p](T)$ 中 $T^p$ 的系数。比较 (378.15) 的次数 $p$ 项得

$$
c_p(t)\in\varpi^s\mathcal A,\qquad
\overline{\frac{c_p(t)}{\varpi^s}}
 =\overline{U(0)}
  \,\overline{\frac{w_p}{\varpi^s}},
\quad s=p^2-p.
\tag{378.17}
$$

因为所有 $j<p$ 的贡献都多含至少一个 $\varpi$。

另一方面，$c_p(t)$ 模 $p$ 是形式群的 Hasse 标量。R290/R294 已给出在任意特征 $p$ 底环上的完整计算。写 $p=6r+5$，则在 (378.13) 中，Hasse 多项式是
$(X^3+tX-1)^{(p-1)/2}$ 的 $X^{p-1}$ 系数；它的首项为

$$
c_0t,\qquad
c_0=(-1)^r\frac{(3r+2)!}{(2r+1)!\,r!}\in\mathbb Z_p^\times,
\tag{378.18}
$$

其余非零项的 $t$ 次数均为 $1\bmod3$。所以

$$
c_p(t)=tV(t)+pW_0(t),\qquad
V(t)\in R_0[[t]]^\times,\quad W_0(t)\in R_0[[t]].
\tag{378.19}
$$

此处只需要 $V(0)$ 为单位；换一个首项为单位的形式参数不影响结论。
因为 $p=\varpi^e$ 且 $e>s$，(378.17)–(378.19) 给

$$
t\in\varpi^s\mathcal A.
\tag{378.20}
$$

接下来核准除去这个幂后的函数在 CM 点确有单位一次项。

## 3. Dickson 不变量与 CM 点的单位一次项

由 (378.14)，

$$
\overline{\varpi^{-p^2}W(\varpi Z)}
 =\prod_{a,b\in\mathbb F_p}(Z-a\alpha-b\beta)
 =Z^{p^2}-\mathcal D Z^p+\mathcal C Z,
\tag{378.21}
$$

其中

$$
\mathcal D
=\frac{\alpha^{p^2}\beta-\alpha\beta^{p^2}}
       {\alpha^p\beta-\alpha\beta^p}.
\tag{378.22}
$$

分母在 Drinfeld 仿射曲线上为非零常数。该公式也可直接由要求
$\alpha,\beta$ 为右边线性化多项式的根解出，不需要另外引用不变量论。

保留 R376 的 Cartan 特征坐标
$(A_0,B_0)=(\widetilde\alpha,\widetilde\beta)$，使

$$
A_0^{p+1}-B_0^{p+1}=c,\qquad
U=A_0^{p+1}-c/2,\qquad V=A_0B_0.
\tag{378.23}
$$

反向线性变换的系数互为 $p$ 次方。代入 (378.22) 得

$$
\mathcal D
=-\frac Vc
\left((U+c/2)^{p-1}-(U-c/2)^{p-1}\right).
\tag{378.24}
$$

例如，在 $B_0=0$ 的 CM 提升处，$U=c/2$、$V=0$，故

$$
\mathcal D=-c^{p-2}V+O(V^2).
\tag{378.25}
$$

该一次系数非零。另一个 CM 提升 $A_0=0$ 给相同结论。
由 (378.17)–(378.21)，函数

$$
\tau=t/\varpi^s
\tag{378.26}
$$

在 CM 点的约化是非零常数乘以 $\mathcal D$，因此是一个整形式参数。

这里先在细模问题上进行。范数一 Cartan 在这两个 CM 提升的仿射轨道上自由作用，正规化子交换二者，因而在商后的选定局部支上不会再造成分歧。具体地，
$Y=UV$ 在 $U=\pm c/2$ 为单位乘以 $V$，所以
(378.25) 在 R376 的细模正规化子商的局部参数中仍有单位一次项。

最后取 $a=1$ 支的有效几何 $\mu_3$ 商。该作用在 $t$ 上为非平凡三次特征，在 $\varpi$ 上平凡，故在 $\tau$ 上同样为这个特征。它的局部不变量环是
$R[[\tau^3]]$。同时有准确的 $j$ 公式

$$
j(\mathcal E_t)
 =\frac{6912t^3}{4t^3+27},
\tag{378.27}
$$

而 $a-1$ 是 $j$ 的单位乘子，见 R376.14。于是

$$
\frac{a-1}{\varpi^{3s}}
 =\tau^3\cdot\text{单位}
\tag{378.28}
$$

在粗局部环中成立，且右边的单位为 $\tau^3$ 的整幂级数。
这证明 (378.2)。这里的尺度是
$3p/(p+1)$，不是 $3/(p+1)$；前者来自 $T^p$ 系数的次数
$p^2-p$。

## 4. 实际未分歧小圆盘与 Galois 作用

$\mu_e\subset K_0$，且 $L/K_0$ 为循环 tame 扩张。选生成元 $\sigma$，使

$$
\sigma(\varpi)=\xi\varpi,
\qquad \xi\text{ 为原始 }e\text{ 次单位根}.
\tag{378.29}
$$

$a$ 为定义于 $\mathbb Q_p$ 的函数。由 (378.2)，

$$
\sigma(z)=\xi^{-D}z=\xi^h z,
\qquad D+h=3e.
\tag{378.30}
$$

这是整个形式圆盘上的准确恒等式，不只是特殊纤维的切线特征。

作代换 $z=\varpi^h w$。任意 $R[[z]]$ 的幂级数经此代换后属于
$R\langle w\rangle$，因为 $h>0$。在这个小圆盘上 $\sigma(w)=w$，
且

$$
(R\langle w\rangle)^{\operatorname{Gal}(L/K_0)}
 =R_0\langle w\rangle.
\tag{378.31}
$$

因此该实际解析圆盘下降到 $K_0$，有光滑整模型
$\operatorname{Spf}R_0\langle w\rangle$。
因 $c_1$ 和函数 $a$ 都在 $\mathbb Q_p$ 定义，$j$ 映射在泛纤维
$c_1$ 处不分歧，其以 $c_1$ 为中心的局部反支唯一；这个反支的全部展开系数在 $\mathbb Q_p$。上述收敛半径估计因此也给出
$\mathbb Q_p$ 上的闭圆盘及
$\operatorname{Spf}\mathbb Z_p\langle w\rangle$ 的模型。
这不是任意选择另一个较有利的水平结构：反支已经由 $c_1$ 固定。

对实际分支，$a\equiv1\bmod p$，且 $1+a+a^2\equiv3\bmod p$。
所以 $v_p(a-1)=v_p(r)$，给出 (378.5)。
R376 的有限平坦同构比较保证实际点确实在这个反支内。

## 5. 好约化目标的整特征坐标

由 R376，$B_L$ 有好约化，记其 abelian scheme 为 $\mathcal B/R$。
完成零截面得到

$$
\widehat{\mathcal B}_0\simeq\operatorname{Spf}R[[Y_1,\ldots,Y_b]].
\tag{378.32}
$$

其 Galois 下降作用保持零截面。令 $\iota$ 是 $\sigma$ 在特殊纤维的自同构。R348/R374 的 CM 惯性角色均有阶整除 $p+1$，且在惯性的三阶子群上都非平凡。通过异于 $p$ 的 Tate 模的忠实性，有

$$
\iota^{p+1}=1,\qquad
1+\iota^{e/3}+(\iota^{e/3})^2=0.
\tag{378.33}
$$

第二式对切空间也成立，三在剩余域中可逆，故该三阶元素没有特征值一。

因为 $e$ 与 $p$ 互素，可以对特殊纤维余切空间作特征分解。
其特征指数可以准确写成

$$
t_i=(p-1)k_i,\qquad
1\le k_i\le p,\qquad 3\nmid k_i.
\tag{378.34}
$$

这里第一个整除条件来自 $\iota^{p+1}=1$；第二个非平凡条件来自
(378.33)，并用到 $p-1\equiv1\bmod3$。
不需要指定全部 $k_i$ 的排列或假定一个整 CM idempotent。

选择这些余切特征向量的任意整坐标提升，再对循环 Galois 群用
$e^{-1}\sum_{j=0}^{e-1}\xi^{-jt_i}\sigma^j$ 平均，可以将坐标选成

$$
\sigma(Y_i)=\xi^{t_i}Y_i
\quad\text{在整个 }R[[Y_1,\ldots,Y_b]]\text{ 上}.
\tag{378.35}
$$

平均保留其模极大理想的相应一次项，因而所得坐标仍是整形式参数系。
这一步是对实际好模型做的，没有从一个仅在有理表示上存在的分解猜测整坐标。

设 $f(P)=q([P-c_1])$。在 (378.2) 的盘上，R376 的延拓给

$$
F_i(z)=f^*Y_i=\sum_{n\ge1}a_{i,n}z^n\in R[[z]].
\tag{378.36}
$$

常数项为零。全部 $a_{i,n}$ 事实上都含 $\varpi$，因为 R376 已证明特殊纤维的整条分量收缩；下文只用它们为整。

由 Galois 等变性、(378.30)、(378.35)，

$$
\sigma(a_{i,n})=\xi^{t_i-nh}a_{i,n}.
\tag{378.37}
$$

令 $r_{i,n}$ 是 $t_i-nh$ 模 $e$ 的最小非负代表。
$L$ 的这个特征空间为 $\varpi^{r_{i,n}}K_0$。因
$0\le r_{i,n}<e$ 且 $a_{i,n}$ 整，可以准确写成

$$
a_{i,n}=\varpi^{r_{i,n}}c_{i,n},
\qquad c_{i,n}\in R_0.
\tag{378.38}
$$

特别，不会出现一个因忽略取整而漏掉的 $p^{-1}$ 系数：
若 $c_{i,n}$ 的整数赋值为负，$a_{i,n}$ 的赋值也必为负。

现在定义实际归一化函数

$$
G_i(w)=\varpi^{-t_i}F_i(\varpi^h w).
\tag{378.39}
$$

由 (378.38)，

$$
b_{i,n}
 =p^{d_{i,n}}c_{i,n},\qquad
d_{i,n}
 =\frac{r_{i,n}+nh-t_i}{e}
 =\left\lceil\frac{3n-k_i}{p+1}\right\rceil.
\tag{378.40}
$$

对 $n\ge1$、$1\le k_i\le p$，此整数非负，并随 $n$ 线性趋于无穷。
这同时证明 (378.6)、(378.8) 及闭单位圆盘上的收敛。

在这个盘上，$f(P)$ 落在 $\mathcal B$ 的形式零邻域，且
$Y_i(f(P))=\varpi^{t_i}G_i(w(P))$。
形式参数同时为零当且仅当点为单位元，证明 (378.9)。
若全部 $G_i$ 恒为零，$f$ 在一个非空解析开集上恒为零，因而在连通代数曲线上恒为零；Abel–Jacobi 像生成 Jacobian，于是 $q=0$，与假设矛盾。

此构造与形式对数的作用相同，都是把准确零像变成解析方程，但直接使用整群坐标避免了积分中 $1/n$ 的额外分母。没有把这些归一化坐标未经证明地称作原 $\mathbb Q_p$ Néron 模型的整参数。

## 6. 统一截断、一个有限零点上界

取 $M$ 如 (378.10)。因所有系数属于离散赋值环 $R_0$，且至少一个非零，最小值是有限非负整数。由 (378.40)，归一化系数满足

$$
v_p(p^{-M}b_{i,n})
\ge
\max\left\{0,\
\left\lceil\frac{3n-k_i}{p+1}\right\rceil-M\right\}.
\tag{378.41}
$$

如果
$3n>k_i+(M+H-1)(p+1)$，右边至少为 $H$。
再用 $k_i\le p$，即得 (378.11)–(378.12)。

设 $G_i^\circ$ 有一个单位系数，令 $n_0$ 为其第一个单位系数的次数。则

$$
1\le n_0\le
N_1=\left\lfloor\frac{p+M(p+1)}3\right\rfloor.
\tag{378.42}
$$

对任意整数 $\lambda\ge1$，代入 $w=p^\lambda T$。
次数 $n_0$ 的系数赋值为 $\lambda n_0$，所有 $n>n_0$ 的系数赋值至少为
$\lambda n>\lambda n_0$。所以此限制幂级数的最小系数赋值的最大达到次数不超过 $n_0$。Strassmann 的论证给出

$$
\#\{w:v_p(w)\ge\lambda,\ G_i^\circ(w)=0\}
\le n_0\le N_1,
\tag{378.43}
$$

计重数；同一个界对公共零点成立。
这个论证在任意完备扩张内仍适用：将系数除以最小赋值的幂后，最大单位系数次数为 $d$；每除去一个闭单位圆盘内的线性根因子，该次数减一，故最多有 $d$ 个根。因而不需要假设剩余域有限。

该上界依赖实际共同因子 $M$，没有给 $M$ 的统一上界，也不是 Serre 的绝对排除界。

## 7. 精确的有限首项证书

设某个非零 $G_i^\circ$ 的首个非零次数为 $d$，其系数记为
$\gamma_d$，并记 $\nu=v_p(\gamma_d)$。全部较高系数都整。

如果 $\nu=0$，则

$$
G_i^\circ(w)
 =w^d\left(\gamma_d+w\,H(w)\right),
\quad H(w)\in R_0\langle w\rangle.
\tag{378.44}
$$

对 $v_p(w)>0$，括号中是单位，故唯一零点为 $w=0$。
这允许 CM 零点有任意有限重数 $d$，并不要求形式浸入。

一般情形，给定实际下界 $\lambda_0=m\in\{1,2\}$，只要检查

$$
v_p(\gamma_n)+(n-d)\lambda_0>\nu
\quad\left(
d<n\le d+\left\lfloor\frac{\nu}{\lambda_0}\right\rfloor
\right),
\tag{378.45}
$$

就已保证所有 $v_p(w)\ge\lambda_0$ 的非零点都不是零点。
因为对更大的 $n$，整性自动给
$v_p(\gamma_n)+(n-d)\lambda_0>\nu$。
所有这些有限系数的必要精度，以及尾项不影响判断，均可由
(378.11)–(378.12) 给出。

在实际取得这些系数之前，(378.45) 只是一个精确的可用证书形式。尤其不能从“至少一个单位系数”跳到“首个非零系数为单位”。

为了明确这个缺口确实未由已有局部信息消除，取一个允许的
$k_i\ge7$、$3\nmid k_i$，并考虑形式上的

$$
G(w)=p^A w+w^2,\qquad A\ge1.
\tag{378.46}
$$

它满足 (378.8) 的全部下界，常数项为零，且其对应
$F(z)=\varpi^{t_i}G(z/\varpi^h)$ 为整并在特殊纤维恒为零。
但除了零，还具有任意深的零点 $w=-p^A$。
这不是构造了一个实际模曲线反例；它只证明已核的局部尺度、下降特征和尾项估计本身不能推出唯一零点。实际商的系数必须进一步输入。

## 8. 本篇完成的接口与下一项具体工作

R376 的好约化基变换收缩，经过本篇的
$w=(a-1)/p^3$ 和 $\varpi^{-t_i}$ 归一化后，产生的是同一个实际商的整解析方程，而不是另一个任意局部匹配族。
R374 对所选秩零商给准确的 $q([P-c_1])=0$，所以任何原实际候选都必须同时满足这些方程。

已解决的部分是：实际源参数、其定义域、实际候选的准确深度、目标坐标的整尺度、每个无限尾项及有限检验证书。
尚未解决的是：证明在 R348 保证存在的某个非零中心值因子中，实际首项满足 (378.44) 或 (378.45)，或得到足以同样排除实际候选的其他系数关系。
特别没有证明 $M=0$、没有证明一个给定 $G_i$ 的一次系数为单位，也没有把正根数或非零复中心值转换成上述 $p$ 进单位性。

## 9. 原文与依赖

- B. Edixhoven, P. Parent, *Semistable Reduction of Modular Curves Associated with Maximal Subgroups in Prime Level*, Documenta Mathematica **26** (2021), 231–269，Theorem 2.3、§2.2.1 的式 (2)–(5)、§3.1–3.4 的商坐标。R376 已逐步对齐本实际六层。
  [原刊 PDF](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)
- B. Edixhoven, P. Parent, *Regular models of modular curves in prime level over $\mathbb Z_p^{\mathrm{ur}}$*, Documenta Mathematica **29** (2024), 1017–1058，DOI 10.4171/DM/974。§2、Proposition 2.1（1020–1022 页）明确可用 $p^{1/(p^2-1)}$ 作参数并给整个 tame 群与模 $p$ 水平群的联合动作。本篇的准确参数与小圆盘下降由 §§2–4 独立算出，不依赖未核的全局模型同一断言。
  [原刊](https://ems.press/journals/dm/articles/14298148)
- Hasse 标量使用 R290/R294 的自含证明；好约化 CM 角色、全部同源代表及三阶惯性恒等式使用 R374、R376。有限零点论证已在 §6 展开。

本篇为纯证明，无扫描或数值数据。
