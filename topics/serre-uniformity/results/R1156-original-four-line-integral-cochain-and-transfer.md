# R1156：原四线整上链、根相位修正与有限 transfer

日期：2026-11-28（Asia/Taipei）  
会话：Astra-serre-24b8836b-20261126  
状态：完整纸证；无新数学执行。一般 $p$ 主目标仍为 OPEN。

## 1. 实际结论与两个不同的塔

固定 $p>37$。本文把
[原 aux-$c$ 笔记](../notes/2026-11-28-original-auxiliary-c-torsion-Manin-correlation.md)
(C.7) 的实际三项相关和，提升为同一批函数的连续
$\mathbf Z_p$ 值中央零上链。所用 primitive 是
[R1133 §11](R1133-original-primitive-unit-equations-and-Heisenberg-source.md)
已经比较到原 $D(\alpha)$ 根代数的 integral dilogarithm cochain。
证明保留乘法根关系的 $\mu_{p^\infty}$ 相位，并给出
$\operatorname{Cor}\operatorname{res}$ 与次数乘法之间的实际 cup
链同伦；不把逐陪集的乘积换成两个 norm 的乘积。

具体地，设 $k$ 是特征零域，原 $E[p]$ 标记定义于 $k$，
$3\le c<p$ 为奇数，$A,B,C\in E[p](k)$ 互异。取
$$
f_A(T)=h_c(T-A),\qquad f_B(T)=h_c(T-B),\qquad
f_C(T)=h_c(T-C),\qquad h_c=\psi_c^{-1}.
\tag{1156.1}
$$
三个实际主除子的支持两两不交。把每个闭支持点处的残数
两槽取成同根规范的 Kummer cocycle，再按完整 residue field
作 corestriction，得到二次上链 $\Omega_c$。本文构造
$$
\mathcal H_c\in C^1_{\rm cont}(G_k,\mathbf Z_p(2)),
\qquad d\mathcal H_c=-\Omega_c.
\tag{1156.2}
$$
其全部 $\bmod p^n$ 约化相容，给出以这些实际 Kummer 槽为
指定交换商的有限 class-two torsor。允许各个 torsor 不连通。

这里的 $p^\infty$ 是**固定函数的根塔**。
虽然同一个证明适用于固定任意 $N=p^r$ 的 $E[N]$ 配置，
它没有证明随 $N$ 改变的 elliptic moment norm-distribution。
尤其不能直接把 (1156.2) 认成
[R1147](R1147-original-canonical-moment-Heisenberg-lift.md)
的指定 $V_\infty,Z_\infty$ 原 moment 塔，或据此调用其 §16
补点并识别规范提升。这一后续比较仍须支付。

## 2. 同一根的两种中央坐标

全部上链采用左 $G$-模、非齐次微分。对
$a\in C^0(G,M)$，$da(g)=ga-a$；对一次上链，
$$
df(g,h)=g f(h)-f(gh)+f(g),\qquad
(a\smile b)(g,h)=a(g)\otimes g b(h).
\tag{1156.3}
$$
将 $\mathbf Z_p(1)^{\otimes2}$ 与 $\mathbf Z_p(2)$ 作原 Tate
识别；以下交换两个一次因子时都包含这个 tensor flip。

对 $u,1-u\in k^\times$，沿同一个
$\overrightarrow{01}\rightsquigarrow u$ 的 étale 路径取全部
兼容根。记实际 Kummer cocycle 为 $a_u,b_u$。
R1133 (1133.74)–(1133.83) 给出的原 ordered 中央上链
$h_u$ 是 $\mathbf Z_p(2)$ 值，并满足
$$
dh_u=-a_u\smile b_u.
$$
其 BCH 中央坐标
$$
t_u=h_u-\frac12a_ub_u=-\ell i_2(u),\qquad
dt_u=-\mathfrak s(a_u,b_u),\quad
\mathfrak s(a,b)=\frac12(a\smile b-b\smile a).
\tag{1156.4}
$$
式中的 $a_ub_u$ 是在同一个 $g$ 上的乘积，属于一次上链。
直接展开 cocycle 等式给
$$
d(ab)=-(a\smile b+b\smile a),
\tag{1156.5}
$$
所以 (1156.4) 不是将 graded 反对称性误当上链恒等式。
唯一分母是 $2$，在本文范围为单位。所有根先在同一
$p^\infty$ 路径中选定，之后才逐层约化；没有逐层独立选解。

### 2.1. 乘法恒等式留下的实际零次上链

有限列表中的同一个函数可以有不同的出现位置及根选择。
必须将这些位置分别记录。若一个实际乘法关系为
$$
\prod_i u_i^{n_i}=1,
$$
则对已选兼容根 $u_{i,n}^{p^n}=u_i$，
$$
r_n=\prod_i u_{i,n}^{n_i}\in\mu_{p^n},
\qquad r=(r_n)_n\in\mathbf Z_p(1).
$$
于是准确有
$$
\sum_i n_i a_{u_i}=dr.
\tag{1156.6}
$$
右边不必为零。它同时处理乘法分解、同一个函数的不同出现
位置、模型常数和不同路径导致的根相位。非 $p$ 次单位根可
取其唯一兼容 pro-$p$ 分根，Kummer cocycle 为零；特别
$-1$ 在本处不产生被隐藏的中央输入。

若系数在 $\mathbf Z_{(p)}$，先清除与 $p$ 互素的分母；
一个仅在 $k^\times\otimes\mathbf Z_{(p)}$ 中成立的乘法关系，
也可再乘一个 $p$ 单位，使它成为上述实际乘积等于 $1$ 的
关系。之后除回的是 $\mathbf Z_p$ 中的单位。

### 2.2. 有限 Bloch 边界的实际上链构造

定义本文的符号边界为
$$
\delta_B[u]=u\wedge(1-u).
\tag{1156.7}
$$
这是本文固定的顺序。对有限表达式
$B=\sum_\rho n_\rho[u_\rho]$，假设已给出准确的
$$
\delta_B B=\sum_j m_j f_j\wedge g_j
\quad\text{于 }\Lambda^2(k^\times\otimes\mathbf Z_{(p)}).
\tag{1156.8}
$$
所有 $u_\rho$ 都不同于 $0,1$。

先取以 $k^\times$ 的全部元素、连同输入中须区分的重复出现位置
为基的自由 $\mathbf Z_{(p)}$-模 $F_\infty$，使它满射到
$k^\times\otimes\mathbf Z_{(p)}$，关系核记为 $R_\infty$。
外积商的核由 $R_\infty\wedge F_\infty$ 生成，故 (1156.8)
具有只含有限个基向量及有限个关系的见证。取包含原输入和该
见证中全部函数的有限自由子模 $F$，并令
$R=F\cap R_\infty$。于是准确可写成有限的
$$
\sum_\rho n_\rho\,\widetilde u_\rho
 \wedge\widetilde{(1-u_\rho)}
-\sum_jm_j\widetilde f_j\wedge\widetilde g_j
=\sum_s r_s\wedge v_s,\qquad r_s\in R.
\tag{1156.9}
$$
这里没有假定有限生成乘法子群的外平方注入完整乘法群的外平方；
必要的有限扩大已纳入 $F$。应用时保留 (1156.9) 这一有限乘法关系证书；本稿的四线、弦线与
Weil reciprocity 逐步展开就提供这些关系，不要求先求出任意函数域
全部单位关系。对每个 $r_s$ 使用 (1156.6)，记其实际零次根相位为
$\rho_s$，并记 $a_{v_s}$ 为相应线性组合的 Kummer cocycle。
置
$$
L_s=\frac12\bigl(\rho_s\smile a_{v_s}
                     +a_{v_s}\smile\rho_s\bigr).
$$
Leibniz 公式逐项给
$$
dL_s=\mathfrak s(d\rho_s,a_{v_s}).
\tag{1156.10}
$$
因此一个明确的 BCH primitive 为
$$
T_B=\sum_\rho n_\rho t_{u_\rho}+\sum_sL_s,\qquad
dT_B=-\sum_jm_j\mathfrak s(a_{f_j},a_{g_j}).
\tag{1156.11}
$$
最后返回原 ordered 约定：
$$
H_B=T_B+\frac12\sum_jm_j a_{f_j}a_{g_j},
\qquad
dH_B=-\sum_jm_j a_{f_j}\smile a_{g_j}.
\tag{1156.12}
$$
所有项都是已给有限路径与根关系的连续 $\mathbf Z_p$ 上链，
所以 (1156.12) 确实定义同一个兼容整塔。

这个结论不声称任意两份 Bloch 表达式给出相同 primitive。
若改变表达式或路径，必须使用 R1133 的实际五项和
(1156.6) 追踪差；仅仅知道两个表达式具有相同 $\delta_B$
并不足以删除其中央一次 cocycle。

## 3. 四条实际直线的边界：直接固定符号

先设四条直线 $L_i=(l_i=0)$ 位于一般位置，任意两线的交点
均不在平面椭圆曲线 $E$ 上。令 $D_i=L_i\cap E$，保完整
交点重数，并假设这些点已在当前域上分裂。
对 $L_i$ 上其余三个交点，按下标递增排序，取
$r(\infty,0,1,t)=t$ 的 cross-ratio。定义有限表达式
$$
B(l_0,l_1,l_2,l_3)=
-\sum_{i=0}^3(-1)^i
 \sum_{P\in D_i}\operatorname{mult}_P(D_i)
 [\,r(L_i\cap L_j\ (j\ne i),P)\,].
\tag{1156.13}
$$
所有参数都不为 $0,1,\infty$。本节直接证明
$$
\delta_B B(l_0,l_1,l_2,l_3)
=\sum_{P\in E}
 \operatorname{res}_P
 \left(\frac{l_1}{l_0}\wedge\frac{l_2}{l_0}
                     \wedge\frac{l_3}{l_0}\right)
\tag{1156.14}
$$
于 $\Lambda^2 k^\times\otimes\mathbf Z_{(p)}$；
不依赖不同文献对 $\delta_B$ 或 tame 的相反约定。

先缩放直线使 $l_3=l_0+l_1+l_2$，写
$f=l_1/l_0,\ g=l_2/l_0,\ h=1+f+g$。
四条线上的参数与完整残数如下：

| 直线 | cross-ratio | 对 $\operatorname{res}(f\wedge g\wedge h)$ 的贡献 |
|---|---|---|
| $L_3$ | $-f$ | $f\wedge g$ |
| $L_2$ | $-f$ | $-f\wedge h$ |
| $L_1$ | $-g$ | $g\wedge h$ |
| $L_0$ | $-k,\ k=l_2/l_1$ | $-k\wedge(1+k)$ |

在 $L_0$ 的最后一行，用 $t=l_0/l_1$，
$f=t^{-1},g=kt^{-1},h=(1+t+k)t^{-1}$ 直接展开。
四行恰等于 (1156.13) 的四个带号边界。
出现的 $-1$ wedge 在反除 $2$ 后消失，因而在本处 $\mathbf Z_{(p)}$ 中消失。

缩放直线没有删除未知 base 常数。改变一个函数槽的常数，
其总残数差是
$\lambda\wedge\prod_P \partial_P\{f,g\}$；
Weil reciprocity 使此积仅差已消去的 $-1$ 因子。因此
(1156.14) 对原来未缩放的实际直线成立。
这些是可代入 (1156.6) 的实际乘法关系，而不是声称每个
单点残数都不受缩放影响。

此处的形式与 Goncharov 的四线 reciprocity 相同，但
(1156.13)–(1156.14) 已按本文 $\delta_B$ 顺序自行付符号；
不把该文有理 Euler-complex 的 $N^{-3}$ 或 $N^{-5}$
当成可在 $N=p$ 时约去的整因子。

## 4. 原三主除子确有可用的四线展开

本节支付一般位置和辅助域，避免先假设 Miller 弦线没有碰撞。

设 $f\in k(E)^\times$，其主除子已分裂，写成
$$
\operatorname{div}f=\sum_{i=1}^n[P_i]-\sum_{i=1}^n[Q_i],
\qquad \sum_iP_i=\sum_iQ_i\quad\text{于 }E(k).
$$
先约去相同的正、负支持点。选辅助点 $R$，置
$$
R_0=R,\qquad
R_i=R+\sum_{j\le i}(P_j-Q_j),\qquad R_n=R_0.
$$
两个实际弦 $\ell_{P_i,R_{i-1}}$、
$\ell_{Q_i,R_i}$ 的第三交点相同：
$-P_i-R_{i-1}=-Q_i-R_i$。所以
$$
f=\lambda\prod_{i=1}^n
 \frac{\ell_{P_i,R_{i-1}}}{\ell_{Q_i,R_i}}
\quad(\lambda\in k^\times).
\tag{1156.15}
$$
这由完整 divisor 与一个非零值比较给出；$\lambda$ 保留。

现在有三个互不交的主除子 $D_1,D_2,D_3$。逐槽选择
$R^{(1)},R^{(2)},R^{(3)}$：

- 第一槽所有弦在 $E$ 上的辅助交点避开另两槽的固定支持。
- 第二槽的辅助交点避开第一槽的全部弦交 $E$，并避开第三槽
  的固定支持。
- 第三槽的弦交 $E$ 避开前两槽的全部弦交 $E$，其直线还避开
  前两槽任意两条线的交点。

这些条件均只排除 $R$ 的有限集合。确实，每条弦为通过一个
固定 $P_i$ 或 $Q_i$ 的非恒定弦线族；待避点若在 $E$ 上，
此前已排除它等于该固定端点，待避的前两线交点则不在 $E$
上。故要求弦经过该点是有限条件。切线、重交及第三交点
退化也只给有限条件。槽内重复的弦可合并指数；它们不会
同时出现在一次跨三槽的四线项中。

特征零的 $k$ 无限，可选 $x(R)\in k$ 避开这些有限条件，
然后仅解一次二次方程取得 $R$。依次选择三个点，所需
扩域是二次扩张塔。最后选一条一般的参考直线 $L_0$，
避开全部已有交点和弦交 $E$，并与 $E$ 横截；其三个交
$E$ 的点至多再需一个三次多项式的 splitting field。

取上述所有辅助域的 Galois closure。二次塔的正常闭包是
$2$-扩张；三次 splitting field 的群为 $S_3$ 的子群。
连同原已分裂支持的 prime-to-$p$ Galois 域，最终得到
$$
L/k\text{ 有限 Galois},\qquad p\nmid[L:k].
\tag{1156.16}
$$
这里并非仅由“扩张次数小于 $p$”便猜测正常闭包 prime-to-$p$；
使用的是这些具体二次与三次 splitting 的群。

把 (1156.15) 各槽都改写成相对同一 $L_0$ 的线性因子，
再展开三重外积。每项正好从三个不同槽各取一条线，
所以都满足 §3 的一般位置；每个交点、重数和 cross-ratio
均在 $L$ 上明确。含 $\lambda$ 的项总残数由同一个
Weil reciprocity 乘法关系消去。于是得到一个有限表达式
$B(f_1,f_2,f_3)$，满足
$$
\delta_B B(f_1,f_2,f_3)
=\sum_{x\in E(L)}
 \operatorname{res}_x(f_1\wedge f_2\wedge f_3).
\tag{1156.17}
$$
系数只用整数和 $p$ 单位；这不是一条仅有有理存在性的
Bloch lifting 声明。§2 随即给该完整残数 cup 的实际整
primitive。所用四线分解、所有常数和根关系都是输入数据，
不会因写成 $B$ 而自动变成 canonical choice。

## 5. Corestriction 与次数乘法的显式链同伦

设 $H\subset G$ 为开子群，指数 $d$，$A,B$ 为连续
$\mathbf Z_p[G]$-格。选右陪集 $H\backslash G$ 的代表集
$\mathcal T$，写
$$
t g=h_{t,g}t_g,\qquad h_{t,g}\in H.
$$
沿用 R1133 的 transfer：
$$
(\operatorname{Cor} f)(g)=
 \sum_{t\in\mathcal T}t^{-1}f(h_{t,g}).
\tag{1156.18}
$$
二次上链使用相继的 $t_g$。这是链映射。

对 $a\in Z^1(G,A),b\in Z^1(G,B)$，置
$$
u_t=t^{-1}a(t),\qquad v_t=t^{-1}b(t),\qquad
U=\sum_tu_t,\quad V=\sum_tv_t.
$$
由实际 cocycle 恒等式，
$$
t^{-1}a(h_{t,g})=a(g)+u_t-g u_{t_g}.
\tag{1156.19}
$$
定义一次上链
$$
\begin{aligned}
K_{a,b}(g)={}&-U\otimes b(g)+a(g)\otimes gV\\
 &+\sum_tu_t\otimes(gv_{t_g}-v_t).
\end{aligned}
\tag{1156.20}
$$
则有准确的链同伦
$$
dK_{a,b}
=\operatorname{Cor}(\operatorname{res}a\smile\operatorname{res}b)
 -d(a\smile b).
\tag{1156.21}
$$

为核全部符号，令 $\mathcal P(A)=\operatorname{Map}(\mathcal T,A)$，
作用为 $(gF)_t=gF_{t_g}$，$i:A\to\mathcal P(A)$ 为常值嵌入。
(1156.19) 恰为 $\widetilde a=ia-du$，同样
$\widetilde b=ib-dv$。展开两 cup 的差为
$$
-du\smile ib-ia\smile dv+du\smile dv.
$$
它正是
$d(-u\smile ib+ia\smile v+u\smile dv)$。
逐坐标求和便得到 (1156.20)–(1156.21)，不漏 $t_g$。

对 skew cup，用
$$
K^{\rm sk}_{a,b}
=\frac12(K_{a,b}-\operatorname{flip}K_{b,a}).
$$
如果 $p\nmid d$，且 $T_L$ 是已实际给出的
$\mathbf Z_p$ 值一次上链，满足
$dT_L=-\operatorname{res}\Omega_{\rm sk}$，则
$$
T_k=\frac{\operatorname{Cor}T_L+K^{\rm sk}}d,
\qquad dT_k=-\Omega_{\rm sk}.
\tag{1156.22}
$$
对于有限和及任何 $G$-等变 bilinear contraction 逐项使用同式。
ordered cup 则直接使用 (1156.20)，不再做 skew。
所有根、陪集及零次修正固定后，这些公式在全部
$\mathbf Z/p^n$ 层相容。

这里除的是 (1156.16) 的实际 $p$ 单位 $d$。
(1156.20) 的最后一项以及原 transfer 中的同陪集乘积必须
保留；没有使用错误的
$\operatorname{Cor}(ab)=\operatorname{Cor}(a)\operatorname{Cor}(b)$。

## 6. 闭点残数的实际系数模与原三项

不必把几何点数当作闭点 corestriction。对一个闭点 $x$，
取 $H_x=G_{k(x)}$。它的每个实际单位槽定义
$$
a_x\in Z^1\!\left(G_k,
 \operatorname{Coind}_{H_x}^{G_k}\mathbf Z_p(1)\right),
\qquad
(a_x(g))_t=t^{-1}\kappa_x(h_{t,g}).
\tag{1156.23}
$$
在两个相同 coinduced 模之间使用逐陪集乘积后求和的
$G_k$-等变配对。其对两个一次上链的 cup 值，准确是
该闭点原 cup 的 (1156.18) corestriction。
因此，所有实际闭点构成有限个 permutation–Tate 格的直和；
原完整残数二次上链 $\Omega$ 是这些指定 Kummer 上链
经一个明确双线性配对的 cup。

将 (1156.16) 的 Galois 域再含全部支持点。限制到 $G_L$
后，permutation 坐标逐个固定，(1156.23) 的每个分量就是
对应几何点、运输后的同一根 Kummer cocycle。
§4 和 §2 构造 $\operatorname{res}\Omega$ 的实际 primitive，
§5 再将它下降为 $-\Omega$ 的 primitive。
这是闭点与全部几何点之间的实际箭头；没有丢掉一个
$\operatorname{Cor}$，也没有把不同陪集强行配成同一个 norm。

回到 (1156.1)，写
$$
u=A-B,\quad v=B-C,\quad w=C-A,\qquad u+v+w=0,
\qquad d_t=c^2\mathbf1_{t=0}-1.
$$
三个 divisor coset 两两不交。按原 aux-$c$ (C.4)–(C.6) 的
$K_2$ 槽顺序定义其 ordered 残数 cup 为
$$
\begin{aligned}
\Omega_c={}&
 \sum_{t\in E[c]_{\rm cl}}\operatorname{Cor}
 d_t\,\kappa(h_c(u+t))\smile\kappa(h_c(w-t))\\
&+\sum_{t\in E[c]_{\rm cl}}\operatorname{Cor}
 d_t\,\kappa(h_c(w+t))\smile\kappa(h_c(v-t))\\
&+\sum_{t\in E[c]_{\rm cl}}\operatorname{Cor}
 d_t\,\kappa(h_c(v+t))\smile\kappa(h_c(u-t)).
\end{aligned}
\tag{1156.24}
$$
值和 root 都在相应 residue field 中；$t=0$ 的系数确为
$c^2-1$。中间槽的 tame 负号已包含在最后一行的槽交换，
转成 ordered cocycle 时使用 §2 的完整二次修正，不能把
field $K_2$ 的反对称性当成 cochain 的逐点反对称性。

$c<p$ 保证 $k(E[c])/k$ 的次数 prime-to-$p$：
其 Galois 群嵌入 $\operatorname{GL}_2(\mathbf Z/c)$，
对每个 $\ell^e\Vert c$，
$\ell^{4e-3}(\ell-1)^2(\ell+1)$ 不含 $p$。
所以 §4–6 对这一实际原配置全部适用，证明 (1156.2)。

若把所有 (1156.23) 的第一、第二槽分别记为
$a\in Z^1(G_k,A_0),b\in Z^1(G_k,B_0)$，
实际 contraction 为 $\mathcal B:A_0\otimes B_0\to\mathbf Z_p(2)$，
则
$$
(x,y,z)(x',y',z')
=(x+x',y+y',z+z'+\mathcal B(x,y'))
\tag{1156.25}
$$
定义一个有限秩的 class-two $\mathbf Z_p$ 群。
$(a,b,\mathcal H_c)$ 是它的真正连续 Galois cocycle。
逐层约化给有限 étale torsor 及兼容的层间态射，
从而完成本文所称的“固定函数兼容整塔”。
这一步不是以 cup 的零 cohomology class 重新选择某个
存在性提升，而是使用上文已经给出的中央 cochain。

## 7. 对原 moment filling 的用途与仍保留的项

本文新增的实际输入是：

1. 原 $D$ primitive 可对任一给定有限 wedge 边界，以
   (1156.6)、(1156.10) 修正成同根的 ordered 零上链。
2. 原三互不交主除子存在 prime-to-$p$ 辅助域上的有限四线
   表达式，全部一般位置、模型常数、线交重数均已支付。
3. (1156.20) 是可直接使用的 transfer 链同伦，不只给
   $\operatorname{Cor}\operatorname{res}=d$ 的 cohomology 等式。
4. 原 $\Psi_c$ 三项已成为实际连续 $\mathbf Z_p$ 上链式。

这些步骤没有删除原 aux-$c$ (C.27)–(C.28) 的
$C_{a,b,c}$。三槽同时平滑得到的是实际相关和的 primitive；
不能把它冒称为原任意两 moment 的裸 cup primitive。

后继若沿原整 moment 塔比较，仍需把指定 S/U filling、不同
$E[p^n]$ 层的 norm-distribution、其 tensor contraction 以及所有根
规范接到原
$V_\infty=\operatorname{Sym}^4T_pE(1)\oplus
\operatorname{Sym}^8T_pE(1)\oplus\mathbf Z_p(5)$ 与原中央 $Z_\infty$。
本文的系数模 (1156.23) 是实际闭点 permutation–Tate 模，
没有将它未经比较替换成这个无限级 moment 模。
因而 R1147 §16 的原 moment 塔识别尚不能仅凭 §1–6 自动应用。
下面另给一个先延伸 raw 塔、再作有限层实际 pushout 的入口；
该入口不要求先证明所有 $E[p^n]$ 层的 norm-distribution。

对已经给出的四线或五点块，其局部读取可使用
[R1155](R1155-original-primitive-dilogarithmic-Frobenius-readout.md)
的完整有限 dilogarithm、Frobenius 改提升及五项运输。
实际参数 $u$ 与其提升之间的 $\varepsilon$、中央二次修正、
全部 ramified nilpotents 和逐陪集乘积须保留。
本文没有将任意分歧域的相对纤维运输当成同点 arithmetic
Frobenius，也没有读出或宣称非零的原 CM $z_{12}$。

## 8. 用原 discriminant 归一后，raw 整塔先补全部内点

这一节消除个别 $h_c(P+t)$ 的 Hodge 权问题，并付实际 raw 塔
的全 noncusp 延伸。它仍不代后续指定 bilinear pushout 和
完整群下降。

### 8.1. 真正的权零单位与三个 $12$ 因子

使用与 $\psi_c$ 同一个 Weierstrass 模型的 discriminant
$\Delta_E$。模型缩放下 $\psi_c$ 的权为 $c^2-1$，
$\Delta_E$ 的权为 $12$。定义
$$
\widehat h_c(T)=\Delta_E^{\,c^2-1}h_c(T)^{12}.
\tag{1156.26}
$$
两项权准确抵消。在原非退化模曲线上，$\Delta_E$ 不灭；
$P+t$ 既非零也不在 $E[c]$，故
$\widehat h_c(P+t)$ 是真正的全局单位。
它可以在实际 $c$-division finite étale cover 上读取，
也可以保闭点系数模作 pushforward。无需选择一个可能
在内点有零极的有理 Hodge 标架。

三个新函数
$\widehat f_A(T)=\widehat h_c(T-A)$ 等，仍有两两不交支持，
但其 divisor 是 $12$ 倍原 divisor。原 (C.9) 的共同常数
计算和循环消去给
$$
\sum_{\rm cyc}\Psi_{\widehat h_c}
=144\sum_{\rm cyc}\Psi_{h_c}
\quad\text{于 }\Lambda^2(k^\times)\otimes\mathbf Z_{(p)},
\tag{1156.27}
$$
其中 $\Psi_{\widehat h_c}$ 暂仍按原 $d_t=c^2\mathbf1_{t=0}-1$
定义。真正三函数的完整残数还要乘第三个 $12$：
$$
\sum_x\operatorname{res}_x
 (\widehat f_A\wedge\widehat f_B\wedge\widehat f_C)
=1728\sum_x\operatorname{res}_x(f_A\wedge f_B\wedge f_C).
\tag{1156.28}
$$
另一种直接核法是展开三槽的同一个
$\Delta_E^{c^2-1}$；每个含 base 常数的总残数由 Weil
reciprocity 消去。没有把常数项逐点删掉。
(1156.27) 是两个值槽的尺度，(1156.28) 另外含 divisor 槽；
二者不能混用。


还须区分 wedge 尺度与 ordered 上链尺度。先在 $E[c]$ 的分裂域，
对每个重复出现的 $h_c(P+t)$ 固定同一根，令
$\widehat h$ 的根为 $(h\text{ 的根})^{12}
(\Delta\text{ 的根})^{c^2-1}$。记
$$
w=c^2-1,\quad D=\kappa(\Delta),\quad
S(P)=\sum_t d_t\,\kappa(h_c(P+t)),\quad
T=S(u)+S(v)+S(w_0),\qquad w_0=C-A.
$$
这里 $w$ 是指数，$w_0$ 才是第三个点差。
由 $t\mapsto-t$、同根偶性和 $\sum_td_t=0$，完整展开给
$$
\widehat\Omega_c-144\Omega_c
=12w(D\smile T+T\smile D)
=-12w\,d(DT).
\tag{1156.28a}
$$
所以只有 skew/BCH 版本逐上链恰有 $144$ 尺度；
ordered 版本必须保留这个二次修正。若
$d\widehat H=-\widehat\Omega_c$，则准确的原 primitive 是
$(\widehat H-12wDT)/144$。真正三函数的残数 primitive
还先按 divisor 的 $12$ 除回；所有除数仍为 $p$ 单位。
从分裂域回原域时，再使用 §5 的 projection/Cor 链同伦，
不能用 cohomology 的 projection formula 省略其上链项。

现在把 §4–6 直接应用于这三个归一函数。
得到的 raw torsor 交换商仅由实际全局单位
$\widehat h_c(P+t)$ 的 Kummer cocycle 构成，中心仍为无挠
$\mathbf Z_p(2)$。所有 $12,144,1728$ 都是 $p$ 单位。
若之后比较原加权矩，原 augmentation 恰为零使共同
$\Delta_E$ 幂在函数等式中严格消失；相应根的
$\mu_{p^\infty}$ 修正仍按 (1156.6) 保留。

### 8.2. 先在整塔上消水平惯性

令 $Y$ 是原固定 Weil component 的 full-level 非 cusp 光滑
模曲线，定义于一个数域，$F=k(Y)$。必要的 $c$-division
cover 在 $Y$ 上有限 étale，故 §6 的所有 permutation–Tate
系数格，以及上一小节的全部交换商 Kummer 类，均已在 $Y$
延伸。归一 raw 塔给一个实际连续 cocycle
$$
c:G_F\longrightarrow G^{\rm raw}_\infty,
\qquad Z^{\rm raw}_\infty=\mathbf Z_p(2).
$$
对任意闭点 $x\in Y$，交换商和系数在 $x$ 无分歧，
所以惯性限制是中心同态
$$
\rho_x:I_x\longrightarrow\mathbf Z_p(2).
$$
因为中心性，torsor 的共轭项不再改变它；
其分解群等变性准确给
$$
\rho_x\in
\operatorname{Hom}_{G_{k(x)}}(\mathbf Z_p(1),\mathbf Z_p(2))
=H^0(k(x),\mathbf Z_p(1))=0.
\tag{1156.29}
$$
最后一个零因 $k(x)$ 是数域，仅含有限多个 $p$ 次幂单位根。
等价地，在一个非 $p$ 有限位，Tate Frobenius 的特征值
不为 $1$。这里使用的是无挠完整 $\mathbf Z_p$ 格；
不能从这句话推出单独的
$H^0(k(x),\mathbf Z/p^n(1))$ 为零。

故归一 raw 塔的每一层在 $Y$ 的全部闭点均无分歧。
对 regular curve 逐层正规化、用 purity，得到 $Y$ 上的
有限 étale torsor。泛点上的作用和层间态射由正常性唯一
延伸，因而全部层相容。无需存在一个同时容纳全部层的
预先选定开集，也不必先去构造 $E[p^n]$ 的 norm-compatible
moment。

对有限多个实际三角形，取 raw 塔的有限纤维积，
中心为 $\bigoplus\mathbf Z_p(2)$；同一个证明逐分量适用。
这确已付“先补点，再约模 $p$”的原固定配置来源。

### 8.3. 可以消费什么，仍须给出什么

现可在已延伸的 raw 塔上先约模 $p$，然后使用实际
$E[p]$ 向量的有限权重作群同态；这一步本身不要求把
$P^d$ 任选提升为 $\mathbf Z_p$ 系数，也不会丢失相应 carry。

但要得到 R1147 的同一目标，必须明确给出：

- 原指定 target bilinear form 是哪些 raw bilinear forms 的
  真线性 pushout，且全 anti-diagonal correlation 一并计入；
- 该有限群同态与全部 actual level/Weil-component 作用相容，
  由此有真实 $\operatorname{GL}_2$ 及算术下降；
- 交换商及根的规范与原 moment 对象相同。

完成这三项后才能在原 $\mathcal M$ 上用已经支付的
$H^1(\mathcal M,Z_1)=0$ 作最后识别。不能在 $Y$ 或另一个
较小开集上先使用该消失。本文不声称 raw primitive 的
任意分解选择已经满足这三项，也没有以其延伸替代原 $z_{12}$
的实际读取。

## 来源与核验范围

- Nakamura–Wojtkowiak，*Tensor and homotopy criteria for functional
  equations of $\ell$-adic and classical iterated integrals*，
  LMS Lecture Note Series 393 (2012)，258–310，§4.2、§5.2、
  §6.1、Theorem 6.1。本文的实际 root/ordered/BCH 规范直接
  消费已付 R1133 §11，不另换一份 dilogarithm。
  https://math.univ-cotedazur.fr/~wojtkow/11NakamuraWojtkowiak.pdf
- A. Goncharov，*Euler complexes and geometry of modular varieties*，
  作者全文 arXiv:math/0510310v5，§2.2 Theorem 2.4、
  Lemma 2.5 和 §2.4 Lemma 2.9：
  https://arxiv.org/pdf/math/0510310 。
  本文仅借它定位四线来源；(1156.13)–(1156.17) 的
  $p$-local 边界、符号、有限辅助域另作完整证明，
  不引用该文有理 Euler-complex 的整性。
- 原 aux-$c$ 笔记 (C.2)–(C.8)、(C.12)、(C.27)–(C.28)：
  全部实际除子、残数、闭点 Cor、half/all 与保留的交叉项。
- §2 的根关系/Leibniz 与 §5 的 transfer 同伦由
  global_route 逐式推导；o2_high_coefficient 已独立纸核
  (1156.19)–(1156.22) 的右陪集作用、三个符号及 prime-to-$p$
  反除。本文没有新数学程序运行。
