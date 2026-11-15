# R150：无穷远第三连接的一维上界、公共四十三阶与条件来源费 8663

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿构造原自然无穷远的二十二条独立三阶左零延拓，证明完整第三连接秩至多一。因此原全部最大子式共同消失至少四十三阶，全部低一阶子式至少三十九阶。结合二十九条原精确 Koszul 曲线及有限 $K_{80}$，同一指定子式给 $72/71/67$ 阶，条件原来源成本为 $8663$。

新增计算只增加原 $u^3$ 系数。它完整回核已付二阶规范，用 $1088\times605$ 的真实有理矩阵构造左延拓；没有重算旧正常形。正的残差增秩只作上界，不证明第三连接恰有秩一。

## 1. 原完整对象及第二页后的维数

取原自然无穷远 $u=1/s$，
$$
A(u)=A_0+uA_1+u^2A_2+u^3A_3+\cdots:
\mathbb Q[[u]]^{6188}\longrightarrow\mathbb Q[[u]]^{4367}.
\tag{1.1}
$$
来源仍是原十七式乘全部次数至多三的单项式。已付完整常数秩为 $4340$，函数域秩为 $4354$，以及
$$
\operatorname{rank}\beta_1=4,\qquad \beta_2=0,
\tag{1.2}
$$
见[原第一连接证明](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)
和[完整第二连接为零](R150-appendix-infinity-full-second-connection-zero-common-order34-and-cost8675.md)。

因此第三页目标维数仍是 $27-4=23$。其完整对偶常项由二十个纯切向泛函和三个已付一次横向泛函组成；它们都有真实二阶左延拓。

保持真实物理反序后的 $K^\sharp$、$v(u)=(1,u,\ldots,u^5)^{\mathsf T}$，以及共动坐标
$$
m_j(u)=\sum_{k=0}^j\binom jk u^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\ (2\le j\le10).
\tag{1.3}
$$
这个变换在全部次数至多三的来源乘子上诱导可逆多项式基变换，并在全部目标上诱导可逆变换。所有下面的原来源身份都在最后作完整转置运输。

## 2. 十个沿全参数恒等的泛函与原三阶纯项

切向平面的完整原身份为
$$
\Gamma(u;c,d,0)=0,\qquad
N(u;c,d,0)=4d^2g(u)v(u)v(u)^{\mathsf T},
$$
$$
g(u)=-2u^2(1-2u)(1+6u).
\tag{2.1}
$$
所以以下十个目标系数泛函，直接以常数泛函沿全参数杀掉原全部来源：
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d.
\tag{2.2}
$$
理由是任何纯输出都有因子 $d^2$；含横向变量的来源不能产生纯输出。无需为 (2.2) 重做第三页校正。

另十个纯切向目标仍按
$$
d^2,\ d^3,\ cd^2,\ d^4,\ cd^3,\ c^2d^2,\
d^5,\ cd^4,\ c^2d^3,\ c^3d^2
\tag{2.3}
$$
排序。加上三个已付横向方向，共十三个二阶左 jet 需要继续。

原三阶纯项可直接核算。写
$$
p_0=K^\sharp e_0=(0,0,0,0,-1,-1)^{\mathsf T},
\qquad
p_1=K^\sharp e_1=(0,0,0,5,5,5)^{\mathsf T}.
$$
由 $g_2=-2,g_3=-8$，
$$
[u^3]\,4g(u)\bigl(v(\zeta)^{\mathsf T}K^\sharp v(u)\bigr)^2
=4g_3p_0(\zeta)^2+8g_2p_0(\zeta)p_1(\zeta)
$$
$$
=80\zeta^7+128\zeta^8+96\zeta^9+48\zeta^{10}.
$$
所以全部十七式按原固定顺序的纯项为
$$
F_3(c,d,0)
=d^2(0,0,0,0,0,0,0,80,128,96,48,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.4}
$$
参数系数采用普通幂级数系数，不含阶乘。

## 3. 固定已付二阶规范及完整第三残差

把上述十三个二阶左延拓合成
$$
\Lambda_0+u\Lambda_1+u^2\Lambda_2.
\tag{3.1}
$$
其中前十列的 $\Lambda_0$ 对应 (2.3)，后三列对应前稿的
$q_0=QV$。全部 $\Lambda_1$ 只支持一次横向目标，$\Lambda_2$ 最高支持二次横向目标。

实际算法按前两稿的同一 RREF 规范重建：

- 十个纯方向的 $[P_0,P_1Q]$ 完整 $170$ 行二阶校正；
- 三个横向方向的 $1088$ 行完整二阶校正；
- 全部 $P_0,P_1,P_2,Q,U,V$、原物理系数与校正哈希。

它未在第三页前重选二阶规范。

第三残差准确为
$$
R_3=A_3^{\mathsf T}\Lambda_0
+A_2^{\mathsf T}\Lambda_1
+A_1^{\mathsf T}\Lambda_2.
\tag{3.2}
$$
仍只需以下全部 $1088$ 个来源行：

- $170$ 个纯来源 $c^ad^bF_i$，$a+b\le3$；
- $918$ 个一次横向来源 $c^ad^bz_lF_i$，$a+b\le2$。

在第二项中，$F_2(c,d,0)$ 乘一次横向来源仍能被 $\Lambda_1$ 读到，这个项完整保留。第三项则使用 $A_1^{\mathsf T}$ 在全部 $585$ 个一次、二次横向目标上的作用，没有删除 $\Lambda_2$ 的二次横向部分。

对其余 $5100$ 个来源，横向次数至少为二。$A_3^{\mathsf T}\Lambda_0$ 和
$A_2^{\mathsf T}\Lambda_1$ 在这些来源上为零，因为它们的目标泛函最高一次横向；$A_1^{\mathsf T}\Lambda_2$ 为零，因为 $F_1$ 自身至少一次横向，乘积至少三次横向。因此 (3.2) 的 $1088$ 行表示精确保留全部来源。

## 4. 第三页实际校正与二十二条独立左 jet

保持前稿同一个
$$
J_0=A_0^{\mathsf T}|_{\text{全部一次、二次横向目标}}
\in\mathbb Q^{1088\times585},
$$
以及
$$
J_1=A_1^{\mathsf T}Q\in\mathbb Q^{1088\times7}.
$$
允许在二阶系数中加任意 $QB$，不改变已付的零至二阶身份；其第三阶贡献是 $J_1B$。三阶校正本身用 $J_0H$。

实际新矩阵为
$$
\mathcal D_3=[J_0,J_1,R_3]\in\mathbb Q^{1088\times605}.
\tag{4.1}
$$
精确有理消元给
$$
\operatorname{rank}[J_0,J_1]=582,\qquad
\boxed{\operatorname{rank}\mathcal D_3=583.}
\tag{4.2}
$$
十三个残差中，前十二个 leading 坐标是自由坐标，最后一个是主元。按单位自由规范，
$$
Z=\begin{pmatrix}I_{12}\\0\end{pmatrix}\in\mathbb Q^{13\times12}.
\tag{4.3}
$$
算法构造并逐全部 $1088$ 行验证
$$
J_0H+J_1B+R_3Z=0,
\quad H\in\mathbb Q^{585\times12},\quad B\in\mathbb Q^{7\times12}.
\tag{4.4}
$$
因此十二个真实左三阶 jet 为
$$
\widetilde\Lambda(u)
=\Lambda_0Z+u\Lambda_1Z
+u^2(\Lambda_2Z+QB)+u^3H.
\tag{4.5}
$$
前三级由已付二阶身份及 $A_0^{\mathsf T}Q=0$ 保持；三级系数由 (4.4) 消失。对其余 $5100$ 个来源，新增 $A_0^{\mathsf T}H$ 至少三次横向，也严格为零。故
$$
\boxed{A(u)^{\mathsf T}\widetilde\Lambda(u)=O(u^4)}
\tag{4.6}
$$
覆盖全部原 $6188$ 来源。

前十二个 leading 方向准确是 (2.3) 的全部十个纯方向和 $Q$ 的前两个横向方向。加上 (2.2)，获得二十二条独立常项。最后一个尚未升起的 leading 方向是原第三个横向方向。这里尚未排除使用更高横向三阶校正将它升起。

如果 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，则原左 jet 为
$T^{\mathsf T}\widetilde\Lambda$。来源乘子变换 $V_{\rm src}$ 和目标变换
$T$ 均在 $u=0$ 可逆，完整三阶运输保留，(4.6) 因而给原自然图的身份。

## 5. 完整第三连接上界与 Smith 下界

对实际满足
$$
A_0v_0=0,\qquad A_1v_0+A_0v_1=0,
$$
$$
A_2v_0+A_1v_1+A_0v_2=0
$$
的来源提升，任一左三阶 jet 给
$$
\begin{aligned}
\lambda_0^{\mathsf T}(A_3v_0+A_2v_1+A_1v_2)
={}&-\lambda_1^{\mathsf T}(A_2v_0+A_1v_1+A_0v_2)\\
&-\lambda_2^{\mathsf T}(A_1v_0+A_0v_1)
-\lambda_3^{\mathsf T}A_0v_0=0.
\end{aligned}
\tag{5.1}
$$
第三页目标维数为 $23$，已有 $22$ 个独立对偶常项杀掉第三连接，所以
$$
\boxed{\operatorname{rank}\beta_{3,\infty}\le1.}
\tag{5.2}
$$
其像只可能沿与 (2.2)、(2.3) 全部纯泛函及前两个横向泛函同时配对为零的那一条线。残差包络的秩一没有给这条线上存在非零真实来源的下界。

原正 Smith 指数中，四个准确为一，没有指数等于二，至多一个等于三，至少九个不小于四。因此
$$
\boxed{\delta_{4354,\infty}\ge4+3+9\cdot4=43,}
\tag{5.3}
$$
$$
\boxed{\delta_{4353,\infty}\ge4+3+8\cdot4=39.}
\tag{5.4}
$$
若第三连接实际为零，以上下界还可增加一；本稿没有预设这个结论。

## 6. 同一指定子式与 K80 来源费

按[完整 Smith—精确 Koszul 因子引理](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)，同一原来源集保二十九条精确形式核曲线常项，删一来源后仍保至少二十八维。故
$$
\boxed{
v_uD_h\ge43+29=72,\quad
v_uD_{{\rm original\ replace},h}\ge43+28=71,\quad
v_uD_{{\rm cofactor},h}\ge39+28=67.}
\tag{6.1}
$$
对任意自然目标换列，只使用 cofactor 的 $67$ 阶，不自动使用原来源换列的 $71$ 阶。

[零点二十三条二阶左延拓](R150-appendix-zero-twenty-three-second-left-jets-factor80-and-cost8672.md)
给同一有限公共因子 $\deg K_{80}=80$。保持原总权 $H=8770$、
$\max a_\ell=55$、$\delta_\ell=a_\ell-10$、$\max\delta_\ell=45$。
令
$$
d_*=D/K_{80},\qquad q=\deg d_*.
$$
原同一子式模 $31$ 非零及完整仿射 gcd 次数 $315$ 只给 $\deg D\ge315$。所以
$$
\boxed{235\le q\le8770-72-80=8618.}
\tag{6.2}
$$

原来源转移仍保持全部输出：
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{80},
\qquad A_JP_\ell=d_*A_\ell,
$$
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-71-80.
\tag{6.3}
$$
明确假定原目标 $b_\nu=h_0t_\nu$ 已有 $\mathbb Q[s]$ 来源，目标权
$\tau_\nu\le64$。成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{80}
$$
为多项式，并有
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-67-80.
\tag{6.4}
$$
对非基来源除以同一 $d_*$ 并移回基来源后，三类成本分别为
$$
\begin{aligned}
q-1+45&\le8662,\\
8770+55-71-80-11&=8663,\\
8770+64-67-80-10-235&=8442.
\end{aligned}
\tag{6.5}
$$
所以
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8663.}
\tag{6.6}
$$
原目标成员性、精确 Smith 阶及指定首系数的 $31$ 单位性仍分别保留为未付问题。

## 7. 已付前两页的 31 局部运输

这里还能安全记录一个有限特征后果。原矩阵按已付 $31$ 单位内容归一定义在
$R=\mathbb Z_{(31)}$ 上。旧完整无穷远证书给常数秩在 $\mathbb Q$ 与
$\mathbb F_{31}$ 中同为 $4340$，第一连接秩在两域中同为 $4$。

先取一个常数 $31$ 单位块作完整 $R[[u]]$ 消元，余块含 $u$。再对其一次系数的四维 $31$ 单位块作消元，可把完整矩阵化成
$$
\operatorname{diag}(I_{4340},\,uI_4,\,u^2C(u))
\tag{7.1}
$$
的矩形形式，全部变换在 $R[[u]]$ 上可逆。

特征零完整 $\beta_2=0$ 意味着 $C(0)=0$ 在 $\mathbb Q$ 中成立。
$C(0)$ 的条目属于 $R$，所以它在 $R$ 中就是严格的零矩阵。于是余块实际含
$u^3$，并得到
$$
\boxed{\beta_{2,\infty,\mathbb F_{31}}=0.}
\tag{7.2}
$$
再记 $C(u)=uD(u)$，$D(0)$ 的特征零秩至多一。因此其全部二阶子式在
$R$ 中为零，约化后也为零，给
$$
\operatorname{rank}_{\mathbb F_{31}}\beta_{3,\infty}\le1.
\tag{7.3}
$$
本段没有把正秩上界提升为等号，也不保证那一个可能的三阶方向在模 $31$ 仍非零。更高阶早页若未证明单位秩一致，不能自动沿用此消元。

## 8. 实际原三阶计算记录

[小源码](../notes/2026-11-15-r150-infinity-third-left-envelope-789f.py)
SHA256 为
eaad9fbcecd3035965de02c9e20e2c4a2372641f3bf6a97a0b99422887bf7d93。
实际运行 $43679903558$，步骤 infinity-third-left-envelope，
执行源码提交 92fabdfdd26102f2ca9de166ec17f5ede9f4b538。

共享数学时限 $30$ 秒、内存上限 $512$ MiB；实际数学用时
$3.3377648440000485$ 秒，退出码 $0$。基块秩 $582$，新增广秩 $583$；
leading 自由坐标准确为 $0,\ldots,11$。全部 $1088$ 行校正、其余 $5100$ 行的横向次数消零和全部 $6188$ 原来源范围均通过。

| 对象 | SHA256 |
|---|---|
| 原 $P_3$ | 04da249f1d140b1f28dbc52aea6638666056dbd7ba7a28050fab84478245ced8 |
| 十三个完整三阶残差 | b40bc66f476d60eb3bd0cabd13e62db4c2532c16644613c40e4f0ef8219ec8d1 |
| 完整 $1088\times605$ 增广矩阵 | 1b3e19c339bc068709ad71a2e355a2545dba00bb4d7ad3735d12867a5c2395f2 |
| 全部三阶校正 | 4a79294dcda661637a4d7ccfb450a03db3b764700a37aab47f26c619f3a9695a |

原临时小回执为 $6576$ 字节，SHA256 为
d6a473ce690e467dd243a0b495c26921457246dcfe9337c1e9bf4f10183f3381。
[小执行记录](../notes/r150-infinity-remote-session-789f/43679903558-infinity-third-left-envelope.json)
保输入哈希、完整二阶规范回核、实际三阶系数、leading 坐标和全部身份标志。可重算矩阵只在作业内临时使用，没有保存大证书或重跑旧模块。
