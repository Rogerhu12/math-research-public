# R12 附录：实际正锚的复分数逆、全旗共同强单位及喷射平坦的精确可除层

日期：2026-11-29（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整的实际来源与范围定理，未构造原平方分子。** 既有 R150 已由同一正锚半群构造全部正实分数逆。本稿不重计那一构造；新增的是复右半平面上的同源延拓、任意有限组参数的同一收缩强*单位、原物理孔数域的实际逆像预算，以及全部形式喷射为零但原 $C$ 可除深度恰为指定整数的显式族。这提供了共同全部幂理想以外的实际有界分母，不把这些分母自身的分数根称为原 $C$ 的根。

## 1. 固定原尾与已经支付的正锚

固定原 Haar 尾 $C=A^{(m_0)}$，$m_0\ge0$。仍用该尾的完整实际
$$
N_j=C^{2^j}/\|C^{2^j}\|,\qquad
V_j=(I-N_j)(I+N_j)^{-1}.
$$
所有 carry 保留，位指标 $j$ 从此尾重新计数。置
$$
a_j=\frac1{j+1},\qquad
\mathcal Z=I+X_a,\qquad
L=\mathcal Z^{-1},
\tag{1}
$$
其中 $X_a$ 是原闭 first-row 乘子，$X_a\Omega=\sum_j a_j\chi_j$。原 R181 的正不可和分支及
[实际分数逆稿 §2](R150-appendix-actual-fractional-inverse-roots-and-rational-newton-edges.md)
给出：

- $\mathcal Z$ 最大增生且空谱，$L\in C'$ 有界、单射、像稠密、拟幂零；
- $S(t)=e^{-t\mathcal Z}$ 是同一个强连续半群，$S(t)\in C'$，且
  $\|S(t)\|\le e^{-t}$；其远端还有既有超指数范数衰减；
- 对正实 $\theta$，同一实际积分已经定义了
  $\Gamma(\theta)^{-1}\int_0^\infty t^{\theta-1}S(t)\,dt$，并付清正实参数的乘法律。

这些原证明逐尾适用：只把 $\alpha_j$ 换为 $\alpha_{m_0+j}$；原局部 carry 比值上界仍成立，闭 first-row 及其正锚构造不变。下面没有使用负整数边界表示。

## 2. 复参数的实际积分与全部共同强单位

对 $\operatorname{Re}\theta>0$ 定义
$$
L_\theta=\frac1{\Gamma(\theta)}
\int_0^\infty t^{\theta-1}S(t)\,dt,
\qquad
t^{\theta-1}=\exp((\theta-1)\log t).
\tag{2}
$$
先对每个向量取强积分。由 $\|S(t)\|\le e^{-t}$，
$$
\boxed{\|L_\theta\|\le
\frac{\Gamma(\operatorname{Re}\theta)}{|\Gamma(\theta)|}.}
\tag{3}
$$
因而它定义实际有界 $C'$ 元。每个紧复参数集上的积分及带任意固定次 $\log t$ 的导数积分都有可积的共同范数上界；差商在该上界下收敛，故 $\theta\mapsto L_\theta$ 在右半平面算子范数全纯。这里不要求 $S(t)$ 在零点算子范数连续。

同一实际半群律和向量 Fubini、复 Beta 积分给
$$
\boxed{L_\theta L_\eta=L_{\theta+\eta}
\quad(\operatorname{Re}\theta,\operatorname{Re}\eta>0),\qquad
L_n=L^n\quad(n\ge1).}
\tag{4}
$$
所有二重积分由 $t^{\operatorname{Re}\theta-1}u^{\operatorname{Re}\eta-1}e^{-(t+u)}$ 支配，因此这不是形式复幂乘法。

对实 $\lambda>0$ 取实际 Yosida 单位
$$
E_\lambda=\lambda(\mathcal Z+\lambda I)^{-1}
=\lambda L(I+\lambda L)^{-1}.
\tag{5}
$$
最大增生性给 $\|E_\lambda\|\le1$，而 $\mathcal Z$ 稠密定义给 $E_\lambda\to I$ 强。亦有强*收敛：可用最大增生伴随的同一预解逼近，或原全 $C'$ 的 $J$ 对称性。

现在给定任意有限组 $\theta_1,\ldots,\theta_d$，全部实部为正。选同一个整数
$$
k>\max_i\operatorname{Re}\theta_i
$$
并定义
$$
U_{\theta_i,\lambda}
=\lambda^k L_{k-\theta_i}(I+\lambda L)^{-k}\in C'.
$$
(4) 逐项给准确等式
$$
\boxed{
L_{\theta_i}U_{\theta_i,\lambda}
=U_{\theta_i,\lambda}L_{\theta_i}
=E_\lambda^k,\qquad
\|E_\lambda^k\|\le1,\qquad E_\lambda^k\to I
\ \text{强*}.
}
\tag{6}
$$
这是整个有限参数组共用的实际收缩强单位，不要求各 $U_{\theta_i,\lambda}$ 一致有界。

由 R88 的全交换子有界强多项式闭包，(6) 的全部因子保持原 $C$ 的每一个闭不变旗，也保持任意固定有限放大中的原旗。对固定 Hilbert 旗子商，原强*极限及伴随压缩到其固定代表空间。若诱导 $L_{\theta_i}$ 杀掉一个向量，(6) 迫该向量为零；又 $E_\lambda^k$ 的像包含于诱导 $L_{\theta_i}$ 的实际像。因此
$$
\boxed{L_\theta\text{ 在全部非零原有限放大闭不变旗子商上单射且像稠密。}}
\tag{7}
$$
全空间 quasiaffinity 没有被直接当成商上的结论。

另外，对实 $\theta\downarrow0$，$L_\theta\to I$ 强*且 $\|L_\theta\|\le1$。将 (2) 写成 Gamma 概率密度
$t^{\theta-1}e^{-t}/\Gamma(\theta)$ 对收缩强连续轨道
$e^tS(t)=e^{-tX_a}$ 的平均即可：密度质量趋向零点。此处只声称实正参数的强*连续性，不声称零点的范数连续性。

## 3. 原物理孔数域的准确逆像

令 $\mathcal N$ 为原 Walsh 孔数算子，$\Lambda=I+\mathcal N$，记
$$
\mathcal H_k=\operatorname{Dom}\Lambda^k.
$$
[R181 §§2–3](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md)
对完整实际 first-row 给有限常数 $D_s$，使
$$
\|\Lambda^s X_a u\|
\le D_s\|a\|_2\|\Lambda^{s+1}u\|
\quad(u\in\mathcal H_{s+1}).
$$
原闭性延拓及逐次同域应用因而给
$$
\mathcal H_k\subseteq\operatorname{Dom}\mathcal Z^k,\qquad
\|\mathcal Z^ku\|\le
A_k\|\Lambda^ku\|,\qquad
A_k=\prod_{s=0}^{k-1}(1+D_s\|a\|_2).
\tag{8}
$$
这保留了全部 carry 的加权局部估计；没有将 $X_a$ 代为纯 Boolean 行。

固定 $\operatorname{Re}\theta>0$，取任一整数 $k>\operatorname{Re}\theta$。对 $u\in\mathcal H_k$，令
$$
g_{\theta,u}=L_{k-\theta}\mathcal Z^ku.
$$
由 (4) 与真实自然逆关系，
$$
\boxed{L_\theta g_{\theta,u}=L^k\mathcal Z^ku=u.}
\tag{9}
$$
单射性使此来源与可用整数 $k$ 的选择无关。特别
$$
\boxed{
\mathcal H_k\subseteq\operatorname{Ran}L_\theta,\qquad
\|L_\theta^{-1}u\|
\le
\frac{\Gamma(k-\operatorname{Re}\theta)}{|\Gamma(k-\theta)|}
A_k\|\Lambda^ku\|.
}
\tag{10}
$$
全部有限 Walsh 柱向量、尤其 $\Omega$，都在这个实际像内。

还有一个不依赖额外孔数核心假设的准确图核心。对 $x=L_\theta v$，
$$
E_\lambda^kx\in\operatorname{Ran}L^k,\qquad
L_\theta^{-1}E_\lambda^kx=E_\lambda^kv\to v,
$$
且 $E_\lambda^kx\to x$。故
$$
\boxed{\operatorname{Ran}L^k
\text{ 是闭算子 }L_\theta^{-1}\text{ 的真实图核心}.}
\tag{11}
$$
在任意固定原旗子商上，相同等式给相应实际像核心。本文没有仅据有限柱在 (10) 中就另称其为该闭逆的图核心。

## 4. 全部形式喷射为零，但原 $C$ 的可除深度准确有限

用[完整交换子兼容喷射稿](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)
的记号
$$
j_\chi:C'\to\mathbb C[[z]],\qquad j_\chi(C)=z,\qquad
\mathfrak I_\infty=\bigcap_\chi\ker j_\chi.
$$

先取正有理 $\theta=p/q$。由 (4)，$L_\theta^q=L^p$，所以 $L_\theta$ 拟幂零。对每个整数 $n\ge1$，同一实际族还有
$$
L_\theta=(L_{\theta/n})^n.
$$
若某个 $j_\chi(L_\theta)$ 非零，则其常数项为零，且其有限正整数消失阶必须被全部 $n$ 整除，矛盾。因此所有正有理参数都有 $j_\chi(L_\theta)=0$。

每个固定喷射系数是 $C'$ 上连续线性泛函，而 (2) 在连通右半平面范数全纯。对每一系数用解析恒等定理，从正有理参数的聚点得到
$$
\boxed{L_\theta\in\mathfrak I_\infty
\quad(\operatorname{Re}\theta>0).}
\tag{12}
$$
尤其所有这些算子均拟幂零，且非零性已有 (7) 支付。

然而它们不在 $CC'$ 内。原权给
$$
\|C^{-1}\Omega\|^2
=\sum_{j\ge0}\frac{2^{-j-1}}{\alpha_{m_0+j}^{\,2}}=\infty,
\tag{13}
$$
即 $\Omega\notin\operatorname{Ran}C$。这里 $C^{-1}$ 仅为真实像上的逆；(13) 是权移公式迫出的唯一可测候选的 $L^2$ 范数。另一方面 (9) 已给 $\Omega\in\operatorname{Ran}L_\theta$。若 $L_\theta=CB$，则其全部像包含于 $\operatorname{Ran}C$，矛盾。

更一般，对每个整数 $r\ge0$，
$$
\boxed{
C^rL_\theta\in
\mathfrak I_\infty\cap C^rC'
\ \setminus\ C^{r+1}C'.
}
\tag{14}
$$
若 $C^rL_\theta=C^{r+1}B$，由实际单射的 $C^r$ 消去，得到刚排除的 $L_\theta=CB$。所以 (14) 是实际有界可除关系的精确深度；它不能由全喷射的零值读出。

特别 $L_\theta$ 不属于共同全部幂理想
$\mathfrak F=\bigcap_{r\ge1}C^rC'$。本文不判定 $\overline{\mathfrak F}$ 与 $\mathfrak I_\infty$ 的关系，也不对非闭主理想给未经支付的范数距离。

## 5. 该新分母对原双源目标实际提供什么

这个族可直接用作原二次式的不同候选分母：
$$
Y^2=C L_\theta^2,\qquad Y\in C'.
\tag{15}
$$
(15) 仍未构造。假如它成立，已刊
[同一有界分子分母的最大闭根定理](R12-appendix-same-flat-denominator-maximal-stable-root-and-all-flag-cores.md)
可使用 (6) 给出的实际同一强单位，产生
$$
S=L_\theta^{-1}Y,\qquad
D(S)=\{x:Yx\in\operatorname{Ran}L_\theta\},
\qquad D(S^2)=D(S),\quad S^2=C|_{D(S)}.
$$
而 (9)–(10) 额外付清
$$
\mathcal H_k\subset D(S),\qquad
S\Omega=Y\,L_{k-\theta}\mathcal Z^k\Omega,\qquad
\|Su\|\le\|Y\|\,
\frac{\Gamma(k-\operatorname{Re}\theta)}{|\Gamma(k-\theta)|}
A_k\|\Lambda^ku\|.
\tag{16}
$$
这里 $S\Omega$ 是同一实际来源，不是任取闭包像。相应逆来源
$L_\theta^{-1}\Omega$ 循环：其 $C$ 循环闭包被全部 $C'$ 保持，并包含
$L_\theta L_\theta^{-1}\Omega=\Omega$。

本稿没有从 $L_\theta$ 自身存在全部分数根，推断 (15)。它的准确作用是提供一组已经全域、全旗和同源范围核实、却严格在共同 $C$ 幂分母类之外的平坦分母。原双源平方关系及普通 ISP 仍然开放。
