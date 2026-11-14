# R13：全部归一化幂的二进位分解与弱聚点分类

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94。

**状态：已证明的中间结论。** 本文把 [R12](R12-normalized-powers-and-compact-commutant.md) 的 dyadic 幂分析推广到所有整数幂，精确分类归一化幂的弱聚点及逐向量强收敛子列。没有由此证明普通不变子空间存在或不存在，也不主张文献新颖性。

## 1. 设定与主结论

令 $X=\mathbb Z_2$，$\mu$ 为 Haar 概率测度，$H=L^2(X,\mu)$。沿用 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 的算子

$$
(Af)(y)=a_{v_2(y)}f(y-1),\qquad w(0)=0,
$$

其中

$$
a_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
\tag{1.1}
$$

$a_j>0$ 严格递减。记

$$
\eta_j=\frac{a_{j+1}}{a_j},\qquad
\varepsilon_m=\sum_{j=m}^{\infty}\eta_j.
\tag{1.2}
$$

由 $L_{j+1}-L_j=1400\,16^j-630\,8^j+300\,2^j\ge770\,16^j$，级数收敛且 $\varepsilon_m\to0$。

对 $n\ge0$ 定义

$$
W_0=1,\quad W_n=\prod_{l=1}^{n}a_{v_2(l)},\qquad
F_n=A^n/W_n.
\tag{1.3}
$$

令 $S(n)$ 为 $n$ 的二进展开中等于 $1$ 的位的集合，$h(n)=|S(n)|$。约定 $S(0)=\varnothing$。

**定理 1.1。**

1. 对所有 $n\ge0$，$\|A^n\|=W_n$。若 $S(r)\cap S(s)=\varnothing$，则
   $$W_{r+s}=W_rW_s,\qquad F_{r+s}=F_rF_s.$$
2. 若整数序列满足 $h(n_l)\to\infty$，则 $F_{n_l}\to0$ 于强算子拓扑。
3. 设 $n_l\to\infty$ 且 $h(n_l)$ 有界。存在子列、固定整数 $r\ge0$、固定整数 $q\ge1$ 及 $s_l$，使
   $$n_l=r+s_l,\quad h(s_l)=q,\quad \min S(s_l)\to\infty,$$
   并且
   $$F_{n_l}\xrightarrow{\mathrm{WOT}}2^{-q}F_r,$$
   $$\|F_{n_l}f\|^2\longrightarrow2^{-q}\|F_rf\|^2,$$
   $$\|(F_{n_l}-2^{-q}F_r)f\|^2
   \longrightarrow(2^{-q}-2^{-2q})\|F_rf\|^2\qquad(f\in H).$$
4. 沿着 $n\to\infty$，归一化幂的全部 WOT 聚点恰为
   $$\{0\}\ \cup\ \{2^{-q}F_r:r\ge0,\ q\ge1\}.$$
5. 对任意固定 $f\ne0$ 和任意 $n_l\to\infty$，向量序列 $F_{n_l}f$ 在范数下收敛，当且仅当 $h(n_l)\to\infty$；此时极限必为零。

第 3 项是在提取子列后的结构陈述，未声称任意有界二进位数序列本身必有唯一的非零弱极限。

## 2. 精确幂范数及无进位乘法

写 $\Delta_j=L_j-L_{j-1}>0$（$j\ge1$）。对每个整数 $n\ge1$，计数 $1,\ldots,n$ 中的 $2^j$ 倍数，得到

$$
-\log W_n=nL_0+\sum_{j\ge1}\left\lfloor\frac n{2^j}\right\rfloor\Delta_j.
\tag{2.1}
$$

右侧只有有限个非零求和项。

另一方面，$A^n=M_{w_n}U^n$，其中 $U$ 是酉平移且

$$
w_n(y)=\prod_{l=0}^{n-1}w(y-l).
\tag{2.2}
$$

连续 $n$ 个剩余类中，每个模 $2^j$ 的指定剩余类至少出现 $\lfloor n/2^j\rfloor$ 次。因此对几乎每个 $y$，把每个 $L_{v_2(y-l)}$ 展开为 $L_0+\sum_{j\le v_2(y-l)}\Delta_j$，可得

$$
-\log w_n(y)\ge nL_0+
\sum_{j\ge1}\left\lfloor\frac n{2^j}\right\rfloor\Delta_j
=-\log W_n.
$$

在权为零的有限个点，不等式按 $w_n=0$ 仍成立。于是 $\|A^n\|=\|w_n\|_\infty\le W_n$。

取 $m$ 使 $2^m>n$。在正测度柱集 $y\equiv n\pmod{2^m}$ 上，$y,y-1,\ldots,y-n+1$ 的二进阶分别与 $n,n-1,\ldots,1$ 相同。因此 $w_n(y)=W_n$ 于该柱集，证明

$$\boxed{\|A^n\|=W_n.}\tag{2.3}$$

若 $r,s$ 的二进位支集不交，则对于每个 $j$，其低于第 $j$ 位的部分相加没有进位，从而

$$
\left\lfloor\frac{r+s}{2^j}\right\rfloor
=\left\lfloor\frac r{2^j}\right\rfloor+
\left\lfloor\frac s{2^j}\right\rfloor.
$$

代入 (2.1) 得 $W_{r+s}=W_rW_s$；再用算子幂的乘法得到 $F_{r+s}=F_rF_s$。特别地

$$
F_n=\prod_{j\in S(n)}F_{2^j},\qquad \|F_n\|=1.
\tag{2.4}
$$

## 3. 高位矩阵单位的统一近似

以 $b_j(y)\in\{0,1\}$ 表示 $y$ 的第 $j$ 位。令 $E_j$ 在第 $j$ 个二进位上作用矩阵单位 $e_{10}$，在其他位上作用恒等算子。具体地，$E_j$ 将输入的第 $j$ 位由 $0$ 改成 $1$；若输入第 $j$ 位为 $1$，则将其杀掉。

不同 $E_j$ 相互交换，$\|E_j\|=1$，且

$$E_j^*E_j=M_{\mathbf1_{\{b_j=0\}}}.$$

R12 §2 的自相似公式直接给出

$$\|F_{2^j}-E_j\|=\eta_j.\tag{3.1}$$

对有限位集 $S$ 写 $E_S=\prod_{j\in S}E_j$，空积为 $I$。按照同一顺序排列两组乘积，逐个替换因子；每个因子范数均不超过一，由伸缩求和有

$$
\left\|\prod_{j\in S}F_{2^j}-E_S\right\|
\le\sum_{j\in S}\eta_j.
\tag{3.2}
$$

这不要求 $F_{2^i}$ 与 $E_j$ 相互交换。如果 $S\subseteq\{m,m+1,\ldots\}$，则右侧至多为 $\varepsilon_m$，与 $S$ 的大小无关。

## 4. 产品参考态上的矩阵单位极限

先设 $f,g$ 只依赖低于第 $d$ 位的数字，且 $S\subseteq\{d,d+1,\ldots\}$。高位与 $f,g$ 独立，逐位计算得

$$
\langle E_Sf,g\rangle=2^{-|S|}\langle f,g\rangle,
\qquad
\|E_Sf\|^2=2^{-|S|}\|f\|^2.
\tag{4.1}
$$

柱函数在 $H$ 中稠密，且 $\|E_S\|\le1$。因此：

**引理 4.1。** 若 $|S_l|=q$ 固定且 $\min S_l\to\infty$，则

$$
E_{S_l}\xrightarrow{\mathrm{WOT}}2^{-q}I,\qquad
\|E_{S_l}f\|^2\to2^{-q}\|f\|^2\quad(f\in H).
\tag{4.2}
$$

若只假设 $|S_l|\to\infty$，则 $E_{S_l}\to0$ 于 SOT，不需要 $\min S_l\to\infty$。

**证明后一陈述。** 给定低 $d$ 位柱函数 $f_d$，将 $S_l$ 拆成低位部分和高位部分 $S_l^+\subseteq\{d,d+1,\ldots\}$。低位乘积为压缩算子并与高位乘积交换，因此

$$
\|E_{S_l}f_d\|\le\|E_{S_l^+}f_d\|
=2^{-|S_l^+|/2}\|f_d\|
\le2^{-(|S_l|-d)/2}\|f_d\|.
$$

对一般 $f$ 加上 $\|E_{S_l}(f-f_d)\|\le\|f-f_d\|$，先令 $l\to\infty$，再令 $f_d\to f$，结论成立。证毕。

## 5. 二进位数趋于无穷时的强零极限

假设 $h(n_l)\to\infty$。固定 $m$，写

$$
n_l=r_l+s_l,\quad 0\le r_l<2^m,\quad 2^m\mid s_l.
$$

这是无进位分解。由 (2.4)、(3.2) 及 $\|F_{r_l}\|=1$，对任意 $f$ 有

$$
\|F_{n_l}f\|
\le\|F_{s_l}f\|
\le\|E_{S(s_l)}f\|+\varepsilon_m\|f\|.
\tag{5.1}
$$

而 $|S(s_l)|\ge h(n_l)-m\to\infty$，所以引理 4.1 使第一项趋零。因此

$$\limsup_l\|F_{n_l}f\|\le\varepsilon_m\|f\|.$$

再令 $m\to\infty$，证明定理第 2 项。这里先固定 $m$ 再取极限，避免把随 $l$ 变化的柱函数逼近误差当作一致可控。

## 6. 有界二进位数的所有非零极限

若 $n_l\to\infty$ 且 $h(n_l)$ 有界，先取子列使 $h(n_l)=h$ 固定，再将其 $h$ 个等于一的位从小到大排列。逐次抽取子列，每个位置要么最终固定，要么趋于无穷。由于这些位置有序，最终固定的位置构成初始的一段。

这些固定位置之和给出 $r\ge0$；其余 $q$ 个位置给出 $s_l$。因为 $n_l\to\infty$，$q\ge1$。因此

$$n_l=r+s_l,\quad h(s_l)=q,\quad\min S(s_l)\to\infty.$$

由 (3.2)，

$$\|F_{s_l}-E_{S(s_l)}\|\le\varepsilon_{\min S(s_l)}\to0.$$

利用 $F_{n_l}=F_{s_l}F_r$，并把引理 4.1 应用于固定向量 $F_rf$，得到

$$F_{n_l}\xrightarrow{\mathrm{WOT}}2^{-q}F_r,\qquad
\|F_{n_l}f\|^2\to2^{-q}\|F_rf\|^2.$$

再将平方展开，弱收敛控制交叉项，便有

$$
\|F_{n_l}f-2^{-q}F_rf\|^2
\longrightarrow(2^{-q}-2^{-2q})\|F_rf\|^2.
\tag{6.1}
$$

$A$ 单射，所以 $F_rf\ne0$ 对 $f\ne0$ 成立；(6.1) 的右侧严格为正。

## 7. 聚点集合与强收敛的精确结论

若沿 $n_l\to\infty$ 存在非零 WOT 极限，而 $h(n_l)$ 无界，则可另取 $h(n_l)\to\infty$ 的子列，由 §5 其 WOT 极限为零，矛盾。因此 $h(n_l)$ 有界，再由 §6 可知原极限必须是某个 $2^{-q}F_r$。

反过来，给定 $r\ge0,q\ge1$，令

$$n_l=r+\sum_{j=0}^{q-1}2^{l+j}\qquad(2^l>r).$$

§6 证明 $F_{n_l}\to2^{-q}F_r$ 于 WOT。取 $n_l=2^l-1$，则 $h(n_l)=l$，§5 给出强零极限。这就证明定理第 4 项；WOT 在有界集上由可数稠密向量对刻画，故这些序列已足以描述聚点。

最后，假设 $f\ne0$，$n_l\to\infty$，且 $F_{n_l}f$ 强收敛。如果 $h(n_l)$ 不趋于无穷，则有二进位数一致有界的子列。§6 对其进一步抽取后给出的弱极限是 $2^{-q}F_rf$，而 (6.1) 说明到该弱极限的范数距离不趋零，矛盾。因此必须 $h(n_l)\to\infty$，并由 §5 得到强极限零。逆向也由 §5 立即成立。

## 8. 对后续路线的意义和边界

例子如下：

| 指数 | WOT 极限 | 固定向量像的范数极限 |
| --- | --- | --- |
| $2^l$ | $I/2$ | $\|f\|/\sqrt2$ |
| $2^l+2^{l+1}$ | $I/4$ | $\|f\|/2$ |
| $r+2^l$（固定 $r$） | $F_r/2$ | $\|F_rf\|/\sqrt2$ |
| $2^l-1$ | $0$，且为 SOT 极限 | $0$ |

如果 $M$ 是任意闭 $A$-不变子空间，上述全部向量等式对 $f\in M$ 仍然成立，且所有 $F_n$ 保持 $M$。因而它们也约束 $A|_M$，却不迫使 $M=0$ 或 $M=H$。

本结果排除了“更换整数幂子列即可获得非零强极限”的路线，包括所有非 dyadic 指数。它没有控制随 $n$ 改变的输入向量、不同的归一化因子或一般多项式组合；更不能将其误读为所有极小向量方法均已处理。
