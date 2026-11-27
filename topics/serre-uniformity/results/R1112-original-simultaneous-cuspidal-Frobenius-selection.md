# R1112：原 good cuspidal 标签的同时 Frobenius 选素

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；global_route，o2 独立纸核。

**已证明。** 固定任意 $p>37$，保留 R1069 的原 Bernoulli-good
cuspidal 子模块及原圆单位基。存在正 Dirichlet 密度的有理辅助素
$\ell\equiv1\pmod p$，使全部这些圆单位的真实模 $\ell$ Kummer
读数同时非零。在这样的素数处，整个原 good 全局标签空间的
localization 是同构；不同的原全局候选不会因为某个圆单位坐标
约为零而合并。

若 good 角色数为 $d$，这组素数在全部有理素数中的准确 Dirichlet
密度为
$$
\frac{(1-1/p)^d}{p-1},
\tag{1112.1}
$$
在 $\ell\equiv1\pmod p$ 的素数中，其相对 Dirichlet 密度严格大于
$1/2$。还可同时要求在指定的、$K=\mathbf Q(\zeta_p)$ 之上次数与
$p$ 互素的有限 Galois 扩张中完全分裂；具体交域和密度在 §6 给出。

这付清实际圆单位读数的同时非退化，不付辅助素的有效大小、
原有限曲线标签像的缺失、CM 以外候选排除或盘内唯一性。
特别不能用 Chebotarev 的无穷多素数替代 R1064 的有效有限范围。
全文仅用纸面证明，无数学程序执行。

## 1. 同一个原子模块和圆单位基

置
$$
F=\mathbf Q(\zeta_p)^+,\quad K=\mathbf Q(\zeta_p),\quad
G=\operatorname{Gal}(F/\mathbf Q),\quad
\Delta=\operatorname{Gal}(K/\mathbf Q),\quad m=(p-1)/2.
$$
$\omega:\Delta\to\mathbf F_p^\times$ 是实际模 $p$ cyclotomic 字符。
所有下面的 $\chi$ 是非平凡偶字符，故从 $\Delta$ 因子化到 $G$。

沿用 R1062 的真实 $V=C_\Sigma[p]$、R1069 的
$$
W=W_{\rm good}=\bigoplus_{\chi\in\mathcal I}V_\chi,\qquad
d=|\mathcal I|.
\tag{1112.2}
$$
这里仅保留实际出现且 $p\nmid B_R$ 的 $\chi=\omega^R$。
每个 $V_\chi$ 一维，$V^G=0$，所以
$$
d\le m-1=(p-3)/2.
\tag{1112.3}
$$
不增加未出现的角色，不删除其它角色的类群项。

选择与 R1069 相同的奇整数 $a$，其在 $G$ 中生成 $G$，并置
$$
\eta_a=\zeta_p^{(1-a)/2}\frac{1-\zeta_p^a}{1-\zeta_p},
\qquad
\beta_\chi=e_\chi[\eta_a]\in F^\times/F^{\times p}.
\tag{1112.4}
$$
$\eta_a$ 是真正的实全局圆单位；不是可能带有限分母的
$\eta_a/a$。R1069 已证明每个 $\beta_\chi$ 非零，且它准确生成
$F(\{p\},p)_\chi$。

从群环幂等元的模 $p$ 系数选任意整数提升，可把
$\beta_\chi$ 表示为一个真正全局单位 $\epsilon_\chi\in\mathcal O_F^\times$。
不同提升只改变 $p$ 次幂类。以下扩张和剩余读数均依赖这个原类，
而不依赖所选单位代表。

R1069 给出的原全局标签空间准确是
$$
\mathscr L=\operatorname{Hom}_{\mathbf F_p[G]}
       (W,F(\{p\},p))
=\left\{\phi:\ \phi(u_\chi)=c_\chi\beta_\chi,\
                   c_\chi\in\mathbf F_p\right\},
\tag{1112.5}
$$
其中 $u_\chi$ 仍为 R1064/R1070 固定的原函数基。
R1071 的每个实际 $p$-local 候选就是这里一个确定的向量
$(c_\chi)_\chi$；本文不重定其尺度。

## 2. 第一条 restriction 与真实 Kummer 扩张

限制
$$
F^\times/F^{\times p}\longrightarrow K^\times/K^{\times p}
\tag{1112.6}
$$
是单射：随后作 $N_{K/F}$，在原群上是乘二，而 $p$ 为奇数。
不同 $\chi$ 的 $\beta_\chi$ 已在 $F^\times/F^{\times p}$ 中线性独立，
故在 $K$ 中仍独立。令
$$
B=\bigoplus_{\chi\in\mathcal I}\mathbf F_p\beta_\chi
       \subset K^\times/K^{\times p},\qquad
L=K(\epsilon_\chi^{1/p}:\chi\in\mathcal I).
\tag{1112.7}
$$
Kummer 理论于是给
$$
H=\operatorname{Gal}(L/K)
=\operatorname{Hom}_{\mathbf F_p}(B,\mu_p),\qquad
[L:K]=p^d.
\tag{1112.8}
$$
这里是同一原圆单位产生的扩张，不是任意同维的 elementary
abelian extension。

$B$ 在 $\Delta$ 下稳定，故 $L/\mathbf Q$ 正规：
$\sigma(\epsilon_\chi)$ 的类仍在 $B$ 中，其任意 $p$ 次根已经在 $L$；
改变根只乘 $\mu_p\subset K$。特征零给可分性。因此
$$
\Gamma=\operatorname{Gal}(L/\mathbf Q),\qquad
1\longrightarrow H\longrightarrow\Gamma\longrightarrow\Delta
\longrightarrow1,\qquad
|\Gamma|=(p-1)p^d.
\tag{1112.9}
$$
所有 $\epsilon_\chi$ 是全局单位，故 $L/K$ 在 $p$ 外未分歧。
可直接在 $p$ 外对 $X^p-\epsilon_\chi$ 用单位导数证明这一点。

必须保 Kummer 对偶的 cyclotomic 扭转。
配对
$$
\langle h,\beta\rangle
=\frac{h(\epsilon^{1/p})}{\epsilon^{1/p}}\in\mu_p
\tag{1112.10}
$$
$\Delta$-等变，$B_\chi$ 的角色是 $\chi$，
$\mu_p$ 的角色是 $\omega$，所以
$$
H=\bigoplus_{\chi\in\mathcal I}H_\chi,\qquad
H_\chi\simeq\mathbf F_p(\omega\chi^{-1}).
\tag{1112.11}
$$
这是 R1064 的实际 cover 群
$\operatorname{Hom}(W,\mu_p)$ 的同一个角色方向：
使用原基 $u_\chi\mapsto\beta_\chi$ 即把两者识别。
没有把 $\chi$ 换成其逆，也没有把 $H$ 当作常数 $\mathbf Q$-群。
不需要选择 (1112.9) 的一个分裂。

## 3. 同一原有限域读数就是 Frobenius 配对

令 $\ell\ne p$ 且 $\ell\equiv1\pmod p$。
选择一个 $K$ 的 $\ell$ 上素点 $\mathfrak l$，
等价地选择实际剩余根
$$
z=\zeta_p\bmod\mathfrak l\in\mathbf F_\ell^\times.
$$
对每个原单位代表定义
$$
B_{\chi,\ell}(z)=
\log_z\left(\bar\epsilon_\chi^{\,(\ell-1)/p}\right)
\in\mathbf F_p,
\tag{1112.12}
$$
其中 $\log_z(z^b)=b\bmod p$。这正是 R1067/R1073
的 circular-unit localization，使用原 $\beta_\chi$、原根和原
$p$ 次幂 quotient。换代表的 $p$ 次幂不影响它。

取 $\mathfrak L\mid\mathfrak l$，用 arithmetic Frobenius
$h=\operatorname{Frob}_{\mathfrak L}(L/K)\in H$。
在 $\mathfrak L$ 处对 (1112.10) 约化：
$$
\langle h,\beta_\chi\rangle\bmod\mathfrak L
=\bar\epsilon_\chi^{\,(\ell-1)/p}.
\tag{1112.13}
$$
因为 Frobenius 在剩余域上作用为 $x\mapsto x^\ell$。
故
$$
B_{\chi,\ell}(z)\ne0
\quad\Longleftrightarrow\quad
h\text{ 在 }H_\chi\text{ 中的分量非零}.
\tag{1112.14}
$$
没有以任意同维 residue space 代替这个实际 Kummer pairing。

改变 $\mathfrak l$ 只对 $h$ 作 $\Gamma$-共轭。
按 (1112.11)，每个分量只乘非零标量，所以同时非零与所选素点无关。
也可直接核原 Weil-root 运输：若 $\chi=\omega^R$、$b\in\mathbf F_p^\times$，
则
$$
B_{\chi,\ell}(z^b)=b^{R-1}B_{\chi,\ell}(z).
\tag{1112.15}
$$
圆单位类受 $\sigma_b$ 乘 $b^R$，而离散对数的根从 $z$ 改为
$z^b$ 再乘 $b^{-1}$，给出准确的两个因子。
特别 $z$ 与 $z^{-1}$ 给同一个实剩余嵌入，但数值对数相反；
非零判据不变。

仅在 $F$ 完全分裂的 $\ell\equiv-1\pmod p$ 不属于这里。
那些素数的原 residue $p$-quotient 为零，不能计入同时非退化集合。

## 4. 准确密度与任意零坐标模式

在 (1112.9) 的实际群中定义
$$
S=\{h\in H:\ h_\chi\ne0\text{ 对所有 }\chi\in\mathcal I\}.
\tag{1112.16}
$$
$H$ 自身交换，$\Gamma/H$ 按 (1112.11) 逐分量伸缩，
所以 $S$ 是整个 $\Gamma$ 的共轭稳定子集。
其元素个数恰为 $(p-1)^d$。

有理素数的 Frobenius 落在 $H$，当且仅当它在 $K$ 完全分裂，
也就是 $\ell\equiv1\pmod p$。
再由 (1112.14)，Frobenius 类落在 $S$，
准确等价于这些素数的全部原 $B_{\chi,\ell}$ 非零。
Chebotarev 对这个有限、共轭稳定的集合给
$$
\delta\{\ell\equiv1\pmod p:\ B_{\chi,\ell}\ne0\ \forall\chi\}
=\frac{(p-1)^d}{(p-1)p^d}
=\frac{(1-1/p)^d}{p-1}.
\tag{1112.17}
$$
本篇的 $\delta$ 均为 Dirichlet 密度。

在 $\ell\equiv1\pmod p$ 中的相对密度为 $(1-1/p)^d$。
由 (1112.3) 和 Bernoulli 不等式，
$$
(1-1/p)^d\ge1-\frac d p
\ge\frac{p+3}{2p}>\frac12.
\tag{1112.18}
$$
这是对每个固定 $p$ 的准确同时选素结论，不使用 regular
素数的密度、Vandiver 或任何有限数值扫描。

更一般地，对任意固定 $\mathcal Z\subset\mathcal I$，
要求恰好 $\mathcal Z$ 中的读数为零、其它全部非零。
对应的群中集合仍共轭稳定，大小为 $(p-1)^{d-|\mathcal Z|}$，
所以它在 split primes 中的相对 Dirichlet 密度准确为
$$
p^{-|\mathcal Z|}(1-1/p)^{d-|\mathcal Z|}.
\tag{1112.19}
$$
这仅是零模式的陈述。没有在任意选择的数值原根下额外宣称
所有具体坐标值独立均匀；原根选择会同时改变 (1112.15) 的相位。

## 5. 对原同一全局候选的准确作用

在 $\ell\equiv1\pmod p$ 上，原 $H_W$ 的 Frobenius 为恒等，
故选择同一 $z$ 后
$$
H^1(\mathbf F_\ell,H_W)\simeq\mathbf F_p^{\mathcal I}.
$$
(1112.5) 的 localization 准确为
$$
\operatorname{loc}_{\ell,z}:\mathscr L\longrightarrow
\mathbf F_p^{\mathcal I},\qquad
(c_\chi)_\chi\longmapsto
(c_\chi B_{\chi,\ell}(z))_\chi.
\tag{1112.20}
$$
在 (1112.17) 的素数处这个对角映射是同构。
因此 R1071 的不同实际全局候选，在该素的完整读数仍然不同；
不能因为单个圆单位余数为零而错误合并候选。

原有理点仍须满足
$$
\operatorname{loc}_{\ell,z}\phi
=\delta_\ell(y_\ell),\qquad
y_\ell\in X_{\rm ns}^+(p)(\mathbf F_\ell),
\tag{1112.21}
$$
而右边的全部角色必须来自同一个 $y_\ell$。
(1112.20) 的同构没有计算 (1112.21) 的曲线点像，
也没有使它自动成为单射。
在有限实际算法中，仍须保全部 necklaces、twists 和 cusps；
本篇只去掉选择辅助素时的全部圆单位退化。

## 6. 同时附加真正 p-prime 次数的分裂条件

先精确设定附加场：令 $E/\mathbf Q$ 为有限 Galois 扩张，
满足
$$
K\subset E,\qquad p\nmid[E:K].
\tag{1112.22}
$$
因为 $[L:K]=p^d$，公共子域的次数同时整除 $p^d$ 和
$[E:K]$，所以
$$
L\cap E=K.
\tag{1112.23}
$$
等价地，第二条 restriction
$$
K^\times/K^{\times p}\longrightarrow E^\times/E^{\times p}
\tag{1112.24}
$$
仍单射：随后 norm 乘 $[E:K]$，其模 $p$ 可逆。
因此原全部 $\beta_\chi$ 在 $E$ 中仍独立，
$[LE:E]=p^d$，且
$[LE:\mathbf Q]=p^d[E:\mathbf Q]$。

在 $\operatorname{Gal}(LE/\mathbf Q)$ 中，
要求 Frobenius 限制到 $E$ 为恒等，再要求其
$\operatorname{Gal}(LE/E)\simeq H$ 的全部分量非零。
这是共轭稳定集合，恰有 $(p-1)^d$ 个元素。
所以这些有理素数的准确密度为
$$
\boxed{\quad
\frac{(1-1/p)^d}{[E:\mathbf Q]}.
\quad}
\tag{1112.25}
$$
在完全分裂于 $E$ 的素数中的相对密度仍是
$(1-1/p)^d>1/2$。可以再删除任意有限素集，不改变密度。

若起点只给 $M/K$ 有限 Galois、$p\nmid[M:K]$，可先取它的全部
$\Delta$-共轭场的合成 $E$。这些共轭均为 $K$ 上次数与 $p$ 互素的
Galois 扩张，其合成次数整除各次数的乘积；故 $p\nmid[E:K]$，
且 $E/\mathbf Q$ Galois。此时 (1112.25) 对这个明确的 $E$ 适用。

若输入是一个 $\mathbf Q$ 上有限 Galois 场 $M$，
且 $p\nmid[M:\mathbf Q]$，应先取
$$
E=KM.
$$
此时 $p\nmid[E:K]$，从而 (1112.23) 是
$L\cap KM=K$；不写成未加 $K$ 的错误交域等式。

若只给非 Galois $M/\mathbf Q$，
必须要求其 Galois 闭包的次数与 $p$ 互素。
单独 $p\nmid[M:\mathbf Q]$ 不足。
一个直接充分条件是 $[M:\mathbf Q]<p$：
其 Galois 闭包嵌入对这 $[M:\mathbf Q]$ 个嵌入的对称群，
阶整除 $[M:\mathbf Q]!$，因此与 $p$ 互素。
有限多个这样已指定的场的 Galois 闭包合成，次数仍与 $p$ 互素。

因此，对实际已付定义域及上述次数条件的 CM 代表、系数域或其它
有限辅助来源，可同时要求完全分裂和 (1112.20) 非退化。
这里不把 CM 共轭的 norm 当作某一个局部 embedding 的标签，
不从“CM”一词自动推断次数条件，也不宣布所选 CM 代表是
$\mathbf Q$-有理点。

## 7. 精确范围与已登记结果的区别

R1067 给原标签只在 $p$ 支撑，R1069 给 good 角色的唯一全局提升，
R1070 给实际 division-polynomial 辅助读数，R1071 给原全部
$p$-local 有限候选。本篇在这些条目连同 R1062、R1064–R1066、R1068 的完整文本中
检索，并回读所用规范化、角色、剩余读数和有限范围各节，
未见已经登记本篇的
同时 Kummer-Frobenius 密度及附加分裂场结论。
原有可见性只检查 $\operatorname{Frob}_\ell$ 在 $H_W$ 上是否为一；
本篇另外检查实际全局圆单位的 Frobenius 配对是否同时非零。

另一方面，R1064 §8 / R1067 §7 已严格证明：
固定 $p$ 的这个 étale twist 家族，在足够大的辅助素处
每个 twist 都有有限域点。
所以本篇无穷多的同时非退化素数并不自动提供无穷多个排除条件。
(1112.17)–(1112.25) 不给最小辅助素的有效上界，
不证明有一个这样的素数落在实际有筛选力的有限范围，
也不证明 (1112.21) 排除非 CM 候选。
Serre 主目标和 O0 的统一共同像问题保持开放。

## 来源与纸核

- [R1062](R1062-original-full-nonsplit-cuspidal-kummer-descent.md)：
  原 cusp 模块、角色与完整规范化。
- [R1067](R1067-original-cuspidal-labels-supported-only-at-p.md) 和
  [R1069](R1069-all-prime-good-cuspidal-characters-and-unique-global-labels.md)：
  原 $p$-only 全局空间、原 $\beta_\chi$ 及逐角色唯一性。
- [R1070](R1070-original-cuspidal-labels-by-division-polynomial-values.md)、
  [R1071](R1071-original-p-local-cuspidal-label-polynomials.md)：
  不更换的原有限域读数与全部实际候选。
- J. S. Milne, *Class Field Theory*, version 4.03 (2020)，
  [作者全文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)。
  已亲读 VII Appendix A, Theorem A.3 和 Proposition A.5
  （印刷 pp.226–227，PDF pp.235–236）；
  VIII §5.2–5.3 的实际 power-residue/Frobenius 对应
  （印刷 pp.244–245，PDF pp.253–254）；
  VIII Theorem 7.4 的共轭稳定集 Dirichlet 密度
  （印刷 p.259，PDF p.268）。
  只使用这三个标准原始输入；本篇角色、群中集合、两个 restriction、
  exact density 和原标签应用均在正文逐项证明。

o2 独立纸核 norm=2 的单射、$\omega\chi^{-1}$ 方向、
同一实际 Kummer residue pairing、共轭稳定集与附加场交域。
无本地或其它数学程序执行。
