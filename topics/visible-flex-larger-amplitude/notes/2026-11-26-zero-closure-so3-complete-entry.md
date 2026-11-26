# 独立零闭合 SO(3) 完整求解入口：数值根、隐式一阶导数与真实几何

日期：2026-11-26。来源：本会话 geometry 分支的完整源码与独立静态复核。此文登记一个新的、可在公开 Actions 执行的完整数值入口；不登记任何尚未返回的数值根、低误差候选、连续证书或完成结论。

数学条件定理使用 [R695](../results/R695-so3-zero-closure-bubble-uniform-IFT.md)。本文说明该证明与实际代码之间的接口，没有重复登记 R695 的解析结论。

## 1. 新表示及其固定输入

真实参考输入是独立的完整 R690 轴对称单位子午线。它包含原五次前缀、解析延续、完整 Hold 和深谷无穷尾，不是把旧优化场的径向导数改名为新参考。完整参考制备源、实际参考 bundle、载体、原标量输入和符号节点报告均经 SHA-256 绑定。当前原始离散域保留 $M=160$、$J=923$、完整 $N=2048$ 角网格以及全部原 legacy/Gauss 观察行。这些数量来自所绑定制备及主算子接口，尚不是本入口的实际成功返回。

固定目标是同一个精确

$$
g=ds^2+a_{\rm deep}(s)^2\,d\theta_0^2,
\qquad
\theta_0(\phi_0)=\Theta_{\rm initial}(\phi_0).
$$

当前全部自由 core 系数仍可变；固定的是材料坐标图 $\theta_0$。当前 normal angle 由 $\Theta_c(\phi_c)=\theta_0$ 确定。目标半径函数、原精确 $S$、仿射符号节点、冻结坐标图和前三个固定 core 系数不随方向重新选择。参考制备实际返回的完整 profile identity 才是后继使用的 identity，不预填旧分支的 `383168...`。

`so3_zero_closure_endpoint_operator.py` 组合真实 `so3_axisymmetric_meridian_operator.py`。组合时分别核对实际 source bytes、全部模型 canonical hash、参考源和完整 scalar definition。`context.scalar_identity/scalar_definition` 是独立参考的真实 API，本层不构造伪造的旧 `context.deep`。

原自由向量完整保留：全部原自由 core、所有共享五次径向/完整 Fourier 旋转变量，以及最后的自由 $H$。新增的三个端点根坐标是这些变量的隐函数，不作为独立自由场，也没有删去原变量。

## 2. 两个六轴 bubble 与三个端点根

在同一精确区间 $[0,S]$ 的内部指定两个互不相交的 bubble 支撑。每个 bubble 用上升的 $S_5(u)=10u^3-15u^4+6u^5$ 和下降的 $1-S_5(u)$ 拼成，支撑外为零。三处接点的值及前两导数相容，所以是完整 $C^2$ 函数。代码使用其实际数值载体，精确 $S$ 和载体之间的误差仍须在连续消费者支付。

每个 bubble 都有三个 world 旋转轴，共六个原控制方向。R695 的固定端轴右逆把它们限制到一个三维端点校正参数 $z(\phi_0)$，没有限制原 $\omega$ 变量。令两个 bubble 的精确质量为 $m_1,m_2$，在冻结 frame 中定义

$$
G_{\rm end}^{-1}
=\frac{e_r e_r^\top}{m_1^2}
+\frac{e_\theta e_\theta^\top}{m_1^2+m_2^2}
+\frac{e_z e_z^\top}{m_2^2},
$$

$$
Q_1=m_1[e_z]_\times G_{\rm end}^{-1},
\qquad
Q_2=-m_2[e_r]_\times G_{\rm end}^{-1},
\qquad
W(s,\phi_0)=b_1(s)Q_1(\phi_0)+b_2(s)Q_2(\phi_0).
$$

先用完整原变量构造 $T_y=\operatorname{Exp}([\omega]_\times)T_0$。新单位场及端点方程为

$$
\widetilde T
=\operatorname{Exp}([Wz]_\times)\,T_y,
\qquad
C(y,z)=\Gamma_c-P_{\rm cap}+\int_0^S\widetilde T\,ds=0.
$$

这里是 **world 中的左乘旋转**。新物理场为

$$
F=P_{\rm cap}+\int_S^s\widetilde T\,du.
$$

它不再包含 $h\Delta$。在精确单位输入、精确积分和精确隐式根的定义下，$F_s=\widetilde T$，故径向 Gram 误差恒为零。完整数值残差仍实际计算并保留径向、交叉和角向三个 Gram 行，不会把浮点径向行直接写成零。

此表示存在一个连续、光滑且对称的根分支，仍需 R695 的同场条件或其他完整证明。代码没有把成功的有限数值 Newton、一个正的 sampled singular value 或一个小端点残差提升为该证明。

## 3. 真正求根以及明确的失败返回

每个新完整自由向量、每个实际 binary64 角地址，都从字面零开始求三个端点变量。它不从另一个候选或邻近角的根猜测一个未登记的分支。每次 Newton 使用同一个完整端点积分和实际三乘三 Jacobian，并作逐角的下降回溯；只有完整实际数值残差达到显式容差才返回。

数值策略由 `EndpointPolicy` 明示，包括 residual tolerance、迭代次数、回溯次数、Armijo 参数及端点坐标开球半径。开球半径定义这次尝试的局部分支范围。它不是已经验证的 R695 收缩球，代码也不要求未计算的 IFT 常数先通过人为设置的检查。

以下任一实际失败都会拒绝该候选：非有限方程/方向、线性求解失败、超过实际根预算、在声明球内没有下降回溯，或返回根的真实数值残差超标。失败不会被替换为零根，不会宣称全局无解。若首场就失败，完整 driver 先写出 `complete=false`、`actual_initial_read_error`、实际根诊断及绑定身份，再重新抛出真实异常。后继可据实际返回改变输入、bubble、工作精度或恢复方向继续。

`root_line_search_evaluations` 记录真实整批端点方程的角求值数。当前实现回溯时实际计算整个角批，所以计数支付整个批，而不是只计仍未接受的角数。

## 4. Newton 图与隐式导数完全分开

数值 Newton、其回溯以及得到的根/角导数都在 detached 数据上执行。完整一阶参数导数来自同一当前点的隐式方程，并不对有限迭代次数求导。

设 $Z=(z,z_{\phi_0},z_{\phi_0\phi_0})$，用真实旋转的完整角 jets 构造总导数方程

$$
R_0=C,\qquad
R_1=\frac{d}{d\phi_0}C,\qquad
R_2=\frac{d^2}{d\phi_0^2}C.
$$

度量只需 $(R_0,R_1)$ 的六维系统，几何 six-jet 使用九维系统。源直接对这个实际系统装配 $R_Z$，保留 R695 的所有下三角耦合，没有把三个角导数当成独立常数。

实际数值根 $\widehat Z$ 给出如下保值的一阶隐式替身：

$$
Z_{\rm used}
=\widehat Z-
R_Z^{-1}\bigl(R(y,\widehat Z)
-\operatorname{stopgrad}R(y,\widehat Z)\bigr).
$$

其 forward 值逐字仍是 $\widehat Z$，一阶参数导数为 $-R_Z^{-1}R_y$。$R_Z$ 使用当前实际数值根处的 detached 小矩阵，没有 Newton 迭代的 autograd 边。$R_y$ 包含全部 $\omega$、全部自由 core、当前 $H$、完整积分、角 jets 和 core 逆图链。

这个替身只声明完整的一阶参数 J/J*。不能把它再次用作真实二阶参数 Hessian 的自动微分图。当前完整 R664 positive residual-Hessian 桥只需要原 J/J*；其中 `functional.jvp` 的 reverse-over-reverse 是对辅助 cotangent 的求导，不要求替身具有正确的二阶参数导数。

数值根处的隐式线性化与精确根处的 J 之间仍有误差责任，小 residual 不使这项自动消失。真实线搜索继续重新计算候选物理场和完整几何，不会以线性模型替代实际接受条件。

## 5. 全 core 逆图以及完整六 jet

当前 core 的 normal angle 也采用明确分离的数值求根和一阶隐式替身：

$$
\delta\phi_c
=-\frac{\delta\Theta_c(\phi_c)}{\rho_c(\phi_c)}.
$$

该导数保留所有自由 core 系数。在固定材料坐标下，

$$
\Gamma_{\phi_0}=\rho_0 e_{\theta_c},
\qquad
\Gamma_{\phi_0\phi_0}
=\rho_0' e_{\theta_c}
-\frac{\rho_0^2}{\rho_c}e_{r_c}.
$$

代码对上述完整表达式使用当前隐式 $\phi_c$，不会只保前三个固定 core 或把当前见证点的导数删掉。

对固定端轴矩阵，令 $Z_0=[e_z]_\times$，则

$$
W_{\phi_0}=\rho_0[Z_0,W],
\qquad
W_{\phi_0\phi_0}
=\rho_0'[Z_0,W]+\rho_0^2[Z_0,[Z_0,W]].
$$

因此旋转参数的完整角 jets 是

$$
w=Wz,\quad
w_{\phi_0}=W_{\phi_0}z+Wz_{\phi_0},
$$

$$
w_{\phi_0\phi_0}
=W_{\phi_0\phi_0}z+2W_{\phi_0}z_{\phi_0}
+Wz_{\phi_0\phi_0},
\qquad
w_s=W_s z.
$$

所有 Rodrigues 系数及其一、二阶导数采用真实固定 base 源的同一求值函数。新输出六 jet 是 $F,F_s,F_{\phi_0},F_{ss},F_{s\phi_0},F_{\phi_0\phi_0}$，保留前式全部项和 world 旋转语义。

数值部分积分与总积分使用原 base 的完整 Gauss/部分插值权重。端点 root 的总积分采用与该 base 相同的实际求和次序。数值积分给出的 $F$ 和另外计算的精确定义导数之间仍有离散求值误差；本文不把部分积分的插值式宣称为已经严格微分一致的连续包围。

## 6. 完整求解器与几何选择

`fullclosed_zero_closure_so3_qp.py` 是完整独立 body。其来源是已经锁定的独立轴对称 base driver，不是运行时 monkeypatch，不是重标签旧 report。纯源码派生器检查原完整源的 SHA，并逐 AST 核对：

- 原完整几何 scan、任意点读取、原 192 selection、world cotangent、双符号幅度和 mmap 追加算法均保持不变，只把几何构造器改为真实 zero 模型与实际来源绑定。
- 原 CommonSlackRows、QP helpers、全变量母范数接口及其它未列出的完整函数保持不变。
- driver 的改动局限于完整参数/输入、实际 zero 组合、完整来源与状态报告、真实 base seed 的地址历史读取以及首场失败记录。

原几何前缀通过原字节的 e783 selection 和 a2a 纯曲率微分复用，后接完整选定幅度行。标记直径预算、body 预算、两见证符号、全部自由 core 的见证点导数、cap/H 行以及每个原自由变量均保留。旧 selector 对原前缀的零梯度行仍可能诚实抛错；本文不声称所有原零梯度情况已经由 Phase I 自动处理。

真筛读全部原网格和所有已提供/永久追加的曲率、半径地址，并保存真实新极值。每个地址仍读双符号见证距离。旧历史 binary 角值按已登记规则读作新冻结 chart 地址，不声称跨模型为同一物理点或继承旧证书。同一个直接 base 的 seed 地址保留同一个冻结 chart，但改变物理表示后仍全部重读。

有几何正违约时，完整公共 slack Phase I 保留全部 typed 原行，只在真实新场的完整最大正违约严格下降时接受恢复，slack 值不能充当物理可行性。进入 metric phase 后，仍要求实际同一谱目标下降、正 Gram 数值域和全真实几何筛通过。新的端点根失败按真实 trial failure 回溯，不会被线性可行结果覆盖。

## 7. seed、继续与报告身份

首入口可以直接用准确独立参考的完整原变量初值。显式新 $H$ 种子来自同一参考制备的完整工作积分，它仍是自由变量，不被称为精确积分值。

可选 `--seed-so3-checkpoint` 与 `--seed-so3-report` 接收一个真实完整 direct $h\Delta$ base 的末态。它必须同时匹配实际 base driver source、完整 base model、同参考 bundle、同 profile、同载体以及真实 checkpoint bytes。全部原变量被复制到新 zero 表示，所有来源历史地址继续保留；重新计算新物理场 baseline，旧 $\Phi$ 或几何不会转移。

真正相同 zero 模型的继续使用 `--restart-checkpoint` 与 `--restart-report`，两种输入方式互斥。bubble 节点、所选分支半径、完整原域及全部 source/model 都进入新数学模型身份。数值容差和积分阶数单独登记为工作求值参数，不能改写固定 $g$。

`read_zero_closure_so3_report.py` 只作 stdlib JSON/source/byte 归因，不重算 $F,J$ 或 raw 数组。它完整核对 zero → direct base → reference 的三层 canonical/source/profile 身份，保留每个 metric/Phase I 方向、真实 trial 几何、初场失败及未返状态。

当前根诊断与跨所有尝试的累计统计分开。`current_all_grid_angle_roots_available` 只是当前数值缓存覆盖，不是全角连续根证明。base 原 core 路径未被调用，其 untouched inf minimum 不写成伪测量：metadata 明示 `base_core_inverse_path_used=false`，两项未执行 core 统计为 null；本层实际 core 根统计独立保存。共享 low-level 计数的作用范围也明确登记。

## 8. 首次完整 Actions 参数

配套 `zero-closure-so3-complete-ready-steps.json` 给出完整 solver 与 attribution argv。首次声明的两个相对 $S$ bubble 三元组是

$$
(1/64,1/32,3/64),
\qquad
(61/64,31/32,63/64).
$$

这是显式新输入选择，不声称当前场满足 R695 的定量球条件。首次工作根策略为 residual tolerance 2e-12、最多 24 次 Newton、每次最多 18 次回溯、Armijo 1e-4 和端点坐标球半径 0.5。全域保持原 $N=2048$、每胞积分阶数 8、角批 8，母范数 jet-sum、径向长度 .05、角过渡 24，显式 $\mu=.01$、$p=4$。它是一条真实全变量 metric direction，最多 16 次 QP advances，并保留至多四条完整 Phase I 恢复方向，各最多 64 次 advances；这些是首预算，不是完成或不可能结论。

新完整代码只在 Rogerhu12/math-research-public 的公开 GitHub Actions 上求值。目前本地只完成源字节操作、AST/compile、完整纯源码派生核和独立静态审查，没有运行科学 fixture、伪造输入或计算实际候选。真实 reference/solver/report/bundle SHA 由该次 Actions 返回，未返时保持未返，不以预期值替代。

## 9. 仍必须由同场证据完成的责任

R695 的 uniform root 条件、角连续性、正 $\rho$、完整积分及符号节点载体误差、数值 implicit-root/角 jet 误差、连续 Gram 上界、嵌入、held、reach、全 $t$ 和同一固定问题的精化仍各有完整责任。数值 radial row 小或形式上的精确径向恒等式都不自动完成这些责任。

这个入口把 R695 的零闭合支变成可真实求解的独立表示，保留原完整约束和全部变量。它不宣称已构造精确 flex，也不把新表示失败当成目标课题的障碍或停止理由。

## 10. 实际依赖的导入修正版本

本次首次执行参数绑定独立参考的导入用途修正版本：provider `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`，完整 direct base `7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf`，direct seed driver `606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`。对应真实参考输出目录是 `axisymmetric-R690-reference-v2-first`。zero endpoint 与 geometry 完整字节不变；zero driver/launcher 的所有完整函数 AST 不变，只刷新封闭 source registry 和精确 driver SHA。此前零闭合源尚无科学执行；不把依赖修复当成新的数学结论或实际 root 返回。

## 完整执行源与参数

|完整文件|字节|SHA256|
|---|---:|---|
|`so3_zero_closure_endpoint_operator.py`|49540|`5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46`|
|`so3_zero_closure_geometry.py`|45504|`7698fd89e1b739391e2139c6c88dacd0c3b3d8be614fd65e435508420326b385`|
|`fullclosed_zero_closure_so3_qp.py`|53929|`b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b`|
|`launch_zero_closure_so3_actions.py`|11595|`27414140270a0fb1a9533a21a0bd28a46988c55aecd9952c38e7c05512b64166`|
|`read_zero_closure_so3_report.py`|26123|`b25e5a5f370e69fe8164d835a608b1845db926d2488939dc9bafaa3bba0a6857`|

完整首次参数实际刊于 `computations/resume-20261126-zero-closure-so3-first-steps.json`，排在同一03运行的实际v2参考准备之后。纯读出沿已实存reference作为控制器输入身份，只有报告真实complete时才校验final；初场失败可如实读回。控制器摘要只取实际scalar叶子，保留完整reader JSON的方向/trial记录在runner，不更改科学argv、源或预算。
