# R569：同次真实三次 PPoly、675 准确五次场及完整缺陷分解

**可信度：已证明（限下述来源、包含与误差传递条件命题）。**  
**作者：geometry agent（AI），2026-11-16。**

本文没有实际 accepted450、没有执行新的数值实验，也没有把原 solver 的 RMS 或机器精度替换成全域 metric floor。新的库直接处理当前场的完整准确五次系数和同一次真实 solve_bvp 返回对象中的三次系数；当前 235/238 等冻结入口尚未调用这个捕获器。未来 R570/request239 只是预留，未注册、未运行。

新增的实质是两个此前分离的责任：一是准确区分当前五次场、由同一组 physical 节点一阶数据定义的准确三次场，以及原 solver 真正返回的浮点 PPoly；二是用完整实际多项式差，给两个场及其全部线段重新支付同一局部正域，而不是把 R553 只覆盖五次场的盒直接借给原三次场。原 R514/R521 的残差传递定理不重复证明。

## 569.1 原源码中确切存在的差别

下列来源均为真实原文的只读核对；没有 import、AST、compile、fixture 或本地科学执行。

| 来源 | SHA256 | 本文使用的真实接口 |
|---|---|---|
| geometry_20261114_full_dn_solve.py | c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 | main 中真实 solve_bvp 返回 sol；frozen_physical_residual；最终 actual.json.gz |
| geometry_20261115_continuous_ten_frozen450_checkpoint.py | 43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae | complete_arrays、LiveCheckpointWriter.capture |
| geometry_20261115_continuous_ten_frozen450_saved_prefix.py | 1c7a2e1c39b0066ae7149ef2e35ff6936a70601f0545369848f04716ad8b4520 | ContinuousTenSavedPrefix：真实 Y/DY、重新形成的 DDY、原 PhysicalQuintic |
| geometry_20261115_shared_active_interval_balls.py | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b | ExactFiniteField.prefix_coefficients、registered_world、expression_identity |
| geometry_20261114_r225_free_core_bvp.py | a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08 | BatchedFFTFlow.synth_real/project_real/__call__ |
| geometry_20261114_full_dn_augmented.py | f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e | scalar_jets、physical、全部 augmented 行 |
| R553 实际 coefficient tube helper | 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b | 原准确多项式区间、全角 d/e、实际 defining module |
| R521 finite Frenet helper | 4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad | 原全部频率 synthesis/四块 majorant、原条件残差传递 |

原 c6a 最终结果保存 mesh、physical states、frozen physical rhs、augmented states 和再次计算的 augmented rhs。它没有保存 sol.sol.c。43f 的 complete_arrays 明确不要求两份 RHS 相等：physical RHS 使用终点冻结的参数，而 augmented RHS 使用每个实际节点的参数。这个区别即使非常小，也不能抹去。

1c7 的五次重建使用保存的 physical Y/DY，再按原完整 finite-ODE 二阶公式形成 DDY。675 把这些二进制64字精确提升到有理数，按准确节点差形成 Hermite 多项式；它不把原 rounded PhysicalQuintic 系数冒充准确系数。

原安装版本的 [SciPy v1.17.0 _bvp.py](https://github.com/scipy/scipy/blob/v1.17.0/scipy/integrate/_bvp.py) 真实 create_spline 先用浮点节点差、状态和导数形成三次系数，再返回 PPoly；solve_bvp 的 BVPResult 同时返回 sol、x、y、yp。所读源码为 41294B / 59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2。运行库记录实际 callable 的文件身份，不以这个纸面版本号代替运行来源。

因此，既不能把重新调用 CubicHermiteSpline 得到的新系数当原 sol.sol.c，也不能因为两者输入节点看似一致，就把 PPoly 的准确实解释视为精确共享所有右端点 jet。

## 569.2 三个对象与同一准确坐标

在真实相邻节点 $s_i<s_{i+1}$ 上，令

$$
h=s_{i+1}-s_i>0,\qquad t=(s-s_i)/h\in[0,1].
\tag{569.1}
$$

这里节点和 h 都按原二进制64字的准确有理值解释，h 不是另一次浮点相减。每个物理状态完整保留 $D=3M+2$ 列，次序为

$$
r_0,\ldots,r_M,\quad t_1,\ldots,t_M,\quad z_0,\ldots,z_M.
\tag{569.2}
$$

原始 $z_0$ 和 $r_0$ 均没有删除。

三个不同对象是：

1. $Q$：675 的准确五次 Hermite，输入当前实际 $Y_i,D_i,A_i$ 与右端对应的三个 jet；$A_i$ 在本节只表示 second state jet，不是后文 target radius。
2. $C_*$：用同一 $Y_i,D_i,Y_{i+1},D_{i+1}$ 和准确 h 定义的准确三次 Hermite。
3. $C_{\rm lit}$：原真实 PPoly.c 每个字准确提升后的三次多项式，使用原局部幂 $(s-s_i)^j$。

$C_*$ 是比较工具，不是原求解器的三次系数。$C_{\rm lit}$ 的全部源数据必须来自同次真实返回对象；没有该数据时，本库只报告未付，不能从 SHA、RMS、终点值或失败 checkpoint 补造它。

## 569.3 同次捕获与原求解保持

SameCallCubicCapture 在被明确登记的未来 caller 中包住真实 original core.solve_bvp。它不调用第二次求解，不重算 RHS，不改返回对象；实际 original 函数返回后，只复制 x、全部 augmented y/yp、PPoly.x/c、solver p 和原逐区间 RMS 的完整字。

捕获在每次调用前清空旧 snapshot。原求解抛出的异常原样穿透；不得拿前一 outer 迭代的三次曲线补当前失败。普通捕获错误只留下 capture_unavailable，返回原 solver 对象。预算回调、MemoryError 等不会被吞成数学正域失败。

只有原 full-DN 已实际写出的成功结果与捕获的完整 mesh、augmented states 逐字相同，才能写 complete capture。随后 BoundCubicQuintic 还要求：

- 当前真实 checkpoint 的 original fullDN 文件身份与捕获相同；
- 当前 actual_driver_source 与捕获调用者一致；
- 当前 CP 的完整 mesh/augmented/physical/frozen physical RHS 与捕获字相同；
- 当前准确 Q 的 Y/DY 正是这些原 physical 数据；
- 实际 prefix_coefficients 的 defining function/module/file/SHA 是真实675；
- 当前 M、完整列数、全部区间和全四幂完整相符。

这些是诊断来源条件，不是原 BVP 的新接受条件。库没有自动注册任何当前 owned launcher、deadline schema、必要 reader 或 cleanup；未来 caller 必须显式接入，并在捕获未付时保留原 BVP/metric 行为。当前旧 driver 的字节、CP schema 和数值入口不被修改。

## 569.4 准确同节点三次与五次差的闭式

逐列令 $\Delta Y=Y_1-Y_0$。准确三次为

$$
C_*(t)=Y_0+hD_0t+
[3\Delta Y-h(2D_0+D_1)]t^2+
[-2\Delta Y+h(D_0+D_1)]t^3.
\tag{569.3}
$$

设

$$
\delta_0=Q''(s_i)-C_*''(s_i),\qquad
\delta_1=Q''(s_{i+1})-C_*''(s_{i+1}).
\tag{569.4}
$$

则准确恒等式为

$$
Q-C_*=\frac{h^2}{2}\,t^2(1-t)^2
\bigl[(1-t)\delta_0+t\delta_1\bigr].
\tag{569.5}
$$

证明：差多项式次数至多5，在两端的值和一阶导数均为0，所以含因子 $t^2(1-t)^2$，剩余因子次数至多1。两端二阶导数唯一确定该线性因子的两个端值，得到(569.5)。

其 degree5 Bernstein 控制列是

$$
0,\ 0,\ \frac{h^2\delta_0}{20},\
\frac{h^2\delta_1}{20},\ 0,\ 0.
\tag{569.6}
$$

若 $D_2=\max(\|\delta_0\|_\infty,\|\delta_1\|_\infty)$，由 convex hull 性质可取

$$
\|Q-C_*\|_\infty\le\frac{h^2D_2}{20},\qquad
\|Q'-C_*'\|_\infty\le\frac{hD_2}{2}.
\tag{569.7}
$$

第二式来自5次 Bernstein 的相邻控制点差除以 h；中间差允许 $\delta_1-\delta_0$，不能漏其因子2。实现还对实际闭子区间用准确全部多项式系数计算 Bernstein 包围，通常比(569.7)更细，但不承诺一定改进。

(569.7)不是无条件精化收敛率；只有实际 $D_2$ 在相应序列上有适当控制，h 的缩小才产生相应结论。

## 569.5 原 literal cubic 的完整差

捕获的 PPoly.c 按 descending power、interval、全部 augmented columns 排列。对每个真实物理列，把它改写到 t 坐标仅需准确乘 $h^j$：

$$
C_{\rm lit}(t)=\sum_{j=0}^3 \widehat c_{3-j,i}\,h^j t^j.
\tag{569.8}
$$

这里 $\widehat c$ 是真实保存字的准确有理数，包含原浮点系数形成和节点差形成的全部效果；没有重新调用 SciPy。

完整差必须是

$$
Q-C_{\rm lit}=(Q-C_*)+(C_*-C_{\rm lit}).
\tag{569.9}
$$

第一项由(569.5)给出。第二项一般不为零，并且其来源同时包括原 physical/augmented 一阶数据差与原 PPoly 形成的舍入。新库不猜这些部分的大小，而直接对两份实际完整多项式相减。

对闭子区间 $[a,b]\subset[0,1]$，准确仿射换元后把全部 degree5 幂转换为 Bernstein 系数。其 convex hull 包含该段全部值；对完整导数多项式同做，得到逐列的准确上界

$$
E_{k,j}\ge\sup_{s\in I}
\left|\partial_s^k(Q_j-C_{{\rm lit},j})(s)\right|,
\quad k=0,1,2,\quad j=0,\ldots,D-1.
\tag{569.10}
$$

没有删高幂、均值或高频列。必要的标量 $E_k=\max_jE_{k,j}$ 来自这整组值，不是仅少量节点采样。

实现另记录 $C_{\rm lit}$ 两端与当前 Y/DY 的真实准确差。由于原 PPoly 系数是浮点形成的，其准确实解释可能存在微小右端点或一阶连接差；本文没有把这个 piecewise literal 对象宣称为准确 $C^1$ 闭面。每条闭片两侧都被覆盖，当前 Q 的准确 $C^2$ 连接仍只来自原共享 nodal 2-jet。

## 569.6 完整比较线段的真实 joint tube

只知道 Q 的系数盒合法，不能对另一个 C 使用其 Lipschitz 常数。新的比较盒逐列取

$$
\mathcal B_j=
\operatorname{hull}
\bigl(\operatorname{BernsteinRange}_I Q_j,\
      \operatorname{BernsteinRange}_I C_{{\rm lit},j}\bigr).
\tag{569.11}
$$

于是对每个 s 和 $\lambda\in[0,1]$，

$$
(1-\lambda)C_{\rm lit}(s)+\lambda Q(s)
\in\prod_{j=0}^{D-1}\mathcal B_j.
\tag{569.12}
$$

此处 Q 与 C 的关联被放宽为独立盒，只会扩大包含，不会漏掉真实线段。代码从全部真实系数计算这个盒；不接受调用者填入一个“已证明 tube”的口头标签。

scalar 仍来自同次已求出的准确 target return：

$$
A\in\mathcal A,\quad
\mu\in\mathcal M=\sqrt{\mathcal G_{ss}},\quad
\nu\in\mathcal N=\mathcal A_s\mathcal M.
\tag{569.13}
$$

这里 s 是原 numeric-$s$，$\mu=L_{\rm true}/L_{\rm numeric}$；不能用数值 profile 默认 $\mu=1$ 替代它。上述盒只覆盖准确 target tuple，尚不自动覆盖原 nominal tuple。

把(569.11)交给原 R553 complete_angular_box，按该原闭角单元全部频率形成 d/e，再准确外包

$$
W=|d\times e|^2,\qquad
P=A^2\mu^2W-\nu^2|d|^6.
\tag{569.14}
$$

这个 P 不应因后面的 metric 密度归一化而改动。按原 a1e 的实际 Frenet 公式，记 $q=|d|^2$，则 normal_raw 的平方范数为 $W/q$，$\kappa=\sqrt{W/q}/q$。因此原比率给

$$
\alpha=-\frac{\nu}{A\kappa}
=-\frac{\nu q^{3/2}}{A\sqrt W},\qquad
\beta^2=\mu^2-\alpha^2
=\frac{A^2\mu^2W-\nu^2q^3}{A^2W}.
\tag{569.14a}
$$

这一推导没有把任意盒中状态假定为已经满足 $|d|=A\rho$；它使用原参考RHS本身的 $\nu/A$ 定义。rho 已属于实际 angular geometry 与 target 的对应，而不是额外的 P 乘数。全模态 d/e 不删除，原 R553/R521 的 P 公式完整保持。

只有该实际盒证明 $A_->0,\mu_->0,P_->0$，才调用原 R521 四块 majorant。旧 quintic-only 的 $P_-$ 不复用。未隔出正下界只记本诊断未付，不影响原 metric/DFS/BVP。

## 569.7 局部角盒与完整有限 DFT 必须分开

单个闭角子单元的正域仅支付这个子单元。代码明确记录 full_angular_circle_positivity_not_inferred_from_this_one_cell。

对固定 s，必须从原完整终叶集合确认全部物理角圈被覆盖，并使同一 C/Q 线段在对应叶的 joint box 内。只有所有实际 DFT 角点及全列都落入已付的覆盖，才可按原 R553.8/R521 汇总最大常数，约束完整参考投影。一个叶的局部 majorant 不是全 N 点 DFT 的独立证明。

两个固定 $\sigma$ 的非负 majorant 具有同样的适用形式，但本文不从源码名称辨认原 worker 的 root/branch。反射保长度、Gram 和 P 的正性；需要讨论具体 Frenet binormal 取向时，仍须正确变换分支，不把反射的 orientation 因子省掉。

库没有自己的全域 DFS、分裂规则或 global-complete 标志。当前 caller 的全部闭 piece、两个反射片、角范围和 pending 责任依旧存在。

## 569.8 从全部系数差到真实几何一阶差

在共同物理角 $\phi$ 下，用原675相同的 Fourier 基和相同的注册定义 $F_Q,F_C$。记逐列值差上界为 $e_j=E_{0,j}$，导数差上界为 $f_j=E_{1,j}$。完整径向分量界为

$$
S_s=\left(
\sum_{j=0}^{M}f_{r_j},\
\sum_{j=1}^{M}f_{t_j},\
\sum_{j=0}^{M}f_{z_j}
\right).
\tag{569.15}
$$

包含随动圆柱基的物理角导数界为

$$
S_\phi=\left(
\sum_{j=1}^{M}(2j\,e_{r_j}+e_{t_j}),\
e_{r_0}+\sum_{j=1}^{M}(2j\,e_{t_j}+e_{r_j}),\
\sum_{j=1}^{M}2j\,e_{z_j}
\right).
\tag{569.16}
$$

因此在整个物理角圈上，

$$
\|\partial_s(F_Q-F_C)\|^2\le|S_s|^2,\qquad
\|\partial_\phi(F_Q-F_C)\|^2\le|S_\phi|^2.
\tag{569.17}
$$

它没有只看 r 或忽略 z0 的径向变化；t 的转动项也全部保留。共同 SE2 注册的旋转和整体下片反射保持这些范数；共同 translation 在差中准确消去。

物理角与材料角不能混淆。当前准确材料映射为 $\theta=\Phi(\phi)$，其导数

$$
\rho(\phi)=1+\sum_m(1-4m^2)c_m\cos(2m\phi)>0.
$$

所以物理角目标为 $G=\operatorname{diag}(\mu^2,A^2\rho(\phi)^2)$。这里的完整 $c_m$ 和严格下界 $\rho_->0$ 直接使用实际675对象已绑定的 field.rho_lower，即原R237的同core整圈证书；不新选密度、不设 $\rho=1$。只要同次 target 的 $A_-,\mu_->0$，

$$
\|(D F_Q-D F_C)G^{-1/2}\|_{\rm op}
\le\|(D F_Q-D F_C)G^{-1/2}\|_{\rm F}
\le
\delta:=
\sqrt{\frac{|S_s|^2}{\mu_-^2}
+\frac{|S_\phi|^2}{(A_-\rho_-)^2}}.
\tag{569.18}
$$

若使用 normalized $q=\phi/(2\pi)$，分子角导数与目标角长度同时多出 $2\pi$，该因子准确相消；$\rho_-$ 仍必须保留。这个几何差界本身不要求 Frenet P 正。P 未付时，源码仍保已付的多项式/几何差，不把它们一并删除。原(569.14)的 Frenet P 公式不另外乘密度，因为其 d/e 已是实际物理角导数；这与相对 metric 归一化必须用 $A\rho$ 是两项不同责任。

若另外已经有同一闭单元、同一 target 的真实 $\epsilon_C\ge\|G^{-1/2}(D F_C^\top D F_C-G)G^{-1/2}\|_{\rm op}$，则由矩阵平方差得

$$
\epsilon_Q\le
\epsilon_C+2\sqrt{1+\epsilon_C}\,\delta+\delta^2.
\tag{569.19}
$$

这里只是已有两项严格上界的条件组合。原 solver RMS 不满足 $\epsilon_C$ 的输入含义；代码也没有从 RMS 自动填它。

## 569.9 同材料图、全相位与跨级比较的边界

上述 Q 与 C 使用**同一次当前场**的材料映射、完整 core、注册与相位规则，不拿两个不同 refinement level 的 q 标签直接相减。

同一个可逆角参数换元同时拉回两个 Gram 与 G，广义谱不变；共同刚转亦保 Gram。因而若原全角覆盖和 R443/R447 的共同材料 conjugacy 条件真实满足，(569.18)—(569.19)可以传到该对场的全 $t\in[0,1]$。根据是同时拉回与整角覆盖，不是断言固定 g 在任意角重标下逐字不变。

跨 level 的第一次材料图仍要使用 $\Theta_j^{-1}\Theta_0$ 的正确方向和真实 B/material receipts。本文没有执行或替代这项注册，也没有靠本引理新选 H/W/marker。

## 569.10 原残差、FFT 形成误差及非线性投影缺陷

令 $V_\sigma(y;A,\nu,\mu)$ 是准确 Frenet 点态速度，$\Phi_N$ 是使用完整 N 点均匀角和原全列投影的准确有限参考。定义

$$
r_C=C_{\rm lit}'-\Phi_N(C_{\rm lit};A,\nu,\mu).
\tag{569.20}
$$

在同一 scalar tuple 和已付的完整比较 tube 中，有准确恒等式

$$
Q'-\Phi_N(Q)
=r_C+(Q'-C_{\rm lit}')
+\Phi_N(C_{\rm lit})-\Phi_N(Q).
\tag{569.21}
$$

因此原 R521 的条件式可实际使用本次得到的 $E_0,E_1$ 与整个比较段的 $K_y$：

$$
\eta_Q\le\eta_C+E_1+K_yE_0.
\tag{569.22}
$$

新增库支付后两项的真实输入和比较路径责任；它没有生产 $\eta_C$。

原实际 sample 若只给 rounded residual，仍必须分别支付：

- literal PPoly 精确求值与其实际浮点评估字之间的状态/导数形成差；
- FFT synthesis、normalization、sqrt、projection 及 residual norm 的形成差；
- original nominal scalar 与准确 $A,\nu,\mu$ 的差及其比较路径；
- sample 到完整闭径向单元的 fill distance 和真实导数界。

R521 的 closed_cell_residual 已给这些量的使用式，本次没有把任何一项填零。保存原整条 rms_residuals 只保原证据，不证明其采样估计等于连续上确界。原 c6a frozen_physical_residual 的两个额外节点项及系数 .05 仍是原有限检查，不替代上述形成误差。

还有一个独立的有限投影缺陷。即使(569.22)为零，也只有系数 ODE 精确；真正几何速度仍满足

$$
\partial_s F_Q-V_\sigma(F_Q)
=\mathcal S\bigl(Q'-\Phi_N(Q)\bigr)
+\bigl(\mathcal S\Phi_N(Q)-V_\sigma(F_Q)\bigr),
\tag{569.23}
$$

其中 $\mathcal S$ 是完整有限 Fourier synthesis。Frenet 的除法与平方根一般产生高频；不能因为 Q 只含有限频率，就认定第二项为零。有限 DFT aliasing、非线性 Fourier 截断和点态几何缺陷依旧要真实外包，或由原 R519/R459 直接全角六jet/metric 消费者支付。

这正是本文不把新 source 诊断升级为等距验收的原因，而不是添加新的前门。

## 569.11 完整闭面范围

本实现只给实际 prefix 上 C/Q 的局部比较。Q 的尾、cut correction、collar、反射连接及两帽仍是原准确场；原完整 metric 继续逐 piece 使用原 target 和 field。

不能把一个只在 prefix 定义、甚至逐片连接有微小误差的 $C_{\rm lit}$，拼上 Q 的旧 tail 后就称它是合法完整比较闭面。cut jet、atlas 和帽连接若要纳入另一个全域比较，需要其真实相容构造。本库没有这样做，也不输出 reach、held 或 quotient distance 证书。

## 569.12 临时表示、预算与失败

捕获完整数组仅存在原同job的全量临时目录，采用明示 <f8/shape/bytes/SHA 的全文件表示，不上传 Git，不编码成必要正文。±0 的原字保留；准确有理计算只在数值解释中把两者视为同一个实数零。

运行中的计算均使用原 caller 的 budget_check，没有新钟。资源异常不能被捕获为普通数学失败。每次 local comparison 都携带原完整 cell 地址；本库不弹出或删减原 DFS frontier。

捕获目录的 quiet、必要 readback、单90000B、超限70和 cleanup 均尚须实际外层登记。没有因为库提供了 result.json 就默认可清理；也没有宣称完整 PPoly 数组会进入90KB正文。未来 reader 可以传完整身份、实际 bounds/错误/未访，但必须明确原全量数组仍在临时原件。

源只含一个实际库，不复制 R521 的数值 majorant，也不另造 solver/target/metric。在实际入口未接之前，本结论是可调用的来源与包含实现，不是既有运行已付的诊断。

## 569.13 已完成与仍未付

本次已证明并实现：

1. 真实捕获原 solve_bvp 返回 PPoly 的透明接口与同一次 accepted CP 的完整字绑定；
2. $Q-C_*$ 的准确因式与全列界；
3. 不依赖共享一阶或精确 PPoly 接缝假设的 $Q-C_{\rm lit}$ 完整 Bernstein 差；
4. 包含两条真实曲线及全部比较线段的系数盒和可调用原 R521 正域/常数；
5. 全物理角、同注册的真实一阶几何差，以及条件 metric 传递；
6. 原 cubic residual、FFT/nominal 形成差、有限非线性投影缺陷的准确分责。

仍未有实际 capture、actual field 或任何数值误差值；当前入口未注册本库，原 sample formation、全角投影缺陷、全闭域比较和 metric floor 没有被本纸证自动支付。原真实精化继续使用原同 g、全参数与 t 范围、全域 metric 测量；固定阈值多次通过仍不等于误差持续下降。
