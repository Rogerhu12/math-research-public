# R1160：原 Hecke 平滑的显式算术下降与实际未平滑 primitive

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；root。

**已证明实际连续一次上链的构造，支付 R1159 的未平滑接口。**
原 Frobenius 路径的数值读取仍须继续；本篇不把未计算的路径值
称作已知 $F_0$，也不由此宣布原局部单位或 Serre 主目标完成。

[R1159](R1159-original-correlation-to-Hecke-cochain-comparison.md)
已给原 source 的指定上链
$$
dh_{\mathcal V_n}=-\mathcal V_n\Omega,\qquad
\Omega=\Pi_0(a_4\cup a_8),\qquad
\mathcal V_n=(n^4+n^{-11})\mathrm{id}-n^2T_n,
$$
及其同一 cohomology 标量
$$
v_n=n^{-11}(n-1)(n^{14}-1).
$$
下面直接构造
$$
\boxed{\quad dB_n=(\mathcal V_n-v_n)\Omega. \quad}
\tag{1160.1}
$$
构造使用原有限 moment cocycles、实际 Hecke cochains、
Tate 切向基点、两个几何生成元、复共轭和固定的有限差分式。
没有另选一个未知的原 Heisenberg lift 来定义 $B_n$。

## 1. 同一个算术群与实际系数

记
$$
M=\operatorname{Sym}^{12}\mathcal H(2),\qquad p>37.
$$
原两个偶 moment 与 $M$ 上的 generic $\mu_2$ 稳定子均平凡作用。
实际一次 cocycle 在该阶二元素上的值必为零，因为 $2$ 为单位。
所以原杯积及其 Hecke transfer 可先在 rigidification 上书写，
随后拉回原 $\mathcal M_{1,1,\mathbb Q}$；没有删掉 level-$p$ 稳定子。

使用 R1144 的同一 Tate $q$-根和正实切向基点。
算术 fundamental group 有实际 splitting
$$
G=N\rtimes Q,\qquad Q=G_{\mathbb Q},\qquad
N=\widehat{C_2*C_3}.
\tag{1160.2}
$$
$Q$ 的 splitting 由 Tate curve over $\mathbb Q((q))$，
以及固定全部兼容 $q^{1/m}$ 后的 coefficient action 给出。
因此 $q\in Q$ 始终表示这个已指定的群元素，而非任意选择的 lift。

R1144 §4 的复解析/étale 比较给 (1160.2) 的几何群：
rigidified modular orbifold 的实际几何群是
$\operatorname{PSL}_2(\mathbb Z)=C_2*C_3$；
其 profinite completion 满足有限阶两因子的连续自由积泛性质。
写生成元为 $S,U$，$S^2=U^3=1$。
取原 cusp generator $T$，并令
$U=ST^{-1}$、$T'=ST^{-1}S^{-1}$。
在原 Tate 基 $X=e_1,Y=e_2$ 上，
$$
T:X\mapsto X+Y,\ Y\mapsto Y,\qquad
T':X\mapsto X,\ Y\mapsto Y+X .
\tag{1160.3}
$$
$T'$ 的取向由此式固定。Tate factor 在 $N$ 上平凡。

保原 positive-real 切向路径，复共轭 $c\in Q$ 的确切动作是
$$
cSc^{-1}=S,\qquad
cUc^{-1}=SU^{-1}S,\qquad
cTc^{-1}=T^{-1},\qquad cT'c^{-1}=T'^{-1}.
\tag{1160.4}
$$
可以在上半平面直接核准：$\tau\mapsto-\bar\tau$ 对 modular
matrices 的动作是以 $\operatorname{diag}(-1,1)$ 共轭，
在 projective group 中固定 $S$，把正 cusp generator 反向。
代入 $U=ST^{-1}$ 得第二式。
所以本篇在复共轭处不调用一个未知的 Galois associator。

原 R1144–1147 已付
$$
M^N=0,\qquad
r:H^1(N,M)\xrightarrow{\sim}L_1.
\tag{1160.5}
$$
$r$ 是同一 Tate residue，具体在几何一次 cocycle 上读取
$u(T)$ 的 $X^{12}$ coinvariant 系数，同时保惯性的 $(-1)$ twist。
特别 $Q$ 在右边的动作是 $\chi_{\rm cyc}$，复共轭为 $-1$。

令 $a_{12}$ 为原 $\mathsf M_{12}$ 的实际同根一次 cocycle，
其 residue 是 $1/12$。给出一个具体线性截面
$$
i:L_1\longrightarrow Z^1(N,M),\qquad
i(\lambda)=12\,a_{12}|_N\otimes\lambda,\qquad r(i(\lambda))=\lambda.
\tag{1160.6}
$$
这里用的是原 moment，未另选抽象 Eisenstein generator；
不要求这个一次代表的截面 $i$ 在 cochain 层严格 $Q$-等变。

## 2. 任一给定二次 cocycle 的指定几何 primitive

先令 $\zeta\in Z^2(G,M)$ 为一个**已给定的 normalized**
连续二次 cocycle。构造实际 profinite group
$$
E_\zeta=M\times G,\qquad
(m,g)(n,h)=(m+g n+\zeta(g,h),gh).
\tag{1160.7}
$$
它的结合律恰是 $d\zeta=0$。

在 $N$ 的两个有限因子上，取完全指定的 lifts：
$$
\boxed{\begin{aligned}
s(S)&=\left(-\frac{\zeta(S,S)}2,S\right),\\
s(U)&=\left(-\frac{\zeta(U,U)+\zeta(U^2,U)}3,U\right).
\end{aligned}}
\tag{1160.8}
$$
若 $R$ 的阶为 $m=2$ 或 $3$，
$(0,R)^m=(z_R,1)$，其中
$z_R=\sum_{j=1}^{m-1}\zeta(R^j,R)$。
这个元素与 $(0,R)$ 交换，故 $Rz_R=z_R$。
于是 $(-z_R/m,R)^m=1$，严格证明 (1160.8) 的有限阶，
并非只在 abelian quotient 上猜一个平均值。

连续自由积的泛性质给唯一连续 group section
$$
s:N\longrightarrow E_\zeta|_N,\qquad s(n)=(b(n),n)
$$
延长这两个指定 lifts。其函数部分满足
$$
\boxed{\qquad
b(nm)=b(n)+n b(m)+\zeta(n,m),\qquad
d_Nb=-\zeta|_N.
\qquad}
\tag{1160.9}
$$
在有限 $S,U$ 字上，(1160.8)–(1160.9) 逐步直接计算 $b$；
在 profinite completion 上取上述唯一连续延拓。
这里不是先使用几何 $H^2=0$ 再任取 primitive。
反过来，这个构造本身也直接证明本系数上的几何 $H^2=0$。

## 3. 全部算术共轭缺陷与一个可计算的修正

对 $q\in Q$，令 $e(q)=(0,q)\in E_\zeta$。
写 $q^{-1}nq$ 为 (1160.2) 中的实际共轭。
定义
$$
e(q)s(q^{-1}nq)e(q)^{-1}
 =\bigl(u_q(n),1\bigr)s(n).
\tag{1160.10}
$$
这是两个真实 geometric sections 之差，
所以 $u_q\in Z^1(N,M)$。全部输入也可展开成
$$
\boxed{\begin{aligned}
u_q(n)={}&q\,b(q^{-1}nq)
 +\zeta(q,q^{-1}nq)
 -n\,\zeta(q,q^{-1})\\
 &+\zeta(nq,q^{-1})-b(n).
\end{aligned}}
\tag{1160.11}
$$
其中 $-\!n\zeta(q,q^{-1})$ 来自 $(0,q)^{-1}$；
不能因 $q=c$ 的阶为二就删掉 $\zeta(c,c)$。

因 $e(q)e(r)=(\zeta(q,r),1)e(qr)$，
内共轭 $(m,1)$ 对 geometric section 的差是 $-d_Nm$，
故
$$
u_q+q\cdot u_r-u_{qr}=-d_N\zeta(q,r).
\tag{1160.12}
$$
这里 $(q\cdot u_r)(n)=q\,u_r(q^{-1}nq)$。
因此
$$
\beta(q):=r(u_q)\in L_1
\tag{1160.13}
$$
是实际连续 $Q$-一次 cocycle。
它是该 extension 的 Hochschild–Serre 边缘缺陷；
尤其若 $[\zeta]=0$，则 $[\beta]=0$。
也可不使用 edge 的符号约定来核最后一点：
一个全局 group section 与 $s$ 的几何差给一个 $N$-cocycle，
其 $Q$-共轭差在 cohomology 中恰是 $\beta$ 的 coboundary。

现在仅对满足 $[\zeta]=0$ 的**这个给定** $\zeta$ 继续。
因为 $L_1^Q=0$，使 $\beta=d_Q\lambda$ 的 $\lambda$ 唯一，
而在复共轭处它有明确值
$$
\boxed{\qquad \lambda=-\frac{\beta(c)}2. \qquad}
\tag{1160.14}
$$
确实 $d_Q\lambda(c)=(c-1)\lambda=-2\lambda$。
抽象零类只用于验证这一实际值满足全部 $q$ 的等式；
本构造没有把一个未知的 $\lambda$ 当作新输入。
(1160.4)、(1160.8)、(1160.11) 使 $\beta(c)$
只需原 cocycle 在固定短字及复共轭上的值。

置
$$
t=-i(\lambda),\qquad
s'(n)=(t(n),1)s(n).
$$
$t$ 是真正的 $N$-一次 cocycle，故 $s'$ 仍为 group section。
它的新共轭缺陷是
$$
u'_q=u_q+q\cdot t-t,\qquad
r(u'_q)=\beta(q)-d_Q\lambda(q)=0.
\tag{1160.15}
$$
由 (1160.5)，每个 $u'_q$ 都是 geometric coboundary。
下一节给其唯一零次原像的固定有限式，不把它留为一个待选量。

## 4. 两个原幺幂元素上的显式反差分

对任意 $u\in B^1(N,M)$，要解
$$
d_Nv(n)=nv-v=u(n).
$$
在 Tate 基中暂时平凡化一维 Tate 因子，置
$$
f(Z)=u(T)(Z,1).
$$
由 (1160.3)，$u(T)=(T-1)v$，所以 $\deg f\le11$。
令 $\Delta f(Z)=f(Z+1)-f(Z)$，并定义准确的次数十二齐次式
$$
v_*(X,Y)=
Y^{12}\sum_{r=0}^{11}\bigl(\Delta^r f\bigr)(0)
                  \binom{X/Y}{r+1}.
\tag{1160.16}
$$
这是真多项式；每一项分母只是 $(r+1)!$，均为 $p$ 单位。
有限 Newton 身份
$f(Z)=\sum_{r=0}^{11}(\Delta^r f)(0)\binom Zr$
及 $\Delta\binom Z{r+1}=\binom Zr$ 给
$$
(T-1)v_*=u(T),\qquad v_*(0,Y)=0.
$$
$T$-invariant 的十二次齐次式只有 $KY^{12}$：
有限差分逐个最高次数使用的整数 $1,\ldots,12$ 都可逆。
因而 $v-v_*=aY^{12}$。用第二个幺幂元素，
$$
u(T')-(T'-1)v_*
 =a\{(X+Y)^{12}-Y^{12}\}.
$$
读取 $X^{12}$ 系数便唯一确定 $a$。定义
$$
\boxed{\quad
\mathcal I(u)=v_*+
 [X^{12}]\{u(T')-(T'-1)v_*\}\,Y^{12}.
\quad}
\tag{1160.17}
$$
于是 $d_N\mathcal I(u)=u$，且它是唯一原像，因为 $M^N=0$。
这一公式只使用两个实际 group elements 上的值、至多十一阶
有限差分和 $1,\ldots,12$ 的单位分母。
没有对 $\operatorname{SL}_2(\mathbb F_p)$ 作含 $1/p$ 的平均。

对 (1160.15)，现在**定义**
$$
v_q=\mathcal I(u'_q).
\tag{1160.18}
$$
这是已指定原数据的有限表达式。
恢复 Tate 因子后所有式子仍在原 $M$ 中；
没有把其算术权丢掉。

## 5. 算术 lifts 自动满足完整群律

令
$$
e'(q)=(v_q,1)e(q)=(v_q,q).
$$
$(v_q,1)$ 的内共轭从 (1160.10) 的缺陷中减去
$d_Nv_q=u'_q$，故
$$
e'(q)s'(n)e'(q)^{-1}=s'(q n q^{-1}).
\tag{1160.19}
$$
现在两个 lifts 的乘法差
$e'(q)e'(r)e'(qr)^{-1}$ 属于 $M$，且由 (1160.19)
与全部 $s'(N)$ 交换。所以它属于 $M^N=0$，
必须准确为一。特别
$$
v_q+qv_r-v_{qr}+\zeta(q,r)=0.
\tag{1160.20}
$$
没有留下另一个需要求解的 $Q$-二次中心 cocycle。

对于唯一分解 $g=nq$，全局 group section 是
$$
s_G(nq)=s'(n)e'(q).
$$
其实际中央坐标为
$b(n)+t(n)+n v_q+\zeta(n,q)$。
所以定义
$$
\boxed{\qquad
\mathcal B(\zeta)(nq)
=-b(n)-t(n)-n v_q-\zeta(n,q).
\qquad}
\tag{1160.21}
$$
完整群律直接给
$$
\boxed{\qquad d\,\mathcal B(\zeta)=\zeta. \qquad}
\tag{1160.22}
$$

所有构造连续：$M$ 有限，$\zeta$ 连续，
几何 section 使用 profinite 自由积的连续泛性质，
$q\mapsto u'_q(T),u'_q(T')$ 连续，
(1160.16)–(1160.18) 仅作固定有限线性运算。
因此 (1160.21) 是真正的连续上链，不是只对离散 $S,U$ 字定义的函数。
在同一组原 choice 下，构造对 $\zeta$ 线性；
例如几何部分的线性可用两个 extensions 的纤维积及中心相加，
再由 (1160.8) 的唯一延拓核准。

## 6. 原 Hecke 平滑确实可以在此上链层解开

现在取唯一指定的输入
$$
\zeta_n=(\mathcal V_n-v_n)\Omega .
$$
它是由原 $a_4,a_8$ 与 R1159 的实际 Hecke cochain
得到的 normalized 连续二次 cocycle。
R1159 (1159.17) 在完整绝对 $H^2$ 上给 $[\zeta_n]=0$，
所以以上构造全部适用。置
$$
\boxed{\qquad B_n=\mathcal B(\zeta_n). \qquad}
\tag{1160.23}
$$
这就支付了 (1160.1)，包含实际算术共轭修正，
而不只是在几何二项复形上写 $d^{-1}$。

当 $v_n$ 为单位时，原未平滑 primitive 是
$$
\boxed{\quad
h_0=\frac{h_{\mathcal V_n}+B_n}{v_n},\qquad
dh_0=-\Omega .
\quad}
\tag{1160.24}
$$
故 $(a_4,a_8,h_0)$ 是原最高
$\operatorname{Sym}^{12}\mathcal H(2)$
Heisenberg group 的实际 arithmetic cocycle。
其 quotient representatives 正是 R1158–1159 已支付根 gauge 后的
原两个 moment。全 $\mathcal M$ 的 $H^0(M)=H^1(M)=0$
随后给与 R1147 canonical lift 的唯一同构，
保持这个 quotient；没有在 smaller open 上使用唯一性。

这里可覆盖全部 $p>37$，无需保留一个新的大素数门：

- 若 $p\ne43,127$，取 R1157 §10 的 $n=2$，
  $v_2=3\cdot43\cdot127/2^{11}$ 为单位；
- 若 $p=43$ 或 $127$，取原已付的 $n=5$。
  分别有 $5^{14}=36\pmod{43}$、$5^{14}=19\pmod{127}$，
  所以 $v_5=5^{-11}\cdot4(5^{14}-1)$ 也为单位。
  两个小算式可由 $5^3=-4\pmod{43}$、
  $5^3=-2\pmod{127}$ 连乘直接核准。

这些是两个指定 scalar 的纸面核算，不是新数值扫描。

## 7. 完成的接口与仍需读取的实际路径

(1160.8)、(1160.11)、(1160.14)、(1160.17)、(1160.21)
给的是原数据上完整且明确的算术 descent 程序。
$\beta(c)$ 只用固定短字，$v_q$ 不再是任取的 solution，
因此 R1159 中未构造的 $B_n$ 现在确为实际一次上链。

仍须严格保留另一项工作：
对一般 Frobenius 元素 $q$，
(1160.11) 中的 $b(q^{-1}T'q)$
要在**这个原有限 Galois/Belyi quotient** 中读取。
Tate 方向 $q^{-1}Tq=T^{\chi(q)^{-1}}$ 已由原 splitting 固定；
第二条路径包含另一条实际 conjugating word。
本篇给了它的确切位置和计算规则，
没有声称已经取得它的数值或 crystalline realization。
用这个未知值重新命名原 $F_0$，不能完成后继局部问题。

同样，本篇没有构造四线各项在 supersingular 退化时的
good-argument 分解，也没有排除 weighted Frobenius 值的抵消。
R1155 的单 primitive 单位仍须经完整原源读取后，
才能用于 R1151–1153 的真实中央减法和所有深盘。
完成上链下降不等于已完成那些读取，更不等于 full-$p$ 全局排除。


## 8. 全部 $p^r$ 层与原三个中心的同一显式构造

**已证明：** §§1–5 的算术构造同时适用于原三个中心，
而且在全部 $p^r$ 层严格与约化相容。
因此原四十二维群及其忠实四十三维格的 generic torsor
有一个直接由原 abelian moment cochains 给出的连续坐标；
不必先把原中央 lift 当作未知输入。

写 $R_r=\mathbb Z/p^r$，并令
$
M_{d,t,r}=\operatorname{Sym}^{d}\mathcal H_r(t),\qquad
(d,t)\in\{(12,2),(8,4),(4,6)\}.
\tag{1160.25}
$
本节的 $r$ 是系数层数，不是 Hecke 素数。
原 [R1147 §§9–11](R1147-original-canonical-moment-Heisenberg-lift.md)
已经从 primitive torsion 与同一 norm 的完整根相位给出
兼容的 abelian torsor tower。固定该 tower 的兼容几何纤维点，
得到实际兼容的一次 cocycles
$a_{4,r},a_{8,r},a_{12,r},\gamma_{5,r}$。
这里的选择只发生在已经构造的 abelian torsors：
有限非空纤维的过渡满射保证兼容点存在，
没有在未构造的中央 torsor 中挑点来循环定义答案。

### 8.1. 整 residue 与真正的三种截面

R1147 (1147.36) 的单位 minor 计算给出整层结论
$
M_{d,t,r}^{N}=0,\qquad
\operatorname{res}_{d,t,r}:H^1(N,M_{d,t,r})
 \xrightarrow{\sim}R_r(t-1).
\tag{1160.26}
$
它是原 Tate residue 的完整 $Q$-等变同构，
不仅是模 $p$ 维数相同。
原 $a_{d,r}$ 的 residue 是以下同一个 $\mathbb Z_p$ 单位的约化：
$
v_{4,\infty}=\frac{1-p^4}{252},\qquad
v_{8,\infty}=\frac{1-p^8}{132},\qquad
v_{12,\infty}=\frac{1-p^{12}}{12}.
\tag{1160.27}
$
所以在三个中心上都能直接指定
$
i_{d,t,r}(\lambda)
=v_{d,\infty}^{-1}\,a_{d,r}|_N\otimes\lambda,\qquad
\operatorname{res}_{d,t,r}i_{d,t,r}=\mathrm{id}.
\tag{1160.28}
$
这一整式在 $d=12,r=1$ 时正是 (1160.6)；
高层不能把它误写成恒定的 $12a_{12,r}$。
张量中的 $\lambda$ 属于 $R_r(t-1)$，
因此原 moment 的 twist $1$ 正确变为 twist $t$。

三个 residual characters 的指数为 $t-1=1,3,5$，
复共轭都严格作用为 $-1$。
对一个已给定、类为零的 normalized
$\zeta_r\in Z^2(G,M_{d,t,r})$，
仍用 (1160.8) 的 $1/2,1/3$ 有阶 lifts 构造 $b_r$，
再以原 residue 读取 $\beta_r$。
其算术修正仍是实际数值
$
\lambda_r=-\frac{\beta_r(c)}2,\qquad
t_r=-i_{d,t,r}(\lambda_r).
\tag{1160.29}
$
$R_r(t-1)^Q=0$ 保证该零次原像唯一；
零类假设验证它对全部 $q$ 成立，
不引入一个待选的算术 solution。

### 8.2. 整层有限反差分及约化相容

对 $u\in B^1(N,M_{d,t,r})$，令 $f(Z)=u(T)(Z,1)$，
其次数不超过 $d-1$。
把 (1160.16)–(1160.17) 原样改为
$
\begin{aligned}
v_{*,d}
 &=Y^d\sum_{j=0}^{d-1}(\Delta^j f)(0)
                   \binom{X/Y}{j+1},\\
\mathcal I_d(u)
 &=v_{*,d}+[X^d]\{u(T')-(T'-1)v_{*,d}\}\,Y^d.
\end{aligned}
\tag{1160.30}
$
完整 Newton 恒等式仍在 $R_r$ 上成立：
其分母仅为 $1!,\ldots,d!$，均在 $p>37$ 时可逆。
同样逐最高次数比较给 $T$-invariants 恰为 $R_rY^d$，
而 $T'$ 的 $X^d$ 系数固定剩下的常数。
因此 $d_N\mathcal I_d(u)=u$，没有使用域上的除法，
也没有使用含 $1/p$ 的群平均。

将 $\mathcal I_d$、(1160.28) 代入 §§3–5，
得到完全指定的线性构造
$
\mathcal B_{d,t,r}:
 \{\zeta_r\in Z^2(G,M_{d,t,r}):[\zeta_r]=0\}
 \longrightarrow C^1(G,M_{d,t,r}),\qquad
d\mathcal B_{d,t,r}(\zeta_r)=\zeta_r.
\tag{1160.31}
$
连续性仍由有限系数、几何自由积及固定有限线性运算给出。

若 $\zeta_{r+1}$ 约化为 $\zeta_r$，
两个 finite-factor lifts 的约化相同；
连续自由积的唯一性迫使整个 $b_{r+1}$ 约化为 $b_r$。
实际共轭、residue、(1160.27) 的固定单位逆、
复共轭修正与 (1160.30) 均与约化交换。
逐个代入全 section 公式 (1160.21)，得到
$
\mathcal B_{d,t,r+1}(\zeta_{r+1})\bmod p^r
   =\mathcal B_{d,t,r}(\zeta_r).
\tag{1160.32}
$
这是实际 cochains 的等式，强于只说相应 cohomology classes 兼容。

### 8.3. 原修正杯积直接给完整中央坐标

在每层保留原三个有序 bilinear 槽：
$
\begin{aligned}
\Omega_{0,r}&=\Pi_0(a_{4,r}\cup a_{8,r}),\\
\Omega_{2,r}&=\Pi_2(a_{4,r}\cup a_{8,r}),\\
\Omega_{4,r}&=\Pi_4(a_{4,r}\cup a_{8,r})
 +\frac{21(1+p^4)}{11}\,a_{4,r}\cup\gamma_{5,r}.
\end{aligned}
\tag{1160.33}
$
最后的 cup 使用 R1147 (1147.39) 同一
$\operatorname{Sym}^4\mathcal H_r(1)\otimes R_r(5)$ 槽。
R1147 (1147.38) 已在完整算术 cohomology 中证明三个类皆零；
本节不以几何 residue 零代替这个输入，
也不删高层的因子 $1+p^4$。

因而直接定义原中心的实际一次 cochain
$
\boxed{
h_r=-\bigl(
 \mathcal B_{12,2,r}(\Omega_{0,r}),
 \mathcal B_{8,4,r}(\Omega_{2,r}),
 \mathcal B_{4,6,r}(\Omega_{4,r})\bigr).}
\tag{1160.34}
$
则 $dh_r=-(\Omega_{0,r},\Omega_{2,r},\Omega_{4,r})$，
所以 $(a_{4,r},a_{8,r},\gamma_{5,r},h_r)$
满足原四十二维 class-two group 的完整 cocycle law。
(1160.32) 使这些 cocycles 逐层严格兼容；
取逆极限即得到连续 $\mathbb Z_p$ 上链及原秩二十七中心，
不是分别挑选的 finite-level lifts。

该 generic tower 与 R1147 的原 canonical tower
具有同一个已固定 abelian quotient。
原 universal 的 $H^0(\mathcal Z_r)=H^1(\mathcal Z_r)=0$
给逐层唯一的 quotient-preserving 同构，
其唯一性又迫使同构沿所有约化相容。
因此它识别到同一个 $S_0$ 上的整 torsor tower，
以及 R1147 的忠实秩四十三格。
这一步只使用已经支付的完整整模型唯一性，
没有在删去点的 smaller open 或单个局部域上冒用唯一性。
原 Cartan pushout 仍先约化至 $p$；
本节没有把 level-$p$ 的 $I$ 擅自提升为 $T_pE$ 的算子。

(1160.34) 的最高分量也与 §6 的
$(h_{\mathcal V_n}+B_n)/v_n$ 在同一 quotient 下唯一同构。
前者使三个中心和整塔的上链构造直接明确，
后者保留实际四线 source 与 Hecke 比较的几何输入；
两者都不能替代 §7 尚待读取的一般 Frobenius 共轭路径。
本节没有由显式算术程序推断原 $F_0$ 的数值、
weighted 局部单位或 full-$p$ 排除。

## 来源与核验

- R1144 §§3–4：同一 Tate frame、actual residue、
  $C_2*C_3$ 几何比较和完整绝对 Hochschild–Serre 同构。
- R1147：原 $a_{12}$、residue $1/12$、
  universal 的 $H^0/H^1$ 消失和 canonical quotient。
- R1158–1159：真实 correlation group、原 root gauge、
  全部 crossed transfer、$h_{\mathcal V_n}$ 及同一 $v_n$。
- 几何有限阶 lifts、(1160.11) 的全符号、复共轭修正、
  两幺幂反差分和完整 arithmetic section 由 root 逐式纸推。
  global_route 独核扩张群号、内共轭的负 coboundary、
  $B_n$ 的最终加号接口及复共轭的短字动作。
  无数学程序执行。
