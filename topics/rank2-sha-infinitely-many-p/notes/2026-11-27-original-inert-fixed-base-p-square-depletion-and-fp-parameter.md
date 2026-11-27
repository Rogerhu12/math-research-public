# 原惰性固定底曲线的全 p² 级剔除和与同一个 fp 整参数

日期：2026-11-27。状态：以下同一原图、真实两退化映射及全范数恒等式已手证；没有数学执行。本篇把**固定原椭圆曲线，只添加全部 cyclic p² 级结构**的向外对应，与已登记的高导子曲线上 canonical 上行对应区分开。后者的完整 imprimitive 和仍为零。

## 1. 原对象与两个不同的模问题

沿用 [R1049](../results/R1049-original-inert-syntomic-graphs-and-crystalline-lattice.md) 的原
$S/B$、$A=E_{27}$、$f_{\Omega_S}=-\delta h_\Gamma$、三条 $\eta_j$、
原 $P_-$、测试侧 $P_-^t=P_+$、全部54条 degree34 同源
$\varphi_i:A\to E_i=S_{b_i}$及外系数 $c_i$。
级结构为原 full9 有序基
$$
\ell_9=((1+\omega)u_9,(\omega-1)u_9).
\tag{1}
$$
所有微分和 Artin 基 $a_{j,p}$均保持原规范。

固定一个好惰性 $p\ge5$，排除原有限坏集，特别
$p\nmid2\cdot3\cdot17$。记
$$
N=p^2,\qquad M=p(p+1).
$$
对每个原 $E_i$，令 $\mathscr C_2(E_i)$是其所有 cyclic order $p^2$
子群，$\lambda_D:E_i\to E_{i,D}=E_i/D$。
本篇把 $(E_i,\ell_i,D)$视为新模曲线上的点；**它的底曲线仍是
$E_i$**。两个实际退化映射分别忘掉 $D$，或取商并沿
$\lambda_D$运输完整级结构。

相反，
[原 p² 全范数笔记](2026-11-27-original-inert-p-square-full-norm-and-endpoint-zero.md)
§4的点以 $E_{i,D}$为底曲线，取其 canonical 上行核
$\ker\widehat\lambda_D$回到 $E_i$。这两种点及其 $V^2$方向不同，
即使使用同一个抽象集合 $\mathscr C_2(E_i)$标号，也不能混同。

新的级结构和始终有 $M$项，不除以 CM 的六个单位。原 full9
已经刚性化曲线自同构。在任何包含全部 $p^2$挠点的辅助域中，
可先对 cyclic subgroup 的有限 étale 纤维取 trace；
不能再把更大 torsion 域的 stabilizer 重数暗中乘进去。
原 $\eta_j$在这一新 $p$-局部相对轨道上平凡。

## 2. 实际 full9 上的两退化映射与剔除形式

在原 full9 模问题上加一个 cyclic $D$，得到有限覆盖
$Y_0(p^2)\to Y$。这里保留原全部 determinant 分量及随后原
$3$型 projector；一个中间 degree $p$商不可提前认作原分量。
令 $\mathcal E_0,\mathcal E_2$分别是忘级端和商端的 universal
elliptic curves，$\lambda:\mathcal E_0\to\mathcal E_2$为真正
degree $p^2$同源。

在光滑开部上定义原两旧形式的组合
$$
\boxed{\quad
\Omega^{[p]}=d_0^*\Omega_S-\frac1{p^2}\lambda^*d_2^*\Omega_S.
\quad}
\tag{2}
$$
这不是把第二项当成一个任意权的 $p$幂。
若 $\lambda^*\omega_2=c\omega_0$，则杯积乘 $N$及 KS 定义给
$$
\lambda^*\operatorname{KS}(\omega_2^2)
=\frac{c^2}{N}\operatorname{KS}(\omega_0^2),\qquad
\lambda^*\bigl(\operatorname{KS}(\omega_2^2)\wedge\omega_2\bigr)
=\frac{c^3}{N}
 \operatorname{KS}(\omega_0^2)\wedge\omega_0.
\tag{3}
$$
在 Tate 的向外 cyclic $p^2$分支，$c=p^2$；所以
$\lambda^*d_2^*\Omega_S$对应 $p^4V_p^2f_{\Omega_S}$。
式(2)于是正是
$$
f_{\Omega_S}^{[p]}=f_{\Omega_S}-p^2V_p^2f_{\Omega_S},
\tag{4}
$$
因为原 weight3 表示有 $a_p=0,\epsilon(p)=-1$。
其它分支由同一个 universal correspondence给出，不能只延拓
$q$展开后再自由重选其微分。

对原 $\mathcal H=H^1_{\rm dR}(\mathcal E/Y)$-值 Coleman primitive
$G$，同一式写成
$$
G^{\rm out}(E_i,\ell_i,D)
=G(E_i,\ell_i)
-\frac{\lambda_D^*}{p^2}
 G(E_{i,D},\lambda_D\ell_i).
\tag{5}
$$
由(3)，其连接就是(2)。这明确给出所有非canonical级结构上的
值：它们是原同一 $G$沿两个真实退化映射的 functorial pullback。
不假定在 supersingular 点存在 canonical order $p^2$子群。

在普通 canonical 分支，(5)与实际 $G-V^2G$相同。
若以后将另一 construction 的负权函数认作(5)，仍需核其
Coleman/Frobenius 规范；不能只因二者的连接相同就省掉 horizontal
常数。本篇的数值恒等式还可完全由下一节的 proper AJ 自然性
证明，因此不依赖那份额外比较。

## 3. degree34 图与每条 degree34p² 图的真正推前

在忘级端纤维 $(E_i,\ell_i,D)$中，仍取原 degree34 图
$$
\widetilde\Delta_{i,D}
=\Gamma_{\varphi_i}-34(E_i\times O_A)-(O_{b_i,D}\times A).
\tag{6}
$$
其底曲线和 $\varphi_i$没有改变，新增的只是 level 标签。

在商端，真正推前为
$$
(\lambda_D\times1)_*\widetilde\Delta_{i,D}
=\Delta_{\lambda_D\varphi_i}
=\Gamma_{\lambda_D\varphi_i}
 -34p^2(E_{i,D}\times O_A)
 -(O_{b_{i,D}}\times A).
\tag{7}
$$
证明逐项给出：图的推前是复合同源的图；竖直纤维的推前次数
为 $p^2$；零截面与 $A$的乘积推前次数为1。
所以 degree0 修正也准确运输，不仅是未修正图在点集上的等式。

由 proper Abel–Jacobi 的推前/拉回自然性，(2)、(7)给
$$
\boxed{\;
\operatorname{AJ}_p(\widetilde\Delta_{i,D})
       (\Omega^{[p]}\omega_A)
=
\operatorname{AJ}_p(\Delta_{\varphi_i})(\Omega_S\omega_A)
-\frac1{p^2}
 \operatorname{AJ}_p(\Delta_{\lambda_D\varphi_i})
       (\Omega_S\omega_A).
\;}
\tag{8}
$$
这也是(5)的杯积式，但(8)保留完整的循环和 degree 修正。

这里不需要声称整座 $p^2$-level 曲面在 $p$处好约化。
右边是原 good-reduction CM 实现的两个实际读数。
左边若用覆盖曲面的旧上同调实现，恰是这两份 good
pullback 的线性组合；其 finite-polynomial 或 de Rham AJ
含义由 functoriality固定。可以在特征零先取 proper compactification
和 resolution；相应边界的 vertical correction由(7)逐项保留，
不会凭一个新模型加上未知“局部周期”。

## 4. 完整向外和的非零 Euler 因子

原 p² 全范数笔记(22)已在同一 full9、同一 primitive 和同一微分下证明
$$
\sum_{D\in\mathscr C_2(E_i)}
 \operatorname{AJ}_p(\Delta_{\lambda_D\varphi_i})
       (\Omega_S\omega_A)
=M\,\operatorname{AJ}_p(\Delta_{\varphi_i})(\Omega_S\omega_A).
\tag{9}
$$
把(8)对全部 $D$求和，得到
$$
\boxed{\;
\sum_D\operatorname{AJ}_p(\widetilde\Delta_{i,D})
       (\Omega^{[p]}\omega_A)
=M(1-p^{-2})\,
 \operatorname{AJ}_p(\Delta_{\varphi_i})(\Omega_S\omega_A).
\;}
\tag{10}
$$

也可在同一 $\mathcal H$上独立读出这个 scalar：
原笔记(6)、(9)–(12)给
$$
\langle p\rangle G=-G,\qquad
\mathsf B_1G=0,\qquad
\mathsf B_1^2=\mathsf B_2+\frac{p+1}{p}\langle p\rangle,\qquad
\mathsf B_2G=\frac{p+1}{p}G.
$$
于是(5)的完整和为
$$
MG-\mathsf B_2G
=\left(p(p+1)-\frac{p+1}{p}\right)G
=M(1-p^{-2})G.
\tag{11}
$$
两条证明使用相同的中心 $-1$及真实回返路径。
这里 $1-p^{-2}$严格非零，但它的 $p$-赋值为$-2$，
不是一个未经整格比较就可丢掉的单位。

## 5. 原全54、η、Cor、最高投影与整格

原 degree34 同源素于 $p$，故每个 $D\subset E_i[p^2]$
与唯一 $D_A\subset A[p^2]$对应。实际商方块满足
$$
\lambda_D\varphi_i=\varphi_{i,D_A}\lambda_{D_A}.
\tag{12}
$$
因此两个退化映射与原2、17全部 weighted邻点交换。
3处的 $Ph$、243项 projector及最高 projector 同样逐项运输。
所有几何 Galois 作用只重标记 $(i,D)$及全9基；
外部 $c_i$与 $\eta_j$权不作额外 Frobenius。

令 $\mathcal A^{\rm out}_{j,p}$为(10)左边再施原
$$
\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
 \eta_j(\sigma)^{-1}
 \sum_{\gamma\in\operatorname{Gal}(L/H)}
 \sum_{i=1}^{54}c_i
\tag{13}
$$
及原最高投影所得的值。没有额外 $1/M$、$1/54$或另一个 $1/18$。
式(10)准确变成
$$
\mathcal A^{\rm out}_{j,p}
=M(1-p^{-2})
 \operatorname{AJ}_p(Y_{j,0})(\Omega_S\omega_A).
\tag{14}
$$
R1049在同一杯积和模型基下已付
$$
\operatorname{AJ}_p(Y_{j,0})(\Omega_S\omega_A)
=\frac p{p+1}\mathcal I_{j,p},\qquad
h_{j,p}=a_{j,p}^{-1}\mathcal I_{j,p}\in\mathcal O.
$$
故完整结果为
$$
\boxed{\quad
\mathcal A^{\rm out}_{j,p}=(p^2-1)\mathcal I_{j,p},\qquad
a_{j,p}^{-1}\mathcal A^{\rm out}_{j,p}=(p^2-1)h_{j,p}.
\quad}
\tag{15}
$$
真正成为单位的是式(15)的 $p^2-1$。
整性属于完整和，不声称每条新标记图的读数都分别为整。

在 R1049已付原格的素数范围内，特别使用下式几何首层时仍保 $p>q_0$ 及全部固定常数好集，
$$
\overline{a_{j,p}^{-1}\mathcal A^{\rm out}_{j,p}}
=-\overline h_{j,p}
=[L:H]\frac{\overline B_j}{\overline a_{j,p}}\,
 \overline K_{j,p}(0).
\tag{16}
$$
最后一式用已付
[未平方原来源笔记](2026-11-27-original-unsquared-toric-theta-source-and-newton-pullback.md)
(5)、(27)，没有新选 Artin 基。

## 6. 与已付零和及尚待正则化的准确关系

以下两行的所有基点、方向和权都必须同时读：

| 模问题 | 剔除项 | 完整结果 |
| --- | --- | --- |
| 新底曲线 $E_{i,D}$，canonical 上行到 $E_i$，再以 $\lambda_D^*/p^2$归一 trace | $G(E_{i,D})-\widehat\lambda_D^*G(E_i)/p^2$ | $0$，原范数笔记(18) |
| 固定底曲线 $E_i$，加全部 cyclic $D$，向外商到 $E_{i,D}$ | $G(E_i)-\lambda_D^*G(E_{i,D})/p^2$ | $M(1-p^{-2})G(E_i)$，本篇(11) |

因此 incoming 的零不排除 fixed-base 的读数；后者也不修改前者。
Kriz的书中出现 $1-p^{-2}$，不能只凭这个形式相同便直接调用：
须先核实际 p²-level 点、两退化映射、微分及 Coleman 规范是否为
本篇这一行，而非另一行。本文(8)–(15)由原 proper 自然性自给证明，
不使用那一全球插值公式。

本篇给出一个保持原 fixed cycle 的真正 p²-level 检测量。
它还没有把这个量与原 $J^{\rm tor}(v)/(pv)$作全精度相认。
已付的(16)及同一源 Newton 恒等式不代替这一剩余 comparison；
特别不能把形式 $n=-2$槽、裸整数权极限或非整数 $p^n$
当成同一个 Coleman regularization。
