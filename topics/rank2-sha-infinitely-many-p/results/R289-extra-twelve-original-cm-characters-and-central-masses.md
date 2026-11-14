# R289 — 原十二个额外来源的局部 CM 特征、四个新形式轨道及完整中心质量

日期：2026-11-13。**状态：以下原 Schwartz 特征、精确导子、四个 CM 新形式轨道、复中心非零、惰性质量及一个固定普通 ray 类上的完整单位质量均已证明。本文没有把这些非零质量替代原三条秩二曲线的完整中央导数。**

[R248](R248-ray17-conjugate-trace-and-original-yang-projections.md) 保留了三个原 ray 来源的全部十二个额外投影。本篇确定它们的算术身份，而不只按矩阵特征值命名。它们给出两个二维和两个四维的 CM 模 Abel 簇；每个共轭新形式的复中心阶数都是零。

一个可供后续完整转置使用的额外事实是：在 R282 的普通 ray 类上，这十二个来源的完整单位质量全部是 $p$-adic 单位。它们不需要再以“可能为零的归一分母”保留。

## 1. 原来源、相位和十二个编号

沿用
$$
K=\mathbb Q(i),\quad E_0:y^2=x^3-x,\quad dz=\frac{dx}{2y},
\quad U=x^2,
$$
$$
\beta=4-i,\quad\bar\beta=4+i,\quad\pi=2+i,
\quad\zeta=\zeta_{16},\quad\zeta^4=i.
\tag{1}
$$
原正空间和真实 CM5 算子是
$$
\mathcal H_+=W\mathbb Q(i)[U]_{\le16},\qquad
W=-y\vartheta\sigma^{67},\qquad
\mathscr N=\frac1{2+i}[\pi]_*[\bar\pi]^*.
\tag{2}
$$
所有有限平坦迹均采用 R248 的原 sigma/theta frame。特别
$$
\mathscr N^{16}=1,\qquad
\det(X-\mathscr N)=(X-1)(X^{16}-1).
\tag{3}
$$
对
$$
\mathcal R=\{1,2,3,5,6,7,9,10,11,13,14,15\}
$$
令 $S_r=WP_r(U)$ 为 R248 已登记的准确来源，规范为
$$
\mathscr N S_r=\zeta^rS_r,\qquad [U^{16}]P_r=1.
\tag{4}
$$
这里 $W=z^{64}+O(z^{68})$、$U=z^{-4}+O(1)$，故 (4) 的归一准确等价于
$$
\boxed{S_r(0)=1.}
\tag{5}
$$
R248 的三个原共轭 ray 迹记为 $T_1,T_2,T_3$。若
$$
\Pi_r=\frac1{16}\sum_{n=0}^{15}\zeta^{-rn}\mathscr N^n,
$$
则
$$
\Pi_rT_k=m_{r,k}S_r,\qquad m_{r,k}\ne0
\quad(r\in\mathcal R,\ 1\le k\le3).
\tag{6}
$$
本篇证书重新从原矩阵及原三个 $T_k$ 计算三十六个 $m_{r,k}$；全部值按 $1,\zeta,\ldots,\zeta^7$ 基保存在输出中。

为把编号和实际单位角色对应起来，定义
$$
\nu_j:\mathbb F_{17}^{\times}\longrightarrow\mu_{16},
\qquad \nu_j(3)=\zeta^j.
\tag{7}
$$
$\nu_j$ 是有限 Schrödinger 模型中的单位权；它与下面 Hecke 特征在 $\beta$ 处的单位限制互逆。原 $H$ 使用 $\lambda^{-1}$，其中 $\lambda(3)=-i$，因而是 $j=4$，不是 $j=12$。

准确编号关系为
$$
\boxed{r=9j\pmod {16},\qquad j=9r\pmod {16}.}
\tag{8}
$$
十二个实际对应是

| $r$ | $j$ | 二处 $I_2$ 特征 $i^j$ |
|---:|---:|---|
| 1 | 9 | $i$ |
| 2 | 2 | $-1$ |
| 3 | 11 | $-i$ |
| 5 | 13 | $i$ |
| 6 | 6 | $-1$ |
| 7 | 15 | $-i$ |
| 9 | 1 | $i$ |
| 10 | 10 | $-1$ |
| 11 | 3 | $-i$ |
| 13 | 5 | $i$ |
| 14 | 14 | $-1$ |
| 15 | 7 | $-i$ |

## 2. 原 half-$(-,-)$ 模型中的四条二处特征线

使用 [R239](R239-third-rank2-curve-and-original-sixteen-coset-transport.md) 的十六格 $e_a$、原 Fourier 矩阵 $I$ 和原 Rao 矩阵 $G$。在 $X^8=Z^8=-1$ 子空间取基
$$
b_a=e_a-e_{a+8},\qquad a=1,3,5,7.
$$
原 $i$ 作用和原 $g_*=(-3+4i)/5$ 作用在这个四维空间上准确满足
$$
(I_2)_{ab}=\frac12\zeta^{-ab},\qquad
G_2=iI_2^2,\qquad I_2^4=1.
\tag{9}
$$
每个特征 $i^a$ 的投影
$$
E_a=\frac14\sum_{n=0}^3 i^{-an}I_2^n
\tag{10}
$$
都恰有秩一。取其任一非零向量 $v_a$，则
$$
I_2v_a=i^av_a,\qquad G_2v_a=i(-1)^av_a.
\tag{11}
$$
(9) 直接由 R239 的 (9)–(10) 限制得到；(10) 的迹为一且幂等，故给出完整秩证明。特别 $a=0$ 就是原 $E_{136}$ 的二处向量
$$
(1,t,-t,-1),\qquad t=\tan(\pi/16),
$$
在上述四维基中的坐标。

范数五 torus 元素是
$$
g_\pi=\frac{\pi}{\bar\pi}=-g_*^{-1}.
$$
所以其二处作用在整个四维空间上都为
$$
\boxed{I_2^2G_2^{-1}=-i\,\mathrm{Id}.}
\tag{12}
$$
这一步保留了原 Rao 相位。不能只看 $g_\pi$ 在十七处的余数。

十七处 $i=4=3^{12}$，故原 $\nu_j$ 线的 $I_{17}$ 特征是
$$
\nu_j(4)=i^{-j}.
$$
全局 $i$ 不变要求二处使用 $v_{j\bmod4}$。另外
$$
g_\pi=14=3^9\pmod\beta.
$$
结合 (12) 和原 $E_8$ 参考所定的共同标量 $2+i$，得到 (8)。于是原 global-$I=1$ 的十七维空间准确分成十五条非平凡 $\nu_j$ 线以及两条平凡 CM 线。

## 3. 真实有限 Hecke 特征及精确导子

令 $\psi_0$ 为 $E_0$ 的 Hecke 特征，采用范数五实际 primary 元素
$$
\gamma_5=-1+2i=i\pi,\qquad \psi_0((\gamma_5))=\gamma_5.
\tag{13}
$$
以下给出无穷型为零的有限特征 $\epsilon_j$。在两个十七素位的单位上规定
$$
\epsilon_{j,\beta}|_{\mathcal O_\beta^\times}=\nu_j^{-1},
\qquad
\epsilon_{j,\bar\beta}|_{\mathcal O_{\bar\beta}^\times}=\nu_j.
\tag{14}
$$
在二处令 $\epsilon_{j,2}$ 在 $\mathbb Q_2^\times$ 上平凡，并给出
$$
\boxed{
\epsilon_{j,2}(1+i)=i^{-j},\quad
\epsilon_{j,2}(i)=(-1)^j,\quad
\epsilon_{j,2}(1+2i)=-i(-1)^j.
}
\tag{15}
$$
这些值的相容性可以直接核实：$(1+i)^2=2i$，且
$(1+2i)(1-2i)=5$。也可沿 Hilbert 90 写为
$$
\eta_j(g)=\epsilon_{j,2}(i(g-1)),\qquad g\in K_2^1,
$$
其中
$$
\eta_j(i)=i^{-j},\qquad
\eta_j(g_*)=-i(-1)^j.
\tag{16}
$$
$i,g_*$ 是 R49/R112 已证明的拓扑生成元；(16) 因而唯一确定这个连续角色。(11) 给
$$
\eta_j(i)I_2v_j=v_j,\qquad
\eta_j(g_*)G_2v_j=v_j.
\tag{17}
$$
所以它确实是修改原 splitting 后的不变 Schwartz 线，而不是另一个同维模型。

### 3.1 全局主 idèle 条件

在 $\beta,\bar\beta$ 处，$i$ 的余数分别是 $4,13$，其以 $3$ 为底的离散对数是 $12,4$；$1+i$ 的余数分别是 $5,14$，离散对数是 $5,9$。因此
$$
8j-12j+4j\equiv0,\qquad -4j-5j+9j\equiv0\pmod {16}.
\tag{18}
$$
这分别支付 $i$ 与二处 uniformizer 的全局关系。由于 $K$ 的类数为一，对与 $2\cdot17$ 互素的主理想可直接定义
$$
\boxed{
\epsilon_j((a))=\epsilon_{j,2}(a)^{-1}
   \nu_j(a\bmod\beta)\nu_j(a\bmod\bar\beta)^{-1}.
}
\tag{19}
$$
(18) 表明 (19) 不依赖所选生成元；它给出原始有限 Hecke 特征。
它在有理 idèle 上平凡，且 $\epsilon_j^c=\epsilon_j^{-1}$。

### 3.2 二处导子恰为六

令 $\lambda_2=1+i$。对所有 $j$，
$$
(1+2i)^2=-3+4i\in1+\lambda_2^5\mathcal O_{K,2},\qquad
\epsilon_{j,2}((1+2i)^2)=-1.
\tag{20}
$$
另一方面，若 $a=1+\lambda_2^6b=1-8ib$，则
$$
\frac a{\bar a}\in1+\lambda_2^8\mathcal O_{K,2}.
$$
原 norm-one 群的这个深度子群为 $g_*^{4\mathbb Z_2}$：可由
$v_{\lambda_2}(g_*-1)=4$ 及
$v_{\lambda_2}(g_*^{2^k}-1)=4+2k$ 得到。由 (16)，$\eta_j(g_*^4)=1$。故 $\epsilon_{j,2}$ 在 $1+\lambda_2^6\mathcal O_{K,2}$ 上平凡。
结合 (20)，其导子恰为 $\lambda_2^6$。

$\psi_0$ 的二处导子仅为 $\lambda_2^3$，不会抵消 (20)。对本篇十二个非零 $j$，(14) 在两个十七素位都一阶分歧。因此
$$
\psi_j=\psi_0\epsilon_j,\qquad
\boxed{\mathfrak f(\psi_j)=\lambda_2^6\beta\bar\beta,
\quad N\mathfrak f(\psi_j)=18496.}
\tag{21}
$$
$\psi_j$ 的无穷型是 $(1,0)$。其 Hecke theta 新形式 $f_r$ 的权为二、nebentypus 平凡、原始 level 为
$$
\boxed{4N\mathfrak f(\psi_j)=73984.}
\tag{22}
$$
这里 $r,j$ 始终按 (8) 对应。

### 3.3 用原范数五 Frobenius 固定方向

$\gamma_5$ 在 $\beta,\bar\beta$ 处的余数分别为 $7=3^{11}$、$8=3^{10}$，而 $\gamma_5=-(1-2i)$。由 (15)、(19)，
$$
\epsilon_j((\gamma_5))=-i\zeta^{9j}=-i\zeta^r.
$$
故
$$
\boxed{
\psi_j((\gamma_5))=(2+i)\zeta^r,\qquad
\psi_j((\bar\gamma_5))=(2-i)\zeta^{-r}.
}
\tag{23}
$$
这与 (4) 的真实 CM5 根逐个一致。作为已有规范的交叉核对，$r=4,8,12$ 返回原 $H,S_{2312},S_{39304}$ 的三个已付根；$r=0$ 返回两条 $E_8$ CM 参考。

## 4. 原 Schwartz 输入与复中心阶数

**定理 1。** 对每个 $r\in\mathcal R$，有
$$
\boxed{L(\psi_j,1)=L(f_r,1)\ne0.}
\tag{24}
$$
所以这十二个实际复中心的消失阶均为零。

**证明。** 在二处取 (10) 的非零 $v_{j\bmod4}$，在两个分裂十七素位取 (14) 对应的原紧平均及 Fourier 运输。其未运输单位权正是 (7)；在其余有限位取原未分歧向量，在无穷处取原零阶 Gaussian。

(17) 证明二处是这个 $\psi_j$ 的实际不变线；分裂十七处由 Yang 的局部 construction 原样给出，导子和单位角色已经在 (14)、(21) 指定。全局 $i$ 特征由 §2 准确抵消。因此这里满足 Yang 1997 §2.1 的局部 epsilon 条件，所用 Hermitian 参数仍是原参数 $1$；不是改变参数后再将来源类比回来。

更具体地，R239 (14) 的原 Fourier 计算把该输入变成
$$
F_j^{\rm raw}(\tau)=c_j\sum_{17\nmid n}
 v_{j\bmod4}(n\bmod16)\nu_j(n)^{-1}
 \zeta_{289}^{236n^2}q^{n^2/9248},\qquad c_j\ne0.
\tag{24a}
$$
$c_j$ 只含所选 $v_j$ 的固定归一、非零十七 Gauss 和及 $\nu_j(4)$；它不依赖 theta 变量。对非平凡 $\nu_j$，有限 Fourier 恒等式
$\sum_{a\ne0}\nu_j(a)\zeta_{17}^{as}=\nu_j(s)^{-1}\tau(\nu_j)$
逐项给 (24a)，二次相位和原缩放完全不变。它也说明 (7) 的源单位权与 raw theta 的权互逆。

还需验证这个 Schwartz 来源对应的是 (4) 的原截面。先作原共同 $[2]$ 拉回，有限模型为 $16\times17$ 的 $272$ 维 Heisenberg 模型。标准 theta 实现把其平移/乘字符基送到 degree-$272$ theta 基，并与原 Heisenberg 作用等变。该映射非零且两边均为同一 primitive 中心特征的不可约表示，所以是同构。不可约性也可直接由 primitive commutator 的循环基证明，正是 R282 §4 所使用的原模型论证。

因此上述非零张量向量的截面像非零；它位于 half-$(-,-)$、global-$I=1$ 块，并由 §2 具有真实 CM5 特征 $\zeta^r$。由 (3) 这一特征空间只有一维，故原 theta 来源为某个固定非零代数标量乘 $S_r$。这里使用简单特征空间只是在已经支付的原 Schwartz 实现中识别来源，不是由矩阵特征值猜测 Hecke 特征。

由 (5)，这个原来源在 $z=0$ 的值非零。$K$ 的类数为一，原紧平均后的全局 theta lifting 在单位点就是这个 theta 值乘固定非零 Haar/归一因子。Yang 的平方公式——1997 Theorem 2.6、Corollary 2.4、Corollary 2.14 及 Theorem 2.15——遂给 (24)。所有局部因子都由以上非零实际向量支付；没有以另一个角色的中心值替代此值。$\square$

同一证明适用于每个系数域嵌入，因为下面的 Galois 作用准确置换同一个原模型中的来源。因此关联模 Abel 簇的全部共轭因子都在中心非零。

## 5. 四个准确 CM 新形式轨道

由 (23)，第五个 Fourier 系数为
$$
a_{5,r}=(2+i)\zeta^r+(2-i)\zeta^{-r}
       =4\cos(\pi r/8)-2\sin(\pi r/8).
\tag{25}
$$
所有 Hecke 值属于 $\mathbb Q(\zeta)$，共轭的两素位相加给实系数。若 $j$ 偶，则有限值已在 $\mathbb Q(\zeta_8)$ 中，所以全部 Fourier 系数在 $\mathbb Q(\sqrt2)$ 中；若 $j$ 奇，则在 $\mathbb Q(\zeta_{16})^+$ 中。

保持 $i$ 的 Galois 自同构为 $\zeta\mapsto\zeta^k$，$k=1,5,9,13$。由于 $\mathscr N$ 的原矩阵在 $\mathbb Q(i)$ 上，且 (4) 采用质量一规范，它们准确把 $S_r$ 送到 $S_{kr}$。它们在实子域上已经给出全部自同构。

精确的四个轨道和最小多项式是

| 实际 $r$ 轨道 | $a_{5,r}$ 的最小多项式 | 全系数域 | $\dim A_{f_r}$ |
|---|---|---|---:|
| $\{2,10\}$ | $X^2-2$ | $\mathbb Q(\sqrt2)$ | 2 |
| $\{6,14\}$ | $X^2-18$ | $\mathbb Q(\sqrt2)$ | 2 |
| $\{1,5,9,13\}$ | $X^4-20X^2+98$ | $\mathbb Q(\zeta_{16})^+$ | 4 |
| $\{3,7,11,15\}$ | $X^4-20X^2+2$ | $\mathbb Q(\zeta_{16})^+$ | 4 |

四个多项式都在 $2$ 处 Eisenstein，所以上表的次数是准确次数。上面已给全系数域的相应上界，而单个 $a_5$ 已达到该次数，故没有遗漏更大的系数域，也没有把两条不同轨道误合。

由权二新形式的标准 Shimura 构造，$A_f/\mathbb Q$ 的维数等于其系数域次数；可参见 Ribet 1992 §3 开头所述构造及其 Shimura Theorem 7.14 引用。因为 $f_r$ 来自 $K$ 的 Hecke 特征，这四个 $A_f$ 均为 CM 型。由 (24) 及其全部共轭式，
$$
\boxed{\operatorname{ord}_{s=1}L(A_f,s)=0}
\tag{26}
$$
对四个轨道都成立。

以上结论识别的是原额外来源的实际高维 CM 因子；它们没有给出新的 $E/\mathbb Q$ 椭圆曲线候选。

## 6. 惰性及普通的完整中心质量

### 6.1 惰性原中央算子

固定本课题的惰性好素数，$d=p+1$。仍使用 R248 §7 的完整算子
$$
J_r(u)=\mathcal J_{68c_0}(S_r;u).
$$
原 $J(0)$ 读取零阶质量，故 (5) 准确给
$$
\boxed{J_r(0)=1.}
\tag{27}
$$
两个 CM 缩放及 ray 来源返回原 degree-$4624$ 模型时，继续保留 R248 (31) 的 $2^{(p-1)u}U_{\bar\beta,p}^u$；(27) 不删除这些缩放的导数。

### 6.2 普通 norm-five ray 上的实际单位质量

取 [R282](R282-true-prime-core-mellin-transfer-and-original-primitive-orbit.md) 的明确普通 ray 类
$$
\pi_0\equiv\gamma_5=-1+2i\pmod {544\mathbb Z[i]},
\tag{28}
$$
排除有限坏素位。它是正密度素理想类，且 $p\equiv5\pmod {16}$。
[R284](R284-original-prime-core-derivative-splitting-and-paid-primitive-transfer.md) 的实际相位为 $\mu_8=-1$，所以在本篇原正空间上
$$
T_p=-\mathscr N,\qquad T_pS_r=-\zeta^rS_r.
\tag{29}
$$
由原 p-depletion
$$
S_r^\times(z)=S_r(z)-b_{17}^{-1}(T_pS_r)(pz/b_0^2)
$$
读取常数项，得到完整单位 Mellin 的质量
$$
\boxed{M_{S_r}(0)=1+\frac{\zeta^r}{b_{17}}.}
\tag{30}
$$
这里 $b_{17}\in K\subset\mathbb Q_p$ 是已固定的原单位；绝不以未去 Euler 的 $S_r(0)$ 代替 (30)。

**定理 2。** 在 (28) 的所有相应好素位，对全部 $r\in\mathcal R$，(30) 是所在系数域局部整数环的单位。

**证明。** 若 (30) 模该素位为零，则 $\overline{\zeta^r}=-\bar b_{17}$ 属于 $\mathbb F_p^\times$。但这些 $r$ 的 $\zeta^r$ 的准确阶是 $8$ 或 $16$；其阶在奇素数处约化不变。而 $p\equiv5\pmod {16}$ 给 $v_2(p-1)=2$，$\mathbb F_p^\times$ 不含阶 $8$ 或 $16$ 的元素，矛盾。$\square$

(27)、(30) 现已支付了所有十二个质量。若统一参考为 $J_8$，真实的质量修正导数仍是
$$
\left.\frac d{du}\frac{M_{S_r}(u)}{J_8(u)}\right|_{u=0}
=\frac{M_{S_r}'(0)}{J_8(0)}
 -\frac{M_{S_r}(0)J_8'(0)}{J_8(0)^2}.
\tag{31}
$$
本篇所识别的复中心值和完整质量并不赋值给 (31)。后续原 tame-one primitive 比较必须使用 R283 的实际
$\Omega_0^{-1}M_{G,1}(u+1/(p-1))$，并保其连接项；该分支不在本篇中重命名为 (24) 的中心值。

## 7. 精确证书与引用

[脚本](../scripts/check-extra-twelve-cm-characters-and-central-masses.py) 和
[输出](../scripts/check-extra-twelve-cm-characters-and-central-masses.json)
给出 140 项准确检查，涵盖：

- 原 half-$(-,-)$ 的四个特征投影、完整 Rao 相位及 (12)；
- (18)、(23) 的原局部单位关系和 norm-five 定向；
- 全部十二个原 $P_r$ 的真实矩阵特征式、每个系数的实性及质量一；
- 从原三个 $T_k$ 重新计算的全部三十六个非零投影质量；
- 四个准确 Galois 轨道、(25) 的最小多项式与 (30) 的单位条件。

整个计算只在固定的 $\mathbb Q[\zeta]/(\zeta^8+1)$ 中进行；没有扫描变化的目标素数，也没有用拟合的 theta 值代替原来源。

文献：

1. Tonghai Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math. **485** (1997), 25–53；§2.1、Theorem 2.6、Corollaries 2.4/2.14、Theorem 2.15。[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
2. Kenneth A. Ribet, *Abelian varieties over Q and modular forms* (1992), §3 开头的权二新形式 Abel 簇构造；其中引用 G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (1971), Theorem 7.14。[作者预印本](https://arxiv.org/abs/alg-geom/9208002)。
3. 本仓库原来源与完整转置：[R239](R239-third-rank2-curve-and-original-sixteen-coset-transport.md)、[R248](R248-ray17-conjugate-trace-and-original-yang-projections.md)、[R282](R282-true-prime-core-mellin-transfer-and-original-primitive-orbit.md)、[R283](R283-original-first-order-primitives-cm-boundary-and-tame-central-rows.md)、[R284](R284-original-prime-core-derivative-splitting-and-paid-primitive-transfer.md)。
