# R150：零点二十三条二阶左延拓、公共因子 K80 与条件来源费 8672

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿在原有限参数 $s=0$ 构造二十三条常项独立的完整二阶左零延拓。因此完整第一、第二连接的秩满足 $r_1+r_2\le4$。结合已付 $r_1\le4$，全部原最大子式在零点共同消失至少三十四阶，有限公共下因子提高为 $K_{80}=s^{20}K_{60}$。

结合已付无穷远指定 $63/62/59$ 阶，完整原来源的条件成本进一步降为 $8672$。本稿没有假定零点第一连接恰为四，也不单独宣称零点第二连接为零。

## 1. 原图与已经支付的二十条左延拓

保持原十七式、次数至多三的全部来源和自然参数 $s$：
$$
A(s)=A_0+sA_1+s^2A_2+\cdots:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
\tag{1.1}
$$
原常数秩为 $4340$，函数域秩为 $4354$；常数余空间维数为 $27$，有十四个正 Smith 指数，见
[零点完整秩证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)。

使用真实均值 $y(s)=(1,s,\ldots,s^5)^{\mathsf T}$ 和共动坐标
$$
m_j=\sum_{k=0}^j\binom jk s^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\ (2\le j\le10).
$$
[原零点二阶纯消去](R150-appendix-zero-second-connection-pure-cancellation-factor77-and-cost8678.md)
已保全部原来源，给出二十个纯切向泛函的真实二阶左延拓，并使用准确原二阶项
$$
F_2(c,d,0)
=d^2(0,0,0,0,0,0,0,0,2400,-960,96,0,0,0,0,0,0)^{\mathsf T}.
\tag{1.2}
$$
同时 $F_0(c,d,0)=F_1(c,d,0)=0$。

[完整第一连接上界](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)
给 $r_1\le4$。零点小横向包络的秩虽等于四，本稿仍不把它自动当作完整来源的下界。

## 2. 其余三个泛函及真实二阶残差

保持原
$$
P_0,P_1,P_2\in\mathbb Q^{170\times135}.
$$
行是十七式乘全部 $c^ad^b$、$a+b\le3$，列是
$c^ad^bz_j$、$a+b\le4$。它们是全部物理式在同一共动图中的零、一、二阶一次横向系数。

取
$$
P_0Q=0,\quad Q\in\mathbb Q^{135\times7},
\qquad
P_0^{\mathsf T}U=0,\quad U\in\mathbb Q^{170\times42}.
$$
令
$$
C_{\rm tr}=U^{\mathsf T}P_1Q,\qquad
V:\mathbb Q^3\xrightarrow{\sim}\ker C_{\rm tr}.
$$
已付规范为
$$
q_0=QV,\qquad P_0W=P_1QV.
\tag{2.1}
$$
三个 $q_0$ 只支持一次横向目标，彼此独立，且独立于二十个纯切向常项。

二阶残差
$$
R=A_2^{\mathsf T}q_0-A_1^{\mathsf T}W
$$
在 $170$ 个纯来源行上等于 $P_2QV-P_1W$；在 $918$ 个一次横向来源
$c^ad^bz_lF_i$、$a+b\le2$ 上等于
$$
R_{(i,a,b,l),k}=(s_2)_i(q_0)_{(a,b+2,l),k},
\tag{2.2}
$$
其中 $s_2$ 是 (1.2) 的系数列。所有其他 $5100$ 个来源至少含两个横向变量，残差在那里严格为零。

## 3. 实际全行校正给三条二阶左延拓

允许二阶校正的全部 $585$ 个目标坐标为
$$
c^ad^bz_j\quad(a+b\le4),\qquad
c^ad^bz_jz_k\quad(a+b\le3,\ 2\le j\le k\le10).
$$
在第 2 节的 $1088$ 个来源行上，分别记
$$
J_0=A_0^{\mathsf T}|_{\text{这 }585\text{ 个目标}},
\qquad
J_1=A_1^{\mathsf T}Q
=\begin{pmatrix}P_1Q\\0\end{pmatrix}.
$$
新原式有理计算给
$$
\operatorname{rank}J_0=578,\qquad
\operatorname{rank}[J_0,J_1]=582,\qquad
\boxed{\operatorname{rank}[J_0,J_1,R]=582.}
\tag{3.1}
$$
最后三列的残差增秩为零。实际构造并逐全部 $1088$ 行验证
$$
J_0H+J_1B+R=0,\qquad
H\in\mathbb Q^{585\times3},\quad B\in\mathbb Q^{7\times3}.
\tag{3.2}
$$
三个常项 leading 坐标准确为 $I_3$。

由此定义
$$
\Lambda(s)=q_0+s(-W+QB)+s^2H.
\tag{3.3}
$$
零阶、一次项分别由 $P_0Q=0$ 和 (2.1) 消失；二次项由 (3.2) 消失。剩余 $5100$ 个原来源上：

- $A_2^{\mathsf T}q_0$ 的输出至少二次横向，而 $q_0$ 只支持一次横向；
- $A_1^{\mathsf T}(-W+QB)$ 的输出至少三次横向；
- $A_0^{\mathsf T}H$ 的输出至少三次横向，而 $H$ 最高二次横向。

故
$$
\boxed{A(s)^{\mathsf T}\Lambda(s)=O(s^3)}
\tag{3.4}
$$
保全部 $6188$ 个原来源。没有把小来源关系假设为完整来源，也不需要排除其他更高横向的可行校正。

若共动矩阵关系为 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，原左列是
$T^{\mathsf T}\Lambda$；这个完整二阶目标转置运输保留，且两侧变换在零点可逆。

## 4. 二十三条独立左延拓给零点三十四阶

第 1 节的二十条纯切向延拓与 (3.3) 的三条延拓有独立常项。因此第三页目标维数至少为二十三。对完整原第一、第二连接的秩，
$$
27-r_1-r_2\ge23,\qquad
\boxed{r_1+r_2\le4.}
\tag{4.1}
$$
对任一真实来源提升 $A_0v_0=0$、
$A_1v_0+A_0v_1=0$，每条左 jet 的系数身份均给
$\lambda_0^{\mathsf T}(A_2v_0+A_1v_1)=0$。所以 (4.1) 确实控制完整连接。

$r_1,r_2$ 分别是十四个正 Smith 指数中等于一、等于二的个数。于是
$$
\begin{aligned}
\delta_{4354,0}
&\ge r_1+2r_2+3(14-r_1-r_2)\\
&=42-r_1-(r_1+r_2)\ge42-4-4=34.
\end{aligned}
\tag{4.2}
$$
同理最小十三个正指数之和至少 $39-4-4=31$，故
$$
\boxed{\delta_{4354,0}\ge34,\qquad \delta_{4353,0}\ge31.}
\tag{4.3}
$$
特别全部原最大子式被 $s^{34}$ 整除。本稿保持 $r_1\le4$ 的正确范围；只有另证 $r_1=4$ 后，(4.1) 才能单独推出 $r_2=0$。

## 5. K80 与同一原来源条件成本

旧其他有限因子及其互异性保持不变。因此
$$
\boxed{
K_{80}=s^{20}K_{60}=s^3K_{77}
=s^{34}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2}
\tag{5.1}
$$
整除全部原最大子式，次数为 $80$，最高系数仍为 $5^6$。
$F_\pm,E_8$ 均是[原公共因子证明](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)
中完全相同的多项式。本稿不称 $K_{80}$ 是完整 gcd。

[无穷远完整第二连接为零](R150-appendix-infinity-full-second-connection-zero-common-order34-and-cost8675.md)
给共同 $34/31$ 阶；结合二十九条完整 Koszul 曲线，原同一指定最大子式、任意原来源换列、cofactor 的阶分别至少 $63,62,59$。新的有限零点阶不再次累加到这些无穷远阶。

保持原 $D=\det A_{I,J}$、总权 $H=8770$、
$\max a_\ell=55$、$\delta_\ell=a_\ell-10$、
$\max\delta_\ell=45$。令
$$
d_*=D/K_{80},\qquad q=\deg d_*.
$$
由同一非零模 $31$ 子式的 $\deg D\ge315$ 和无穷远六十三阶，
$$
\boxed{235\le q\le8770-63-80=8627.}
\tag{5.2}
$$
这里只用旧模 $31$ gcd 次数作次数下界，没有提升其因子。

对原来源列，完整多项式身份为
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{80},
\qquad A_JP_\ell=d_*A_\ell,
$$
且
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-62-80.
\tag{5.3}
$$
明确假定原目标 $b_\nu=h_0t_\nu$ 已有 $\mathbb Q[s]$ 来源，保目标权 $\tau_\nu\le64$。则
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{80}
$$
为多项式；它只使用 cofactor 的五十九阶：
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-59-80.
\tag{5.4}
$$
对所有非基来源除以同一 $d_*$ 并移回基来源后，三类成本为
$$
\begin{aligned}
q-1+45&\le8671,\\
8770+55-62-80-11&=8672,\\
8770+64-59-80-10-235&=8450.
\end{aligned}
\tag{5.5}
$$
所以
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8672.}
\tag{5.6}
$$
目标分支仍是 $8450$：有限因子增加三次与 $q$ 下界降低三恰好抵消。原目标成员性以及指定 $D$ 最高系数的 $31$ 单位性均未由本稿完成。

## 6. 实际计算与复现

[小源码](../notes/2026-11-15-r150-zero-second-normal-envelope-789f.py)
从原 $K,J_2,J_3$ 和全部十七式重建到 $s^2$，回核已付零、一阶矩阵及一阶校正的全部哈希，保真实二阶卷积。其 SHA256 为
c8dde441995f3c9b57728a68ec7b29aa56e9abfbbee280fc334961b64e561403。

实际运行 $43679903558$，步骤 zero-second-normal-envelope，
执行源码提交 eab04908a0a2c4d102ccd0e44a6417a6336c1a4f。
共享数学限额 $30$ 秒，内存限额 $512$ MiB；实际数学用时
$1.5371551719999843$ 秒，退出码 $0$。只新增一个 $1088\times595$ 小矩阵，未重算旧正常形、大 Dixon 或高位模页。

| 对象 | SHA256 |
|---|---|
| 原 $P_2$ | 4c1b4be738601fd7b5ad09117390c2ec4988b60f585886d2153706b824029460 |
| 完整增广矩阵 | 32c631226fea7afa2185c7328c634692608dabb4781fae030806a772a138d096 |
| 全部校正与三列单位 leading 坐标 | a0a1c8d76f023c8d251b2c755f15afccf7798ef2359bed6e833d7d42e4cc5c8d |

三个前缀秩实际为 $578,582,582$，全部 $1088$ 行乘回、其余 $5100$ 原来源的次数消零、完整 $6188$ 来源范围均通过。
原小回执 $3909$ 字节，SHA256 为
7651da121c8f1f894c5c36f657c92d70ce383197caa8e8bddeed0308e1a37448。
[小执行记录](../notes/r150-infinity-remote-session-789f/43679903558-zero-second-normal-envelope.json)
保参数、原矩阵哈希、秩和全部身份标志。可重算的大数组只在实际作业内临时使用。
