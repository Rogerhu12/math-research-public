# R236 附录：真实核图的准仿射根、单向量首flip检验与非紧边界型

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：已证明的同一真实核图后继。只在[自然核图稿](R236-appendix-first-flip-natural-graph-and-actual-boundary-form.md)的实际图域及闭像缺陷上工作，不选新的 gauge，不换正常态。它给指定 first-flip 的一个单向量等价检验，并排除有限秩或紧的非零边界实现；没有证明这个边界型必非零，也没有证明原缺陷为零。

## 1. 固定原核、实际度量及新的精确关系

沿用自然核图稿的 k、a、S、Z、R、t、Q=Q_max，以及
$$
\mathscr D=\operatorname{Dom}Q\cap\ker(R^2-4a^2tS^2),
\qquad
\|f\|_Q^2=\|f\|^2+\|Qf\|^2,
$$
$$
\mathcal U f=(-Qf,f),\qquad
\mathscr D_0=\overline{S\mathscr D}^{\|\cdot\|_Q},\qquad
\mathscr E=\mathscr D/\mathscr D_0.
$$
U 是到同一个原核 M=ker T_N 的等距映射；E 是到 M/closure(SM) 的等距 Hilbert 商。这里只剥离了不参与的有限前头；加回该前头后所有论断仍是同一原物理表示的有限放大。

实际等式 Q^2=t=eta_k N_(k+1) 及全部尾算子的原 C_tail 对称性给
$$
\boxed{\mathfrak b(Qf,g)=-\mathfrak b(f,Qg),\qquad
\mathfrak b(tf,g)=\mathfrak b(f,tg).}
\tag{1.1}
$$
第一式逐项为
$$
\begin{aligned}
\mathfrak b(Qf,g)
&=B_{\rm tail}(tf,g)-B_{\rm tail}(Qf,Qg),\\
-\mathfrak b(f,Qg)
&=-B_{\rm tail}(Qf,Qg)+B_{\rm tail}(f,tg),
\end{aligned}
$$
两式相等，因为 t 对原 B_tail 对称。没有把 C_tail 限制到 D。

对任何真实尾完整交换子 V，有
$$
\mathfrak b(Vf,g)=\mathfrak b(f,Vg).
\tag{1.2}
$$
因为 V 与 Q 在真实图域上交换，并且在环境尾空间对 B_tail 对称。
S D 包含于 Dom Q_min，故 b 在 D_0 上为零；(1.1)–(1.2) 下降到 E。
Q 保持 D_0，且在 D 和 E 上都是范数不超过 1 的真实图算子。

## 2. 同一个图缺陷上的全部归一幂与准仿射性

令
$$
c_{k,r}=\prod_{i=0}^{r-1}\eta_{k+i}^{2^{r-1-i}},\qquad r\ge1.
$$
逐次使用原 carry，得到准确关系
$$
\boxed{Q^{2^r}=c_{k,r}N_{k+r}.}
\tag{2.1}
$$
这里 N_(k+r) 表示在 D 或 E 上的原尾算子作用；这些作用都由同一个实际 M 的限制或半不变商获得，范数不超过 1，且
$$
N_{k+r}\longrightarrow\tfrac12I\quad\text{WOT},\qquad
\|N_{k+r}^2\|\le\eta_{k+r}\longrightarrow0.
\tag{2.2}
$$
正常性来自固定物理表示的限制及固定正交压缩，未由逐层改变的商自动推断。

由 (2.1)–(2.2)，Q 在 D 上及在 E 上都单射且像稠密。若 Qf=0，则所有 N_(k+r)f=0，弱极限给 f=0；而所有 N_(k+r)f 都在 Ran Q 中，弱极限给 f/2 属于 Ran Q 的闭包。

Q 也拟幂零。由 (2.1) 及原 u_j=-log eta_j，有
$$
\|Q^{2^r}\|^{1/2^r}
\le \exp\!\left[-\sum_{i=0}^{r-1}2^{-1-i}u_{k+i}\right]
\longrightarrow0.
\tag{2.3}
$$
所以若 E 非零，它必无限维。这一结论用的是同一个实际图商，不是假设一个一般 Volterra 模型代替原算子。

式 (2.1) 确实把所有实际 N_j 写成 Q 的归一幂。然而把 S 或 Z 写成这些幂得到的标量形式级数通常半径为零：c_(k,r)^(-1) 按四次幂尺度增长，而原 a_j 只有多项式衰减。尽管原算子级数按范数绝对收敛，不能据此把形式最低幂因子当成一个可逆解析芽。

## 3. 指定 first-flip 的单向量等价判据

定义
$$
\mathfrak q(f,g)=\mathfrak b(f,Qg).
$$
由 b 交错及 (1.1)，q 是对称双线性型，且
$$
\boxed{\mathfrak q(f,f)
=B_{\rm tail}(Qf,Qf)-B_{\rm tail}(f,tf).}
\tag{3.1}
$$
Q 在 D 上像稠密，所以
$$
\boxed{
\mathfrak b\not\equiv0
\quad\Longleftrightarrow\quad
\mathfrak q\not\equiv0
\quad\Longleftrightarrow\quad
\exists f\in\mathscr D:\ 
B_{\rm tail}(Qf,Qf)\ne B_{\rm tail}(f,tf).
}
\tag{3.2}
$$
最后一步是复对称双线性型的极化，不是正性的推断。完全相同的等价在 E 上成立。

令 J=diag(1,-1) 为同一个实际首位翻转。因为 N_k U f=-UQf，自然核图稿的配对等式给
$$
\boxed{
B_2(\mathcal U f,J N_k\mathcal U f)
=-\mathfrak q(f,f).
}
\tag{3.3}
$$
所以指定 first-flip 的非零双向量配对，等价于存在原核中的一个向量 w，使 B_2(w,J N_k w) 非零。这里第二个向量使用原真实右算子 N_k w，而不是在核外选一个未付向量。

一个充分条件是
$$
|B_{\rm tail}(Qf,Qf)|>\eta_k\|f\|^2,
\tag{3.4}
$$
因为 |B_tail(f,tf)| 不超过 eta_k ||f||^2。本文没有证明实际 D 必有满足 (3.4) 的向量；C_tail 不必保持 D，故不能把左侧改写成 ||Qf||^2。

还需区分尾循环与完整首位循环：对任意尾完整交换子 V、W，
$$
\mathfrak b(Vf,Wf)=\mathfrak b(f,VWf)=0.
\tag{3.5}
$$
第一式用 (1.2) 及交换性；第二式因为 VW 对 b 对称而 b 交错。因此一个向量的尾右循环子空间总是 b 全等向。式 (3.3) 恰加入不能从尾循环免费取得的首位 Q 方向；仅有一个 rank-one 正常见证，并不支付该方向的非零配对。

## 4. 非零实际边界型不能是紧型

以下结论可以用于 D，也可以用于 E，所有范数均为相应真实图或商范数。令 X 是二者之一，b 为其上的实际下降型，并记
$$
L_b:X\longrightarrow X^*,\qquad (L_bf)(g)=\mathfrak b(f,g).
$$
这是复线性有界算子；X^* 取连续复线性泛函。没有在 X 上引入一个虚构的 C 共轭。由 (1.2)，
$$
L_bN_j=N_j' L_b,
\tag{4.1}
$$
其中 N_j' 是 Banach 转置。

若 L:X→X^* 紧，则对每个固定 f，(2.2) 给
$$
LN_jf\longrightarrow\tfrac12Lf\quad\text{范数}.
$$
再对固定 g 配对，得到
$$
N_j' L N_j\longrightarrow\tfrac14L\quad\text{WOT}.
\tag{4.2}
$$
另一方面，(4.1) 和真实 carry 给
$$
N_j' L_bN_j=L_bN_j^2\longrightarrow0\quad\text{算子范数}.
\tag{4.3}
$$
写 E=L_b-L，由 ||N_j||≤1，(4.2)–(4.3) 迫
$$
\tfrac14\|L\|\le\|E\|.
$$
故对每一个紧 L，
$$
\|L_b\|\le\|L\|+\|E\|\le5\|E\|.
$$
于是
$$
\boxed{\|L_b\|_{\rm ess}\ge\tfrac15\|L_b\|.}
\tag{4.4}
$$
特别，若实际 first-flip 边界型非零，则它不紧、非有限秩，也不属于任何 Schatten 类。这里排除的是整个边界型的紧实现，不是排除从其一个非零配对提取的向量态；一个 rank-one 正密度与非紧全局边界算子是不同对象。

## 5. 对现有全等向工具的准确范围审计

[固定阶双导子全等向稿](R236-appendix-fixed-order-double-commutators-and-generalized-kernel-isotropy.md)的假设是普通 Bell 行，幅度重排满足固定正 alpha 的伸缩指数上下界。它没有覆盖这里的多项式慢行，也没有给本稿 F=(S^2+Z)^2-4a^2tS^2 的全部广义核配对。

若未来能在这个真实 F 上证明 B_tail(ker F,ker F)=0，那么 f、Qf 均属 ker F 会立刻迫 b|D=0；那将排除本稿指定 first-flip 分支，不是提供它所需的非零配对。当前不能把不同算子范围的全等向结论代入这一步。

现在准确剩下的是原自然核图稿 §6 的两个实际部分：核内图核心间隙，以及 D 在最大/最小商边界中的像是否全等向。上述准仿射性、全部归一幂、S=Z=0 和 (4.4) 都在同一个真实图商上成立，但不把这两个未付步骤消除。

完整尾交换子的原C对称性及交换性使用[R24 §1](R24-complex-symmetric-moments-and-escape.md)的循环复对称论证；这里始终先在原物理尾空间使用，再取真实图限制或半不变商，没有把环境共轭自动下降。
