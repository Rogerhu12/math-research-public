# 原连续尾与平衡 star 的接口：实际不可约性、外场范围及换权的完整费用

日期：2026-11-14；工作标识：789f。

## 0. 结论范围

本稿从原 graph 已发表定义出发，核清三件事：

1. 原连续尾 \(D_m\) 及其物理伴随共同生成整个局部 Boolean \(C^*\) 代数，故没有非平凡的全尾 reducing 子空间。有限全异正权有相同的有限维结论。
2. 原实际测试的祖先出生随孔层 \(q\) 上移，而其尾位标签没有已付的有限截止；原外场不统一落在一个正紧区间。
3. 有界对角换权能准确运输左、裸和普通完整右的可行集与最小费用，但 flat 费仍保完整非交换乘积。把尾位分块或把近似相等权改成相等权，需要另付这一共同 Schur / Riesz 反馈。

这些是实际模型识别和运输公式。它们不否定未知实际 \(W=M\ominus N\) 来源具有更多结构，不是原 \(N=M\) 的反例，也不把平衡 star 的完整源定理扩大到全部出生。

依赖的原接口：
[首物理头商 Gram](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)，
[固定测试最小双链](../results/R271-appendix-fixed-physical-tests-and-minimum-two-chain-local-gram.md)，
[真实测试流](2026-11-14-actual-test-flow-filtered-bare-chain-and-primitive-free-source-kernel-2220.md)，
[R286 实际祖先出生](../results/R286-fixed-source-l1-zero-mode-energy-and-uniform-all-height-tail-bounds.md)。

## 1. 原连续尾的全 \(C^*\) 代数

在有限子集 Hilbert 空间 \(\ell^2(\mathcal P_{\rm fin}(I))\) 上，
\(E_i\) 删除第 \(i\) 位，\(E_i^*\) 创建该位，\(n_i=E_i^*E_i\)。
先取任意实正权
\[
 b\in\ell^1(I),\qquad b_i^2\ne b_j^2\quad(i\ne j),\qquad
 D=\sum_i b_iE_i.
\]
原 \(b_i=(i+1)^{-2}\)、\(i>m\)，正好满足这些假设。
级数在算子范数中收敛。

**命题。** 令 \(\mathcal A=C^*(I,D,D^*)\)，则
\[
 \boxed{\mathcal A=
 \overline{\bigcup_{F\Subset I}
       \mathcal B((\mathbb C^2)^{\otimes F})\otimes I_{F^c}}^{\,\|\cdot\|}.}
                                                               \tag{1.1}
\]
尤其 \(\mathcal A'=\mathbb CI\)，所以 \(D\) 在整个尾空间上不可约
（此处不可约严格指没有非平凡同时对 \(D,D^*\) 不变的闭子空间）。

证明。不同位的算子交换，同一位有
\([E_i,E_i^*]=I-2n_i\)。故
\[
 [D,D^*]=S I-2W,\qquad
 S=\sum_i b_i^2,\quad W=\sum_i b_i^2n_i,
\]
并且
\[
 W\in\mathcal A,\qquad
 \operatorname{ad}_W^kD=(-1)^k\sum_i b_i^{2k+1}E_i.
                                                               \tag{1.2}
\]
因此对任意多项式 \(p\)，
\[
                  \sum_i b_i p(b_i^2)E_i\in\mathcal A.           \tag{1.3}
\]

固定一位 \(i_0\)。紧集
\(\{0\}\cup\{b_i^2:i\in I\}\) 的每个正点都孤立：
\(\ell^1\) 保证任意正阈以上只有有限多个 \(b_i\)，且各正点互异。
可在一个包含该紧集的实紧区间上选连续函数 \(f\)，使
\[
 f(b_{i_0}^2)=1/b_{i_0},\quad f(b_i^2)=0\ (i\ne i_0),
 \quad f(0)=0.
\]
取一致逼近 \(f\) 的实多项式 \(p_n\)。实际算子范数满足
\[
 \left\|\sum_i b_i[p_n(b_i^2)-f(b_i^2)]E_i\right\|
       \le\|b\|_1\|p_n-f\|_\infty\longrightarrow0.
\]
由 (1.3) 得 \(E_{i_0}\in\mathcal A\)，故也有 \(E_{i_0}^*,n_{i_0}\in\mathcal A\)。
这些算子生成每个有限位局部全矩阵代数；反向 \(D\) 已是其范数极限，
证明 (1.1)。

若 \(T\) 与 \(\mathcal A\) 交换，则它与所有 \(n_i\) 交换，因而在原子集基中
为对角 \(Te_J=t_Je_J\)：全部 \(n_i\) 的联合特征空间均为一维。
再与每个 \(E_i\) 交换，得到 \(t_J=t_{J\setminus\{i\}}\)，故全部
\(t_J=t_\varnothing\)。这证明共同 commutant 只有标量。

有限位情形可直接用 (1.2) 的 Vandermonde 矩阵分离每个 \(E_i\)，
于是 \(\mathcal A=\mathcal B((\mathbb C^2)^{\otimes I})\)。

### 1.1 对 star 的准确含义

平衡 star 的组模块同时约化删除和其物理伴随；其完整 MP 可以在该
reducing 模块中计算。因此，(1.1) 排除了把原全异权连续尾直接正交分解成
非平凡的这些全梯度模块。

它不排除一个特定单层压缩或某个有限短段出现特殊子空间，不排除非酉相似，
也不排除添加新的等权池以后得到另一模型。它更不排除 \(D\) 自身的非平凡
不变子空间；原 primitive 核当然仍存在。这里必须同时保 \(D,D^*\)，
因为真正 MP 逆读取完整物理伴随。

有限位前缀张量外尾真空是 \(D\)-不变的，却不是 \(D^*\)-不变的；
外尾创建项不为零。故将这种前缀当作完整 MP 的 reducing 子块也不合法。

## 2. 原实际测试没有统一正紧外场

按照 R286 §7 和真实测试流 (2.2)，固定原 \(m,d=2^m\) 后，
\[
 t_q\in\bigoplus_{i=0}^{d-3}e_i
       (E_{d-i-1,q}\ominus E_{1,q}),\quad
 E_{h,p}=\ker D^h\cap\mathcal H_p.
\]
真实正交塔分解给第 \(i\) 个头的全部允许祖先为
\[
 1\le h\le d-i-2,\qquad
                       s=q-h\in[q-d+i+2,q-1].            \tag{2.1}
\]
这限制的是出生与高度，不限制尾位标签。特别不能把固定起始测试
\(f\in\mathscr T_n\) 解释成经过实际受限逆之后仍是固定有限尾支持。

为避免原文尾起点的 \(m\) 与 \(m+1\) 约定，只写从整数 \(x\) 开始的重标
\[
                         b_j=j^{-2},\quad j\ge x.
\]
相应平方权 \(z_j=j^{-4}\)。任何共同标量归一都不能改变
\[
 \frac{\max_{x\le j<x+N}z_j}{\min_{x\le j<x+N}z_j}
                     =\left(\frac{x+N-1}{x}\right)^4.    \tag{2.2}
\]
无限尾的外场下确界本来就是零。合法完整 primitive 高度 \(h\) 的有限
Boolean 前缀需要 \(N\ge2s+h\)；对 (2.1) 的移动出生，若使用原起点前缀，
\(N\) 至少是 \(q\) 的量级，而 \(x\) 只是原 \(m\) 的量级。
于是原大窗 \(q\gg d\) 中 (2.2) 没有统一上界。

这里没有断言未知实际 \(t_q\) 必须把质量放在每个极端标签上。准确结论是：
已付源定义不包含一个可将其限制到统一正紧外场的标签局部化定理。
任何这样的改进都须对同一个真实 \(t_q,e_q\) 及完整逆另外证明。

可选远处的窄物理位块使块内权比有界，但那只是选择了一个不同的有限支撑
环境；(1.1) 及 §4 说明为何其外尾与完整 Schur 不能免费删除。

## 3. 把原权改成等权时，完整层对角运输的准确代价

取有限块 \(I=\{x,\ldots,x+M-1\}\)，原 \(b_j=j^{-2}\)，改为常数权
\(\bar b_j=\beta>0\)。令
\[
 R_r e_J=\left(\prod_{j\in J}\frac{b_j}{\beta}\right)e_J,
                      \qquad |J|=r.
\]
有准确交织
\[
                    D_b R_{r+1}^{-1}=R_r^{-1}D_{\bar b}.
                                                               \tag{3.1}
\]
所以所有纯核旗代数地对应；这不把非酉 \(R_r\) 变成等距。

在整个物理 \(r\) 层，最大和最小对角分别取最早、最晚的 \(r\) 个标签，
因此条件数准确为
\[
 \boxed{\operatorname{cond}R_r=
 \left[
   \frac{\prod_{j=0}^{r-1}(x+M-r+j)}
        {\prod_{j=0}^{r-1}(x+j)}
 \right]^2.}                                             \tag{3.2}
\]
该式与共同等权值 \(\beta\) 无关。
对 \(M=2r\)，
\[
 \boxed{\frac{2r^2}{x+2r-1}
          \le\log\operatorname{cond}R_r
          \le\frac{2r^2}{x}.}                             \tag{3.3}
\]
证明只用
\[
 \log\operatorname{cond}R_r
       =2\sum_{j=0}^{r-1}\log\left(1+\frac r{x+j}\right)
\]
以及 \(t/(1+t)\le\log(1+t)\le t\)。

所以即使每一个单个位的改权比有固定界，完整半密度层的
环境对角条件数仍可为 \(\exp(cr)\)。在 \(x\gg r\) 的窄远块中，
其对数量级改为 \(r^2/x\)。

(3.2)–(3.3) 只计算“先用完整物理层对角条件数支付换权”这条路线的成本。
极值子集基未必属于相关 primitive 或实际 \(W\) 源，故本文没有把这些数
冒称为受限 primitive / graph Schur 条件数的下界。实际特殊源若能改善
这个代价，仍是合法的未闭方向。

## 4. 同一个源上的左、裸及普通右费用运输

以下给换权时真正可直接使用的结论。设 \(b,c\) 两组正权只在一个有限位集
上不同，或所需各有限孔层上的对角及逆均有界。定义
\[
 R_p e_J=\prod_{j\in J}(b_j/c_j)e_J,\qquad
 D_b=R_{p-1}^{-1}D_cR_p\quad\hbox{于 }\mathcal H_p.        \tag{4.1}
\]
头算子 \(A\) 不变，\(R_p\) 在头上作用单位。于是
\[
 R_{p-h}D_b^h=D_c^hR_p,\qquad
                  R_pE_{h,p}(b)=E_{h,p}(c).              \tag{4.2}
\]
令源 \(x=R_qr\)。整个左可行向量和完整右链逐孔乘 \(R_p\)，准确送到
同源 \(x\) 的另一权模型；所有头旗、内部方程和最右封口均保留。

裸链使用高出生商。这里 \(R_p\) 一般不保持高出生空间的物理正交补，
必须把它作为商空间之间的诱导映射，再各取原物理最小代表。
若在相关右孔层
\[
             \ell_R I\preceq R_p^*R_p\preceq u_RI,
\]
则两个商范数也满足相同的上下界：对全部高出生代表取下确界即可。
不能直接把原裸最小代表乘 \(R_p\) 后仍称为新裸最小代表。

同理在左孔层取常数 \(\ell_L,u_L\)。原
\[
 \mu_b(r)^2=\langle L_br,r\rangle,\quad
 \alpha_b(r)^2=\langle B_br,r\rangle,\quad
 \lambda_b(r)^2=\langle G_b^{-1}r,r\rangle
\]
于是满足
\[
 u_L^{-1}\mu_c(x)^2\le\mu_b(r)^2
                     \le\ell_L^{-1}\mu_c(x)^2,
\]
\[
 u_R^{-1}\alpha_c(x)^2\le\alpha_b(r)^2
                     \le\ell_R^{-1}\alpha_c(x)^2,
\]
\[
 u_R^{-1}\lambda_c(x)^2\le\lambda_b(r)^2
                     \le\ell_R^{-1}\lambda_c(x)^2.       \tag{4.3}
\]
它们来自全部可行集的双向运输和真实最小化；没有使用逐矩阵 entry 比较。

## 5. flat、负图与固定测试仍须共同运输

在同一个新源 \(x=R_qr\) 上定义
\[
 \widetilde L=R_q^{-*}L_bR_q^{-1},\quad
 \widetilde B=R_q^{-*}B_bR_q^{-1},\quad
 \widetilde G=R_qG_bR_q^* .
\]
则准确有
\[
 \boxed{\lambda_{{\rm flat},b}(r)^2
    =\langle\widetilde L\widetilde G\widetilde Lx,x\rangle,\qquad
 \Xi_b(r)^2
    =\langle(\widetilde B+\widetilde L\widetilde G\widetilde L)x,x\rangle.}
                                                               \tag{5.1}
\]
(4.3) 仅给
\[
 u_L^{-1}L_c\preceq\widetilde L\preceq\ell_L^{-1}L_c,\quad
 u_R^{-1}B_c\preceq\widetilde B\preceq\ell_R^{-1}B_c,
\]
\[
               \ell_R G_c\preceq\widetilde G\preceq u_RG_c.
                                                               \tag{5.2}
\]
这些式子不能通过交换乘法变成
\(\widetilde L\widetilde G\widetilde L\) 与 \(L_cG_cL_c\) 的同常数比较。
例如写
\[
 X=L_c^{-1/2}\widetilde L L_c^{-1/2},
\]
则还需要控制真实非自伴运输
\[
 (G_c^{1/2}L_c^{1/2})X(G_c^{1/2}L_c^{1/2})^{-1},
\]
而不仅是 \(X\) 的正谱上下界。本文没有把这个未付量删掉。

原完整前缀负图同样运输为
\[
 r\perp_{L_b+B_b}X_K(b)
 \quad\Longleftrightarrow\quad
 x\perp_{\widetilde L+\widetilde B}X_K(c),                 \tag{5.3}
\]
因为 (4.2) 保其整个头/尾源旗。它一般不是
\(x\perp_{L_c+B_c}X_K(c)\)。后续 \(M_2\) 正交消元和固定测试行也必须使用
(5.1) 的同一个度量。

原所需局部量仍是
\[
 \mathbb K_{n,h}=\mathcal A_n^*
       (\mathbb R_{\mathfrak D}-\mathbb R_{\mathfrak Z_h})
                                  \mathcal A_n,\qquad
 \mathcal A_n=-D_{UK}D_{KK}^{-1}\iota_n.
\]
统一 \(\|\mathbb K_{n,h}\|=O_n(K_{\rm eff})\) 会支付固定测试，
但本文的分块换权身份本身没有给这个界。特别原
\(\Gamma=\mathcal T^*\mathcal T=I+S^*S\) 是接合 graph Gram，
不是平衡 star 所处理的同一个 primitive 三高度相位矩阵。

## 6. 可继续的准确位置

平衡 star 的有界外场全源结论可以作为一种明确模型预算。
把它接到原慢尾，仍须给以下实质新对象中的一个：

- 保同一实际测试源的尾标签局部化，并付出真正两费余商中的误差；
- 对有限位块的非酉换权，在 (5.1)–(5.3) 中付完整 Riesz / Schur 反馈；
- 直接处理原全异尾的完整高出生源与普通右费。

仅有块内权比、单高度最小逆比较或一个新增等权池，均没有完成这一接续。
