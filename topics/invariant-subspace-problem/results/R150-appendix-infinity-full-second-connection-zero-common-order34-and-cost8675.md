# R150：无穷远完整第二连接为零、公共三十四阶与条件来源费 8675

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿证明原自然无穷远的完整第二连接准确为零。原十四个正 Smith 指数中，准确四个等于一，其余十个全部不小于三；全部原最大子式共同消失至少三十四阶，全部低一阶子式至少三十一阶。

证明为剩余三个横向泛函构造完整二阶左延拓，保持全部原 $6188$ 来源。新计算只涉及原 $u^2$ 系数和一个 $1088\times595$ 有理矩阵，未重算旧正常形。结合原二十九条精确 Koszul 曲线和有限公共 $K_{77}$，同一指定子式给 $63/62/59$ 阶及条件原来源成本 $8675$。

## 1. 原完整对象及尚余的三个左泛函

固定自然参数 $u=1/s$，原成本齐次矩阵为
$$
A(u)=A_0+uA_1+u^2A_2+\cdots:
\mathbb Q[[u]]^{6188}\longrightarrow\mathbb Q[[u]]^{4367}.
\tag{1.1}
$$
来源仍是原十七式乘全部次数至多三的单项式；目标是原次数一至五的全部单项式。参数系数不含阶乘。

已付事实如下。

- [完整常数纤维](R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md)有秩 $4340$，函数域秩为 $4354$，完整常数余空间维数为 $27$。
- [完整第一连接](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)准确有秩 $4$。其目标余空间是二十维纯切向部分和七维一次横向部分；第一连接像位于后者。
- [纯切向第二连接消去](R150-appendix-infinity-second-connection-pure-cancellation-and-common-order31.md)已给全部二十个纯切向泛函的真实二阶左延拓。

故第二页目标维数为 $27-4=23$。还需延拓的只有已付的三个一次横向泛函。本稿直接构造这些延拓。

## 2. 同一原图及三个真实一阶左延拓

先按前稿作物理反序，记
$$
K^\sharp_{ij}=K_{5-i,5-j},\qquad
v(u)=(1,u,u^2,u^3,u^4,u^5)^{\mathsf T}.
$$
再作可逆共动矩变换
$$
m_j(u)=\sum_{k=0}^j\binom jk u^{j-k}n_k,
\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\ (2\le j\le10).
\tag{2.1}
$$
在下文矩阵上，$A_k$ 均指这个真实共动图的系数。最终通过完整目标转置变换返回原自然图。

沿用原
$$
P_0,P_1\in\mathbb Q^{170\times135},\qquad
\operatorname{rank}P_0=128.
$$
其行是 $(i,a,b)$，对应 $c^ad^bF_i$、$a+b\le3$；列是
$c^ad^bz_j$、$a+b\le4$。取完整核基
$$
P_0Q=0,\quad Q\in\mathbb Q^{135\times7},
\qquad
P_0^{\mathsf T}U=0,\quad U\in\mathbb Q^{170\times42}.
$$
令
$$
C_{\rm tr}=U^{\mathsf T}P_1Q,\qquad
V:\mathbb Q^3\xrightarrow{\sim}\ker C_{\rm tr}.
\tag{2.2}
$$
原第一连接稿已构造并全行验证
$$
q_0=QV,\qquad
P_0W=P_1QV,\qquad W\in\mathbb Q^{135\times3}.
\tag{2.3}
$$
因此 $q_0-uW$ 是三个真实一阶左零延拓。它们的常项与二十个纯切向泛函共同构成完整第二页对偶基。

七个 $Q$ 自由坐标保持原规范
$$
z_{10},\ c z_{10},\ c^4z_6,\ c^4z_7,\ c^4z_8,\ c^4z_9,\ c^4z_{10}.
$$
$V$ 仍取前稿的 $e_0,e_1$ 及第三个已核有理列；本次以全部矩阵哈希和完整 $170$ 行身份检查这一规范，没有另换来源或任意重选一阶校正。

## 3. 完整二阶残差只需哪些真实来源行

原共动式在切向平面上的二阶项已准确为
$$
F_2(c,d,0)
=d^2s_2,\qquad
s_2=(0,0,0,0,0,0,0,0,-8,-16,-8,0,0,0,0,0,0)^{\mathsf T}.
\tag{3.1}
$$
同时 $F_0(c,d,0)=F_1(c,d,0)=0$。

令 $P_2\in\mathbb Q^{170\times135}$ 是同一真实原式的二阶一次横向系数。对三个给定一阶延拓，残差为
$$
R=A_2^{\mathsf T}q_0-A_1^{\mathsf T}W.
\tag{3.2}
$$
它只支持以下来源：

1. 全部 $170$ 个纯切向来源 $c^ad^bF_i$，$a+b\le3$。
2. 全部 $918$ 个一次横向来源 $c^ad^bz_lF_i$，$a+b\le2$、$2\le l\le10$。

纯行上的矩阵为
$$
R_{\rm pure}=P_2QV-P_1W.
\tag{3.3}
$$
一次横向行 $(i,a,b,l)$ 的第 $k$ 列准确为
$$
R_{(i,a,b,l),k}=(s_2)_i(q_0)_{(a,b+2,l),k}.
\tag{3.4}
$$
这里保留了 $A_2$ 的纯项；不能只使用 $P_2$。

对于含至少两个横向变量的其他 $5100$ 个来源，$A_2^{\mathsf T}q_0$ 为零，因为乘积至少有两个横向变量，而 $q_0$ 只支持一次横向目标；$A_1^{\mathsf T}W$ 为零，因为 $F_1$ 本身至少有一个横向变量。故 (3.3)–(3.4) 已准确记录全部原来源上的残差。

## 4. 保一阶歧义和全部二次横向校正

允许二阶目标校正使用以下全部 $585$ 个坐标：

- $135$ 个一次横向目标 $c^ad^bz_j$，$a+b\le4$；
- $450$ 个二次横向目标 $c^ad^bz_jz_k$，$a+b\le3$、$2\le j\le k\le10$。

把完整 $A_0^{\mathsf T}$ 在这些目标和第 3 节来源上的限制记为
$$
J_0\in\mathbb Q^{1088\times585}.
$$
它在其余 $5100$ 个来源上严格为零：$F_0$ 至少有一个横向变量，乘至少二次横向来源后至少有三个，超过该校正的横向次数。

一阶校正还可以加任意 $QB$。其二阶贡献准确为
$$
J_1=A_1^{\mathsf T}Q
=\begin{pmatrix}P_1Q\\0\end{pmatrix}
\in\mathbb Q^{1088\times7}.
\tag{4.1}
$$
实际计算使用
$$
\mathcal D=[\,J_0,\ J_1,\ R\,]\in\mathbb Q^{1088\times595}.
\tag{4.2}
$$
对这个真实有理矩阵只作一次 RREF，得到
$$
\operatorname{rank}J_0=578,\qquad
\operatorname{rank}[J_0,J_1]=582,\qquad
\boxed{\operatorname{rank}\mathcal D=582.}
\tag{4.3}
$$
最后三列的增秩为零。按这三列的单位自由坐标，实际构造了
$$
H\in\mathbb Q^{585\times3},\qquad
B\in\mathbb Q^{7\times3}
$$
并逐全部 $1088$ 行验证
$$
\boxed{J_0H+J_1B+R=0.}
\tag{4.4}
$$
三列的常项坐标矩阵准确为 $I_3$，没有丢掉任何给定的 $q_0$ 方向。

上述有界校正空间足以给 (4.4)。证明不需要断言所有可能的二阶校正都支持在这 $585$ 个坐标，也没有把非纯像预先认成高横向空间。

## 5. 三个完整二阶左延拓与第二连接为零

把 $H$ 按其真实一次、二次横向目标坐标延拓到完整目标空间，定义
$$
\Lambda(u)=q_0+u(-W+QB)+u^2H.
\tag{5.1}
$$
零阶由 $P_0Q=0$ 消失；一次项由 (2.3) 消失；二次项由 (4.4) 消失。对遗漏的 $5100$ 个来源：

- $A_2^{\mathsf T}q_0$ 已由第 3 节的次数理由为零；
- $A_1^{\mathsf T}(-W+QB)$ 至少含三个横向变量，不能被一次横向目标泛函读到；
- $A_0^{\mathsf T}H$ 至少含三个横向变量，不能被最高二次横向的 $H$ 读到。

因此
$$
\boxed{A(u)^{\mathsf T}\Lambda(u)=O(u^3)}
\tag{5.2}
$$
是全部原 $6188$ 来源上的身份。

若共动矩阵写为 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，完整原左列为
$T^{\mathsf T}\Lambda$。两侧基变换在 $u=0$ 可逆，二阶转置运输保留；所以 (5.2) 也给原自然图的真实左延拓。

第 1 节的二十条纯切向左二阶 jet 加上 (5.1)，其常项独立且覆盖完整 $23$ 维第二页对偶。对任意真实来源提升
$$
A_0v_0=0,\qquad A_1v_0+A_0v_1=0,
$$
把左 jet 的零、一次、二次身份配上 $v_1,v_0$，得到
$$
\lambda_0^{\mathsf T}(A_2v_0+A_1v_1)=0.
$$
全部第二页目标泛函都杀掉第二连接，故
$$
\boxed{\beta_{2,\infty}=0.}
\tag{5.3}
$$
这是完整第二连接的等式。实际计算开始时只设计为上界接口；上界为零后已足以得到 (5.3)，无需任何未付的完整来源下界。

## 6. 完整 Smith 阶及指定原子式

原十四个正指数中，准确四个为一，第二连接为零说明没有指数等于二。因此十个其余正指数至少为三：
$$
\boxed{\delta_{4354,\infty}\ge4+10\cdot3=34.}
\tag{6.1}
$$
取最小的 $4353$ 个非零指数，相当于从十四个正指数中保留最小十三个，仍有
$$
\boxed{\delta_{4353,\infty}\ge4+9\cdot3=31.}
\tag{6.2}
$$
没有由此证明这两个下界取等。

按[完整 Smith 与真实 Koszul 曲线的因子引理](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)，原指定来源集 $J$ 保留二十九维精确完整形式核曲线常项。删掉一个来源坐标仍保至少二十八维。因此同一个原最大子式、原来源换列及 cofactor 分别满足
$$
\boxed{
v_uD_h\ge34+29=63,\quad
v_uD_{{\rm original\ replace},h}\ge34+28=62,\quad
v_uD_{{\rm cofactor},h}\ge31+28=59.}
\tag{6.3}
$$
任意无极点目标换列只使用 cofactor 的 $59$ 阶；不能因为目标有全局多项式来源，就把它自动纳入原来源换列的 $62$ 阶。

## 7. 结合 K77 的完整原来源条件界

[零点第二纯消去](R150-appendix-zero-second-connection-pure-cancellation-factor77-and-cost8678.md)
已给有限公共因子
$$
K_{77}=s^{31}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2,
\qquad \deg K_{77}=77.
$$
保持原总权 $H=8770$、$\max a_\ell=55$、$\delta_\ell=a_\ell-10$、
$\max\delta_\ell=45$。原同一个指定 $D$ 模 $31$ 非零，完整仿射 gcd 次数 $315$ 只给 $\deg D\ge315$。

令 $d_*=D/K_{77}$、$q=\deg d_*$。由 (6.3)，
$$
\boxed{238\le q\le8770-63-77=8630.}
\tag{7.1}
$$
对原非基来源列，
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{77}
\in\mathbb Q[s]^J,\qquad A_JP_\ell=d_*A_\ell
$$
保持全部原输出，且
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-62-77.
\tag{7.2}
$$

明确假定某原目标 $b_\nu=h_0t_\nu$ 已属于 $\operatorname{im}_{\mathbb Q[s]}A$，保原目标权 $\tau_\nu\le64$。成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{77}
$$
为多项式，cofactor 给
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-59-77.
\tag{7.3}
$$
用同一 $d_*$ 对非基来源作除法并移回基来源后，三类成本上界为
$$
\begin{aligned}
q-1+45&\le8674,\\
8770+55-62-77-11&=8675,\\
8770+64-59-77-10-238&=8450.
\end{aligned}
\tag{7.4}
$$
于是
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8675.}
\tag{7.5}
$$
原目标成员性及 $\operatorname{lc}D$ 的 $31$ 单位性仍未由本稿完成。

## 8. 原二阶生成与实际计算记录

脚本直接从原 $K^\sharp,J_2,J_3$ 重建十七式到 $u^2$。具体地，记
$p_r=K^\sharp e_r$，$M_r=[u^r]M$，并用
$L_yM=J_3^{-1}B(K^\sharp v)J_2M$ 得到零至二阶系数 $\ell_r$。
它使用完整卷积
$$
(MKM)_k=\sum_{r=0}^kM_rK^\sharp M_{k-r},\qquad
\tau_k=\sum_{r=0}^k\operatorname{tr}(K^\sharp M_rK^\sharp M_{k-r}),
$$
$$
N_k=4(MKM)_k+6\sum_{r=0}^k(\ell_r)_{p_{k-r}},
$$
$$
\Gamma_k=
2\sum_{r=0}^k\tau_r e_{k-r}
+8\sum_{r=0}^k(MKM)_r p_{k-r}
-12\sum_{r=0}^k\ell_r:(K^\sharp M_{k-r}K^\sharp),
\quad 0\le k\le2.
$$
这些是实际参数系数卷积；特别保留一次项之间的二阶乘积。单个 $n_j$ 对 $m_{j+k}$ 的贡献为 $\binom{j+k}{k}u^k$。提取一次横向系数时，二阶纯平面值也完整相减。

[小脚本](../notes/2026-11-15-r150-infinity-second-normal-envelope-789f.py)
SHA256 为
6cb201867c430b4375dbe93cb411ad1e74bea39571261d1ecfec233e4b397517。
运行 $43679903558$，步骤 infinity-second-normal-envelope，
执行源码提交 9caa16ab891585d8b6fb427111cce773df592801。
共享时限 $30$ 秒、地址空间 $512$ MiB，实际数学用时
$1.2912803999988682$ 秒，退出码 $0$。

实际前缀秩依次为 $578,582,582$；全部 $1088$ 行校正通过，
三个 leading 自由坐标为 $I_3$。主要哈希为：

| 对象 | SHA256 |
|---|---|
| 原 $P_2$ | 06eb39dc2c16d6dd5760e405c602b2f60b0d2239383d6d2d01c2bd063317982b |
| 完整 $1088\times595$ 增广矩阵 | ac9ad0297fbe1b1d91ca10669d0031ac2ad991e6ffaf6c9f2b4a58daadfc705a |
| 全部校正与三个单位 leading 列 | fbc94c9c58520b5ceca4b9e3d4dbccd6789d2643ff9c05876984beead36deed5 |

原临时小回执 $3703$ 字节，SHA256 为
9885a405a820797addc6a9a399af0e51e44ca0cd6e7aff604e79b608a784aac2。
[小执行记录](../notes/r150-infinity-remote-session-789f/43679903558-infinity-second-normal-envelope.json)
保输入哈希、真实参数、秩和全部身份标志。可重算大数组只在实际作业内临时使用；本稿未调用旧正常形、旧大 Dixon 或新的模素数高位。
