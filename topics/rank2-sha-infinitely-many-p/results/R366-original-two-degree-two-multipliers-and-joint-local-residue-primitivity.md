# R366：两个原次数二乘子的共同提升核与联合局部扭留数

日期：2026-11-13。**状态：已证明。** 两个真实归一化乘子作用在整个原 canonical 来源上，其完整乘法图保持所有提升核、第一 Bockstein 和正确第二余核。另在 R356 指定的正规局部连接中，两乘子的全部角因子给一个共同 forcing 向量的原始联合留数矩阵。后者由一个固定整数 Bézout 恒等式证明，对除有限集外的全部允许素数成立。将这个局部单位模型用于原有限 theta 代表，还必须保留该代表的真实零阶；本篇没有提前把两者等同。

## 1. 同一个整个来源上的两个真乘子

采用 R335 的原规范
$$
h_7=16t^2+4t+7,\qquad
\rho=\Theta^{17}(1+8t),\qquad \Theta=x\sigma^2,\quad t=-b/x^3,\quad b=17.
$$
相对径向变量记为 $\mathscr R$，在物理评价时准确取 $\rho$。
原次数 $n$ 的整格是
$$
\mathcal V_n=\mathscr R^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
q_n=\frac{(th_7)^{\alpha_n}(t-1)^{\beta_n}}{(1+8t)^{\gamma_n}},
$$
$$
\alpha_n=\lfloor(n+1)/4\rfloor,\quad
\beta_n=\lfloor(n+1)/3\rfloor,\quad
\gamma_n=\lfloor n/2\rfloor,\qquad
\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4.
\tag{1}
$$
这里固定公共导子和 charge40 按原规范保留。

取
$$
\boxed{
Q_0=\mathscr R^2\frac{t(t-1)h_7}{1+8t},
\qquad Q_1=tQ_0.
}
\tag{2}
$$
它们都是 R335 的 $\mathcal N_2$ 中的真实元素：基本分式就是
$\mathscr R^2t(t-1)h_7/(1+8t)$，其允许多项式次数为六，
而 (2) 使用零次和一次多项式。

这还可以对整个来源直接逐 floor 检验。写
$\Delta\alpha=\alpha_{n+2}-\alpha_n$、
$\Delta\beta=\beta_{n+2}-\beta_n$，则两者都在 $\{0,1\}$，
且 $\gamma_{n+2}-\gamma_n=1$。所以
$$
\frac{t(t-1)h_7q_n}{(1+8t)q_{n+2}}
=(th_7)^{1-\Delta\alpha}(t-1)^{1-\Delta\beta}
\in\mathcal O[t].
\tag{3}
$$
乘以 $t^i$，$i=0,1$，仍为整多项式。
(2) 的有理角次数为 $3+i\le4$，而 (1) 的总次数上界从 $n$ 到
$n+2$ 增加九。因此
$$
\boxed{Q_i\mathcal V_n\subset\mathcal V_{n+2}\quad(n\ge0,\ i=0,1).}
\tag{4}
$$
此证明确实包含所有余数类、所有最高列及全部固定零极。

两者的物理式为
$$
Q_{i,\mathrm{phys}}=\Theta^{34}F_i(t),\qquad
F_0=t(t-1)(1+8t)h_7,\quad F_1=tF_0.
\tag{5}
$$
在原点 $w=z^6$，
$$
Q_{0,\mathrm{phys}}=7bw+\cdots,\qquad
Q_{1,\mathrm{phys}}=-7b^2w^2+\cdots.
\tag{6}
$$
除 $p\mid7b$ 外，显示首系数为单位。这里没有把两个物理乘子当成原点单位。

## 2. 完整截断乘法图与全部 Bockstein 自然性

取原惰性窗口
$$
p=6s-1,\qquad s>16,\qquad 1\le\ell<s-15,\qquad
T=2s+\ell+13.
\tag{7}
$$
因此 $T+2<3s$，下述三个目标都在同一已付三块中。
令 $M_{D,T}$ 为 R338/R351 的整个原矩阵 $m_{13}J$。
其目标 $\Gamma_T$ 使用完整基
$e_r=w^r/p^{\lfloor r/s\rfloor}$，$0\le r<T$，
并保留 $w^s=p\epsilon$ 的真实乘法。

由于 (6) 的最低阶至少为一，
$$
\mu_i:\Gamma_T\longrightarrow\Gamma_{T+1},\qquad
f\longmapsto [Q_{i,\mathrm{phys}}f]_{<T+1}
\tag{8}
$$
良定且整。未知的 $w^T$ 及更高系数只可能到 $w^{T+1}$ 及更高，
不会进入目标。完整除幂乘法的结构系数是
$p^{\lfloor(a+b)/s\rfloor-\lfloor a/s\rfloor-\lfloor b/s\rfloor}$，
其指数非负；(8) 保留乘子本身的全部 Gaussian 块。

由同一物理评价及 (4)，准确有
$$
\boxed{
M_{D+2,T+1}(Q_iP)=\mu_iM_{D,T}(P).
}
\tag{9}
$$
原十三行、公共规范、两条 $p$ 边界和新末行都在式内。
特别是 $\mu_1$ 在这个共同短目标中可能丢掉最后一个输入方向；
本篇并不宣称它单独可逆或单独原始。
$\mu_0$ 的 $w$ 行移也仍有跨过 $s,2s$ 的原 $p$ 成本。

对任意整矩阵 $M$，置
$$
K_r(M)=\{P:M(P)\in p^r\Gamma\}.
$$
(9) 直接给
$$
Q_iK_r(M_{D,T})\subset K_r(M_{D+2,T+1})\qquad(r\ge1).
\tag{10}
$$
若 $\bar P\in\ker\bar M$，第一 Bockstein 是
$M(P)/p$ 在 $\operatorname{coker}\bar M$ 中的类。
将 (9) 除以 $p$ 即得
$$
\beta'_1(Q_i\bar P)=\bar\mu_i\beta_1(\bar P).
\tag{11}
$$
因此 $\bar\mu_i$ 还下降到正确的
$$
C_2(M)=\operatorname{coker}\bar M/\beta_1(\ker\bar M).
$$
对真正 $P_2\in K_2(M)$，将 (9) 除以 $p^2$，
得到第二提升类的同一自然性。换提升造成的第一 Bockstein 项
仍由 (11) 落入被商去的正确子空间。这证明两乘子在整个
$K_r/\beta_1/d_2$ 系统上的相容性。

对偶地，若 $\lambda_rM_{D+2,T+1}=0\bmod p^r$，
则
$$
(\lambda_r\mu_i)M_{D,T}=0\bmod p^r.
\tag{12}
$$
所以拉回的是一个真正可提升的整左核，并非任意抽取的系数行。
也可以使用
$(D,T)\to(D+2,T+1)\to(D+4,T+2)$ 的共同梯子，
使两个乘子的拉回都来自同一个较大的可提升左核。

## 3. 同一个原核元素与总 Euler

记 $\mathcal E=\mathscr R\partial_{\mathscr R}$。
两乘子均为次数二，故整个混合次数 $P$ 都满足
$$
\boxed{
(\mathcal E+40)(PQ_i)=Q_i(\mathcal E+42)P.
}
\tag{13}
$$
这里右边的 $P$ 对 $i=0,1$ 完全相同。
因此 R363/R365 的原总 charge 连接可以在 (9)、(12) 的同一梯子上
施用，得到同一原 $P$ 与真正拉回左核的配对。
不需要、也没有断言 $\mathcal E$ 或 $\mathcal E+40$ 保持 $K_2$。
(13) 不允许将混合次数的 $P$ 拆成逐次数的核元素。

以下局部线性定理用一个共同向量 $\boldsymbol q$。
当它来自 R342 的配对时，必须继续使用该文的
$\boldsymbol q(\lambda,P)$ 与全部两接触尾。
(9)–(13) 支付的是原来源和提升核之间的运输；
它们本身还没有把该配对变成以下每个测试极的零条件。

## 4. 两个完整角权的局部留数

沿 R356/R361，在覆盖 $y^2=v^6+b$ 上取
$x=v^2$、$Dv=y/v$、$Dy=3v^4$。
实际非原点测试极满足 $Z_p=0$、$DZ_p=1$，
且 $v,y$ 为单位。用同一原规范
$$
G_\kappa=-\sum_{j=1}^{p-1}
 \frac{D^{j-1}x(P)}{j!}Z_p^j\bmod Z_p^p,\qquad
h_{68,P}=\exp\left(68\int_0^{Z_p}G_\kappa\,dZ_p\right).
\tag{14}
$$
这里只取小于 $p$ 的阶数，所有所需分母都是单位。

令
$$
\omega_{\boldsymbol q}
=\sum_{n=1}^{K}q_nZ_p^{-6n}\,d\log r,\qquad
d\log r=-6v\,dz,\qquad 1\le K\le s-2,
$$
$$
\mathcal H_{i,P}
=h_{68,P}
 \left(\frac{v(P+Z_p)}{v(P)}\right)^{68}
 F_i(t(P+Z_p)),\quad i=0,1.
\tag{15}
$$
这里没有除以 $F_i(t(P))$；所有真实角零都保留。
两权采用同一向量 $\boldsymbol q$ 和同一局部连接。

写 $e_0=1,e_1=2$，
$F_i=\sum_{d=e_i}^{e_i+4}c_{i,d}t^d$。
两者最低系数都是 $-7$。
R361 的普遍递推给
$$
A_n^{m,A}(\xi)=
\frac{v^{-A}}{(6n-1)!\,y v^{6n-3}}
 \left.(D-x\partial_g+mg)^{6n-1}v^{A+1}\right|_{g=0},
\qquad \xi=b/v^6,
$$
$$
\deg A_n^{m,A}\le3n-1,\qquad
A_n^{m,A}(0)=[u^{6n-1}](1-u)^{m-A-1}e^{mu}.
\tag{16}
$$
这些是原导数及局部权的恒等式，适用于显示的任意整数 $A$。

定义
$$
\widehat A_{i,n}(\xi)=
 \sum_{d=e_i}^{e_i+4}c_{i,d}(-1)^d
 \xi^{d-e_i}A_n^{68,68-6d}(\xi).
$$
则两个完整留数分别为
$$
\boxed{
\operatorname{Res}_P(\mathcal H_{i,P}\omega_{\boldsymbol q})
=-6(Y/b)\xi^{e_i-K}P_{i,\boldsymbol q}(\xi),
}
$$
$$
P_{i,\boldsymbol q}
=\sum_{n=1}^{K}q_nb^n\xi^{K-n}\widehat A_{i,n}(\xi),
\qquad
\deg P_{i,\boldsymbol q}\le3K+3.
\tag{17}
$$
其中 $Y/b=y/v^3$ 是同一个椭圆商坐标。

## 5. 固定 Charlier 多项式与完整 Bézout 证书

为避免把有理系数的单位条件隐藏在记号中，定义整数多项式
$$
P_r(N)=68^r\sum_{j=0}^{r}
 (-1)^j\binom rj\frac{(N)_j}{68^j}.
\tag{18}
$$
它满足
$$
P_0=1,\quad P_1=68-N,\qquad
P_{r+1}=(68+r-N)P_r-68rP_{r-1}.
\tag{19}
$$
令 $N=6n-1$。由 (16)，两个最低对角准确为
$$
\widehat A_{0,n}(0)
=7\,\frac{68^{N-5}}{N!}P_5(N),\qquad
\widehat A_{1,n}(0)
=-7\,\frac{68^{N-11}}{N!}P_{11}(N).
\tag{20}
$$
负的显示指数也无问题，因为 $68$ 是单位。

以下固定恒等式在 $\mathbf Z[N]$ 中成立：
$$
\boxed{U(N)P_5(N)+V(N)P_{11}(N)=C,}
$$
$$
\boxed{C=57898118088659915362886263937901527040\ne0.}
\tag{21}
$$
为完整给出可逐系数检查的证明，下面所有数组均按 $N$ 的次数
从零次向上排列；没有省略中间零项或依赖任何目标素数计算。

```text
P5 = [1453933568, -110145744, 3286830, -48315, 350, -1]

P11 = [
  143746751770690322432,
  -25128299125929231616,
  1962971811893150432,
  -90505446934949816,
  2738004949542940,
  -57094912473038,
  837797842035,
  -8654615013,
  61705710,
  -289300,
  803,
  -1
]

U = [
  72481798322203529923681046985187211520,
  -11502810853413039056123710243243036384,
  804300560683587649508117438895826552,
  -32651930132562937473107831542877340,
  852887020985620225381628743709150,
  -14988288513162240742534504932451,
  179598313397055640038302844861,
  -1449995207939593618688897870,
  7554162979292297085413300,
  -22948575824487295830355,
  30890608812371990457
]

V = [
  -733120702162865882540879760,
  43728349002672218202947326,
  -951021737129710830630203,
  8955130032482784153334,
  -30890608812371990457
]
```

(19) 直接产生上面的 $P_5,P_{11}$。
将这些整数数组作卷积相乘，常数项为 $C$，
所有正次系数为零，便逐项证明 (21)。
同目录的有限 BigInt 证书完整实现这两步，不使用浮点数。
特别是对任意 $p\nmid C$，$P_5$ 与 $P_{11}$ 在
$\overline{\mathbf F}_p$ 没有共同零点。
这里排除的是一个明确固定整数的素因子，当然只有有限个；
无需将其剩余大因子进一步分解。

## 6. 联合矩阵的原始单射

**定理。** 在 (7)、(15) 的原测试格中，假设
$$
p>83,\qquad p\nmid bC.
\tag{22}
$$
则
$$
\boldsymbol q\longmapsto
 \bigl(\{\operatorname{Res}_P(\mathcal H_{0,P}\omega_{\boldsymbol q})\}_P,
       \{\operatorname{Res}_P(\mathcal H_{1,P}\omega_{\boldsymbol q})\}_P\bigr)
\tag{23}
$$
有一个 $K$ 阶单位子式。因此它是原始整单射；
其像上的逆可以取整，不损失任何 $p$ 精度。

**证明。** 原测试代数是
$\mathcal A=\mathcal O[\xi]/(\widetilde B_p)$，
其中 $\deg B_p=3s-1$、$B_p(0)B_p(-1)\ne0$，
并且 $B_p$ 模 $p$ 平方自由。按 R346 的有限 étale 覆盖及
迹除以二、六，(17) 中每个非零公因子均是整行单位。
因
$$
3K+3\le3s-3<3s-1,
$$
两个多项式 (17) 都没有模 $B_p$ 回绕到低行的现象。
在各块中取系数行 $K-n$，并将 forcing 列按 $n$ 倒序排列，
得到三角形，其两个候选对角分别是
$b^n\widehat A_{i,n}(0)$。

由 (21)、(22)，对于每个 $n$ 至少有一个
$P_5(6n-1),P_{11}(6n-1)$ 是单位。
其余因子 $7,b,68,N!$ 都是单位，故可选择一个块 $i(n)$，
使其对应对角为单位。在联合矩阵中，为每个 $n$ 取
第 $i(n)$ 块的第 $K-n$ 行；这些行彼此不同。
所得到的 $K\times K$ 子矩阵仍三角，全部对角为单位。
其行列式的乘积给所需单位子式。整行消元因而给左逆，
证明原始性。$\square$

原 R342 的完整接触长度 $K=s-14$ 满足本定理的范围。
所以在这个共同的局部单位模型中，不需要从 $K$ 列删掉
单一 Charlier 多项式可能为零的那些方向。
这是两个真来源的共同观察；没有给两个观察分配两个任意 forcing。

## 7. 原有限 theta 代表的适用边界

(23) 使用的是正规单位局部权 $h_{68,P}$ 与全部角因子。
原有限 theta 代表在这些测试点可能另有固定零阶。
特别是从原点的有限有理 primitive 构造出来的
$(Z_p^2x)^{34}$ 因子带有 $Z_p^{68}$；
在该代表中，$\omega_{\boldsymbol q}$ 的留数阶数相应变成
$6n-69$，而非 $6n-1$。
这会把 $n\le11$ 的方向完全消去。
不能用 (23) 的行单位变换删除这个非单位因子。

因此 (9)–(13) 和 (23) 的结论必须分别保留：
前者是整个原矩阵中实际 source、target、提升核和正确余核的相容性；
后者是已指定正规连接模型的联合局部原始性。
将两者变成原 $C_2$ 配对的全局零传播，还要支付实际有限
theta frame、原公共 $G_0/U_0$、$Z_p^{-78}$ 及所有移位留数。
R363 的二阶有理系数在测试点为零这一事实本身不支付这些项。
本篇没有增加一个原中央零，亦没有由此得出无穷素数上的 Sha 有限。

## 引用与证书

- [R335](R335-full-integral-canonical-conductor-and-exact-relative-source.md)：整个 canonical 整格及归一化乘子。
- [R338](R338-original-second-bockstein-and-fixed-miller-forcing-pairing.md)：原第二提升、两接触与正确余核；准确文件导航另见分段索引。
- [R346](R346-original-off-origin-residue-injection-and-full-cartier-polar-part.md)：原测试极代数及整留数坐标。
- [R351](R351-original-canonical-serre-adjoint-and-integral-second-lift-connection.md)：真实可提升整左核及完整 Serre 伴随。
- [R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)：同一 Gaussian 规范的短局部 jets。
- [R361](R361-full-canonical-theta-twisted-residues-and-linear-unit-block-loss.md)：普遍局部递推、完整角权及三角行。
- [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)、[R365](R365-whole-original-conductor-carrier-and-total-charge-connection.md)：实际二阶连接与总 charge 算子。
- 有限整数证书：[check-jzero-two-degree-two-multipliers-bezout.js](../scripts/check-jzero-two-degree-two-multipliers-bezout.js)。
