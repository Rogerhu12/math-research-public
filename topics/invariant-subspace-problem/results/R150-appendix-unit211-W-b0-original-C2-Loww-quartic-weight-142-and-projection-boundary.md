# R150 附录：整 b0 的原 C2、完整 Loww 四次、一个权核与后续冻结边界

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（UTC）。

**状态：前三项原恒等式已证明；第二投影按实际资源边界冻结。**

## 1. 实际完成的数学与准确边界

在当前 W、distinct-singleton、物理 $D\ne0$ 的整个 b0 原图上，新的同点输入已完成：

1. 三个原均值余式的叉积给一个纯 lambda 二次 $C_2$，完整返回四原均值；
2. 完整 $L_w=NS-PS+E_{W2}$ 经同一个首一 qf、全域同 f 恢复，给纯 lambda 四次 $P_L$，完整返回七原源；
3. 固定 q2/Loww 六阶矩阵给非零纯权原核 $F_{142}(u,\nu)$，全部七原源返回。

第二个预定 C2/Loww 固定六阶目标在原 180 秒边界终止，未输出任何完成 checkpoint。它没有结式、原权核或原单位结果，不补记其内部步数。本次没有判断该分支为空，没有新的纯 u 覆盖，也没有新增有限点界。

前三项已完成的原恒等式不因后续源退出码 −14 而失效；首次执行的真实负状态同时保留。本篇不重播成功目标，也不重启被冻结的第二目标。

## 2. 同一点七原源与已有全域 f 关系

沿[整 b0 五原二次](R150-appendix-unit211-W-b0-inverse-slope-five-original-quadrics-six-weight-conditions.md)的同一个可逆权图，

$$
\nu=\frac{(2u-1)(k+2)}{uk+2},\quad
d=u\nu-(2u-1),\quad r=2u-1-\nu,
$$

$$
k=\frac{2r}{d},\qquad Q=\frac{2(u-1)r}{d},\qquad
\ell=\frac{u\{\nu^2-(u+1)\nu+2u-1\}}r.
$$

只在本 b0 支，既有原值支付 $A_*=uQ(\nu+2)$，并恢复

$$
\kappa=\frac{\ell}{\nu+2},\qquad
T=-\kappa(3-2\lambda).
\tag{1}
$$

此次固定七原源为

$$
\mathcal F=(E_1,E_{B,e},E_{B,o},N_1,q_2,NS,PS).
\tag{2}
$$

其中独立 $E_1$ 来自真 dual 乘法，原 $q_2=2a_d/\ell$ 由 $C_4=mD\ell q_2$ 在当前物理图支付；没有倒 q2 的二次头。完整原 $I_{11}$ 始终保留。

[全域 f 唯一恢复](R150-appendix-unit211-W-original-I4-six-rows-entire-paid-f-head-and-unique-recovery.md)给首一 qf、三个原余式及纯权 v：

$$
q_f=f^2+q_1f+q_0,\qquad
r_i=A_i+B_if,\qquad
\sum_i v_iB_i=1,\qquad
f+g=\sum_i v_i r_i,\quad g=\sum_i v_iA_i.
\tag{3}
$$

新源只再生 (3) 的必要系数定义，将每个实际比值完整约消后核最终分母全为旧原单位，再完整返回四原源。没有反演一个未取消的 raw global head。

同一个 (1) 代入所有原式、乘子和几何坐标后，

$$
B_i=B_{i0}+\lambda B_{i1},\qquad
v\cdot B_0=1,\quad v\cdot B_1=0.
\tag{4}
$$

因此 f 的唯一恢复不依赖本次新叉积非零，也不依赖先前四乘五新 h 的开图。

## 3. 新 C2 与叉积零面的完整代数意义

取

$$
\mu=B_0\times B_1.
$$

其完整原组合为

$$
C_{\rm raw}(\lambda)=\mu\cdot A(\lambda)
=\sum_i\mu_i r_i(\lambda,f),
\qquad\deg_\lambda C_{\rm raw}\le2.
\tag{5}
$$

因 $\mu\cdot B_0=\mu\cdot B_1=0$，f 系数恒等消失。这里没有倒置叉积的任何分量。

对 (5) 清实际七乘子的旧已付分母，只共同精除全部七个分子，再把新的七乘子完整乘回 (2)。最后仅剥旧付费权支撑，实际得到非零 $C_2$：

| 原条件 | u 次数 | ν 次数 | lambda 次数 | 总次数 | 项数 | 定义字节 |
|---|---:|---:|---:|---:|---:|---:|
| $C_2$ | 19 | 24 | 2 | 31 | 1198 | 33271 |

SHA256：e91ebd4d4d732ca803cf7faa9267f162b8b05a2ee84361484fe0dd86a45a1e03。

实际共同乘子因子双次数 $(2,2)$、总次数 3、8 项；随后只剥 u、u−1 各一个 gcd 层。最终七源的后三个乘子恒零，所以这是完整四均值的原条件，不借 q2、NS 或 PS。未知共同因子没有被当单位，因取消后的原组合本身已逐 f 坐标成立。

下面是基于 (4) 的直接纸面补充，不增加执行门。向量三重积给

$$
\mu\times v=B_1.
\tag{6}
$$

因此在同一纯权环中有准确理想等式

$$
(\mu_1,\mu_2,\mu_3)=(B_{11},B_{21},B_{31}).
\tag{7}
$$

叉积同时为零的整面，正是三个余式的 lambda-f 系数同时为零的整面。它不是一个被默认删除的秩退化集。

再令

$$
P=A-(B_0+\lambda B_1)g.
$$

则

$$
v\cdot P=0,\qquad
P=(B_0\times P)\times v,\qquad
B_1\times P=v\,C_{\rm raw}.
\tag{8}
$$

这些都是交换环上的多项式恒等式。故三个原均值余式完整保留；在某个明确 $B_{j1}\ne0$ 的开图，(8) 才允许用 $P_j,C_{\rm raw}$ 恢复其余两个 P。没有将这一开图外推到 (7) 的整零面；后者保全部原均值、qf、q2 和个别值条件。

式 (6)–(8) 使用的是原始叉积 $C_{\rm raw}$；本次 primitive $C_2$ 有自己完整的原乘子，不能省略其清分母和共同精除的尺度身份。

## 4. 完整 Loww 的同 f 纯四次

同一自由 T、自由 f 的真 Gram 给出

$$
\begin{aligned}
E_{W2}&=b(2p-u-X)E_B+c(2q-u-Y)E_C\\
&=(2u-u\ell-V)E_{B,e}
 +(2\theta-um-mx-\ell\delta y)E_{B,o},
\quad\theta=u-\ell Q.
\end{aligned}
\tag{9}
$$

准确的全自由 f 原修正是

$$
\begin{aligned}
K_w=2[&t^2+(5u-4x-2)t+2(x^2-\delta y^2)\\
 &+4x+4\delta y-4ux+2u^2-6u+Q],\\
L_w={}&2P_{02}(2\lambda-1)w
 -bc\,t\{K_w+4(f-u)(t-2)\},\\
w={}&\lambda-1-T.
\end{aligned}
\tag{10}
$$

本次完整核回

$$
L_w=NS-PS+E_{W2}.
\tag{11}
$$

Loww 是几何总次数至多三的原式，没有误称二次。先作同一个 (1) 代入，再由首一 qf 精确短除：

$$
L_w=Q_Lq_f+A_L+B_Lf.
$$

用 (3) 的同 f 原关系消去 f，得到

$$
P_{L,\rm raw}=A_L-B_Lg
=L_w-Q_Lq_f-B_L(f+g),
\qquad\deg_\lambda P_{L,\rm raw}\le4.
\tag{12}
$$

全部七个真实原乘子和全部 f 系数已返回。实际七乘子共同因子仅为非零有理常数；最终只剥 u、u−1 各一个 gcd 层，得到非零 primitive $P_L$：

| 原条件 | u 次数 | ν 次数 | lambda 次数 | 总次数 | 项数 | 定义字节 |
|---|---:|---:|---:|---:|---:|---:|
| $P_L$ | 34 | 41 | 4 | 55 | 5888 | 202047 |

SHA256：2af047cf94933ab01c0060740497b5769e116992dbc6be309fc50c4f79111d38。

C2 在数学时间 0.994569908 秒完整返回，纯 Loww 在 1.799899898 秒返回；同 lambda 的完整接口 checkpoint 在 1.831538731 秒完成。所有 q2/C2/Loww 首项零面仍是原必要条件的范围，不加新的几何逆。

## 5. 首个固定六阶给真实权核 F142

对 q2 与 $P_L$ 固定容量二、四。六行是

$$
q_2,\lambda q_2,\lambda^2q_2,\lambda^3q_2,\quad
P_L,\lambda P_L
$$

对 $1,\lambda,\ldots,\lambda^5$ 的系数矩阵。所有次数下降仍保留在这个固定矩阵中。

fraction-free 消元的全部多项式整除均实际乘回，并以完整变换矩阵核

$$
TM=RI
$$

的全部 36 个坐标。第一行于是给

$$
R=U(\lambda)q_{2,\rm num}
   +V(\lambda)P_L,\qquad
\deg U\le3,\quad\deg V\le1.
\tag{13}
$$

将 q2 的原已付分母恢复，并将 (13) 完整复合至七原源；只取消全部七个真实乘子共同因子，再逐原式返回。最终只剥 u 三层、u−1 一层、ν+2 三层的已付 gcd 支持。所有共同内容零面、瞬时主元零面和原 lambda 首项零面由最终多项式身份覆盖。

实际非零权核为

$$
F_{142}(u,\nu)\in(\mathcal F).
\tag{14}
$$

它的 u、ν 次数分别是 92、110，总次数 142，8426 项，定义 537398 字节，SHA256：

3f7afa85c72dd36f0154c39f99dd6be5764adb0d758a2060d05e8528fade670f。

该条实际七乘子共同因子双次数 $(12,5)$、总次数 17、24 项，SHA256 为 cef915bc9ee1945273ec74699e0964dde178d3a5d07d67abc7bbda71d189f5c2。其单位性未被假定；精除后的七个原组合已全部返回。

原组合在 54.218849511 秒完成，随后 54.336530547 秒输出完整首投影 checkpoint。若干来源乘子的展开定义达到数 MB，只保字节数/SHA，不保存任何系数缓存。

本次没有对 $F_{142}$ 作 QQ 因式分解、平方自由处理、gcd 或纯 u 投影；也没有断言它的不可约性。非零原必要权条件不等于原理想含 1。

## 6. 第二目标的真实负状态

第二个预定目标是 C2 与同一个 $P_L$ 的固定六阶矩阵。执行进入该目标后，在总预算 180 秒处以 SIGALRM 终止：

- 源实际退出码：−14；
- driver 墙钟：180.072328987 秒；
- 最大子进程 RSS：267776 KiB；
- 最后完整数学输出仍是第5节首投影的 54.336530547 秒 checkpoint。

第二目标没有输出任何完整变换矩阵、结式或新权核，也没有内部步数 checkpoint。因此本篇不报告它做了几步，不把它记成零结式、单位、原图排空或已成第二曲线。

首个目标和已成 C2/Loww 接口保持有效；第二目标准确冻结。不提高预算、不换序重派，也不因旧参数需要再次执行这条固定结式。全部原 $I_{11}$ 和未付权零面继续保留。

## 7. 源、实际执行与规则读取

源：

[2026-11-28-unit211-W-b0-cross-C2-complete-Loww-same-lambda-seven-source-projections-8542.py](../notes/2026-11-28-unit211-W-b0-cross-C2-complete-Loww-same-lambda-seven-source-projections-8542.py)。

源 Git blob：43638940b02eb65da644a1b2eef4f68c078c4aec；22818 字节；SHA256：

7a732655b5bf64144f91d6992910ceb67563e4125a12246c12dbb83e1f4f1831。

[首次输入说明](../notes/2026-11-28-unit211-W-b0-cross-C2-complete-Loww-same-lambda-seven-source-projections-8542-input.md)保留当时未执行状态。本次是唯一首次 180 秒、4 GiB、自含零依赖，外层 195 秒。

- Run：[46142342880](https://github.com/Rogerhu12/math-research-public/actions/runs/46142342880)。
- Job：[140970848068](https://github.com/Rogerhu12/math-research-public/actions/runs/46142342880/job/140970848068)。
- 冻结源提交：9ac4dfef1e4128cfb89ac62bf3c0e382ac38d9d5。
- stdout：11026 字节；SHA256 5c38f813dd86a47433f5e9133c187441192743896554fc3a9c9c3503d0f6faa0。
- 真实 pull：2026-11-28 11:58:25.500188 UTC；从冻结提交到 3199b753e8057f3b0632b3df092eae1039a47de7，两 README 无变。
- 已读 root blob：99c5ad8d06e939e6cfbbab1afdeffa5463f15f18；课题 blob：5fbd905291dd044c88d35bd9c07ac0e586ff795a。

[小执行回执](../notes/2026-11-28-unit211-W-b0-cross-C2-complete-Loww-same-lambda-seven-source-projections-8542-execution.json)保五条真实数学 checkpoint、driver 和参数规模/SHA。没有旧1898伴随、旧10ab六投影/PRS的重放，也没有新的权长度或原解排空结论。第3节 (6)–(8) 是已返回系数身份的完整纸面推论，不依赖附加执行。
