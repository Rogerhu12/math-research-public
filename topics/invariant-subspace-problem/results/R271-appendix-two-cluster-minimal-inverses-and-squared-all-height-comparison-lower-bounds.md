# R271 附录：两簇最小逆、暗对高阶矩与全高度比较常数的平方下界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；暗对全阶正交展开由 kernel_resume_1cf 与 boundary_resume_1cf 分别推导。AI-assisted，GPT-6 Astra Pro。
状态：完整证明；根代理与 boundary_resume_1cf 已独立核查全阶有限公式、真实最小逆、暗对高阶矩及全部连续尾量词。本文强化七位反例与连续尾暗对传递；所有最小原像仍取在整个实际 Hilbert 空间中。

## 1. 结论与已证范围的扣除

沿用 [连续尾暗对稿](R271-appendix-dark-pair-transfer-and-continuous-tail-adjacent-descent-counterexample.md) 的实际尾
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,
$$
以及
$$
E_{h,p}=\ker D_m^h\cap\mathcal H_p,\qquad
U_{h,p}=E_{h,p}\ominus E_{h-1,p}.
$$
对 $h\ge2$、primitive 孔数 $s$，置
$$
A_{h,s+h-1}
=P_{U_{h-1,s+h-2}}D_m|_{U_{h,s+h-1}},
$$
$$
A_{h+1,s+h}
=P_{U_{h,s+h-1}}D_m|_{U_{h+1,s+h}}.
$$
定义允许取无穷大的真实比较常数
$$
\mathfrak c_{m,s,h}
=\sup_{0\ne x\in U_{h,s+h-1}}
\frac{\|A_{h+1,s+h}^*x\|^2}
{\|A_{h,s+h-1}x\|^2}.
\tag{1.1}
$$
分母对非零 $x$ 为正。确实，若第一下降为零，则 $D_mx\in\ker D_m^{h-2}$，进而 $x\in\ker D_m^{h-1}$，与 $x\in U_h$ 矛盾。

**定理 1.1。** 对每个固定整数 $h\ge2$，
$$
\boxed{
\liminf_{m\to\infty}\ \inf_{s\ge4\cdot2^m}
\mathfrak c_{m,s,h}
\ge \left(\frac{h}{h-1}\right)^2.
}
\tag{1.2}
$$
特别 $h=2$ 时必要下界是 $4$。此前七位稿及连续尾稿给出的 $8/3$ 下界被本节严格加强。

同一个平方下界也约束任意正异权有限布尔模型的普遍比较常数。
本文没有证明这个平方常数是上界，也没有证明任何有限统一上界存在。

新增的两个具体输入是：有限两簇模型的全阶真实最小逆公式，以及相邻暗对背景的全部固定阶伴随矩。后者还给任意固定有限活跃 primitive 空间上最小逆 Gram 的原范数逼近，不使用无限空间核投影连续性。

## 2. 两个对称活跃簇及 primitive 向量

取 $q\ge1$ 个权为 $1$ 的强位、$n$ 个权为 $\varepsilon$ 的弱位，其中
$$
0<\varepsilon<1,\qquad n\ge q+h.
$$
这里 $q,n$ 是固定有限活跃参数，不是原边界问题的窗口参数。
记强、弱簇的规范对称孔向量分别为 $e_i,w_j$：
$$
e_i=\binom qi^{-1/2}\sum_{|I|=i}e_I,\qquad
w_j=\binom nj^{-1/2}\sum_{|J|=j}e_J.
$$
令 $D_{\rm a}=D_{\rm s}+\varepsilon D_{\rm w}$。准确有
$$
D_{\rm s}e_i=\sqrt{i(q-i+1)}\,e_{i-1},\qquad
D_{\rm w}w_j=\sqrt{j(n-j+1)}\,w_{j-1}.
\tag{2.1}
$$

置
$$
Z_\varepsilon
=\sum_{i=0}^q\binom{n-q+i}{i}\varepsilon^{2i},
$$
$$
\boxed{
g_\varepsilon
=Z_\varepsilon^{-1/2}
\sum_{i=0}^q(-\varepsilon)^i
\sqrt{\binom{n-q+i}{i}}\ e_iw_{q-i}.
}
\tag{2.2}
$$
它是单位第 $q$ 孔向量。相邻两项在每个 $e_iw_{q-i-1}$ 坐标上的系数恰好相消，故
$$
D_{\rm a}g_\varepsilon=0.
\tag{2.3}
$$
例如其系数满足
$$
c_{i+1}\sqrt{(i+1)(q-i)}
=-\varepsilon c_i\sqrt{(q-i)(n-q+i+1)}.
$$
这逐项验证了实际 primitive 条件。

## 3. 全阶最小逆的有限公式

对 $0\le k\le h$，令 $v_k$ 为 $D_{\rm a}^kv=g_\varepsilon$ 在整个第 $q+k$ 孔层中的最小范数解，约定 $v_0=g_\varepsilon$。下面同时证明存在性和准确公式：
$$
\boxed{
v_k=
\frac1{\sqrt{Z_\varepsilon}}
\sum_{j=0}^q
(-1)^j\varepsilon^{j-k}
\binom{k+q-j}{q-j}
\sqrt{\frac{(q-j)!\,(n-q-k+j)!}
{j!\,(q+k-j)!\,(n-q)!}}\,
e_jw_{q+k-j}.
}
\tag{3.1}
$$
所有阶乘指标非负，由 $n\ge q+h$ 保证。

### 3.1 求解公式只用有限右逆

在所用弱孔层上定义实际上升右逆
$$
Rw_j=\frac{w_{j+1}}{\sqrt{(j+1)(n-j)}}\quad(0\le j<n),\qquad Rw_n=0.
$$
这里仅在出现的有限层使用它，不称其为全空间 $D_{\rm w}^{-1}$。
在实际使用、尚未到达顶层的输入上 $D_{\rm w}R=I$；$R$ 在整个有限弱簇上有界，并与强簇算子交换。因此
$$
\mathcal J
=\varepsilon^{-1}R
\sum_{\ell=0}^q(-\varepsilon^{-1}D_{\rm s}R)^\ell
$$
在所需输入上满足 $D_{\rm a}\mathcal J=I$。
强簇的幂零性使级数有限；全部非零项的弱孔数不超过 $q+h\le n$。

对 $k\ge1$，有限负二项式展开给
$$
\mathcal J^k
=\varepsilon^{-k}R^k
\sum_{\ell=0}^q
(-1)^\ell\binom{k+\ell-1}{\ell}
\varepsilon^{-\ell}D_{\rm s}^\ell R^\ell.
\tag{3.2}
$$
将 (2.2) 代入，固定最终强孔数 $j$ 后，各项除二项系数外相同；所需有限求和为
$$
\sum_{\ell=0}^{q-j}\binom{k+\ell-1}{\ell}
=\binom{k+q-j}{q-j}.
$$
这恰给 (3.1)。$k=0$ 时 (3.1) 直接退回 (2.2)。
所以
$$
D_{\rm a}^kv_k=g_\varepsilon.
\tag{3.3}
$$

### 3.2 它们是整个布尔空间中的最小解

置换群 $S_q\times S_n$ 酉作用并与 $D_{\rm a}$ 交换。
在第 $q+k$ 孔层，其固定空间的基是
$$
e_jw_{q+k-j},\qquad 0\le j\le q,
$$
故维数为 $q+1$。第 $q$ 孔层的固定空间也有相同维数。

$D_{\rm a}^k$ 在这两个固定空间之间是三角矩阵；其第 $j$ 个对角元为
$$
\varepsilon^k
\sqrt{
\frac{(q+k-j)!}{(q-j)!}
\frac{(n-q+j)!}{(n-q-k+j)!}
}>0.
\tag{3.4}
$$
因而这个矩阵可逆。

对任意完整核向量 $z\in\ker D_{\rm a}^k\cap\mathcal H_{q+k}$，将其平均到上述群的固定空间。平均仍在核中，而 (3.4) 迫平均为零。$v_k$ 本身固定，所以 $v_k\perp z$。
结合 (3.3)，这证明 $v_k$ 正是全空间最小解。

又因为 $D_{\rm a}g_\varepsilon=0$，
$$
v_k\in U_{k+1,q+k}.
$$
$D_{\rm a}v_k$ 仍固定并解 $D_{\rm a}^{k-1}u=g_\varepsilon$，由同一三角唯一性，
$$
\boxed{D_{\rm a}v_k=v_{k-1}.}
\tag{3.5}
$$

上述固定空间中的 $\ker D_{\rm a}^{k+1}$ 为一维：先用 (3.4) 到第 $q$ 孔层，再用 $D_{\rm a}$ 的一维 primitive 核。其 $\ker D_{\rm a}^{k}$ 为零。因此 $U_{k+1,q+k}$ 的固定部分准确由 $v_k$ 张成。

### 3.3 范数渐近及真实比较比

记
$$
a_k=\|v_k\|^2,\qquad a_0=1.
$$
(3.1) 是有限正交和。当 $\varepsilon\downarrow0$ 时，$Z_\varepsilon\to1$，最高负阶来自 $j=0$。所以
$$
\boxed{
a_k\sim
\varepsilon^{-2k}
\frac{(q+1)^{\overline k}}
{(k!)^2(n-q)^{\underline k}},
\qquad 0\le k\le h,
}
\tag{3.6}
$$
其中 $x^{\overline k}=x(x+1)\cdots(x+k-1)$，
$x^{\underline k}=x(x-1)\cdots(x-k+1)$；空积为1。

因各固定高度部分是一维，(3.5) 及真正受限伴随给：对 $v_{h-1}/\sqrt{a_{h-1}}$，原相邻第一下降比准确为
$$
\mathcal C_h(q,n,\varepsilon)
=\frac{a_{h-1}^2}{a_{h-2}a_h}.
\tag{3.7}
$$
将 (3.6) 代入，得到
$$
\boxed{
\lim_{\varepsilon\downarrow0}\mathcal C_h(q,n,\varepsilon)
=
\left(\frac{h}{h-1}\right)^2
\frac{q+h-1}{q+h}
\frac{n-q-h+1}{n-q-h+2}.
}
\tag{3.8}
$$
先令 $q\to\infty$、$n-q\to\infty$，两个额外因子均趋1。
因此任意普遍异权的有效比较常数都至少为 $(h/(h-1))^2$。
这一步只用有限模型；没有把一般 primitive Gram 假设为彼此交换。

## 4. 相邻暗对的全部固定阶伴随矩

现在把剩余背景按相邻暗对和远尾单个位分成张量组件。
每个组件有单位基向量 $\chi_\nu$ 和上升算子 $B_\nu$，满足
$$
B_\nu\chi_\nu\perp\chi_\nu,\qquad
B_\nu^2\chi_\nu=0,\qquad
d_\nu=\|B_\nu\chi_\nu\|.
$$
具体地：

- 对一对相邻权 $b_j,b_{j+1}$，取
  $$
  \chi_\nu=
  \frac{b_{j+1}e_j-b_je_{j+1}}{\sqrt{b_j^2+b_{j+1}^2}},
  \qquad B_\nu=b_jE_j^*+b_{j+1}E_{j+1}^*.
  $$
  上升一次变成两孔顶态，故第二次为零，且
  $$
  d_\nu^2=\frac{(b_j^2-b_{j+1}^2)^2}{b_j^2+b_{j+1}^2}.
  $$
- 对远尾未占据的单个位，取真空和 $B_\nu=b_jE_j^*$，于是 $d_\nu=b_j$。

令 $\chi=\bigotimes_\nu\chi_\nu$，
$D_{\rm b}^*=\sum_\nu B_\nu$，
$\delta^2=\sum_\nu d_\nu^2$。
不同被激活的组件集合给正交张量向量；同一集合的全部排列给阶乘。因此对每个固定 $\ell\ge0$，
$$
\boxed{
\|(D_{\rm b}^*)^\ell\chi\|^2
=(\ell!)^2e_\ell(d_\nu^2)
\le \ell!\,\delta^{2\ell}.
}
\tag{4.1}
$$
这里 $e_\ell$ 是全部组件平方权的第 $\ell$ 个初等对称和。
不等式来自
$\ell!e_\ell(d_\nu^2)\le(\sum_\nu d_\nu^2)^\ell$。

背景算子级数在本题按范数收敛，故可先作有限组件展开，再取算子范数极限；右端的非负对称和也单调收敛。无限远尾没有被删除。

## 5. 全阶最小逆的真实传递及有限 Gram 界

令
$$
\widehat D=D_{\rm a}\otimes I+I\otimes D_{\rm b},
\qquad
D_{\rm b}\chi=0,\quad\|\chi\|=1.
$$
固定活跃 primitive 孔层和单位 $g$。
对所需 $k$，假设活跃 $D_{\rm a}^k$ 到该目标层满射，置
$$
w_k=[D_{\rm a}^k(D_{\rm a}^*)^k]^{-1}g,\qquad
v_k=(D_{\rm a}^*)^kw_k,\qquad a_k=\|v_k\|^2.
$$
令 $x_k$ 为 $\widehat D^kx=g\otimes\chi$ 的全空间最小解，记
$a_k^{\rm full}=\|x_k\|^2$。解集非空，因为 $v_k\otimes\chi$ 是解。
所有最小解均在指定总孔层；若在全直和中极小化，其他正交孔层只增加范数，所得值相同。

取 $W_k=w_k\otimes\chi$。真实二项式展开给
$$
(\widehat D^*)^kW_k
=\sum_{\ell=0}^k\binom k\ell
(D_{\rm a}^*)^{k-\ell}w_k\otimes(D_{\rm b}^*)^\ell\chi.
$$
各项的活跃孔数不同，故严格正交。由 (4.1)，
$$
\|(\widehat D^*)^kW_k\|^2
\le a_k+
\sum_{\ell=1}^k
\binom{k}{\ell}^{2}\ell!\,
\|(D_{\rm a}^*)^{k-\ell}w_k\|^2\delta^{2\ell}.
\tag{5.1}
$$
又 $\langle g,w_k\rangle=a_k$。对任意真实解使用 Cauchy--Schwarz，得到
$$
\boxed{
\frac{a_k^2}
{a_k+\displaystyle\sum_{\ell=1}^k
 \binom{k}{\ell}^{2}\ell!\,
 \|(D_{\rm a}^*)^{k-\ell}w_k\|^2\delta^{2\ell}}
\le a_k^{\rm full}\le a_k.
}
\tag{5.2}
$$
右侧用试探解；左侧不使用全空间像闭性、全局谱隙或核投影连续性。

若活跃参数在一个固定紧邻域中、各有限 Gram 保持正定，且 $k$ 固定，则对 $\delta\le1$，
$$
a_k-C_k\delta^2\le a_k^{\rm full}\le a_k
\tag{5.3}
$$
有共同有限常数 $C_k$。

还有准确的有限维矩阵版本。取活跃 primitive 层中任意固定有限维子空间 $K$，令
$H_k^{\rm a}$ 为其最小逆 Gram；
将 $K$ 通过 $g\mapsto g\otimes\chi$ 嵌入真实 primitive 层，令 $\widetilde H_k$ 为完整最小逆 Gram 在该有限源空间上的压缩。
对任意 $g\in K$，(5.1) 的余项至多
$C_k\delta^2\|g\|^2$。而
$a^2/(a+b)\ge a-b$，所以
$$
\boxed{
H_k^{\rm a}-C_k\delta^2 I_K
\le\widetilde H_k\le H_k^{\rm a}.
}
\tag{5.4}
$$
完整最小逆只需在这些已构造的源上定义，其像通过试探解及核正交投影给出；没有声明全层 Moore--Penrose 逆有界。
(5.4) 也不把压缩后逆与原逆的压缩混同。

### 5.1 任意高度比较的必要标量式

对单位真实 primitive 源 $G$，记 $x_k$ 为 $D^kx=G$ 的真实最小解。则
$$
x_k\in U_{k+1},\qquad A_{k+1}x_k=x_{k-1}.
\tag{5.5}
$$
后一式来自把 $Dx_k$ 投影到 $U_k$，得到同一个 $D^{k-1}$ 方程的唯一最小解。

因而
$$
|\langle x_h,A_{h+1}^*x_{h-1}\rangle|^2
=\|x_{h-1}\|^4.
$$
Cauchy--Schwarz 及 $A_hx_{h-1}=x_{h-2}$ 给真实比较常数的下界
$$
\boxed{
\mathfrak c_h\ge
\frac{(a_{h-1}^{\rm full})^2}
{a_{h-2}^{\rm full}a_h^{\rm full}}.
}
\tag{5.6}
$$
这里始终使用同一个 primitive 源的三个真正最小原像。
不从单个成本收敛直接推出未经支付的算子乘积序。

## 6. 两个活跃簇嵌入原连续尾

固定 $h,q,n,\varepsilon$ 如第2节。对充分大 $m$：

- 强活跃簇取 $[m,m+q)$；
- 弱活跃簇取 $[\ell_m,\ell_m+n)$，其中
  $$
  \ell_m+1=\varepsilon^{-1/2}(m+1)+O(1),
  \qquad \ell_m-m-q\text{ 为偶数}.
  $$
  可向上调整不足2个整数达到这个奇偶条件。

对每个 $s\ge4\cdot2^m$，取
$$
K=m+2s+n-q.
$$
将背景区间
$$
[m+q,\ell_m),\qquad [\ell_m+n,K)
$$
分别按相邻两位配对。两段长度都为偶数，共有 $2(s-q)$ 个位置，因而恰有 $s-q$ 个暗对。
在 $j\ge K$ 取无孔真空。由 $n-q\ge h$，这些区间对充分大的 $m$ 全部合法，且 $s-q\ge0$。

归一化 $\widehat D=D_m/b_m$，$b_m=(m+1)^{-2}$。
活跃权在这个固定有限模型中趋于
$$
(\underbrace{1,\ldots,1}_{q},
 \underbrace{\varepsilon,\ldots,\varepsilon}_{n}).
$$
背景保持真实 $D_{\rm b}\chi=0$；前稿的同一逐对估计给
$$
\boxed{
\delta_{m,s}^2
\le\frac8{5(m+1)}+\frac{(m+1)^4}{3K^3}
\le \kappa_m\longrightarrow0
}
\tag{6.1}
$$
这里可明确取
$$
\kappa_m=\frac8{5(m+1)}
+\frac{(m+1)^4}{3(m+8\cdot2^m+n-q)^3}\longrightarrow0.
$$
对全部 $s\ge4\cdot2^m$ 一致。每个固定高阶随后由 (4.1) 控制，不能改用会随 $m$ 增大的 $\|D_{\rm b}\|^{\ell-1}\delta$。

### 6.1 有限活跃 Gram 及 primitive 向量的连续性

活跃总位数为 $q+n$，而 $n\ge q+h$。对每个 $k\le h$，
$$
D_{\rm a}(c)^k:\mathcal H_{q+k}^{\rm a}\to\mathcal H_q^{\rm a}
$$
在所有正权处满射。

为核此有限事实，先取全部权为1，总位数记为 $M=q+n$。删除 $D$ 和上升 $L=D^*$ 满足
$$
[D,L]|_{\mathcal H_p}=(M-2p)I.
$$
若 $f\in\ker D\cap\mathcal H_j$，归纳给
$$
DL^rf=r(M-2j-r+1)L^{r-1}f.
$$
按 $\mathcal H_p=\operatorname{Ran}L\oplus\ker D$ 逐层作正交分解，得到第 $q$ 层的 primitive 串；在条件 $q+k\le M-q$ 下，每条串继续上升 $k$ 次都有严格正范数，所以 $L^k:\mathcal H_q\to\mathcal H_{q+k}$ 单射。
不同串仍正交，这也可逐次把 $L$ 用伴随 $D$ 移回较低层验证。因此 $D^k$ 满射。

对任意正权 $c$，有限可逆对角矩阵
$$
R_p(c)e_I=\Bigl(\prod_{j\in I}c_j\Bigr)e_I
$$
给
$$
D_{\rm a}(c)^k
=R_q(c)^{-1}D_{\rm a}(1)^kR_{q+k}(c).
$$
故其秩不变。

因此所有有限 Gram 的普通逆在极限权附近连续。
令 $g_0=g_\varepsilon$ 为第2节单位 primitive，取
$$
g(c)=
\frac{P_{\ker D_{\rm a}(c)|_{\mathcal H_q^{\rm a}}}g_0}
{\|P_{\ker D_{\rm a}(c)|_{\mathcal H_q^{\rm a}}}g_0\|}.
$$
该有限核投影连续，分母趋1，所以定义对充分大 $m$ 合法。
这只涉及固定有限活跃矩阵；没有断言无限连续尾的核投影连续。

活跃 $g(c)$、全部 $w_k(c),v_k(c)$ 连续趋于第2—3节的向量。
它们与背景相乘给总第 $s$ 孔层的单位真实 primitive 源
$$
G_{m,s}=g(c)\otimes\chi.
$$
由 (5.2)、(6.1)，对每个 $0\le k\le h$，
$$
a_k^{\rm full}(m,s)\longrightarrow a_k(q,n,\varepsilon)
$$
对全部 $s\ge4\cdot2^m$ 一致。

## 7. 平方常数下界的完成及边界

将上述一致极限用于 (5.6)，对每个固定 $q,n,\varepsilon$ 得
$$
\liminf_{m\to\infty}\inf_{s\ge4\cdot2^m}
\mathfrak c_{m,s,h}
\ge \mathcal C_h(q,n,\varepsilon).
$$
先令 $\varepsilon\downarrow0$，再令 $q\to\infty$、
$n-q\to\infty$，使用 (3.8)，得到定理1.1。
这些极限依次取；没有要求活跃模型大小增长时有限 Gram 连续性的常数一致。

因此，原连续尾在全高孔层上的任何统一相邻第一下降序，若使用常数 $C_h$，都必须满足
$$
C_h\ge\left(\frac{h}{h-1}\right)^2.
$$
这仍只是必要下界。真实比较常数可能更大，甚至可能无统一有限上界；本文未判定。

构造源 $G_{m,s}$ 位于完整 $\ker D_m$，但尚未证明它是原边界向量经完整低链投影后产生的返回源，或属于实际 $\zeta,\sigma$ 的特定来源。
因此它没有否定只在真实窄 Schur 源上成立的较弱估计，也没有构成原 $E_2$、普通不变子空间或一般慢主理想结论的反例。
后续仍须支付原实际源的完整合成范数。
