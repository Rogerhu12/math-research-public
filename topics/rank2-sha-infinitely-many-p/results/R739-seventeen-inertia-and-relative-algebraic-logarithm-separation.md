# R739 — 两个实际三次点相对十七处分歧的对数分离

日期：2026-11-15。**状态：已证明。**

本篇将 R733 的两个实际代数点，与十七处不分歧扩张中的**全部代数点**分离，而不限于另外两个已知点。结论对每个选定的 p-adic 嵌入成立；辅助域可以随 p、深度和实际条件改变，且允许在 p 处任意分歧。

因此，若一个实际返回行已被完整识别为十七处不分歧域中的椭圆点对数，则它不能消去 R735 两条负一矩的非平凡代数组合。本篇不将“一个局部 Schwartz 因子不分歧”直接升级成这个点身份；原四单位部分和所有外部条件仍须保留。

## 1. 同两个点与同一个三次扩张

令
\[
 K=\mathbb Q(\omega),\quad \omega^2+\omega+1=0,\qquad
 t^3=17,\quad L=K(t),\quad E_1:y^2=x^3+1.
 \tag{1}
\]
保 R733 的
\[
 P_2=(-4,15)\in E_{289}(\mathbb Q),\qquad
 P_4=(42,397)\in E_{83521}(\mathbb Q)
\]
和实际同源模型同构
\[
 Q_2=(-4/t^2,\,15/17),\qquad
 Q_4=(42/t^4,\,397/289)\quad\text{于 }E_1(L).
 \tag{2}
\]
R733 已证明两点非扭。所有 E_1 的几何端同态都定义在 K 上，
\(\operatorname{End}_{\overline{\mathbb Q}}E_1=\mathbb Z[\omega]\)。

十七在 K 中惰性。多项式 \(X^3-17\) 在唯一的十七处是 Eisenstein 多项式，故 L/K 在该处全分歧，次数三。因为 K 包含 \(\mu_3\)，L/K 是循环扩张。取
\[
 \sigma(t)=\omega t.
\]
在代数点上，准确有
\[
 \sigma Q_2=[\omega]Q_2,\qquad
 \sigma Q_4=[\omega^2]Q_4.
 \tag{3}
\]
这些等式只作用于代数点。没有把十七处的 Galois 元看成所选 \(\mathbb C_p\) 的连续自同构。

## 2. 相对任意线性不交辅助域的真实点分离

**命题 1。** 设 F/K 是任意有限扩张，满足
\[
 F\cap L=K.
 \tag{4}
\]
若 \(a,b\in\mathbb Z[\omega]\)、\(R\in E_1(F)\)，并且
\[
 [a]Q_2+[b]Q_4+R
\]
是扭点，则 \(a=b=0\)，且 R 是扭点。

**证明。** L/K 是三次 Galois 扩张，(4) 使
\(\operatorname{Gal}(LF/F)\simeq\operatorname{Gal}(L/K)\)；
因此可将 (3) 的 \(\sigma\) 延到 LF，使其逐点固定 F。
所有端同态系数均被它固定。

先对给定关系作用 \(\sigma-1\)，再作用
\(\sigma-[\omega^2]\)。扭点仍映为扭点，而 R 被第一步消掉，Q_4 被第二步消掉。因此
\[
 [a(\omega-1)(\omega-\omega^2)]Q_2
 \quad\text{是扭点}.
 \tag{5}
\]
若 a 非零，(5) 中的端同态非零，因而是有限核的同源映射。非扭点不可能被它映成扭点：若目标被整数 n 杀掉，Q_2 就落在非零同源映射 \([n a(\omega-1)(\omega-\omega^2)]\) 的有限核中。这与 (2) 的非扭性矛盾。故 a=0。第一次差分随后给
\([b(\omega^2-1)]Q_4\) 扭，按同一理由 b=0。原关系再给 R 扭。证毕。

清除端同态的整数分母，同一结论适用于
\(E_1(\overline{\mathbb Q})\otimes_{\mathbb Z}\mathbb Q\) 上的 K 线性关系。换言之，Q_2、Q_4 相对
\(E_1(F)\otimes_{\mathbb Z[\omega]}K\) 是两个独立的真实端同态方向。

若 F/K 在十七处不分歧，则 (4) 自动成立：三次扩张 L 的子域只有 K、L，而含 L 的扩张在十七处必有被三整除的分歧指数。因此本命题同时适用于所有这样的 F；不要求 F/K 本身 Galois。

## 3. 对所有 p 的代数系数对数分离

固定任意素数 p 及嵌入
\[
 \iota_p:\overline{\mathbb Q}\hookrightarrow\mathbb C_p.
\]
用微分 \(\omega_1=dx/(2y)\) 规范 E_1 的延拓形式对数
\(\log_{1,p}\)。

对任意有限定义域的局部完备化，E_1 的点群紧，且有一个有限指数的形式开子群。将点乘同一个足够大的整数，可使它们全部落在指数映射的定义域内。此处形式对数单射，故延拓对数的核恰为扭点。这也适用于坏约化的 p=2,3；不需要对原曲线换一个好约化素数。

**定理 2。** 设 F 满足 (4)，取任意有限个
\(R_1,\ldots,R_m\in E_1(F)\)。若
\(A,B,C_1,\ldots,C_m\in\overline{\mathbb Q}\) 满足
\[
 A\log_{1,p}(Q_2)+B\log_{1,p}(Q_4)
       +\sum_{j=1}^m C_j\log_{1,p}(R_j)=0,
 \tag{6}
\]
则 \(A=B=0\)。

**证明。** 从 \(R_j\) 生成的有限维 K 线性空间中选一组由实际点组成的基
\(S_1,\ldots,S_d\)，全部模扭处理。每个 \(R_j\) 的对数因此是这些 \(S_i\) 对数的 K 线性组合，且所有系数均为代数数。

命题1说明
\[
 Q_2,Q_4,S_1,\ldots,S_d
\]
模扭在 \(\operatorname{End}E_1\) 上独立。对数的端同态关系若为零，按对数核的说明将给出相应代数点的扭关系，因此它们的对数也在 \(\operatorname{End}E_1\) 上独立。

同乘一个非零整数使各点进入共同的局部指数域后，Fuchs–Pham 的 Theorem 2.2 适用于简单阿贝尔簇 E_1。该定理将这里的端同态独立性提升为
\(\operatorname{End}_{\overline{\mathbb Q}}(\operatorname{Lie}E_1)\) 系数的独立性。因为 Lie E_1 是一维，这个系数环就是 \(\overline{\mathbb Q}\)。共同整数只乘各对数一个非零代数因子，故原对数亦在 \(\overline{\mathbb Q}\) 上线性独立。

把 \(R_j\) 的 K 线性展开代入 (6)，由此独立性得 A=B=0。证毕。

一手来源为 Fuchs–Pham，
*Some applications of the p-adic analytic subgroup theorem*，
Glasnik Matematički 51(71) (2016), 335–343，
[作者期刊全文](https://web.math.pmf.unizg.hr/glasnik/51.2/51(2)-04.pdf)，
Theorem 2.2 及其 §3.2 证明。这里只使用其线性独立结论，没有声称这些对数代数独立。

令 \(K^{\mathrm{nr}(17)}\) 表示所有在十七处不分歧的有限 K 扩张的合成，并置
\[
 \mathcal L_{17,p}
 =\operatorname{Span}_{\overline{\mathbb Q}}
   \{\log_{1,p}(R):R\in E_1(K^{\mathrm{nr}(17)})\}.
 \tag{7}
\]
有限多个不分歧扩张的合成在十七处仍不分歧。因此定理2对每个有限线性组合适用，严格得到
\[
 \boxed{
 \bigl(\overline{\mathbb Q}\log_{1,p}(Q_2)
       +\overline{\mathbb Q}\log_{1,p}(Q_4)\bigr)
       \cap\mathcal L_{17,p}=\{0\}.
 }
 \tag{8}
\]
此外 (8) 左边所列两对数本身独立，所以它们在商空间
\(\mathbb C_p/\mathcal L_{17,p}\) 中仍张成二维空间。


### 3.1 代数常数与代数数的普通对数

若完整返回还含代数常数或代数数的标准 p-adic 对数，可令
\[
 \mathcal T_p=\overline{\mathbb Q}
   +\operatorname{Span}_{\overline{\mathbb Q}}
      \{\log_p(a):a\in\overline{\mathbb Q}^{\,\times}\},
 \qquad \log_p(p)=0.
 \tag{8a}
\]
则更强地有
\[
 \boxed{
 (\overline{\mathbb Q}\log_{1,p}Q_2+
  \overline{\mathbb Q}\log_{1,p}Q_4)
  \cap(\mathcal L_{17,p}+\mathcal T_p)=\{0\}.
 }
 \tag{8b}
\]
证明直接使用同篇 Fuchs–Pham Theorem 2.1：对一条椭圆曲线，它给出包含1、有限个代数数对数及椭圆对数的代数线性空间维数，等于1、普通对数的有理秩及椭圆对数的端同态秩之和。先各取实际对数的基，再用命题1，维数公式就给 (8b)。标准 \(\log_p\) 可通过整数幂、根单位及 p 的有理幂将每个代数输入归到主单位域；这些调整保持代数输入，且不改变所需线性关系。椭圆点仍如上同乘整数归到指数域。

(8b) 只针对显示的代数系数。若某个实际条件质量或未消周期仍是未经识别的 p-adic 系数，它并不因此落在 (8a) 中。

## 4. 原 E24 及所有十七单位六次扭曲的准确尺度

设 \(b\in K^\times\) 在十七处为单位，令
\[
 E_b:y^2=x^3+b,\qquad \vartheta^6=b.
\]
多项式 \(X^6-b\) 在十七的局部整数环上判别式为单位；等价地，其根均为单位且导数 \(6X^5\) 为单位。因此 K(\(\vartheta\))/K 在十七处不分歧。

原同构和微分为
\[
 \phi_b:E_b\longrightarrow E_1,\qquad
 (x,y)\longmapsto(x/\vartheta^2,y/\vartheta^3),\qquad
 \phi_b^*\omega_1=\vartheta\,\omega_b.
 \tag{9}
\]
若 R 定义在十七处不分歧的有限 F/K 上，则
\(\phi_b(R)\in E_1(F(\vartheta))\)，该域仍在
\(K^{\mathrm{nr}(17)}\) 中。对数的实际函子性给
\[
 \boxed{\log_{1,p}(\phi_b(R))
       =\vartheta\,\log_{\omega_b,p}(R).}
 \tag{10}
\]
这不是更换原积分变量；它是同一代数点同构的准确微分尺度。

特别 \(b=24\) 满足此条件。所以从原 E24 的代数点对数回 E_1 时，只要点定义域已证明在十七处不分歧，(8) 就适用。允许定义域在 p 处随实际层数增长；十七处不分歧是唯一在本结论中使用的局部域条件。

本段不适用于不加条件的 \(b=2312=8\cdot17^2\)：它的六次缩放在十七处具有三次分歧。第三原来源不能仅凭本段删除。

## 5. 回到 R735 的同两个负一矩

保 R735 的实际周期 \(\Omega_p\) 和两个原单位负一矩
\(I_{2,p},I_{4,p}\)。该篇已付
\[
 \Omega_p I_{k,p}=A_{k,p}\log_{1,p}(Q_k),\qquad
 A_{k,p}\in\overline{\mathbb Q}^{\,\times},\qquad k=2,4.
 \tag{11}
\]
其具体平方、Euler、有限向量及微分尺度均沿用该篇；本篇不要求
\(A_{k,p}\) 为单位或与 p 无关。

由定理2，若 \(a,b\in\overline{\mathbb Q}\) 不全为零，则
\[
 \boxed{
 \Omega_p(a I_{2,p}+b I_{4,p})
 \notin \mathcal L_{17,p}+\mathcal T_p.
 }
 \tag{12}
\]
包括 R734 的同一个实际组合
\[
 a=c/a_0,\qquad b=1/a_0
\]
在内，其已付代数非零系数不能被十七处不分歧代数点的任何有限对数组合抵消。

这里 F 和有限点集可以分别依赖 p、N、n；证明在每个实际有限集合上进行，不要求统一次数或在 p 处无分歧。但下列内容必须另行给出，才可把 (12) 用于原 R737 的外部：

1. 将对应完整条件积分识别为有限代数点对数的真实公式，包括全部 p 处扭角色、Euler 和 period。
2. 证明这些点的实际定义域在十七处不分歧；仅有某个局部球向量还不是这个域结论。
3. 同时保留原四单位部分、两条不同返回观察、条件质量与移动门。定理2不把这些未识别项赋零。

因此本篇支付的是**实际代数点身份之后的无条件分离步骤**。它没有提前支付点身份，也没有由局部角色或一个非零内行宣布原中央非零。

依赖：
[R733](R733-two-cubic-points-and-algebraic-independence-of-p-adic-logarithms.md)；
[R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)；
[R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)；
[R737](R737-common-depth-elimination-and-native-primitive-strips.md)。
