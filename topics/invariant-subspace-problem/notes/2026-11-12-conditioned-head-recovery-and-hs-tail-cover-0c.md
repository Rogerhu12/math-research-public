# 高位条件化的完整头恢复与最高阶尾平方和覆盖

日期：2026-11-12（UTC）。会话：Astra-ISP-0c017065。预留 R98。

**状态：下述实际条件化估计与尾平方和覆盖定理已证明；关键算子排列、顶阶系数保留及指数预算已由 l2_moments 独立核验。** 本稿把 R96 的影响量剥离和 R97 的创建下界接回真实算子，而不是只在独立位模型中工作。

新结论是：如果两个非零有限 Walsh 次数向量的全部实际矩消失，那么每个高位尾中，删去至多常数乘 $16^m$ 个顶点之后，其最高阶系数的整个平方和范数必小于 $e^{-a16^m}$。这控制的是总质量，严格补充 R94 的逐系数阈值覆盖；仍未控制全部固定低位行或所有较低次数。

## 1. 记号与主定理

令 $H=L^2(\mathbb Z_2,\mu)$，实际算子、归一化幂及双线性型为
$$
A f(y)=w(y)f(y-1),\qquad
N_j=A^{2^j}/d_j,\qquad
B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
$$
记 $E_j=e_{10}$ 为第 $j$ 位的独立算子，
$$
\|N_j\|=\|E_j\|=1,\qquad
\|N_j-E_j\|=\eta_j\le e^{-770\,16^j}.
\tag{1.1}
$$
令 $H_{\le p}$ 是总 Walsh 次数至多 $p$ 的空间。

设 $0\ne f\in H_{\le p}$、$0\ne g\in H_{\le q}$，其中 $p,q\ge1$；以下取 $p,q$ 为两端的实际最高次数，若原先仅给次数上界，先降到实际次数。假设
$$
B(A^nf,g)=0\qquad(n\ge0).
\tag{1.2}
$$
定义纯尾最高阶核
$$
u_m=\sum_{\substack{|S|=p\\S\subseteq[m,\infty)}}
\widehat f(S)x_S.
\tag{1.3}
$$
平方自由单项式 $x_S$ 正交归一。对有限 $B\subseteq[m,\infty)$，令 $u_m^{\setminus B}$ 只保留 $S\cap B=\varnothing$ 的系数。

取
$$
\Lambda_{p,q}=2q\binom{p+q-2}{p-1},\qquad
\rho_{p,q}=\frac1{2\Lambda_{p,q}},\qquad
a_{p,q}=\frac{20}{q+1+2\log 2/\rho_{p,q}}.
\tag{1.4}
$$
这些常数仅依赖次数，且全部为正。另令 $M_0=\max(1,\|f\|_2)$。

**定理 1.1。** 对全部充分大的 $m$，存在有限集 $B_m\subseteq[m,\infty)$，使
$$
\boxed{
|B_m|\le
\left\lceil\frac2{\rho_{p,q}}
\bigl(\log M_0+a_{p,q}16^m\bigr)\right\rceil,
\qquad
\|u_m^{\setminus B_m}\|_2\le e^{-a_{p,q}16^m}.
}
\tag{1.5}
$$
不要求这些顶点的最大编号受控。交换 $f,g$ 后得到另一端的同型结论；两个删点集的并同时控制双方，大小仍是 $O_{p,q,f,g}(16^m)$。

同一结论允许把 $a_{p,q}$ 同时替换为任意固定 $0<a\le a_{p,q}$，包括删点预算中的对应系数。证明中的剥离从该新目标 $e^{-a16^m}$ 重新启动，因而小指数可同时缩小条件化预算；不能只把已经选出的较大删点集当作具有新预算。

如果某端是非零常数，R11 的常向量循环性和 $B$ 对称性已经排除 (1.2)，故无需在主定理中处理 $p=0$ 或 $q=0$。

## 2. 物理零条件化的次数估计与不坍缩锚

对任意有限位集 $B$，把其物理位全部固定为 $0$，即令 $\chi_j=+1$，记所得剩余空间向量为 $f_B$。这不是在无穷多个位上取点值；有限次数空间上的有界条件化给出其准确含义。

按 $B$ 上的 Walsh 系数分组，
$$
f=\sum_{\substack{T\subseteq B\\|T|\le p}}\chi_T f_T,
\qquad f_B=\sum_{\substack{T\subseteq B\\|T|\le p}}f_T.
$$
不同 $T$ 的原项正交，故 Cauchy–Schwarz 给
$$
\boxed{
\|f_B\|_2\le D_p(s)\|f\|_2,\qquad
D_p(s)=\left(\sum_{k=0}^p\binom{s}{k}\right)^{1/2}
\le C_p(s+1)^{p/2},\quad s=|B|.
}
\tag{2.1}
$$
约定 $k>s$ 的二项系数为零。同样适用于 $g_B$。条件化后的总次数上限不变。

取一个固定 $q$ 元集合 $S_0$，使 $\widehat g(S_0)\ne0$。当 $m>\max S_0$ 且 $B\subseteq[m,\infty)$ 时，
$$
\widehat{g_B}(S_0)
=\sum_{T\subseteq B}\widehat g(S_0\cup T)
=\widehat g(S_0),
$$
因为所有非空 $T$ 都使总次数超过 $q$。因此
$$
\boxed{\|g_B\|_2\ge\alpha:=|\widehat g(S_0)|>0.}
\tag{2.2}
$$
这个下界同时独立于 $B$ 的大小、位置和条件化后的其他系数。

同理，$f_B$ 的最高 $p$ 阶纯尾部分恰为 $u_m^{\setminus B}$：条件化不能从原来更高次数产生新的 $p$ 阶项，因为那些次数根本不存在。较低次数可能改变，本稿会在模型余项中保留它们。

## 3. 允许任意有限高位集的真实头恢复

令 $N=2^m$，$A_m$ 是低 $m$ 位有限链，$W_n=\|A^n\|$，并把实际径向权记为 $\alpha_m^{\rm op}=a_m^{\rm op}$，以免与 (1.4) 的正数混淆。

R89/R94 的头 Walsh 插值给每个 $K\subseteq[0,m)$ 一个多项式 $p_K$，满足
$$
p_K(A_m)1=\chi_K,\qquad
\|p_K(A)\|,\|p_K(A_m)\|\le2^N,
$$
$$
\|p_K(A)-p_K(A_m)\|
\le\frac{N^22^N\alpha_m^{\rm op}}{W_{N-1}}.
\tag{3.1}
$$

固定任意有限 $B\subseteq[m,\infty)$，令 $s=|B|$、$E=[m,\infty)\setminus B$。在剩余头尾空间上取有限测试
$$
h=\sum_{\substack{K\subseteq[0,m)\\J\subseteq E,\ |J|\le p+q}}
c_{K,J}\chi_K\chi_J.
$$
将它在 $B$ 上张量常函数后仍记为 $h$。令
$$
T_j=2N_j-I,\quad S_j=2E_j-I,
$$
$$
P_h(A)=\sum_{K,J}c_{K,J}(-1)^{|J|}p_K(A)T_J,
\qquad
\widetilde P_h=\sum_{K,J}c_{K,J}(-1)^{|J|}p_K(A_m)S_J.
\tag{3.2}
$$
有 $\widetilde P_h1=h$。R84 的合成定理始终应用在原来的 $f\in H_{\le p}$ 上，R94 的排列给
$$
\|(P_h(A)-\widetilde P_h)f\|_2
\le C_{p,q}\sqrt N\,2^N
\left(\frac{N^2\alpha_m^{\rm op}}{W_{N-1}}+\eta_m\right)
\|h\|_2\|f\|_2,
\tag{3.3}
$$
$$
\|\widetilde P_h f\|_2
\le C_{p,q}\sqrt N\,2^N\|h\|_2\|f\|_2.
\tag{3.4}
$$
把合成指标限制为避开 $B$ 的集合不会增加这些常数。

写 $N_B=\prod_{j\in B}N_j$、$E_B=\prod_{j\in B}E_j$。排序 telescoping 与 (1.1) 给
$$
\|N_B\|\le1,\qquad
\|N_B-E_B\|\le\sum_{j\in B}\eta_j\le s\eta_m.
\tag{3.5}
$$
$N_B$ 与 $P_h(A)$ 交换；$E_B$ 与 $\widetilde P_h$ 交换。因而准确的差分排列是
$$
\boxed{
P_h(A)N_B-\widetilde P_h E_B
=N_B(P_h(A)-\widetilde P_h)
+(N_B-E_B)\widetilde P_h.
}
\tag{3.6}
$$
这里无需假设 $N_B$ 与模型测试交换，也没有先把 $N_Bf$ 当作有限 chaos 输入。

所有 $P_h(A)N_B$ 都是 $A$ 的多项式，故由 (1.2) 其与 $f,g$ 的配对为零。另一方面，逐位的精确式
$$
B(E_j u,v)=\tfrac12 B_{\rm remaining}(u|_{b_j=0},v|_{b_j=0})
$$
给
$$
B(\widetilde P_h E_Bf,g)
=2^{-s}B_{\rm remaining}(\widetilde P_h f_B,g_B).
\tag{3.7}
$$
反射在剩余坐标逐位进行；它与把这些位从指标集中删去完全相容。

结合 (3.3)—(3.7)，得到
$$
|B_{\rm remaining}(\widetilde P_h f_B,g_B)|
\le\varepsilon_{m,s}\|h\|_2\|f\|_2\|g\|_2,
$$
$$
\boxed{
\varepsilon_{m,s}
=C_{p,q}2^s\sqrt N\,2^N
\left(\frac{N^2\alpha_m^{\rm op}}{W_{N-1}}+(s+1)\eta_m\right).
}
\tag{3.8}
$$

## 4. 条件化模型的完整近核与最高创建项

对 $f_B$ 构造 R94 的模型乘法 $L_{f_B,m}$。明确地，把它分解为
$$
f_B=\sum_{\substack{K\subseteq[0,m)\\|K|\le p}}
\chi_K\sum_{r=0}^{p-|K|}f^B_{K,r},
$$
其中 $f^B_{K,r}$ 是剩余尾 $E$ 上纯 $r$ 阶向量，然后令
$$
L_{f_B,m}
=\sum_{K,r}(-1)^r p_K(A_m)\mathscr S_r(f^B_{K,r}).
\tag{4.1}
$$
R84 保证每项在固定有限尾次数层间有界；有限头可作任意 Hilbert 系数。

在这些自然次数层上，$L_{f_B,m}1=f_B$，它与全部模型测试交换并且对剩余双线性型对称。于是
$$
B_{\rm remaining}(\widetilde P_h f_B,g_B)
=B_{\rm remaining}(h,L_{f_B,m}g_B).
$$
输出尾次数至多 $p+q$，测试 $h$ 在完整有限头加这些尾次数的空间中稠密。因此 (3.8) 等价于完整向量估计
$$
\boxed{
\|L_{f_B,m}g_B\|_2
\le\varepsilon_{m,s}\|f\|_2\|g\|_2.
}
\tag{4.2}
$$

设 $u=u_m^{\setminus B}$。由 §2 的顶阶系数保留，最高升 $p$ 阶部分精确为 $C_u$，故
$$
L_{f_B,m}=C_u+R_{f_B,m},
\tag{4.3}
$$
余项在每个纯尾次数上至多升 $p-1$ 阶。R94 的头计数和 (2.1) 给
$$
\|R_{f_B,m}\|_{\mathrm{tail},\le q\to H}
\le H_{m,s},\qquad
H_{m,s}\le
C_{p,q}2^N(m+1)^{p/2}(s+1)^{p/2}\|f\|_2.
\tag{4.4}
$$
允许全部头分量，不曾把条件化后的较低次数项丢弃。

实际权的闭式及 R94 的同一计算给
$$
\log\varepsilon_{m,s}
\le-\frac{260}{3}16^m+s\log2+\log(s+1)
+O_{p,q}(8^m+m2^m).
\tag{4.5}
$$
特别地，$s$ 的指数代价只有已明确列出的 $2^s$；次数限制使 (4.4) 中的条件化损失仅为 $s$ 的固定次幂。

## 5. 低影响分支会与完整近核矛盾

对纯 $p$ 阶核 $u$，记
$$
I_i(u)=\sum_{S\ni i}|u_S|^2.
$$
R97 已自含证明，在所有尾次数 $\le q$ 上
$$
\|C_uv\|_2^2
\ge\bigl(\|u\|_2^2-\Lambda_{p,q}\sup_i I_i(u)\bigr)\|v\|_2^2.
\tag{5.1}
$$
此式也适用于带任意头 Hilbert 系数的输入。

假设某个 $B$ 满足
$$
\|u_m^{\setminus B}\|_2>\delta,
\qquad
\sup_i I_i(u_m^{\setminus B})
\le\rho_{p,q}\|u_m^{\setminus B}\|_2^2.
\tag{5.2}
$$
那么 $C_u$ 的左界为 $\delta/\sqrt2$。

将 $g_B=\sum_{k=0}^q v_k$ 按纯尾次数分解，并令 $v=L_{f_B,m}g_B$。从最高输出次数 $p+q$ 向下，在 $p+k$ 次数处，只有 $C_uv_k$ 以及由更高 $v_\ell$ 经余项产生的项。于是
$$
\|v_k\|_2\le\frac{\sqrt2}{\delta}
\left(\|v\|_2+H_{m,s}\sum_{\ell>k}\|v_\ell\|_2\right).
$$
有限下降递归给
$$
\boxed{
\|g_B\|_2
\le C_q\delta^{-1}
\left(1+H_{m,s}/\delta\right)^q
\|L_{f_B,m}g_B\|_2.
}
\tag{5.3}
$$
这里并非由最高创建项单射直接推整个模型单射；所有下降项都支付了 (5.3) 的代价。

## 6. 剥离、完整指数预算及主定理证明

令
$$
\delta_m=e^{-a_{p,q}16^m},\qquad \rho=\rho_{p,q}.
$$
对 $u_m$ 使用 R96 的影响量剥离。每一步若残余范数尚大于 $\delta_m$，且存在影响量大于残余平方范数的 $\rho$ 倍的顶点，就删去它。残余平方范数每次乘以小于 $1-\rho$ 的因子。因此存在有限 $B_m$，满足 (1.5) 的大小界，而且或已小残余，或满足 (5.2)。

反设沿无穷多个充分大的 $m$，算法以 (5.2) 的低影响大残余停止。它的大小满足
$$
s_m\le\frac{2a_{p,q}}\rho16^m+O_{p,q,f}(1).
\tag{6.1}
$$
把 (4.2) 代入 (5.3)。由 (4.4)，$\log(1+H_{m,s_m})=O_{p,q,f}(2^m+m)$，因为 $s_m=O(16^m)$。结合 (4.5)，右侧的对数上界为
$$
-\frac{260}{3}16^m+s_m\log2
+(q+1)a_{p,q}16^m
+O_{p,q,f,g}(8^m+m2^m).
$$
使用 (6.1) 和 (1.4)，其主项至多
$$
\begin{aligned}
&-\left[\frac{260}{3}
-a_{p,q}\left(q+1+\frac{2\log2}\rho\right)\right]16^m\\
&\hspace{2em}=-\frac{200}{3}16^m.
\end{aligned}
\tag{6.2}
$$
所以 (5.3) 强迫 $\|g_{B_m}\|_2\to0$。这与 (2.2) 的固定正下界 $\alpha$ 矛盾。

故全部充分大的 $m$ 只能落在小残余分支，正是 (1.5)。交换两端的论证相同。取删点集之并只会继续减少纯尾最高阶系数的平方和，故同时覆盖的陈述也成立。证毕。

## 7. 一个直接的无限秩配对排除类

定理 1.1 给可检验的反面判据。若某个非零 $f\in H_{\le p}$ 的最高阶核满足：对任意固定 $a,C>0$，有无穷多个 $m$ 使
$$
\inf_{\substack{B\subseteq[m,\infty)\\|B|\le C16^m}}
\|u_m^{\setminus B}\|_2>e^{-a16^m},
\tag{7.1}
$$
则它与任意非零有限 chaos 向量都不能全部矩消失。若存在一个次数 $q$ 的消失端点，(1.5) 会给具体的 $a,C$ 并与 (7.1) 矛盾。

R96 的星形块例子满足该判据。在其中心起点 $m=c_n$，精确最优残余为
$$
\inf_{|B|\le K}\|u_{c_n}^{\setminus B}\|_2^2
=\sum_{r\ge n+K}r^{-2}\ge\frac1{n+K}.
$$
取 $K=\lfloor C16^{c_n}\rfloor$，因 $n\le c_n+1$，该下界的平方根仅衰减为 $\exp[-O(c_n)]$，远大于任何固定 $e^{-a16^{c_n}}$。因此以这些核为最高阶部分、加上任意较低次数的向量，都与任意有限 chaos 端点分离。另一端可以有任意无限秩系数；本结论不要求双方同时局部有限。

## 8. 仍未闭合的部分

本条已把最高阶纯尾的逐系数信息提高为可支付实际进位误差的总平方和控制。为了取得它，确实允许条件化位数随 $m$ 增长，并明确证明了测试端不会因此坍缩；没有假设顶点位置受控或条件化代价为常数。

但 $f_B$ 的较低次数会收到原来含 $B$ 的高阶项的贡献。控制 $u_m^{\setminus B}$ 并不控制这些下降项的全部固定低位行。尤其不能把小最高阶纯尾直接当作 $f_B$ 接近常数，也不能由这里的近核估计宣称任意有限 chaos 已全部分离。

下一步需处理这些低阶行及其条件化后新增项，或找到足以结束有限次数下降的真实标量卷积机制。任意 $L^2$ 配对、普通不变格和完整 ISP 均仍未解决。
