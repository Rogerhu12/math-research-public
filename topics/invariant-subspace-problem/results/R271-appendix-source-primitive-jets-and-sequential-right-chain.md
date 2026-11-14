# R271 附录：实际源的 primitive jets、全部自由坐标与顺次最小右链

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_rebuild。

状态：**已证明。** 本文把[完整左坐标](R271-appendix-full-left-primitive-coordinates-and-boundary-schur.md)中的真实源约束完全对角化到有限头旗，识别全部自由坐标，并证明跨界右段精确只依赖同一个原源。没有把该显式右链认成完整旗上的全局最小链，也没有得到所需三 Gram 上界。

## 1. 一般短核的 primitive Taylor 公式

继续原 $m\ge5$、$d=2^m$、$4d\le q\le e^{d^3/4}$，写 $D=D_m$、$A=A_m$、$P_0=P_{\ker D}$。固定有限孔层上的 $D_n$ 满射，其单步 Moore--Penrose 逆有界。以下只在有限多个孔层使用它。

对 primitive 输入，沿前稿记顺次最小原像为 $Q_t$，即
$$
Q_t|_{K_n}=D_{n+t}^{\dagger}\cdots D_{n+1}^{\dagger}|_{K_n},
\quad K_n=\ker D\cap\mathcal H_n.
$$
它满足 $DQ_t=Q_{t-1}$、$P_0Q_t=0$（$t\ge1$）。因此对所有允许的 $k,t$，
$$
\boxed{P_0D^kQ_t|_{K_n}=\begin{cases}I,&k=t,\\0,&k\ne t.\end{cases}}
\tag{1.1}
$$
当 $k<t$，左侧为 $P_0Q_{t-k}=0$；当 $k>t$，剩下一个正次 $D$ 作用于 primitive 输入。

若 $f\in\ker D^s\cap\mathcal H_n$，逐层使用
$$
f=P_0f+D_n^\dagger Df
$$
并重复到 $D^sf=0$，得到有限的准确式
$$
\boxed{f=\sum_{k=0}^{s-1}Q_kP_0D^kf.}
\tag{1.2}
$$
第 $k$ 项的输入在 $K_{n-k}$，输出回到 $\mathcal H_n$；负孔项自然为零。所有使用的最大总孔数仍有限。不同 $Q_k$ 像不必正交，(1.2) 是由 (1.1) 分离的唯一有限坐标展开。

## 2. 完整原源约束的精确 jets

沿前稿记
$$
\mathscr P_q=\mathbb C^d\otimes\bigoplus_{n=0}^qK_n,
\quad
\mathcal E=P_{\le q}\sum_{t=0}^{d-1}(-A)^tQ_t,
\quad
\mathcal B=E_q\mathcal E.
$$
其源式是
$$
\mathcal Bp=\sum_{t=0}^{d-2}(-1)^tA^{t+1}Q_tp_{q-t}.
\tag{2.1}
$$
对原完整源空间
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_i\bigl(\ker D^{d-i-1}\cap\mathcal H_q\bigr)
$$
中的 $r$，定义
$$
g_k(r)=P_0D^kr,\qquad 0\le k\le d-2.
$$
由源旗，$D^kr$ 只能在头指标 $i\le d-k-2$ 非零；故
$$
g_k(r)\in\operatorname{Ran}A^{k+1}\otimes K_{q-k}.
\tag{2.2}
$$
由 (1.1) 对 (2.1) 逐项取 jet，恰有
$$
\boxed{g_k(\mathcal Bp)=(-1)^k A^{k+1}p_{q-k}.}
\tag{2.3}
$$
反过来，由 (1.2)，$r=\sum_{k=0}^{d-2}Q_kg_k(r)$。所以全部 (2.3) 是完整约束 $\mathcal Bp=r$ 的充要条件，不仅是必要条件。

## 3. 全部自由坐标及强制三角坐标

原 $A$ 严格上三角且第一条上对角线非零，所以
$$
\ker A^{k+1}=\operatorname{span}\{e_0,\ldots,e_k\},
\quad
\operatorname{Ran}A^{k+1}=\operatorname{span}\{e_0,\ldots,e_{d-k-2}\}.
$$
令
$$
A_k=A^{k+1}|_{(\ker A^{k+1})^\perp}:
\operatorname{span}\{e_{k+1},\ldots,e_{d-1}\}
\longrightarrow\operatorname{Ran}A^{k+1}.
\tag{3.1}
$$
它是保原物理内积的有限维同构；不以抽象 Jordan 基替换其实际逆。

全部零源 primitive 坐标空间准确为
$$
\boxed{
\begin{aligned}
\mathscr F:=\ker\mathcal B
={}&\left(\mathbb C^d\otimes\bigoplus_{n\le q-d+1}K_n\right)\\
&\oplus\bigoplus_{k=0}^{d-2}
\left(\ker A^{k+1}\otimes K_{q-k}\right).
\end{aligned}}
\tag{3.2}
$$
这是坐标空间中的原正交直和。其正交补为强制三角坐标
$$
\boxed{\mathscr T=\mathscr F^\perp
=\bigoplus_{k=0}^{d-2}
\left(\operatorname{span}\{e_{k+1},\ldots,e_{d-1}\}\otimes K_{q-k}\right).}
\tag{3.3}
$$
每个原源 $r$ 唯一强制了
$$
\boxed{\sigma_k(r)=(-1)^k(A_k^{-1}\otimes I)g_k(r),
\qquad \sigma(r)=\bigoplus_{k=0}^{d-2}\sigma_k(r)\in\mathscr T.}
\tag{3.4}
$$
全部可行 $p$ 恰为 $\sigma(r)+\mathscr F$。
因此 $B_{\mathscr T}=\mathcal B|_{\mathscr T}:\mathscr T\to\mathscr R_q$ 是有界同构，(3.4) 是其实际逆。各有限头逆 $A_k^{-1}$ 的大小仍须支付，没有温和上界被隐去。

## 4. 跨界右段准确杀掉全部自由坐标

沿前稿写
$$
\mathcal Z=\sum_{t=0}^{d-1}(-A)^tQ_t,
\qquad \mathcal C_R=P_{>q}\mathcal Z.
$$
若自由坐标的输入孔数为 $n\le q-d+1$，其 $\mathcal Z$ 输出最高只到 $q$。
若输入位于 $n=q-k$ 且头在 $\ker A^{k+1}$，跨界必须有 $t\ge k+1$，而对应项含 $A^t$，故准确为零。
这证明 $\mathscr F\subset\ker\mathcal C_R$。

另一方面，前稿完整旗身份 $F_{\rm flag}\mathcal C_R=-\mathcal B$ 给反向包含。因此
$$
\boxed{\ker\mathcal C_R=\ker\mathcal B=\mathscr F.}
\tag{4.1}
$$
特别，任意两个左可行向量只要具有同一首源，按这套顺次 MP 坐标作全 $L$ 核延拓时，其整个右侧延拓完全相同。

## 5. 同一个原源的显式顺次 MP 右链

对 $r\in\mathscr R_q$，令
$$
\widehat Q_jr=D_{q+j}^{\dagger}\cdots D_{q+1}^{\dagger}r,
\qquad 1\le j\le d-1.
$$
这些正是[全尾正规化](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md) §14.2.A 的真正顺次单步最小原像。定义正首源链
$$
\boxed{(\mathcal R_{\rm seq}r)_j
=(-1)^{j-1}A^{j-1}\widehat Q_jr
\quad(1\le j\le d-1),\qquad
(\mathcal R_{\rm seq}r)_d=0.}
\tag{5.1}
$$
$A$ 只作用于头，与每个单步 MP 逆交换。
首段有 $D(\mathcal R_{\rm seq}r)_1=r$，相邻段由 $D\widehat Q_{j+1}=\widehat Q_j$ 相消，最右端由 $A^{d-1}r=0$ 消失。

完整逐头旗也直接成立。原头 $\ell$ 的 $r_\ell$ 属于 $\ker D^{d-\ell-1}$；经 $\widehat Q_j$ 属于 $\ker D^{d-\ell-1+j}$，而 $A^{j-1}$ 只落在 $i\le\ell-j+1$，故 $d-i\ge d-\ell-1+j$。头指标亦满足 $i\le d-j-1\le d-j$。于是
$$
\boxed{\mathcal R_{\rm seq}r\in\ker S,\qquad
F_{\rm flag}\mathcal R_{\rm seq}r=r.}
\tag{5.2}
$$

下面核对它与 $\mathcal C_R$ 的完全相同，而不只比较首源。
由 (1.2) 及顺次 MP 的组合，
$$
\widehat Q_jr=\sum_{k=0}^{d-2}Q_{j+k}g_k(r),
$$
这里若暂时定义到较高阶，只用有限孔层单步逆即可。乘 $A^{j-1}$ 后，(2.2) 使全部 $j+k\ge d$ 的项为零。因此有效项最多到 $j+k=d-1$，全部落在前稿原 $Q_t$ 预算内。另一方面，由 $g_k(r)=(-1)^kA^{k+1}p_{q-k}$，右第 $j$ 段准确为
$$
\begin{aligned}
(\mathcal C_Rp)_j
&=\sum_{k=0}^{d-1-j}(-1)^{j+k}A^{j+k}Q_{j+k}p_{q-k}\\
&=(-1)^j A^{j-1}\sum_{k=0}^{d-1-j}Q_{j+k}g_k(r).
\end{aligned}
$$
所以
$$
\boxed{\mathcal C_Rp=-\mathcal R_{\rm seq}(\mathcal Bp).}
\tag{5.3}
$$
不同阶 $Q_t$ 并未被当成多步 MP 逆；$\mathcal R_{\rm seq}$ 也不被当成原完整旗上范数最小的 $\mathcal R_q$。

## 6. 一次消掉全部自由坐标的真实左度量

将 $\mathcal D=\mathcal E^*\mathcal E\succeq I$ 按 $\mathscr F\oplus\mathscr T$ 写成
$$
\mathcal D=\begin{pmatrix}D_{FF}&D_{FT}\\D_{TF}&D_{TT}\end{pmatrix}.
$$
令
$$
\boxed{S_{\rm src}=D_{TT}-D_{TF}D_{FF}^{-1}D_{FT}.}
\tag{6.1}
$$
由真实最小化及 $\mathcal D\succeq I$，有 $D_{FF}\succeq I$、$S_{\rm src}\succeq I$。
源 $r$ 的真实左最小坐标为
$$
\boxed{p_{\min}
=\sigma(r)-D_{FF}^{-1}D_{FT}\sigma(r),}
\tag{6.2}
$$
其中第二项位于 $\mathscr F$。准确能量及原源 Gram 是
$$
\boxed{\mu_q(r)^2
=\langle S_{\rm src}\sigma(r),\sigma(r)\rangle,
\qquad J_q=B_{\mathscr T}S_{\rm src}^{-1}B_{\mathscr T}^*.}
\tag{6.3}
$$
特别给出同一个实际源的必要估计
$$
\boxed{\sum_{k=0}^{d-2}
\|(A_k^{-1}\otimes I)P_0D^kr\|^2
\le\mu_q(r)^2.}
\tag{6.4}
$$

若 $y=J_q^{-1}r$、$c^\flat=F_{\rm flag}^*y$，前稿的准确配对 $\mathcal Dp=-\mathcal C_R^*c^\flat$ 及 (4.1) 还给
$$
\boxed{S_{\rm src}\sigma(r)
=-(\mathcal C_R|_{\mathscr T})^*c^\flat.}
\tag{6.5}
$$
右端在强制空间中，因为 $\mathcal C_R$ 精确杀掉 $\mathscr F$。
因此没有删除任何中间边界坐标；它们的自由头部分与低孔部分共同经 (6.1) 消元。

## 7. 裸输入与全右最小链仍须保留的区别

沿[首段先消元](R239-appendix-boundary-first-elimination-small-sources-and-exact-return-energy.md) §3，令 $P_L$ 为完整右输入的低出生投影，$Z=\ker S_L$，$\mathcal U=Z\ominus\ker(F|_Z)$。完整链的低部分属于 $Z$，具有相同首源，故
$$
\boxed{a(r)=P_{\mathcal U}P_L\mathcal R_{\rm seq}r}
\tag{7.1}
$$
是真正的裸最小原像。完整右最小链则为
$$
\boxed{\mathcal R_qr
=P_{(\ker F_{\rm flag})^\perp}\mathcal R_{\rm seq}r,}
\tag{7.2}
$$
其中 (7.2) 的投影在 $\ker S$ 内取。
两个不同投影不得混同，亦不得将整个顺次链的范数换成裸费。

本稿完成的是原 $\mathcal B$ 约束及全部自由坐标的显式化。真正未付的仍是 (6.3) 的 $S_{\rm src}$，相对于 (7.1) 的裸费和 (6.5) 中的完整 $c^\flat$ 范数的足够温和比较。原目标子序列常数 $O(e^{d^3/4}/d)$、无权 $N=M$ 及普通复 Hilbert ISP 均未由这些准确等式自动得到。
