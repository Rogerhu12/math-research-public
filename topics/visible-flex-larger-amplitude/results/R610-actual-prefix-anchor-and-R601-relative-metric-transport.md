# R610：同一实际前缀的入口锚、完整径向输运与 R601 到相对度量的消费

作者：ChatGPT /root（AI）。日期：2026-11-16 UTC。

**可信度：已证明（限本文完整数学推导、实际已绑定对象与源码接点的条件结论）。** 本条新增完整源组件，将 R601 已形成的同一准确前缀速度缺陷，沿实际 R553 完整覆盖与真实首节点接到 R514 相对 Gram 界。尚未实际执行该新组件，没有新数值常数、accepted450、完整闭面证书或误差精化结论。它不新增原 BVP/native/FD/fullDN/metric 接受门。

## 1. 已有结论与本条真正补齐的责任

[R514](R514-complete-field-defect-transport-and-literal-residual-transfer.md) §514.3–5 已证明角长输运、Gram 矩阵控制和带全部模式权的入口锚。[R601](R601-actual-analytic-projection-and-saved-RHS-world-C1-defect.md) 已把同一真实 R580/R596 对象的准确全角投影、全部 alias 和保存 RHS 形成差接成物理角导数缺陷，但明确未形成目标正分母、入口锚或径向积分。本条不把这些已证公式另换编号冒成新理论；新工作是**把那些空接口落实为同一次已绑定场的数据和原遍历责任，并给出完整条件消费证明**。

新增源：

| 路径 | UTF-8 字节 | SHA256 |
|---|---:|---|
| computations/geometry_20261116_actual_prefix_R601_metric_transport.py | 31602 | 4b49ea2a80ef8215d04fda4d607f6bb288a31728c927e0beddbec56f1da6d4fe |

完整接口见[配套 notes](../notes/2026-11-16-actual-prefix-anchor-R601-metric-interface.md)。本组件没有 CLI、独立 workflow 或独立扫描；调用者必须已拥有真实 R601、同一原 R553、原 metric kernel 和原 budget callback。若其中责任未付，返回明确不可用而继续保原 metric 结果。

| 已有对象 | 完整源身份 | 本条消费的真实成员 |
|---|---|---|
| R601 | 23113 B / 12450be1cbdd289b69f74535d98fa42586506709244ed066b338c98cd494490d | 已实际返回的 complete_prefix_bound；同一 analytic/saved/tubes/current；原 finish 状态 |
| R553 | 24412 B / 81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b | 同一原 cell 的 scalar_box、全部 terminal 计数、已付正界 minima |
| 原 Active | 33310 B / 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b | 真实 prefix_coefficients/prefix/registered_world/material_angle/evaluate |
| 原 metric kernel | 35473 B / a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17 | 原 physical q 与完整材料密度的尺度约定 |
| 原保存场内核 | 16911 B / 51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0 | 被实际 saved loader 检查的完整 R237 材料正界来源 |
| R596 | 56627 B / 8a242686845844df64d248b7b9fd47096ff2c7a8c2044346c85fc9b7425afb3f | 已绑定完整 checkpoint 原字节；physical/core 数组及 exact_word/row_words |

动态 M 的 saved loader 不是强塞旧112源。其真实类模块、完整文件身份以及同一对象 checked source_sha256 均记录；当前 loader 必须在自己已检查的完整来源闭包内。R601/R596 已绑定真实 full checkpoint、实际 3M+2 全数组、当前 target 和同 job，不能换一个相似名字的 saved 对象来提供锚。

## 2. 同一当前场，而非旧数值 renderer 或未付修补

原 Active 的 prefix 先从实际完整共享节点构造各分量准确有理五次 Hermite，再合成全部偶频与两个 mean，最后施加同一个常量 proper SE2 registration。它的原 evaluate 对下片只作全空间竖向反射。

R416 accurate-cut 子类修改的是 cut_targets 与 expression_identity。当前 refined C leaf 重新构造该类型，仍保相同 prefix/nodal/core/density/registration/rho 与原径向节点；它不把旧切口系数用于新目标。R610 进一步在真实对象上要求上述五个方法的 __func__ 就是已经核过完整 SHA 的 Active.ExactFiniteField 对应函数。仅仅 prefix_coefficients 的名字相同不足以通过这个来源绑定。

因此本文的场 $F$ 是当前 accurate-cut 对象的**实际完整前缀限制**。在前缀上没有遗漏一个尚未计入 R601 的 cut patch；它不等于宣称 native/collar/切口区也由同一前缀式覆盖。

场的真实原字节由同一 R596 绑定：physical_states、physical_rhs、augmented、augmented_rhs、core 和 mesh 均与实际 checkpoint 的完整 array identity 一致；actual Hermite 的前两组 nodal 数组还与对应 physical/Y、physical_rhs/DY 全字节核过。R610 首节点直接读这个 R596 对象已保存的完整 physical/core 字节，再核 actual field 首节点与所有 core。它不再求 field six jets、不调用 target、不执行 DFT/FFT、也不把原 BC 浮点最大残差作为准确锚。

首节点读取包含全部 3M+2 行。竖向 mean 的物理角导数恒为零，但其原字节仍读入、返回准确值及全数组身份；它没有从 R601 径向缺陷中删除。负零原词保在数组字节身份中，准确有理零只是该已绑定词对应的实数，不冒 binary64 词完全相等。

## 3. 正确的物理角单位与固定准确目标

固定同一个真实 C 族成员、全部十个准确参数和当前场。记数值前缀坐标为 $s\in[0,L_{\rm num}]$，物理角为 $\phi$，完整材料映射为

$$
\Theta(\phi)=\phi+\sum_{m=1}^{M}\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
\qquad
\rho(\phi)=1+\sum_{m=1}^{M}(1-4m^2)c_m\cos(2m\phi).
$$

所有 $c_m$ 来自该当前 checkpoint，不以旧 M96 的数值端点替代。原 loader 已按 R237 完整 core 三角界支付全圈严格正下界 $\rho_-$，本组件只消费那个实际正界，并核它与 field.rho_lower、saved.rho_lower_exact 完全一致。

原 metric kernel 的真实式是 $q=\phi/(2\pi)$、$\Theta_q=2\pi\rho$。其 angle_density 返回 $\Theta_q$ 的外包，不能直接把这个对象填成 R514 的 $\rho$。本组件始终用物理弧度角；R601 的 C1 字段同样明确以 $\phi$ 为导数坐标。因此后续没有遗漏或重复乘除 $2\pi$。

准确目标为

$$
g=\mu^2\,ds^2+A(s)^2\rho(\phi)^2\,d\phi^2,\qquad
\mu=L_*/L_{\rm num},\qquad
A(s)=a_*(\mu s).
$$

$L_*$ 是同 C 语义准确长度，$L_{\rm num}$ 是实际 mesh 的末端准确提升；不令二者相等。对整个原允许根族，外包必须同时成立。R553 同次 scalar_box 的 $\nu$ 是准确弧长导数乘同一 $\mu$，因而是这个 $A_s$；没有以 numeric ap 的标签替代它。

R610 绑定 actual field.x[0]=0、末端正数 $L_{\rm num}$，并核其与 current.target.numeric_length 相等。只读这个实际数值坐标长度，不选择 target 区间中点当新真实长度。

## 4. 沿原 retirement 取得入口目标，不重查目标

R610 只增加一个原 cell retirement 的旁路消费者。对每个原 prefix cell，R553 已 inspect 完成、原 split 决策已作出、R553 原 commit 已执行后，把**同一个 cell、同一完整 R553 diagnostic 和原 split 布尔**传给 retire。新组件不决定 split，也不为取得更窄锚再询问一个 $[0,0]$ target。

每个 terminal diagnostic 内原 scalar_box 保存：

- actual_same_target_return，包括原 numeric s 区间、准确半径外包和实际原 target-return identity；
- 原 A、mu 及 joint P/W；
- 原完整 coefficient tube、全角范围、可用/错误状态。

组件核实际 committed/split/terminal 计数与 R553 逐步相同，且 last_observed_address 就是当前 cell。terminal 必须来自同一可用完整 diagnostic；其半径区间、原 numeric s 区间与该 cell 明确相等。split 行把责任交给原全部子格，不用父格极值假付终态。

对所有实际 terminal 且左端为零的 prefix cell，其完整目标半径区间都包含同一个准确族的 $A(0)$。令这些区间为 $I_j$。组件保存

$$
I_0=\bigcap_j I_j=[A_{0,-},A_{0,+}].
$$

**证明其合法。** 固定任一允许成员 $\zeta$。原同次 target 返回保证 $A_\zeta(s)\in I_j$ 对该整个闭 cell 的径向区间成立；因为 $0$ 是其闭端点，$A_\zeta(0)\in I_j$。每个 $j$ 对同一允许族均成立，故 $A_\zeta(0)$ 在交集中。交集不选中点，不交换根成员，也不把一个角格的状态系数当另一个角格。若交集为空则来源/外包责任不可用，不能制造正分母。证毕。

完整原根计划覆盖全部闭前缀片、整角圈和两片；原闭四叉细分保端点。完整终态覆盖必有第一片 $s=0$ 的 terminal cell。组件仍要求实际 entry_cells>0，不能从计划存在就填出未访问锚。它返回候选总数、首末实际 witness 与区间；每行完整 retirement 保在同一临时原 ledger 中。necessary 只给原 ledger 身份和完整责任结果，不冒完整 ledger 已逐行运输。

## 5. 实际首节点的全模式入口锚

直接提升 R596 已验证的首节点原 binary64 词，得到

$$
(r_0,r_1,\ldots,r_M,t_1,\ldots,t_M,z_0,z_1,\ldots,z_M).
$$

令 $n_m=2m$，现场按准确有理数形成

$$
b_0=r_0-1,\qquad b_{t,m}=t_m+n_mr_m,\qquad b_{c,m}=c_m-r_m .
$$

不假设 $b_c=0$，不假设入口高度全零，也不依据一个约 $10^{-11}$ 的打印 BC 值推这些准确残差。完整 core/状态关系若真为零，由原词的准确算术自己给出。

在未注册旋转框架，逐项对原全部 Fourier 表达求角导数：

$$
F_\phi-\rho e_\phi=
\left(
-\sum_m b_{t,m}\sin(n_m\phi),\
b_0+\sum_m((n_m^2-1)b_{c,m}+n_mb_{t,m})\cos(n_m\phi),\
-\sum_m n_mz_m\sin(n_m\phi)
\right).
$$

常量 registration 把等式两边同乘一个实正交矩阵，平移导数为零，所以下面的范数界同时适用于实际 registered field。

由实际完整 density 形成

$$
\rho_+=1+\sum_{m=1}^{M}|(1-n_m^2)c_m|.
$$

每项取绝对值得 $\rho(\phi)\le\rho_+$，无需新角网格。用 §4 的实际入口半径外包定义

$$
\begin{aligned}
B_r&=\sum_m|b_{t,m}|,\\
B_t^0&=|b_0|+\sum_m((n_m^2-1)|b_{c,m}|+n_m|b_{t,m}|),\\
\epsilon_A&=\max(|1-A_{0,-}|,|1-A_{0,+}|),\\
B_t&=B_t^0+\epsilon_A\rho_+,\\
B_z&=\sum_m n_m|z_m|.
\end{aligned}
$$

对同一个目标成员，$F_\phi-A(0)\rho e_\phi$ 的三个旋转分量绝对值分别不超过 $B_r,B_t,B_z$。反三角不等式给

$$
\left|\frac{|F_\phi(0,\phi)|}{A(0)\rho(\phi)}-1\right|
\le
q_0:=
\frac{\sqrt{B_r^2+B_t^2+B_z^2}}{A_{0,-}\rho_-}.
$$

这是 R514.13 的全部前提在真实对象上形成的值；式中 $A_{0,-}>0,\rho_->0$ 来自当前原覆盖/loader。没有把 $A(0)$ 默认为1；若返回区间不窄，$\epsilon_A$ 会真实扩大锚。完整模式残差列表的身份、原字节身份、全部实际和式、两 mean、首末 target witness 与向外平方根结果都保留，不以 identity 自身冒一个数值证明。

本界不保证很小。尤其小 $\rho_-$、高模式权、当前入口误差和宽 $A_0$ 外包都会放大它。这是真实估计结果应当揭示的限制，不能借换目标、缩模式或丢项掩盖。

## 6. 消费同一个已完成 R601，不再次 finish

原调用者继续拥有 R601.summary 的唯一科学完成调用。R610.summary 接受它实际返回的整个 necessary 对象，并与同一个 R601 对象的状态核对：

1. 完整 binding 与 actual describe 相同，原 summary_calls=1，原 finish_started真、pending空；
2. 两个原 R580/R596 summary 与实际对象缓存逐值相同，完整 C0/C1 bound 与 last_completed_composition 相同；
3. 原 error/stop/close_errors 为空，没有 recovery 或旧 formation_error；
4. 原 coverage 真正 completed_all_DFS_work，原完整 ledger 与 R601/R580/R596 同一身份；
5. 原 R601.validate_complete_originals 对该同一 coverage/ledger 的检查保持；
6. R610、R553、R580/R596 的原 observed/committed/split/terminal 责任相同；每个 terminal 都付清，实际入口存在。

R610 **不调用 R601.summary**，也不重复 R580 的指数/alias 完成算术。该检查是当前必要消费者确认自己消费的对象，不能从一个 caller 提供的 $B_0,B_1$ 数字或 source SHA 推成完整原结果。

若真实 ResourceStop 或 MemoryError 在新界形成过程中发生，它们按原异常通道传播；原 caller 记录 actual stop 后可再次进入 R610 的 halted metadata 分支。该分支不重算入口、不重算 Gram、不重开 R601 finish。以前完成的界若存在，只以 previous_completed_bound_not_current_after_a_stop 保存，当前 complete 标志为假。普通数值/来源错误记录真实类型、消息、traceback、未完成操作，保持新界不可用；不转成原场被数学否定。

## 7. 完整前缀上的正分母与径向积分

同一 R601 返回的原界记为

$$
\|r\|_\infty\le B_0,\qquad
\|\partial_\phi r\|_\infty\le B_1,\qquad
r=F_s-V_+(F;A,A_s,\mu).
$$

它已经包含 R596 完整有限重构残差和 R580 全无限尾/全部整数 alias；C1 中还包含旋转到 world 框架的连接项。这里不再次把某个局部有限角离散范数冒成 $B_1$。

原 R553 全部 paid terminal minima 给同一完整域上的

$$
A\ge A_->0,\quad \mu\ge\mu_->0,\quad P\ge P_->0,\quad W\ge W_->0 .
$$

R610 只在 §6 完整原终态责任成立时消费这些 extrema；partial/observed extrema 从不升级为全局界。$P,W$ 保证 R514 准确 Frenet 速度在该域合法，$|F_\phi|>0$。

令 $h=|F_\phi|/(A\rho)$。由 R514.8，

$$
|\partial_s h|\le\frac{B_1}{A_-\rho_-}=:T.
$$

完整闭前缀片通过同一节点二阶 jet 拼接，$h$ 沿实际 $s\in[0,L_{\rm num}]$ 连续且分片可微；合法域及 C2 前缀给所需积分恒等式。对每个完整角和每个目标成员，

$$
|h(s,\phi)-1|
\le q_0+\int_0^s T\,dx
\le q_0+L_{\rm num}\frac{B_1}{A_-\rho_-}=:q.
$$

这里取的是已付全域常界乘真实整个路径长度，不把不同角的 DFS 已访问子集拼成一条假路径。原 complete coverage 含每个角、所有 prefix spans、所有 seam 和闭端点，因而这条全径向路径确实在域内。无需新增公共径向网格或第二次 sweep。

同时

$$
|r|/\mu\le\delta:=B_0/\mu_- .
$$

$L_{\rm num}$ 只在积分中出现一次；$\mu=L_*/L_{\rm num}$ 已在原 Frenet/scalar 中出现。不能把长度当成 $L_*$ 再漏掉或多乘一次比例。

## 8. 相对 Gram 算子界及向外舍入

用实际 $\delta,q$ 定义

$$
a=2\delta+\delta^2,\qquad
b=\delta(1+q),\qquad c=2q+q^2 .
$$

R514.11 对同一个当前场直接给

$$
\left\|g^{-1/2}(F^*e-g)g^{-1/2}\right\|_{\rm op}
\le
\eta_{\rm prefix}
:=
\frac{a+c+\sqrt{(a-c)^2+4b^2}}{2}.
$$

为使这份应用独立可读，归一化 Gram 误差的三个量分别满足

$$
\left|\frac{|F_s|^2}{\mu^2}-1\right|\le a,\qquad
\left|\frac{F_s\cdot F_\phi}{\mu A\rho}\right|\le b,\qquad
\left|\frac{|F_\phi|^2}{A^2\rho^2}-1\right|\le c.
$$

第一、二式用 $F_s=V+r$、$|V|=\mu$、$V\cdot F_\phi=0$；第三式用 $h\ge0$ 及 $|h-1|\le q$。对单位向量逐项取绝对值，由非负矩阵 $\begin{pmatrix}a&b\\b&c\end{pmatrix}$ 最大特征值得上式。没有额外 $q<1$ 假设，也没有以分量最大值冒算子范数。

代码所有输入是准确有理端点。平方根使用同一原 R521 的完整有理向外 sqrt_bounds；正比值、和、乘积再用原 R580 relative_dyadic_bounds 上端点。每个形成步骤前调用同一原 budget callback。先向上放大 $\delta,q$ 使 $a,b,c$ 逐项不小，随后再分别向上舍入也合法：非负对称矩阵的最大特征值关于非负各项单调，可用 Rayleigh 商中绝对值向量直接证明。因此代码即便用向上后的 $a,c$ 形成 $(a-c)^2$，也是对**该放大矩阵**的准确谱公式，而非错误地宣称平方差对每个输入单调。

新界不调用未知准确等距解或全 BVP 逆定理。它界定当前场自身；取得某个很小的原 RMS 既不是输入替代品，也不会自动使本界小于 $10^{-6}$。

## 9. 反射、材料坐标与全相位的准确范围

原上片作常正交 registration 不改变上述 Gram/向量范数。原完整下片为竖向反射，目标对应相同，故同一个 Gram 界适用。若用速度缺陷来解释反射下片，正确支是 $\widetilde\sigma=\det(J)\sigma=-\sigma$；不能把下片仍称作未变的原上片正支。代码明确记录这个区别，不借它识别 native DtN worker 的支。

对任意合法坐标变换，同时拉回 induced metric 与同一 target，广义特征值及相对算子范数不变。因此已有原共轭/首材料 API 可以在其真实来源绑定和完整覆盖成立时使用本界。但**本组件没有调用那个 API，也没有新形成当前 full-phase 同构记录**，返回中保留这项未付。它不以独立固定 N DFT 与任意角平移“可交换”代替实际 material pullback。

完整闭面还包括 native/collar/accurate-cut patch、两帽及所有接缝；本条不把前缀上界冒成全闭面最大值。帽目标与帽 induced metric 的原身份也需原绑定先成立。reach、held-image amplitude、含反射非刚性和完整闭面 $D$ 均不由本式产生。

## 10. 预算、异常和完整必要正文

构造时绑定的 callback 就是同一 R601/R596/R553 原对象 callback，无新 wall clock、子进程、owner allowance 或清理权限。retire 只是沿原决策保存短元数据和实际区间；逐模式锚、原平方根及最终谱界都在原科学剩余时间内。该少量工作仍会消耗原真实资源，不承诺资源截止点或 elapsed 与未接此组件相同。

summary 原样保留**完整实际 R601 necessary**，包括原 R580/R596 全部错误、unpaid、unknown、已选择的原完整范围；不挑成功字段。新 summary 另给自身 binding、retirement 计数/链身份、首末 unpaid、实际 anchor、全域下界、完整每一步上界、错误与未完成操作。它没有改原 source/science 单份90000字节上限或70语义。

未来完整 caller 若在同一必要对象里另保同一 R601 全体，可使用明确命名、同体完整可逆的相等共享并比较整个最终正文；本组件本身没有压缩任意树、切包或上传 raw 的通道。实际正文仍可能超限；如果如此，不能把完整界已经在 runner 内形成称作正文已经运输或允许清理。

没有实际科学 run 在本条写作中执行。本地只作者源码、文字推导与 UTF-8/哈希元数据；没有 Python import/AST/compile/数值求值/fixture。未来正式 caller 必须在公开本仓库 Actions 的真实 computations 中绑定原完整来源，按实际终态另记 run/head/job/参数/必要身份。

## 11. 条件消费定理

**定理。** 假定未来公开 Actions 用本条完整源绑定原实际 R601/R553/R596/Active/kernel、当前完整保存场和准确 target；原完整 DFS 责任与所有本条同对象/同原值检查成立；同一个 R601 已首次返回完整 $B_0,B_1$；新组件在原预算内返回 complete_prefix_relative_metric_bound=true。则它返回的 complete_prefix_relative_Gram_operator_upper 是该同一当前准确前缀、完整闭径向区间、整角圈和两反射片相对原准确 target 的统一算子范数上界，对原允许 C 族全体成立。

**证明。** §2 保当前准确前缀与真实首节点一致，§3 保 target、完整材料正界和导数单位。§4 所有 entry 区间对同一族的 $A(0)$ 成立，其交集仍成立；§5 全模式三角界支付 $q_0$。§6 拒绝 partial、stale、recovery 或不同对象的假完整输入，使 §7 所用 $B_0,B_1,A_-,\mu_-,P_-,W_-$ 均来自同一原完整覆盖。§7 的全实际径向积分给 $\delta,q$；§8 的准确 Gram 不等式和逐步向外形成给返回上界。§9 的原反射保持 Gram。各步骤均按原完整域统一外包，因此同一允许族中任意成员成立。证毕。

该定理是来源与计算的条件命题，不预告未来所有检查都会返回、不预告该上界小，也不把 field source pin 或 job success 本身当作理论前提已数值支付。没有完整非零112/338/450、全闭面误差 floor 或 README 比例结论在这里新增。

## 12. 紧接的实际工作

完整组件现在可直接登记；不等待独立审查、fixture 或机械重跑。未来完整 caller 在已真实消费 R601 的同一 full metric 路径接 retire/summary，保所有旧来源与原判据、原 clock、原必要/cleanup。这份接线与实际执行结果必须独立记录，不能改已结束的 run 或将旧 partial 记作 R610 已执行。

随后仍需真实完成共同材料/全相位消费、尾部及准确 patch 的相应缺陷与 cuff 锚、原完整闭面接受与同目标实际精化。原 open.md 的全几何和振幅责任继续保留。
