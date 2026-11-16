# R872 — 原 P0 jets、146 核与固定 Picard 类418空间的执行契约

日期：2026-11-16。本执行契约只实现
[R872 有界两权 RR 证明](R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)
第3、5节的首个实际 scope；证明 SHA256 为
bd6ee11af3fbbce8db2767bc327265176992bb3be15395018df6612ab4e2dae2。
五个原 $\mathscr L_j(254P_0)$ 的128维空间、144个权1补截面、原参数 $t=a^3$
的帧校准及 Poincaré period 均不是本次完成旗标。

## 1. 真正输入与不改的原对象

原曲线 $Y$ 的 genus 是127，$\deg H=272$。R805 的完整正规自由基
$\beta=(1,w,\ldots)$ 的次数为 $(0,1^{144},2^{127})$。输入 W 是原 R806
已完成的、列表示输入的乘 $w$ 矩阵。它的34组准确系数已由 R860 续存；
本次保留这些原字节、原来源和原坐标映射，不再求 W、幂基大逆或三条共轭。

R868 的实际成功源为 run43819875762/source9586473c46712b6c00a6f8e5736bf387b987ef6b。
其准确右核 $h$ 满足

$$
(W(z_0)-w_0 I)h=0,\qquad h_{271}=1,
$$

并已在584位后通过全部272个 K 方程。既有单位子式的行、列均为0至270。
首辅助素数固定为1000000753。R868 保有两个 K 剩余嵌入的子式、逆及原整数列尺度；
本次依据 R827 实际 place 的原 $\zeta$ 根选择其中一个，不能默认选择第一根。

选入六个真实组：

| 组 | 必要内容 |
|---|---|
| R805 | 原完整 free-basis 和成功 metadata |
| R806 | 原34组准确 W 坐标及原成功 metadata |
| R856 | 原 P0 的两图完整正规基评价和成功 metadata |
| R860 | 原 W 系数 source-index、坐标映射和成功 metadata |
| R868 | 准确 h、实际271子式、同模逆、整数列尺度 index 和成功 metadata |
| R827 | 同素点完整 W 约化、真实 place audit、原五个 cyclic 节点0至4 |

R827 只要求已结束 producer 中这些完成数学 stage 的真实来源闭包。原全局
Hermite 任务的预算终点不影响已完成 W 或五个 Krylov stage。若该原任务没有 FINAL，
配置必须写 certificate:null，另用已 pin 的 W reduction 作 configuration_stage，
核其原完整数学 tag、run/core/manifest 和真正退出码；不得造一个成功证书。
其余五组必须是原成功 producer。

expanded config 的每个 source 给原 BASE 五键、configuration_sha256、所选 files
的完整 file/bytes/SHA 和选件指纹。目录仅是运行位置，不进数学 tag。public wrapper
可从仍存活的后继载体运输这些未改变的原文件；运输 run 不能冒名为数学 producer。

输入 keys 固定为 exact_socle、point_minor、point_inverse、point_integral_index、
point_values、free_basis、W_source_index、W_reduction、place_audit 和五项
Krylov_points。每项均为 source_group 加原 plain spec。

## 2. 新局部算术前必须核实的单位条件

原点左行是 $\ell=(\beta_i(P_0))$，原矩阵为 $A_0=W(z_0)-w_0I$。
从 R868 已存的271方块和原左右核恢复缺失一行、一列，不重新求原点 W 值或模逆。
全部 W 多项式系数的整性取自 R827 完整约化的真实检查；只知 $W(z_0)$ 整不够。

只新形成原 Taylor 系数 $W(z_0+x)$，并求

$$
\alpha=\ell h,\qquad \beta=\ell W'(z_0)h.
$$

若 $\alpha$ 是所选剩余域中的单位，取 $x=z-z_0$；否则若 $\beta$ 是单位，
取 $x=w-w_0$。两者均非单位时只输出这一合法素点选择未达充分条件，不否定
原平面点光滑，也不更换曲线、原点或函数。

这次线性化、$h/\ell$ 的真实约化、旧尺度和实际参数选择作为一个原子 stage 保存。
续算直接复用，不能重复该次实际算术。

## 3. 第0至272阶的原 normal jets

每一阶使用证明(872.9)–(872.12)的原 Hensel 唯一分支。对右端 r，按原列尺度
调用已存在的271模逆求

$$
yA_0=r,\qquad y_0=0.
$$

先设临时第271坐标为0，再扣其第0坐标乘原 $\ell$。每阶完整乘回全部272方程，
并核 $\beta_0=1,\beta_1=w$ 的原正常化；不能只核所选271列。
以 $w-w_0$ 为参数时，用已成 $z-z_0$ 的二、三次标量卷积形成新右端，
不逐阶物化或重复构造273个稠密 W 矩阵。

每阶同时保：

- 实际辅助剩余域中272坐标、z/w 的这一阶和两条必要标量幂系数；
- 原点、准确 W/h、固定单位子式及前一已成阶的 SHA 引用；
- 准确特征零 Hensel 表达式的递推规则和阶数；
- 完整方程与归一化的真实验证旗标。

有限域数值不是已经有理重构的特征零系数。准确来源是原方程的唯一 Hensel
系数表达式，合法单位保证这些系数整且实际数组是它们的约化。

单阶输出先原子提交，再检查下一预算边界。硬中断在 current 更新之前时，
恢复从真正存在的完整阶继续。旧 current 和旧 incomplete FINAL 都不能覆盖
更晚的完整阶。

## 4. 第一个完整146维空间

原 V2 基按 normal 行先、z 幂后列出：

$$
\mathcal V_2=\{z^a\beta_i:0\le a\le2-\epsilon_i\}.
$$

直接由已成 jets 形成第0至272阶的273×418矩阵。
前272行是完整消失条件。对它和单位矩阵作一次联合消元，得到实际272个主列
及该单位方块逆；两侧乘回都核实。自由146列取标准单位坐标，主列按准确
$-J_{\rm pivot}^{-1}J_{\rm free}$ 定义。实际模核通过全部272×146条件。

R872 的 RR 证明给准确 rank272。因此实际单位子式连同这个已知准确维数证明
所选列正是完整特征零 $H^0(2H-272P_0)$ 的 unit-solve 来源，不仅是一个可提升
的猜测核。若所选剩余域实际秩不足，只记录该失败充分条件。

保额外第272阶在全部146列上的值，取第一个值非零的原规范基列 u。于是

$$
\operatorname{div}_{2H}(u)=272P_0+D_\chi,\qquad
\deg D_\chi=272,\quad P_0\notin D_\chi.
$$

本次保原函数 $u/\tau^2$，以及

$$
(H-272P_0)-(D_\chi-H)=-\operatorname{div}(u/\tau^2).
$$

原整数尺度已在 W/free-basis 中，只用一次；不能另乘 $82^2$ 或其他次数补偿。

## 5. 只新两条 V2 乘法矩阵，复用五个真实节点

固定第一锚为 u，第二锚按准确整数次幂族

$$
b_c=\sum_{j=0}^{145}c^jU_j,\qquad c=1,2,\ldots
$$

依次试验。参数是原整数 c，不把有限域代表本身当成改变过的特征零系数。

在已成节点0至4，令 K 为原已认证的272列 Krylov 矩阵。只新形成

$$
K_a=[a,Wa,\ldots,W^{271}a],\qquad M_a=K_aK^{-1}.
$$

旧 W 值和旧 K 逆直接读入。每个新节点独立保存。然后仅做五点插值，
逐条核加权次数界

$$
\deg(M_a)_{ij}\le2+\epsilon_j-\epsilon_i\le4
$$

及完整首列为原 a。真实准确乘法矩阵存在且有这个次数界；
原 cyclic 单位子式与 Vandermonde 单位说明其准确系数在本素点整，
所以这个插值数组是其真正约化。这里不额外构造完整 char0 CRT、一般乘法表，
或另一份旧逆。

将 $M_a$ 的各列按 V3 的原 z 幂移位，得到完整1234×690的
$V_3\xrightarrow{\ a\ }V_5$ 矩阵；所有超出 V5 的项都必须实际为零。

## 6. 同一次两锚消元直接给418空间

u 的乘法像 rank690。用一次带单位矩阵的行选择消元保存其690行单位块和逆；
完整两侧乘回后形成544维行商

$$
\Pi_u(y)=y_R-(P_u)_R(P_u)_I^{-1}y_I.
$$

这个 u 阶段在全部 c 之间只算一次。每个新 b 只形成其乘法矩阵及
544×690的商矩阵 $Q=\Pi_uP_b$。

实际 $\operatorname{rank}Q=272$ 恰给两锚 rank962；R872 的 Koszul 维数公式
证明这排除了在 $272P_0$ 以外的全部共同零。不足272只保留这个试次的诚实
未达充分证书，按后续真实预算继续，不否定原 divisor。

由同一 Q 的实际272行/列单位方块定义完整418个 s；配对坐标

$$
t=-(P_u)_I^{-1}(P_b)_Is
$$

并完整核

$$
Qs=0\quad(544\times418),\qquad
P_ut+P_bs=0\quad(1234\times418).
$$

两块已知单位方阵的 Schur 分解直接证明原962阶合并子式非零；
不另求同一个大行列式。规范自由坐标与这些原选行给准确特征零 unit-solve
表达式，其完整空间为 $H^0(3H-D_\chi)$，维418。
同一商核不再重复做第二次 membership 消元。

## 7. 文件、断点和实际结论

数学 RESULT 为 R872-original-P0-jets-and-fixed-Picard-RR-spaces。
CLI 是 --config、--out、--budget-minutes。
完成数学 stage 全为 output 根目录的 R872-*.json.gz，complete:true；
R872-current.json.gz 是 complete:false 的进度，不进入已成 inventory。
所有实际数学 stage 的 configuration 完全等于本次数学 tag。

数学 tag 固定新源码、本文和 R872 正文 hash、原六组身份/选件指纹、全部输入
plain specs、素点和完整策略。预算、有限 c 试次上限及纯运输位置排除在 tag 外。
增加试次上限只续已有结果，不重做前缀。不同数学代码或源不能改标签冒充续算。

每次结束都重建所有真实完成 stages 的清单。只有原点 jets、146核、真实 rank962
和完整418空间全部完成时 FINAL.complete 才为 true。FINAL 精确给
actual_original_P0_jets_through_order272_computed、
actual_original_complete_146_kernel_certified、
actual_fixed_chi_complete_418_RR_space_certified 和 actual_pencil_rank。
BudgetStop、当前素点单位失败或有限试次未达秩都保持完整已成阶段和实际原因。

本次无论成功与否，five_original_Lj_RR128_computed、
five_original_Lj_weight_one_144_complements_computed、
original_t_frame_calibration_computed 与
connection_Poincare_period_or_height_computed 均为 false。
后继真正五类消费者应读这些已成准确表达式及实际模矩阵，继续 R872 第6至9节；
它不能用固定 $\chi$ 的418空间代替原五类的128空间。
