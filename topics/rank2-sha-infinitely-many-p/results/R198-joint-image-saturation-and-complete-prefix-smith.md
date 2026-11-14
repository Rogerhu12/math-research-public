# R198. 真实共同像的整化层、累计 Smith 与完整前缀证书

日期：2026-11-12。**状态：一般共同像整化恒等式、准确 jump 旗标的
累计 Smith 公式，以及原 $p=23,D=7,k=30$ 完整矩阵证书均已证明。**
本文只校准这一组此前已使用的参数；不扩展素数列表，也不从该
有限例子推断统一的严格范数预算。

## 1. 同一个真实矩阵的全部 p-saturation

令 $\mathcal O=\mathbb Z_p$，$E$ 为秩 $M$ 的原整源，
$$
 J:E\longrightarrow\mathcal O^k
 \tag{1}
$$
是同一组已付整性的实际行。允许 $J$ 有核，也允许目标行有有理
冗余。记其有理秩为 $\rho$，像格为 $I_0=J(E)$，非零整 Smith
指数为 $s_1,\ldots,s_\rho\ge0$。

定义实际源空间及目标空间中的格
$$
 \Lambda_t=\{x\in p^{-t}E:Jx\in\mathcal O^k\},\qquad
 I_t=(p^{-t}I_0)\cap\mathcal O^k,
 \qquad t\ge0.
 \tag{2}
$$
这些格没有改变原有理次数空间。准确有
$$
 \begin{aligned}
 &J(\Lambda_t)=I_t,\qquad
   \ker(J|_{\Lambda_t})=p^{-t}\ker(J|_E),\\
 &\Lambda_{t+1}=p^{-1}\Lambda_t\cap J^{-1}(\mathcal O^k),\qquad
   I_{t+1}=(p^{-1}I_t)\cap\mathcal O^k.
 \end{aligned}
 \tag{3}
$$
第一条例如由 $p^{-t}J(E)$ 的同一个原源原像直接得到；并未要求
各个源 summand 的像分别满足前缀。

**定理 1。** 对每个 $t\ge0$，
$$
 \boxed{\begin{aligned}
 \operatorname{length}(I_t/I_0)
       &=\sum_{i=1}^{\rho}\min(t,s_i),\\
 \operatorname{length}(\Lambda_t/E)
       &=t(M-\rho)+\sum_{i=1}^{\rho}\min(t,s_i).
 \end{aligned}}
 \tag{4}
$$
若 $r_t=\dim_{\mathbb F_p}(I_t\bmod p)$，这里约化指在目标
$\mathcal O^k/p\mathcal O^k$ 中的像，则
$$
 r_t=\#\{i:s_i\le t\},\qquad
 \operatorname{length}(I_{t+1}/I_t)=\rho-r_t,\qquad
 \operatorname{length}(\Lambda_{t+1}/\Lambda_t)=M-r_t.
 \tag{5}
$$

**证明。** 只为证明指数公式，在源、目标作同一整 Smith 换基。
前 $\rho$ 个源坐标的映射是乘 $p^{s_i}$，其余 $M-\rho$ 个坐标
构成核。条件 (2) 在前者上允许除以 $p^{\min(t,s_i)}$，在后者
上允许除以 $p^t$。目标像的相应指数是
$\max(s_i-t,0)$。这同时给出 (4)–(5)。所有格本身仍由 (2)
定义，不依赖这种换基的选择。$\square$

### 1.1. R196 第一层的实际原列

在原 theta 平面取
$$
 E_D=\mathbb Z_p[A,C]_{\le D},\quad C=B-A,\quad
 A=w+\cdots,\quad C=-22w^2+\cdots,
 \qquad p=4r-1\ne11.
 \tag{6}
$$
令 $k=rq+s$，$0\le s<r$、$\lceil r/2\rceil\le q\le p-2$，
并取 R196 的全部连续归一行
$$
              J_n(P)=p^{\lfloor n/r\rfloor}[w^n]P,
                         \qquad 0\le n<k.
 \tag{7}
$$
其模 $p$ 核准确为原权 $i+2j\ge r$ 的列空间。因而 (2) 的
第一层不只是一个可用子格，而准确等于
$$
 \Lambda_1=E_D+p^{-1}H_{D,r},\qquad
 H_{D,r}=\operatorname{span}_{\mathbb Z_p}
                \{A^iC^j:i+j\le D,\ i+2j\ge r\}.
 \tag{8}
$$
若 $N_{D,r}=\#\{(i,j):i+j\le D,i+2j<r\}$，则
$$
 \begin{aligned}
 \operatorname{length}(\Lambda_1/E_D)&=M_D-N_{D,r},\\
 \operatorname{length}(I_1/I_0)&=\rho-N_{D,r},\\
 \operatorname{length}\bigl(\ker(J|_{\Lambda_1})/\ker(J|_{E_D})\bigr)
                                      &=M_D-\rho.
 \end{aligned}
 \tag{9}
$$
尤其不能把源格指数全部记作目标像或 jet 范数的收益。
以后每一层要重新计算 $J|_{\Lambda_t}$ 的实际模 $p$ 核。

## 2. 累计 Smith 与准确 jump 旗标

设 $\ell_n:E\to\mathbb Q_p$ 是按原输出阶排列的真实 jet 行。
先保留真正的有理秩跳行号 $n_1<\cdots<n_\rho$，并记
$$
 K_i=\ker(\ell_{n_1},\ldots,\ell_{n_i})\cap E,
 \qquad K_0=E.
 \tag{10}
$$
此前未选的冗余行在 $\mathbb Q_p$ 上属于已选行的张成空间，
所以 (10) 是原完整连续前缀的准确核，而非仅稀疏选择的核。
各 $K_i$ 在 $E$ 中饱和，并且
$$
              \ell_{n_i}(K_{i-1})=p^{v_i}\mathbb Z_p
 \tag{11}
$$
给出真正的第 $i$ 个 jet 值理想。允许 $v_i<0$。

选择已证明使各行整的整数 $h_i$，置
$$
 J^\mathrm{jump}=(p^{h_i}\ell_{n_i})_{1\le i\le\rho}.
 \tag{12}
$$
令该满行秩矩阵的非零 Smith 指数为 $\sigma_i$。

**定理 2（累计旗标恒等式）。**
$$
 \boxed{\qquad
       \sum_{i=1}^{\rho}v_i
           =\sum_{i=1}^{\rho}\sigma_i-\sum_{i=1}^{\rho}h_i.
 \qquad}
 \tag{13}
$$
因此实际累计局部 jet 对数范数是
$\bigl(\sum h_i-\sum\sigma_i\bigr)\log p$。

**证明。** 从 (11) 的最小赋值原像选取 $e_i\in K_{i-1}$，
使 $\ell_{n_i}(e_i)$ 生成其值理想。于是
$K_{i-1}=\mathbb Z_pe_i\oplus K_i$。依次得到适配整个饱和旗标的
原整基 $e_1,\ldots,e_\rho$ 及 $K_\rho$ 的整基。矩阵 (12)
在前 $\rho$ 列为三角矩阵，对角元赋值为 $h_i+v_i$；其余列
全部为零。故其最大非零 minors 的理想赋值为
$\sum(h_i+v_i)$，亦即 $\sum\sigma_i$。$\square$

若原来的全 $k$ 行有理独立，可以直接对它们使用 (13)。若存在
冗余，不能把包含后期冗余行的 full $J$ 的 minor gcd 代入 (13)。
例如秩一源上的早行 $px$ 与晚行 $x$，真正 jump 只有前一行，
值理想赋值是一；包含两行的最大 minor 理想却是单位。
因此每次使用 (13) 必须先保留准确 jump 行。

## 3. 同一 p=23、D=7、k=30 的完整实际矩阵

取
$$
 p=23,\qquad r=6,\qquad D=7,\qquad k=30=r\cdot5.
 \tag{14}
$$
原源维数 $M_D=36$，并使用准确原整基
$$
 e_{m,c}=A^{m-c}C^c=A^m(B/A-1)^c,
                  \qquad0\le c\le m\le7.
 \tag{15}
$$
式 (15) 右端仅是计算同一个多项式的便利写法，没有向源添加
$B/A$ 这个独立坐标。

矩阵 $J$ 的三十行是 (7)。R196 给
$$
                    N_{7,6}=12,\qquad
                    \operatorname{rank}(J\bmod23)=12.
 \tag{16}
$$
(8) 的实际基只把 $m+c\ge6$ 的二十四个原列除以 $23$。
完整原级数证书直接计算出
$$
              \operatorname{rank}\bigl(J(\Lambda_1)\bmod23\bigr)=30.
 \tag{17}
$$
这包括全部余类、全部早期实际行。R194 中 $j=3$ 的缺阶关联块
前五行只有秩四，并没有使这里的完整矩阵继续缺秩。

(17) 先证明 $J$ 的有理行秩为三十；又由整有限生成像的 Nakayama
引理得到 $I_1=\mathbb Z_{23}^{30}$。结合 (16) 与定理 1，准确有
$$
 \boxed{\quad
 \operatorname{SNF}(J)=(0^{\times12},1^{\times18}),\qquad
 \mathbb Z_{23}^{30}/J(E_7)\simeq(\mathbb Z/23\mathbb Z)^{18}.
 \quad}
 \tag{18}
$$
源的第一层指数为二十四，实际像指数为十八，准确核的格指数为六。
它们在 (9) 中严格相符。

## 4. 同一完整前缀的真正逐行值理想

全部三十行有理独立，所以它们本身就是原连续前缀的 jump 行。
记 $K^{<n}=E_7\cap\bigcap_{j<n}\ker\ell_j$。
对原矩阵逐行作最小赋值的整列消元，独立得到
$$
 \begin{array}{c|rrrr}
 n&0\ldots7&8\ldots15&16\ldots23&24\ldots29\\ \hline
 v_{23}\bigl(\ell_n(K^{<n})\bigr)&0&-1&-2&-3 .
 \end{array}
 \tag{19}
$$
在第零行前取整个源。
这些列变换的系数全部在 $\mathbb Z_{23}$ 中，没有先把不同
summand 分别前缀化。

由 (7)，三十个归一指数之和为
$$
          \sum_{n=0}^{29}\lfloor n/6\rfloor=60.
$$
式 (18) 的 Smith 总和为十八，所以 (13) 准确给
$$
            \sum_{n=0}^{29}v_n=18-60=-42,
 \tag{20}
$$
与 (19) 的 $-8-16-18=-42$ 一致。
因此这一真实完整前缀的累计对数范数为 $42\log23$，
而逐行只用 $p^{\lfloor n/r\rfloor}$ 整性给的是 $60\log23$。
这十八层收益来自实际共同像的整化，不来自对坏对角块的忽略。

## 5. 精确短证书与范围

[证书脚本](../scripts/check-joint-prefix-saturation.py) 从既有固定
$P,Q,W$ 级数计算 (15)，再用实际 $w=s\mathcal L(s)^4$ 反演回
原 $w=z^4$。程序分别核查：

- $J$ 及同一个第一整化格的全部元素确实整；
- 两个模 $23$ 秩为十二和三十；
- 原连续矩阵的整列消元给全部三十个 (19) 的值理想；
- 源、核、像三个指数及 (20) 的累计恒等式相符。

两个秩已经足以通过定理 1 证明全部 (18)，无需把浮点奇异值或
某个未饱和行列式当成 Smith 指数。逐行证书与整像秩使用不同的
消元任务，在同一个原矩阵上交叉核对。

本结果尚未给出随 $D,k,p$ 统一的全部 $r_t$，也未把有限例子
外推成严格预算。对于进一步 Schur 消元，(2)–(5) 给出的正是
需计算的实际共同像及其核；(13) 则把这些指数准确接回真正的
原前缀范数。

依赖：

- [R194：原列缺阶块和有界 w 第一带](R194-sparse-jet-smith-and-actual-lacunary-hermite-blocks.md)。
- [R196：连续第一带准确核与第一整化格](R196-continuous-first-band-euler-pade-kernel.md)。
- [固定原平面系列和饱和前缀消元](../scripts/check-theta-plane-saturated-jets.py)。
