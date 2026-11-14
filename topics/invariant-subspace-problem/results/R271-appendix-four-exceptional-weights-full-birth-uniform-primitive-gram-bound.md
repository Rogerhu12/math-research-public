# R271 附录：四个独立异权与任意等权池的全出生统一相邻界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：完整证明；逐一使用已付固定块，并支付原全空间的完整逆约化。

## 1. 整个有限模型的结论

在 $N=M+4$ 个物理位的 Boolean Hilbert 空间中取
$$
D=\sum_{i=1}^4a_iE_i+\sum_{j=5}^{M+4}E_j,
\qquad a_i>0,\qquad M\in\mathbb Z_{\ge0}.
$$
$\mathcal H_s$ 表示实际 $s$ 孔层，$K_s=\ker D\cap\mathcal H_s$。
对
$$
0\le s\le\lfloor N/2\rfloor,\qquad h=N-2s,
$$
定义
$$
F_n^{(s)}=\frac{D^n(D^*)^n|_{\mathcal H_s}}{(n!)^2},
\qquad
\Gamma_n^{(s)}=P_{K_s}(F_n^{(s)})^{-1}|_{K_s},
\qquad0\le n\le h.
\tag{1.1}
$$
这里总是先在整个 $\mathcal H_s$ 上取逆，再压到 $K_s$。

**定理。** 对任意四个独立正头权、任意单位池长 $M$、任意合法出生 $s$，
$$
\boxed{
\Gamma_n^{(s)}(\Gamma_{n+1}^{(s)})^{-1}\Gamma_n^{(s)}
\preceq16\Gamma_{n-1}^{(s)},
\qquad1\le n<h.
}
\tag{1.2}
$$
常数与头权比例、池长、出生层及相邻高度均无关。

本稿新增的是整个 $K_s$ 的结论。各固定块的估计已经分别建立；
这里必须证明真实正交分块穷尽全空间，而且保持完整逆。
这与任意正权模型的一般 primitive 压缩不同。

## 2. 完整逆的合法范围

先对全部权为一的有限 Boolean 删除使用 §3 的正交 Lefschetz 串。
每条到达第 $s$ 层的串从其 primitive 出生一直延续到对称的最高层。
若 $n\le N-2s$，该串中的第 $s+n$ 层仍存在，且 $D^n$ 的系数非零。
所以
$$
D(1)^n:\mathcal H_{s+n}\longrightarrow\mathcal H_s
$$
满射。

对一般正物理权，令
$$
R_pe_I=\left(\prod_{i\in I}a_i\right)e_I
$$
（池位的 $a_i=1$）。准确有
$$
D(a)^n=R_s^{-1}D(1)^nR_{s+n}.
\tag{2.1}
$$
这些有限维正对角矩阵可逆，因此保持秩。
故 (1.1) 所需的整个 $F_n^{(s)}$ 严格正定；
其压缩 $\Gamma_n^{(s)}$ 也严格正定。
(2.1) 只用于满射性，不把它当作保持 Hilbert 范数的酉相似。

## 3. 原等权池的完整共同正交串

在原 $M$ 位等权池中记删除为 $D_{\rm w}$。
在第 $j$ 孔层，
$$
[D_{\rm w},D_{\rm w}^*]=(M-2j)I.
\tag{3.1}
$$
对每个 $0\le j\le\lfloor M/2\rfloor$，取
$\ker D_{\rm w}\cap\mathcal H_j^{\rm w}$ 的一组正交归一基。
对其中任意一个 $\eta$，置
$$
L=M-2j,\qquad
\eta_r=\frac{(D_{\rm w}^*)^r\eta}
{\sqrt{r!\,L^{\underline r}}},
\qquad0\le r\le L.
\tag{3.2}
$$
从 (3.1) 逐次交换得
$$
D_{\rm w}\eta_r=\sqrt{r(L-r+1)}\,\eta_{r-1},
\qquad
D_{\rm w}^*\eta_r=\sqrt{(r+1)(L-r)}\,\eta_{r+1},
\tag{3.3}
$$
越界项为零。因此每条串同时约化 $D_{\rm w}$ 和 $D_{\rm w}^*$。

这里给完整性核验，避免只写出一族试探串。
不同 primitive 基向量的串正交：同出生时反复移伴随；
不同出生时将多余的上升移回，较高出生的 primitive 正交于真实上升像。
当 $j<M/2$，由 (3.1)
$$
\|D_{\rm w}^*v\|^2-\|D_{\rm w}v\|^2=(M-2j)\|v\|^2
$$
知上升在该层单射。因此第 $j$ 个 primitive 维数为
$$
\binom Mj-\binom M{j-1}.
$$
在任一池孔层 $p$，能到达它的串恰有
$j\le\min(p,M-p)$；
这些维数望远镜相加正好为 $\binom Mp$。
所以全部串的正交和就是原池整个 Hilbert 空间。
$M=0$ 时也成立：只有 $j=0,L=0$ 的一维串。

(3.3) 与 $L$ 个单位物理位的归一对称层完全相同。
因此每条原弱串酉等价于一个 $L=M-2j$ 位单位池的置换固定部分，
但物理孔层有固定平移 $j$。

## 4. 完整逆随这些串真正分块

将每条池串与四个实际头位张量。
由 (3.3)，所得子空间同时约化完整 $D$ 与 $D^*$，并保持总孔数。
故在每个 $\mathcal H_s$ 中，它们的正交投影与
$$
D^n(D^*)^n,\quad F_n^{(s)},\quad(F_n^{(s)})^{-1}
$$
交换；最后一步使用 §2 已付的严格正定性。
同样，primitive 核与其正交投影也按这些块分解。

因此完整 Gram 逆、primitive 压缩，以及压缩后的逆全部按同一正交直和分块。
不是先作任意压缩，再把压缩的逆冒充完整逆。

固定原出生 $s$ 和一条出生于 $j$ 的弱串，写
$$
t=s-j,\qquad L=M-2j.
$$
该块的实际删除和伴随酉等价于“四个头权 $a_i$ 加 $L$ 位单位池固定部分”，
相对出生恰为 $t$。
所有块有同一个合法串长：
$$
\boxed{
L+4-2t=M+4-2s=h.
}
\tag{4.1}
$$
所以对同一个原比较 $1\le n<h$，每块所需的三个阶
$n-1,n,n+1$ 都在其真实合法范围内。

虚拟 $L$ 位池的置换平均也同时约化其完整 $D,D^*$。
故该虚拟全空间完整逆限制到固定部分，正是本原弱串块中的逆。
这一步把既有固定块的完整 MP 结论准确接到原 $M$ 位全空间；
没有遗失固定块之外可能降低最小范数的方向。

## 5. 所有可能的相对出生

以下只须处理 $h\ge2$；否则没有相邻比较。

若 $t<0$，该块没有目标向量。
若 $t\ge5$，(4.1) 给
$$
L=h+2t-4\ge2t-2.
$$
相对第 $t$ 和第 $t-1$ 层此时都以全部十六个头集合 $A\subseteq[4]$ 为索引，
对应池孔数为 $t-|A|$ 与 $t-1-|A|$。
前者在 $1,\ldots,L$ 内，后者在 $0,\ldots,L$ 内。
删除按头集合大小是三角矩阵；其池删除对角元为
$$
\sqrt{(t-|A|)(L-t+|A|+1)}>0.
$$
因此这两个固定层间的删除可逆，primitive 核为零。

所以全部非零 primitive 块只可能有
$$
\boxed{t=0,1,2,3,4.}
\tag{5.1}
$$
下面逐类核对所用结论及短池端点。

### 5.1 相对出生 $t=0$

这是一个真空标量源。对 $0\le n\le h=L+4$，
$$
\Gamma_n=
e_n(a_1^2,a_2^2,a_3^2,a_4^2,\underbrace{1,\ldots,1}_{L})^{-1}.
$$
正权实根多项式的 Newton 不等式给
$$
\frac{\Gamma_n^2}{\Gamma_{n-1}\Gamma_{n+1}}
=\frac{e_{n-1}e_{n+1}}{e_n^2}<1.
$$
这包含 $L=0,1$，不需要一个正长度弱池。

### 5.2 相对出生 $t=1$

此时 $h=L+2$，允许全部 $L\ge0$。
[出生一全部短池和完整固定块](R271-appendix-four-exceptional-birth-one-short-pools-and-complete-fixed-block-bound.md)
已付
$$
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\preceq16\Gamma_{n-1},
\qquad1\le n<L+2.
$$
其全部短端逐一为：
$L=0$ 的真实三维四位角用已证三异权结果；
$L=1,2$ 的全部短边由真实受约束 MP 的 $9/4$ 迹证书；
$L=3$ 的首边为 $2$、中两边为 $9/4$；
$L\ge4$ 由已付首边、次边和中段统一界。
这里没有假设原源始终四维；$L=0$ 的降维条件已在该稿支付。

### 5.3 相对出生 $t=2$

此时 $h=L$，故合法比较迫 $L\ge2$。

- $L=2$：
  [R239 四异权完整高度二](R239-appendix-four-exceptional-weights-full-height-two-primitive-gram-bound.md)
  已付该真实固定六维块的严格常数 $1$。
- $L=3$：
  [三位短池真实最小逆](R271-appendix-four-exceptional-weights-three-pool-exact-trace-bound.md)
  已付两个相邻边的严格常数 $9/4$；使用完整约束 $F([4])=0$。
- $L\ge4$：
  [任意池长低边](R271-appendix-four-exceptional-weights-arbitrary-pool-low-edge-uniform-trace-bound.md)
  已付首尾边常数 $3$，并与 R239 已证中段组合为整个固定块
  $4L/(L-3)\le16$。

$L=0,1$ 时 $h<2$，没有被遗漏的比较。

### 5.4 相对出生 $t=3$

此时 $h=L-2\ge2$，自动有 $L\ge4$。
这正是
[R239 倒数第二出生固定块 §§9--10](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)
的 $q=4$ 范围。
其已经证明的全部端点及内部相邻常数为
$$
q^2=16.
$$
不是仅引用原一参数公式，而是引用其后独立支付的全相邻上界。
短池 $L<4$ 在当前 $h\ge2$ 的问题中不出现。

### 5.5 相对出生 $t=4$

此时 $h=L-4\ge2$，所以 $L\ge6$。
[R239 饱和固定线 §8](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)
已对任意多个独立头权给出完整最小逆与固定正矩。
取其中 $q=4$，在全部 $n+1\le L-4$ 上，
$$
\Gamma_n^2<
\frac{4+n}{5+n}\Gamma_{n-1}\Gamma_{n+1}.
$$
该真实固定 primitive 块只有一维，所以直接给常数小于一。
所引公式只在头饱和的一维块使用，未推广为一般矩阵 Hankel 正性。

## 6. 正交合并与统一常数

§5 的五类都已在相同的原相邻阶 $n$ 上支付常数至多十六。
由 §4，原 $K_s$ 是这些真实 primitive 块的有限正交直和，
$\Gamma_{n-1},\Gamma_n,\Gamma_{n+1}$ 及其逆都是同一分块的直和。
逐块相加即得 (1.2)。

在整个推导中，固定块内的非正交源 Gram 只通过已付的同余
$$
H_nH_{n+1}^{-1}H_n\preceq cH_{n-1}
$$
读取；全空间拼合使用原 Hilbert 空间中的正交串。
这两种步骤各自保持真实乘积次序，没有假设各阶 Gram 可交换。

### 6.1 短原池的较小常数

若原池长 $0\le M\le3$，每条弱串都有 $0\le L\le3$。
在 $h\ge2$ 时不出现相对出生三或四。
出生一、二的全部可出现短块均已付严格常数 $9/4$，
真空块为严格常数一。因此在整个 $K_s$ 上，
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n
\prec\frac94\Gamma_{n-1},
\qquad M\le3,\quad1\le n<h.
}
\tag{6.1}
$$
特别任意五个正物理权，整体缩放其中一个为一，便是 $M=1$；
故该任意五位模型的所有合法 primitive 相邻比较均满足 (6.1)。
这里的严格式按非零 primitive 空间理解。

### 6.2 等权池的共同权和原第一下降常数

若原池共同正权是 $b$ 而非一，对全部删除作整体除以 $b$。
$\Gamma_n$ 相应乘一个几何因子，(1.2) 的两边具有同一因子，
所以同一常数仍成立。

先用严格正矩阵的 Schur 等价把 (1.2) 的邻居反转，取 $n=\ell-1$，得到
$$
16\Gamma_\ell\succeq
\Gamma_{\ell-1}\Gamma_{\ell-2}^{-1}\Gamma_{\ell-1}.
$$
由原归一化关系 $\Gamma_n=(n!)^2H_n^{\rm MP}$，准确有
$$
16\left(\frac{\ell}{\ell-1}\right)^2H_\ell^{\rm MP}
\succeq H_{\ell-1}^{\rm MP}(H_{\ell-2}^{\rm MP})^{-1}H_{\ell-1}^{\rm MP}.
$$
再用[有限—原尾归约稿](R271-appendix-universal-adjacent-height-constants-finite-models-and-continuous-tail.md)
§1 的真实第一下降同余 (1.3)–(1.5)，得到此有限模型实际相邻第一下降块的界
$$
A_{\ell+1}A_{\ell+1}^*
\preceq16\left(\frac{\ell}{\ell-1}\right)^2A_\ell^*A_\ell,
\qquad\ell\ge2
$$
（仅在对应的合法出生和孔层上）。
这是原正交高度的第一下降块，不是整个 $D$ 的算子序。
其粗上界至多六十四，与出生和池长无关。

## 7. 完成范围

本稿完整覆盖“四个任意独立正权位，加任意大小的共同正权池”的全部出生和全部 primitive 表示。
主常数十六未声称最优；小池更精确的常数由真实迹证书保留。

一般任意数量独立异权、任意有限正权型的普遍上界以及原连续尾的全部相邻比较，仍不能从本模型直接推出。
既有有限模型与连续尾的双向归约需要覆盖所有有限权型，而本稿使用了实际等权池的共同正交串。
本定理也没有将有限相邻常数直接代入原边界窄 Schur 返回源，或删去它的真实来源费用。
