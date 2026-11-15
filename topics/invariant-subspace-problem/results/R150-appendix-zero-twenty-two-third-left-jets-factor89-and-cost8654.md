# R150：零点二十二条三阶左延拓、公共因子 K89 与条件来源费 8654

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿在原有限参数 $s=0$ 构造二十二条常项独立、保全部原来源的三阶左零延拓。完整前三连接的秩满足
$r_1+r_2+r_3\le5$；结合已付 $r_1\le4$ 和 $r_1+r_2\le4$，原全部最大子式在零点共同消失至少四十三阶，低一阶子式至少三十九阶。

有限公共因子因此提高为 $K_{89}=s^{29}K_{60}$。结合已付原无穷远指定 $72/71/67$ 阶，同一来源的条件成本为 $8654$。本稿不假定零点 $r_1=4$，也不单独宣称零点 $r_2=0$ 或 $r_3\le1$。

## 1. 原完整图与同一二阶规范

保持原十七式、次数至多三的全部来源，以及自然参数 $s$：
$$
A(s)=A_0+sA_1+s^2A_2+s^3A_3+\cdots:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
\tag{1.1}
$$
其常数秩为 $4340$，函数域秩为 $4354$。因此常数余空间维数为 $27$，有十四个正 Smith 指数，见
[原零点完整秩证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)。

使用原 $K$，不作无穷远反序；真实均值为
$y(s)=(1,s,\ldots,s^5)^{\mathsf T}$。共动坐标为
$$
m_j=\sum_{k=0}^j\binom jk s^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\quad(2\le j\le10).
\tag{1.2}
$$
来源和目标都采用这个变换在全部原单项式上的完整诱导。

[二十三条二阶左延拓](R150-appendix-zero-twenty-three-second-left-jets-factor80-and-cost8672.md)
已给
$$
r_1\le4,\qquad r_1+r_2\le4.
\tag{1.3}
$$
其中二十个常项是纯切向目标系数泛函，另外三个是一次横向泛函
$q_0=QV$。这里
$$
P_0Q=0,\qquad
Q\in\mathbb Q^{135\times7},\qquad
P_0W=P_1QV,
$$
$P_i$ 是原 $170\times135$ 一次横向矩阵，且 $V$ 保前稿同一个三维常项规范。

本次只增加原 $s^3$ 系数。算法重建并逐哈希核对已付 $P_0,P_1,P_2$、全部原物理映射、两组二阶校正及其 RREF 规范，没有在第三页前更换二阶延拓。

## 2. 十个恒等方向与原三阶纯项

原切向平面满足完整身份
$$
\Gamma(s;c,d,0)=0,\qquad
N(s;c,d,0)=4d^2g(s)y(s)y(s)^{\mathsf T},
\qquad
g(s)=-2s^2(s-2)(s+6).
\tag{2.1}
$$
因此
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d
\tag{2.2}
$$
这十个目标泛函沿全参数直接杀掉原全部来源。所有纯输出都有 $d^2$ 因子，含横向变量的来源不能产生纯输出。

其余十个纯方向按
$$
d^2,d^3,cd^2,d^4,cd^3,c^2d^2,
d^5,cd^4,c^2d^3,c^3d^2
\tag{2.3}
$$
排序。与三个 $q_0$ 方向合成十三条已付二阶左 jet：
$$
\Lambda_0+s\Lambda_1+s^2\Lambda_2.
\tag{2.4}
$$
$\Lambda_1$ 只支持一次横向目标，$\Lambda_2$ 最高二次横向。

三阶纯系数可直接由原 (2.1) 求得。记
$$
p_0(\zeta)=5\zeta^4-\zeta^5,\qquad
p_1(\zeta)=-32\zeta^3+5\zeta^4-\zeta^5.
$$
由于 $g_2=24,g_3=-8$，
$$
[s^3]\,4g(s)\bigl(y(\zeta)^{\mathsf T}K y(s)\bigr)^2
=4g_3p_0^2+8g_2p_0p_1
$$
$$
=-30720\zeta^7+10144\zeta^8-1600\zeta^9+160\zeta^{10}.
\tag{2.5}
$$
因此按 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 原顺序，
$$
F_3(c,d,0)=
d^2(0,0,0,0,0,0,0,-30720,10144,-1600,160,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.6}
$$
这里使用普通幂级数系数，不混入阶乘。

## 3. 完整第三残差与实际有理校正

第三残差为
$$
R_3=A_3^{\mathsf T}\Lambda_0+
A_2^{\mathsf T}\Lambda_1+
A_1^{\mathsf T}\Lambda_2.
\tag{3.1}
$$
它只可能支持以下 $1088$ 个原来源：

- $170$ 个纯来源 $c^ad^bF_i$，$a+b\le3$；
- $918$ 个一次横向来源 $c^ad^bz_lF_i$，$a+b\le2$。

原二阶纯项乘一次横向来源后仍可被 $\Lambda_1$ 读到；(3.1) 的第二项保留该贡献。第三项保留 $\Lambda_2$ 的全部二次横向目标。

令
$$
J_0=A_0^{\mathsf T}|_{\text{全部 }585\text{ 个一次、二次横向目标}},
\qquad
J_1=A_1^{\mathsf T}Q=\begin{pmatrix}P_1Q\\0\end{pmatrix}.
$$
实际精确有理计算给
$$
\operatorname{rank}[J_0,J_1]=582,\qquad
\operatorname{rank}[J_0,J_1,R_3]=583.
\tag{3.2}
$$
十三个 leading 坐标中，前十二个准确为自由坐标。令
$$
Z=\begin{pmatrix}I_{12}\\0\end{pmatrix}.
$$
算法构造并逐全部 $1088$ 行验证
$$
J_0H+J_1B+R_3Z=0,\qquad
H\in\mathbb Q^{585\times12},\quad B\in\mathbb Q^{7\times12}.
\tag{3.3}
$$
于是
$$
\widetilde\Lambda(s)=
\Lambda_0Z+s\Lambda_1Z+
s^2(\Lambda_2Z+QB)+s^3H
\tag{3.4}
$$
为十二条真实三阶左零延拓。

对其余 $5100$ 个原来源，乘子至少二次横向。$A_3^{\mathsf T}\Lambda_0$ 和
$A_2^{\mathsf T}\Lambda_1$ 因泛函最高一次横向而为零；
$A_1^{\mathsf T}\Lambda_2$ 因 $F_1$ 至少一次横向、泛函最高二次横向而为零；
$A_0^{\mathsf T}H$ 同理由 $F_0$ 至少一次横向而为零。因此
$$
\boxed{A(s)^{\mathsf T}\widetilde\Lambda(s)=O(s^4)}
\tag{3.5}
$$
覆盖全部 $6188$ 个原来源，未假定任何小来源关系可升成完整来源。

若共动矩阵为 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，原左 jet 为
$T^{\mathsf T}\widetilde\Lambda$。目标转置和来源变换的全部三阶项都保留，且在零点可逆，故 (3.5) 是原自然参数的身份。

十二个 leading 常项准确为 (2.3) 的十个纯方向与前两个横向方向。再加 (2.2)，得到二十二个独立常项。小包络的正增秩只提供上界；更高横向校正是否可升起剩余方向，未由本次计算判定。

## 4. 不假定零点第一页等号的 Smith 估计

设完整原前三连接的秩为 $r_1,r_2,r_3$。二十二个独立三阶左 jet 给
$$
27-r_1-r_2-r_3\ge22,\qquad
\boxed{r_1+r_2+r_3\le5.}
\tag{4.1}
$$
这是完整连接的上界：对任何满足真实零、一、二阶来源提升方程的
$(v_0,v_1,v_2)$，逐左 jet 系数身份使
$\lambda_0^{\mathsf T}(A_3v_0+A_2v_1+A_1v_2)=0$。
没有以包络秩代替真实来源的下界。

$r_j$ 是正 Smith 指数恰等于 $j$ 的个数。由 (1.3)、(4.1)，
$$
\begin{aligned}
\delta_{4354,0}
&\ge r_1+2r_2+3r_3+4(14-r_1-r_2-r_3)\\
&=56-r_1-(r_1+r_2)-(r_1+r_2+r_3)\\
&\ge56-4-4-5=43.
\end{aligned}
\tag{4.2}
$$
对最小十三个正指数，同式的 $56$ 换成 $52$，给
$$
\boxed{\delta_{4354,0}\ge43,\qquad\delta_{4353,0}\ge39.}
\tag{4.3}
$$
尤其全部原最大子式被 $s^{43}$ 整除。这里只有累计秩界；
单独的 $r_1=4$、$r_2=0$、$r_3\le1$ 均没有从零点小包络冒推出去。

## 5. K89 及完整原来源条件成本

其他有限因子保持不变，故
$$
\boxed{
K_{89}=s^{29}K_{60}=s^9K_{80}
=s^{43}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2}
\tag{5.1}
$$
整除全部原最大子式。其次数为 $89$，最高系数仍为 $5^6$。
$F_\pm,E_8$ 是[原公共因子证明](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)
中同一批多项式；(5.1) 不称完整 gcd。

[无穷远第三页](R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)
及[完整 Smith—精确 Koszul 引理](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)
已经给原同一指定子式 $D$、原来源换列、cofactor 的自然无穷远阶分别至少
$72,71,67$。有限零点新阶不再次累加到这些无穷远阶。

保持 $H=8770$、$\max a_\ell=55$、
$\delta_\ell=a_\ell-10$、$\max\delta_\ell=45$。令
$$
d_*=D/K_{89},\qquad q=\deg d_*.
$$
原同一子式模 $31$ 非零及旧仿射 gcd 的次数 $315$ 仅给 $\deg D\ge315$，故
$$
\boxed{226\le q\le8770-72-89=8609.}
\tag{5.2}
$$
原来源转移多项式为
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{89},
\qquad A_JP_\ell=d_*A_\ell,
$$
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-71-89.
\tag{5.3}
$$
明确假定原目标 $b_\nu=h_0t_\nu$ 属于
$\operatorname{im}_{\mathbb Q[s]}A$，且原目标权 $\tau_\nu\le64$。成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{89}
$$
为多项式；目标只用 cofactor 的 $67$ 阶，给
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-67-89.
\tag{5.4}
$$
对非基来源除以同一 $d_*$ 并移回原基来源后，完整三类成本为
$$
\begin{aligned}
q-1+45&\le8653,\\
8770+55-71-89-11&=8654,\\
8770+64-67-89-10-226&=8442.
\end{aligned}
\tag{5.5}
$$
因此
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8654.}
\tag{5.6}
$$
目标分支仍是 $8442$：有限因子的次数增加九，与 $q$ 的下界降低九恰好抵消。原目标成员性、真实端点精确 Smith 指数、指定 $D$ 最高系数的 $31$ 单位性仍未由本稿完成。

## 6. 实际执行与可复现参数

[小源码](../notes/2026-11-15-r150-zero-third-left-envelope-789f.py)
SHA256 为
b073a5b465aaecbe0a4c8382113c8759fac313ea0ca6ec2ca19abf853a7b46df。
实际运行 $43679903558$，步骤 zero-third-left-envelope，
执行源码提交 efcd0941eaea2392f60dbf935f2a9a56bada2872。

共享数学时限 $30$ 秒，实际内存限额 $512$ MiB；
数学用时 $4.390881418003119$ 秒，退出码 $0$。
两个前缀秩为 $582,583$，leading 自由坐标为 $0,\ldots,11$；
全部 $1088$ 校正行、其余 $5100$ 行次数消零和完整 $6188$ 来源均通过。

| 对象 | SHA256 |
|---|---|
| 原 $P_3$ | 9149b9496dd202cd4882a181cca2800c3303cedc089bf8cf38426611a9f60fe3 |
| 十三个完整三阶残差 | 611efac9c23fc0abeacefecca21cc9eaee9890530b9cdc95e0c2769bbd13e2e6 |
| 完整 $1088\times605$ 增广矩阵 | f44c39eea14d1f0087dc20b4f2627667ce265cca1cf34fc19cee0fe13d5ecb91 |
| 全部三阶校正 | 6dcaf5a433aab32a30be647b7e6eac86d31d9854e4805d0136c47a11aa17a2e1 |

原小回执 $6801$ 字节，SHA256 为
ef518460e9a311da48e71eb3b11a8aad1feaad7aa38ac0678c46558f57750315。
[执行记录](../notes/r150-infinity-remote-session-789f/43679903558-zero-third-left-envelope.json)
保原参数、所有二阶规范哈希、三阶全行校正及 leading 坐标。
可重算的大矩阵只在作业内临时使用，没有重算旧正常形或大模页。
