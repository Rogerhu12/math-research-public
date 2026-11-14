# 一般有限 chaos 零矩的高次尾匹配与有限顶点覆盖必要条件

日期：2026-11-12。会话：Astra-ISP-0c017065，子任务 l2_moments。

**状态：本稿主必要条件已证明。** 任意非零有限 Walsh 次数配对若对实际 $A$ 全部矩消失，则两端最高阶纯尾系数中，大于某个 $e^{-c16^m}$ 阈值的超图都具有一致有界的匹配数，因此分别有一致有界大小的顶点覆盖。

证明把 R89 的完整有限头恢复推广到任意有限次数第一端，再接 R93 的 Pouzet 定量有限块创建左逆。最高尾次数项是纯尾最高阶核的创建算子，其他项至多升 $p-1$ 阶，所以有限反向递归控制完整第二端，包含所有固定低位无限行。

本条只给阈值以上超图的覆盖。一般 $p\ge2$ 时，一个顶点可连接无穷多边，故本文不把删去有限个顶点当作删去有限个系数，也不声称覆盖之外的 $\ell^2$ 或 $\ell^1$ 质量已经可控。

依赖：R84 的多位平方可和合成；R89 §2 的头 Walsh 插值；R93 的固定匹配数量及系数幂次左逆。R93 准确使用 Pouzet 已出版的集合代数横截定理，本稿只调用 R93 的已证量化形式，不将旧定理另称新发现。

## 1. 主定理

设

$$
0\ne f\in H_{\le p},\qquad 0\ne g\in H_{\le q},
\qquad p,q\ge1,
$$

且

$$
B(A^nf,g)=0\quad(n\ge0).
\tag{1.1}
$$

可以把 $p,q$ 取为两端实际最高 Walsh 次数。令 R93 的固定整数与指数为

$$
\nu=\nu_{p,q}=N_{p,q},\qquad K=K_{p,q}\ge1.
$$

其量化结论是：若纯 $p$ 阶核 $u$ 有 $\nu$ 条两两不交的非零支持边，系数模至少为 $t>0$，且 $\|u\|_2\le M$，则

$$
\|C_uv\|_2
\ge c_{p,q}M^{1-K}t^K\|v\|_2
\quad\left(v\in\bigoplus_{k=0}^qH_{=k}\right).
\tag{1.2}
$$

这里 $C_u$ 是无交叠平方零卷积创建算子；指数、匹配数量和常数只依赖 $p,q$，与坐标位置无关。

**定理 1.1。** 存在 $m_0=m_0(f,p,q)$，使对所有 $m\ge m_0$，超图

$$
\mathcal H_{f,m}
=\left\{
S\subseteq[m,\infty):
|S|=p,\,
|\widehat f(S)|>e^{-c_{p,q}'16^m}
\right\}
\tag{1.3}
$$

的匹配数至多 $\nu_{p,q}-1$。这里可取某个仅依赖次数的正数，例如在下文非优化估计下取

$$
c_{p,q}'=\frac{20}{K_{p,q}(q+1)}.
\tag{1.4}
$$

因此存在有限集 $B_{f,m}\subseteq[m,\infty)$，满足

$$
|B_{f,m}|\le p(\nu_{p,q}-1),
\tag{1.5}
$$

并且

$$
S\cap B_{f,m}=\varnothing,\quad
S\subseteq[m,\infty),\quad |S|=p
\quad\Longrightarrow\quad
|\widehat f(S)|\le e^{-c_{p,q}'16^m}.
\tag{1.6}
$$

交换两端，得到 $g$ 的相应结论，覆盖大小至多 $q(\nu_{q,p}-1)$。取两个覆盖的并，可以同时覆盖两端各自阈值以上的最高阶纯尾系数。

## 2. 全部有限头的插值测试

令

$$
N=2^m,\qquad \alpha_m=a_m^{\mathrm{op}},
$$

并令 $A_m$ 为低 $m$ 位有限链。对每个头 Walsh 向量 $\chi_K$、$K\subseteq[0,m)$，取次数小于 $N$ 的插值多项式 $p_K$，使

$$
p_K(A_m)1=\chi_K.
\tag{2.1}
$$

R89 §2 已完整证明

$$
\|p_K(A)\|,\ \|p_K(A_m)\|\le2^N,
\tag{2.2}
$$

$$
\|p_K(A)-p_K(A_m)\|
\le\Gamma_m,\qquad
\Gamma_m=\frac{N^22^N\alpha_m}{W_{N-1}}.
\tag{2.3}
$$

这些界对全部 $N$ 个头 Walsh 向量统一成立。

设 $R=p+q$。对任意有限展开

$$
h=\sum_{\substack{K\subseteq[0,m)\\
J\subseteq[m,\infty),\ |J|\le R}}
c_{K,J}\chi_K\chi_J,
\tag{2.4}
$$

定义实际多项式

$$
\mathcal P_h(A)
=\sum_{K,J}c_{K,J}(-1)^{|J|}p_K(A)T_J,
\qquad T_j=2N_j-I,
\tag{2.5}
$$

以及模型测试

$$
\widetilde{\mathcal P}_h
=\sum_{K,J}c_{K,J}(-1)^{|J|}p_K(A_m)S_J,
\qquad S_j=2E_j-I.
\tag{2.6}
$$

头和尾作用分离，故

$$
\widetilde{\mathcal P}_h1=h.
\tag{2.7}
$$

现在对每个 $K$ 和尾次数，先把所有尾系数作 R84 的平方可和合成，输入是固定的 $f\in H_{\le p}$；随后使用 (2.2)–(2.3)，最后对有限个头标签和次数作 Cauchy–Schwarz。得到

$$
\|(\mathcal P_h(A)-\widetilde{\mathcal P}_h)f\|_2
\le\varepsilon_{m,p,q}\|h\|_2\|f\|_2,
\tag{2.8}
$$

其中

$$
\varepsilon_{m,p,q}
\le C_{p,q}\sqrt N\,2^N
\left(
\frac{N^2\alpha_m}{W_{N-1}}+\eta_m
\right).
\tag{2.9}
$$

与 R89 相同，

$$
\boxed{
\log\varepsilon_{m,p,q}
\le-\frac{260}{3}16^m
+O_{p,q}(8^m+m2^m).}
\tag{2.10}
$$

本步骤没有让实际幂先作用于 $f$ 后再误用有限 chaos 合成；全部无限尾合成都先作用于原来的 $f$。

## 3. 一般有限次数向量的模型乘法

将 $f$ 按头 Walsh 系数和尾次数正交分解：

$$
f=\sum_{\substack{K\subseteq[0,m)\\|K|\le p}}
\chi_K\sum_{r=0}^{p-|K|}f_{K,r},
\tag{3.1}
$$

其中 $f_{K,r}$ 是纯尾 $r$ 阶向量，且

$$
\sum_{K,r}\|f_{K,r}\|_2^2=\|f\|_2^2.
\tag{3.2}
$$

对有限尾次数输入 $v$，定义

$$
\mathcal L_{f,m}v
=\sum_{K,r}
(-1)^r p_K(A_m)\,\mathscr S_r(f_{K,r})v.
\tag{3.3}
$$

这里 $\mathscr S_r$ 是 R84 的独立位合成。每个 $f_{K,r}$ 的尾系数可以无限，但 R84 使该合成在任意固定有限尾次数输入上连续。头和尾分离，故同一估计适用于带任意头 Hilbert 空间系数的输入：对头正交分量逐个应用标量估计再平方相加即可。

设输入尾次数至多 $q$。由 (2.2)、(3.2) 和有限个头标签的 Cauchy–Schwarz，

$$
\|\mathcal L_{f,m}v\|_2
\le
C_{p,q}2^N(m+1)^{p/2}\|f\|_2\|v\|_2.
\tag{3.4}
$$

使用了

$$
\#\{K\subseteq[0,m):|K|\le p\}
\le C_p(m+1)^p.
$$

输出尾次数至多 $p+q$，头次数不作限制。

因为 $(-1)^r\mathscr S_r(f_{K,r})1=f_{K,r}$，有

$$
\mathcal L_{f,m}1=f.
\tag{3.5}
$$

它在有限尾次数自然定义域上与每个模型测试 (2.6) 交换；无限系数先用有限和验证，再用 R84 的逐层连续性取极限。各 $p_K(A_m)$ 和 $S_j$ 都对 $B$ 对称且头尾相互交换，所以同样在该定义域上有

$$
B(\mathcal L_{f,m}u,v)=B(u,\mathcal L_{f,m}v).
\tag{3.6}
$$

因此

$$
\widetilde{\mathcal P}_hf
=\mathcal L_{f,m}h,
$$

而全部实际零矩使 $B(\mathcal P_h(A)f,g)=0$。结合 (2.8)，对 (2.4) 的全部测试 $h$ 得

$$
|B(h,\mathcal L_{f,m}g)|
\le
\varepsilon_{m,p,q}\|h\|_2\|f\|_2\|g\|_2.
$$

$\mathcal L_{f,m}g$ 的尾次数至多 $p+q$，所以这些测试在所需的完整头尾空间中稠密。于是

$$
\boxed{
\|\mathcal L_{f,m}g\|_2
\le\varepsilon_{m,p,q}\|f\|_2\|g\|_2.}
\tag{3.7}
$$

与只控制最高纯尾卷积的 R84 相比，这里恢复了整个 $g$，包括固定低位的无限行。

## 4. 最高升阶项正是纯尾最高核的创建

记

$$
u_m=f_{\varnothing,p}
=\sum_{\substack{|J|=p\\J\subseteq[m,\infty)}}
\widehat f(J)\chi_J.
\tag{4.1}
$$

这是 $f$ 的最高阶纯尾部分，且 $\|u_m\|_2\le\|f\|_2$。

在单个位上，$S_j=D_j-C_j-2P_j$；其中 $C_j$ 升一阶，$D_j$ 降一阶，$P_j$ 保阶。故 $(-1)^pS_J$ 的最高升 $p$ 阶项是 $\prod_{j\in J}C_j$。

在 (3.3) 中，尾次数达到 $p$ 的系数只可能来自 $K=\varnothing,r=p$，此时头插值为 $p_\varnothing(A_m)=I$。因此

$$
\boxed{
\mathcal L_{f,m}=C_{u_m}+\mathcal R_{f,m},}
\tag{4.2}
$$

其中 $C_{u_m}$ 精确升 $p$ 阶，而 $\mathcal R_{f,m}$ 对任意纯尾次数最多升 $p-1$ 阶。

由 R84 合成上界和平方零卷积的 Hilbert 上界，可以统一取

$$
\|\mathcal R_{f,m}\|_{H_{\mathrm{tail},\le q}\to H}
\le
H_{m,p,q},
\qquad
H_{m,p,q}
\le C_{p,q}2^N(m+1)^{p/2}\|f\|_2.
\tag{4.3}
$$

这里空间始终允许任意头 Hilbert 系数。特别地，

$$
\log(1+H_{m,p,q})=O_{p,q,f}(2^m+\log(m+1)).
\tag{4.4}
$$

## 5. R93 有限匹配左逆与完整下降递归

假设在尾 $[m,\infty)$ 中存在 $\nu_{p,q}$ 条两两不交的 $p$ 元边

$$
S_1,\ldots,S_\nu,
\qquad
|\widehat f(S_i)|\ge t>0.
\tag{5.1}
$$

把 R93 的 (1.2) 应用于 $u_m$，取 $M=\|f\|_2$。于是 $C_{u_m}$ 在每个纯尾 $k\le q$ 阶上有统一左界

$$
\|v\|_2\le K_m(t)\|C_{u_m}v\|_2,
$$

$$
K_m(t)\le
c_{p,q}^{-1}\|f\|_2^{K_{p,q}-1}t^{-K_{p,q}}.
\tag{5.2}
$$

该下界张量上任意头 Hilbert 空间后不变。

写

$$
g=\sum_{k=0}^qg_k,\qquad
v=\mathcal L_{f,m}g,
$$

其中 $g_k$ 为纯尾 $k$ 阶。最高输出次数 $p+q$ 只有 $C_{u_m}g_q$；在输出次数 $p+k$，只有 $C_{u_m}g_k$ 以及由 $g_{k+1},\ldots,g_q$ 经 $\mathcal R_{f,m}$ 产生的项。更低的 $g_j$ 不可能升到这个次数。

因此从 $k=q$ 向下逐层有

$$
\|g_k\|_2
\le K_m(t)
\left(
\|v\|_2+
H_{m,p,q}\sum_{\ell>k}\|g_\ell\|_2
\right).
\tag{5.3}
$$

有限递归给，例如，

$$
\|g\|_2
\le
C_q K_m(t)
\left(1+H_{m,p,q}K_m(t)\right)^q
\|v\|_2.
\tag{5.4}
$$

对充分高位，可令 $t\le\min(1,\|f\|_2)$；较大系数只涉及有限初始情况。把固定 $\|f\|_2$ 的幂吸收进常数，结合 (4.4)，得到

$$
\boxed{
\|g\|_2
\le
C_{p,q,f}\exp(C_{p,q}2^m)
t^{-K_{p,q}(q+1)}
\|\mathcal L_{f,m}g\|_2.}
\tag{5.5}
$$

没有把“最高纯尾创建单射”直接替代完整算子单射；(5.3) 明确处理了全部下降项和头分量。

## 6. 实际误差排除阈值以上的大匹配

将 (3.7) 代入 (5.5)，并用 $g\ne0$ 消去 $\|g\|_2$，得到

$$
1\le
C_{p,q,f}\exp(C_{p,q}2^m)
t^{-K_{p,q}(q+1)}
\varepsilon_{m,p,q}\|f\|_2.
\tag{6.1}
$$

由 (2.10)，右侧除 $t$ 的负幂以外，其对数为

$$
-\frac{260}{3}16^m+O_{p,q,f}(8^m+m2^m).
$$

所以每个这样的 $\nu$ 条匹配，其最小系数模必满足

$$
t\le
\exp\left[
-\frac{20}{K_{p,q}(q+1)}16^m
\right]
\tag{6.2}
$$

对全部充分大 $m$ 成立。由定义 (1.3)，阈值以上不能有 $\nu$ 条两两不交边，匹配数最多为 $\nu-1$。

选择一个极大匹配；因为匹配数有上述有限上界，贪心过程至多取 $\nu-1$ 条边后终止。其顶点并 $B_{f,m}$ 至多有 $p(\nu-1)$ 个顶点，而且与每条阈值以上边相交，否则还能加入下一条不交边。这证明 (1.5)–(1.6)，主定理得证。

## 7. 对称版本及准确边界

由实际 $B$-对称性，可交换 $f,g$ 重复全部论证。因此两端最高次数的高位超图都得到同型结论。取两个有限覆盖的并，可同时处理两端阈值以上的边，覆盖大小仍只依赖次数。

但一般 $p\ge2$ 时，下列推断没有得到证明：

$$
\sup_{\substack{S\subseteq[m,\infty)\setminus B_{f,m}\\|S|=p}}
|\widehat f(S)|\text{ 很小}
\quad\not\Rightarrow\quad
\sum_S|\widehat f(S)|^2\text{ 或 }\sum_S|\widehat f(S)|
\text{ 同样小}.
$$

在一个固定尾起点，仅有逐系数阈值时，可以有非常多的小系数保留相当大的 $\ell^2$ 质量。原本的一致平方可和性不能自动给出与 $\alpha_m$ 同步的尾速率。

尤其不能照搬 R91 的一次序列计数：在 $p=1$ 中删去 $\ell$ 个顶点只删去 $\ell$ 个系数；在高阶超图中，一个顶点就可连接无穷多条边。R91 用到的“尾第 $\ell+r$ 大系数由后移 $\ell$ 位的第 $r$ 大系数控制”在这里没有同样含义。

本稿已证的是实际零矩的有限匹配、有限顶点覆盖必要条件及完整头行恢复。覆盖之外的总质量控制、较低次数条件化，以及最终的任意有限 chaos 配对分离仍需后续论证。
