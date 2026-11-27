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

## 8. 原 full47 的同时普通、全 Hecke 分裂及标签非退化素

本节只消费已经认证的固定原输入，不搜索替代当前辅助素数。
令 $p=47$，$X=X_{\rm ns}^+(47)$，$J=\operatorname{Jac}(X)$，
并令 $\mathbb T\subset\operatorname{End}_{\mathbf Q}(J)$ 为原整数
Hecke 代数。[R1080](R1080-certified-full-level47-Jacobian-rank.md)
§§1–3 给出同一个完整新 Fricke 正号谱：
$$
A=\mathbb T\otimes\mathbf Q
 =F_{16}\times F_{24}\times F_{33},\qquad
[F_d:\mathbf Q]=d,\qquad \dim_{\mathbf Q}A=\dim J=73.
\tag{1112.26}
$$
这里的下标表示三个实际系数域的次数，分别对应 R1080 固定分解
中的因子 $8,10,11$；不是仅用局部有限类型猜出的系数子域。
每个共轭新形式在原 Hodge 谱中出现一次。

令 $\widetilde F_d$ 为 $F_d/\mathbf Q$ 的正规闭包。
其 Galois 群忠实作用于 $d$ 个嵌入，故阶整除 $d!$。
由于 $16,24,33<47$，三个正规闭包的次数都与 $47$ 互素。

R1074 的八个原 $\mathbf Q$-有理 CM 点，其 endomorphism order
分别属于以下四个虚二次域：
$$
M_{\rm CM}=\mathbf Q(i,\sqrt{-2},\sqrt{-3},\sqrt{-7}).
\tag{1112.27}
$$
这个合成场是有限 $2$-扩张，因而次数与 $47$ 互素。
定义明确的有限 Galois 场
$$
E=\mathbf Q(\zeta_{47})\,
   \widetilde F_{16}\widetilde F_{24}\widetilde F_{33}M_{\rm CM}.
\tag{1112.28}
$$
在 $K=\mathbf Q(\zeta_{47})$ 上，其次数整除上述正规闭包和
$M_{\rm CM}$ 的次数乘积，所以
$$
47\nmid[E:K].
\tag{1112.29}
$$
无须知道这些闭包的实际 Galois 群，也不假设它们彼此不交；
这里只用每个阶与 $47$ 互素。

[R1072](R1072-certified-original-p47-cuspidal-disk-labels.md)
已在原相位和原函数基中认证
$$
W_{\rm good}=V=
 \bigoplus_{R=26,28,\ldots,44}V_{\omega^R},\qquad d=10.
\tag{1112.30}
$$
因此应用 §6，存在准确 Dirichlet 密度
$$
\boxed{\qquad
\frac{(46/47)^{10}}{[E:\mathbf Q]}>0
\qquad}
\tag{1112.31}
$$
的有理素数 $q$，使 $q$ 在 $E$ 完全分裂，且全部十个原
$B_{\chi,q}$ 同时非零。以下再删一个固定有限素集，不改变密度。

第一，$q\equiv1\pmod{47}$，原全部 $23$ cusps 有理，
且 (1112.20) 在整个原十维全局标签空间上为同构。
R1072 的 $235$ 个不同实际候选在这些素数处保持不同。
这只是不同全局候选之间的非合并；不称原全部
$X(\mathbf F_q)$ 的标签映射自动单射。

第二，删去八个已指定 CM 椭圆曲线模型的坏素数及其 CM order
的 conductor 素数。由于 $q$ 分裂于 (1112.27) 的每个虚二次域，
八个原 CM 点对应的椭圆曲线均普通约化。
可以从实际 CM 作用直接核此结论：在 $q$-divisible group 上，
$\mathcal O_{\rm CM}\otimes\mathbf Z_q=\mathbf Z_q\times\mathbf Z_q$
的两个 idempotents 被主极化的 Rosati 对合交换，因而分出的
两个因子高度相同、均为一；其总维数为一，
因此一个因子乘法型、另一个 étale，正是普通约化。
本节保留原 CM 点上的 canonical $47$-Cartan，
不把任一普通椭圆曲线的某条新 necklace 代入。
若需要八个特殊纤维点彼此不同，可另外删去八个互异整数
$j$-值之差的素因子，仍只删有限集。

第三，置
$$
\mathcal O_A=\mathcal O_{F_{16}}\times
             \mathcal O_{F_{24}}\times\mathcal O_{F_{33}}.
$$
原 Hecke 特征值为代数整数，故
$\mathbb T\subset\mathcal O_A$；由 (1112.26)，二者是同秩
$73$ 的 $\mathbf Z$-格，指数有限。删去
$[\mathcal O_A:\mathbb T]$ 和三个域判别式的素因子。
在 $E$ 完全分裂便给出三个真正系数域的全部一次无分歧完成域，
从而
$$
\boxed{\quad
\mathbb T\otimes\mathbf Z_q
 =\mathcal O_A\otimes\mathbf Z_q
 \simeq\mathbf Z_q^{\,73}.
\quad}
\tag{1112.32}
$$
这是真实最大整 Hecke order 的陈述，不是把某个非极大 order
的剩余线性角色冒作一次完整因子。

在这些 $q\ne47$ 上，原 $J$ 的阿贝尔模型良好。
整数 Hecke endomorphisms 延伸到模型，(1112.32) 的整 idempotents
逐个作用于其 Hodge 和 Lie 格。每个格在泛纤维的各因子上秩一，
且本身 $\mathbf Z_q$-无挠；故各因子是自由秩一的 $\mathbf Z_q$-模。
于是 Hodge 与 Lie 格均为
$\mathbb T\otimes\mathbf Z_q$ 上的自由秩一模。
这也可按 R1083 §6 已付的原整格论证直接消费；
没有使用 Chen 同源的未经验证整运输。

所以，八个真实 CM 点的普通约化、完整原 Hecke 代数的
$73$ 个一次整块，以及十个原圆单位的同时非零读数，
可以由同一组正密度辅助素同时满足。这排除了这些已指定条件
之间潜在的 Galois 冲突。

本节不给最小这样的 $q$，不搜索或替换当前 $4513$，
不保证 $q\nmid\#J(\mathbf F_q)$，不保证新的 CM 对数或高度为单位，
也不将这些素数自动放进 §7 的有效有限筛选范围。
当前 $4513$ 的已认证矩阵、对数、高度和正在进行的实际有限
第三类微分计算保持其原来源；本节没有重跑其中任何输入。


## 9. 同一原圆单位扩张的精确导子和判别式

本节仍对全部 $p>37$，不加 regular 假设。
令 $\mathcal I_0$ 是 $\mathcal I$ 的任一非空子集，按
$$
\chi_i=\omega^{r_i},\qquad
2\le r_1<\cdots<r_{d_0}\le p-3,\qquad r_i\text{ 偶},
\qquad d_0=|\mathcal I_0|
\tag{1112.33}
$$
排列，始终使用 (1112.4) 的原类 $\beta_{\chi_i}$。
定义
$$
L_0=K(\epsilon_{\chi_i}^{1/p}:1\le i\le d_0).
$$
这是 (1112.7) 的实际子扩张；特别可以取 $\mathcal I_0=\mathcal I$，
或只取 R1069 的 forced good 角色。

**精确结论为**
$$
\boxed{\quad
|\operatorname{Disc}(L_0/\mathbf Q)|=p^{D_0},\qquad
D_0=p^{d_0}(p-2)
 +(p-1)\sum_{i=1}^{d_0}p^{d_0-i}(p+1-r_i).
\quad}
\tag{1112.34}
$$
$p$ 在 $L_0/\mathbf Q$ 中完全分歧，没有别的有限分歧素数。
因此
$$
\boxed{\quad
\operatorname{rd}(L_0)
 =p^{\,\frac{p-2}{p-1}
           +\sum_{i=1}^{d_0}\frac{p+1-r_i}{p^i}}
 <p^2.
\quad}
\tag{1112.35}
$$
这里的根判别式属于原圆单位场；没有另选同维的 Kummer 空间。

### 9.1 真实单位的准确局部深度

令 $K_p=\mathbf Q_p(\zeta_p)$，$\pi=\zeta_p-1$，取
$v_{K_p}(\pi)=1$。于是 $v_{K_p}(p)=p-1$。
记 $\overline U_n$ 为 $1+\pi^n\mathcal O_{K_p}$ 在
$K_p^\times/K_p^{\times p}$ 中的像。

R1062 (1062.23) 给出的正是原圆单位的截断对数。
对 $\chi_i$ 投影，其最低项为
$$
\log\beta_{\chi_i}
 \equiv
 \frac{B_{r_i}(a^{r_i}-1)}{r_i\,r_i!}\,\pi^{r_i}
       \pmod{\pi^{r_i+1}}.
\tag{1112.36}
$$
式 (1112.36) 表示：先把原类在实局部域中取 principal-unit
代表，再取实际收敛对数。非平凡角色的 Teichmüller 常数可由局部
$p$ 次幂去掉；不把 $\eta_a/a$ 当作全局单位。
因为实局部域的绝对分歧指数为 $(p-1)/2$，其 principal units
从 $K_p$ 的 $\pi^2$ 层开始，log/exp 在这里互逆且保最低赋值。

good 条件、$a^{r_i}\ne1$ 及 $r_i<p$ 使显示系数为单位。
模 $p$ 群环幂等元的不同整数提升只改 $p$ 次幂类，
并不改变上述深度：若 $v\in K_p^\times$ 且 $v^p\equiv1\bmod\pi$，
则其剩余类是 $1$，从而 $v=1+w$、$v_{K_p}(w)\ge1$；
二项式展开给
$$
v_{K_p}(v^p-1)\ge p.
\tag{1112.37}
$$
所以在严格小于 $p$ 的各层，局部 $p$ 次幂不能消掉已显示的首项。
因此准确有
$$
\beta_{\chi_i}\in\overline U_{r_i}
                      \setminus\overline U_{r_i+1}.
\tag{1112.38}
$$

对任一非零组合
$\beta=\sum_i b_i\beta_{\chi_i}$，若 $i_0$ 为首个 $b_i\ne0$ 的指标，
不同 $r_i$ 使最低项不能相消，故其准确深度是 $r_{i_0}$。
特别这些原类在 $K_p^\times/K_p^{\times p}$ 中仍线性独立。
这重新付清所需的局部 restriction，而不是只用全局角色独立。

### 9.2 一个深度为 r 的原 Kummer 线

所需标准局部公式可核于 C. S. Dalawat，
[*Further remarks on local discriminants*](https://arxiv.org/pdf/0909.2541)，arXiv:0909.2541v2，
§1，印刷第2页：包含 $\mu_p$ 的局部域上，深度为 $r$ 的非未分歧
Kummer 线的唯一 ramification break 为 $pe_1-r$。
本题 $e_1=1$，故 break 为 $p-r$，导子为 $p-r+1$。

为固定本题全部赋值和 $+1$，这里再直接证明。
取代表
$$
a_r=1+c\pi^r,\qquad c\in\mathcal O_{K_p}^{\times},
\qquad 2\le r\le p-3,
$$
并令 $\alpha^p=a_r$、$z=\alpha-1$。
多项式
$$
(1+z)^p-1-c\pi^r
$$
的 Newton polygon 是从 $(0,r)$ 到 $(p,0)$ 的单线段：
中间二项式系数的赋值均为 $p-1>r$。
所以 $v_{K_p}(z)=r/p$，扩张 $M_r=K_p(\alpha)$ 的次数和分歧指数
均为 $p$。取 $v_{M_r}$ 为整数归一化，则
$$
v_{M_r}(\pi)=p,\qquad v_{M_r}(z)=r.
$$
选 $1\le A\le p-1$ 和 $B\in\mathbf Z$ 使 $Ar+Bp=1$；
$\varpi=z^A\pi^B$ 是 $M_r$ 的 uniformizer。
对任一非恒等 $g\in\operatorname{Gal}(M_r/K_p)$，
有 $g(\alpha)=\zeta_p^j\alpha$、$p\nmid j$，因此
$$
v_{M_r}\left(\frac{g(z)}z-1\right)
 =v_{M_r}\left(\frac{(\zeta_p^j-1)\alpha}{z}\right)
 =p-r.
$$
$A$ 为单位，所以
$$
v_{M_r}(g(\varpi)-\varpi)=1+p-r.
\tag{1112.39}
$$
循环 $p$ 群只有这一处 lower break；upper break 相同。
每个非平凡一维角色的 Artin 导子准确为 $p+1-r$。
这也排除深度为 $r$ 的类给出未分歧扩张的可能。

### 9.3 全分歧与全部角色的计数

(1112.38) 使 $L_0$ 在唯一 $p$ 位的局部次数为 $p^{d_0}$，
等于其全局相对次数。任一 degree-$p$ 子扩张对应一个非零
Kummer 线，其深度由 §9.1 决定，且均由 §9.2 分歧。
若局部 $L_0/K_p$ 有非平凡未分歧商，由其 elementary abelian
Galois 群会得到一个未分歧 degree-$p$ 商，矛盾。
故局部扩张全分歧，且 $p$ 在全局 $L_0$ 中只有一个素点。

Kummer pairing 把
$\operatorname{Hom}(\operatorname{Gal}(L_0/K),\mu_p)$
参数化为这些原类。这里计数的是 Galois 群的非平凡**对偶角色**，
不是把 (1112.11) 的 $\omega\chi^{-1}$ 再当成单位深度。

首个非零指标为 $i$ 的组合恰有
$(p-1)p^{d_0-i}$ 个，每个导子指数为 $p+1-r_i$。
导子—判别式公式因此给
$$
v_{\mathfrak p_K}(\mathfrak d_{L_0/K})
 =(p-1)\sum_{i=1}^{d_0}p^{d_0-i}(p+1-r_i).
\tag{1112.40}
$$
这个标准公式及其 cyclic-character 计数也可直接核于 Dalawat
同文 §4，印刷第15页。原单位使 $p$ 外无分歧，见 §2。
再用 $|\operatorname{Disc}K|=p^{p-2}$、
$N_{K/\mathbf Q}(\mathfrak p_K)=p$ 和判别式塔公式，
得到 (1112.34)。除以 $[L_0:\mathbf Q]=(p-1)p^{d_0}$ 得 (1112.35)。
因 $r_i\ge2$，
$$
\sum_{i=1}^{d_0}\frac{p+1-r_i}{p^i}
 \le (p-1)\sum_{i=1}^{d_0}p^{-i}=1-p^{-d_0},
$$
故其指数严格小于 $2$。

若 $\mathcal I_0$ 仅取原 forced good 角色，
$r_i=p-1-2j_i$、$1\le j_i\le\lfloor p/4\rfloor-1$，
便有
$$
p+1-r_i=2j_i+2\le2\lfloor p/4\rfloor\le(p-1)/2.
$$
因此更准确地
$$
\operatorname{rd}(L_0)
 <p^{\,\frac{p-2+2\lfloor p/4\rfloor}{p-1}}
 \le p^{\,3/2-1/(p-1)}<p^{3/2}.
\tag{1112.41}
$$
R1069 保证这种 forced good 子集可以取维数
$\Omega(p/\log p)$，但这个维数下界不是判别式证明的额外假设。

## 10. 以原单角色场代替整大场的有效计数接口

仍用原全部 $\mathcal I$、$d=|\mathcal I|$，令
$$
L_\chi=K(\epsilon_\chi^{1/p}).
$$
每个 $\beta_\chi$ 的线在 $\Delta$ 下稳定，故
$L_\chi/\mathbf Q$ 为 Galois，
$$
[L_\chi:\mathbf Q]=p(p-1),\qquad
|\operatorname{Disc}L_\chi|
 =p^{\,p(p-2)+(p-1)(p+1-r_\chi)}
 <p^{\,2p^2}.
\tag{1112.42}
$$
这里不把 $L_\chi$ 换成任意 degree-$p(p-1)$ 场。
若只消费 forced good 角色，同式指数还严格小于 $3p^2/2$。

令 $\pi_{\rm spl}(M;x)$ 计数不超过 $x$、
在指定 Galois 场 $M/\mathbf Q$ 中完全分裂的有理素数。
$p$ 不计入。令 $\pi_{\rm good}(x)$ 计数 (1112.17) 的实际同时非零素数。
对 $\ell$ 在 $K$ 完全分裂，
$$
B_{\chi,\ell}=0
 \quad\Longleftrightarrow\quad
\ell\text{ 在 }L_\chi\text{ 完全分裂}.
\tag{1112.43}
$$
这来自同一个 arithmetic Frobenius/Kummer pairing (1112.13)，
不是一个平均密度的替代。
于是逐素数的集合并集界给出完全有效的恒等输入
$$
\boxed{\quad
\pi_{\rm good}(x)\ge
\pi_{\rm spl}(K;x)-
 \sum_{\chi\in\mathcal I}\pi_{\rm spl}(L_\chi;x).
\quad}
\tag{1112.44}
$$

特别，若对这些**次数至多 $p(p-1)$ 的实际场**已经取得某些明确误差
$$
\left|\pi_{\rm spl}(K;x)-\frac{\operatorname{Li}(x)}{p-1}\right|
 \le E_K(x),
\qquad
\left|\pi_{\rm spl}(L_\chi;x)
 -\frac{\operatorname{Li}(x)}{p(p-1)}\right|
 \le E_\chi(x),
$$
则不经过 degree $(p-1)p^d$ 的全扩张误差，直接得到
$$
\pi_{\rm good}(x)\ge
 \frac{1-d/p}{p-1}\operatorname{Li}(x)
 -E_K(x)-\sum_{\chi\in\mathcal I}E_\chi(x).
\tag{1112.45}
$$
$1-d/p>1/2$ 已由 (1112.3) 支付。
式 (1112.44) 无需任何解析假设；式 (1112.45) 则明确把所需解析
输入单列，不在这里未经证明给出误差的大小。

同样可以在 §6 的指定 $E$ 完全分裂的素数中逐一去掉
$EL_\chi$ 的完全分裂素数；交域仍由 (1112.23) 支付。
但这时实际场的次数和判别式须另计，不能继续使用 (1112.42)
冒称附加分裂条件没有代价。

本节给出避免整 $p^d$ 次场粗误差的具体入口，
没有证明存在所需素数小于 $p^2/4$，没有证明它落在 (1064.39)
尚可能有筛力的区间，也没有计算原同点曲线像。
小根判别式本身不推出小辅助素或非 CM 候选排除。
所有既有有限计算、源文件及 pin 均保持不变；本附节没有运行数学程序。



## 11. 原同时非退化素的无条件有效上界

本节只把 §9 的准确 conductor 接到已发表的有效 Chebotarev
定理，不改变原圆单位、角色或辅助读数。仍取任一非空原 good
子集 $\mathcal I_0$，令 $d_0=|\mathcal I_0|$、$r_{\min}=r_1$，
以及 §9 的同一个 $L_0/K$。记 $\ell_{\mathrm{faith}}$ 为满足
$
\ell\equiv1\pmod p,\qquad
B_{\chi,\ell}\ne0\quad(\chi\in\mathcal I_0)
$
的最小有理素数。这里 $B_{\chi,\ell}$ 始终是 (1112.19)
中由原 $\beta_\chi$、同一 arithmetic Frobenius 和同一
$\mu_p$-配对给出的读数；不是替换后的抽象非零坐标。

准确有无条件有效界
$
\boxed{\begin{aligned}
\ell_{\mathrm{faith}}\ll{}&
 p^{694(p-2)+521(p+1-r_{\min})}\\
&+p^{232(p-2)+367(p+1-r_{\min})}
       (p-1)^{290(p-1)}.
\end{aligned}}
\tag{1112.46}
$
隐含常数是绝对且可有效计算的，特别与 $p,d_0$ 和角色选择无关。
因此这是 $p^{O(p)}$ 的界，没有出现来自
$[L_0:\mathbf Q]=(p-1)p^{d_0}$ 的指数维数损失。

### 11.1 所用已发表定理及真正的 abelian subgroup

J. Thorner、A. Zaman，
*An explicit bound for the least prime ideal in the Chebotarev density theorem*，
Algebra & Number Theory **11** (2017), 1135–1197，
[正式全文](https://msp.org/ant/2017/11-5/ant-v11-n5-p04-s.pdf)，
Theorem 1.1，印刷第1137页（PDF第3页，以封面为第0页）。

该定理的准确输入是有限 Galois 扩张 $L/F$、共轭类
$C\subset\operatorname{Gal}(L/F)$，以及一个与 $C$ 相交的
abelian subgroup $A$。若 $K'=L^A$，
$
\mathcal Q(L/K')
 =\max_{\vartheta\in\widehat A}
      N_{K'/\mathbf Q}\mathfrak f(\vartheta),
$
则其定义 (1-3) 的最小 degree-one 素理想满足
$
P(C,L/F)\ll
 D_{K'}^{694}\mathcal Q(L/K')^{521}
 +D_{K'}^{232}\mathcal Q(L/K')^{367}
       [K':\mathbf Q]^{290[K':\mathbf Q]}.
\tag{1112.47}
$
定理的 degree-one 条件要求素理想范数为有理素数；
不是仅保证一个可能为高次素数幂的范数。
本文取 $F=\mathbf Q$，因而得到的就是实际有理辅助素。

在本题中，取
$
L=L_0,\qquad A=H_0=\operatorname{Gal}(L_0/K)
                     \simeq\mathbf F_p^{d_0}.
$
这是原扩张中的真正 abelian subgroup，其固定域准确为
$K=\mathbf Q(\zeta_p)$，并非一个只由次数猜出的子域。

由 (1112.11)，$\Delta$ 在 $H_0$ 的各一维分量上通过
$\omega\chi^{-1}$ 作用。任选一个在每个分量上都非零的
$h\in H_0$，并取它在 $\operatorname{Gal}(L_0/\mathbf Q)$
中的共轭类 $C$。$H_0$ 正规且自身交换，$\Delta$ 作用只乘各分量
的非零标量，所以
$
C\subset H_0,\qquad
C\subset\{v:\text{全部原分量均非零}\},\qquad
C\cap A\ne\varnothing.
\tag{1112.48}
$
因此 (1112.47) 的所有群论假设成立。
在 $C$ 中的 Frobenius 限制到 $K$ 为恒等，故
$\ell\equiv1\pmod p$；其全部原 Kummer 分量非零，
按 (1112.13) 恰给全部 $B_{\chi,\ell}\ne0$。
共轭只改变允许的共同相位，不能把非零读数变成零。
特别 $\ell_{\mathrm{faith}}\le P(C,L_0/\mathbf Q)$。

### 11.2 最大 conductor 与尺度代入

原 $L_0/K$ 只在 $\mathfrak p_K$ 分歧，
且 $N_{K/\mathbf Q}\mathfrak p_K=p$。
§9.1–9.3 已证明，每个非零 Kummer 组合的准确深度是
其首个非零角色的 $r_i$，相应一维 Galois 角色的导子指数是
$p+1-r_i$。这些是 $\widehat H_0$ 的全部非平凡角色。
故最大 conductor 准确为
$
\mathcal Q(L_0/K)=p^{p+1-r_{\min}}.
\tag{1112.49}
$
这里不乘 $d_0$，也不把所有角色的 conductor 乘积
（判别式）误作最大 conductor。最大值由原 $r_{\min}$
那条线实际取得。

再用
$
D_K=p^{p-2},\qquad [K:\mathbf Q]=p-1
$
代入 (1112.47)，即得 (1112.46)。
若只要一个较粗的单项写法，由 $(p-1)<p$，
第二项的指数至多
$
889p-387-367r_{\min}.
$
第一项的指数为 $1215p-867-521r_{\min}$；
二者之差
$
326p-480-154r_{\min}
 \ge172p-18>0
$
使用了 $r_{\min}\le p-3$。因而也可写为
$
\ell_{\mathrm{faith}}
 \ll p^{1215p-867-521r_{\min}}.
\tag{1112.50}
$
本证明保留了定理的完整两项，没有为删除第二项另加关于
$[K:\mathbf Q]$ 的适用条件。

### 11.3 这个有效界尚未支付的范围

(1112.46) 是同一原圆单位同时非退化条件的无条件有效存在性。
它可对 R1128 的全部实际 good 子模块使用，
并没有因该子模块的线性维数而失效。
但它不给 $\ell<p^2/4$，也没有把所给素数放进
R1064 (1064.39) 尚可能有筛选力的有限范围。
尤其不能从这个上界声称原曲线的同点像缺失。

附加普通性、Hecke 系数域分裂或其它指定场的完全分裂时，
须对实际合成扩张重新计算 (1112.47) 的固定域和最大 conductor；
§6 的定性相容性本身不允许沿用 (1112.46) 的数值参数。

所以本节关闭的是“原同时非退化素是否有一个不依赖指数次数
粗界的无条件有效上界”这一输入。它不声称局部允许标签就是
全局点，不证明任一非 CM 候选被原辅助点集排除，
也不改变主目标仍需真正同点像约束的范围。
无数学程序执行。


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

§§9–10（2026-11-27）新增原圆单位局部深度、全部导子、准确判别式和单角色并集计数接口；root/global_route/o2_high_coefficient 独立纸核，包括对偶角色计数、判别式塔与解析误差尚未支付的边界。未执行数学程序。

§11：root 已亲读 Thorner–Zaman 正式 Theorem 1.1、定义 (1-3)/(1-6)，独核真实 H₀/固定域、共轭类、最大 conductor、原 phase 非零条件及两项的准确代入与吸收。全节无数学程序执行。
