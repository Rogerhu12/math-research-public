# R894：七项原常数域共轭极除子的有界聚合、完整主函数与下降资料

日期：2026-11-16。状态：**完整纸面执行证明；本篇的聚合翻转尚未运行。** 原七个 A/B 输入已经实际完成；原第零个 D*、共同 C*、固定 Dχ 和原 t 首项已经实际完成，另外六个 D* 的新消费者已经激活。本篇给它们完成之后的一个确定后继，不把输入任务的启动或本篇的18次操作计数写成实际输出。

此处的七项运算是原常数域扩张 $L/K$ 的 Galois 共轭极除子之和。它不是 R873/R876 的曲线 Hecke 对应范数；后者的两投影、八维对应环、九个截面范数与原 dual7 不在本篇更换。

## 1. 原对象、原七项和需要保留的等式

固定原 $Y/K$、$K=\mathbb Q(\zeta)$、$L=K(b)$、$\gamma\in\operatorname{Gal}(L/K)$。所有曲线、原正常基、$\tau,\sigma$、原 $P_0$、$H=\operatorname{div}(\tau)$、$\deg H=272$、$g(Y)=127$ 保持不变。原 $\tau(P_0)\ne0$，所以这个具体 $H$ 避开 $P_0$。

记原七个有效、次数272且避开 $P_0$ 的除子为
$$
\mathscr D_j=\gamma^jD^*,\qquad 0\le j\le6,
$$
并记共同原输入
$$
\mathscr C=C^*,\qquad \mathscr X=D_\chi.
\tag{894.1}
$$
$\mathscr C,\mathscr X$ 在 $K$ 上定义。$\mathscr D_j$ 的完整空间必须是原同一固定图的共轭
$$
W_{\mathscr D_j}=H^0(Y_L,3H-\mathscr D_j)\subset V_3(L),
\qquad\dim W_{\mathscr D_j}=418.
\tag{894.2}
$$
不能另选同类除子或换自由坐标后仍称其为原共轭。

原七根轨道证书给 $\gamma$ 次数 $0,1,\ldots,6$ 对应的实际整数分支次序
$$
(0,6,1,2,4,3,5).
\tag{894.3}
$$
此表只用于原剩余嵌入的来源映射；后继应读取并验证该证书，不能把按大小排序的模根当作 Galois 次序。原原型仍是 free1186 等于1、其余自由坐标为0。

对每个准确除子 $A$ 记 $x_A=A-H$。R887 与六 D* 方法给的是完整除子等式
$$
E_j-1206P_0=-x_{\mathscr C}+3x_{\mathscr D_j}
       +4x_{\mathscr X}+\operatorname{div}\widetilde Q_j,
\qquad E_j=E_{\gamma^jf}.
\tag{894.4}
$$
原 $\gamma^j$ 作用于整个单位解表达式及函数，不能只替换椭圆常数 b。将 $\gamma^jf$ 的靶曲线按原 $\rho_j$ 相位同构回原靶时，非零常数相位不改变 y 函数的极除子；这不是三同源实下降。相位仍不能在 $\widetilde Q_j$ 或原帧中随意删去。

具体主函数仍为
$$
\widetilde Q_j=
 \frac{(a_j/v_j)^3\,(u_C/\tau^2)}
      {(u_\chi/\tau^2)^4}.
\tag{894.5}
$$
这里 $a_j,v_j$ 都是原 V3 截面，同权比 $a_j/v_j$ 不添尺度。$u_C,u_\chi$ 是已成原 V2 截面；已有 $82$、$\lambda$、content 和原核归一化都只出现一次。

设
$$
S=\sum_{j=0}^6 x_{\mathscr D_j},\qquad
T=-x_{\mathscr C}+4x_{\mathscr X},\qquad
Q_{\rm orb}=\prod_{j=0}^6\widetilde Q_j.
\tag{894.6}
$$
逐个相加 (894.4)，严格得到
$$
\boxed{\mathcal T_f:=\sum_{j=0}^6E_j-8442P_0
        =3S+7T+\operatorname{div}Q_{\rm orb}.}
\tag{894.7}
$$
$Q_{\rm orb}$ 是原函数的整个常数域范数，属于 $K(Y)^\times$。这句不把辅助素点的七个数值乘积冒称已经展开的特征零范数系数。

本篇要产生一个实际有效、次数272且避开 $P_0$ 的 $D_N$、完整 $W_{D_N}$，以及准确原函数 $\mathcal Q_N$，使
$$
\boxed{\mathcal T_f=(D_N-H)+\operatorname{div}\mathcal Q_N.}
\tag{894.8}
$$
$D_N$ 可在 $L$ 上定义。它不因左边是 $K$ 定义就自动是 $K$ 定义；第6节给原线丛的准确下降资料。

## 2. 只消费已经规定完整出口的同一个 flip

本篇使用 R872 §§7–8、R890 §§2–3 的完整操作
$$
A_3=\operatorname F(A_1,A_2).
$$
每个输入须有原正常 V3 坐标的完整418空间，且两个实际有效除子都避开 $P_0$。操作须实际完成下列对象，不能只选一条截面便视为一次完成的 flip：

1. 完整乘法像 $H^0(6H-A_1-A_2)$，维962；
2. 原 $\tau^3,\sigma^3$ 两锚截下的完整
   $U=H^0(3H-A_1-A_2)$，维146；
3. 一个未重新缩放的实际 $u\in U$，满足 $(u/\tau^3)(P_0)\ne0$；
4. 同一完整 U 内两锚的真实962秩、完整关系核和第二块投影；
5. 完整 $W_{A_3}=H^0(3H-A_3)$，维418。

原函数及准确除子关系为
$$
q=u/\tau^3,\qquad
\operatorname{div}_{3H}u=A_1+A_2+A_3,
$$
$$
x_{A_1}+x_{A_2}+x_{A_3}=\operatorname{div}q,\qquad
q(P_0)\ne0.
\tag{894.9}
$$
特别地，$A_3$ 有效、次数272且避开 $P_0$。因此这一性质在本篇所有节点归纳保持。

原七个完整272维纤维可直接沿 R890 的1904行接口执行；既有 W、Krylov逆、正常评价和实际已成乘积阶段按来源身份复用。保留非约化 Artin 因子，不取每个纤维的一个点。

每个新 flip 仍须有真实962像、1884×690余项的544秩/146核，以及完整两锚关系和418投影。只有它们全部完成，节点才可用于下一步。有限试次或预算未成只给部分终点，不据线丛全局生成的存在性预填一个模单位或成功核。

## 3. 18个明确节点；有两项原产物时只新增16个

下表的“类向量”指原度零除子在模主除子后的系数；第4节同时维护准确主函数，不能只核这个表。

先聚合七个 $\mathscr D_j$。固定按原 $\gamma$ 次数编号，使用以下六个节点：
| 节点 | 调用 | 类向量 |
|---|---|---|
| $A_1$ | $\operatorname F(\mathscr D_0,\mathscr D_1)$ | $-x_{\mathscr D_0}-x_{\mathscr D_1}$ |
| $A_2$ | $\operatorname F(\mathscr D_2,\mathscr D_3)$ | $-x_{\mathscr D_2}-x_{\mathscr D_3}$ |
| $A_3$ | $\operatorname F(A_1,A_2)$ | $\sum_{j=0}^3x_{\mathscr D_j}$ |
| $A_4$ | $\operatorname F(A_3,\mathscr D_4)$ | $-\sum_{j=0}^4x_{\mathscr D_j}$ |
| $A_5$ | $\operatorname F(\mathscr D_5,\mathscr D_6)$ | $-x_{\mathscr D_5}-x_{\mathscr D_6}$ |
| $A_6$ | $\operatorname F(A_4,A_5)$ | $S$ |

这里用了两次四项和恒等式
$\operatorname F(\operatorname F(A,B),\operatorname F(C,D))$ 代表四个输入类之和。
它不要求中间有效除子不相交；全部重数由同一个完整 flip 保留。

接着用三个节点取得 $-3S$：
| 节点 | 调用 | 类向量 |
|---|---|---|
| $A_7$ | $\operatorname F(A_6,A_6)$ | $-2S$ |
| $A_8$ | $\operatorname F(A_7,H)$ | $2S$ |
| $A_9$ | $\operatorname F(A_8,A_6)$ | $-3S$ |

共同固定部分用八个节点取得 $-7T$：
| 节点 | 调用 | 类向量 |
|---|---|---|
| $B_1$ | $\operatorname F(\mathscr X,\mathscr X)$ | $-2x_{\mathscr X}$ |
| $B_2$ | $\operatorname F(B_1,B_1)$ | $4x_{\mathscr X}$ |
| $B_3$ | $\operatorname F(\mathscr C,H)$ | $-x_{\mathscr C}$ |
| $B_4$ | $\operatorname F(B_3,B_2)$ | $x_{\mathscr C}-4x_{\mathscr X}=-T$ |
| $B_5$ | $\operatorname F(B_4,B_4)$ | $2T$ |
| $B_6$ | $\operatorname F(B_5,B_5)$ | $-4T$ |
| $B_7$ | $\operatorname F(B_6,B_4)$ | $5T$ |
| $B_8$ | $\operatorname F(B_7,B_5)$ | $-7T$ |

最后一个节点为
$$
D_N=\operatorname F(A_9,B_8),\qquad
x_{D_N}\equiv3S+7T.
\tag{894.10}
$$
所以完整树有 $6+3+8+1=18$ 次 flip。这只是明确上界，不声称是最短链。

$B_1,B_2$ 正是原 R890 固定链中标作 D、E 的两个节点。若它们已经有可读、原字节可绑定的完整418输出和原 q/累计主函数，须直接消费；这时新增节点数是 $18-2=16$。不是仅见到 R890 的请求、过程名或部分乘积就扣除这两次。

实际复用还必须固定：

- 原 $\mathscr X$ 的 producer、配置、完整 normal418 及原 P0 标记；
- 原 $\operatorname F(\mathscr X,\mathscr X)$ 和 $\operatorname F(B_1,B_1)$ 的准确选列、未缩放 q、全部关系及完整418；
- 原累计函数中重复输入保两次，不能把平方因子去掉；
- 来源字节/SHA 与本次新 tag 明确分开，不能改旧 stage 配置冒作新生产。

本篇不需要先对另外六个 $E_j$ 分别执行 R890 的整套八步，再把七个结果相加。这里直接聚合 (894.7) 的同一原输入；第零个 $E_f$ 的已成结果仍原样保留，既不撤销也不重算。

## 4. 每个节点的准确函数递推

对每个节点 A 保存准确恒等式
$$
\kappa_A=x_A+\operatorname{div}F_A,
\tag{894.11}
$$
其中 $\kappa_A$ 是上表中由原 $x_{\mathscr D_j},x_{\mathscr C},x_{\mathscr X}$ 组成的准确度零除子。初始输入取 $F=1$，只表示它们自身的恒等表达，并未把任一所选截面或帧值缩放成1。

若 $A=\operatorname F(B,C)$ 的原函数为 $q_A$，由 (894.9) 得
$$
\boxed{\kappa_A=-\kappa_B-\kappa_C,\qquad
F_A=(q_AF_BF_C)^{-1}.}
\tag{894.12}
$$
这是真正的除子等式，不仅是 Jacobian 中的加法。若 $B=C$，分母含 $F_B^2$；若原节点从 R890 复用，必须同时接其原 $F_A$，不能仅导入一个418矩阵后把 F 重置为1。

令最终节点累计函数为 $F_N$。表中逐步 (894.12) 给
$$
3S+7T=(D_N-H)+\operatorname{div}F_N.
$$
于是准确出口为
$$
\boxed{\mathcal Q_N=Q_{\rm orb}F_N.}
\tag{894.13}
$$
式 (894.7) 立即给 (894.8)。在原 $I_D=\mathcal O(-D)$ 约定下，
$$
\boxed{I_{\mathcal T_f}
=\mathcal Q_N\,I_{D_N}\,I_H^{-1}.}
\tag{894.14}
$$
主函数是正乘，不是其逆。这条式子保整个原七项 pole divisor；未把 $E_f$ 换成三同源后的 $E_{f_R}$ 或仅一个代表类。

每条函数 DAG 记录两个父来源、原 $u/\tau^3$、选行求解的原矩阵身份以及准确整数幂。它可以保为 unit-solve 表达式，不要求先展开全部特征零坐标；实际模数组与准确表达式必须分别标记。

## 5. 原 P0 单位、完整首项及原 t 框架

每个新 q 在 $P_0$ 都是实际未缩放单位，因此
$$
F_A(P_0)=
  \bigl(q_A(P_0)F_B(P_0)F_C(P_0)\bigr)^{-1}.
\tag{894.15}
$$
等式使用原 $P_0$，包括重复因子。不得以另一个点上的单位或有限域元素的形式非零代它。

沿原 $\rho=z-z_0$，每个输入的准确首项是
$$
\widetilde Q_j=\lambda_j\,\rho^{-1205}(1+O(\rho)),
\qquad
\lambda_j=
 \frac{a_j(P_0)^3\,u_{C,252}}
      {v_{j,123}^3\,u_{\chi,272}^4}.
\tag{894.16}
$$
这里 $a_j(P_0)$ 表示其原 $\tau^3$ 帧值；$v_{j,123}$、$u_{C,252}$、$u_{\chi,272}$ 是各自原帧下的实际系数。共同 $\lambda$ 的域缩放、原 content、$82$ 及首列自由坐标都不另插一次。式中的符号 $\lambda_j$ 仅表示本行首项，不替代原数域的缩放常数。

由 (894.13)–(894.16)，
$$
\operatorname{ord}_{P_0}\mathcal Q_N=-8435,
\qquad
L_N=F_N(P_0)\prod_{j=0}^6\lambda_j.
\tag{894.17}
$$
阶数也可由 (894.8) 直接核对：每个原 $E_j(P_0)=1$，左边的 P0 系数是 $7-8442=-8435$；右边 $D_N,H$ 都避开 $P_0$。

R883 已准确给原 $t=c\rho+O(\rho^2)$ 及 $c^{1205}$。因此原 t 首项为
$$
\boxed{\mathcal Q_N
 =\left(L_Nc^{8435}\right)t^{-8435}(1+O(t)),
 \qquad c^{8435}=(c^{1205})^7.}
\tag{894.18}
$$
这是正乘；不需要重新求原 t、旧273 jets 或另一个 $c^{8435}$ 来源。代码只新增同一已成标量节点的第七幂，保其准确源。

$F_N(P_0)$ 可属于 L，故最终首项不被预先宣称在 K；它和第6节的新平凡化下降资料相容。辅助素点的单位不声明为原41处或所有非 p 处的单位，也不删去原高度的非 p 项。

## 6. 非对称树的最终除子及准确 Galois 下降

输入七项之和与 $Q_{\rm orb}$ 都在 K 上，但上表依次选择中间截面的树不对 Galois 对称。故不能从其类在 K 上就称 $D_N$ 本身在 K 上，或因模数组由整数写出就称其为 Q-fixed。

对 (894.8) 作用原 $\gamma$，因 $\mathcal T_f,H$ 固定，
$$
(D_N-H)+\operatorname{div}\mathcal Q_N
=(\gamma D_N-H)+\operatorname{div}(\gamma\mathcal Q_N).
$$
于是
$$
\boxed{\operatorname{div}
 \left(\frac{\gamma\mathcal Q_N}{\mathcal Q_N}\right)
 =D_N-\gamma D_N.}
\tag{894.19}
$$
所以原完整空间 $W_{D_N}=H^0(3H-D_N)$ 上有准确半线性作用
$$
\boxed{
\mathcal D_\gamma(s)=
  \frac{\gamma\mathcal Q_N}{\mathcal Q_N}\,\gamma(s).}
\tag{894.20}
$$
若 $s$ 消于 $D_N$，则 $\gamma(s)$ 消于 $\gamma D_N$；再乘 (894.19) 的函数，正好恢复消于 $D_N$。$3H$ 固定，故没有漏掉无穷图条件或额外极点。这同时验证了比值方向。

七次迭代的乘子准确望远镜：
$$
\prod_{i=0}^{6}
 \gamma^i\!\left(\frac{\gamma\mathcal Q_N}{\mathcal Q_N}\right)
 =\frac{\gamma^7\mathcal Q_N}{\mathcal Q_N}=1.
\tag{894.21}
$$
故 $\mathcal D_\gamma^7=1$，满足原有限 Galois 下降条件。正乘 $\mathcal Q_N$ 识别
$$
\mathcal Q_N W_{D_N}
 =H^0(2H-\mathcal T_f)\otimes_K L,
\tag{894.22}
$$
并将 (894.20) 变成左边原嵌入函数的通常 $\gamma$ 作用。该空间次数544、维418；保持的是原 K 上线丛，不是另选一个有利的 Picard 类。

因为 $Q_{\rm orb}$ 在 K 上，(894.20) 的乘子也可写成 $\gamma F_N/F_N$；这仅在保留完整原 $Q_{\rm orb}$ 身份后使用，不是删掉其极除子或帧。

本篇明确区分三件事：

- (894.19)–(894.22) 给准确下降资料和原 K 线丛；
- 新18节点若实际完成，给一个指定 L 平凡化中的完整 normal418；
- 将半线性作用实际写成矩阵并求 K-fixed 基是另一项可消费运算，未在本篇假称已经执行。

此处仅是 $\operatorname{Gal}(L/K)$，不替代原 $c_Y$ 的 K/Q 半线性作用。不得将整个函数上的 $\gamma$ 偷换成有限域常数的恒等作用，也不把 $C^*$ 的 K-fixed 性误读为 Q-fixed。

## 7. 对原五个 Lj 的共享输入作用

设后继对原每个 $g_j$ 得到相同类型的准确出口
$$
\mathcal T_{g_j}:=\sum_{\gamma}E_{\gamma g_j}
       -7\deg(E_{g_j})P_0
=(D_{N,j}-H)+\operatorname{div}\mathcal Q_{N,j}.
\tag{894.23}
$$
本篇不预填这些新的完整 RR 空间；它们来自 R893 的原和同态初始源及后续完整有界算术，而不是 CM 点值、另一组候选函数或本篇的 f 聚合。

原整数 $p_j,q_j$ 满足 $q_j\deg E_{g_j}=p_j\deg E_f$。因此原 R849 的同一个
$$
Z_j=q_j\sum_\gamma E_{\gamma g_j}
        -p_j\sum_\gamma E_{\gamma f}
$$
恰为
$$
Z_j=q_j(D_{N,j}-H)-p_j(D_N-H)
  +\operatorname{div}
       \left(\frac{\mathcal Q_{N,j}^{\,q_j}}
                    {\mathcal Q_N^{\,p_j}}\right).
\tag{894.24}
$$
对应嵌入理想的共享入口是
$$
\boxed{
I_{Z_j}=
 \frac{\mathcal Q_{N,j}^{\,q_j}}{\mathcal Q_N^{\,p_j}}\,
 I_{D_{N,j}}^{q_j} I_{D_N}^{-p_j} I_H^{p_j-q_j}.}
\tag{894.25}
$$
每个 j 直接引用同一份本篇终点；不重复计算 f 的七项 trace 或另一个帧版本。原 $\mathscr L_j=I_{Z_j}$、$\eta$ 的负号与 $1/q_j$、$\kappa/R$、theta 二挠比较及完整非 p 项保持原来源。式 (894.25) 不用 $\mathscr L_j^3$ 代替它。

从这些输入到128/144两权空间，继续用 R872 的完整有界类算术、18行条件和两图证书。本篇没有宣称这两个新核或 Hecke 活跃支持/连接/高度已算。

## 8. 新消费者必须记录的来源与断点

直接数学输入为：

1. 原第零支 R880 完整 $W_{D^*}$、$\widetilde Q_0$ 来源及首项；
2. 六 D* producer 实际完成的六个完整418/原函数/首项，按原七次轨道排列；
3. R887 共同 $C^*$、$u_C$，R872 固定 $D_\chi$、$u_\chi$；
4. 原七个已成 cyclic 节点和同一个 normal V3/原 P0 评价；
5. 原 R883 的 $c^{1205}$ 准确节点及实际模值；
6. 若已完成且来源可读，R890 的 $B_1,B_2$ 完整产物、全部函数父节点和单位值。

完整 source audit 应固定原 prime $1000000753$、$\zeta=549966761$、$s=99932770$、原 normal 次序和输入轨道，并明确原件与续载运输的两层身份。某个新节点所需数据未实际发布时保 pending，不因该 producer 正在运行而伪造一个输出 SHA。

新 producer 依依赖 DAG 原子保存每个 flip 的产品增量、真实像/余项/完整核、P0 单位与两锚认证、完整418、函数和未缩放单位值。恢复时直接读取已完成节点，不能因不同队列位置重算同一 $q$、共同评价或乘积块。

最终证书至少分别给：

- 原七个共轭输入完整且次序准确；
- 本篇所需18节点的完成清单，其中哪些引用原 R890；
- 指定 $3S+7T$、准确 (894.8)/(894.14)、完整终点418；
- 原 $\rho$ 阶 −8435 与原 t 首项的完整来源；
- 准确下降资料 (894.19)–(894.22)；
- 是否真正执行了 K-fixed 基、五个 Lj128/144、Hecke支持或高度。

任何未执行项都不得借其他项的成功改成 true。实际 new flip 数必须来自保存的节点清单，不能直接把18或16抄成真实运算次数。

## 9. 既有六 D* 来源计数的文字勘误

旧六 D* 证明 §8(2) 的“G/Γ 的两份 tau 索引与各16块”有来源计数笔误，应为：

**每个算子17块，每块至多16行，覆盖原0至271行；两个算子共34块。**

实际冻结 core、request 和 R827-only intake 的49原件一直按17块×16行读取，包含 rows-256 的末块；数学与来源闭包没有缺失。该文字勘误不更换已启动任务的原 proof 字节/SHA或数学 tag，不重置其断点。新消费者按原 index 的真实 row_blocks 及逐字文件来源读取，不硬截16块。

## 原来源

- [R872 原点 jets、有界 Picard 代表及两权 RR](../notes/R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)，尤其 §§7–8。
- [R880 原 D/cusp 有界输入实证](R880-certified-original-D-and-common-cusp-bounded-RR-inputs.md)。
- [R880 六个同一共轭 D* 固定图](../notes/R880-original-six-conjugate-bounded-Dstar-spaces.md)，原 proof SHA256 b2e523171c08f61b4c1f66ee7738e8fb687f45a3e1dd72ccd6956800cc9d2d84。
- [R880 七原 Galois 正规输入实证](R880-certified-original-seven-Galois-normal-inputs.md)。
- [R887 原共同 cusp 翻转](../notes/R887-original-common-cusp-flip-and-P0-unit-bounded-representatives.md)，(887.20)。
- [R887 真实完整 C* 与首项](R887-certified-original-common-cusp-flip-and-bounded-RR-inputs.md)。
- [R890 原完整 flip 与原帧契约](../notes/R890-original-eight-flip-Ef-and-marked-frame-method.md)。
- [R883 原 t 首项实证](R883-certified-original-t-first-order-frame.md)。
- [R849 原全局函数和五极理想](R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)。
