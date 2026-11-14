# R230：正正常态的 chaos 指数矩分解与实际湮灭者排除

日期：2026-11-12（UTC）。独占作者：literature；l2_moments 独立确认实际有限 chaos 乘积可用排序展开直接构造。

**状态：以下结论有完整证明。** 本稿针对原 Haar 表示，不在边界表示上推断正常性。它不排除任意正常正湮灭态，也不排除任意有限秩正常态。新范围是：支撑在任意固定有限 Walsh 次数上的全部正迹类算子，以及具有足够 Walsh 次数指数矩的正迹类算子；各向量在位指标上的尾可以任意慢。

令 $\mathcal N$ 为 Walsh 次数算子，$P_p$ 为次数恰为 $p$ 的正交投影。对正迹类算子 $\rho$ 及 $r>1$，定义
$$
\mathcal E_r(\rho)=\sum_{p=0}^{\infty}r^{2p}\operatorname{Tr}(P_p\rho).
\tag{0.1}
$$
这是非负项级数，允许值为无穷。有限时也等于
$\|r^{\mathcal N}\rho^{1/2}\|_{\mathrm{HS}}^2$，不需要先把两个无界算子的形式乘积当成处处定义。

**主结论。** 若 $r>9$、$\mathcal E_r(\rho)<\infty$，则存在唯一 $h_\rho\in H$，使对每个有界交换子 $T\in\{A\}'$，
$$
\boxed{\operatorname{Tr}(\rho T)=B(Th_\rho,1),\qquad
B(h_\rho,1)=\operatorname{Tr}\rho.}
\tag{0.2}
$$
若 $S\in\{A\}'$ 在全 $H$ 上单射，则
$$
\rho\ge0,\quad
\operatorname{Tr}(\rho SF)=0\quad(F\in\mathcal A),\quad
\mathcal E_r(\rho)<\infty
\quad\Longrightarrow\quad \rho=0.
\tag{0.3}
$$
这里 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$。只需在 (0.3) 检验 $F=A^n$，$n\ge0$。

## 1. 实际算子与双线性形式

沿用原 Haar 空间 $H=L^2(\mathbb Z_2,\mu)$、Walsh 基 $\chi_F$、常函数 $1$，以及
$$
(Cf)(y)=\overline{f(-1-y)},\qquad
B(f,g)=\langle f,Cg\rangle.
\tag{1.1}
$$
内积对第一变量线性；$B$ 连续、对称且双线性。每个 $T\in\{A\}'$ 都满足
$$
B(Tf,g)=B(f,Tg).
\tag{1.2}
$$
常函数 $1$ 对 $A$ 循环。上述输入见 [R122](../results/R122-dyadic-gauge-coboundaries-and-kernel-exclusion.md) §1。

为避免把两个模型混同，定义
$$
E_j=e_{10}^{(j)},\qquad D_j=I-2E_j,
$$
$$
N_j=A^{2^j}/d_j,\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
\tag{1.3}
$$
$D_j$ 是独立位模型；$V_j$ 是实际有界交换子。由实际递推和逆界，
$$
\|N_j\|=1,\quad N_j^2=\eta_jN_{j+1},\quad
\|N_j-E_j\|\le\eta_j,\quad
\|(I+N_j)^{-1}\|<3,
$$
$$
0<\eta_j\le e^{-770\,16^j},
\tag{1.4}
$$
从而
$$
\|V_j\|\le6,\qquad
\|V_j-D_j\|\le8\eta_j.
\tag{1.5}
$$
例如
$$
V_j-D_j=-2(N_j-E_j)+2N_j^2(I+N_j)^{-1},
$$
立即给出第二个界。

对有限集合 $F$，有准确恒等式
$$
V_F:=\prod_{j\in F}V_j\in\mathcal A,\qquad V_F1=\chi_F.
\tag{1.6}
$$
因此若 $f=\sum_F\widehat f(F)\chi_F$ 是有限柱函数，
$$
X_f=\sum_F\widehat f(F)V_F\in\mathcal A,\qquad X_f1=f.
\tag{1.7}
$$
这是 [R88](../results/R88-riesz-basis-bounded-multipliers-strong-closure.md) §6 的实际有限柱乘子。特别地，不同位的 (1.6) 不允许把同一位的实际平方当作点态平方：
$V_j^21$ 一般不等于 $1$。

在 Walsh 基上，
$$
D_j\chi_G=
\begin{cases}
\chi_{G\cup\{j\}},&j\notin G,\\
2\chi_G-\chi_{G\setminus\{j\}},&j\in G.
\end{cases}
\tag{1.8}
$$

## 2. 纯模型的全维数无关双线性估计

记 $H_p=P_pH$。对有限柱 $f\in H_p$、$g\in H_q$，置
$$
\mathcal P(f,g)=
\left(\sum_{|F|=p}\widehat f(F)D_F\right)g.
\tag{2.1}
$$

**引理 2.1。** 对全部 $p,q\ge0$，
$$
\boxed{\|\mathcal P(f,g)\|
\le9^{p+q}\|f\|\,\|g\|.}
\tag{2.2}
$$
常数不依赖参与位的个数；因此 (2.1) 唯一延拓为
$H_p\times H_q\to H$ 的连续双线性映射。

**证明。** 对一对 $|F|=p$、$|G|=q$，把共同位 $F\cap G$ 分为在 (1.8) 中选择删除的集合 $D$，以及选择保留的集合 $K$。另置
$$
U=F\setminus G,\qquad V=G\setminus F.
$$
这四个集合两两不交。令
$$
r=|F\cap G|,\quad d=|D|,\quad k=|K|=r-d,
$$
$$
u=p-r,\quad v=q-r,\quad \ell=u+v+k=p+q-r-d.
$$
这一项的输出是 $\chi_{U\cup V\cup K}$，系数为 $(-1)^d2^k$。

固定 $r,d$。给定互不交的 $U,V,K$，内层求和为
$$
H_{U,V,K}
=\sum_{\substack{|D|=d\\D\cap(U\cup V\cup K)=\varnothing}}
\widehat f(U\cup K\cup D)\,
\widehat g(V\cup K\cup D).
\tag{2.3}
$$
Cauchy–Schwarz 后，去掉两个非负和中额外的不交限制，再对 $U,V,K$ 求和，得到
$$
\sum_{U,V,K}|H_{U,V,K}|^2
\le C_p C_q\,\|f\|^2\|g\|^2,
\tag{2.4}
$$
其中
$$
C_p=\binom pk\binom{p-k}{d}
=\frac{p!}{k!\,d!\,u!},
\quad
C_q=\frac{q!}{k!\,d!\,v!}.
\tag{2.5}
$$
为付清计数：固定 $K$ 时，$f$ 的每个 $p$ 集合被 $(U,D)$ 分拆计
$\binom{p-k}{d}$ 次；随后对 $K$ 求和再计 $\binom pk$ 次。对 $g$ 同理。最后使用
$\sum_K A_KB_K\le(\sum_KA_K)(\sum_KB_K)$，所有量均非负。

对一个固定输出集合 $J$，其 $(U,V,K)$ 分拆数为
$$
M_{\ell,u,v,k}=\frac{\ell!}{u!\,v!\,k!}.
$$
再一次 Cauchy–Schwarz 使这一 $(r,d)$ 分量的范数不超过
$$
2^k\sqrt{M_{\ell,u,v,k}C_pC_q}\,\|f\|\,\|g\|.
\tag{2.6}
$$
各多项式系数计数给
$C_p\le3^p$、$C_q\le3^q$、$M_{\ell,u,v,k}\le3^\ell\le3^{p+q}$，
并且 $k\le(p+q)/2$。所以 (2.6) 至多
$$
2^{(p+q)/2}3^{p+q}\|f\|\,\|g\|.
$$
令 $m=\min(p,q)$。可能的 $(r,d)$ 数量为
$(m+1)(m+2)/2$；$m=0$ 时为一，$m\ge1$ 时不超过 $4^m\le2^{p+q}$。
相加得到 $(6\sqrt2)^{p+q}\|f\|\|g\|$，小于或等于 (2.2) 的右侧。
$p=q=0$ 时直接为常数乘积。证毕。

这个估计同时支付所有重复位的保留项与删除项，没有把实际乘法换成普通 Walsh 点乘。

## 3. 实际 carry 的排序展开及全次数常数

定义
$$
\epsilon=8\sum_{j\ge0}\eta_j37^{j/2}.
\tag{3.1}
$$
由 $16^j-1\ge15j$，
$$
\epsilon\le
\frac{8e^{-770}}{1-\sqrt{37}\,e^{-11550}}<1.
\tag{3.2}
$$

**引理 3.1。** 对有限柱 $f\in H_p$、$g\in H_q$，
$$
\boxed{\|X_fg\|\le(1+\epsilon)9^{p+q}\|f\|\,\|g\|.}
\tag{3.3}
$$

**证明。** 每个有限集合 $F$ 按位从小到大排序。准确 telescoping 恒等式为
$$
V_F-D_F=
\sum_{j\in F}
V_{F\cap[0,j)}(V_j-D_j)D_{F\cap(j,\infty)}.
\tag{3.4}
$$
这里不假设混合的实际因子和纯因子彼此交换。

固定 $j$ 及 $K\subset[0,j)$，$\lvert K\rvert\le p-1$，定义高尾齐次函数
$$
f_{j,K}
=\sum_{\substack{L\subset(j,\infty)\\|L|=p-1-|K|}}
\widehat f(K\cup\{j\}\cup L)\chi_L.
\tag{3.5}
$$
对每个固定 $j$，有
$$
\sum_K\|f_{j,K}\|^2\le\|f\|^2.
\tag{3.6}
$$
把 (3.4) 对 $F$ 求和，后面的纯因子和先作用于 $g$。引理2.1给
$$
\left\|\sum_L\widehat f(K\cup\{j\}\cup L)D_Lg\right\|
\le9^{p+q}\|f_{j,K}\|\,\|g\|.
$$
前面的实际因子范数不超过 $6^{|K|}$；中间误差至多 $8\eta_j$。
因此所有固定 $j$ 项的总范数至多
$$
8\eta_j9^{p+q}\|g\|
\sum_{K\subset[0,j)}6^{|K|}\|f_{j,K}\|
\le8\eta_j9^{p+q}37^{j/2}\|f\|\|g\|.
\tag{3.7}
$$
最后一步用 (3.6) 及
$\sum_{K\subset[0,j)}36^{|K|}=37^j$。
对 $j$ 求和，(3.1) 控制整个实际误差；再加 (2.2) 即得 (3.3)。
若 $p=0$，误差为空，结论仍成立。证毕。

因 (3.3) 是双线性的统一范数估计，低位条件期望逼近给唯一连续延拓
$$
\mathcal M_{p,q}:H_p\times H_q\longrightarrow H.
\tag{3.8}
$$
对有限柱的两个输入，它正是 $X_fg=X_gf$，因为两个有界实际乘子交换并在 $1$ 上取值。因此
$$
\mathcal M_{p,q}(f,g)=\mathcal M_{q,p}(g,f).
\tag{3.9}
$$
输出允许有无限 Walsh 次数；本稿没有把它放回 $H_{\le p+q}$。

## 4. 指数次数空间、图域和双线性配对

置
$$
\mathscr H_9=
\left\{f\in H:
\|f\|_{\mathscr H_9}:=\sum_{p\ge0}9^p\|P_pf\|<\infty
\right\}.
\tag{4.1}
$$
有限柱函数在此 Banach 空间中稠密：先截断次数，再在每个有限次数内截断位指标。引理3.1给绝对 $H$ 收敛的双线性乘积
$$
f\odot g=\sum_{p,q\ge0}\mathcal M_{p,q}(P_pf,P_qg),
$$
$$
\boxed{\|f\odot g\|
\le(1+\epsilon)\|f\|_{\mathscr H_9}\|g\|_{\mathscr H_9}.}
\tag{4.2}
$$
该乘积对称。由于输出只已知在 $H$，这里不把 $\mathscr H_9$ 宣称为实际乘法下的 Banach 代数。

下面付清图域。对任意 $f\in H$，在有限柱函数空间 $\mathscr D$ 上定义
$$
\mathfrak X_f^0g=X_gf,\qquad g\in\mathscr D,
\tag{4.3}
$$
其中 $X_g$ 是 (1.7) 的真实有界算子。若 $g,h\in\mathscr D$，由 (1.2) 及
$X_gh=X_hg$，
$$
B(\mathfrak X_f^0g,h)=B(f,X_gh)
=B(f,X_hg)=B(g,\mathfrak X_f^0h).
\tag{4.4}
$$
因此 $\mathfrak X_f^0$ 为稠密定义的 $C$ 对称算子，故可闭。
也可直接核验：若 $g_n\to0$ 且 $\mathfrak X_f^0g_n\to v$，则 (4.4) 给
$B(v,h)=0$ 对所有 $h\in\mathscr D$ 成立，稠密性迫 $v=0$。

若 $f,g\in\mathscr H_9$，取 $g_n\in\mathscr D$ 在 $\mathscr H_9$ 中逼近 $g$。
对固定有限柱 $g_n$，再以有限柱逼近 $f$，有界性给
$$
\mathfrak X_f^0g_n=X_{g_n}f=f\odot g_n.
$$
由 (4.2)，右侧在 $H$ 中趋 $f\odot g$，故
$$
\boxed{
g\in\operatorname{Dom}\overline{\mathfrak X_f^0},
\qquad
\overline{\mathfrak X_f^0}g=f\odot g.
}
\tag{4.5}
$$
不需要假定任意未界乘子已经在全 $H$ 上定义，也不需要在未知的自然乘积域上交换两个未界算子。

最关键的配对恒等式是：对每个 $T\in\{A\}'$ 及 $f,g\in\mathscr H_9$，
$$
\boxed{B(Tf,g)=B(T(f\odot g),1).}
\tag{4.6}
$$
先对有限柱 $f,g$，利用有界 $X_f,X_g$、(1.2) 和交换性，
$$
B(Tf,g)
=B(TX_f1,X_g1)
=B(TX_gX_f1,1).
$$
其右侧等于 (4.6)。随后在 $\mathscr H_9$ 中同时逼近两个输入：
左侧由 $H$ 连续性取极限，右侧由 (4.2) 取极限。
这一步没有将 $T$ 强行作用到未知的未界图域内。

另外，
$$
C\chi_F=(-1)^{|F|}\chi_F,
$$
系数同时被复共轭，所以 $C$ 等距保持每个次数层及 $\mathscr H_9$。
取 $T=I$、$g=Cf$，得到
$$
\boxed{B(f\odot Cf,1)=\|f\|^2.}
\tag{4.7}
$$

## 5. 正迹类算子的向量分解

若 $r>9$，则 Cauchy–Schwarz 给
$$
\|f\|_{\mathscr H_9}
\le\left(1-\frac{81}{r^2}\right)^{-1/2}
\|r^{\mathcal N}f\|.
\tag{5.1}
$$

设 $\rho\ge0$ 为迹类，$\mathcal E_r(\rho)<\infty$。
取其正秩一分解
$$
\rho=\sum_{\nu\ge1}x_\nu\otimes x_\nu,
\qquad \sum_\nu\|x_\nu\|^2=\operatorname{Tr}\rho,
\tag{5.2}
$$
例如用谱分解，平方根特征值吸收到 $x_\nu$ 中。
由 (0.1) 及 Tonelli，
$$
\sum_\nu\|r^{\mathcal N}x_\nu\|^2=\mathcal E_r(\rho)<\infty.
\tag{5.3}
$$
所以每个 $x_\nu\in\mathscr H_9$，并且
$$
h_\rho:=\sum_{\nu\ge1}x_\nu\odot Cx_\nu
\tag{5.4}
$$
在 $H$ 中绝对收敛。明确地，
$$
\boxed{
\|h_\rho\|\le
\frac{1+\epsilon}{1-81/r^2}\,\mathcal E_r(\rho).
}
\tag{5.5}
$$
对每个有界 $T\in\{A\}'$，(4.6) 给
$$
\operatorname{Tr}(\rho T)
=\sum_\nu B(Tx_\nu,Cx_\nu)
=B(Th_\rho,1).
\tag{5.6}
$$
左侧级数由 $\|T\|\sum_\nu\|x_\nu\|^2$ 控制，右侧由 (5.5) 控制。
特别 (4.7) 给
$$
B(h_\rho,1)=\sum_\nu\|x_\nu\|^2=\operatorname{Tr}\rho.
\tag{5.7}
$$

$h_\rho$ 与 (5.2) 的选择无关。如果 $h,h'$ 都满足 (5.6)，则
$B(A^n(h-h'),1)=B(h-h',A^n1)=0$ 对全部 $n$ 成立。
$1$ 的循环性及 $C$ 的等距双射性迫 $h=h'$。

更一般地，本节只需某个正秩一分解满足
$\sum_\nu\|x_\nu\|_{\mathscr H_9}^2<\infty$。
指数矩条件 (0.1) 是一个基无关、易于检验的充分条件。

## 6. 正正常湮灭者的排除

设 $S\in\{A\}'$ 在原 $H$ 上单射，$\rho\ge0$ 满足本稿指数矩条件及
$$
\operatorname{Tr}(\rho SF)=0\qquad(F\in\mathcal A).
\tag{6.1}
$$
取 $F=A^n$，由 (5.6)、交换性及 (1.2)，
$$
0=B(SA^nh_\rho,1)=B(Sh_\rho,A^n1).
\tag{6.2}
$$
因多项式轨道 $\{p(A)1\}$ 稠密，得到 $Sh_\rho=0$。
全 $H$ 上的单射性给 $h_\rho=0$。而 (5.7) 给
$\operatorname{Tr}\rho=0$，正性遂迫 $\rho=0$。证明 (0.3)。

这不是把全空间稠密像擅自搬到不变限制上：实际使用的是 (5.6) 的单向量分解，以及 $S$ 在全空间上已知的单射性。

特别有以下结论。

- 对任意固定 $p$，若 $\rho\ge0$、$\operatorname{Ran}\rho^{1/2}\subset H_{\le p}$，则
  $\mathcal E_r(\rho)\le r^{2p}\operatorname{Tr}\rho$。因此这种任意秩正迹类算子都不能非零地湮灭 $S\mathcal A$。
- 任意有限秩 $\rho=\sum_{\nu=1}^d x_\nu\otimes x_\nu$，若每个 $x_\nu$ 都是有限 chaos，便属于上述某个统一有限 $p$。每个 $x_\nu$ 可以涉及无限多位，其位索引尾无需满足任何速度。
- 若一个非零正正常 $\rho$ 确实湮灭 $S\mathcal A$，则必对每个 $r>9$ 有
  $\mathcal E_r(\rho)=\infty$。这不排除此类正常算子的存在；正常性本身不提供任何这样的指数矩。

## 7. 实际慢符号及共同零商的应用

本题的
$$
S_N=\sum_{j\ge0}(j+1)^{-2}N_j,\qquad
S_Y=\sum_{j\ge0}(j+1)^{-2}N_j(I+N_j)^{-1}
\tag{7.1}
$$
均为已知全 $H$ 单射的有界交换子。
$S_Y$ 由 [R122](../results/R122-dyadic-gauge-coboundaries-and-kernel-exclusion.md) 主定理给出；
$S_N$ 的每个 dyadic gauge 增量是真正解析芽，且它不是标量，因此同稿 §4.2 的一般判据适用。
故 (0.3) 同时适用于这两个实际慢符号。

对于 R208 的共同零商，令实际第一行 $a\in\ell^2$ 非零，并置
$$
Z=\sum_j a_j^2(I-V_j^2)
=4\sum_j a_j^2N_j(I+N_j)^{-2}.
\tag{7.2}
$$
这是按范数绝对收敛的 $\mathcal A$ 元素。
设 $j_0$ 是第一个非零系数位，则其形式首项系数为
$4a_{j_0}^2/d_{j_0}\ne0$，故它不是标量。
每个 dyadic gauge 只改变有限个 $j$ 项，差是真正解析芽。
再次由 R122 §4.2，$Z$ 在全 $H$ 上单射。实系数是当前共同 $W/Z$ 零商的情形，但此处的单射输入不需要相位假设。

准确的有限放大推论如下。设 $N\subset M\subset H^{\oplus d}$ 为闭 $A^{(d)}$ 不变子空间，以 $Q=M\ominus N$ 表示其子商。
由 R88 的强闭包定理，所有实际有界交换子同时保持 $M,N$。
若 $v=(v_1,\ldots,v_d)\in Q$ 且 $S_Qv=0$，则
$$
\phi_v(T)=\sum_{i=1}^d\langle Tv_i,v_i\rangle
$$
满足 $\phi_v(SF)=0$ 对全部 $F\in\mathcal A$：
$S^{(d)}v\in N$，而 $F^{(d)}N\subset N$。
因此只要 $S$ 全 $H$ 单射，
$$
\boxed{
v\in\ker S_Q,\quad
v_i\in\operatorname{Dom}r^{\mathcal N}\ (1\le i\le d),\quad r>9
\quad\Longrightarrow\quad v=0.
}
\tag{7.3}
$$

移去固定有限头后的实际尾模型仍满足 §1 的全部输入：$\eta_j$ 只移到更高位，(1.4) 的衰减界仍有效，尾常函数及尾对合具有同样的循环性与对称性。因此 R208 在其实际尾空间中应用同一证明。

对 R208 的 $Q=L/N$，若 $Q\ne0$ 且 $Z_Q=0$，则每个非零正交代表都必须在某个分量上违反所有统一的 $r>9$ 次数指数域条件。
特别该商没有非零有限-chaos正交代表。
这条结论只用有界 $Z$，没有把商正交投影作用到任意未知的未界第一行域。

同样，若某个 $A$ 不变 $M$ 上 $\overline{SM}\ne M$，则
$M\ominus\overline{SM}$ 中不存在非零的上述指数次数向量。
这不是说该正交差空间对 $A$ 不变；推论来自正常正向量态，而不是从循环性直接推出。

## 8. 与现有缺口的区别

本稿的分解是一个有明确正则性条件的正常泛函分解。不能据此宣称每个正常泛函都能写成 (0.2)，也不能宣称任意有限秩状态满足这一条件。对一般 $x\in H$，次数分量可以衰减得任意慢，$\sum_p r^{2p}\|P_px\|^2$ 可以对每个 $r>1$ 发散。

本稿也不需要位尾快衰减。一个第一 chaos 向量的系数可以遍及所有高位并任意慢地平方可和；其次数仍只有一，所以 (7.3) 的障碍仍然适用。这与低头柱投影测试所得到的指数位尾下界是不同的限制。

实际 carry 在 §3 全部按算子范数支付；图域在 §4 由有限柱初始算子的闭包支付；迹类极限在 §5 按绝对收敛支付。没有使用未经证明的“纯模型核在小扰动下连续”，没有假设湮灭理想在 UHF 左乘下稳定，也没有把不同 gauge 的目标子空间并在一起。

剩余目标依然是一般 Haar-normal 正湮灭者、一般慢符号在未知不变子商上的核与范围，以及普通 Hilbert 不变子空间问题。


## 9. 全部 R16 收敛乘积及任意相位的有限正状态

本节把指数矩假设核验在一个已有的具体循环向量类上，不对任意有限秩状态增加结论。

设 $h$ 是 R16 的非零收敛归一化乘积，写为
$$
h=\bigotimes_{j\ge0}(\mu_j1+\nu_j\chi_j),
\qquad |\mu_j|^2+|\nu_j|^2=1,
\qquad \sum_j|\nu_j|^2<\infty.
\tag{9.1}
$$
局部常数相位按该乘积的收敛约定选择；允许另乘一个非零全局标量。
若有任意有限前缀，也可以先将它单独保留。

对局部截断 $h_m$，Walsh 正交性给准确恒等式
$$
\|r^{\mathcal N}h_m\|^2
=\prod_{j<m}\bigl(|\mu_j|^2+r^2|\nu_j|^2\bigr)
=\prod_{j<m}\bigl(1+(r^2-1)|\nu_j|^2\bigr).
\tag{9.2}
$$
对任意固定 $r>1$，右侧被
$$
\exp\!\left((r^2-1)\sum_j|\nu_j|^2\right)
\tag{9.3}
$$
一致控制。因为 $h_m\to h$ 于 $H$，每个固定次数投影满足
$P_ph_m\to P_ph$。先对有限次数求和再用 (9.2)—(9.3)，得到
$$
\boxed{
h\in\operatorname{Dom}r^{\mathcal N},\qquad
\|r^{\mathcal N}h\|^2
\le\exp\!\left((r^2-1)\sum_j|\nu_j|^2\right)
\quad(r>1).
}
\tag{9.4}
$$
也可从各 Walsh 系数直接使用非负项乘积求和得到同一结论。若有限前缀占据 $d$ 位，则其次数至多 $d$，只需把右侧乘以
$r^{2d}$ 及该前缀的范数平方。没有要求各乘积的局部相位彼此相同。

因此任意有限个这样的 R16 乘积所张成的空间，都包含在每个
$\operatorname{Dom}r^{\mathcal N}$ 中。若正有限秩 $\rho$ 的范围包含于这个有限线性张成，则 (0.1) 对每个 $r>1$ 有限，§6 排除其非零地湮灭 $S\mathcal A$。
这里允许不同乘积之间任意相对复相位，不需要另加相对虚部差的可和性条件。

特别，任意复杂第一 chaos
$$
v=v_*+\sum_j b_j\chi_j,\qquad b\in\ell^2,
$$
的点态指数 $e^v$ 属于该范围。其第 $j$ 位归一化因子为
$$
\frac{e^{b_j\chi_j}}{\sqrt{\cosh(2\operatorname{Re}b_j)}}
=\mu_j1+\nu_j\chi_j,
$$
$$
\mu_j=\frac{\cosh b_j}{\sqrt{\cosh(2\operatorname{Re}b_j)}},
\qquad
\nu_j=\frac{\sinh b_j}{\sqrt{\cosh(2\operatorname{Re}b_j)}}.
\tag{9.5}
$$
有 $|\mu_j|^2+|\nu_j|^2=1$；对充分高位，
$|\nu_j|^2\le C|b_j|^2$，故 (9.1) 成立。前面有限位单独保留。
原未归一化乘积的 $L^2$ 范数由
$\prod_j\cosh(2\operatorname{Re}b_j)<\infty$ 控制，归一化只改全局常数。
所以任意有限个 $e^{v_\ell}$ 的有限线性组合，以及支撑在该张成上的任意正有限秩状态，也满足本稿的排除结论。
