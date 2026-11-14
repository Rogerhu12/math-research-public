# R93：Pouzet横截定理与有限块定量创建左逆

日期：2026-11-12（UTC）。子任务：literature。正式结果 R93；主会话逐段独审。**状态：已证明；第 2 节准确引用已出版旧定理，第 3—7 节为本次推导的 Hilbert 层量化结论。**

考虑交换平方零变量 $x_i^2=0$，齐次次数 $p$ 的系数空间为
$$
\mathcal R_p(E)=\ell^2([E]^p),\qquad E=\mathbb N
$$
或任意可数指标集。乘法是无交叠卷积
$$
(f\star g)_J
=\sum_{\substack{S\subseteq J\\|S|=p}}
f_Sg_{J\setminus S},
\qquad |J|=p+q. \tag{0.1}
$$

所问“无有限顶点覆盖的 $f$ 是否在每个有限次数层乘法单射”有肯定答案，而且可加强为**每个固定有限次数层都有有界左逆**。再进一步，固定数量的不交单项式及其系数模下界，给出与指标位置无关的统一幂次下界：

**主量化结论。** 对每个 $p\ge1,q\ge0$，存在整数
$N_{p,q},K_{p,q}\ge1$ 及常数 $c_{p,q}>0$，使以下成立。若
$$
u\in\mathcal R_p(E),\qquad \|u\|_2\le M,\qquad M>0,
$$
且存在 $N_{p,q}$ 个两两不交的 $p$ 元集合 $S_i$，满足
$$
|u_{S_i}|\ge t>0,
$$
则对每个 $v\in\bigoplus_{k=0}^q\mathcal R_k(E)$，
$$
\boxed{
\|u\star v\|_2
\ge c_{p,q}M^{1-K_{p,q}}t^{K_{p,q}}\|v\|_2.
} \tag{0.2}
$$
等价地，创建映射在这些有限次数层上有有界左逆，其范数至多
$c_{p,q}^{-1}M^{K_{p,q}-1}t^{-K_{p,q}}$。常数可以极大；证明不需要它们的实用数值。

## 1. 卷积的 Hilbert 有界性

对 $|J|=p+q$ 使用有限和的 Cauchy–Schwarz：
$$
|(f\star g)_J|^2
\le {p+q\choose p}
\sum_{\substack{S\subseteq J\\|S|=p}}
|f_S|^2|g_{J\setminus S}|^2.
$$
对 $J$ 求和，每个不交对 $(S,T)$ 出现一次，故
$$
\boxed{
\|f\star g\|_2
\le C_{p,q}\|f\|_2\|g\|_2,\qquad
C_{p,q}=\sqrt{{p+q\choose p}}.
} \tag{1.1}
$$
所以该乘法在 $\ell^2$ 齐次完成中良定义且连续。这里不需诉诸超可积性，也没有把无限坐标和逐点相乘的收敛性作为前提。

每个输出系数只有有限个分拆。因此将一个 $\ell^2$ 系数数组看成任意集合函数，是忠实嵌入；$\ell^2$ 中乘积为零恰等于所有有限集合系数都为零。这允许准确使用下一节的集合代数定理。

## 2. 已出版旧定理：零因子支撑有共同有限横截

原始来源：

Maurice Pouzet, **When is the orbit algebra of a group an integral domain? Proof of a conjecture of P. J. Cameron**, *RAIRO — Theoretical Informatics and Applications* **42** (2008), no. 1, 83–103. DOI:
[10.1051/ita:2007054](https://doi.org/10.1051/ita:2007054)。
[期刊原文 PDF](https://numdam.org/item/10.1051/ita:2007054.pdf)；
[作者预印本 arXiv:0704.1548](https://arxiv.org/abs/0704.1548)。

2026-11-12 已直接核对期刊原文：集合代数定义和 **Theorem 1.3 在印刷页 86**；证明为 **§2，页 92–99**；一次情形的精确界为 **Theorem 3.4，页 100–101**。使用的是全体有界次数的集合函数代数，不限有限支撑，也不要求群不变性或平方可和性。

对超图 $\mathcal H$，用 $\tau(\mathcal H)$ 表示最小顶点横截数，即最少多少个顶点可与每条边相交。Pouzet 的定理给出：对每个 $p,r$，存在仅依赖这两个次数的有限整数 $T(p,r)$；若特征零域上的两个非零齐次集合函数 $a,b$ 满足 $a\star b=0$，则
$$
\tau(\operatorname{supp}a\cup\operatorname{supp}b)\le T(p,r).
\tag{2.1}
$$
可取 $T(p,0)=0$；一次情形的最优值为 $T(1,r)=2r$。

因此这里原先待证的定性断言已由既有定理覆盖，而且结论更强：两个支撑有同一个有限覆盖，不只是至少一端有覆盖。下文不把这一旧结果冒充本仓库的新定理；新增的是它在 $\ell^2$ 创建映射上的明确左逆及统一幂次量化。

## 3. 足够多不交支持边给有限矩阵的满列秩

固定 $p\ge1,q\ge0$。取
$$
T_{p,q}=\max_{0\le r\le q}T(p,r),\qquad
N=N_{p,q}=1+\max(q,T_{p,q}). \tag{3.1}
$$
假设 $u\in\mathcal R_p(E)$ 的支持包含 $N$ 个两两不交集合
$S_1,\ldots,S_N$。记
$$
B=\bigcup_{i=1}^N S_i,\qquad b=|B|=pN,\qquad
u_B=\sum_{\substack{S\subseteq B\\|S|=p}}u_Sx_S.
$$
注意 $u_B$ 保留 $B$ 内的全部 $p$ 阶系数，不能只保留选中的 $N$ 条边。

对 $0\le r\le q$，定义有限维矩阵
$$
M_r(u_B):\mathcal R_r(B)\longrightarrow\mathcal R_{p+r}(B),
\qquad h\longmapsto u_B\star h. \tag{3.2}
$$
其行列按有限集合标号，矩阵元为
$$
[M_r(a)]_{J,T}
=\begin{cases}
a_{J\setminus T},&T\subseteq J,\\
0,&T\not\subseteq J,
\end{cases}
\quad |J|=p+r,\ |T|=r. \tag{3.3}
$$

**引理 3.1。** 每个 $M_r(u_B)$ 都满列秩。

**证明。** 不交支持边使任何 $\operatorname{supp}u_B$ 的覆盖至少有 $N$ 个顶点，故
$$
\tau(\operatorname{supp}u_B)\ge N>T(p,r).
$$
如果某个非零 $h\in\mathcal R_r(B)$ 满足 $u_B\star h=0$，(2.1) 会给
$\tau(\operatorname{supp}u_B)\le T(p,r)$，矛盾。原定理要求底集至少有 $p+r$ 个元素；这里
$b=pN\ge p(q+1)\ge p+q\ge p+r$，所以该条件已核对。$r=0$ 时也可直接由 $u_B\ne0$ 得到。证毕。

因此
$$
\beta=\min_{0\le r\le q}
s_{\min}(M_r(u_B))>0. \tag{3.4}
$$
对每个 $r$ 取标准有限维左逆
$$
L_r=(M_r^*M_r)^{-1}M_r^*,
\qquad \|L_r\|\le\beta^{-1}. \tag{3.5}
$$

## 4. 块外次数的有限三角结构给全空间左逆

先固定总次数 $q$；所有较低层会在本节末一起处理。对有限集 $B$ 的外部次数作正交分解：
$$
\mathcal R_q(E)
=\bigoplus_{\ell=0}^q
\mathcal R_{q-\ell}(B)\otimes\mathcal R_\ell(E\setminus B),
\tag{4.1}
$$
$$
\mathcal R_{p+q}(E)
=\bigoplus_{\ell=0}^{p+q}
\mathcal R_{p+q-\ell}(B)\otimes\mathcal R_\ell(E\setminus B).
\tag{4.2}
$$
有限维中不存在的次数空间取零。

定义有界算子
$$
L:\mathcal R_{p+q}(E)\longrightarrow\mathcal R_q(E)
$$
为：在输出外部次数 $\ell\le q$ 的块上取
$L_{q-\ell}\otimes I$，在 $\ell>q$ 的块上取零。于是
$$
\|L\|\le\beta^{-1},\qquad L\,C_{u_B}=I,
$$
其中 $C_u h=u\star h$。

记 $u_{\rm ext}=u-u_B$。它的每个非零单项式至少含一个 $B$ 外顶点。故
$$
K:=L\,C_{u_{\rm ext}}
$$
严格增加外部次数（超过 $q$ 的部分被 $L$ 删去）。因此
$$
K^{q+1}=0,\qquad
LC_u=I+K. \tag{4.3}
$$
并且由 (1.1)
$$
\|K\|\le \beta^{-1}C_{p,q}\|u-u_B\|_2.
$$
这给出真正的有限和左逆：
$$
\Lambda=(I+K)^{-1}L
=\left(\sum_{j=0}^q(-K)^j\right)L,
\qquad \Lambda C_u=I. \tag{4.4}
$$
其范数满足
$$
\boxed{
\|\Lambda\|
\le\beta^{-1}
\sum_{j=0}^q
\left(\frac{C_{p,q}\|u-u_B\|_2}{\beta}\right)^j.
} \tag{4.5}
$$
这里没有要求块外系数很小。它们只造成有限个严格升层步骤，所以可用幂零逆精确处理。

对任意总次数 $k\le q$，重复同一构造，用到的有限左逆只属于
$0\le r\le k$，因而仍受同一个 $\beta$ 控制。又
$C_{p,k}\le C_{p,q}$、幂零阶至多 $q+1$，所以 (4.5) 同时控制所有这些层。不同输入总次数的输出总次数为 $p+k$，彼此正交；将这些左逆直和，便得到 $\bigoplus_{k\le q}\mathcal R_k(E)$ 上的同一统一界。

**推论 4.1。** 如果 $\operatorname{supp}u$ 没有有限顶点覆盖，那么对每个固定 $q$，$C_u$ 在 $\bigoplus_{k\le q}\mathcal R_k(E)$ 上有有界左逆。

**证明。** 可以贪心选出任意指定数量的不交支持边：已选边的顶点并是有限集，既然它不是覆盖，就存在下一条与它完全不交的支持边。取 (3.1) 的 $N$ 条，再用本节。证毕。

因此无有限覆盖不仅给逐层单射，还给逐层闭值域。下界可以随 $u,q$ 变化，不宣称在所有无有限覆盖的单位向量 $u$ 上有一个正的统一下界。

## 5. Nullstellensatz 给有限块的统一幂次下界

本节把依赖整个 $u_B$ 的 $\beta$，变成只依赖固定匹配系数下界的幂函数。先归一化
$$
\|u\|_2\le1,\qquad
|u_{S_i}|\ge t,\quad 0<t\le1.
\tag{5.1}
$$
重标号后，可固定
$$
B=\{1,\ldots,pN\},\qquad
S_i=\{p(i-1)+1,\ldots,pi\}.
$$
因此下面所有有限多项式和常数只依赖 $p,q$，不依赖原来的高位位置。

把 $a=(a_S)_{S\in[B]^p}$ 当作独立复变量，记
$$
P(a)=\prod_{i=1}^N a_{S_i}.
$$
固定 $r\le q$，令
$$
d_r=\dim\mathcal R_r(B)={pN\choose r}.
$$
取矩阵 $M_r(a)$ 的全部 $d_r\times d_r$ 满列极大子式，记作有限族
$\Delta_{r,\nu}(a)$。

**引理 5.1。** 若这些子式同时为零，则 $P(a)=0$。

**证明。** 若 $P(a)\ne0$，则指定 $N$ 条不交支持边全都存在。引理 3.1 完全不依赖系数的大小，故 $M_r(a)$ 满列秩，至少一个极大子式非零，矛盾。证毕。

由复多项式环的 Nullstellensatz，存在正整数 $\ell_r$ 及有限多项式
$Q_{r,\nu}(a)$，使
$$
\boxed{
P(a)^{\ell_r}
=\sum_\nu Q_{r,\nu}(a)\Delta_{r,\nu}(a).
} \tag{5.2}
$$
为明确所用形式：在附加变量 $z$ 中，理想
$$
(\Delta_{r,\nu}(a),\,1-zP(a))
$$
没有复共同零点，故含 $1$。把该有限恒等式中的 $z$ 替为 $1/P(a)$，再乘足够高的 $P$ 幂清分母，即得 (5.2)。这只是有限多项式证书；未要求实际算出巨大证书。

在单位球 $\|a\|_2\le1$ 上，各坐标模不超过一。令
$$
A_r=\max\left(1,\sum_\nu
\sum_{\alpha}|\operatorname{coef}_{a^\alpha}Q_{r,\nu}|\right)<\infty.
$$
由 (5.1)—(5.2)，
$$
\max_\nu|\Delta_{r,\nu}(a)|
\ge A_r^{-1}|P(a)|^{\ell_r}
\ge A_r^{-1}t^{N\ell_r}. \tag{5.3}
$$

再把子式与最小奇异值联系起来。由 (1.1)，
$$
\|M_r(a)\|\le C_{p,r}.
$$
任一极大方子矩阵 $M_{r,\nu}$ 是把输出投影到指定行后的矩阵。因此
$s_{\min}(M_{r,\nu})\le s_{\min}(M_r)$，而其余奇异值都不超过
$\|M_r\|$。故
$$
|\Delta_{r,\nu}(a)|
\le C_{p,r}^{\,d_r-1}s_{\min}(M_r(a)).
$$
结合 (5.3)，
$$
s_{\min}(M_r(a))
\ge A_r^{-1}C_{p,r}^{-(d_r-1)}t^{N\ell_r}. \tag{5.4}
$$

取
$$
\kappa=\max_{0\le r\le q}N\ell_r,\qquad
c_0=\min\left(
1,\min_{0\le r\le q}
A_r^{-1}C_{p,r}^{-(d_r-1)}
\right)>0.
$$
由于 $0<t\le1$，(5.4) 给
$$
\boxed{\beta\ge c_0t^\kappa.} \tag{5.5}
$$
$\kappa$ 是固定有限整数，$c_0>0$ 只依赖 $p,q$。

### 5.1 证书存在性所需的代数事实

为自含说明 (5.2) 的逻辑，这里给出标准的短证明。若复多项式理想是适当理想，把它包含于极大理想；对应商域是有限生成的 $\mathbb C$ 代数。Zariski 引理说明这样的域必为 $\mathbb C$，所以极大理想来自一个复点。

Zariski 引理可如下验证。假定域
$K=\mathbb C[a_1,\ldots,a_s]$。从生成元选一个极大代数独立子族
$a_1,\ldots,a_d$；其余元在
$\mathbb C(a_1,\ldots,a_d)$ 上代数，故在清除有限多个首项分母后，它们在
$$
R=\mathbb C[a_1,\ldots,a_d,D^{-1}]
$$
上整。由于 $R\subseteq K$ 且 $K$ 本来已由这些元作代数生成，$K$ 是 $R$ 的整扩张。整扩张若为域，底环也为域：对非零 $r\in R$，$r^{-1}\in K$ 的整方程乘以适当的 $r$ 幂即给 $r^{-1}\in R$。

若 $d\ge1$，可选复数 $c$ 使不可约元 $a_1-c$ 不整除固定非零多项式 $D$；它在 $R$ 中仍不可逆，与 $R$ 是域矛盾。因此 $d=0$，$K$ 是 $\mathbb C$ 的有限代数扩张，只能等于 $\mathbb C$。这证明了上面用的弱 Nullstellensatz；附加变量及清分母步骤便给 (5.2)。

## 6. 从有限块到完整创建算子的统一幂下界

仍在归一化 (5.1) 下。因为 (3.4) 的最小值包含 $r=0$，有
$$
\beta\le s_{\min}(M_0)=\|u_B\|_2\le1.
$$
又 $\|u-u_B\|_2\le1$、$C_{p,q}\ge1$。由 (4.5)，
$$
\|\Lambda\|
\le (q+1)C_{p,q}^{\,q}\beta^{-(q+1)}.
$$
与 (5.5) 组合，令
$$
K_{p,q}=\kappa(q+1),\qquad
c_{p,q}=\frac{c_0^{\,q+1}}{(q+1)C_{p,q}^{\,q}},
$$
得到
$$
\boxed{
\|u\star v\|_2
\ge c_{p,q}t^{K_{p,q}}\|v\|_2
\quad\left(v\in\bigoplus_{k=0}^q\mathcal R_k(E)\right).
} \tag{6.1}
$$

一般情形 $\|u\|_2\le M$ 只需对 $u/M$ 应用归一化结论。匹配系数下界变为 $t/M\le1$，再乘回 $M$：
$$
\|u\star v\|_2
\ge c_{p,q}M(t/M)^{K_{p,q}}\|v\|_2,
$$
正是 (0.2)。

本证明没有把无有限覆盖条件当作紧性条件。定量来源是：只选固定数量的不交边，所有其他有限块系数任意；其秩退化集合是有限代数簇，匹配坐标乘积在该簇上恒零，于是取得有限幂证书。块外无限系数则由严格升层的幂零逆处理。

## 7. 与实际 R84 零矩误差的直接接口

设实际向量 $f\in H_{\le p}$、$g\in H_{\le q}$ 满足全部 $A$ 矩消失。R84 已证明最高纯尾无交叠卷积满足
$$
\|f_{p,m}\star g_{q,m}\|_2
\le D_{p,p+q}\eta_m\|f\|_2\|g\|_2, \tag{7.1}
$$
其中 $f_{p,m}$ 只保留所有指标至少为 $m$ 的 $p$ 阶系数，$g_{q,m}$ 同理。

若 $f_{p,m}$ 在高位中有 $N_{p,q}$ 条两两不交的 $p$ 边，且各系数模至少为 $t$，则把 (0.2) 应用于
$u=f_{p,m}$、$M=\|f\|_2$，得到
$$
\boxed{
\|g_{q,m}\|_2
\le
\frac{D_{p,p+q}}{c_{p,q}}\,
\eta_m\,\|f\|_2^{K_{p,q}}\,
t^{-K_{p,q}}\,
\|g\|_2.
} \tag{7.2}
$$
所有常数只依赖次数，尤其不依赖所选高位的最大索引或间隔。

更一般地，(4.4) 和 (0.2) 提供的是全部有限次数创建块的左逆，可用于实际有限下降递归，而不只是最高纯尾单个分量。相应的真实进位与有限异常位条件化由并行的 R94 工作另行处理，本条不重复其尚在推进的步骤。

## 8. 准确结论与边界

已完成的定性问题是：对于 $\ell^2$ 完成的齐次平方零集合代数，若 $u$ 的支持没有有限顶点覆盖，则它在每个固定有限次数层上的乘法有有界左逆；若两个非零齐次元素乘积为零，则原出版定理还保证二者有共同的有限覆盖。

已完成的量化工具是 (0.2)，它允许任意复系数，并有固定次数决定的有限幂指数。它不提供最优的 $N_{p,q}$ 或最小指数，也不要求为这些巨大有限矩阵实际运行数值计算。

(7.2) 单独仍不能证明一般有限 chaos 全部矩分离：固定低位行及下降项还需结合实际模型处理。也未由任何完成环定性单射直接跨过进位误差，更没有据此宣称完整 Hilbert 不变子空间问题已解决。
