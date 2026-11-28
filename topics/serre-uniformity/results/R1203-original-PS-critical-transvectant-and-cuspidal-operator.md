# R1203：原 PS 临界有限模上的准确秩一尖点算子

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明。** 保持 R1195 的同一个有限尖点幂等元及正规化子平均。在本篇的实际 polynomial 模
$\operatorname{Sym}^{3p-1}k^2\otimes\det^{m-1}$ 上，$p$ 倍单尖点投影的模 $p$ 作用准确等于普通二阶 transvectant 与其回嵌复合的 $-1/4$ 倍。其正规化子固定空间为二维，原算子是一个显示的非零秩一 nilpotent。

这个模是 R1202 末节待读取 PS 返回的有限表示入口。本篇支付其完整群环作用和绝对常数；尚未把一个仅凭极阶找到的多项式认作原 $\Psi$ 在第 $p$ 个 normal 层的真实系数。实际 Frobenius／Cartier 来源继续计算，不由本篇直接宣布指定 $C$ 上的单位。

## 1. 同一个群环元素和固定规范

设
$$
p=12g-1>37,\qquad m=(p-1)/2,
\qquad G=\operatorname{PGL}_2(\mathbf F_p).
$$
$k$ 为代数闭剩余域，$N$ 为原非分裂 Cartan 的完整正规化子在 $G$ 中的像。仍取
$$
e_N=\frac1{2(p+1)}\sum_{n\in N}n,\qquad
U_m=p\,e_{V_m}e_N.
\tag{1203.1}
$$
这里 $V_m$ 是 R1193/R1195 的特征零 cuspidal representation，参数为
$\widetilde\omega_2^{m(p-1)}$。它的维数是 $p-1$。本篇不重新归一 $e_{V_m}$ 或 $e_N$。

令
$$
\mathcal M=\operatorname{Sym}^{3p-1}(k^2)\otimes\det^{m-1},
\qquad
W=\operatorname{Sym}^{p-3}(k^2)\otimes\det^{m+1},
\qquad \eta=\det^m.
\tag{1203.2}
$$
$\det^{m+1}=\det^{1-m}$ 于 $\operatorname{GL}_2(\mathbf F_p)$；所以 $W$ 就是 R1195 的共同剩余因子 $W_{m-1}$。
各模的中心作用均平凡，因而确为 $G$-模。

对 $\mathbf F_p$ 矩阵，Frobenius 乘法给真正的 $k[G]$-同构
$$
\mu:\operatorname{Sym}^{p-1}(k^2)\otimes
        \operatorname{Sym}^{2}(k^2)\otimes\det^{m-1}
 \xrightarrow{\sim}\mathcal M,
$$
$$
\mu(f\otimes h)=f(X,Y)h(X^p,Y^p).
\tag{1203.3}
$$
证明无需维数猜测：左边的 monomial 下标是 $j+pa$，
$0\le j\le p-1,\ 0\le a\le2$，恰好无重复覆盖 $0,\ldots,3p-1$。
群矩阵的系数在 $\mathbf F_p$，故该映射与真实有限群作用相容。
记 $\operatorname{St}=\operatorname{Sym}^{p-1}(k^2)$。

以下二阶算子严格使用普通导数，没有除以 $2!$：
$$
q_2(f\otimes h)
=f_{XX}h_{YY}-2f_{XY}h_{XY}+f_{YY}h_{XX}.
\tag{1203.4}
$$
它把 (1203.3) 左边送到 $W$。
反向映射是
$$
i(H)=X^2H\otimes Y^2-2XYH\otimes XY+Y^2H\otimes X^2.
\tag{1203.5}
$$
两个式子中的 determinant twist 正相匹配；二阶 alternating contraction 及 alternating square 各贡献 $\det^2$。
在 $\mathcal M$ 的原 polynomial 坐标中，(1203.5) 就是
$$
\mu i(H)=C^2H,\qquad C=X^pY-XY^p.
\tag{1203.6}
$$
本篇后文略去 $\mu$，把这两条同一尺度的映射直接记为 $q_2,i$。

## 2. 唯一的同型回嵌与商映射

$W$、$\operatorname{St}$ 均不可约且自对偶。次数小于 $p$ 的对称幂不可约性，可由两个根子群的有限差分提取所有 divided derivatives 直接证明；所需阶乘均小于 $p$。

本处需要准确重数，而不是只知道 $i,q_2$ 非零。有限群上有
$$
\operatorname{Hom}_G(\mathcal M,W)
\simeq
\operatorname{Hom}_G\left(
 \operatorname{St},
 \operatorname{Sym}^{p-3}(k^2)\otimes\operatorname{Sym}^2(k^2)
\right).
\tag{1203.7}
$$
所有 determinant 因子在此严格抵消。
右边的 tensor product 有实际直和
$$
\operatorname{Sym}^{p-3}\otimes\operatorname{Sym}^2
\simeq
 \operatorname{Sym}^{p-1}
 \oplus\left(\operatorname{Sym}^{p-3}\otimes\det\right)
 \oplus\left(\operatorname{Sym}^{p-5}\otimes\det^2\right).
\tag{1203.8}
$$
为核该分裂在本特征合法，可取三个最高向量
$(X_1Y_2-Y_1X_2)^jX_1^{p-3-j}X_2^{2-j}$，$j=0,1,2$。
其最高权依次为 $p-1,p-3,p-5$，都小于 $p$。
用 divided lowering 生成的三个子模分别不可约，维数为
$p,p-2,p-4$。Casimir 特征值依次为 $-1,3,15$，在 $p>37$ 下互异，故三个子模直和；维数相加恰为 $3(p-2)$，得到 (1203.8)。
这也可用三条有限极化／transvectant 恒等式验证，不需要反除 $p$。

因此
$$
\dim\operatorname{Hom}_G(\mathcal M,W)
=\dim\operatorname{Hom}_G(W,\mathcal M)=1.
\tag{1203.9}
$$
第二个等式也由 $\mathcal M,W$ 的自对偶性得到。
(1203.4) 非零，例如对
$X^{p-1}\otimes Y^2$ 给
$2(p-1)(p-2)X^{p-3}=4X^{p-3}$。
(1203.5) 非零，所以它是这一唯一 $W$ 子模的回嵌。

直接在次数 $d=p-3$ 的齐次 $H$ 上求导，Euler 等式给
$$
q_2i(H)=2(d+2)(d+3)H
       =2p(p-1)H=0.
\tag{1203.10}
$$
故 $iq_2$ 为非零的平方零算子。这里没有把复合零误当作 $i$ 或 $q_2$ 零。

## 3. 原 character sum 的像准确在这个 W 中

先去掉 $e_N$，记
$$
z=\overline{p\,e_{V_m}}\in k[G].
$$
标准中央幂等元的准确系数是
$$
p\,e_{V_m}=\frac1{p+1}\sum_{\gamma\in G}
       \chi_{V_m}(\gamma^{-1})\gamma.
$$
因 $p+1\equiv1\pmod p$，约化后没有另一个标量。

R1195 的同一 Brauer 分解给
$\overline V_m^{\,\mathrm{ss}}=W\oplus\eta$。
它在所有 $p$-regular 元上的 character 相等。
剩下的非平凡 unipotent 也须核：有限 cuspidal 表示在一个 unipotent 根子群上没有不变量，split torus 传递作用于其全部非平凡 additive characters，维数又是 $p-1$，故每个非平凡 character 出现一次，其 trace 为 $-1$。
$W\oplus\eta$ 在模 $p$ 的对应 trace 是 $(p-2)+1=-1$。
恒等元处亦相等。故对所有群元素都有
$$
\overline{\chi_{V_m}(\gamma)}
=\operatorname{tr}W(\gamma)+\eta(\gamma).
\tag{1203.11}
$$

对任意不可约 $S$，群环元素
$\sum_\gamma\operatorname{tr}S(\gamma^{-1})\gamma$
生成的左理想是若干份 $S$ 的商，因此为 $S$-isotypic 半单模。
自足地，取矩阵系数
$$
E_{ab}=\sum_\gamma S(\gamma^{-1})_{ab}\gamma.
$$
左平移只按 $S$ 的矩阵线性组合这些 $E_{ab}$，所以该左理想是
$S^{\oplus\dim S}$ 的像。这条论证在特征 $p$ 下仍成立，不使用除以 $|G|$ 的平均。

另一方面
$$
\operatorname{Hom}_G(\eta,\mathcal M)
\simeq
\operatorname{Hom}_G\left(
 \operatorname{St},\operatorname{Sym}^2(k^2)\otimes\det^{-1}
\right)=0.
\tag{1203.12}
$$
两个不可约模的维数分别为 $p$ 与 $3$。
所以 (1203.11) 的 $\eta$-character sum 在 $\mathcal M$ 上为零。
$W$-character sum 的像则在 (1203.9) 的唯一 $i(W)$ 中。
由同一个 Hom 重数，存在一个尚待求值的 $c\in k$，使
$$
z|_{\mathcal M}=c\,i q_2.
\tag{1203.13}
$$
下面从原群和求出 $c$；不从“一个非零 intertwiner”补上单位。

## 4. 一个完整 rank-one 群和固定常数 -1/4

取输入和所读 monomial 为
$$
F=X^{p-1}Y^{2p},\qquad T=X^{3p-3}Y^2.
$$
由 (1203.3)–(1203.6)，
$$
[T]\,iq_2(F)=4.
\tag{1203.14}
$$

用 $\operatorname{GL}_2(\mathbf F_p)$ 计算同一个 $G$ 群和，每个元素有
$p-1=-1$ 个 scalar 代表。$W$ 自对偶，故可把 character 的逆元去掉。
其 determinant twist 与 $\mathcal M$ 的 twist 相乘为
$\det^{(m+1)+(m-1)}=\det^{p-1}=1$。
于是，在 (1203.12) 已消去的 $\eta$ 项之外，
$$
[T]z(F)=
-\sum_{\gamma\in\operatorname{GL}_2(\mathbf F_p)}
 \operatorname{tr}\!\left(\operatorname{Sym}^{p-3}\gamma\right)
 [T]\operatorname{Sym}^{3p-1}(\gamma)F.
\tag{1203.15}
$$

写 $\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，
作用为 $(X,Y)\mapsto(aX+bY,cX+dY)$。因为矩阵系数在 $\mathbf F_p$，
$$
[T]\operatorname{Sym}^{3p-1}(\gamma)F
=\binom{p-1}{2}a^{p-3}b^2c^{2p}
=a^{p-3}b^2c^2.
\tag{1203.16}
$$
最后等号是有限域函数的等号。

将右边与 $\operatorname{tr}(\operatorname{Sym}^{p-3}\gamma)$ 相乘，
总次数为 $2p-2$。在全部四变量 $\mathbf F_p^4$ 上求和为零：
一个 monomial 若有非零全和，每个变量的指数必须是正的
$p-1$ 倍数，总次数至少 $4(p-1)$；指数为零时该变量之和是
$p=0$，亦不贡献。因此 (1203.15) 等于在 singular matrices 上的正和。
零矩阵不贡献，只需全部 rank-one 矩阵。

把 rank-one 矩阵写为
$$
\gamma=\binom{x}{y}(u\ v).
$$
每个非零 rank-one 矩阵恰有 $p-1$ 个这样的非零向量对表示。
其 trace polynomial 是
$\operatorname{tr}(\operatorname{Sym}^{p-3}\gamma)=(xu+yv)^{p-3}$。
故所需 rank-one 和为
$$
\frac1{p-1}
\sum_{x,y,u,v\in\mathbf F_p}
 (xu+yv)^{p-3}x^{p-1}y^2u^{p-1}v^2.
\tag{1203.17}
$$
零向量对的被加项为零，所以这里可将和写在整个四维空间。

展开 $(xu+yv)^{p-3}$，第 $j$ 项的四个指数分别是
$$
p-1+j,\quad p-1-j,\quad p-1+j,\quad p-1-j,
\qquad 0\le j\le p-3.
$$
只有 $j=0$ 的四个幂和非零；该项为 $(-1)^4=1$。
再乘 $(p-1)^{-1}=-1$，得到
$$
[T]z(F)=-1.
\tag{1203.18}
$$
结合 (1203.13)–(1203.14)，准确结论是
$$
\boxed{\quad
\overline{p\,e_{V_m}}\bigm|_{\mathcal M}
=-\frac14\,i q_2.
\quad}
\tag{1203.19}
$$
这是原中央幂等元的原尺度；没有残留的 character、basis 或 Gauss 单位。

## 5. 原正规化子固定二维空间的显示矩阵

取同一个 nonsplit Cartan 的 $s\in\mathbf F_{p^2}$，
$s^2\in\mathbf F_p^\times$ 非平方、$s^p=-s$，并设
$$
A=X+sY,\qquad B=X-sY.
$$
Cartan 固定 monomial 的 $A$ 指数必须同余于 $m-1\bmod(p+1)$。
在次数 $3p-1=6m+2$ 中，只有
$m-1,3m+1,5m+3$ 三个可能值。
正规化子的另一陪集交换 $A,B$；$\det^{m-1}$ 不添负号，因为 $m$ 奇。
因此准确的 $N$-固定基为
$$
F_0=A^{m-1}B^{5m+3}+A^{5m+3}B^{m-1},
\qquad
F_1=A^{3m+1}B^{3m+1}.
\tag{1203.20}
$$

令 $H=(AB)^{m-1}$。
Frobenius 乘法中 $A(X,Y)^p=B(X^p,Y^p)$，另一式同理，故不得把 Cartan 两个系数的 Frobenius 交换删掉。
由二阶 contraction 的坐标变换因子 $4s^2$，
$$
q_2(F_0)=4s^2\cdot4m(m+1)H=-4s^2H,
$$
$$
q_2(F_1)=4s^2\cdot(-2m^2)H=-2s^2H.
$$
另一方面
$$
C=\frac{A^{p+1}-B^{p+1}}{2s},\qquad
i(H)=\frac{F_0-2F_1}{4s^2}.
\tag{1203.21}
$$
全部 $s$ 因子在 (1203.19) 中准确抵消。由于 $e_N$ 在该空间为恒等，
最终得到
$$
\boxed{\quad
\overline U_m(F_0)=\frac14(F_0-2F_1),\qquad
\overline U_m(F_1)=\frac18(F_0-2F_1).
\quad}
\tag{1203.22}
$$
以列向量记矩阵为
$$
\boxed{\quad
[\overline U_m]_{(F_0,F_1)}
=
\begin{pmatrix}
1/4&1/8\\
-1/2&-1/4
\end{pmatrix}.
\quad}
\tag{1203.23}
$$
它非零、秩一、平方为零；像与核均为
$k(F_0-2F_1)$。这不是把 R1202 那两个临界模的一维直和搬到当前模：
当前确有非零 nilpotent 返回。

## 6. 对实际后继计算的准确接口

R1202 已付每个实际最高权负 deck 整微分的单尖点投影整性，
但同底提升差仍有
$$
q\bigl(\pi_0^{e_0-p}\Psi_{\rm high}\bigr)
=\pi_0^{-p}U_m\Psi_{\rm high}.
$$
因此必须读取原 $\Psi_{\rm high}$ 的第 $p$ 层，而非仅证明某个
相关模中允许一个返回。

本篇说明：一旦该原层按真实 full-level 坐标、determinant 运输及所有节点项识别到 (1203.2)，它的群环作用必须按 (1203.19) 或 (1203.22) 计算；不得把该层的 $U_m$ 设为零。
实际输入多项式的来源、其二阶收缩的值和同一原点的对数配对，仍须继续支付。没有用同型替换来源，也没有为指定 $C$ 的饱和格另设一个单位。

## 来源与核对

- [R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md) 与 [R1195](R1195-original-full-integral-normalizer-corner-and-one-p-gluing.md)：原 $V_m,W_{m-1},e_N,U_m$、中央幂等元规范及完整有限角。
- [R1202](R1202-original-highest-character-cuspidal-projection-integrality.md)：原实际最高角色格的整性及尚存的同底提升返回。
- 本文的 Frobenius monomial 同构、两个 transvectants、唯一重数、矩阵系数左理想、完整 singular-matrix 求和和最终二维矩阵均在正文自证。
- root 与 global_route 分别算出 $-1/4$；本稿采用双方核准的 rank-one 求和，并逐项保留 Cartan 系数的 Frobenius 交换。全文为纸面证明，没有本地数学执行，没有重扫已有窗口。

主目标仍 OPEN；继续原临界层的几何来源和完整 Mordell–Weil 消去。
