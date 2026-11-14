# R710 — 实际平方 jet 的未分歧下降与完整粗 Abel 约化

状态：**已证明。** 第 1–6 节为全素数结构定理；第 7 节精确数字已在
公开 Actions 43589720709 从固定原证书提取完成。

全篇取 $p\ge41$、$p\equiv5\pmod6$。保持 R575/R588/R592/R705
的实际正三次族、$\theta=\theta_{-1}$、原 tame 向量、Cartan 平均、
Hodge 帧和两个不同坐标：$Y$ 是固定 CM 椭圆曲线的整形式坐标，
$z_{\rm f}$ 是原模曲线的 flat 变形坐标。
以下不把二者等同。

## 1. 完整定理

记 $q=p^2$、$e=q-1$、$\sigma=p/(p+1)$，并沿用
$\alpha^3=4$、$\beta^2=3$、$\zeta^2+\zeta+1=0$ 和 R705 的单位 $B$。
原实际 Abel 原函数为

$$\mathcal I(z_{\rm f})=
\sum_{j\ge1}\frac{M_{3j-1}}{(3j)!}z_{\rm f}^{3j}.$$

设

$$V=\frac{z_{\rm f}^3}{p^3},\qquad
P_p(V)=p^{-2}\mathcal I(z_{\rm f})
=\sum_{j\ge1}b_jV^j,\qquad
b_j=\frac{p^{3j-2}M_{3j-1}}{(3j)!}.$$

则有以下全素数结论。

1. 存在一个有限未分歧 $p$ 进域 $K_0$，使每个实际允许 jet
   $M_m$（$m\ge2$、$m\equiv2\pmod3$）满足 $M_m^2\in K_0$。
   因而 $2v_p(M_m)\in\mathbb Z$，零值按赋值 $+\infty$ 处理。
   不据此声称 $M_m$ 自身在未分歧域内。
2. 在一个固定有限扩域 $K'/K_0$ 的整数环上，
   $$P_p\in\mathcal O_{K'}\langle V\rangle.$$
   令 $j_*=(p-2)/3$、$J=(p+1)/3=j_*+1$。其剩余多项式
   $\overline P_p$ 的次数至多 $J$，而 $j_*$ 次系数非零，并且
   $$\overline b_{j_*}^{2}
   =-\frac{\zeta^2\alpha^2}{12B^8}.$$
   因此次数恰为 $j_*$ 或 $J$。
3. 在原粗参数 $s=a-1$、$v=s/p^3$ 中，同一个归一原函数仍属于
   $\mathcal O_{K'}\langle v\rangle$，其约化精确为
   $$\overline P_p\bigl((3/8)v\bigr).$$
   所有非线性换参项都约化为零，既不改变约化的最低次数，也不改变
   上述最高次数界。

这里约化是对 $\mathcal O_{K'}$ 的极大理想约化；需要平方系数时，
使用 R705 给出的模 $p$ 精确恒等式。微分与实际商 Abel 对数之间的
非零常数始终保留：它把整个原函数乘以同一个标量，不影响零集，
但其赋值没有被称为单位。

## 2. 确切的未分歧 CM 坐标和实际 torsion 幂

取良好约化 CM 曲线

$$E_0:y^2=x^3-1,\qquad \omega=dx/(2y).$$

其 $p$ 进 CM 基是 $W(\mathbb F_{p^2})[1/p]$。必要时只作有限
未分歧扩张，以包含原六挠点、$\chi_6$、$\theta$ 的值和 $\zeta$。
这些都是 prime-to-$p$ 的数据：六挠群在良好模型上有限 étale，
$\theta$ 的阶整除 $p+1$，$\mu_{p^2-1}$ 是未分歧 Teichmüller 群。

R589 的形式 CM 作用定义在这个未分歧基的整数环上。若 $u$ 是整
参数、线性项为一，令

$$Y=\frac1e\sum_{\xi\in\mu_e}\xi^{-1}[\xi](u).$$

每个 $[\xi]$ 都是定义在该基上的整形式 CM 自同态，$e$ 为单位。
因此 $Y$ 的系数在该未分歧整数环中，线性项仍为一，并且
$[\xi]^*Y=\xi Y$。这是在整形式群上的等变参数，不是从分歧
torsion 域选取的坐标。

同一坐标中 R589 的完整乘法律为

$$[p](Y)=Y\left(p+a_1Y^e+a_2Y^{2e}+\cdots\right),
\qquad a_1\equiv-1\pmod p,\quad a_i\equiv0\pmod p\ (i\ge2).$$

所有 $a_i$ 都在未分歧整数环中。设

$$F(T)=p+a_1T+a_2T^2+\cdots.$$

在 $T\in p\mathcal O_{K_0}$ 上此级数收敛，$F(0)\in p\mathcal O_{K_0}$，
$F'(0)=a_1$ 为单位。形式 Hensel 迭代在 $p\mathcal O_{K_0}$ 中给出
唯一根 $T_0$。其赋值为一，并且 $T_0/p\equiv1\pmod p$。

若 $\varpi=Y(P)$ 为原标记的任一非零 $p$ 挠点坐标，则
$v_p(\varpi)=1/e$，$T=\varpi^e\in p\mathcal O_{\overline{\mathbb Q}_p}$
满足同一个 $F(T)=0$。单位导数的唯一性在任一扩张中仍成立，故

$$\boxed{\varpi^e=T_0\in p\mathcal O_{K_0},\qquad v_p(T_0)=1.}$$

特别地，$\varpi$ 本身可以分歧；本步下降的是其确切的 $e$ 次幂。
这里使用了完整乘法律和 Hensel 唯一性，不能仅从
$\varpi^e/p\equiv1$ 的剩余合同式就断言下降。

## 3. 所有阶的完整 Fourier 乘积和有限范数均在未分歧域

### 3.1 完整 Kronecker 系数

在同一原六挠标记下，令

$$H^-(P,v)=\sum_Q\chi_6(Q)^{-1}\Theta_Q(P,v),\qquad
H_r(P)=[u^rv^r]H^-(P+u,v).$$

对每个固定 $r$，包括 $r\ge p$，完整 Kronecker 系数都是实际
completed primitive $E$ 的有限多项式，其系数为定义在 $K_0$ 的
椭圆有理函数。完整逆 sigma 因子仍保留。
这只是在特征零中断言系数所属域；不把 R658 的 $r<p$ 整性结论
错误地延伸到高阶，也不删去 $r!$ 中的 $p$ 因子。

原 $E(Y)$ 是 $-x\omega$ 的奇原函数，并由 R589 的除法多项式
恒等式识别为原代数 completed 值。其系数在 $K_0$，且
$v_p(e_k)\ge-v_p(k)$。故其在 $Y=\varpi$ 收敛。对固定 $r$，
上述有限多项式及其完整有理系数也在该点收敛；其 Taylor 系数
$h_{r,n}$ 在 $K_0$。tame 求和后的函数在 $Y=0$ 正规，因而可写

$$H_r(Y)=\sum_{n\ge0}h_{r,n}Y^n.$$

即使 $r\ge p$，任何阶乘只带来固定有理分母，不改变所属域；
随 $n$ 的 primitive 分母增长至多为固定倍数的 $\log n$，所以
下列整轨道筛选后的级数仍收敛。

### 3.2 两个完整轨道和的下降

实际 $\theta=\theta_{-1}$ 对第一和选取指数 $p-1\pmod e$，
其逆角色对第二和选取指数 $p(p-1)\pmod e$。因此对于每个
$m\ge2$、$m\equiv2\pmod3$，不是只对前几阶，

$$S_m=-e\varpi^{p-1}
\sum_{j\ge0}h_{m,p-1+je}T_0^j,$$
$$S_{m+1}=-e\varpi^{p(p-1)}
\sum_{j\ge0}h_{m+1,p(p-1)+je}T_0^j.$$

括号内的两个收敛和均属于完备域 $K_0$，而两个前置指数的和为
$(p-1)+p(p-1)=e$。从而

$$\boxed{S_mS_{m+1}\in K_0.}$$

这里只断言完整乘积下降；两个单独的和一般仍含 $\varpi$ 的分歧
幂，不能分别称为未分歧值。

### 3.3 $N_\theta$ 不含隐藏的 $\zeta_p$

R434/R592 的有限型基 $e_r$ 上，Borel 作用为置换；Weyl 作用为

$$we_r=-\frac1p\sum_{y\in\mathbb F_{p^2}^{\times}}
\theta(y)e_{r\operatorname N(y)+\operatorname{Tr}(y)}.$$

因此所有有限矩阵元素都属于 $\mathbb Q_p(\theta)$，该域未分歧。
式中的 $1/p$ 影响整性而不影响域；R434 的纤维角色和又证明
真实商格上的这些矩阵实际是整的。整数 Hermitian 矩阵为
$G(e_r,e_s)=p\delta_{rs}-1$，实际 Cartan 平均的分母为单位 $p+1$。
于是 R588 的

$$N_\theta=G(e_0,\operatorname{Tr}_{\mathsf T}e_0)
=(p+1)G(A_{\mathsf T}e_0,A_{\mathsf T}e_0)$$

在同一个未分歧域内，且 $N_\theta\equiv-1\pmod p$。
角色共轭只把 $\theta$ 换成 $\theta^{-1}$，仍在同域中。

$\zeta_p$ 只出现在随后把抽象 $e_r$ 送到模形式 cusp 展开的式子
$f_r=\sum a_n\zeta_p^{-nr}Q^n$，没有进入上述有限矩阵或
$N_\theta$ 的定义。因此这一步不对实际模形式值的分歧性作循环假设。

### 3.4 高阶 norm 身份与平方 jet

R705 §2 已证明，对全部允许 $m$，实际 norm 身份为

$$M_m\overline M_m
=\frac{[m!(m+1)!]^2N_\theta}{18(p+1)^2}S_mS_{m+1},
\qquad \overline M_m=-\zeta M_m.$$

这两个等式是特征零精确恒等式：相同 tame 向量、有限局部因子、
两组阶乘和原周期均已保留，不要求 $m<p$。
高阶的 factorial $p$ 因子不能删，但它们是有理数，故不影响
所属域。结合前面两小节，得到

$$\boxed{M_m^2\in K_0,\qquad 2v_p(M_m)\in\mathbb Z.}$$

实际复共轭不必稳定选定 $p$ 进位置；这里使用的是先在代数数中
证明的 $\overline M_m=-\zeta M_m$，然后施加同一个位置。
这一步没有把 $v_p(M_m)$ 升格为整数。

还可选取一个固定有限扩域容纳全部这些 jets。因为 $p$ 为奇数，
$K_0^\times/(K_0^\times)^2$ 由一个非平方单位和 $p$ 生成，
取 $K_1=K_0(\sqrt u,\sqrt p)$ 即含每个 $K_0$ 元素的平方根。
所有 $M_m$ 因而在 $K_1$ 中，其赋值群至多为 $\tfrac12\mathbb Z$。

## 4. 全部阶乘与唯一边界项的赋值

先不除以 $p^2$，记

$$E_j=\frac{p^{3j}M_{3j-1}}{(3j)!}=p^2b_j.$$

R592 的完整 Hodge/flat 界是

$$v_p(M_n/n!)\ge-n\sigma.$$

注意该式已经含有 $n!$，不能在高阶处再次遗漏或重复扣除它。
由 $(3j)!=(3j)(3j-1)!$ 精确得到

$$\boxed{v_p(E_j)\ge
\sigma+\frac{3j}{p+1}-v_p(3j).} \tag{710.1}$$

该界随 $j$ 趋于无穷而趋于无穷，因为
$v_p(3j)\le\log_p(3j)$。此外，$E_j$ 只比 $M_{3j-1}$ 相差
有理数，所以由第 3 节，$v_p(E_j)\in\tfrac12\mathbb Z\cup\{\infty\}$。

对于 $1\le j\le j_*=(p-2)/3$，R705 的实际前缀给
$v_p(M_{3j-1})\ge2-3j$，且 $(3j)!$ 是单位。故

$$v_p(E_j)\ge2,\qquad v_p(E_{j_*})=2.$$

唯一相邻边界项是 $j=J=(p+1)/3$。此时 $3j=p+1$，不被 $p$
整除，(710.1) 给

$$v_p(E_J)\ge\frac{2p+1}{p+1}=2-\frac1{p+1}>\frac32.$$

半整数赋值格因此给 **$v_p(E_J)\ge2$**。这里对应的是 $M_p$，
不能使用 R705 的 $m\le p-3$ 前缀来代替这个独立论证。

若 $j\ge J+1$ 且 $h=v_p(3j)=0$，则

$$v_p(E_j)\ge\sigma+\frac{p+4}{p+1}
=2+\frac2{p+1}>2.$$

若 $h\ge1$，由于 $p\ne3$，有 $p^h\mid j$，故 $j\ge p^h$，
于是

$$v_p(E_j)\ge\sigma+\frac{3p^h}{p+1}-h>2.$$

最后的不等式在 $h=1$ 为 $3-4/(p+1)>2$；当 $h$ 增加一时，
右端增加 $3p^h(p-1)/(p+1)-1>0$。这覆盖全部 $p$ 可除的指标，
不是仅检查最初几个 $j$。

所以每个 $j>J$ 的 $E_j$ 都有赋值至少 $5/2$，并且赋值趋于无穷。
除以 $p^2$ 得

$$b_j\in\mathcal O_{K_1}\quad(\text{所有 }j),\qquad
v_p(b_j)\ge\tfrac12\quad(j>J),\qquad v_p(b_j)\longrightarrow\infty.$$

这证明完整的 Tate 级数整性和有限约化次数界。

R705 端点 $m=p-3$ 给

$$\bigl(p^{p-4}M_{p-3}\bigr)^2
\equiv-\frac{\zeta^2\alpha^2}{12B^8}\pmod p.$$

此时 $b_{j_*}=p^{p-4}M_{p-3}/(p-2)!$，而
$(p-2)!\equiv1\pmod p$，故第 1 节的非零端点平方成立。

更一般地，对 $1\le j\le j_*$、$m=3j-1$，R705 给完整前缀平方

$$\overline b_j^{\,2}
=\frac{864\zeta^2}{\alpha^2}\frac{(m-2)!}{(m+1)!}B^{2m+1}
\mathfrak r_{p+2-m}\mathfrak r_{p-m-1}.$$

该式所有前置因子都为单位，R683 的实际六挠 Cartier 比较因而给

$$\overline b_j\ne0\quad\Longleftrightarrow\quad
C_{p+3-3j}C_{p-3j}\ne0\pmod p.$$

这里每个固定 CM 系数使用 R683/R697 的原归一；没有把平方相位
通过任意选根改写成一个未经证明的系数符号公式。

## 5. 原粗参数中的全部换参

不能只取首项 $z_{\rm f}^3=(3/8)s+\cdots$ 而忽略高次系数的
分母。R592/R705 给完整的整变换

$$w=s/\lambda^3,\qquad U=z_{\rm f}^3/\lambda^3=\Phi(w),
\qquad \Phi\in w\mathcal O[[w]],\quad \Phi'(0)=3/8,$$

其中 $v_p(\lambda)=\sigma$。取

$$\kappa=p^3/\lambda^3,\qquad v_p(\kappa)=3/(p+1)>0.$$

对原粗变量 $v=s/p^3$，完整换参正是

$$V=\Psi(v)=\kappa^{-1}\Phi(\kappa v)
=\frac38v+\sum_{n\ge2}\phi_n\kappa^{n-1}v^n.$$

各 $\phi_n$ 整，故非线性项系数赋值至少
$3(n-1)/(p+1)$，严格正且趋于无穷。于是

$$\Psi\in\mathcal O_{K'}\langle v\rangle,\qquad
\overline\Psi=(3/8)v,$$

其中只需把 $K_1$ 再有限扩张以包含 $\lambda$。对 $v_p(v)\ge0$，
有 $v_p(\Psi(v))=v_p(v)$。线性项为单位，全部非线性系数有共同
严格正的赋值下界；逐次代入
$v=(8/3)(V-(\Psi(v)-(3/8)v))$ 是严格压缩，给闭单位盘上唯一
逆变换。这也说明换参保留整个开单位盘及其零的重数。

将完整受限级数 $P_p$ 与 $\Psi$ 复合，得到同一粗 Abel 原函数，
且约化为 $\overline P_p((3/8)v)$。因此没有隐藏的高次换参项
返回改变约化多项式。

## 6. 约化最低次数与真正零集的准确边界

设 $r$ 是 $\overline P_p$ 的最低非零次数。前面证明
$1\le r\le j_*$。这使实际特征零 Abel 原函数的首阶 $d$ 满足
$1\le d\le r$，但不能推出 $d=r$：低于 $r$ 的系数可以非零，
只是其赋值为正。

这个实际剩余次数还具有精确的固定 CM 判据

$$\boxed{r=\min\{1\le j\le(p-2)/3:
C_{p+3-3j}C_{p-3j}\not\equiv0\pmod p\}.}$$

终点 $(C_5,C_2)=(9/2,-1/2)$ 保证这个集合非空。

还可准确控制开单位盘的零。对完备 DVR $\mathcal O_{K'}$，
$\overline P_p=V^r\overline U$、$\overline U(0)\ne0$。形式
Weierstrass 分解给

$$P_p=W_r(V)U(V),$$

其中 $W_r$ 是首一 $r$ 次多项式，其低次系数全在极大理想中，
$U\in\mathcal O_{K'}[[V]]^\times$。此分解可直接逐位构造：若
已模 $\pi^n$ 分解，把误差除以 $\pi^n$，先将其除以
$\overline U$ 并对 $V^r$ 取余，得到对 $W_r$ 的次数小于 $r$
的修正；剩余项可被 $V^r$ 整除，给出对 $U$ 的修正。完备性给
极限和精确恒等式。

$U$ 在 $v_p(V)>0$ 上收敛且不为零；$W_r$ 的每个根都有严格正
赋值，因为负赋值时首项唯一最小，零赋值时约化不能是
$V^r$ 的非零根。因此，在代数闭包中，实际标量 Abel 原函数在
$v_p(V)>0$ 的零总重数恰为 $r$，其中 $V=0$ 的重数为实际 $d$。
非零零点总重数为 $r-d\le r-1$。

特别地，若原 $C_pC_{p-3}\ne0\pmod p$，则 $r=1$，因此该原
primitive 在整个 $v_p(a-1)>3$ 开盘上仅有中心零，且该零简单。
这给 R592 的局部唯一零结论一个完整残差多项式表述；实际
$\mathbb Q_p$ 候选的整数赋值条件 $v_p(a-1)\ge4$ 包含在此范围内。

R705 已把此原函数以非零常数接到同一实际正三次商的 Abel
线性泛函。因此任何该实际 Abel 向量回到中心值的点，必须在这个
标量零集中。若进一步输入 R682 的归一 $t_i$、平方差和高度外积，
仍保留 R616 的 $L'(g_{-1,+},1)L(g_{-1,-},1)\ne0$ 前提。
本条没有证明完整高度等于该 Abel 原函数，也没有从有限零数推出
所有有理候选已被排除。

## 7. 真正例外 $p=137147$ 的原系数及残差最低次数

公开 R706 原 $z_{\rm ell}$ 算法证书固定为

`computations/R706-original-z-137147/43587480525-1/original-z-137147.json.gz`

其 gzip SHA 是
`54fcc49e58f9f53eaf459d2c59379578ed64281874dede30d097e69c115afc05`，
原生成源提交为 `fdb4c969bfd5f3e3a3e921875d1f10f34e52b5ba`。
其中 $N=(p-5)/6=22857$，完整原坐标数组满足

$$x=z_{\rm ell}^{-2}X(w),\quad
y=z_{\rm ell}^{-3}V_0(w)/2,\quad
\sigma(z_{\rm ell})^6=z_{\rm ell}^6Q(w),\quad w=z_{\rm ell}^6.$$

为避免与本条模曲线坐标 $V$ 混淆，此处将证书中名为 `V` 的
固定椭圆曲线数组写为 $V_0$。它满足

$$V_0=-2X+6wX',\qquad V_0^2=4X^3-4w.$$

小提取器只复用已返回的全部数组，并核其三个 SHA 和完整能量
方程；不重跑微分方程或素数窗口。令
$F=XQ$、$G=-XV_0Q/2$。取原两截面的 $N,N-1$ 次系数得到

| 固定 CM 权 $k$ | 原截面系数 | $A_k\bmod p$ | $C_k\bmod p$ |
|---:|---:|---:|---:|
| $p=137147$ | $[w^N]F=103259$ | 103259 | 80155 |
| $p-3=137144$ | $[w^N]G=0$ | 0 | 0 |
| $p-6=137141$ | $[w^{N-1}]F=36306$ | 110121 | 117309 |
| $p-9=137138$ | $[w^{N-1}]G=25244$ | 92058 | 122674 |

这里始终用 R697 的**普通阶乘**归一。若 $m=k-1\equiv4\pmod6$，

$$A_k=2^{-m/2}m![w^{(m-4)/6}]F,\qquad C_k=3A_k^2/m!;$$

若 $m\equiv1\pmod6$，

$$A_k=2^{-(m-1)/2}m![w^{(m-1)/6}]G,\qquad C_k=-A_k^2/(2m!).$$

因而没有把仅对最初两个权有效的 $C=-3A^2\pmod p$ 公式套到
$p-6,p-9$ 上。提取器还保存了两个末次卷积 summands 的 SHA。

R705 的实际索引对接是

| 实际 flat jet | 固定 CM 权对 |
|---|---|
| $M_2$ | $(p,p-3)$ |
| $M_5$ | $(p-3,p-6)$ |
| $M_8$ | $(p-6,p-9)$ |

于是前两对残差为零，第三对均为单位，给

$$v_p(M_2)\ge-\tfrac12,\qquad
v_p(M_5)\ge-\tfrac72,\qquad v_p(M_8)=-7.$$

本条 $b_j$ 因此满足

$$v_p(b_1)\ge\tfrac12,\qquad
v_p(b_2)\ge\tfrac12,\qquad v_p(b_3)=0.$$

**所以 $p=137147$ 的完整粗 Abel 残差多项式最低次数恰为三。**
实际特征零首阶只得到 $d\le3$；在 $v_p(a-1)>3$ 的开盘上，
原标量 Abel 原函数的零总重数为三，非零零点总重数至多二。
特别地，这涵盖 R317 的实际 $v_p(a-1)\ge4$ 候选范围，却并不
排除这些至多两个可能零点，更不对完整 QC 高度首项作结论。

### 提取器及公开复现

脚本 `R710_extract_next_original_Abel_pair.py` 的 SHA-256 为
`3911788be295069bb32a6b2adcc114296820e6adee227d6308d29914b9d5030c`。
它硬编码检查上述输入 gzip SHA，命令为

```text
python R710_extract_next_original_Abel_pair.py \
  --certificate /path/to/original-z-137147.json.gz \
  --output /path/to/R710-next-actual-Abel-pair-137147.json
```

公开提取已在
[Actions 43589720709](https://github.com/Rogerhu12/math-research-public/actions/runs/43589720709)
完成，源提交 `adfe2b74b2e7ff6e6d668ec28b97f02ca719a6fd`。
完整返回位于
`computations/R710-next-original-Abel-pair/43589720709-1/`。
数字证书 `R710-next-actual-Abel-pair-137147.json` 的 SHA-256 为
`6196cccfafd2c7f117d1f3e2ecabf02c584cb1a89b49215a0a8d462a6bdcd5f6`，
与开发阶段的相同提取字节一致。其 `public-actions-input.json` SHA 为
`5751afebe82af35c56634cf042934a2cb195f4c21f736a14de32d756907a81de`。
全素数第 1–6 节不依赖这次提取结果。
