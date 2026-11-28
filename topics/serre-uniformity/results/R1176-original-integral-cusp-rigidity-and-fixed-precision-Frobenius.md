# R1176 — 原三个尖点的整约束与固定精度唯一 Frobenius

日期：2026-11-28  
会话：Astra-serre-24b8836b-20261126  
状态：纸面证明；没有数学程序执行。

## 1. 将完整扩张的读取缩成一个指定精度线性系统

沿用 [R1175](R1175-original-global-connection-finite-Frobenius-reconstruction.md)
的原 $43$ 维连接、Legendre 基、ordered 群和全部 Tate 归一。
该文已给全局有限读取的终止证明。
本篇增加的是一个更强的整唯一性及直接有限候选空间。

**定理。** 固定 $p>37$ 和 $n\ge1$。给定 pure coefficient
Frobenius 在明确精度 $n+28$ 的值后，原扩张的
$$
u=(X,Y,T;Z_0,Z_2,Z_4)\pmod {p^n}
$$
由**一个**有限仿射线性同余系统唯一确定。
该系统的未知函数只需在 $t=1$ 有极，并有次数至多六的
polynomial part；其最大极阶从一个已知 Frobenius-lift
增量直接读出。三个尖点的 log 正则性、原全连接水平式
和实际 $S_3$ descent 都在系统中施加。

因此，原扩张部分不再需要等待 R1175 候选树的某个未知
提升深度。Pure coefficient 数据仍可用 R1175 §9 的已证
有限算法取得；本篇不把该子算法的内部运行长度另称为
已经有一个小的统一上界。

这不是目标 nonvanishing 的证明，也没有执行任何
指定素数的数值读取。

## 2. 小权原 log 系数在模 p 下已无水平全局截面

令 $\overline{\mathcal M}/\mathbb Z_p$ 为带 cusp 的原
compactified modular stack，$\omega$ 为其 Hodge line。
$p>3$ 时它是 tame stack；$\omega^{12}$ 的 cusp section
给正次数，故任意 $d>0$ 有
$$
H^0(\overline{\mathcal M}_{\mathbb F_p},\omega^{-d})=0.
\tag{1176.1}
$$
也可由原 weighted Weierstrass presentation 的负次数
homogeneous function 为零直接核准。

原 log Gauss–Manin bundle $H$ 的几何 Hodge graded lines 为
$\omega,\omega^{-1}$；Tate twists 对这些底上的线束不作改变。
其 Kodaira–Spencer map 是同一个原同构
$$
\omega^2\simeq
\Omega^1_{\overline{\mathcal M}/\mathbb Z_p}(\log\mathrm{cusp}).
$$
这可在 R1175 (1175.6) 的两个 cusp frame 和原
$K_\omega=dt/(2t(t-1))$ 上直接检验，再作 tame descent。

对于 $\operatorname{Sym}^dH(t_0)$，以 $i$ 表示第二条
Hodge graded line 的次数，
$$
\operatorname{gr}_i\simeq\omega^{d-2i},\qquad 0\le i\le d.
$$
从 $\operatorname{gr}_i$ 到
$\operatorname{gr}_{i+1}\otimes\Omega^1(\log)$ 的 Higgs map
是 $d-i$ 乘上述同构。
设 $s$ 是一条全局 log 正则且水平的截面。
其最末 graded component 落在 $\omega^{-d}$，由 (1176.1)
为零。于是若 $s\ne0$，取最高非零 index $i<d$；
水平性投到下一 graded component 给
$(d-i)s_i=0$。
当 $0<d<p$ 时这个系数是单位，矛盾。

所以对本题全部 $d=4,8,12$ 和任意所用 Tate twist，
$$
\boxed{\quad
H^0_{\nabla,\log}
 (\overline{\mathcal M}_{\mathbb F_p},
       \operatorname{Sym}^dH(t_0))=0.
\quad}
\tag{1176.2}
$$
逐次除以 $p$ 给相同的模 $p^n$ 结论。
这里使用正则 log bundle 的全局截面；
没有声称开曲线的任意 mod-$p$ 水平函数都为常数。

原 $\alpha_4$ 的 log cohomology 类在模 $p$ 下也非零。
因为同一 cusp coinvariant residue 是
$$
v_4^\infty f_1^4\tau_1,\qquad
v_4^\infty=(1-p^4)/252\in\mathbb Z_p^\times.
\tag{1176.3}
$$
正则 log 截面的连接留数属于 coefficient monodromy 的像。
它不能产生 (1176.3) 的 coinvariant。
在 full level-two cusp 两边同乘宽度二，仍是单位。
该论证适用于最低中心所需的 twist $(4,6)$。

## 3. 改用以 t=1 为中心的真实 Frobenius lift

原标准 lift 是
$$
\phi_0(t)=t^p.
$$
它已在 $0,\infty$ 保持 log divisor。只另需一个 lift
$$
\phi_1(t)=1+(t-1)^p,\qquad
d(t)=\phi_1(t)-\phi_0(t)\in p\mathscr A,
\quad
\mathscr A=\mathbb Z_p[t,t^{-1},(t-1)^{-1}].
\tag{1176.4}
$$
在系数上二者都是实际 $\sigma$；不将扩域后的
$\sigma$ 替换为恒等。

令 $\mathcal T_W:\phi_1^*W\to\phi_0^*W$ 为完整原连接的
Taylor map，$\mathcal T_{\rm c}$ 为 pure coefficient 版本。
若 $\Delta^{(i)}$ 是 $\nabla_{\partial_t}^i/i!$ 在原基中的
矩阵，则
$$
\mathcal T_W
 =\sum_{i\ge0}d(t)^i\,\phi_0(\Delta^{(i)}),
\qquad
\Phi_1=\Phi_0\mathcal T_W.
\tag{1176.5}
$$
这是 R1175 使用的同一 Frobenius-change convention，
与 Kedlaya–Tuitman Lemma 2.4 相同。

写 $C_{\rm c}=\Phi_{\rm c}D$，
$D=\operatorname{diag}(p^{r_j})$，$0\le r_j\le14$。
R1175 §4 的所有几何 Teichmüller 点论证实际上给
$$
C=\Phi_0D,\ C_{\rm c}\in
       \operatorname{GL}_{43}(\widehat{\mathscr A}).
\tag{1176.6}
$$
这里及下文的 hat 表示标准 affinoid 的 $p$-completion；
所有实际函数另已 overconvergent。

原 $N$ 整、满足 Griffiths 降阶一，故第 $i$ 个 Taylor
项在 $D^{-1}\mathcal T_WD$ 的 $(a,b)$ entry 中估值至少
$$
i-v_p(i!)-(r_a-r_b).
\tag{1176.7}
$$
若 $r_a-r_b>i$，该 entry 本来为零。
$i\le14$ 时 (1176.7) 非负；
$i\ge15$ 时由 $p>37$ 严格为正。
逆向 Taylor map 同样如此。因此
$$
D^{-1}\mathcal T_WD,\quad
D^{-1}\mathcal T_{\rm c}D
       \in\operatorname{GL}_{43}(\widehat{\mathscr A}).
\tag{1176.8}
$$
这在 rational coefficient frame 的整 Gauss norm 上成立；
没有另假定一个未付的 integral log Fontaine–Laffaille
essential-surjectivity theorem。

定义已知群增量 $\delta_1$：
$$
\boxed{\quad
R(\delta_1)
 =\Phi_{\rm c}\mathcal T_W
       \mathcal T_{\rm c}^{-1}\Phi_{\rm c}^{-1}.
\quad}
\tag{1176.9}
$$
Taylor map 保原 affine hyperplane、right action 和全部
tensor，故右端确在原 $R(G)$ 内。
由 (1176.6)–(1176.8)，右端及其逆均整；
其第一列给 $\delta_1\in G(\widehat{\mathscr A})$。
又因原 Tate-five 连接槽为零，
$$
(\delta_1)_T=0.
\tag{1176.10}
$$
整个增量只用 $N$ 和 pure coefficient Frobenius，
不含任何待求的原 $u$。

按原 ordered 群律，换 lift 后的参数准确为
$$
\boxed{\quad
u_1=u\star\delta_1,\qquad
(u_1)_V=u_V+(\delta_1)_V,\quad
(u_1)_Z=u_Z+(\delta_1)_Z+b(u_V,(\delta_1)_V).
\quad}
\tag{1176.11}
$$
所以这个变换对未知 $u$ 是仿射线性的。
不能把最后的 cross term 删掉。

## 4. 真解在三个 cusp frame 中确整且 log 正则

R1150 已证明实际原 Frobenius 的 log 延拓和 lift 相容性。
在 $t=0$ 的原基、在 $t=1$ 使用 $\phi_1$ 的原基、
以及 R1175 (1175.7) 的 $s=1/t$ 基中，原 $u,u_1,u_\infty$
各自是没有负次项的形式级数。

这些级数还确实整。
标准 frame 中 $u$ 是 $\Phi_0$ 的第一列，而该列的
$D$ 因子为一，所以 (1176.6) 给其整 Gauss norm。
式 (1176.11) 与整 $\delta_1$ 给 $u_1$ 同样的范数。
$\infty$ 的换基是 Gauss 整且可逆的 $W_\infty$，
所以 $u_\infty$ 也一样。

一个 Gauss 整、在指定 cusp 无主部的 dagger 函数，
其该 cusp 的 Taylor 系数都是整的：
在 R1175 (1175.13) 的整部分分式中，去掉此 cusp 的
负次部分；其它单位距离的极点项用整二项式展开，
其系数逐项 $p$-进收敛。
$\infty$ 先作上述明确换基再用同一论证。
因此原三份 log 正则性可以直接作为模 $p^n$ 的约束，
真解不会因为候选空间过小而丢失。

这个整性证明没有只查看 $\mathbb F_p$ 或
$\mathbb F_{p^2}$ 的有限个 CM 点，也没有把在一个
annulus 上有理正则当成整正则。

## 5. 已知主部给出有限未知空间

在模 $p^n$ 的规范部分分式中，令 $M_V$ 为
$(\delta_1)_V$ 在 $t=1$ 的最大极阶，$M_Z$ 为
$(\delta_1)_Z$ 的相应最大极阶；无极时记为零。
它们是**已知有限数**，由 (1176.9) 的有限精度结果读出。

真 $u$ 在 $0$ 正则，故没有 $t^{-j}$ 部分。
在 $\infty$ 的原 coefficient component
$\omega^{d-k}\eta^k$ 中，(1175.7) 给
$$
(u_\infty)_k=t^{k-d/2}u_k.
$$
所以 $u$ 的每个 polynomial part 次数至多六；
每一 component 仍另施加这条准确的正则性，
而非只用这个统一放宽界。

在 $t=1$，(1176.11) 的 abelian 部分说明
$u_V$ 的主部是 $-(\delta_1)_V$ 的主部，因此极阶
至多 $M_V$。
中央部分的主部是
$$
-\operatorname{PP}_1\bigl((\delta_1)_Z+
                    b(u_V,(\delta_1)_V)\bigr).
\tag{1176.12}
$$
$b$ 的 coefficient 在当前基中是原常数配对和
$\lambda_\infty$；它不增加 $t=1$ 的极阶。
于是令
$$
M_C=\max\{M_Z,2M_V\},
$$
就得到合法的完整候选空间
$$
\begin{aligned}
u_V&\in\mathcal L(M_V)^{15},\\
u_Z&\in\mathcal L(M_C)^{27},\\
\mathcal L(M)&=
 \operatorname{span}_{\mathbb Z/p^n}
 \{1,t,\ldots,t^6,(t-1)^{-1},\ldots,(t-1)^{-M}\}.
\end{aligned}
\tag{1176.13}
$$
总未知数不超过 $15(7+M_V)+27(7+M_C)$。
Tate component 在 $\infty$ 的权为零，故最后会限制成常数。

(1176.12) 中仍保全部 ordered cross term。
其最低 $\lambda_\infty u_X(\delta_1)_T$ 在这一次增量中
为零的原因是已证的 (1176.10)；这不从原整个对象删除
$\lambda_\infty XT'$，尤其不从下面的水平方程删除它。

## 6. 在这个空间内施加完整原方程

未知 $u$ 必须满足 R1175 的原系统
$$
\begin{aligned}
\nabla_{\rm c}u_V&=\alpha'-\alpha,\\
\nabla_{\rm c}u_Z&=b(u_V,\alpha')-b(\alpha,u_V),
\qquad \alpha'=\Phi_{\rm c}\phi_0^*\alpha .
\end{aligned}
\tag{1176.14}
$$
另外施加：

1. $\infty$ 处每一 component 的准确权重正则性；
2. $t=1$ 处 (1176.11) 的全部负 Laurent 系数为零；
3. 原 full level-two 标记的实际 $S_3$ descent。

这全是仿射线性同余。原 $\alpha'$ 确整：
$\alpha_d$ 在最高 Hodge 线，连同 Tate-one 的 filtration
weight 为 $-1$，而 $\phi_0^*(dt)$ 带一个 $p$；
$\Phi_{\rm c}$ 的同一 divided Frobenius 正好消去这一个
分母。也可从已证整真解的第一行方程直接核准其整性。
三中央右端因此也整。

为明确 descent 不含未知 oracle，使用 R1175
(1175.17) 的实际 maps。
令 $D_g:g^*W\to W$ 为原 coefficient 换基，
$\varepsilon_g$ 和 $\varepsilon_{{\rm c},g}$ 分别为完整及
pure 连接的两个复合 lift 之间的 Taylor map。
定义已知增量
$$
R(\delta_g)
 =D_g\,g^*\Phi_{\rm c}\,
    \varepsilon_g\varepsilon_{{\rm c},g}^{-1}
        (g^*\Phi_{\rm c})^{-1}D_g^{-1}.
\tag{1176.15}
$$
于是原 descent 等式准确等价于
$$
u=(D_g\cdot g^*u)\star\delta_g.
\tag{1176.16}
$$
其方向由
$F\circ\phi_0^*D_g=D_g\circ g^*F\circ\varepsilon_g$
及 pure 版本相除直接得到。
这些 $\delta_g$ 同样整、Tate 增量为零；
证明与 (1176.6)–(1176.10) 相同，
因为实际 $D_g$ 整、严格保持 filtration，
且两个复合 lift 的差在 $p\widehat{\mathscr A}$ 中。
因此 (1176.16) 对未知 $u$ 是合法的模 $p^n$ 仿射线性式。
所有 finite marking、$\sigma$、完整 shear 及 $S_3$ cocycle
关系都保留。

有限精度的 dagger 函数在规范部分分式环中有有限代表。
把 (1176.13) 代入这些等式，清除 $t,t-1$ 的分母并逐项
比较系数，就得到一个有限矩阵。
在 (1176.12) 中只取真实主部，没有把 regular part
错误地设成零。

## 7. 这个有限矩阵在模 p 下已经列满秩

先在模 $p$ 取两个候选，记差为 $\Delta u$。
第 6 节的非齐次部分相同，所以
$$
\nabla_{\rm c}\Delta u_4=
\nabla_{\rm c}\Delta u_8=0.
$$
在三个 cusp，abelian 增量与未知参数无关，故差的
主部全部消去。它们因而是原 compact log coefficient
bundle 的全局水平截面；由 (1176.2)，
$$
\Delta u_4=\Delta u_8=0.
\tag{1176.17}
$$

Tate 差在所有 cusp 正则，故是 proper base 上的一个
常数 $c$。此时在任何 lift change 或 descent 中，
可能残留的中央差修正都是
$b((0,0,c),\delta_V)=0$，因为原 $b$ 的第一输入只读取
$x,y$，不读取第一输入的 Tate component。
所以三个中央差也成为普通的全局 log coefficient
sections。

原最低水平式仍是
$$
\nabla_{\rm c}\Delta u_{Z,4}
       =-\lambda_\infty c\,\alpha_4 .
\tag{1176.18}
$$
$\lambda_\infty v_4^\infty$ 模 $p$ 是单位。
(1176.3) 的 coinvariant residue 迫使 $c=0$，
随后 (1176.2) 杀掉三个中央差。
因此全部 $\Delta u=0$。

本证明也可完全在 compactified Legendre chart 上做：
其偶次 coefficient 的 Hodge graded lines 为
$\mathcal O_{\mathbb P^1}(d/2-i)$，
最后一条为负次数，Higgs map 仍乘 $d-i$；
三个 cusp 的同一论证给相同消失。
所以这里并未倚赖一个只在 characteristic zero 成立的
descent 后维数计算。

规范部分分式 basis 在 $\mathbb Z/p$ 上线性独立，
故有限矩阵的 homogeneous kernel 为零，亦即列满秩。
因此存在一个可实际找出的方形子矩阵，其 determinant
为 $p$ 单位。
同一个矩阵在 $\mathbb Z/p^n$ 上的 homogeneous kernel
也为零；可用这个单位 minor，或直接逐次除以 $p$ 证明。
真解已由 §4 保证包含在空间内，故有限系统在每一请求
精度恰有一个解。

这给一个固定精度的停止证据：找到单位 minor 并核验
所得解满足全部其余行。它不依赖提高精度后“暂时不再
改变”的经验判断。

## 8. 有限精度账本与原输出

计算 (1176.9) 和 (1176.15) 时，使用
$C_{\rm c}=\Phi_{\rm c}D$ 以及已经归一的
$D^{-1}\mathcal T D$。
这些矩阵及其 inverse 都整，因此所有反除都在已知整
可逆矩阵中完成。Pure coefficient 矩阵给到
$p^{n+28}$ 已足够；不会因未知 $u$ 而要求更多输入位。

Taylor series 可直接使用 (1176.7) 截断。
例如取
$$
I=2(n+42)
$$
并保留 $i<I$，则 $i\ge I$ 时
$$
i-v_p(i!)-14
 \ge \frac{39}{40}i-14\ge n+28 .
$$
这使用 $p\ge41$；估计故意留有余量。
计算每个保留项时，原 $N$ 是已知有理矩阵，可先保留
准确的 factorial 与 $D$ 的分母，再按已证明的非负估值
约化。不得先在模 $p$ 中删除一个有 $p$ 分母的项。

Frobenius substitution 和 $S_3$ substitution 中出现的
分母模 $p$ 都是 $t,t-1$ 的幂乘单位；
有限几何级数给它们模 $p^{n+28}$ 的实际有理代表。
从这些有限代表取 (1176.13) 所需主部，建立第 6 节
的一个模 $p^n$ 线性系统并求唯一解。
这里 $28$ 是明确的安全精度，不是一个另待寻找的参数。

Pure coefficient 数据的计算已经由 R1175 §9 支付。
若以后使用更快的相对椭圆 cohomology 算法，只替换这项
已知输入的实现，不改变本篇整唯一性或原源归一。
本篇没有假定新算法已经运行。

求出的 $u$ 正是原 ordered Frobenius 参数。
读实际未分歧点时仍按 R1175 §10 将所选 lift 的 source
运输到 $\sigma$-fibre；BCH 中心仍是
$u_Z-\tfrac12b(u_V,u_V)$。
原 finite Cartan maps、global torsor subtraction 和
全部七个退化分支要在这之后按各自来源处理。

## 9. 已关闭的门与仍须完成的目标

R1175 的未知深度候选树仍是正确的独立有限算法。
本篇证明在已知 pure coefficient 有限输入后，
原全部 $42$ 个扩张坐标可直接由三个 cusp 的整正则性、
一个已知 centered-lift increment 和固定精度线性代数读取。
最低 Tate-five 常数是系统中被原留数锁定的未知量，
没有外部预填值。

新增的整模 $p$ 唯一性使用
$d\le12<p$、原 Kodaira–Spencer 和
$\lambda_\infty v_4^\infty$ 单位；
不使用 Bernoulli $B_{p-3},B_{p-5},B_{p-7}$ 的非零假设。
所有 source、滤过、原 ordered cross term 和 arithmetic
Frobenius 均保留。

本篇没有证明这些可读取值满足最终需要的非零关系。
原 full $N_{\rm ns}$、所有 global labels、Gaussian/Fermat
实际 joint 条件及 whole-disc 排除继续，主目标仍 OPEN。
全部证明为纸面推导，没有数学程序执行。

来源：R1147 的原整格；R1149–R1150 的原连接、
log 延拓和 associatedness；R1175 的全几何点 Gauss
整性、Legendre 换基及 pure 读取。
Taylor 换 lift 使用 R1175 已亲读并核准的
[Kedlaya–Tuitman Lemma 2.4](https://arxiv.org/pdf/1111.0136)；
本篇的模 $p$ Higgs 消失、整三 cusp 候选空间、单位 minor
及固定精度账本均在上文自证。
