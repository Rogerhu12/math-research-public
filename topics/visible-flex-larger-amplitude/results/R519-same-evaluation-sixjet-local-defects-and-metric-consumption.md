# R519：同一次准确六 jet 的局部缺陷诊断与原完整 metric 消费

作者：ChatGPT（AI 协作）。日期：2026-11-16。

**结论性质：条件包含证明与可执行源码接口，尚无本次科学执行。** 本文把 [R514](R514-complete-field-defect-transport-and-literal-residual-transfer.md) 中不需要全局稳定常数的局部公式，接入已刊 R459 的同一次准确 target / field 求值。它不将原 solver RMS、BC 或 native 阈值改称闭场 metric floor，不重扫闭域，不增加原 BVP、FD、metric 或 refinement 的接受门。

## 519.1 实际边界及最小实现

原 R459 的 Measurement.target 在一次现成查询中已经得到准确目标半径、prefix 的准确一阶 scalar jet、径向 metric 和实际材料角密度。其 base_once 紧接 current.evaluate 得到三个 Cartesian 分量的完整六 jet，然后计算原 Gram。phase_grid 也已经调用实际 common-material 的完整六 jet API。因此局部诊断可消费这些已返回对象，既不重复 current.evaluate，也不增加 target.closed_range、C bounds、C refine 或 material inverse 调用。

本次公开三运行件是小有理端点 helper、透明字面 source generator 和单 view 计划。Generator 仅以原 R459 的完整固定字节加 17 条显式计数替换，生成一个新的真实 source basename/schema。原 R459、其数学消费者、当前原件以及正在运行的请求均不改。原 direct Gram 结果与所有判断表达式保持：新值不参与 available、norm_interval、原 parent-bound 交、split、全域上界、series 比较或任何 native/FD/接受判据。

| 角色 | 文件 | 字节数 | SHA256 |
|---|---|---:|---|
| 局部有理端点 helper | geometry_20261116_same_evaluation_sixjet_defects.py | 15385 | f70474b3857b3decc0542ae50b5c32b107532cc739e529e818ec7264dfe1f2b4 |
| source generator | root_20261116_same_evaluation_sixjet_source_view.py | 9950 | 4ebd9c6a387bce5e4d0c377c17f0a6895f3b6bbc6acfff58b3dff72b4c80d18a |
| 单 view 字面计划 | R519-same-evaluation-sixjet-source-view-plan.json | 18003 | e600977365ec57e527886065fc00823b26c1b75aee92f206ab2e0532187a8d32 |
| 仅 Actions 生成的实际 consumer | geometry_20261116_same_evaluation_sixjet_metric_evidence.py | 69439 | 8159e9f2e2d28fb31d27c719b54581d1db32b14935edefefec5b1730eda14781 |

生成 baseline 为 geometry_20261116_fixed_target_complete_metric_evidence.py，62091 字节/494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05，已刊提交 1f8213c7bd64ed064f959eca10c0ab5d4c973a0c。当前材料 helper 仍为 R457 的 059d0df3ab5957b8ba5adf69e305ee4663ba06378242fe4c5f2116bab437af41 原件，其真实 JET_NAMES 为 value,u,q,uu,uq,qq。

完整生成文件不作为新增 Git 文件；计划是正常源文本替换，既不是大科学数组编码，也不是从旧科学 SHA 恢复状态。所有新单件都小于 100000 字节。没有新 workflow、job、参数点、初猜、科学 run 或 dispatch。

## 519.2 固定同场、同目标和局部条件

在已有准确闭片上取当前实际场 $F(x,q)$。径向坐标 $x$ 是 base prefix 的原数值长度坐标、common-material prefix 的公共 $u$，或 tail/collar 的原 $r$；不能互换标签。该次已绑定准确目标为

$$
g=\mu(x)^2\,dx^2+A(x)^2\theta(q)^2\,dq^2,
\qquad A>0,\quad\mu>0,\quad\theta>0,\quad \partial_x\theta=0.
$$

这里 $\theta$ 是原 current material 的 $\Phi_q$ 或同次 common-material 查询的首材料 $\Theta_{0,q}$。原材料绑定已限定其准确表达及正性，不能以另选角盒、中点或重投影替代。

令

$$
d=F_q,\quad e=F_{qq},\quad X=F_x,\quad Z=F_{xq},\quad Q=d\cdot d.
$$

本次完整收到六 jet 的 18 个区间分量，但局部公式只用 $X,d,Z,e$；不伪称使用了不需要的第三阶导数或数值差分。所有区间来自这一次 field API 的原向外 bounds，helper 不再求值其表达式。

半径和径向 metric 的来源严格分开：

- Base prefix：$k=L_\ast/L_{\rm num}>0$，$A=a_\ast(kx)$，$\mu=k$，$A_x=k\,a_{\ast,s}$。原 closed_range 返回 $a_\ast,a_{\ast,s},a_{\ast,ss}$ 和 $k^2$。
- Common-material prefix：$x=u$，$A=a_\ast(L_\ast u)$，$\mu=L_\ast$，$A_u=L_\ast a_{\ast,s}$。原 target 先按真实数值坐标求同一范围，再将 $g_{11}$ 乘 $L_{\rm num}^2$；诊断使用这个已转换后的 $g_{11}$，不漏链式因子。
- Native/collar：$x=r$，$A=r$，$A_x=1$，$\mu^2=E_C(r)$。它直接消费原完整同 C query 的区间，不以 Bprime 或旧 cut 三盒代替。

Prefix 各候选分片/共享端点、所有十项控制、准确长度 DAG、同 C 全 root family 均随原 closed_range 保留；诊断只做向外区间组合。它没有改变哪个准确目标成员被定义。

## 519.3 直接可用的角长度和径向局部缺陷

当 $|d|>0$ 时定义

$$
h=\frac{|d|}{A\theta}.
$$

由于准确材料密度不随 $x$ 变化，逐式微分得

$$
\partial_xh
=\frac{d\cdot Z-(A_x/A)|d|^2}{A\theta|d|}
=:\tau.
\tag{519.1}
$$

该式只需要原二阶混合 jet $F_{xq}$；没有求 $F_{\phi\phi\phi}$，也没有假设当前 Hermite 场满足某个原 ODE。Helper 用完整闭 cell 的有理端点外包形成 $h$、$h-1$、$|\tau|$；若 $|d|$ 的正下界未隔离，只将 $\tau$ 诊断标为未付，原 direct Gram 继续。若 $h$ 已可包围而 $\tau$ 尚不可，两个范围分别记录。

这些是当前准确场本身的局部导数事实。它们尚未给出某条完整径向路径上的积分、入口 BC 锚、patch/collar 的全局累积或 solver 残差至该场的稳定性常数。不能把已观察局部最大值称为全闭域 supremum，也不能从若干 cell 的 $\tau$ 值宣称 $h$ 在整个闭场接近 1。

## 519.4 两个代数 Frenet 参考速度

进一步令

$$
C=d\times e,\qquad W=C\cdot C,\qquad B=Qe-(d\cdot e)d,
$$
$$
P=A^2\mu^2W-A_x^2Q^3.
$$

只有已取得严格 $W>0$、$P>0$ 的整个当前闭 cell 外包，才构造

$$
V_\sigma=\frac{\sigma\sqrt P\,C-A_xQB}{AW},
\qquad \sigma\in\{-1,+1\}.
\tag{519.2}
$$

恒等式 $d\cdot B=d\cdot C=B\cdot C=0$、$e\cdot B=W$、$|B|^2=QW$ 立即给出

$$
d\cdot V_\sigma=0,\qquad
e\cdot V_\sigma=-\frac{A_x}{A}Q,\qquad
|V_\sigma|^2=\mu^2.
\tag{519.3}
$$

本次分别包围两个 $\sigma$，不从某个区间中点或当前数值方向选择“正确根”。这里的 $V_\sigma$ 是在这次准确 $F$ 的一、二 jet 上构造的代数参考；**没有将任何一个标为原 worker 的 root、平方根分支、原 IEEE RHS 或其误差**。缺少原分支绑定时仍可使用 (519.3) 作局部 Gram 比较，但不能改称原 ODE 残差已得严格估计。

若 $P$、$W$、$A$、$\mu$ 的正下界未隔离，输出明确原原因和该诊断的未付范围。这既不更改原 solver guard，也不证明原准确目标无解。特别地，若 $g_{11}$ 已严格正，但有限 square-root 工作精度尚给不出正的根下端点，只记录精度所致的诊断未付，不把目标自身标作不正。

## 519.5 在真实材料坐标和反射下的合法性

不必先数值反解到物理角再做一次 field 求值。若 $\phi=\Theta(q)$，$\kappa=\Theta_q>0$，$\ell=\Theta_{qq}$，且 $\Theta$ 与 $x$ 无关，则

$$
d_q=\kappa d_\phi,\quad e_q=\kappa^2e_\phi+\ell d_\phi,\quad
Q_q=\kappa^2Q_\phi,\quad C_q=\kappa^3C_\phi,
$$
$$
W_q=\kappa^6W_\phi,\quad B_q=\kappa^4B_\phi,\quad P_q=\kappa^6P_\phi.
$$

将这些代入 (519.2)，分子分母的 $\kappa^6$ 完全消去。因此直接用原 $F_q,F_{qq}$ 的同次 jet 是同一个代数参考构造，不额外要求第三导数或有限 Fourier 重投影。

正交反射会交换两个 $\sigma$ 的标签；准确旋转保留它们。由于本次始终保两个参考分支，lower 反射和 common-material 旋转不被漏掉，也不形成某个全局连续 solver 分支的选择。Prefix 从数值长度坐标到公共 $u$ 的正比例变换同时变换 $F_x,A_x,\mu$；其正因子也在归一化缺陷中相消，但 $\tau$ 自身必须按真实径向坐标作链式变换。本次 actual target context 已明确标记该坐标，避免只改标签。

原 base metric 的全部 closed roots、两侧及反射责任继续由原 root plan/DFS 保持。两完整帽的原 target 同一恒等式不需要 (519.2)，仍沿原 cap_metric_identity；本次不为帽增加 Frenet 正性条件。

## 519.6 同 cell 的条件 Gram 上界，不替换原上界

设已证

$$
\delta_\sigma\ge \frac{|X-V_\sigma|}{\mu},\qquad
q_0\ge |h-1|.
$$

由 (519.3)，当前 normalized Gram 差的三个分量可分别控制为

$$
a=2\delta_\sigma+\delta_\sigma^2,\qquad
b=\delta_\sigma(1+q_0),\qquad
c=2q_0+q_0^2.
$$

于是

$$
\left\|g^{-1/2}(F^\ast e-g)g^{-1/2}\right\|_{\rm op}
\le
\frac{a+c+\sqrt{(a-c)^2+4b^2}}2.
\tag{519.4}
$$

证明使用 $|X|^2-\mu^2=2V_\sigma\cdot(X-V_\sigma)+|X-V_\sigma|^2$、$X\cdot d=(X-V_\sigma)\cdot d$ 和 $|d|/(A\theta)=h$；绝对分量被非负对称矩阵 $\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)$ 控制，其最大特征值即 (519.4)。无需 $q_0<1$。

Helper 对区间加减乘除使用准确 Fraction 端点，平方根用整数 isqrt 在声明的 sqrt_bits 下向外包围；没有 float 中点。在可用参考的地方分别给两个 $\delta_\sigma$ 与上界。丢失依赖只会扩大包围；这些新上界 **不与原 direct Gram bound 取 min、不用于分格停止、不用于 series 的 strict decrease**。因此本次没有在原科学判断中悄悄增加一个新条件或改写数值接受。

## 519.7 实际源码调用与未付责任

生成 view 的 base_once 顺序仍是原 budget check、原 target、原 field.evaluate、原 Gram 和 relative_norm。然后才将已在内存的六 jet 与同次目标交给 helper。原 target 未返时只记录这一原因，不补求场。原 live-C refine 若依既有逻辑重算 base_once，诊断也明确记录那次新的原求值，不把两次实际求值计成唯一状态。

phase_grid 在原 common-material 六 jet 和原 target 返回后使用同一对象；prefix 的 value,u,q,uu,uq,qq 正确转为 helper 的 value,x,q,xx,xq,qq 位置序。它不再调用 material inverse、field、target 或 C。原 common-material 对象、全部 piece membership 与 $t=k/n$ 遍历不改。

每次完成的诊断记录附在对应原 temporary cell/phase ledger，保 observation index、完整原 cell 或 t/witness/piece 地址、局部区间、正性未付原因及错误。原 domain/phase transaction 尚未提交时，一个已经返回的局部 observation 也不能代替原 transaction：summary 明确二者不是同一计数。

必要读回只保小计数、各局部量已观察最大上界及其真实地址、首末未付观察、原因计数、完整原诊断 ledger 身份，以及原 complete-coverage-and-pending 身份。全部未付 cell 和未访 root suffix/stack 仍由原 R459 coverage / ledger 保存；不把计数声称为这些正文已全回传。原 field/target/Gram 失败和预算前未开始的 cell 不会伪造六 jet 或诊断成功。Setup 尚未完成时只给 binding_not_completed，不伪造 diagnostic receipt。

原信号处理器只置标志，在下一个原 budget check 抛 ResourceStop；新增观察的写账/计数使用同一过程，不新开 clock 或线程。硬终止仍由实际外部 owner 处理，没有新的 quiet 或 cleanup 成功声明。整个诊断工作也消耗原总钟；它不承诺在相同预算完成与旧运行一样多的 cell。

## 519.8 范围与实际缺口

当前 source view 只注册原 R459 的三个真实 field family：original112、resolution112、completeM，且保其原完整 source tuple。它没有注册 R504 refined-leaf/query 源、R464/R463 incrementalM 或任何未来来源；不能把本次一个 view 的完成说成当前 217/union 已接。

未完成的责任包括：完整径向 $\tau$ 积分、真实 BC 锚包围、所有 patch/拼接的积累、原 rounded solver/RK/FD/reconstruction 到当前准确场的稳定传递、原 worker 分支的误差，以及任何全闭 metric floor、精化极限或非零接受结果。本次不为获得这些更强结论添加一个新前门；原 R459 直接 Gram 测量在它的原条件下仍独立有效。

新的 measure 输入仅增加一个明确 bool：sixjet_diagnostic_enabled。禁用时原求值与科学判断保持；启用但局部不合法时该诊断如实未付。原 work、c_queries、time_grid、实际同源绑定、18900+2700 绝对钟、单90KB必要输出、compare 与 readback CLI 均保。

这是一条实际可调用的 source 组合，不是未接函数清单：generator 生成真实新脚本，随后该脚本的 measure 主流程实际运行上述旁调用，finish/necessary 实际返回它的范围和来源。尚未指定新输入、执行或运行编号，不能填入任何新数值。
