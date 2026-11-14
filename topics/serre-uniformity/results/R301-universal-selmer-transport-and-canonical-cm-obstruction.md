# R301：整 $j$ 同余的全域 Selmer 运输与实际 CM 非零障碍

日期：2026-11-13。状态：**已证明；全局必要条件，主要目标仍未完成。**

本文把 R258、R289 的实际模 $p$ 同余传到全局 Selmer 群。比较适用于全部有限数域及全部二次扭曲，包括在 $p$ 处高度分歧的扩域；并不要求原曲线在 $p$ 已经好约化。关键是在一个固定的小分歧好约化域上先延拓有限平坦同构，然后基变换、下降，而不是在任意大域上重新使用 Raynaud 的小分歧定理。

在双同域的一参数模型中，本文还找到一个实际非 CM 曲线的二次扭曲上的明确无限阶点。这迫使同一个指定 CM 扭曲的 $p$-Selmer 群非零，给出一个真正全局的排除条件。该条件不能改写成 CM 曲线必有正 Mordell–Weil 秩：Tate–Shafarevich 群的 $p$ 挠点必须保留。

## 1. 全域比较定理

给定椭圆曲线 $B/K$、素数 $p$ 及 $K$ 的位置 $v$，记
$$
\mathcal L_v(B)=
\operatorname{im}\left(B(K_v)/pB(K_v)
\longrightarrow H^1(K_v,B[p])\right).
\tag{301.1}
$$
这里的局部条件由该曲线本身的 Kummer 映射定义。对二次特征 $\chi$，$B^\chi$ 总是通常的二次扭曲；其模 $p$ 表示为 $B[p]\otimes\chi$。

**定理 301.1。** 设 $p>13$，$B_1,B_2/\mathbb Q$ 满足
$$
j(B_1),j(B_2)\in\mathbb Z,\qquad
\phi:B_1[p]\xrightarrow{\sim}B_2[p]
\quad\text{为实际 }G_{\mathbb Q}\text{-模同构}.
\tag{301.2}
$$
则对每个有限数域 $F/\mathbb Q$、每个二次特征
$\chi:G_F\to\{\pm1\}$，$\phi\otimes\chi$ 诱导
$$
\boxed{\operatorname{Sel}_p(B_1^\chi/F)
\xrightarrow{\sim}
\operatorname{Sel}_p(B_2^\chi/F).}
\tag{301.3}
$$
更准确地，利用 $\phi\otimes\chi$ 识别全局上同调后，这两个 Selmer 群是同一个子空间；每一个位置的 Kummer 子空间也分别相同。

这里没有限制 $[F:\mathbb Q]$、$F$ 在 $p$ 处的分歧或 $\chi$ 的导子。也没有假设 $\phi$ 保持 Weil 配对。结论只涉及模 $p$ Selmer 群，不能自动提升为模 $p^n$ 同构或 Mordell–Weil 群同构。

这是 Mazur–Rubin 的 Selmer companion 机制在当前潜在好约化范围的一个直接形式。其 Theorem 3.1 在表示素数处要求已经好约化，不能不加论证地直接套在 R258 的加性分支上；第 2–5 节补全所需下降。

## 2. 固定的小分歧好约化域

**引理 301.2。** 对两条在 $\mathbb Q_p$ 潜在好约化的椭圆曲线，$p>13$，存在有限 Galois 扩张 $L/\mathbb Q_p$，使得
$$
[L:\mathbb Q_p]\text{ 仅含素因子 }2,3,\qquad
e(L/\mathbb Q_p)\le12<p-1,
\tag{301.4}
$$
且两条曲线在 $L$ 上都好约化。

**证明。** 可取
$$
L=\mathbb Q_p(B_1[3],B_2[3]).
\tag{301.5}
$$
其 Galois 群嵌入
$\mathrm{GL}_2(\mathbb F_3)\times\mathrm{GL}_2(\mathbb F_3)$，所以次数整除 $48^2$，仅含素因子 $2,3$。

潜在好约化使 $T_3B_i$ 上的惯性像有限。核
$1+3M_2(\mathbb Z_3)$ 无非平凡有限阶元素：若非平凡元素写作
$I+3^sM$、$s\ge1$ 且 $M\not\equiv0\bmod3$，则取三次幂会把首个非零 $3$ 进阶数准确提高一，而取素于三的次幂保持该阶数，故任何有限次幂不可能等于 $I$。因此有限惯性在 $B_i[3]$ 上的作用忠实。模三惯性在 (301.5) 上平凡，故整个 $T_3$ 惯性平凡，由 Néron–Ogg–Shafarevich 判据得到好约化。

在剩余特征 $p>3$，潜在好约化的惯性像为温和循环群，阶
$$
e_i\in\{1,2,3,4,6\}.
\tag{301.6}
$$
这一事实也可从极小短模型直接得到。若极小判别式赋值为 $\delta_i$，整 $j$ 给
$3v_p(a_i)\ge\delta_i$、$2v_p(b_i)\ge\delta_i$，极小性给
$0\le\delta_i<12$。短模型判别式公式使
$\delta_i\in\{0,2,3,4,6,8,9,10\}$。在加入
$u_i=p^{\delta_i/12}$ 后作 $x=u_i^2X,y=u_i^3Y$，得到好模型；该扩张的分歧指数为
$12/\gcd(12,\delta_i)$，加入所需单位根只需不分歧扩张。反过来，任何好约化扩张的分歧指数都必须使 $e\delta_i$ 被十二整除。因此 (301.6) 正是最小好约化分歧指数。

两个惯性核都是同一温和惯性群中的开子群，其交的指数为
$\operatorname{lcm}(e_1,e_2)\le12$。有限惯性在模三上忠实，故这恰是 (301.5) 的分歧指数，证明 (301.4)。$\square$

若 $B_1[p]\simeq B_2[p]$，令 $\mathcal B_i/\mathcal O_L$ 为好约化阿贝尔概形。Raynaud, Corollaire 3.3.6(1)，在 (301.4) 下使 $\phi$ 及其逆唯一延拓为
$$
\widetilde\phi:\mathcal B_1[p]
\xrightarrow{\sim}\mathcal B_2[p].
\tag{301.7}
$$
唯一性保证两次复合为恒等。此后只对 (301.7) 作基变换，不再要求新的底域小分歧。

## 3. 好约化 Kummer 条件及素于 $p$ 的下降

令 $K$ 为任意特征零非阿基米德局部域，$\mathcal B/\mathcal O_K$ 为好约化模型。由有限域上的 Lang 定理及光滑 Hensel 提升，
$$
H^1_{\mathrm{fppf}}(\mathcal O_K,\mathcal B)=0.
\tag{301.8}
$$
具体地，一个 $\mathcal B$-torsor 的特殊纤维有有理点，光滑性将其提升至 $\mathcal O_K$-点，从而 torsor 平凡。乘 $p$ 的 fppf Kummer 正合列及 properness 给
$$
B(K)/pB(K)
\simeq H^1_{\mathrm{fppf}}(\mathcal O_K,\mathcal B[p]).
\tag{301.9}
$$
右边在泛纤维上的像正是 (301.1)。因此一个有限平坦 $p$ 挠点同构保持好约化 Kummer 条件；这对任意绝对分歧指数都成立，只要该同构本身已经给出。

另需以下下降，注意它不要求曲线在原底域好约化。

**引理 301.3。** 设 $M/K$ 为有限局部扩张、$p\nmid[M:K]$，$B/K$ 为椭圆曲线。则
$$
\mathcal L_K(B)
=\operatorname{res}_{M/K}^{-1}\bigl(\mathcal L_M(B)\bigr).
\tag{301.10}
$$

**证明。** Kummer 正合列把 $\mathcal L_K(B)$ 识别为
$$
\ker\left(H^1(K,B[p])\longrightarrow H^1(K,B)[p]\right).
\tag{301.11}
$$
若一个类的限制在 $\mathcal L_M(B)$ 中，其在
$H^1(K,B)[p]$ 的像限制为零。对这个像作限制后再 corestriction，结果为乘 $[M:K]$，因而该像本身为零。这证明一边包含；另一边由 Kummer 映射与限制相容直接得到。$\square$

## 4. 任意扩域、任意二次扭曲的 $p$ 处比较

取第 2 节的固定 $L/\mathbb Q_p$，令 $K/\mathbb Q_p$ 任意有限。给定二次特征 $\chi$，令 $K_\chi/K$ 为使 $\chi$ 平凡的至多二次扩张，取
$$
M=LK_\chi.
\tag{301.12}
$$
由于 $L/\mathbb Q_p$ 为 Galois，
$$
[M:K]\mid 2[L:\mathbb Q_p],
\qquad p\nmid[M:K].
\tag{301.13}
$$
这里即使 $K/\mathbb Q_p$ 的分歧指数或次数被 $p$ 整除，也不影响 (301.13)。

在 $M$ 上，选定二次扭曲平凡化后，
$B_i^\chi$ 与 $B_i$ 同构，且 $\phi\otimes\chi$ 变成 $\phi$。将 (301.7) 基变换到 $\mathcal O_M$，通过好模型的唯一性及这些平凡化，得到实际同余在好约化群概形上的延拓。由 (301.9)，它识别 $M$ 上的两个 Kummer 条件。再分别对两条曲线应用 (301.10)，便得到
$$
(\phi\otimes\chi)_*\mathcal L_K(B_1^\chi)
=\mathcal L_K(B_2^\chi).
\tag{301.14}
$$
选择另一个扭曲平凡化只差 $[-1]$，它也保持 Kummer 子空间，故比较不依赖这些选择。

## 5. 其余位置及全局运输

整 $j$ 等价于所有有限位置潜在好约化；这一性质在扩域和二次扭曲后仍保持。令 $K/\mathbb Q_q$ 有限、$q\ne p$，把两条已扭曲的曲线记作 $C_1,C_2$。

若一条好约化，则另一条也好约化。事实上，对潜在好约化曲线，$T_p$ 的有限惯性像在模 $p$ 上忠实：核 $1+pM_2(\mathbb Z_p)$ 无有限阶非恒等元素，证明与第 2 节相同。因此模 $p$ 惯性平凡当且仅当完整 $T_p$ 惯性平凡，再用 Néron–Ogg–Shafarevich 判据即可。好约化时两个局部条件均等于
$$
H^1_{\mathrm{ur}}(K,C_i[p])
=\ker\bigl(H^1(K,C_i[p])
\longrightarrow H^1(K^{\mathrm{ur}},C_i[p])\bigr),
\tag{301.15}
$$
故实际同构保持它们。式 (301.15) 也可由好模型的 étale Kummer 正合列和有限域 Lang 定理得出。

若两条均坏约化，潜在好约化意味着它们为加性约化。过滤
$$
C_{i,1}(K)\subset C_{i,0}(K)\subset C_i(K)
\tag{301.16}
$$
的第一项是形式群，乘 $p$ 为自同构；中间商是剩余域的加法群，阶为 $q$ 的幂；最后商的阶整除加性约化的几何分支群阶，后者至多四。因此 $p>3$ 时三个部分的乘 $p$ 都是自同构，
$$
C_i(K)/pC_i(K)=0,\qquad
\mathcal L_K(C_i)=0.
\tag{301.17}
$$
这也处理了剩余特征二、三的野分歧；不能只用温和 Kodaira 表来略过这些位置。上述局部结论与 Mazur–Rubin, Lemmas 5.1、5.3 的奇素数部分一致。

阿基米德位置的绝对 Galois 群阶为一或二，所以 $p$ 为奇数时 $H^1(K,C_i[p])=0$。

现在取任意有限数域 $F/\mathbb Q$。第 4 节适用于每一个 $v\mid p$，本节适用于其他位置；所以 $\phi\otimes\chi$ 保持所有实际 Kummer 条件。将 Selmer 群写为
$$
\ker\left(H^1(F,B_i^\chi[p])
\longrightarrow
\bigoplus_vH^1(F_v,B_i^\chi[p])/\mathcal L_v(B_i^\chi)\right)
\tag{301.18}
$$
即证明定理 301.1。

由 Mordell–Weil 定理和通常 Selmer 正合列，
$$
0\longrightarrow B_i^\chi(F)/p
\longrightarrow\operatorname{Sel}_p(B_i^\chi/F)
\longrightarrow\Sha(B_i^\chi/F)[p]\longrightarrow0.
\tag{301.19}
$$
模 $p$ 同构也识别 $F$-有理 $p$ 挠点，所以 (301.3) 给准确数值关系
$$
\boxed{
\operatorname{rank}B_1^\chi(F)
+\dim_{\mathbb F_p}\Sha(B_1^\chi/F)[p]
=
\operatorname{rank}B_2^\chi(F)
+\dim_{\mathbb F_p}\Sha(B_2^\chi/F)[p].}
\tag{301.20}
$$
不需要假设整个 $\Sha$ 有限；只使用包含于有限 Selmer 群的 $\Sha[p]$。式 (301.20) 不允许删去两个 $\Sha[p]$ 项。

## 6. 实际一参数族中的无限阶点

现在回到 R258、R263、R266、R287、R289 的实际分支：$p>37$、$K=\mathbb Q(\sqrt{-3})$、$\sigma=1$、整 $j$，且实际二除域和三除法 $S_3$ 商域分别与指定 CM 参考相同。R289 在保持实际模 $p$ 同余的明确扭曲后给
$$
\begin{gathered}
a^3+db^3=1,\quad a,b\in\mathbb Z,\quad b\ne0,\quad d>0
\text{ 立方自由},\\
r=1-a^3=db^3,\qquad a\ne0,1,\\
\varepsilon=
\begin{cases}
-1,&4\mid a,\\
1,&a\equiv1\pmod {16},
\end{cases}\\
G_a:\ y^2=x^3+3ar\,x+r(2a^3-1),\qquad
G_a^{(\varepsilon)}[p]\simeq A_r[p],\quad
A_s:\ y^2=x^3+s .
\end{gathered}
\tag{301.21}
$$
排除 $a=0$ 是因为原曲线非 CM，排除 $a=1$ 是因为 $r\ne0$；这些不是新增假设。

令
$$
H_a=G_a^{(-1)}:
\quad y^2=x^3+3ar\,x-r(2a^3-1).
\tag{301.22}
$$
则有一个明确有理点
$$
P_a=(a^2,1)\in H_a(\mathbb Q),
\tag{301.23}
$$
因为
$a^6+3a^3r-r(2a^3-1)=a^6+a^3r+r=1$。

**引理 301.4。** 对 (301.21) 的每一个允许整数 $a$，$P_a$ 都为无限阶。

**证明。** 先给一个仅用于二进分母的形式群事实。若
$$
C:\ y^2=x^3+Ax+B,\qquad A,B\in\mathbb Z_2,
\tag{301.24}
$$
非奇异，且 $Q\in C(\mathbb Q_2)$ 满足 $v_2(x(Q))<0$，则 $Q$ 不是挠点。由方程首项赋值可知
$v_2(x(Q))=-2n$、$v_2(y(Q))=-3n$、$n\ge1$。于是 $t=-x/y$ 是原点形式群中的非零元素，$v_2(t)=n$。短模型的逆元使 $[-1](t)=-t$，因而其整系数倍乘级数满足
$$
[2](t)=2t+O(t^3).
\tag{301.25}
$$
对 $v_2(t)\ge1$，首项赋值为 $v_2(t)+1$，所有高次项赋值至少 $3v_2(t)>v_2(t)+1$，故 $[2](t)\ne0$，且赋值准确提高一。乘任意奇数的级数则保持 $v_2(t)$、也不为零。任意正整数分解成奇数与二的幂，便证明非零 $t$ 不可能为挠点。这个论证只用原点附近的整形式群，不要求 (301.24) 是好约化或极小模型。

对 (301.23) 作切线倍点。其斜率为
$$
\frac{3a^4+3ar}{2}=\frac{3a}{2},
$$
所以
$$
2P_a=\left(\frac{a^2}{4},\frac{9a^3-8}{8}\right).
\tag{301.26}
$$
若 $a$ 奇，$v_2(x(2P_a))=-2$，上一段立即说明 $2P_a$，从而 $P_a$ 为无限阶。

若 $4\mid a$，则 $a\ne0$，$P_a$ 与 $2P_a$ 的 $x$ 坐标不同。相加的斜率为 $(16-9a^3)/(6a^2)$，从而
$$
x(3P_a)=
\frac{9a^6-72a^3+64}{9a^4}.
\tag{301.27}
$$
令 $s=v_2(a)\ge2$。分子三项的赋值分别为 $6s$、$3+3s$、$6$，唯一最低值为 $6$。因此
$$
v_2(x(3P_a))=6-4s<0.
\tag{301.28}
$$
同一形式群论证说明 $3P_a$，从而 $P_a$ 为无限阶。两种分支全部处理。$\square$

## 7. 指定 CM 扭曲必须有非零 $p$-Selmer 群

将 (301.21) 的实际同余两边同时扭曲 $-\varepsilon$，得到
$$
\boxed{H_a[p]\simeq B_a[p],\qquad
B_a=A_{-\varepsilon r}:
y^2=x^3-\varepsilon(1-a^3).}
\tag{301.29}
$$
这是原来同一个 $d$ 所确定的
$$
B_a=A_d^{(-\varepsilon b)}.
\tag{301.30}
$$
扭曲参数 $-\varepsilon b$ 不能任意换成一个有利的参数；$B_a$ 也不是三次曲线
$X^3+dY^3=Z^3$ 的 Jacobian $y^2=x^3-432d^2$。

$j(H_a)=6912a^3(1-a^3)\in\mathbb Z$，而 $j(B_a)=0$。所以定理 301.1 适用。引理 301.4 给 $\operatorname{rank}H_a(\mathbb Q)\ge1$，于是
$$
\boxed{\dim_{\mathbb F_p}\operatorname{Sel}_p(B_a/\mathbb Q)\ge1.}
\tag{301.31}
$$
这使用 Mordell–Weil 自由部分模 $p$ 非零。**没有声称 $P_a$ 本身在 $H_a(\mathbb Q)/p$ 中必非零**；一个明确无限阶点可能是全局 $p$ 倍点，但正秩仍足以推出 (301.31)。

在 (301.29) 的实际范围内，模 $p$ 表示为一个二次扭曲的非分裂正规化子表示，仍不可约，故两条曲线都没有有理 $p$ 挠点。因此更明确地，
$$
\boxed{
\operatorname{rank}B_a(\mathbb Q)
+\dim_{\mathbb F_p}\Sha(B_a/\mathbb Q)[p]\ge1.}
\tag{301.32}
$$
由此得到实际排除规则：
$$
\operatorname{Sel}_p\!\left(A_{-\varepsilon(1-a^3)}/\mathbb Q\right)=0
\quad\Longrightarrow\quad
\text{该 }a\text{ 不可能来自当前实际异常分支}.
\tag{301.33}
$$
如果已经证明该 CM 曲线秩零，则 (301.32) 强迫
$\Sha(B_a/\mathbb Q)[p]\ne0$。但只知道中心 $L$ 值非零、从而秩零，还不能直接代替 (301.33) 的 Selmer 零条件。

两种符号准确为：

| 实际二进分支 | $\varepsilon$ | 被强迫有非零 $p$-Selmer 的 CM 曲线 |
|---|---:|---|
| $4\mid a$ | $-1$ | $y^2=x^3+1-a^3$ |
| $a\equiv1\bmod16$ | $1$ | $y^2=x^3+a^3-1$ |

所有结论保持原来的 $p\equiv2,5\bmod9$、$v_p(d)=2,1$ 方向以及 R290/R294 的 $p$ 进接近条件，但证明 (301.31) 不需要用高度下界替代全局同余。

## 8. $K=\mathbb Q(\sqrt{-3})$ 上的有限域标量

还有一个可直接用于 CM Selmer 计算的结构性后果。令 $F$ 包含 $K$，且 $\chi$ 是 $F$ 上任意二次特征。由于 $p\equiv2\bmod3$，
$$
\mathbb Z[\zeta_3]/(p)\simeq\mathbb F_{p^2}.
\tag{301.34}
$$
$A_d^\chi$ 的 CM 端同态都定义在 $F$ 上，对每一个 Kummer 映射具有函子性，因此
$\operatorname{Sel}_p(A_d^\chi/F)$ 是一个 $\mathbb F_{p^2}$ 向量空间。由定理 301.1，实际 $E_0^\chi$ 的 Selmer 群通过给定同余取得同样的标量作用，特别
$$
\dim_{\mathbb F_p}\operatorname{Sel}_p(E_0^\chi/F)
=\dim_{\mathbb F_p}\operatorname{Sel}_p(A_d^\chi/F)
\quad\text{为偶数}.
\tag{301.35}
$$
这个作用只在有限 Selmer 群及相应模 $p$ 上同调上；它不产生 $E_0$ 的代数 CM 端同态。

对 $B_a$ 的情形，在 $K/\mathbb Q$ 作限制。因为扩张次数二素于 $p$，限制
$H^1(\mathbb Q,B_a[p])\to H^1(K,B_a[p])$ 单射，且保持 Selmer 条件。因此 (301.31) 还给
$$
\dim_{\mathbb F_{p^2}}\operatorname{Sel}_p(B_a/K)\ge1.
\tag{301.36}
$$
这是同一个实际 CM 曲线的非零全局 Selmer 条件，不是任意选择一个环类角色后所得的形式条件。

## 9. 来源、与旧结果的关系及剩余缺口

- B. Mazur、K. Rubin，*Selmer companion curves*，Transactions AMS **367** (2015), 401–421，DOI [10.1090/S0002-9947-2014-06114-X](https://doi.org/10.1090/S0002-9947-2014-06114-X)；[作者全文](https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/a/189/files/2023/01/SELMER-COMPANION-CURVES.pdf)，Lemmas 5.1、5.3，Proposition 5.8，Theorems 3.1、6.1，作者 PDF 第 4、7–8、10–13 页。本文逐处证明实际范围，额外在表示素数的加性潜在好分支使用第 2–4 节的固定域延拓与下降；不漏掉原定理的好约化前提。
- M. Raynaud，*Schémas en groupes de type $(p,\ldots,p)$*，Bulletin SMF **102** (1974), 241–280，[原文](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)，Corollaire 3.3.6(1), p. 268。此处仅在固定 $L/\mathbb Q_p$、$e_L\le12<p-1$ 上应用一次。
- Néron–Ogg–Shafarevich 判据、潜在好约化与整 $j$、约化群过滤及形式群：J. H. Silverman，*The Arithmetic of Elliptic Curves*，2nd ed., 2009，Chapters IV、VII。两条曲线同时好约化域的次数与分歧界、素于 $p$ 的下降、以及无限阶点判定均已在本文展开。
- [R17](R17-local-selmer-conditions-at-new-primes.md) 只比较固定 $y^2=x^3-x$ 参考及实际新增乘法素数的局部差异，并明确没有声称全二次扭曲 companionship。本文限于整 $j$、无乘法素数的分支，允许变化 $d$、表示素数处加性约化、任意数域和任意二次扭曲。
- [R258](R258-sextic-cm-normal-form-and-exact-integral-j-level.md)、[R289](R289-dyadic-supersingularity-and-actual-integral-cubic-normal-form.md) 提供本文应用中的实际同余和准确二进符号。第 7 节不能只从有限处匹配、相同二除域或三除商域独立推出；R293 已证明这些较弱条件不够。

当前新的全局任务是控制 (301.31) 的指定、随 $a,d,b$ 变化的 CM Selmer 群，或证明相应非零条件与其他实际信息冲突。一般变化 CM 扭曲可能有正秩或非平凡 $\Sha[p]$，所以本文没有声称它们统一为零，也没有得到 $c$ 上界或绝对 $p$ 排除。

本文为纯证明产物，无数值搜索、数据表或验证脚本。主要目标仍为 OPEN。
