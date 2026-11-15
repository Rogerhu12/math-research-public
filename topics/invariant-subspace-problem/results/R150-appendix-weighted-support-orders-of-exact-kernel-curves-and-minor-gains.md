# R150：带支撑消失阶的精确核曲线与全部原子式的加权因子

日期：2026-11-15 UTC。Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。

本稿把[完整 Smith 与精确核曲线的因子引理](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)从常项支撑推广到有限阶支撑。关键条件是同一条完整精确核曲线在所选来源之外消失到几阶；不能用仅有常项的核或未经校正的有限右 jet 替代。

该推广给一个只涉及已有二十九条 Koszul 曲线的后继入口：计算其未校正的一阶外来源矩阵 $M_1$，无需恢复其余七个大有理核，也无需再消元旧 $1603$ 阶单位块。本稿不预报 $M_1$ 的实际秩。

## 1. 完整 Smith 因子和固定来源集

令 $R=\mathbb Q[[u]]$，赋值记为 $v_u$。设
$$
A:R^p\longrightarrow R^m,\qquad \operatorname{rank}_{\mathbb Q((u))}A=n.
$$
完整 Smith 分解可写为
$$
A=X\,\operatorname{diag}(u^{a_1},\ldots,u^{a_n})\,E,
\qquad 0\le a_1\le\cdots\le a_n.
\tag{1.1}
$$
这里 $X$ 是某个 $GL_m(R)$ 矩阵的前 $n$ 列，$E$ 是某个 $GL_p(R)$ 矩阵的前 $n$ 行。特别，$X$ 在分式域上单射，故
$$
A\kappa=0\quad\Longrightarrow\quad E\kappa=0.
\tag{1.2}
$$
记 $\delta_j=\sum_{i=1}^j a_i$，$\delta_0=0$。

固定一个大小为 $k\le n$ 的原来源集 $J$。假定有 $t\le k$ 条完整精确曲线
$$
\kappa_1,\ldots,\kappa_t\in\ker_R A
$$
及正整数 $\ell_1,\ldots,\ell_t$，满足：

- 各 $\kappa_{q,J}(0)$ 在 $\mathbb Q^J$ 中线性独立；
- 各外来源部分满足
$$
\kappa_{q,J^c}(u)\in u^{\ell_q}R^{J^c}.
\tag{1.3}
$$

给这 $k$ 个来源方向配权
$$
e=(\ell_1,\ldots,\ell_t,\underbrace{0,\ldots,0}_{k-t}).
$$
对 $0\le j\le k$，令 $\sigma_j(e)$ 为这 $k$ 个数中最小 $j$ 个的和。

## 2. 同一个可逆右基变换保留全部支撑阶

由于各常项独立，列 $\kappa_{q,J}(u)$ 可以补成
$$
U(u)\in GL_k(R).
$$
具体只需用常数列补齐它们在 $u=0$ 的基；所得行列式有非零常项，故在 $R$ 上可逆。

对任意 $j$ 个 active Smith 行 $K\subseteq\{1,\ldots,n\}$，由 (1.2) 得
$$
E_{K,J}\kappa_{q,J}
=-E_{K,J^c}\kappa_{q,J^c}\in u^{\ell_q}R^j.
$$
因此同一个 $U$ 给
$$
E_{K,J}U
=Y_K\,\operatorname{diag}(u^{e_1},\ldots,u^{e_k})
\tag{2.1}
$$
，其中 $Y_K$ 的全部系数在 $R$ 中。这里没有除以可能带极点的目标或来源变换。

取任意 $j$ 个实际来源列 $L\subseteq J$。从
$E_{K,J}=Y_K\operatorname{diag}(u^e)U^{-1}$
作 Cauchy–Binet 展开，$E_{K,L}$ 的每个行列式项都含 $j$ 个不同来源权的和，因而
$$
\boxed{v_u\det E_{K,L}\ge\sigma_j(e).}
\tag{2.2}
$$
所有 $U^{-1}$ 子式均在 $R$，不能降低赋值。式 (2.2) 同时成立于全部实际删列；并不是为每个子式重新选择来源曲线。

## 3. 原矩阵的全部子式下界

对任意大小为 $j$ 的原输出集 $I'$ 和 $L\subseteq J$，再次在 (1.1) 上展开：
$$
\det A_{I',L}
=\sum_{\substack{K\subseteq\{1,\ldots,n\}\\|K|=j}}
\det X_{I',K}\;
u^{\sum_{q\in K}a_q}\;
\det E_{K,L}.
$$
每个输出小子式都无极点，而 $\sum_{q\in K}a_q\ge\delta_j$。结合 (2.2)，
$$
\boxed{v_u\det A_{I',L}\ge\delta_j+\sigma_j(e).}
\tag{3.1}
$$
恒零子式按无限赋值处理。这里把完整 Smith 阶和独立来源支撑阶相加，是因为它们来自上述同一展开的两个不同因子。

特别，当 $k=n$ 时，记
$$
g=\sum_{q=1}^t\ell_q,\qquad
L_{\max}=\max(\{0\}\cup\{\ell_q:1\le q\le t\}).
$$
则所选最大子式和全部对应 cofactor 分别满足
$$
\boxed{
v_uD_J\ge\delta_n+g,\qquad
v_u(\text{cofactor})\ge\delta_{n-1}+g-L_{\max}.}
\tag{3.2}
$$

若把 $J$ 中一个原来源换成任意另一个原来源 $a$，则 active 来源因子是
$[E_{:,J\setminus\{b\}},E_{:,a}]$。沿最后一列展开，每项都含一个 (2.2) 的 $n-1$ 阶小子式。因此
$$
\boxed{
v_uD_{\text{original replace}}
\ge\delta_n+g-L_{\max}.}
\tag{3.3}
$$
若新列只是任意解析目标列，而非 $A$ 的一个原来源列，则直接适用的是 cofactor 下界
$\delta_{n-1}+g-L_{\max}$。有全局多项式来源，并不自动保证换到原成本齐次图后仍无极点。

式 (3.2)–(3.3) 的删列损失由 exterior minors 支付。不能把删去一个来源后对曲线常项和一次项的两道支撑条件，未经论证只算成一条常数约束。

## 4. 原二十九条 Koszul 曲线的一阶外支撑接口

回到本课题 $p=6188,m=4367,n=k=4354$，保持原同一 $I,J$ 和自然 $u=1/s$。

原十七式的齐次化记为 $F_i^h(u,m)$。全部
$$
m^\alpha(F_j^h e_i-F_i^h e_j),
\qquad i<j,\quad |\alpha|\le1,
\tag{4.1}
$$
给一共 $1632$ 条原来源次数至多三的完整精确 Koszul 曲线。把它们列成 $\Phi(u)$，有原式恒等
$$
A^h(u)\Phi(u)=0.
\tag{4.2}
$$
同一自然参数、全部来源坐标及原权合法性见
[原二十九条形式核曲线](R150-appendix-selected-koszul-curves-infinity-order43-and-source-cost8712.md)。

[精确支撑交](R150-appendix-selected-infinity-twentynine-exact-koszul-kernels.md)已经给常数有理矩阵
$$
X\in\mathbb Q^{1632\times29},
$$
使 $\Phi(0)X$ 在 $J^c$ 全零，且其 $J$ 部分的二十九列常项独立。原完整整数列、全来源乘回和自由坐标秩均已支付。

唯一新增的小矩阵为
$$
M_1=(\Phi_1X)_{J^c}\in\mathbb Q^{1834\times29},
\qquad \Phi_1=[u]\Phi(u).
\tag{4.3}
$$
设其实际精确秩为 $r$，置
$$
t_2=29-r.
$$
取 $\ker M_1$ 的基并补成 $GL_{29}(\mathbb Q)$ 的常数基变换。对应 $t_2$ 条完整精确曲线在外来源上为 $O(u^2)$；其余 $29-t_2$ 条为 $O(u)$。所有二十九个常项仍独立。

所以 (3.2)–(3.3) 可用
$$
g=29+t_2,\qquad
g-L_{\max}=28+\max(t_2-1,0).
\tag{4.4}
$$
这里只使用固定的二十九条原曲线的常数线性组合。允许另加 $u\Phi(u)Y$ 等可行纠偏后，二阶支撑空间可能更大；本稿既不排除该改进，也不把 $t_2$ 称为最大可能维数。

## 5. 若取得实际 t2，可直接更新哪些已付界

[完整无穷远第二连接零](R150-appendix-infinity-full-second-connection-zero-common-order34-and-cost8675.md)已给
$\delta_n\ge34,\delta_{n-1}\ge31$。因此一旦 (4.3) 的实际精确秩完成，便有
$$
\boxed{
v_uD_h\ge63+t_2,\quad
v_uD_{\text{original replace},h}\ge62+\max(t_2-1,0),\quad
v_uD_{\text{cofactor},h}\ge59+\max(t_2-1,0).}
\tag{5.1}
$$
这三个式子是相对于当前公共 $34/31$ 阶的条件公式；不能把尚未计算的 $t_2$ 填成期望值，也不把本稿视为新的数值消失阶。

[有限零点完整二阶延拓](R150-appendix-zero-twenty-three-second-left-jets-factor80-and-cost8672.md)已付 $K_{80}$。令
$d_*=D/K_{80}$、$q=\deg d_*$，旧同一非零模 $31$ 子式给 $\deg D\ge315$。置 $a=\max(t_2-1,0)$，则
$$
235\le q\le8627-t_2.
$$
原非基、转回基来源和目标分支的成本分别不超过
$$
8671-t_2,\qquad 8672-a,\qquad 8450-a.
$$
因此在原目标 $h_0t_\nu$ 的完整 $\mathbb Q[s]$ 成员性前提下，
$$
\boxed{\operatorname{cost}(y_\nu)\le8672-\max(t_2-1,0).}
\tag{5.2}
$$
式 (5.2) 仍只是来源降度条件界；没有支付原目标成员性、固定分母指数或指定 $D$ 的 $31$ 单位首项。

## 6. 接续范围

后继可直接读取已有二十九条 primitive 整数系数列和本次已核的原 $F_0,F_1$ 整数缓存，生成 (4.3)。它应保相同 $1632$ 家族顺序、全部 $1834$ 外来源、全部 $6188$ 原系数以及完整一阶 syzygy
$$
A_0(\Phi_1X)+A_1(\Phi_0X)=0.
$$
先保存实际一阶外矩阵，再求其完整有理核，便可从实际检查点接续。它不需要重求旧 $1603$ 支撑核，也不需要从七个巨大有理方向重新开始。

本稿完成的是全来源加权因子定理及明确的较小后继接口。普通 Hilbert ISP、原目标成员性和边界同源预算保持开放。
