# R471：原始 CM 轨道的统一非消失判据与指定商零像

**状态：已证明，适用范围为下述显式判据。** 本篇把 R348 的全族非消失平均推进到 R390/R434 指定的原始 CM 商：所有原始角色组成一个有理 Galois 轨道；一个统一绝对值界给出可直接检查的判据，保证这个轨道中有非零中心值，从而指定有理商本身秩零且所有有理点的像准确为零。

判据尚未对所有 $p$ 成立。本篇也没有计算实际 CM 小盘的本原一次项。因此它关闭的是所列 $p$ 范围内指定商的全局零像输入，不是 Serre 一致性的完成证明。

## 1. 定理及准确的范围

保持 R348、R390 的实际角色与扭向，令
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
这里 $\kappa_4^{-1}$ 是 R348 在真实六层上确定的扭向。指定原始角色为
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
进一步，令 $B_-/\mathbb Q$ 是与 $A_-$ 同源的任意代表，令
$q_-:J_{Z_p}\twoheadrightarrow B_-$ 是实际有理商；则
$$
B_-(\mathbb Q)=0,\qquad
q_-([P-c_1])=0\quad\text{对每个 }P\in Z_p(\mathbb Q).
\tag{471.7}
$$
这里 $Z_p$、$c_1$、模六标记及商的实际来源全部与 R348、R374 相同。

两个直接可用的范围是：

1. 若 $p+1=2^a3^b$，则 $\delta(p)=0$，所以 (471.5) 自动成立。因为 $p\equiv2\bmod3$ 且 $p$ 为奇素数，此处实际有 $a,b\ge1$。
2. 若 $p+1=S q$，其中 $S=2^a3^b$、$a,b\ge1$，$q\ge5$ 为素数且 $q\ge13S$，则 (471.5) 成立。

第二条并不声称满足这些条件的素数对有无穷多个。定理对每个满足条件的实际素数逐一有效，没有借用关于同时为素数的猜想。

## 2. 原始角色为什么是同一个实际有理因子

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

在 R348 的实际 Hecke 角色式中，对每个与 $6p$ 互素的主理想，
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
这没有交换实际 $\kappa_4^{-1}$ 扭向。

对一个权二新形式，附属有理模 abelian variety 由整个 Hecke 系数 Galois 轨道定义；共轭形式给同一个有理 Hecke 因子，因而给同一个有理同源类。故任何原始 $g_k$ 的附属因子都与 $A_-$ 同源。

这一步的用途是运输 **有理秩零结论和实际商**。只要找到其中一个
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

## 6. 与真实 CM 小盘的接口

在满足 (471.5) 的范围内，R390/R434 指定的权一通道可以选在
$B_-$ 中，并且所有有理点在其中已有准确零像。因此该范围内后续局部证明不再需要另等“指定原始轨道中有非零中心值”的输入。

还须真正计算同一个 $c_1$ 小盘上的本原对数轮廓。例如若能证明 R434 的
$$
\operatorname{in}_E(\mathscr L)=u w+w^2R(w),\qquad u\ne0,
\tag{471.22}
$$
则对 R390 的实际候选 $v_p(w)\ge1$，零像只可能来自 $w=0$。本文没有证明 (471.22)，也没有把 R434 的尖点单位或 R390 的固定 Cartier 系数当作该式。

对不满足 (471.5) 的其余 $p$，原始轨道的全局秩零输入仍未由本篇得到；R348 已有的某个 CM 非消失商仍然存在。下一步继续这两个明确的实际缺口。

## 7. 输入与产物

本篇为纯证明，无必需数据或脚本。

- R348 的真实 $\kappa_4^{-1}$ 扭向、准确导子和根号、Mellin 公式、统一平均下界，以及 Kato 的秩零应用。其 Hecke–Shimura 与 Kato 原文位置沿用 R348 已核记录；本篇没有改变它们的假设。
- R374 的同一有理 CM 因子在任意同源整格上的挠点消失。
- R390、R434 的指定原始角色、实际权一通道与本原形式对数接口。
- §2 的 Galois 轨道、§3 的六角格计数及全部显式常数均在正文证明，不用有限样本或关于素数分布的假设代替。
