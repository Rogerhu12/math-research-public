# R471：相反扭向 CM 原始轨道的非消失判据与抽象模因子秩零

**R575 范围修正。** 本文是原冻结稿的独立修正版，原稿字节保持不变。统一记
$g_\theta=f_{\Psi_\theta\kappa_4^{-1}}$ 为**相反扭向的独立 Hecke 新形式**，
$A_-$ 为其中指定本原轨道的模 abelian variety，$B_-$ 为与 $A_-$ 在
$\mathbb Q$ 上同源的任意 abelian variety；这里的 $B_-$ 不含“是 $J_{Z_p}$ 的商”这一断言。
R575 证明实际六层的相应 CM 成分是 $f_{\Psi_\theta\kappa_4}$，根号为 $-1$，中心值恒零。
因此撤回 $g_\theta$ 在实际 $Z_p$ 中的出现性、由该出现性得到的商映射，以及对实际有理点的零像应用。
本文独立的有限型、固定曲线或 $g_\theta$ 的 $L$ 值结论保留；在本文列出的非零前提成立时，
Kato 的秩零结论及 R374 的惯性无扭点论证仍给抽象 $B_-(\mathbb Q)=0$。
实际模曲线的局部公式若用于某一通道，须先独立识别该通道；相同的 $p$ 局部型不替代这个全局识别。

**状态：已证明，适用范围为下述显式判据和独立 Hecke 家族。** 本篇把 $\kappa_4^{-1}$ 家族的全族正平均推进到指定原始轨道：所有原始角色组成一个有理 Galois 轨道；统一绝对值界给出可直接检查的判据，保证该轨道中有非零中心值，从而其抽象有理模因子秩零且 $B_-(\mathbb Q)=0$。

判据尚未对所有 $p$ 成立。R575 后，本篇不再声称该因子在实际 $J_{Z_p}$ 中出现，也不提供实际有理点的零像输入。实际粗 CM jet 和实际全局零像来源均须另行研究。

## 1. 定理及准确的范围

固定 R348 的相反扭向独立 Hecke 角色族，令
$$
p\ge41,\qquad p\equiv2\pmod3,\qquad
M=p+1,\qquad h=M/6,
\tag{471.1}
$$
并固定
$$
\Theta_p=\{\theta_k:k\bmod M,\ k\equiv5\pmod6\},\qquad
\theta_k(\alpha)=[\bar\alpha]^{(p-1)k},\qquad
g_k=f_{\Psi_{\theta_k}\kappa_4^{-1}}.
\tag{471.2}
$$
这里 $\kappa_4^{-1}$ 只定义本篇的独立家族；R575 已证明实际六层为另一扭向 $\kappa_4$。指定原始角色为
$\theta_-:=\theta_{-1}=\theta_p$，相应有理模因子记为 $A_-$。

写
$$
B=\frac{5393}{6150},\qquad
C=\frac43\sqrt{3\sqrt3},\qquad
\delta(p)=1-\frac{3\varphi(M)}M
=1-\prod_{\substack{q\mid M\\q\ge5\text{ prime}}}
\left(1-\frac1q\right).
\tag{471.3}
$$
空乘积为一。

**定理。** 对本族每个角色，都有统一界
$$
|L(g_k,1)|<C\sqrt p.
\tag{471.4}
$$
若
$$
\boxed{\quad C\sqrt p\,\delta(p)<B,\quad}
\tag{471.5}
$$
则存在阶恰为 $M$ 的 $\theta_k\in\Theta_p$ 使 $L(g_k,1)>0$。所有这样的原始 $g_k$ 都属于同一个有理 Galois 轨道，包含 $g_-$。因此
$$
\operatorname{rank}A_-(\mathbb Q)=0.
\tag{471.6}
$$
进一步，令 $B_-/\mathbb Q$ 是与独立模因子 $A_-$ 同源的任意 abelian variety；则
$$
B_-(\mathbb Q)=0.
\tag{471.7}
$$
这里不再断言存在 $q_-:J_{Z_p}\twoheadrightarrow B_-$，也不据此对实际点 $P\in Z_p(\mathbb Q)$ 作 Abel–Jacobi 零像推断。该群为零来自秩零和 R374 的独立惯性无扭点论证。

两个直接可用的范围是：

1. 若 $p+1=2^a3^b$，则 $\delta(p)=0$，所以 (471.5) 自动成立。因为 $p\equiv2\bmod3$ 且 $p$ 为奇素数，此处实际有 $a,b\ge1$。
2. 若 $p+1=S q$，其中 $S=2^a3^b$、$a,b\ge1$，$q\ge5$ 为素数且 $q\ge13S$，则 (471.5) 成立。

第二条并不声称满足这些条件的素数对有无穷多个。定理对每个满足条件的实际素数逐一有效，没有借用关于同时为素数的猜想。

## 2. 原始角色为什么给同一个独立有理模因子

$\theta_k$ 的阶是 $M/\gcd(k,M)$，故
$$
\Theta_p^{\mathrm{prim}}
=\{\theta_k:k\equiv5\bmod6,\ \gcd(k,M)=1\}.
\tag{471.8}
$$
对每个这样的 $k$，取
$$
a\equiv-k^{-1}\pmod M.
\tag{471.9}
$$
因为 $k\equiv-1\bmod6$，有 $a\equiv1\bmod6$。于是
$\sigma_a\in\operatorname{Gal}(\mathbb Q(\mu_M)/\mathbb Q)$，
$\sigma_a(\zeta_M)=\zeta_M^a$，固定 $K=\mathbb Q(\sqrt{-3})$ 及所有六次单位根。

在固定的 Hecke 角色式中，对每个与 $6p$ 互素的主理想，
$$
\Psi_{\theta_k}((\alpha))\kappa_4((\alpha))^{-1}
=\alpha\,\epsilon_3(\alpha)\theta_k(\alpha)
 \kappa_4((\alpha))^{-1}.
\tag{471.10}
$$
$\alpha\in K$，$\epsilon_3$ 取有理值，而 $\kappa_4$ 的值在
$\mu_3\subset K$ 中。它们全被 $\sigma_a$ 固定，只有 $\theta_k$ 被变成
$\theta_{ak}=\theta_{-1}$。在坏理想上，两侧的扩张系数同时为零。因此逐项的完整 Fourier 恒等为
$$
\sigma_a(g_k)=g_-.
\tag{471.11}
$$
这没有交换本篇固定的 $\kappa_4^{-1}$ 扭向。

对一个权二新形式，附属有理模 abelian variety 由整个 Hecke 系数 Galois 轨道定义；共轭形式给同一个有理 Hecke 因子，因而给同一个有理同源类。故任何原始 $g_k$ 的附属因子都与 $A_-$ 同源。

这一步运输的是**独立模同源类的有理秩零结论**，不运输一个未经证明存在的实际商。只要找到其中一个
$L(g_k,1)\ne0$，R348 已核准的 Kato 输入便给该有理因子秩零，随后由同源运输到 $A_-$。不需要先为每个复嵌入另选周期来比较其中心值。

最后，由 $M$ 被六整除，$M$ 的单位剩余类都模六为 $1$ 或 $5$，取负号交换两类且无不动点。因此
$$
|\Theta_p^{\mathrm{prim}}|=\frac{\varphi(M)}2,\qquad
|\Theta_p\setminus\Theta_p^{\mathrm{prim}}|
=h\,\delta(p).
\tag{471.12}
$$
这也证明 (471.3) 的 Euler 乘积式；重复素因子不额外改变该比例。

## 3. 对变化 $p$ 一致的中心值绝对界

R348 给每个 $g_k$ 准确层 $N=108p^2$、根号 $+1$。同一 Mellin 分拆给
$$
L(g_k,1)=2\sum_{n\ge1}\frac{a_n(g_k)}n e^{-x n},\qquad
x=\frac{2\pi}{\sqrt N}=\frac{\pi}{3\sqrt3\,p}.
\tag{471.13}
$$
该式绝对收敛。

固定 $K=\mathbb Q(\sqrt{-3})$ 的整数环为
$\mathbb Z[\zeta_3]$，类数一、单位数六。Hecke 角色在好理想上的复绝对值是理想范数的平方根；删除导子支撑的限制只增加接下来非负的上界。由每个主理想恰有六个生成元，
$$
|L(g_k,1)|
\le\frac13\sum_{0\ne\alpha\in\mathbb Z[\zeta_3]}
\frac{e^{-x|\alpha|^2}}{|\alpha|}.
\tag{471.14}
$$
所有 $\theta_k$、$\epsilon_3$、$\kappa_4$ 的有限权都只贡献绝对值一，所以这一界不依赖 $k$。

写 $\alpha=A+B\zeta_3$，其范数为 $A^2-AB+B^2$。对整数 $m\ge1$，六角壳
$$
\max\{|A|,|B|,|A-B|\}=m
\tag{471.15}
$$
恰有 $6m$ 个点；例如边界上六条边每条分配一个端点后各有 $m$ 个点。每条边上的二次式在边中点达到最小值，所以壳上都有
$$
|\alpha|^2\ge\frac34m^2.
\tag{471.16}
$$
代入 (471.14)，再用正的严格递减 Gaussian 的积分比较，得到
$$
\begin{aligned}
|L(g_k,1)|
&\le\frac4{\sqrt3}\sum_{m\ge1}e^{-3xm^2/4}\\
&<\frac4{\sqrt3}\int_0^\infty e^{-3xt^2/4}\,dt\\
&=\frac{4\sqrt\pi}{3\sqrt x}
=\frac43\sqrt{3\sqrt3}\,\sqrt p.
\end{aligned}
\tag{471.17}
$$
这证明 (471.4)。没有以固定角色、固定 $p$ 或隐藏的导子参数吸收常数。

## 4. 排除“只有非原始轨道贡献”的可能性

R348 的已证统一下界为
$$
\sum_{\theta_k\in\Theta_p}L(g_k,1)>hB.
\tag{471.18}
$$
所有 $g_k$ 都是平凡 nebentypus 的权二新形式，Fourier 系数实，故这些中心值为实数。用 (471.4)、(471.12)，有
$$
\begin{aligned}
\sum_{\theta_k\in\Theta_p^{\mathrm{prim}}}L(g_k,1)
&=\sum_{\Theta_p}L(g_k,1)
 -\sum_{\Theta_p\setminus\Theta_p^{\mathrm{prim}}}L(g_k,1)\\
&>h\bigl(B-C\sqrt p\,\delta(p)\bigr).
\end{aligned}
\tag{471.19}
$$
(471.5) 使右端为正，所以至少一个原始角色中心值为正。此论证并未预设所有单个中心值都非负。

由 §2 的同一有理轨道和 R348 的 Kato 秩零结论，得到 (471.6)。再用
R374：阶为 $M$ 的本原角色仍有被六整除的阶，故其所有有理同源代表在
$\mathbb Q_p^{\mathrm{nr}}$ 上的挠点群为零。有限生成的
$B_-(\mathbb Q)$ 既秩零又无挠，因而就是零群，得到 (471.7)。

## 5. 两个可直接核验的素数范围

若 $M$ 只含素因子二和三，(471.3) 的乘积为空，$\delta(p)=0$。这时
R348 给出的任一非零中心值已经来自唯一的原始有理轨道。

若 $M=S q$ 如定理第二条，则
$\delta(p)=1/q$。所需的数值比较可完全有理地验证：
$$
C^2=\frac{16\sqrt3}{3}
<\frac{416}{45}
<\frac{49}{4}B^2
<13B^2.
\tag{471.20}
$$
第一个不等式使用 $\sqrt3<26/15$；第二个不等式两端之差为
$8848667/50430000>0$。于是 $q\ge13S$ 给
$$
C^2p\,\delta(p)^2
=C^2\frac{Sq-1}{q^2}
<C^2\frac S q
\le\frac{C^2}{13}<B^2,
\tag{471.21}
$$
从而 (471.5) 成立。

更一般时应直接使用 (471.5) 的准确 $\delta(p)$，而不是把第二条误读成必要条件。如果判据失败，本文没有证明原始轨道中心值全为零，也没有证明其有理商有正秩；仅表示这个统一绝对值估计不足以从总平均分离出它。

## 6. 实际 CM 小盘的接口已经撤回

满足 (471.5) 时，本文得到的是相反扭向独立模同源类的 $B_-(\mathbb Q)=0$。R575 证明实际六层相应的 CM 族为 $f_{\Psi_\theta\kappa_4}$，根号 $-1$，所以不能把本篇的非零中心值或秩零运输到实际六层。

R434 的条件局部判据
$$
\operatorname{in}_E(\mathscr L)=u w+w^2R(w),\qquad u\ne0,
\tag{471.22}
$$
只有在一个实际通道已独立识别、局部前提已经核定且同一实际商具有全局零像时，才可用于排除相应候选。本文不提供那个实际商或全局零像；尖点单位和固定 Cartier 系数也不自动给 (471.22)。

不满足 (471.5) 的其余 $p$ 上，指定独立原始轨道的非消失仍未由本篇得到。原 R348 的另一家族正平均仍是该家族的算术结论，不能再说成实际 $Z_p$ 有 CM 秩零商。

## 7. 输入与产物

本篇为纯证明，无必需数据或脚本。

- R348 关于独立 $\kappa_4^{-1}$ 家族的准确导子和根号、Mellin 公式、统一平均下界，以及 Kato 的秩零输入；其实际出现性按 R575 撤回。其 Hecke–Shimura 与 Kato 原文位置沿用 R348 已核记录；本篇没有改变它们的假设。
- R374 的同一有理 CM 因子在任意同源整格上的挠点消失。
- R390、R434 的指定原始角色记号；其旧实际商接口按 R575 撤回，形式对数只作为具有明列前提的条件引理。
- §2 的 Galois 轨道、§3 的六角格计数及全部显式常数均在正文证明，不用有限样本或关于素数分布的假设代替。
