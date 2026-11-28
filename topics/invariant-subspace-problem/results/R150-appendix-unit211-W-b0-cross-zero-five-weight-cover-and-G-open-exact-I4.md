# R150 附录：整个 W/b0 的三条交叉头给五次权覆盖与其补图的精确四式呈示

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：唯一首次精确执行完整成功；没有排空整个交叉头零支、b0 支或 W。
- 适用范围：当前正确 W、distinct-singleton、物理 $D\ne0$，并施加已刊 $b_0=0$。既有原权单位保持原范围。
- 本文的新结果是三条真实 $\lambda f$ 系数的原理想五次覆盖，以及该覆盖非零图上的精确均值呈示。所有五次覆盖零纤维与全部原值条件继续保留。

## 1. 原坐标、原均值与三条头的定义

沿[整个 W 的同 f 原六行与唯一恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)、[三 pair 与三同 f norm 的完整 I4 呈示](R150-appendix-unit211-W-three-pairs-three-same-f-norms-complete-original-I4-presentation.md)，使用已付逆权坐标

$$
u=e+1,\qquad \nu=\frac{(2u-1)(k+2)}{uk+2},
$$

$$
d=u\nu-(2u-1),\qquad r=(2u-1)-\nu,\qquad
k=\frac{2r}{d},\qquad Q=\frac{2(u-1)r}{d}.
\tag{1}
$$

这里 $d,r$ 的非零性来自原权图的精确正反身份，不是额外丢弃权纤维。令

$$
\ell=\frac{u\{\nu^2-(u+1)\nu+2u-1\}}{r},
\qquad m=u-\ell,\qquad \delta=1-Q,\qquad M=4bc\delta.
$$

在当前 $b_0=0$ 支，原 $A_*=uQ(\nu+2)$ 已付，故

$$
T=-\kappa(3-2\lambda),\qquad
\kappa=\frac{\ell}{\nu+2}.
\tag{2}
$$

$(\nu+2)^{-1}$ 只在本 b0 范围使用。

四个真实原式记为

$$
F=(E_1,E_{B,e},E_{B,o},N_1).
$$

其中 $E_1$ 独立保留，不使用未经证明的 $E_1=E_W$ 替换。唯一源直接由完整 dual 乘法生成它们；特别是原 germ 平方的一阶坐标为 $2d_0d_1$，均值项是 $-4d_0d_1$。

原首一式及三个剩余式是

$$
q_f=f^2+q_1f+q_0,\qquad
r_i=A_i(\lambda)+B_i(\lambda)f,\qquad
B_i=B_{i0}+\lambda B_{i1}\quad(1\le i\le3).
\tag{3}
$$

具体地，若 $\beta=u\nu$，则

$$
q_f=\frac{bc}{2u(u-\beta)}
 \left(E_{B,e}+\frac{\ell\delta}{m}E_{B,o}\right),
$$

并从 $E_1,E_{B,o},N_1$ 各减去其 $f^2$ 系数乘 $q_f$ 得到 $r_1,r_2,r_3$。全部分母是当前已付原权单位。源码在代入 (2) 后仍逐式、逐 $f$ 坐标返回四个原来源。因此

$$
I_4=(E_1,E_{B,e},E_{B,o},N_1)
   =(q_f,r_1,r_2,r_3).
\tag{4}
$$

其中 $\deg_\lambda A_i\le2$、$\deg_\lambda B_i\le1$、$\deg_\lambda q_1\le1$、$\deg_\lambda q_0\le2$。

以下令 $B_0=(B_{10},B_{20},B_{30})^t$、$B_1=(B_{11},B_{21},B_{31})^t$。旧完整恢复已给纯权行 $v$，满足

$$
v\cdot B_0=1,\qquad v\cdot B_1=0,\qquad
g=v\cdot A,\qquad v\cdot(r_1,r_2,r_3)^t=f+g.
\tag{5}
$$

所有系数仍只在旧原权单位环中。

## 2. “交叉头零”准确等于三条新系数的理想

定义

$$
\mu=B_0\times B_1.
$$

由向量三重积和 (5)，

$$
\mu\times v
  =(B_0\times B_1)\times v
  =B_1(v\cdot B_0)-B_0(v\cdot B_1)=B_1.
\tag{6}
$$

反向 $\mu=B_0\times B_1$ 同样是纯权线性组合。因此在当前权系数环 $A_W$ 中有真正的理想等式

$$
(\mu_1,\mu_2,\mu_3)=(B_{11},B_{21},B_{31}).
\tag{7}
$$

这保留全部重数，不只是一个集合论判别。

**三条 $B_{i1}=0$ 是本文所接的交叉头零分支条件，绝不是对整个 b0 原解额外施加的方程。** 本文只对该分支取权投影。交叉头非零处仍保持所有原条件。

## 3. 唯一新执行的三个固定投影与完整 Bézout

源码先对三条实际 $B_{i1}$ 的分子只除旧已付支持，并同步调整其真正三来源乘子。得到 $p_i=c_iB_{i1}$，其中 $c_i$ 是旧权单位，故不改变 (7)。

| 系数 | $(u,\nu)$ 次数 | 总次数 | 项数 | 定义 SHA256 |
|---|---:|---:|---:|---|
| $p_1$ | $(6,6)$ | 9 | 42 | 277f9248f5d82aa9107aab1606bee937aedd369b0f0b7d0212d59e6f6ffc4aab |
| $p_2$ | $(8,8)$ | 12 | 70 | 85ab8eee07094bee0a71eed0378ff4278b2646f87dada8dae7a449192d84a984 |
| $p_3$ | $(8,9)$ | 12 | 74 | 46d5e21a0738143d71daf8108cb9e5743958cc591a2002551c05912f16d4c3fd |

依次只执行固定三对 $(1,2),(1,3),(2,3)$。它们的原 $\nu$ 容量分别为 $(6,8),(6,9),(8,9)$，即固定 Sylvester 阶数 $14,15,17$。

每个矩阵在 $\mathbb Q[u]$ 上作带全变换矩阵的精确无分式消元；每次整除均乘回。最终所有矩阵坐标返回

$$
T_{ij}S_{ij}=R_{ij}(u)I.
\tag{8}
$$

其中一行给 $R_{ij}=U_{ij}p_i+V_{ij}p_j$，再完整组合到三个原 $B_{i1}$。临时主元从未被当作物理单位；(8) 是多项式身份，因此保留所有 $\nu$ 首项下降乃至同时下降的纤维。

三个结果只剥旧原权支持后，实际纯 $u$ 次数为 $18,29,36$。对应定义 SHA256 为

- 18 次：f6fce93a6843b99be050937e4eb5a39d8a890b84aeacaabdd73ac5871895e131；
- 29 次：e6c11f08a6e8a77639bafc3a5949a2a994dd34c2325b949c15d22feb1297c7f9；
- 36 次：90955caeef87c3e7e296b472c8b29782c5a34a8c1b337d05184c6c935f2cbb1e。

剥除记录按源中的 gcd 层数为：

| 固定对 | $u$ | $u-1$ | $2u-1$ |
|---|---:|---:|---:|
| $(1,2)$ | 7 | 37 | 16 |
| $(1,3)$ | 2 | 35 | 18 |
| $(2,3)$ | 2 | 42 | 25 |

随后只在 $\mathbb Q[u]$ 中作两个真实扩展 gcd，全部原乘子同时组合并返回。实际 gcd 次数为

$$
18\longrightarrow5\longrightarrow5.
$$

故获得非零五次 $G(u)$ 和三个真实原系数乘子 $w_i\in A_W$，满足

$$
\boxed{\quad G(u)=\sum_{i=1}^3 w_i B_{i1}.\quad}
\tag{9}
$$

这里 $w_i$ 的全部分母已按旧原权支持检查。没有除未知纯 $u$ 因子、没有只用多元 gcd=1 判空。

$G$ 的精确定义是冻结源码最后两次原扩展 gcd 得到的 cover；其规范五元指数表示为 6 项、134 字节，SHA256 为

$$
\texttt{9f9544b1500bc385df9f8a04d4693c3895655712721661a109854be0845ea8d2}.
\tag{10}
$$

这只登记参数定义与哈希，不保存可重算的系数载荷。

## 4. 五次覆盖的完整有理因式与整零纤维

首次完整 $\mathbb Q[u]$ 因式分解及全乘回返回三个不可约因子，次数与重数分别是

$$
(1,1),\qquad(1,1),\qquad(3,1).
\tag{11}
$$

两个一次因子已按**实际相同规范编码的完整 SHA256** 精确识别：

$$
\phi_1(u)=4u+5,\qquad \phi_2(u)=6u-1.
$$

其定义 profile 分别为

- $\phi_1$：37 字节，9b702a5320030eb66ea9572167b2589cb503a6035fd67b350256e6248dcbe9ec；
- $\phi_2$：38 字节，c708effec8346a565d2ecf2264cb6635e4adeffe15c1ec12f222a57378d441ed。

这个识别只是把两个小数学参数的规范文本与既有实际哈希比对；没有重算任何原头、投影、Bézout 或分支。

第三个参数也已按同一规范 SHA256 精确识别为

$$
\phi_3(u)=20u^3-4u^2-20u+9.
\tag{12}
$$

它的四个升序整数系数为 $[9,-20,-4,20]$，五元指数规范表示恰为 77 字节，其 SHA256 完整等于实际输出的

$$
\texttt{bf8d54f313b63c7f42b5f24b2bfc31e789f1c65ca2b4c5fd5bf3b8be236675b2}.
$$

再只作这三个小数学参数的整数乘法，得到

$$
(4u+5)(6u-1)\phi_3
=480u^5+424u^4-684u^3-284u^2+334u-45.
$$

除以 480 后的规范表示为 134 字节，其完整 SHA256 与 (10) 一致。因此实际原覆盖的精确参数定义是

$$
G(u)=\frac{(4u+5)(6u-1)(20u^3-4u^2-20u+9)}{480}.
$$

三个因子及这个首一乘积的四个实际哈希均匹配。这个后续参数识别没有执行任何原均值、固定投影、扩展 gcd 或 QQ 因式分解；原因式的不可约性、重数一和原来源仍取自本次唯一实际运行。

由 (7)、(9)，交叉头零的整个原权支都位于

$$
u=-\frac54,\qquad u=\frac16,\qquad
\phi_3(u)=0.
\tag{13}
$$

三个完整常数域以及其中所有 $\nu,\lambda,f$ 纤维均保留。因为各因子重数一且不可约，它们互素，权系数商可按这三个整个常数域作 CRT 分解；没有只挑复根或数值采样。

这是交叉头零支的 $u$ 覆盖。它本身不给每个 $u$ 的 $\nu$ 纤维界，更不宣布交叉头零、b0 或 W 已空。

## 5. G 非零图的新精确均值呈示

(9) 在整个旧权系数环成立，不只在 $G\ne0$。令

$$
\widetilde w=w-(w\cdot B_0)v.
$$

则

$$
\widetilde w\cdot B_0=0,\qquad
\widetilde w\cdot B_1=G.
\tag{14}
$$

构造纯权三行矩阵

$$
U=\begin{pmatrix}v\\\widetilde w\\\mu\end{pmatrix}.
$$

由 (5)、(14) 及标量四重积，

$$
\det U=(v\times\widetilde w)\cdot(B_0\times B_1)
=(v\cdot B_0)(\widetilde w\cdot B_1)
 -(v\cdot B_1)(\widetilde w\cdot B_0)=G.
\tag{15}
$$

定义

$$
C_{\rm raw}=\mu\cdot A,\qquad
C_3=\widetilde w\cdot A-G\lambda g,\qquad
P_0=g^2-q_1g+q_0.
$$

对三个原 $r_i$ 有完整代数身份

$$
U\begin{pmatrix}r_1\\r_2\\r_3\end{pmatrix}
=\begin{pmatrix}
f+g\\
G\lambda(f+g)+C_3\\
C_{\rm raw}
\end{pmatrix}.
\tag{16}
$$

这里 $C_{\rm raw}$ 是未除任何未知公因子的交叉原式，不能无尺度地与别处归一化后的 $C_2$ 混用。并且

$$
q_f=(f+q_1-g)(f+g)+P_0.
\tag{17}
$$

因此只有在明确的 $G$ 主开图，(15) 使 $U$ 真可逆，得到精确的双向理想等式

$$
\boxed{\quad
I_4 A_W[G^{-1}][\lambda,f]
=(f+g,\ P_0,\ C_{\rm raw},\ C_3).
\quad}
\tag{18}
$$

其 $\lambda$ 次数上界依次为 $2,4,2,3$；第一式对 $f$ 首一。在尚未局部化 $G$ 的环中，(16) 和伴随身份仍给

$$
G(r_1,r_2,r_3)^t
\in(f+g,C_3,C_{\rm raw})^3.
\tag{19}
$$

所以 (18) 的补图没有被悄悄丢弃。

在整个 b0 值支再添原 $q_2$ 时，(18) 只是把对应 $J_5$ 改写为

$$
(f+g,\ P_0,\ C_{\rm raw},\ C_3,\ q_2)
\quad\text{于 }G\ne0.
$$

原 $NS,PS$ 及完整其余个别值条件仍须在同一点保留。四式均值呈示本身不是整个原解的充分系统。

本节是从实际 (9) 和已刊 (5) 的纸面原代数推论；本次运行没有另外展开新的 $C_3$、它的投影或新的权曲线。

## 6. 唯一真实执行与可复核材料

- 自含[冻结源码](../notes/2026-11-28-unit211-W-b0-entire-cross-zero-three-original-lambda-f-heads-8542.py)，Git blob 681d0a0b3d76b30cf572c3e28d2b296cc704f73c，19739 字节，SHA256 1e41e505bf925b8f5e4422c60267efc9e0db6cc5f311daef9524efa9f44f372f。
- [首次输入说明](../notes/2026-11-28-unit211-W-b0-entire-cross-zero-three-original-lambda-f-heads-8542-input.md)。
- [小实际回执](../notes/2026-11-28-unit211-W-b0-entire-cross-zero-three-original-lambda-f-heads-8542-execution.json)。
- Actions run [46143877410](https://github.com/Rogerhu12/math-research-public/actions/runs/46143877410)，job 140975574446。
- 源提交 4b347d2620d5e4543958ea3e5537758b2ed1f674。
- 真实 pull 于 2026-11-28 12:17:20.525204 UTC 到 1e43da19c2da4c5d3e129de8b491eb125e6a7d2e，两 README 无变。
- 原内层预算 120 秒、1 GiB，外层 135 秒；真实 exit 0，driver 墙钟 2.084278499 秒，最大子进程 RSS 46812 KiB。
- 数学最终 checkpoint 2.016026571 秒；source 自报最大 RSS 46356 KiB。
- stdout 8049 字节，SHA256 714a428931f471f34e4a8a43ece3d5bf421b84205421d882f24f26af1e57e820。

实际返回包括 6 个原 $f$ 坐标、21 次三原系数身份、19980 次新 $\nu$ 矩阵整除乘回、710 个完整矩阵坐标、两个真 $\mathbb Q[u]$ Bézout，以及全 QQ 因子乘回。原统计字段中未运行的旧项目仍为零，没有把它们计作新成功。

没有再执行已成 C2/Loww、旧四乘五矩阵、旧六投影或冻结 PRS。未声明新的整体点数上界；此前[整个 b0 的规范 Artin 长度 23088](R150-appendix-unit211-W-entire-b0-23088-normalized-Artin-length.md)保持其独立来源。

下一接口是 (13) 三个**整个**常数域中的原 $\nu$ 返回，以及 (18) 补图的新低次原条件。任何额外头零、非单位或值条件仍须按其真实原来源处理。
