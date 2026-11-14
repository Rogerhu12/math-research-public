# R218 — 原整源的全次数交集递推与真实 jump 收益

日期：2026-11-12。**状态：全次数、全深度及全部连续前缀的有限像递推已证明；满秩时给全部 truncated Smith 的准确正项分解，并合法传递到原真实 jump。原交集的深度增长尚未证明，主目标仍未完成。**

本篇继续 R216。小素数处不使用可能非整的消低截面，而始终使用原整直和 $K_D\oplus A^2E_{D-2}$。代价不是把低块的耦合删掉，而是把它准确保存在两个真实有限模交集中。这给一条可以反复应用的原像递推。

## 1. 同一原双分量目标

取惰性素数
$$
 p=4r-1\ge7,\qquad p\ne11,\qquad O=\mathbf Z_p,
$$
并取 R215 的全深原行权 $e_j=e_{p,j}$。原源、参数及双分量为
$$
 E_D=O[A,C]_{\le D},\qquad v_0=-22,\qquad
 v=\sqrt{C/v_0},\qquad C=v_0v^2,
$$
$$
 \alpha(v)=A(w(v))=u(C)+v\beta(C),\qquad
 H(v)=U_H(C)+\alpha(v)V_H(C).
 \tag{1}
$$
偶行 $2m$ 读取 $p^{e_{2m}}[C^m]U_H$，奇行 $2m+1$ 读取
$p^{e_{2m+1}}[C^m]V_H$。

这是同一个原 $w$ 目标的整单位下三角变换。R214 §10 与 R216 使用的目标证明只需
$$
 A/w,\quad C/(v_0w^2),\quad v/w,\quad w(v)/v,\quad \alpha/v
                         \in\mathscr B_e
$$
及 $e$ 的超可加性，不需要 $r>2D$。这些单位和平方根的递推只除以二；固定分母五及 $v_0$ 在本篇素数处均为单位。因此该目标证明也包含 $p=7$。本篇不使用 R216 删 $C$ 商中需要 $e_2=0$ 的步骤。

固定精度 $N\ge1$。以
$$
 \mathcal V_k=(O/p^N O)^k,\qquad k\ge0
$$
表示保留行 $0,\ldots,k-1$ 的目标；$\mathcal V_0=0$。记同一原源的实际有限像为
$$
 I_{D,k,N}=\operatorname{im}(J_{D,<k}:E_D\to\mathcal V_k),
 \qquad L_N(D,k)=\operatorname{length}_O I_{D,k,N}.
 \tag{2}
$$
记 $m_D=\binom{D+2}{2}$，定义完整源缺额
$$
                         B_N(D,k)=Nm_D-L_N(D,k).             \tag{3}
$$
若有理秩不足，(3) 包含源核的 $N$ 倍长度；只有满列秩时，它才等于
$\sum_i\min(N,s_i)$。下文不会把未观测的源核长度称为真实 jet 收益。

## 2. 乘 A² 的准确整目标算子

置
$$
 T(C)=2u(C),\qquad
 \mathcal N(C)=u(C)^2-\frac C{v_0}\beta(C)^2,\qquad
 M(C)=\begin{pmatrix}0&-\mathcal N\\1&T\end{pmatrix}.
$$
乘原函数 $A$ 在双分量目标上就是 $M$，因而乘 $A^2$ 是 $M^2$。准确分解为
$$
 M(C)^2=\mathcal U(C)\frac C{v_0}I,\qquad
 \mathcal U(C)=\frac{v_0}{C}M(C)^2.
 \tag{4}
$$
$\mathcal U$ 是乘实际标量单位 $\alpha(v)^2/v^2$ 的双分量矩阵。
该单位及其逆在 $\mathscr B_e$ 中，所以 $\mathcal U$ 在全部加权目标上为整单位下三角算子。

令 $k^-=\max(k-2,0)$。因为 $A$ 首项为 $w$，输出至第 $k-1$ 行只读输入至第 $k-3$ 行，故有确定的有限目标映射
$$
                 \Sigma_k:\mathcal V_{k^-}\longrightarrow\mathcal V_k.
 \tag{5}
$$
它先把第 $m$ 行送到第 $m+2$ 行，并乘
$v_0^{-1}p^{e_{m+2}-e_m}$，再施加整单位算子 $\mathcal U$。
没有读取任何未来输入。

因此其整个有限目标核长度准确为
$$
 c_{p,N}(k)
  =\sum_{m=0}^{k^--1}\min\{N,e_{m+2}-e_m\}.
 \tag{6}
$$
空和为零。若 $k\ge2$，则
$$
 c_{p,N}(k)\le e_{k-2}+e_{k-1}-e_0-e_1
                         =e_{k-2}+e_{k-1}.
 \tag{7}
$$
这是目标算子的全部核成本；没有乘任何原源列数。

## 3. 两个实际交集与单步恒等式

对 $D\ge2$，原单项式给无需除法的整分解
$$
 E_D=K_D\oplus A^2E_{D-2},
$$
$$
 K_D=\langle C^b:0\le b\le D\rangle_O
       \oplus\langle AC^b:0\le b\le D-1\rangle_O,
 \qquad \lambda_D=2D+1.
 \tag{8}
$$
记它在当前目标中的实际像为
$$
 \mathscr K_{D,k,N}=\operatorname{im}(K_D\to\mathcal V_k).
$$
其第 $j<\min(k,\lambda_D)$ 个坐标准确为
$p^{e_j}O/p^NO$，其余为零，因而
$$
 \operatorname{length}\mathscr K_{D,k,N}
             =\sum_{j<\min(k,\lambda_D)}(N-e_j)_+.
 \tag{9}
$$

现在所有对象都由同一个原矩阵确定。置
$$
 I_{\rm old}=I_{D-2,k^-,N},\qquad
 Y_{D,k,N}=\Sigma_k I_{\rm old},
$$
以及两个非负整数
$$
 \ell_{D,k,N}
   =\operatorname{length}(I_{\rm old}\cap\ker\Sigma_k),
 \qquad
 \iota_{D,k,N}
   =\operatorname{length}(\mathscr K_{D,k,N}\cap Y_{D,k,N}).
 \tag{10}
$$
第一交集位于旧目标 $\mathcal V_{k^-}$，第二交集位于当前目标
$\mathcal V_k$。它们不是自由选择的新列，也不是在两个不同 $Q$ 上分别满足的条件。

由 (6)，
$$
                       0\le\ell_{D,k,N}\le c_{p,N}(k).        \tag{11}
$$
从 (8) 得
$$
                         I_{D,k,N}=\mathscr K_{D,k,N}+Y_{D,k,N}.
 \tag{12}
$$
限制 (5) 到 $I_{\rm old}$ 的核正是 (10) 第一项，所以
$$
 \operatorname{length}Y_{D,k,N}
       =L_N(D-2,k^-)-\ell_{D,k,N}.
$$
再对 (12) 使用有限模的和与交长度公式，得到本篇主恒等式
$$
 \boxed{\quad
 L_N(D,k)
  =\sum_{j<\min(k,\lambda_D)}(N-e_j)_+
     +L_N(D-2,k^-)-\ell_{D,k,N}-\iota_{D,k,N}.
 \quad}                                                       \tag{13}
$$

为包括尚未观察全部低行的短前缀，定义准确低核缺额
$$
 \tau^*_{D,k,N}
   =N(\lambda_D-k)_+
         +\sum_{j<\min(k,\lambda_D)}\min(N,e_j).
 \tag{14}
$$
用 $m_D-m_{D-2}=\lambda_D$ 改写 (13)，即
$$
 \boxed{\quad
 B_N(D,k)=\tau^*_{D,k,N}
             +B_N(D-2,k^-)+\ell_{D,k,N}+\iota_{D,k,N}.
 \quad}                                                       \tag{15}
$$
若 $k\ge2D+1$，第一项就是 R216 的实际低 torsion 长度
$$
                       \tau_{D,N}=\sum_{j=0}^{2D}\min(N,e_j).
 \tag{16}
$$
若 $k<2D+1$，(14) 中的 $N(2D+1-k)$ 是未观测的低源核，不能把它并入已取得的像收益。

式 (13)–(15) 对任意 $D\ge2$、任意 $k\ge0$ 及全部 $N\ge1$ 成立。没有假定非整低块可消元，也没有使用 $D<p$ 或 $\partial_A^2$ 的除法截面。

## 4. 满秩沿原 A² 向下传递

假设当前 $J_{D,<k}$ 有满列有理秩。若
$Q\in E_{D-2}\otimes\mathbf Q_p$ 的全部旧行 $<k-2$ 为零，则
$$
                    \operatorname{ord}_w(A^2Q)\ge k,
$$
因为 $A=w+\cdots$。原满秩推出 $A^2Q=0$，进而 $Q=0$。
所以 $J_{D-2,<k-2}$ 也满列秩。

反复令
$$
 d_t=D-2t,\qquad k_t=k-2t
$$
可见每个旧前缀都满列秩，直到 $d_t=0$ 或 $1$。每步均已观察其全部低核行，所以 (15) 的第一项始终是 (16)，没有源核虚增。

终端源也明确。对 $D=0$，只要 $k\ge1$ 就有 $B_N(0,k)=0$。
对 $D=1$、$k\ge3$，源为 $1,A,C$，故
$$
                         B_N(1,k)=\min(N,e_2).               \tag{17}
$$
在 $p\ge19$ 时它为零；$p=7$ 时 $e_2=1$，所以该固定小素数终端也被准确保留。

因此对满秩当前前缀，有完整正项分解
$$
 \boxed{\quad
 B_N(D,k)
  =B_N(d_{\rm end},k_{\rm end})
      +\sum_{\substack{t\ge0\\d_t\ge2}}
          \bigl(\tau_{d_t,N}
                +\ell_{d_t,k_t,N}
                +\iota_{d_t,k_t,N}\bigr).
 \quad}                                                       \tag{18}
$$
左边现在是同一个原连续矩阵的全部 truncated Smith 总和。
交集 $\iota$ 恰保留 R216 所警告的低 $F$ 经 $M^2$ 向高尾的全部耦合；它没有被置零后再作形式递归。

对固定 $D,k,p$，还可取足够大的 $N$。所有相关原矩阵都满列秩，
其有限像长度最终等于“源秩乘 $N$ 减完整 Smith 总和”。
$\mathscr K$、$Y$、原完整像的秩相加关系由 (8) 与原满秩保证。
故 (10) 的两个交集长度最终稳定，(18) 给对应的完整 Smith 恒等式。
这里的 $\iota_\infty$ 是模 $p^N$ 的同余交集的稳定长度；
原特征零函数空间中的 $K_D$ 与 $A^2E_{D-2}$ 仍是直和。

### 4.1. 每个精度增量的准确生成元计数

对本节固定的整矩阵 $Z$，令
$$
 \rho_t(Z)=\#\{\text{非零 Smith 指数 }s_i(Z)\le t\}.
$$
它也是 $Z$ 模 $p^{t+1}$ 的实际像所需的最少 $O$ 生成元数。R198 给
$$
                   L_{N+1}(Z)-L_N(Z)=\rho_N(Z).
$$
把 $\mathscr K,Y,J$ 理解为同一固定原矩阵在相应源块上的整映射，(10)、(13) 准确给
$$
 \boxed{\begin{aligned}
 \iota_{D,k,N+1}-\iota_{D,k,N}
    &=\rho_N(\mathscr K)+\rho_N(Y)-\rho_N(J)\ge0,\\
 \ell_{D,k,N+1}-\ell_{D,k,N}
    &=\rho_N(J_{\rm old})-\rho_N(Y)\ge0.
 \end{aligned}}                                               \tag{18a}
$$
这里所有 $\rho_N$ 都在精度 $p^{N+1}$ 上取最少生成元数。

非负性的证明不需要独立源假设。$J$ 的有限像是 $\mathscr K$ 与 $Y$ 两个有限像之和，合并它们的任一最小生成集即可生成原联合像；故
$\rho_N(J)\le\rho_N(\mathscr K)+\rho_N(Y)$。而 $\Sigma$ 在旧像到 $Y$ 之间给满射，所以 $\rho_N(Y)\le\rho_N(J_{\rm old})$。

因此待证的深度增长也可等价地计算为
$$
 \iota_{D,k,N}
   =\sum_{t=0}^{N-1}
        \{\rho_t(\mathscr K)+\rho_t(Y)-\rho_t(J)\}.
 \tag{18b}
$$
每项都记录同一原目标中联合像相对于两块像的生成元数减少，不能把两块各自置核后相加。

(18a) 只证明交集的**长度单调**，不表示模 $p^N$ 交集中的每个元素都能提升为下一精度交集元素。也只有在上面已证明满秩向下传递的情形，才保证整个交集族最终稳定；秩不足的 $\iota_{D,k,N}$ 可以含随 $N$ 线性增长的原源重叠，仍不能作为真实 jet 收益。

## 5. 到真实 jump 的合法收益方向

令 $0=k_1<\cdots<k_{m_D}=K_D^{\rm jump}$ 为原真正的有理秩跳阶，取
$k=K_D^{\rm jump}+1$。R215 的完整目标变换下三角且对角为单位，保持整个前缀旗标和这些跳阶。这里不将带有冗余行的连续 Smith 当作 jump Smith。

先通过已经证明的完整目标整同构返回原 $w$ 目标，再投影到原真实 jump 行，得到有限像的满射
$$
 I_{D,k,N}\twoheadrightarrow I^{\rm jump}_{D,N}.
$$
这个论证不要求“选取 jump 行”与整下三角变换交换，也不假设两个被抽出的 jump 子矩阵逐个 Smith 等价。准确得到
$$
 L_N(J_p^{\rm jump})\le L_N(D,k),
 \qquad
 \boxed{\quad
 B_N(J_p^{\rm jump})\ge B_N(D,k).
 \quad}                                                       \tag{19}
$$
于是 (18) 中每个已证明的交集下界，均能作为原真实 jet 的合法收益下界。允许这个不等式严格；不能用等号删除未支付的冗余行投影。

由 R198 的原范数恒等式进一步得到
$$
 \begin{aligned}
 \sum_i\log\|\varphi_D^{k_i}\|_p
 &=\left(\sum_i e_{p,k_i}
             -\sum_i s_i(J_p^{\rm jump})\right)\log p\\
 &\le\left(\sum_i e_{p,k_i}
             -\sum_{d_t\ge2}\iota_{d_t,k_t,N}\right)\log p.
 \end{aligned}                                               \tag{20}
$$
为显示关键新对象，最后一行只保留了 (18) 中的交集正项；其余非负项可以同时加入。整个推导始终使用原整源系数范数，没有换成非整 Schur 源上的范数。

## 6. 全素数预算中哪些项已经是次阶

R191 给
$$
                         K_D^{\rm jump}\le(1+o(1))D^2.
$$
取上节的完整前缀 $k=K_D^{\rm jump}+1$，并先在有正分母成本的支持
$$
                  \mathcal P_D=\{p\equiv3\pmod4:
                         7\le p\le4K_D^{\rm jump}-1,\ p\ne11\}
 \tag{21}
$$
中记账。

R217 的低 torsion 估计给
$$
 \sum_{p\in\mathcal P_D}\sum_{d_t\ge2}
             \tau_{d_t,N}\log p
                =O\!\left(D^3\min(N,\log D)\right).
 \tag{22}
$$
现在这份和确实来自 (18) 的实际递推，不再只是形式可支付的总上界。

由 (7)、R173/R215 的行权求和界，
$$
 \sum_{p\in\mathcal P_D}\ell_{d_t,k_t,N}\log p
 \le\sum_p(e_{p,k_t-2}+e_{p,k_t-1})\log p
                         =O(k_t\log(k_t+2)).
$$
全部步骤相加，得到
$$
 \sum_{p\in\mathcal P_D}\sum_{d_t\ge2}
             \ell_{d_t,k_t,N}\log p
                           =O(D^3\log D),                   \tag{23}
$$
常数不依赖 $N$。本递推使用完整旧目标后乘 $A^2$，没有额外删掉两条未计费的目标行；短化恰是原函数阶数增加二所要求的 $k\mapsto k-2$。

所以这条连续像递推若要提供 $D^4\log D$ 级的主项，必须控制实际量
$$
 \boxed{\quad
 \mathcal I_{D,N}
  =\sum_{p\in\mathcal P_D}
       \sum_{d_t\ge2}\iota_{d_t,k_t,N}\log p.
 \quad}                                                       \tag{24}
$$
该表述仅针对本递推。它不排除 (19) 的冗余行投影另有主项，也不排除 (21) 之外的原分子素数提供额外负范数贡献。

从 (18) 的非负性与 $B_N(D,k)\le Nm_D$，还准确有
$$
                    \mathcal I_{D,N}=O(ND^4).                \tag{25}
$$
这里每个素数上先合并了全部次数步骤，不把每步的粗上界重复当成独立源。固定 $N$ 仍不能让 (24) 改变严格预算的对数主项。

## 7. 一个完全具体的充分预算接口

记
$$
                              S_D=\sum_i k_i=\Theta(D^4).
$$
R217 给原无条件权包络
$$
              \sum_p\sum_i e_{p,k_i}\log p
                       =4S_D\log D+O(D^4),
$$
以及原复侧累计上界
$$
                  -2S_D\log D+O(D^4).
$$
因此，若假设两条原完整中央导数对所有充分大惰性素数均为零，并能在此假设下对某个精度
$N=N(D)$ 和固定 $\varepsilon>0$ 证明
$$
 \boxed{\qquad
                \mathcal I_{D,N(D)}
                       \ge(2+\varepsilon)S_D\log D
                \quad\text{对所有充分大的 }D,
 \qquad}                                                      \tag{26}
$$
则 (20) 与原乘积公式直接矛盾。固定有限坏位的总成本是 $O(D^4)$，由 (4) 的 $D^4\log D$ 规模吸收；普通位的原真实成本非正。也可在 (26) 中加入已经证明的 jump 投影收益或其他原像收益，但不得重复计数。

式 (26) 是一个准确的原矩阵交集条件，**尚未证明**。它比“全部 high tails 应有收益”具体：每个 $\iota$ 都是同一模 $p^N$ 目标中，原 $K_d$ 像与原 $A^2E_{d-2}$ 像的交集长度；全部目标权、输入行、次数及源范数已经固定。

由 (25)，要仅靠 (24) 达到 (26)，仍需要 $N(D)\not=o(\log D)$，或直接控制交集的稳定完整长度。达到这个精度量级不保证 (26)；当前仍缺原中央条件对这些实际同余交集的统一深度下界。

依赖：[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R191](R191-first-band-source-divisibility-and-global-multiplicity.md)、
[R198](R198-joint-image-saturation-and-complete-prefix-smith.md)、
[R214](R214-quadratic-pair-tail-recursion-and-deleted-c-image.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R216](R216-all-degree-nonunit-low-kernel-and-true-finite-quotient.md)、
[R217](R217-fixed-precision-budget-and-true-jump-scale.md)。
