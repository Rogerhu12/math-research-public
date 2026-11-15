# R150：零点十五条七阶左延拓、K103与条件来源费8621

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

原零点的五条已付六阶左 jet 全部继续延至七阶。新完整校正允许全部4347个非纯目标坐标，并保留最后常核歧义；全部6188原来源实际乘回为零。加上十个沿全参数恒等的纯切向方向，得到十五个独立七阶可延头。

本次给最大、低一阶子式的共同零点阶57、49，有限公共因子为 $K_{103}=s^2K_{101}$，最大正 Smith 指数在8至17之间。结合已经独立证明的指定无穷远阶 $93/90/90$，条件来源费为8621。该结论不等待其他无穷远高页，仍明确以原目标成员性为前提。

## 1. 原参数与完整第七方程

保持原自然参数 $s$、原十七式和全部次数至多三的6188来源，写

$$
A(s)=\sum_{k\ge0}s^kA_k:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
$$

[第六页完整证明](R150-appendix-zero-fifteen-sixth-left-jets-exact-first-four-factor101-and-cost8625.md)
已给五条头独立的真实族

$$
g(s)=\sum_{j=0}^6s^jg_j,\qquad A(s)^{\mathsf T}g(s)=O(s^7).
\tag{1.1}
$$

同稿还精确确定零点第一连接秩4、第二连接秩0，以及共同阶55、48。其完整 cochain 的临时文件及逻辑哈希在本次入口逐项核对，不重新选择原五个头。

共动运输仍是

$$
m_j=\sum_{k=0}^j\binom jk s^{j-k}n_k,\qquad c=n_0,\ d=n_1.
\tag{1.2}
$$

原来源乘子和目标单项式一并运输；$A_{\rm new}=TA_{\rm old}V_{\rm src}$ 时，原目标左 jet 为 $T^{\mathsf T}\lambda_{\rm new}$。

真实第七残差为

$$
R_7=\sum_{i=1}^7A_i^{\mathsf T}g_{7-i}
\in\mathbb Q^{6188\times5}.
\tag{1.3}
$$

本次先逐元素核对实际 $g_1,\ldots,g_6$ 的所有二至五次横向块均为零。随后仍用原式逐行形成 (1.3)，独立核其2295个二次横向、2805个三次横向来源行全部为零。不能只根据上一页的零矩阵哈希删除这些来源。

令 $Q$ 为一次横向目标上的完整七维常左核。它在全部原行满足 $A_0^{\mathsf T}Q=0$；20个纯常核的 $A_1^{\mathsf T}$ 作用也为零。最后常核歧义因此可保为 $Qb$。全部第七延拓方程是

$$
A_0^{\mathsf T}x+A_1^{\mathsf T}Qb+R_7z=0,
\qquad
x\in\mathbb Q^{4347},\quad
b\in\mathbb Q^7,\quad z\in\mathbb Q^5.
\tag{1.4}
$$

此处 $x$ 使用全部非纯目标，未限制为低横向支持。

## 2. 为什么可完整复用二维高齐次空间

第六页已验证的完整中层升列矩阵为

$$
M_{\rm old}\in\mathbb Q^{3769\times9}.
$$

前3762行是三、四、五次横向目标校正，最后7行是其原五阶族的头，记作 $Z_{\rm old}$。本次直接在该完整矩阵上验证

$$
\operatorname{rank}Z_{\rm old}=7,\qquad
\dim\ker Z_{\rm old}=2.
\tag{2.1}
$$

设 $Q_z$ 是其完整 $9\times2$ 核，令

$$
M_{\rm old}Q_z=
\begin{pmatrix}N\\0\end{pmatrix},
\qquad N\in\mathbb Q^{3762\times2}.
\tag{2.2}
$$

第六页的顶层和中层参数化均为原方程全部解的双向参数化。因此令旧头为零所得的 (2.2)，恰是原 $A_0^{\mathsf T}$ 在全部5100个高来源上的**整个**高校正齐次核，不只是两个合法列。本次另核 $N$ 的独立性及全部5100原行产品。

这一步保留了原四、五次横向顶核的三维自由量，并经过已付的完整中层兼容条件消元。它没有因第七高 forcing 为零而直接删除那三维。

设 $C_{\rm old}$ 是第六页完整低右端的九列，$X_{\rm old}$ 是其在原582阶单位块 $U_0$ 上已经验证的解。旧残差中的头项在 $Z_{\rm old}Q_z=0$ 后严格消去，故

$$
C_h=C_{\rm old}Q_z=A_0^{\mathsf T}|_{\rm low}N,\qquad
X_h=X_{\rm old}Q_z,
$$

$$
U_0X_h+(C_h)_I=0.
\tag{2.3}
$$

本次在原未缩放582行再次核 (2.3)。因此两个高齐次列的单位解来自真实旧解的精确线性组合，不重复求解，也不形成任何完整逆。

## 3. 七列新低系统与全部七阶产品

记

$$
B=[J_0,A_1^{\mathsf T}Q]\in\mathbb Q^{1088\times592},
\qquad \operatorname{rank}B=582,
$$

其中 $J_0$ 为585个一、二次横向校正的原低行作用。高齐次核 (2.2) 及五个第七残差进入同一完整低矩阵

$$
M_7=[B,C_h,(R_7)_{\rm low}]
\in\mathbb Q^{1088\times599}.
\tag{3.1}
$$

其常数582阶单位、完整十维常核及逐行比例全部复用；只为五个真实新右端求解。每列恢复原比例后在原单位行乘回，随后保全部1088行作完整 Schur。

实际结果为

$$
\operatorname{rank}M_7=584,\qquad
\dim\ker M_7=15.
\tag{3.2}
$$

完整 Schur 秩为2。低核在原五头上的投影为 $I_5$，五个头全部可升。其零头纤维维数 $15-5=10$，与已付完整第一连接精确秩4给出的 $14-4=10$ 一致。

若实际核系数为 $(x_{\rm lo},b,a,z)$，新第七校正是
$x=x_{\rm lo}+Na$，全部低阶 cochain 与同一个 $z$ 运输：

$$
\lambda(s)=
\sum_{j=0}^{5}s^jg_jz+
s^6(g_6z+Qb)+s^7(x_{\rm lo}+Na).
\tag{3.3}
$$

$A_0^{\mathsf T}Q=0$ 保持0至6阶原身份；第七式恰是 (1.4)。实际最终再次核五列在全部
$6188\cdot5=30\,940$ 个原来源坐标的产品，得到

$$
\boxed{A(s)^{\mathsf T}\lambda(s)=O(s^8).}
\tag{3.4}
$$

本次完整允许四、五次横向校正；它们通过 (2.2) 保在同一个核中。代码没有以它们在某个代表中的数值简化替代完整源空间。

## 4. 共同零点阶57、49及K103

令 $c_j$ 为前 $j$ 个完整连接秩之和。已付十个恒等方向与本次五个独立头合计十五维，故

$$
c_7\le27-15=12.
$$

连同先前各页，

$$
c_1=4,\quad c_2=4,\quad c_3\le5,\quad c_4\le8,\quad
c_5\le10,\quad c_6\le12,\quad c_7\le12.
\tag{4.1}
$$

十四个正 Smith 指数在阈值1至8的计数至少为

$$
14,\ 10,\ 10,\ 9,\ 6,\ 4,\ 2,\ 2.
$$

其和为57；最小十三个正指数的每个计数最多少一，和至少49。因此

$$
\boxed{\delta_{4354,0}\ge57,\qquad
\delta_{4353,0}\ge49.}
\tag{4.2}
$$

原完整模31仿射子式 gcd 的零点阶66只用于特征零上界
$\delta_{4354,0}\le66$。故最大正 Smith 指数满足

$$
a_{\max}=\delta_{4354,0}-\delta_{4353,0}\le66-49=17.
$$

上述第八个阈值计数至少2，所以

$$
\boxed{8\le a_{\max}\le17.}
\tag{4.3}
$$

其余有限因子保持，得到

$$
\boxed{
K_{103}=s^2K_{101}=s^{43}K_{60}
=s^{57}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2.}
\tag{4.4}
$$

次数103，最高系数仍为 $5^6$，整除全部原最大子式；不称其为完整特征零 gcd。原最大子式公共阶的完整上界66和低一阶上界55均未改变。

## 5. 指定无穷远阶93/90/90给条件来源费8621

[所选第二连接精确秩9](R150-appendix-selected-natural-second-connection-exact-nine-from-koszul29-and-cost8623.md)
已经独立给同一指定 $D$、原来源换列、cofactor 的无穷远阶至少 $93,90,90$。
同一子式的非零模31次数8527给 $\deg_{\mathbb Q}D\ge8527$。原总权仍为8770。

置 $d_*=D/K_{103}$、$q=\deg d_*$，则

$$
\boxed{8424=8527-103\le q\le8770-93-103=8574.}
\tag{5.1}
$$

保原最大列权55、来源成本偏移 $\delta_\ell=a_\ell-10$ 及最大偏移45。完整伴随来源转移继续满足

$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{103},\qquad
A_JP_\ell=d_*A_\ell
$$

于全部4367输出，次数界为
$\deg(P_\ell)_j\le8770-a_j+a_\ell-90-103$。

明确以原目标 $h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A$ 为前提，并保 $\tau_\nu\le64$。原非基、基转移、基目标三个成本分支为

$$
\begin{aligned}
q-1+45&\le8618,\\
8770+55-90-103-11&=8621,\\
8770+64-90-103-10-8424&=207.
\end{aligned}
\tag{5.2}
$$

因此

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8621.}
\tag{5.3}
$$

这一层只用已经正式证明的 $93/90/90$。后续无穷远更强界可以另行代入，不影响本条独立结论。

## 6. 原目标配对及实际记录

原目标

$$
t_j(s,m)=\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2
$$

按真实共动运输后是 $n_j^2$。本次八组 $\lambda_0,\ldots,\lambda_7$ 的九平方坐标全部逐项为零；每组 $9\times5$ 逻辑矩阵哈希都是

~~~
0f6dc74c0400d79aae2d5244e774010ffe4eca006549d70d01a20a1cab0b8f90
~~~

因此本族的已存截断左 jet 不给原九目标新的非零配对障碍。这不证明目标成员性，也不把当前包络秩当完整第七连接的秩下界。

[已推小回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-seventh-reused-complete-high-kernel.json)
记载 run43702348535，step zero-seventh-reused-complete-high-kernel，
执行源码提交 e5d636e9d70cbb39d875f86744ad248603b1bc00。
实际数学7.783896052998898秒，墙钟7.887592761999258秒，退出码0；上限180秒、2048MiB。

[完整小源码](../notes/2026-11-15-r150-zero-seventh-reused-complete-high-kernel-789f.py)
为21770字节，SHA256

~~~
b46ca6a4fc594b53687d692986229edc97ca770e21ac6332703eaf998c9e0b67
~~~

| 已验证完整对象 | 形状 | 逻辑SHA256 |
|---|---:|---|
| 第七原残差 | $6188\times5$ | 593d56343ca2b10ac849359c2b2c04f44053c7575e9ae727e0ffe5f97530cf6c |
| 完整低核 | $599\times15$ | fc0a152f8452d13221f26fb7ad1b0c8202ab1ec3f3a7719cdf09b56ee1080caa |
| 全部0至7阶cochain | $13304\times5$ | 39b267e734b93021d1bb668307e7d413280635aeb8fedece8d3d3eb04ae018b8 |

完整 cochain 临时gzip为54547字节，SHA256
f081bc97fce90ec15ef106dc462efc2ffc45fc29422f6891c75d2350dd1df189。
数学绑定为

~~~
9524a1877c1743c8fbe6793c4e41822470011bf68da83e8ee3e12a1fccc4567a
~~~

实际完整小回执34098字节，SHA256

~~~
872fdfc076f21fbfdf53d5edae44f40b35a3a027538a40961d61787b466decec
~~~

所有大对象只作为同作业内临时数组和可续检查点。旧988阶与582阶完整逆均未计算；旧顶、中层消元及旧右端解均未重做。
