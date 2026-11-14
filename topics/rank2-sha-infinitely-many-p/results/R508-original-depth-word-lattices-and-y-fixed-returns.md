# R508 — 原两框架压深词的像格唯一性与全部保 Y 返回

日期：2026-11-14。**状态：已证明。** 本篇使用 R500、R503 的同一个
真实三输入来源 $\nu_{\mathcal L}(Z,V)\otimes\nu_\sigma(x)$。
四条压深轴 $Z,V,U=W'/2,P$ 的来源都是 scalar eigen-source，
但其物理压深词形成无穷多不同像格。本篇给出所有长度的准确分类，
并确定哪些词真正保持第一输出 $Y$。

这不赋 R503 的单位边界 $B_0$ 中央零；它排除在这四条轴内继续把
相同 scalar 来源误认为相同实际域的做法。

## 1. 全部实际矩阵和固定有限坏集

沿用
$$
\alpha=37+3\delta,\quad \delta^2=-3,\quad
\kappa=p\lambda^2,\quad\beta=-\lambda,\quad\chi_V^2=1.
$$
$U,P$ 与 $(Z,V)$ 的实际关系是
$$
U=(\alpha Z+2V)/54,\qquad
P=(-274Z+\bar\alpha V)/54.
\tag{1}
$$
固定独立输入 $x$。对 $a\in\{Z,V,U,P\}$，令
$$
D_a=I+(\kappa-1)E_a,
$$
$$
E_Z=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad E_V=I-E_Z,
\qquad
E_U=\frac1{1944}
 \begin{pmatrix}1396&2\bar\alpha\\274\alpha&548\end{pmatrix},
\quad E_P=I-E_U.
\tag{2}
$$
这些是 R500/R503 已支付完整来源、周期和中心的物理矩阵。
其标量分别为
$$
c_Z=c_U=\beta,\qquad c_V=c_P=\chi_V\lambda.
\tag{3}
$$
因此下面讨论的是已存在的真实核心，不是抽象新矩阵模型。

记互补字母
$$
Z^*=V,\quad V^*=Z,\quad U^*=P,\quad P^*=U.
$$
全部幂等恒等式给
$$
\boxed{D_aD_{a^*}=D_{a^*}D_a=\kappa I.}
\tag{4}
$$

模普通素数 $p$，$D_a$ 的像线依次由
$$
\boxed{
L_Z=(0,1)^t,\quad L_V=(1,0)^t,\quad
L_U=(-2,\alpha)^t,\quad L_P=(\bar\alpha,274)^t
}
\tag{5}
$$
生成，其核线恰为 $L_{a^*}$。
按顺序 $(Z,V),(Z,U),(Z,P),(V,U),(V,P),(U,P)$，
六个两列行列式准确为
$$
-1,\quad2,\quad-\bar\alpha,\quad\alpha,\quad274,\quad-1944.
\tag{6}
$$
所以只需删除 $2,3,137,349$。
这些素数已经在 R500/R503 的当前整框架与角度坏集中：
尤其 $137\equiv2\bmod3$ 本就不是当前普通素数。
以下四条像线在 residue field 中全部不同，不增加新的 ray 条件。

## 2. 真实词、相邻约简和全长 Smith 形

对一个非空词 $w=a_1\cdots a_\ell$，定义
$$
D_w=D_{a_1}\cdots D_{a_\ell},\qquad
\Lambda_w=D_w\mathcal O_p^2.
\tag{7}
$$
左端是最外层操作。若相邻出现 $aa^*$，按 (4) 删掉并提出一个
$\kappa$。重复至没有相邻互补字母，就得到
$$
\boxed{D_w=\kappa^sD_{\bar w},}
\tag{8}
$$
其中 $\bar w$ 是通常的自由约简词。
其唯一性也可由逐字压栈得到；$2s+|\bar w|=|w|$。

**引理。** 若 $\bar w$ 是长度 $\ell\ge1$ 的约简词，则 $D_{\bar w}$
的两个 elementary divisors 的赋值准确为 $(0,\ell)$；
其像格模 $p$ 的像线为 $L_{a_1}$。

**证明。** 每个 $\bar D_a=I-\bar E_a$ 都是秩一算子。
相邻两个的乘积为零，当且仅当右边像线等于左边核线；
由 (5)–(6)，这恰好是互补相邻对。
因此约简词的整个模 $p$ 乘积非零且秩一，像线为最外字母的
$L_{a_1}$。至少有一个矩阵元为单位，故最小 elementary divisor
的赋值为零。每个 $\det D_a=\kappa$，而 $v_p(\kappa)=1$，
所以行列式赋值为 $\ell$，第二项就是 $\ell$。证毕。

于是一般词 (8) 的 elementary divisors 为
$$
\boxed{(s,s+|\bar w|).}
\tag{9}
$$
这是对全部长度的证明，不依赖扫描若干短词。

## 3. 像格唯一确定整个约简词

**定理。** 两个真实压深词的像格相等，当且仅当它们有相同的
$s$ 和相同的约简词 $\bar w$。此时其物理矩阵本身也相等。

**证明。** 从像格先读 (9) 的最小赋值 $s$，以及两项之差
$\ell=|\bar w|$。除去共同 $\kappa^s$ 后，若 $\ell>0$，
像格模 $p$ 的像线由引理给出 $L_{a_1}$。
四条线互不相同，所以最外字母 $a_1$ 唯一确定。
对两个相等像格同时作用 $D_{a_1}^{-1}$，得到余下词的相等像格。
逐次继续，恢复所有字母。反方向由 (4) 立即成立。证毕。

特别在 $\operatorname{PGL}_2(K_{\mathfrak p})$ 中，
$$
\boxed{\langle D_Z,D_U\rangle\ \text{是秩二自由群}.}
\tag{10}
$$
因为 $D_V$、$D_P$ 在射影群中分别是其两个逆；任何非空自由约简
词的 elementary divisors 差为正，所以不可能是一个 scalar 矩阵。
这给出实际两框架的自由性，不是由一个抽象自由群作类比。

## 4. 对原来源的全部词域公式

R500/R503 的四个来源身份可以递归附上内层实际域。
因此对每个正词有
$$
\boxed{
\nu_{\mathcal L}|_{\Lambda_w}
=\left(\prod_{j=1}^{|w|}c_{a_j}\right)(D_w)_*\nu_{\mathcal L}.
}
\tag{11}
$$
独立 sigma 输入 $x$ 和全部 $x$ 测试保留。

证明只需归纳：最外字母的恒等式先将其整个像格拉回原格，
再限制到内词像格。没有把两个未按词序拉回的深条件直接相交。
若发生相邻约简，对应标量准确为
$$
c_ac_{a^*}=-\chi_V\lambda^2,
\tag{12}
$$
正是两个输出同时深的原标量。因此 (11) 与 (8) 的所有已付
像格等号完全相容。

特别，scalar 来源相同不产生额外词域等号。
若要比较不同约简词，必须保留它们的真实交域、差域与全部
测试转置；(11) 不允许删除这些差域。

## 5. 哪些词真正保持第一输出 Y

第一输出是
$$
Y=Z+\bar\gamma x.
\tag{13}
$$
先只作用于 $(Z,V)$，固定 $x$。

**定理。** 一个正压深词保持物理 $Y$，当且仅当它就是某个
$D_V^n$。没有含 $U$ 或 $P$ 的非平凡返回词保持 $Y$。

为证明此点，先确定射影群中 $L_Z=(0,1)^t$ 的稳定子。
若一个约简词包含 $U$ 或 $P$，删掉其开头和末尾的最大
$Z/V$ 字母块。它们都保持 $L_Z$，所以原词保持该线当且仅当
剩余词保持该线。剩余词的首、末字母都是 $U$ 或 $P$。
末字母的核线不是 $L_Z$，故将 $L_Z$ 送到非零像线；沿约简词
逐字作用，始终非零。最终模 $p$ 的像线为首字母的
$L_U$ 或 $L_P$，都不等于 $L_Z$。
所以其稳定子只能是由 $Z,V$ 组成的循环子群。

现在若 $D_w$ 保持 (13)，其第一行必须为 $(1,0)$，
从而它保持向量线 $L_Z$。由上述稳定子，约简词只有两种可能：
$Z^\ell$ 或 $V^\ell$（包括空词）。
结合提出的 $\kappa^s$，
其第一坐标尺度分别为 $\kappa^{s+\ell}$ 或 $\kappa^s$。
因 $v_p(\kappa)=1$，该尺度等于一只允许第二种且 $s=0$，
即恰为 $D_V^\ell$。反方向显然成立。

若同时允许原独立 $x$ 的第 $t$ 层 core，即 $x\mapsto\kappa^t x$，
并只要求 $Y$ 被整体乘以 $\kappa^t$，同一证明给出更完整分类：
$$
\boxed{
(Z,V,x)\longmapsto
(\kappa^tZ,\kappa^mV,\kappa^t x),\qquad t,m\ge0.
}
\tag{14}
$$
所有本质含 $U/P$ 的约简词都被排除。
(14) 正是旧 $Z,V,x$ 正交框架已有的返回，并未产生新的混合
$Y$ 核心。其标量是
$\beta^{2t}(\chi_V\lambda)^m$；在第一 Mellin 权中还必须保留
$\langle\lambda^2\rangle^{tdu}$ 和相应 log 质量项。

## 6. 对 R503 单位边界的含义

R503 已把全部正浅环带准确求和到
$$
J_S(u)=B_0(u)+\beta\mathcal A(u,\kappa).
$$
本篇表明，在同一三个输入的四个 scalar 方向内，
继续寻找一个“来源返回且物理第一 $Y$ 不动”的新有限词，
不会产生比 $V$ 纯伴随核心更多的条件。
所有非平凡混合词都给新像格，并真正移动第一 $Y$。

这不排除利用不同域的完整线性组合、真实固定 CM fiber、
R493 的六输入几何，或更大的来源系统控制 $B_0$。
当前继续点仍是该单位边界中的两个实际近相消支，
不把本篇的自由性误读为主问题不可能。

## 证书与依赖

- [全部四幂等矩阵与六个交叉行列式的精确证书](../scripts/check-r508-original-depth-word-geometry.mjs)；
  [有限数据](../scripts/check-r508-original-depth-word-geometry.json)。
  同一 BigInt 有理/CM 证书函数已在可用 V8 工具执行通过。
  全长唯一性和稳定子由本文证明，未由有限词枚举外推。
- [R503：原 18/2466 来源及唯一单位边界](R503-original-unit-annuli-and-single-shallow-boundary.md)。
- [R500：原三输入来源与完整纯 Y 轴](R500-original-pure-y-axis3699-and-complete-w-depth-complement.md)。
