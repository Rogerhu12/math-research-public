# R1175 — 从原全局连接有限重建完整 43 维 Frobenius

日期：2026-11-28  
会话：Astra-serre-24b8836b-20261126  
状态：已证明；本篇只作纸面推导，没有执行数学程序。

## 1. 这次支付的输入

固定 $p>37$。使用 [R1149](R1149-original-relative-Hodge-section-and-central-connection.md) 的原 Hodge frame、原两个 Eisenstein 连接形式、原三个 pairing 和完整
$$
\lambda_\infty=\frac{21(1+p^4)}{11}.
$$
相应 rank-$43$ filtered connection 的实际 overconvergent/log Frobenius，以及它与原 moment tower 的识别，已经由
[R1150](R1150-original-relative-log-Frobenius-and-crystalline-identification.md)
证明。本篇不再把这些列为假设或重新证明。

**定理。** 存在一个只使用上述原有理连接、椭圆曲线的 pure coefficient crystal 和有限线性同余的算法。对每个 $p>37$、每个给定精度 $n$，它在有限步内确定原全部 Frobenius 矩阵模 $p^n$。因此，对任何给定的 good、未分歧、可计算提升，也能有限读取原
$$
(X,Y,T;Z_0,Z_2,Z_4)\pmod {p^n}.
\tag{1175.1}
$$
算法没有把 $\gamma_{5,\infty}$ 的未知 $p$-进数值或任何原中央 Frobenius 条目作为输入。它保留最低 $\lambda_\infty XT'$ 修正、ordered 群律、实际 Frobenius lift 的运输和全部 descent。

这里的“有限”有可检查的停止条件：在一个明确的、线性增长的有理极阶界内建立有限候选树；当固定精度投影成为单点时停止。下面证明真解始终在树中，并证明这个停止条件必在有限深度发生。没有把“唯一存在”直接当成可计算性，也不承诺一个小的运行时间或一致的精度上界。

本篇没有运行此算法、给某个新素数的数值输出或证明 (1175.1) 的某个目标组合非零。主目标及全局/whole-disc 排除继续。

## 2. 原最低中心同时锁定 Tate 常数

按原定义
$$
\begin{aligned}
V&=\operatorname{Sym}^4H(1)\oplus
   \operatorname{Sym}^8H(1)\oplus\mathbb Q_p(5),\\
Z&=\operatorname{Sym}^{12}H(2)\oplus
   \operatorname{Sym}^8H(4)\oplus
   \operatorname{Sym}^4H(6),\\
b((x,y,t),(x',y',t'))
 &=\bigl(\Pi_0(x,y'),\,\Pi_2(x,y'),\,
                \Pi_4(x,y')+\lambda_\infty xt'\bigr).
\end{aligned}
$$
在 $W=\mathbb Q_p\oplus V\oplus Z$ 上，原 faithful representation 是
$$
R(v,z)=
\begin{pmatrix}
1&0&0\\
v&I&0\\
z&b(v,-)&I
\end{pmatrix}.
\tag{1175.2}
$$
注意这个矩阵对 $(v,z)$ **线性**，虽然原群乘法有二次项。

记原连接一形式为 $\alpha=(\alpha_4,\alpha_8,0)$，
pure coefficient Frobenius 为 $\Phi_{\rm c}$，并置
$\alpha'=\Phi_{\rm c}\phi^*\alpha$。
R1150 (1150.4) 给完整的线性系统
$$
\begin{aligned}
\nabla_{\rm c}u_V&=\alpha'-\alpha,\\
\nabla_{\rm c}u_Z&=b(u_V,\alpha')-b(\alpha,u_V),\\
\Phi&=R(u_V,u_Z)\Phi_{\rm c}.
\end{aligned}
\tag{1175.3}
$$

设同一原模叠上有两组 overconvergent 解，pure coefficient map 和原群结构相同。由 R1150 (1150.6) 的
$H^0_{\rm rig}(\operatorname{Sym}^dH(t))=0$，
$$
\Delta u_4=\Delta u_8=0,\qquad
\Delta u_5=c\in\mathbb Q_p.
$$
前两中央差水平。最低中央差则满足
$$
\nabla_{\rm c}\Delta u_{Z,4}
     =-\lambda_\infty c\,\alpha_4.
\tag{1175.4}
$$
在原 cusp coinvariant 中，右端的留数是
$$
-\lambda_\infty c\,v_4^\infty f_1^4\tau_1^6,\qquad
v_4^\infty=\frac{1-p^4}{252}\ne0.
$$
R1150 的 residue 同构说明 $\alpha_4$ 在这一 twist 的
$H^1_{\rm rig}$ 中非零。因此 (1175.4) 有全局 primitive
迫使 $c=0$；随后三个中心的 $H^0=0$ 消去全部中央差。

所以同一原连接和 pure coefficient Frobenius **唯一决定整组**
$\Phi$，包括原 Tate-five 常数。这个结论不是删除该常数：
恰是原正号 $\lambda_\infty XT'$ 的全局 residue 检测了它。
若删掉这个最低修正，以上唯一性证明便不成立。

## 3. 一个具有明确整基和三个分离边界点的坐标

使用 Legendre 曲线
$$
E_t:\quad y^2=x(x-1)(x-t),\qquad
U=\mathbb P^1_{\mathbb Z_p}\setminus\{0,1,\infty\},
\qquad \phi(t)=t^p.
\tag{1175.5}
$$
原 $43$ 维对象中的所有 $H$ 次数都是偶数，故 $[-1]$
作用平凡；它在这个 full level-two chart 上是真正的向量丛。
最后仍施加第 7 节的实际 $S_3$ descent，不以任意一份
Legendre 解替换原模叠上的解。

取
$$
\omega=\frac{dx}{2y},\qquad \eta=x\omega.
$$
它们在 good locus 上是整 de Rham 基。以下也经原
$\nu$ 和 Tate pairing 用于 $H$；该转换不改连接矩阵。
对同一函数作 de Rham reduction，得到
$$
\nabla(\omega,\eta)=(\omega,\eta)N_H\,dt,\qquad
N_H=
\begin{pmatrix}
-\dfrac1{2(t-1)}&-\dfrac1{2(t-1)}\\[4pt]
 \dfrac1{2t(t-1)}&\dfrac1{2(t-1)}
\end{pmatrix}.
\tag{1175.6}
$$
例如
$$
d\!\left(\frac{y}{x-t}\right)
=\left((x-t)+\frac{t(1-t)}{x-t}\right)\omega
$$
给第一列；$x/(x-t)=1+t/(x-t)$ 给第二列。两个有限
residue 都幂零。此处所用 $\eta$ 是未平移的 $x\omega$；
若使用短模型基，须保其明确的三角换基。

短模型的系数为
$$
A=-\frac{t^2-t+1}{3},\qquad
B=\frac{-2t^3+3t^2+3t-2}{27}.
$$
代 R1149 的原 $\alpha_4,\alpha_8$，有
$$
K_\omega=\frac{dt}{2t(t-1)},\quad
E_6=864B,\quad E_{10}=-41472AB.
$$
所以完整原矩阵 $N$ 在
$\mathbb Z_p[t,t^{-1},(t-1)^{-1}]$ 内，且在 $0,1$ 至多
简单极；连同 (1175.2) 的上、下 flag，其 residues 幂零。
这用了全部原 Tate 和中央项，没有另取一个指数较小的替代连接。

在 $\infty$ 处令 $s=t^{-1}$。变换
$x=tX,\ y=t^{3/2}Y$ 把曲线变成 $E_s$。
在二次扩张上
$$
\omega_t=t^{-1/2}\omega_s,\qquad
\eta_t=t^{1/2}\eta_s.
$$
所有偶次 symmetric powers 中半整数幂消去。
若以 $\omega^{d-k}\eta^k$ 为原 coefficient 基，新的
$s$-chart 基相对旧基的因子为 $t^{d/2-k}$。
Tate 因子不变，原唯一 Hodge section 也随同一个 functor
运输，不产生额外的原 torsor 平移。因此整个 $W$ 有一个
明确对角换基 $W_\infty$，其幂指数在 $[-6,6]$ 内。
在这个基中，$s=0$ 的矩阵就是原 $0$-chart 的矩阵，
因而至多简单极且 residue 幂零。特别
$$
v_p(W_\infty)=v_p(W_\infty^{-1})=0,\qquad
\operatorname{ord}_\infty W_\infty\ge-6,\quad
\operatorname{ord}_\infty W_\infty^{-1}\ge-6.
\tag{1175.7}
$$
这里的 norm 都在 $|t|=|t-1|=1$ 的标准 affinoid 上读取。

## 4. 原整格给全 Gauss 范数界

令 $D=\operatorname{diag}(p^{r_j})$ 是原 Hodge basis 的
weight 矩阵，$0\le r_j\le14$。本节需要的是对**所有几何
剩余点**的整性，不是只对有限个 CM 参考点的整性。

取任意有限未分歧扩域 $F/\mathbb Q_p$，以及任意
$\bar t\in k_F\setminus\{0,1\}$ 的 Teichmüller 提升 $t_0$。
此时 $\phi(t_0)=\sigma(t_0)$。R1147 §14 的原
Fontaine–Laffaille 格、R1149 §12 的唯一 Hodge splitting，
以及 R1150 已付的同一 relative associatedness，给
$$
\Phi(t_0)D\in\operatorname{GL}_{43}(\mathcal O_F).
\tag{1175.8}
$$
这是原给定的格；没有一个未知的 $p$-power index。
对 pure coefficient 对象同样成立。

由此在整个标准 affinoid 上
$$
\boxed{\quad
v_p(\Phi)\ge-14,\qquad v_p(\Phi^{-1})\ge0.
\quad}
\tag{1175.9}
$$
详细地，先因 overconvergence 知每个条目的 Gauss norm
有限。若 $p^{14}\Phi$ 或 $\Phi^{-1}$ 有负 Gauss 估值，
除以其最小 $p$ 次后，取非零的 mod-$p$ 有理函数。
它在 $U_{\overline{\mathbb F}_p}$ 某个闭点非零；
该点在某个有限域上定义。对应 Teichmüller 点违背
(1175.8)。这个论证明确使用任意有限未分歧扩域。

令
$$
\Psi=p^{14}\Phi.
$$
则
$$
v_p(\Psi)\ge0,\qquad
v_p(\Psi^{-1})\ge-14,\qquad v_p(N)\ge0.
\tag{1175.10}
$$
对 $\infty$ 的 (1175.7) 基变换也保持这些界。
乘以 $p^{14}$ 仍是同一连接上的可逆 Frobenius structure，
所以可以直接把 $\Psi$ 送入下节的收敛定理。

## 5. 明确的线性极阶界

使用 Kedlaya–Tuitman 的 *Effective convergence bounds for
Frobenius structures on connections*，Theorem 2.1、
Lemmas 2.2–2.5 和 Corollary 2.6。[来源 1]
它的假设在这里逐项成立：底未分歧，$0,1,\infty$ 的
reduction 两两不同，每处有明确的 simple-pole 基，
exponents 全为零，且 R1150 给真正 overconvergent Frobenius。

该定理中的 Taylor 下界可用
$$
f(i)\ge-14\lfloor\log_p i\rfloor,\qquad c=0.
\tag{1175.11}
$$
因 $p\ge41$，对于 $i\ge1$ 有
$$
14\lfloor\log_p i\rfloor\le i/2.
$$
确实若 $p^k\le i$，则 $28k\le p^k$，由 $k=1$
及归纳即得。因此该定理的 $g(m)$ 不超过 $2m$。
在 $1$ 处，$\Psi\bmod p^m$ 的极阶至多 $2pm$；
在 $0$ 处无负 Laurent 项。在 $\infty$ 的 log 基中同样
无负项；返回原基时 Corollary 2.6 和 (1175.7) 至多增加
$6(p+1)$ 的极阶，不损失 $p$-进精度。

故以下单一的、刻意放宽的界适用于原全部条目：
$$
\boxed{\qquad D(m)=2pm+6(p+1).\qquad}
\tag{1175.12}
$$
模 $p^m$，每个条目都有在 $0,1,\infty$ 的极阶均不超过
$D(m)$ 的有理代表。对 pure coefficient Frobenius 也成立。

这里读取的是该定理证明中实际的 Laurent 尾估计：
改变到以奇点为中心的 Frobenius lift 后，再用
$p^iu^i\Phi'\sigma'(\Delta^{(i)})$ 返回；超过所列 cutoff
的项都在 $p^m$ 中。不能把“任意有理近似”解释为允许
在同一剩余盘内另放一个未知极点。所得到的 bound 正是
在原三个点的部分分式次数界。

## 6. 有限有理模型及无限分支为何仍 overconvergent

令
$$
\mathscr A=\mathbb Z_p[t,t^{-1},(t-1)^{-1}],
$$
并用下列唯一部分分式规范：
$$
c_0+\sum_{j\ge1}c_jt^j
       +\sum_{j\ge1}a_jt^{-j}
       +\sum_{j\ge1}b_j(t-1)^{-j}.
\tag{1175.13}
$$
$p$-adic completion 中系数趋零。这些 basis elements 的
Gauss norm 都是一；不同极的主部及 polynomial part
模 $p$ 线性独立，所以系数最小估值就是 Gauss 估值。

对每个 $m$，令 $L_m$ 为 (1175.13) 中三个次数均
$\le D(m)$、系数属于 $\mathbb Z/p^m$ 的有限模。
一个 level-$m$ 矩阵候选属于 $\operatorname{Mat}_{43}(L_m)$。
相邻两层须逐个部分分式系数模 $p^m$ 相同；
高于 $D(m)$ 的新系数须在模 $p^m$ 下为零。
不要只比较某几个点的值。

真 $\Psi$ 的规范约化给所有层的一条相容分支。
反过来，任一相容无限分支给一个 completed matrix，
而 (1175.12) 迫使其次数 $j$ 的系数估值至少
$$
\frac{j-6(p+1)}{2p}-1.
\tag{1175.14}
$$
因此它在一个严格大于标准 affinoid 的邻域上收敛，
确属 $\mathscr A^\dagger\otimes\mathbb Q_p$。
这一步不能用任意的多项式或指数次数界代替：
我们需要这里实际证明的**线性**界。

导数、乘原有理连接矩阵、Frobenius pullback 及下一节
的 Taylor/descent 操作在这些收敛环上连续。故在每个
有限层成立的相容线性同余，沿无限分支成为准确的
水平、原群结构和 descent 等式。

## 7. 每层真正施加的线性同余

水平条件准确为
$$
N\Psi+\frac{d\Psi}{dt}
       =pt^{p-1}\Psi\,\phi(N).
\tag{1175.15}
$$
原 $N$ 已知且整，因此在有限 $L_m$ 中清除
$t,t-1$ 的分母后是有限线性同余；求导不损失精度。

先假定 $\Phi_{\rm c}=\operatorname{diag}(1,\Phi_V,\Phi_Z)$
已能读到任意有限精度。第 9 节将给独立的有限算法，
所以这不是原扩张数据的 oracle。
设 $\upsilon,\zeta$ 分别为 $\Psi$ 第一列的 $V,Z$ 部分。
原 (1175.2) 的全部 affine 结构恰是
$$
\Psi=
\begin{pmatrix}
p^{14}&0&0\\
\upsilon&p^{14}\Phi_V&0\\
\zeta&b(\upsilon,-)\Phi_V&p^{14}\Phi_Z
\end{pmatrix}.
\tag{1175.16}
$$
这仍是线性同余。需要时把整条等式乘以 $p^{14}$，
使所有已知系数整；逐层提高精度后，极限仍迫使原等式
准确成立。已知 coefficient 矩阵算到模 $p^{m+14}$
足以安全地施加 level-$m$ 的这些等式。

最后施加实际 full level-two descent。$S_3$ 的两个生成元
$t\mapsto1-t$、$t\mapsto t^{-1}$ 由实际 Legendre
isomorphisms 给出。它们在偶次对象上的 coefficient
换基 $D_g:g^*W\to W$ 是明确的有理矩阵；中间的平方根
仅有 $[-1]$ 歧义，已在原偶次表示上消去。
唯一 Hodge section 与整个 affine/right-action tensor
一并运输。

两种复合 Frobenius lift 在模 $p$ 下相同。由原连接的
Taylor series，构造
$$
\varepsilon_g:\phi^*g^*W\longrightarrow g^*\phi^*W.
$$
实际 descent 方程是同源 maps 的等式
$$
F\circ\phi^*D_g
  =D_g\circ g^*F\circ\varepsilon_g.
\tag{1175.17}
$$
此式对 $\Psi$ 仍线性；$D_g,\varepsilon_g$ 均只由原连接
计算，不用未知 Frobenius。两 lift 的差在 $p\mathscr A$，
$N$ 整，所以 Taylor 第 $i$ 项的估值至少
$i-v_p(i!)$。这给一个明确、可算的有限 cutoff；
所需 coefficient、inverse 和复合均按有限精度的几何级数
在原部分分式环内计算。原 $S_3$ cocycle 关系也保留。

因此本节是有限线性代数，而不是比较“相同 residue”
或任意更换 reference torsor。任一无限分支在原模叠上
给 (1175.3) 的一组真正 overconvergent 解。

## 8. 合法停止条件及终止证明

从 $m=1$ 起，列出本层满足第 7 节同余的全部矩阵候选，
只保留和上一层某个已保留候选相容的边。
这是有限分支的、可逐层构造的树。每个节点只需有限
环上线性消元；亦可使用有限穷举，不假定运行效率。

真解保证每层非空。固定希望输出的矩阵精度 $r$，
在深度 $m\ge r$ 考察所有现存路径的 level-$r$ 投影。
它们是一列有限的、递减的非空集合。

若这些集合永远不成为单点，则至少有一个与真解不同的
level-$r$ 投影存活到任意深度。限制到具有该投影的有限
分支树，由 König 引理取得一条无限分支。
第 6 节的线性 bound 使其 overconvergent，第 7 节使其
成为原全局 (1175.3) 的一组解。第 2 节的唯一性迫使它
等于真解，矛盾。

故算法在某个有限深度发现 singleton，立即输出该值。
此时真解仍在候选中，所以没有“暂时稳定”导致的误停。
不需要从连续两次同值猜测精度已足够，也没有把一个
未知的稳定深度当成输入。

欲得到 $\Phi\bmod p^n$，取 $r=n+14$，输出
$\Psi\bmod p^{n+14}$ 后除以 $p^{14}$。第一列的整性来自
原格；因此原 $(u_V,u_Z)\bmod p^n$ 同时被准确恢复。
整个停止证据可以用同一有限线性系统的候选差在目标精度的投影为零模
来核验，不需要保存所有可重算的候选树。

## 9. Pure coefficient 输入本身也能有限取得

这里不用在整个模参数上假设一个未证明的相对数值算法。

先在 $t=-1$ 的 good 曲线上计算 pure $H^1_{\rm cris}$ 的
$p$-Frobenius 矩阵。因为 $(-1)^p=-1$，它正是所选
$\phi(t)=t^p$ 在此 fibre 的 map。
Kedlaya 的原 Monsky–Washnitzer 算法给任意有限精度：
使用 $Q(x)=x(x-1)(x+1)$，在
$\mathbb Z_p[x,y,y^{-1}]/(y^2-Q)$ 的 weak completion 中取
$$
\phi(y)=y^p
 \left(1+\frac{Q(x^p)-Q(x)^p}{Q(x)^p}\right)^{1/2},
$$
再对 $\omega,x\omega$ reduction。其 §3 的两个 denominator
lemmas 和 §4 的 finite precision algorithm 给已知尾界，
适用于 ordinary 和 supersingular 两种情形。[来源 2]
这里读的是**矩阵**，并非仅从点数猜其 conjugacy class。

经原 polarization、$\nu$、Tate generator 及 symmetric
power functors，取得全部 $\Phi_{\rm c}(-1)$ 的有限精度。
所有 pure 数据及其 log 连接具有第 3–5 节相同的范数和
极阶界。

于是再运行第 6–8 节的同一种有限树，只对 pure block
施加水平等式和已知 anchor 值
$\Psi_{\rm c}(-1)=p^{14}\Phi_{\rm c}(-1)$。
这时唯一性不需第 2 节：两个 horizontal matrices 在
good 点相同，微分方程递推使其完整 Taylor series 相同；
标准 affinoid 连通，解析恒等定理使它们处处相同。
因此该 pure 有限树对每个请求精度同样终止。

完整算法先作这个 pure 步，再作第 7–8 节的原扩张步；
二者都是已证明终止的有限过程。没有输入原 $\gamma_5$
或 $Z_r$ 的任何有限位。

## 10. 回到实际曲线、半线性及 whole-disc 的准确范围

对任意给定的 good 未分歧曲线，可先在有限未分歧扩域
分裂 $E[2]$，选同一个原标记和 Legendre 坐标。
三个 roots 的差都是单位，所以所需平方根也至多需要
有限未分歧扩张。偶次结构随后按 (1175.17) 下降；
没有抹掉原 twist 或实际 Frobenius $\sigma$。

若实际点的 lift 满足 $\phi(t_0)\ne\sigma(t_0)$，
二者之差在 $p\mathcal O_F$ 中。先用完整原连接的
Taylor map 将 source fibre 从 $\phi(t_0)$ 运输到
$\sigma(t_0)$，再读取 crystalline Frobenius。
与第 7 节同样的阶乘估值给任意请求精度的有限 cutoff。
不能把标准 lift 在一个任意非 Teichmüller 点的求值，
直接冒称该点的 arithmetic Frobenius。

从 (1175.16) 的第一列恢复原 ordered $u$；
若需要 BCH 中心，才按原
$z_{\rm BCH}=u_Z-\tfrac12 b(u_V,u_V)$ 转换。
最低 Tate cross term 在这个转换和全部 quotient
运输中均仍在。之后才能应用原 finite Cartan $q_I$
及 R1149/R1171 的实际小盘增量。

因而 R1170–R1174 的另一路 all-SS 重建，不再是读取
原中央常数的唯一入口；本篇给了包括最低 Tate 槽的
独立、可终止全局算法。一般辅助同源的 ordinary source
仍可继续用于更短的符号公式和实际非零性，不必等它
完成才拥有有限读取方法。

可计算任意精度并不等于已经排除 whole discs，
也不等于对所有 $p$ 给出某个目标 nonvanishing。
原 global label subtraction、七个 Bernoulli 退化分支、
全 $N_{\rm ns}$ 及 open.md 的其余目标都继续保留。
本篇没有新增 vanishing 假设，未将有限算法当成
Serre 一致性主目标的完成证明。

## 11. 亲读的 primary 与本篇自证部分

1. Kiran S. Kedlaya、Jan Tuitman，
   *Effective convergence bounds for Frobenius structures on connections*，
   Rendiconti del Seminario Matematico della Università di Padova
   **128** (2012), 7–16，
   [作者全文](https://arxiv.org/pdf/1111.0136)，
   [正式出版页](https://ems.press/journals/rsmup/articles/11880)，
   DOI 10.4171/RSMUP/128-2。
   已亲读 Theorem 2.1、其全部证明、Lemmas 2.2–2.5 和
   Corollary 2.6。本篇的已知原格范数、$D(m)$、候选树及
   终止论证均在上文另给，不把文献的存在断言当数值输出。

2. Kiran S. Kedlaya，
   *Counting points on hyperelliptic curves using Monsky–Washnitzer cohomology*，
   Journal of the Ramanujan Mathematical Society **16** (2001), 323–338，
   [作者全文](https://arxiv.org/pdf/math/0105031)。
   已亲读 §3 的实际 Frobenius、de Rham reduction、
   Lemmas 2–3 的 denominator bound 和 §4 的算法。
   本篇仅用其在一个明确 good fibre 上的有限矩阵计算；
   pure family 的全局重建另由本篇有限树证明。

原 source、格与 associatedness 沿 R1147、R1149–R1150
已登记结论。新增唯一性、实际 Legendre 三边界坐标、
全几何点的 Gauss bound、线性极阶界、两个有限候选过程、
半线性/实际 lift 运输及合法停止条件如上。
