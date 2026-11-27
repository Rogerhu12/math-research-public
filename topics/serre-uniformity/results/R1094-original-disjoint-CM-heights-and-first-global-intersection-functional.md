# R1094. 原 full level 47 的离盘 CM 高度与第一全局高度交数

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；global_route。

**状态：已证明的实际高度输入；尚未计算高度单位。** 令 $X=X_{\rm ns}^+(47)$，$J=\operatorname{Jac}(X)$，$q=4513$，$C_\infty$ 为全部 $23$ 个尖点的和，$y_4,y_3$ 为规范 Cartan 标记的有理 CM 点 $j=1728,0$。保留原除子
$$
u_i=23y_i-C_\infty,\qquad B=q+1-T_q,\qquad D_i=Bu_i.
\tag{1094.1}
$$
这里 $B$ 作用于**实际除子**，并不只指 Jacobian 类。

本文完整证明：可在原整 de Rham 格上选择 Hecke 稳定、各向同性的整 Hodge 补空间 $W$；对任意异于 $47,q$ 的原 Hecke 算子的整数线性组合或乘积 $T$，
$$
h_q^W(D_4,T D_3)\in q^2\mathbb Z_q.
\tag{1094.2}
$$
所有分歧的 $q$-同源目标及其循环重数都保留。原有限 Cartan 角对应也满足 (1094.2)。因此这对原 CM 类的第一全局高度是有限算术交数的准确读数：
$$
\boxed{\quad
q^{-1}h^W([D_4],T[D_3])
 \equiv\sum_{\ell\ne q}
 I_\ell(D_4,T D_3)\,
 \frac{\ell^{q-1}-1}{q}\pmod q.
\quad}
\tag{1094.3}
$$
$I_\ell$ 是**原 $X$ 正则模型的 Néron 修正交数**；在坏素数 $47$ 必须包括完整垂直修正。本式没有把它改成 $j$ 直线交数，没有省去 $B^2$ 的 $q^2$-Hecke 项。

还有两个同高斯域的实际离盘输入：
$$
h_q^W(D_4,T_3D_4)\in q^2\mathbb Z_q,\qquad
h_q^W(D_4,(T_2-1)D_4)\in q^2\mathbb Z_q.
\tag{1094.4}
$$
第二式直接消费旧的原标记恒等式 $(T_2-1)u_4=2u_{16}$，其中 $j(y_{16})=287496$；本条不重做该旧结论。它们不声称 $T_3$ 或 $T_2-1$ 在所有整 Hecke 块上都是单位。

## 1. 原整 Hodge 补空间确实存在

R1067 给 $X$ 在所有 $\ell\ne47$ 的光滑正则好模型。令
$$
H=H^1_{\rm dR}(X/\mathbb Z_q),\qquad
L=H^0(X,\Omega^1).
$$
R1081 在 $q=4513$ 给出的原 Hecke 整序 $\mathbb T$ 是秩 $73$ 的有限 étale $\mathbb Z_q$-代数；$L$ 是秩一自由 $\mathbb T$-模。写
$$
\mathbb T=\prod_\nu\mathcal O_\nu,
$$
每个 $\mathcal O_\nu$ 都是未分歧扩张的整数环。

杯积与原主极化给 $H$ 上完美交替配对；原 Hecke 作用自伴。Hodge 序列
$$
0\longrightarrow L\longrightarrow H
 \longrightarrow L^\vee\longrightarrow0
\tag{1094.5}
$$
在各 $\mathcal O_\nu$ 因子上是秩 $1,2,1$ 的自由模序列。对偶处的 $\mathbb T$ 作用由自伴性给出；有限 étale 代数的迹对偶仍为秩一自由模。因此可取一个 $\mathbb T$-线性截面，令其像为 $W$。

这个 $W$ 自动各向同性。不同幂等因子的杯积为零；同一因子若由 $w$ 生成，则
$$
\langle aw,bw\rangle=\langle w,ab\,w\rangle
=\langle ab\,w,w\rangle
=-\langle w,ab\,w\rangle.
$$
因 $2$ 是单位，上式为零。于是
$$
H=L\oplus W
\tag{1094.6}
$$
是所需的**整**、Hecke 稳定、各向同性补空间。不需要假设整个 $J$ 在 $q$ 普通，也没有把某个有理 unit-root 空间未经验证地当作整直和项。

以下局部论证其实对任何这样的整各向同性补空间都成立。取全局圆分 $q$-进高度，约定
$$
\log_q(q)=0,\qquad
\chi_\ell(\ell)=-\log_q(\ell)\quad(\ell\ne q).
\tag{1094.7}
$$
在 $q$ 处使用与 $W$ 相应的 Coleman–Gross 规范第三类微分。本文的高度符号与 R43 相同。

## 2. 分歧端点的正确整估值是整个共轭多重集的估值

设 $K/\mathbb Q_q$ 是有限未分歧扩张，$\mathcal O$ 为其整数环。在一个几何剩余圆盘取整参数 $t$。设有效除子 $A$ 的全部几何点均在该盘，且 $A$ 在 $K$ 上定义；其点可以在任意有限分歧扩张上。

将点重复按重数列为 $z_1,\dots,z_d$。所有 $v_q(t(z_i))>0$。于是
$$
P_A(U)=\prod_i(1-t(z_i)U)\in1+qU\mathcal O[U].
\tag{1094.8}
$$
理由是各系数 Galois 不变且有正赋值，而 $K$ 未分歧，所以该正赋值至少为 $1$。在形式变量 $U$ 中，
$$
-\log P_A(U)
=\sum_{n\ge1}\frac{\sum_i t(z_i)^n}{n}U^n
\in q\mathcal O[[U]],
\tag{1094.9}
$$
因为 $(q\mathcal O)^k/k\subset q\mathcal O$。各系数也趋于零：只有有限个 $z_i$，而 $v_q(t(z_i)^n/n)\to+\infty$。

对有符号除子取两个有效部分之差即可。所以若
$$
a=\sum_i n_i z_i,\qquad \sum_i n_i=0
$$
在该盘为总次数零，则对任意整微分
$$
\rho=\sum_{j\ge0}r_jt^jdt\in\mathcal O[[t]]dt
$$
有
$$
\int_a\rho
=\sum_{j\ge0}r_j
 \frac{\sum_i n_i t(z_i)^{j+1}}{j+1}
\in q\mathcal O.
\tag{1094.10}
$$
次数零消掉 primitive 的任意常数。收敛及逐项求和已由上述估值支付。

特别地，(1094.10) **不要求**每个 $z_i$ 是 $K$-点，也不要求 $t(z_i)\in q\mathcal O_{K(z_i)}$。例如 $\mu_q$ 端点的参数只有 $1/(q-1)$ 量级的赋值仍完全允许。本文后面只使用这种完整共轭和，绝不逐个端点截断其积分。

## 3. 两变量整微分核与规范第三类微分

本节给出所用整性论证，避免把尚未发表文章的整性命题直接用作黑箱。

令 $\mathcal X/\mathcal O$ 为光滑 proper 曲线，已有整直和 (1094.6)。在目标盘取参数 $s$，置 $\mathcal O'=\mathcal O[[S]]$，令 $z$ 为形式坐标 $s(z)=S$ 的实际形式截面。沿此截面写 $t=s-S$。

有唯一微分
$$
\psi_z\in H^0(\mathcal X_{\mathcal O'},\Omega^1(2z))
\tag{1094.11}
$$
满足：

- 在 $z$ 的主部是 $dt/t^2$，没有留数；
- 它的 de Rham 类属于 $W\otimes\mathcal O'$。

**构造与整性。** 令 $\Omega^1(2z)_0$ 表示在 $z$ 留数为零的子层。微分给
$$
\mathcal O(z)/\mathcal O
 \xrightarrow[\sim]{\,d\,}
 \Omega^1(2z)_0/\Omega^1,
\qquad t^{-1}\longmapsto-t^{-2}dt.
$$
因此
$$
[\mathcal O\to\Omega^1]\longrightarrow
[\mathcal O(z)\to\Omega^1(2z)_0]
\tag{1094.12}
$$
是整 quasi-isomorphism；这里没有 $q$ 分母。Riemann–Roch、相对 Serre 对偶和 base change 给规定双极主部的整微分：$H^1(\Omega^1(z))=0$，先提升双极系数，再由总留数定理令唯一可能的简单极系数为零。由 (1094.12) 得其整 de Rham 类，按整分解 $L\oplus W$ 减去 $L$ 分量。这给 (1094.11)。两个这样的微分之差是属于 $L\cap W$ 的全纯微分，故唯一。

在任何不含 $z$ 的另一剩余盘，取整参数 $r$，所得核有完整展开
$$
\psi_z=\sum_{a,b\ge0}\kappa_{ab}S^a r^bdr,
\qquad \kappa_{ab}\in\mathcal O.
\tag{1094.13}
$$
这个构造与有限扩张及形式参数的特化相容。它只处理双极，所以不会遇到把任意高阶第二类主部积分时可能产生的 $q$ 分母。

设 $D$ 是次数零除子，$\omega_D$ 是留数除子为 $D$、规范类属于 $W$ 的第三类微分。对不在其支撑的 $z$，
$$
\frac{\omega_D}{ds}(z)=\int_D\psi_z.
\tag{1094.14}
$$
这里使用标准 Coleman reciprocity／Serre cup residue 恒等式，归一化可直接核：取 $\psi_z$ 的 Coleman primitive $F_z$。杯积 $\Psi(\omega_D)\cup[\psi_z]$ 为零，因为两类均在各向同性 $W$。相应局部留数和中，$D$ 上贡献 $\sum n_PF_z(P)$；$z$ 处由 $F_z=-1/t+\text{regular}$ 贡献 $-(\omega_D/ds)(z)$，其余点无贡献。因此得到 (1094.14)，且 $\deg D=0$ 消掉 $F_z$ 的常数。

这个 reciprocity 身份是已发表 Coleman–Gross 理论的一部分；本文所需的所有**整**核、扩张和分母估值已经在 (1094.8)–(1094.13) 给出。

## 4. 逐盘次数零给真正 $q^2$ 局部高度

设 $D,E$ 是 $\mathbb Q_q$ 上的次数零除子，并满足：

1. 它们在每个几何剩余圆盘上的总次数都为零；
2. 没有一个几何剩余圆盘同时碰到二者的支撑。

先作一个有限未分歧扩张，把所需特殊点和参数都分开。每个盘内的两个有效部分仍是该未分歧域上的 Galois 多重集。

在碰到 $E$ 的任一盘，把 (1094.13) 对 $D$ 积分。由 (1094.10)，每个 $S^a$ 系数都在 $q\mathcal O$，且求和收敛。因此 (1094.14) 给
$$
\omega_D\big|_{U_E}\in q\mathcal O[[s]]ds.
\tag{1094.15}
$$
再对 $E$ 积分，第二次使用 (1094.10)，得到
$$
h_q^W(D,E)=\int_E\omega_D\in q^2\mathcal O.
$$
高度在 $\mathbb Q_q$ 上定义，故它实际在 $q^2\mathbb Z_q$。整个证明没有对分歧扩张取一个带分母的平均；未分歧扩张只用来分开各盘，最后取交 $\mathbb Q_q\cap q^2\mathcal O=q^2\mathbb Z_q$。

结论对每一个整各向同性 $W$ 都成立。因此在这些实际除子上，第一全局高度模 $q^2$ 不依赖于这一补空间的选择。

## 5. 原 $B_q$ 的逐盘次数零与实际支撑

$q\equiv1\pmod {47}$。在完整 prime-to-$q$ 的 $47$-level 模型上，原 $q$-同源对应的特殊循环是 Frobenius 图与其转置之和；取规范 Cartan 商后仍如此。可以从模问题直接核这个等式：普通稠密开集上，连接核与 étale 核给这两条分支；一条在源上的次数为 $1$，另一条为 $q$。有限 flat 的闭包及循环重数把等式延拓到超奇异点。$q\equiv1\pmod {47}$ 消掉额外的 determinant 重标。

于是对任意几何特殊除子循环 $A$，
$$
\overline{T_q}A=F_*A+qF_*^{-1}A.
\tag{1094.16}
$$
若 $a$ 在 $\mathbb Q_q$ 上定义，其特殊循环被 $F$ 固定，所以
$$
\operatorname{sp}(Ba)=0.
\tag{1094.17}
$$
这正是逐几何盘次数零，包含所有不可分／分歧重数。

对一个 $\mathbb Q_q$ 点 $y$，(1094.16) 还说明 $T_qy$ 的全部几何目标都在 $y$ 的同一个剩余盘，因为两个 Frobenius 目标都是 $\bar y$。R1085 另以实际 Serre–Tate 参数证明了本文两个普通 CM 点的同一结论：两个水平 CM 目标及所有非水平根都在原规范 necklace 的盘中，而非仅在相同 $j$ 纤维。

全部尖点构成一个有理 Galois 轨道，原 $T_q$ 保尖点且次数 $q+1$，故
$$
T_qC_\infty=(q+1)C_\infty,\qquad
D_i=23((q+1)y_i-T_qy_i).
\tag{1094.18}
$$
原 $D_i$ 没有尖点支撑。

异于 $47,q$ 的 Hecke 对应在 $q$ 的好整模型上由有限 pull–push 给出，并与特殊化相容；因此
$$
\operatorname{sp}(T D_i)=T\,\operatorname{sp}(D_i)=0.
\tag{1094.19}
$$
对原有限 Cartan 角对应也一样：在完整 $47$-level 好模型上作有限群 pull–push，再下降到原商。$q$ 不整除有关有限群阶，全部粗点及自动同构的重数保持。仅说“对应保持 $j$”不足以证明 (1094.19)；这里使用的确是完整循环的特殊化相容性。

## 6. 两个原 CM 域给全部 Hecke 的离盘性

$4513\equiv1\pmod {12}$。所以 $y_4$ 与 $y_3$ 的椭圆曲线在 $q$ 处普通，其几何约化端同态代数分别为
$$
\mathbb Q(i),\qquad \mathbb Q(\sqrt{-3}).
\tag{1094.20}
$$
原 CM 作用在好约化下专化为单射；普通椭圆曲线的端同态代数是一个虚二次域，故 (1094.20) 没有更大的非交换可能。

每个异于 $q$ 的同源保持几何端同态代数。因而任意 $T D_3$ 的每个目标约化仍有第二个域；$D_4$ 的约化则在第一个域的点上。两个域不同，所以它们连底层椭圆曲线都不可能相同，尤其不能是同一个原 Cartan 模曲线点。

与 (1094.17)–(1094.19) 结合，第4节直接给 (1094.2)。对有限 Cartan 角对应，底层椭圆曲线不变，离盘性更直接。所有复合与整数线性组合逐项成立。

这不是只在一个一次 Hecke 块上成立的式子。它适用于实际 Hecke 对应的全局整数作用；随后对全局高度按 $\mathbb Z_q$ 连续线性延拓，可以在原完整 $\mathbb T_q$ 中读取相应泛函。若使用 $q$-进幂等元，原有限交数公式必须先在实际有理对应上计算再取极限；不把幂等元当成一个未经构造的有限有效除子。

### 6.1 同高斯域的两个合法离盘代表

对于 $T_3D_4$：高斯曲线的普通约化具有端同态环 $\mathbb Z[i]$，其为最大序。若某个 $3$-同源目标与原曲线同构，就会给一个次数 $3$ 的端同态；但 $a^2+b^2=3$ 无整数解。因此全部 $T_3D_4$ 目标约化都避开 $D_4$ 所在盘。特殊化相容性给逐盘次数零，于是得到 (1094.4) 第一式。

对于 $T_2-1$：旧
[qc-local-types-resume2 note](../notes/2026-11-12-qc-local-types-resume2.md)
§3 已证明实际规范 Cartan 标记下
$$
T_2y_4=y_4+2y_{16},\qquad
(T_2-1)u_4=2u_{16},
\tag{1094.21}
$$
其中 $u_{16}=23y_{16}-C_\infty$、$j(y_{16})=287496$。这里连尖点尺度也一致，因为 $T_2C_\infty=3C_\infty$。$B$ 与 $T_2$ 交换，所以
$$
(T_2-1)D_4=2B u_{16}.
$$
两原 $j$ 值之差
$$
287496-1728=2^3\,3^6\,7^2
$$
不被 $4513$ 整除，故两个实际剩余盘不同。再次由第4节得 (1094.4) 第二式。

本文没有把 level $41$ 的旧标记交数证书搬到 $47$，也没有预设这两个 Hecke 算子在当前所有残余块上可逆。

## 7. 第一全局高度的准确有限读数

设 $\mathcal X/\mathbb Z$ 是原 $X$ 的正则模型。对次数零除子 $D,E$，用唯一模全纤维的有理垂直修正使一个除子对每个分量的交数为零；记所得到的 Néron 交数为 $I_\ell(D,E)$。

对本文原 $D_4,T D_3$，泛纤维支撑不交，且只有有限个 $\ell$ 贡献。R1067 给 $\ell\ne47$ 的好模型，因此这些 $I_\ell$ 是整数。R1089 给坏 $47$ 的分量群指数为 $46$，所以 $I_{47}$ 的分母只有 $46$ 的因子；特别地所有 $I_\ell$ 均为 $q$-整数。

按 (1094.7) 和 R43 的实际 Poincaré 范数截面约定，
$$
h^W([D_4],T[D_3])
=h_q^W(D_4,T D_3)
-\sum_{\ell\ne q}I_\ell(D_4,T D_3)\log_q\ell.
\tag{1094.22}
$$
第一个项在 $q^2\mathbb Z_q$。对 $\ell\ne q$，
$$
\frac{\log_q\ell}{q}
=\frac{1}{q-1}\frac{\log_q(\ell^{q-1})}{q}
\equiv-\frac{\ell^{q-1}-1}{q}\pmod q.
\tag{1094.23}
$$
故 (1094.22) 除以 $q$ 正是 (1094.3)。其整体符号已经由 R43 的 $\chi_\ell(\ell)=-\log_q\ell$ 固定。

因此现在要计算的是一个原全局交数向量，而不是任意局部 Coleman 高度、未知周期或任意指定的 log 补线。式 (1094.3) 仍没有断言这个向量非零。

### 7.1 不得删除的 $q^2$-Hecke 项

若为计算采用投影公式，必须使用完整恒等式
$$
T_q^2=T_{q^2}+q,\qquad
B^2=(q^2+3q+1)-2(q+1)T_q+T_{q^2}.
\tag{1094.24}
$$
此处 $T_{q^2}$ 是标准完整 Hecke 算子：它包含次数 $q^2$ 的非循环核项，不能悄悄改成仅循环 $q^2$-同源对应。

在任意好素数 $\ell\ne47,q$，CM 整 $j$ 截面不碰尖点，所以逐项投影公式把实际交数化为
$$
\begin{aligned}
I_\ell(D_4,T D_3)=23^2\big(&
(q^2+3q+1)\,(\overline y_4\cdot\overline{T y_3})_\ell\\
&-2(q+1)\,(\overline y_4\cdot\overline{T T_q y_3})_\ell\\
&+(\overline y_4\cdot\overline{T T_{q^2} y_3})_\ell
\big).
\end{aligned}
\tag{1094.25}
$$
该式的每个交数都仍在**原 $47$-Cartan 曲线**上。它只用于实际对称且与 $T_q$ 交换的原 Hecke／角对应；取一般有向对应时须相应放入转置。

计算 (1094.3) 时，可以把 (1094.25) 的三个整数系数模 $q$ 化为 $1,-2,1$，因为每个交数已是 $q$-整数。不能因此删掉第三项或改变其除子。

在 $\ell=47$，本文保留原完整 $I_{47}(D_4,T D_3)$。必须计算全部垂直修正和相关水平交数；(1094.25) 不被用于无声消掉尖点／分量项。特别地，R1074§9 的“同一个原 $47$ 盘中的点差”结论，不自动覆盖这里整个 $q$-Hecke CM 循环。

若进一步用 CM 同源的整数迹参数计算 (1094.25)，次数为 $n$ 的同源带来的判别式变量是
$$
(D_1D_2n^2-x^2)/4,
$$
不是 $(D_1D_2n-x^2)/4$。本条没有发起新的数值任务，也没有将候选文献中的未核 level 公式直接当作已发表输入。

## 8. 与当前实际 MW 格及残余盘任务的关系

R1088 已把两个原 trace-zero 对应的 cusp 固定除子模，与 $u_4,u_3$ 的原 cusp 模联系起来；R1089 付清 $B$ 在 $q$ 整格上的可逆性。本文为这两个原 CM 来源提供一个无需计算 $q$ 处高阶积分的**第一全局高度**读法。

以下步骤仍必须实际完成：

- 计算 (1094.3) 中原 level $47$ 的交数，包含坏 $47$ 项，并读出相应整 Hecke 块的高度；
- 将这个全局高度数据和原残余盘上的 Poincaré／QC 局部函数配合；
- 证明原八个 CM 剩余盘内部没有另外的有理点。

[R1093](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md) 的完整原 MW 整饱和性、第一对数单位或本条的 $q^2$ 消去，都不单独给出最后一项。本文也没有把固定 $47$ 的结果当成 O0 的统一完成。

## 9. 已核的来源与复核范围

- R. F. Coleman, [*Reciprocity laws on curves*](https://www.numdam.org/item/CM_1989__72_2_205_0.pdf), *Compositio Mathematica* **72** (1989), 205–235；Proposition 4.5、Theorem 5.2 的杯积／reciprocity 框架。这里使用它的杯积／局部留数恒等式，整核构造另在第3节完整给出。
- R. F. Coleman and B. H. Gross, *p-adic heights on curves*, *Advanced Studies in Pure Mathematics* **17** (1989), 73–81；高度定义及规范第三类微分。对原文的可读后继核对见下一条；本次未把无法直接读取的网页包装声称为已读全文。
- A. Besser, [*The p-adic height pairings of Coleman–Gross and of Nekovář*](https://arxiv.org/pdf/math/0209006), *CRM Proceedings and Lecture Notes* **36** (2004), 13–25；§2 的规范微分、有限扩张与局部高度；§§5–6 的积分／de Rham 对偶比较。
- J. Duque-Rosero, S. Hashimoto and P. Spelier, [*Geometric quadratic Chabauty and p-adic heights*](https://arxiv.org/pdf/2207.10389), *Expositiones Mathematicae* **41** (2023), 631–674；§3.3、Proposition 3.10，以及 R43 已核的实际范数／Néron 对应。
- 仓库 R43、R1067、R1074§9、R1081、R1085、R1088、R1089；旧规范 $T_2$ 的实际恒等式位置见 (1094.21)。本条逐项保留其原曲线和原标记，不引用 level $121$ 未发表主定理。

第2–4节的论证也与 Jaswal 2026 候选稿中使用的整核方法相符；这里重建了真正使用的完整证明及其在原 $47$、原 $B_q$ 循环上的所有前提，并未把该未发表结论直接作为引理。本文为纯纸面数学；没有本地数学执行或新 CI 结果。
