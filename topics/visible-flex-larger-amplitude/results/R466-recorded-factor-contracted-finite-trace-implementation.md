# R466 — 实际记录因子的完整有限轨迹切向收缩实现

AI 作者：ChatGPT（OpenAI）；日期：2026-11-16。  
状态：独立源码与条件实现说明；未在本地执行、导入、解析 AST、编译或测试任何科学程序。实际数值范围只能由后续公开 Actions 给出。

## 466.1 已付结论与本次唯一数值改动

[R465](R465-recorded-factor-backsolve-defect-and-complete-column-contraction.md) 已在提交 $f454d36788c6efbdb375b4239b54c03c56e1fc7a$ 发表，原文 $19378$ 字节、SHA256 为 $6f9200ea16b08f8305b29c15d6f5712d67c747c4a5f6d27ef8f7b202f835c347$。该证明的对象是由实际保存的因子、两次回代结果和原 literal Gram 结构确定的局部名义系数系统。它没有证明新旧 binary64 运算逐词相等，也没有把一般舍入缺陷的导数置零。

本实现把实际195的一个耗时切点替换为这个系统的另一数值实现：在每个原求根器真正接受的内部更新处，先共享形成完整的系数矩阵，再应用全部 $224$ 个方向。原195显式因子导数与两次回代导数的函数原文保留，只用于本次明确规定的数值回退。零次更新返回不进入收缩 helper。

原 noJ 根求值、原停止与回溯分支、实际保存的 $R,z,s$、原角上 $F$ 与 $C$ 的不同表达式、完整 RK/cusp 时序、$226$ 态和两个 mean 均保留。原当前 $H$ 的完整 R273 候选、十档真实 noJ 接受判据、完整 $338\times112$ 响应、物理 FD、full-DN、末 Jacobian、敏感度和 audit 继续由原调用链执行，源码存在不等于这些责任已实际完成。

本次后继选用与195相同的 actual119 第三批六参数和 $\lambda=0.001$，重新生成未接受初猜；它不恢复已清理的195现场。具体公开入口是独立 request208，实际结果编号 R467。

## 466.2 精确基线与新数值范围

实际195固定来源为提交 $4ad7fb771218585af1091c9d322c9d61b64a949c$。其切向 kernel 为：

- 文件：geometry_20261115_original64_finite_trace_variation.mjs；
- 大小：$11427$ 字节；
- SHA256：$742ab15a2168084167eeab9879a074ee1cd586d33f324e837223134a8cbf9705$。

新实现由以下四件核心组成，全部是独立新文件：

| 角色 | 新文件 | 字节 | SHA256 |
|---|---|---:|---|
| 完整收缩 helper | geometry_20261116_recorded_factor_contracted_solve.mjs | 11427 | 2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59 |
| 真实有限轨迹局部切向 | geometry_20261116_original64_contracted_finite_trace_variation.mjs | 12270 | e6be662ba5c795d4e3f91bbcead469482c746520b36b1d4c14a1c49b00dd2bb6 |
| noJ 匹配的完整 RK 传播 | geometry_20261116_original64_contracted_finite_trace_flow.mjs | 9412 | c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7 |
| 原求根观察与实际导入接线 | geometry_20261116_original64_contracted_finite_trace_loader.mjs | 10758 | 65f6e211342c608844dc91a4570ba61d1365cf72c39abea75fac792bb4d0f916 |

helper schema 为 original64-recorded-factor-complete-column-contraction-v1。变分 schema 为 original64-recorded-factor-contracted-finite-root-variation-v1；实际 worker 的 backend 为 original64-noJ-primal-recorded-factor-contracted-finite-root-variation-v1。这些新身份不会把新运算顺序标成实际195的旧实现。

完整七件协议/当前系统薄源、进程 wrapper、必要 reader 与参数闭包见[request208总接口](../notes/2026-11-16-request208-recorded-factor-contracted-finite-trace-complete112-interface.md)。所有既有原始磁盘源码保留；新 loader 的原根观察插入与195相同，仍可逐字逆回原 capacity-adapted 根源码。

## 466.3 原记录与局部模型

令 $J=113$、$K=224$、$B=225$。一次实际接受根更新保存：

$$
R\in\mathbb R^{J\times J},\qquad z,s\in\mathbb R^J,
$$

其中 $R$ 是原 solveSPD 返回前保存的下三角 Cholesky 因子，$z$ 是原 forward substitution 的实际结果，$s$ 是原 backsolve 的实际结果。它们只读。原方向形成给出 $f=dF$ 和全部 $\gamma=d\beta\in\mathbb R^{B\times K}$。

R465 的名义方程为

$$
XR^\top+RX^\top=D,\qquad
Xz+Ru=f,\qquad
X^\top s+R^\top v=u,
$$

其中 $X$ 下三角，$D=dC$ 按原 $225$ 个 moment 的 literal 结构形成。设

$$
E_0=RR^\top-C,\qquad a_0=Rz-F,\qquad b_0=R^\top s-z.
$$

正对角邻域内的明确局部模型

$$
R(C')=\operatorname{chol}(C'+E_0),\qquad
z(C',F')=R(C')^{-1}(F'+a_0),\qquad
s(C',F')=R(C')^{-\top}(z(C',F')+b_0)
$$

在基点复现记录，且导数正是上面三式。因此这里的常数缺陷是被定义的局部模型系数；这不表示原浮点算法沿邻域的舍入误差实际保持常数。

一般光滑缺陷仍满足

$$
(RR^\top)\,ds
=dF-(dC)s+da+(dR)b+R\,db-(dE)s.
$$

本源码不估计这些一般缺陷的导数，也不由未付的 IEEE 导数推导根接受性。R465 的一般缺陷公式和实际方向残差公式继续适用。

## 466.4 实际 backsolve 缺陷的形成与显式投影

原先若直接按普通 binary64 点积计算 $R^\top s-z$，可能先把准确非零缺陷舍成零。本 helper 对每个有限输入 word 解码：

$$
x=m\,2^e.
$$

normal 的整数 significand 包含隐含首位，指数为原 exponent bits 减 $1023+52$；subnormal 指数为 $-1074$。符号并入整数。对每个 $i$，所有 $R_{ji}s_j$（$j=i,\ldots,J-1$）与 $-z_i$ 使用 BigInt 按共同二幂指数准确相加。这里只处理已保存 binary64 words 的准确有理值，不调用新的根、RHS、角采样或科学模型。

随后把该准确 dyadic 数显式投影一次到 binary64。若绝对整数的 bit length 为 $\ell$、共同指数为 $e$，最高位指数为 $e+\ell-1$，量子选择为

$$
q=\max(e+\ell-1-52,-1074).
$$

需要右移时，代码比较完整余数与半量子，tie 按保留整数的奇偶舍入；需要左移时准确补位。因此 subnormal 直接按 $2^{-1074}$ 的量子舍入，不先作一次 normal 舍入。无进位时，投影整数至多占 $53$ 个二进制位；向上舍入可能恰好进位成 $2^{53}$，其二进制写法占 $54$ 位，但它是准确二幂。因此这个整数始终能由 Number 准确表示，再乘二幂。在有限可表示范围内，该最后缩放准确。核心 helper 注释中的“53 significant bits (including a carry)”按有效精度解释，包含这个准确二幂的进位情形，不表示其整数 bit length 仍是53。

准确零约定为 $+0$；准确负非零投影为零时保留 $-0$。但这种非零损失不能作为收缩中的 $b=0$：整组 $J$ 个分量统计完后，该次更新改用保留的原195显式方向函数。投影溢出同样回退。一般非零且非精确的有限投影允许继续，但原统计明确累计 changed components；没有宣称其误差严格界已付。

本节证明的是该整数表示/投影算法的范围。源码未在本地运行，不能把算法说明写成运行观测。

## 466.5 全部 literal Gram 槽的共享形成

原 Gram 结构保持

$$
C_{00}=1+\beta_0,\quad
C_{0i}=C_{i0}=\sigma_2\beta_i,\quad
C_{ij}=\delta_{ij}+\beta_{|i-j|}+\beta_{i+j}\quad(i,j\ge1),
$$

其中 $\sigma_2$ 使用原表中的实际 sq2 word；没有重新求 $\sqrt2$，没有用另一个 cosine 乘积恒等式替换原表。$T_k=\partial C/\partial\beta_k$ 共 $225$ 个。

helper 用实际 $R$ 数值形成下三角逆 $A$。记其第 $i$ 行转置为 $a_i$，并形成

$$
v_i=\sum_{j<i}b_j a_j+\tfrac12 b_i a_i,\qquad
Q_{ik}=a_i^\top T_kv_i.
$$

代码对每一行严格执行：

1. 向槽 $0$ 加 $a_{i0}v_{i0}$。
2. 对 $j=1,\ldots,i$，向槽 $j$ 加 $\sigma_2(a_{i0}v_{ij}+a_{ij}v_{i0})$。
3. 对全部有序 $(r,s)\in\{1,\ldots,i\}^2$，把 $a_{ir}v_{is}$ 同时加至 $|r-s|$ 与 $r+s$ 槽。
4. 当前行结束后才把 $b_i a_i$ 加进供下一行使用的 prefix。

有序对不可改成只取一个三角而不补完整权重。$1/2$ 来自 Cholesky 共轭式中 $\Phi$ 的半对角，并不把原 Gram 额外乘半。

另按同一结构形成 $S_s$，满足 $S_s\gamma=(dC)s$。实现只通过原 $s$ 和上述槽索引形成它。共享矩阵为

$$
\Gamma=S_s-RQ.
$$

若完整准确 backsolve 缺陷确为零，$Q$ 项可省；这是一项准确代数简化，并非把普通舍入得到的零当成准确零。

这里的 $A,Q,\Gamma$ 在执行中仍是 binary64 数值矩阵。因此准确实数推导并没有免除形成它们的舍入误差。新 source/policy 和必要摘要均明确 roundoff bound 未付。

## 466.6 全 $224$ 列应用、原回退与部分事务

对全部列 $c=0,\ldots,223$，helper 形成

$$
h_c=f_c-\Gamma\gamma_c,
$$

再使用同一个实际保存的 $R$ 作 forward 和 transpose-backsolve，返回

$$
v_c\approx(RR^\top)^{-1}h_c.
$$

没有把它替换为 $C^{-1}h_c$，没有重新分解一个理想 $C$，没有只做少数列。原 root 更新仍逐分量为

$$
dL_{\mathrm{next}}=dL-\alpha\,v,
$$

其中 $\alpha=2^{-k}$ 来自该原求根器真正选中的 backtrack，$k$ 的原范围和验证不变。只有完整返回后才替换当前 $dL$ 并增加原 differentiated_accepted_updates 计数。

收缩内部非有限算术、记录因子数值不可用或准确非零缺陷投影丢失，触发专用 NumericalFallback。这种回退只重走原195的 differentiatedOriginalSolve 原文，不改变 root、$F/C$ 形成、任何 residual 阈值或接受状态。原函数自身的有限检查/资源错误继续直接传播。

资源 deadline、来源/tape 尺寸错误和任意非专用异常不在回退捕获范围。由于新路径只读 primal 与输入方向数组，部分预组装、部分方向应用或原回退异常不会把部分新方向提交为完整切向。资源检查仍调用原 variation 的同一个绝对单调钟，不另开预算。

预组装形式的工作为 $O(J^3)$，应用全部方向为 $O(J^2K)$；它不构造 $J\times J\times K$ 的因子导数张量。该量级是循环结构的纸面说明，不是测得的速度或整个 job 峰值内存保证。原角形成与完整状态传播的成本仍存在。

## 466.7 原有限分支和完整 RK 责任

原根最多运行30次迭代、每次最多20档内部回溯；成功 normal/fallback 返回实际记录0至29次接受更新。第30次接受后若走出原循环，仍是原 iteration-limit throw，不能被新 helper 当成成功返回。

原零更新路径仍直接返回目标导数 $Dt$，不调用收缩 helper。原 split RHS 仍逐角形成完整 $226\times224$ 局部方向：

- 全 $112$ 个形状块与 $112$ 个动量块；
- 第一个 mean 的真实形状导数；
- 第二个 mean 的完整零形状导数行。

mean 行不能因其某些导数为零而删除。完整 RK 状态仍是226维；传播矩阵保留两个 mean，mean 不反向馈入原 shape 方程。

flow 源保留原四个 noJ 根/RHS 调用，先完成每个原 RK step 的 primal，再消费其真实 tape。原 $h a/2$ 括号、cusp 分割、局部 profile 与坐标时序未改。原 RHS/根不因切向 phase 重执行。新实现改变方向后，后续 nonlinear solver 可能选择不同状态，所以“不修改同一输入下的 primal 路径”不等于“整次新旧运行轨迹逐词相同”。

R412 已记录 actual195 在零 $H$ 阶段完成后，首个正 $H/64$ 的 withJ 在 stage368 因资源预算停止，尚无正基点完整 J、R273 correction 或原 native trial。该零阶段已有27772个零更新根返回；本次 helper 不进入零更新路径，不能据此声称消除那部分耗时。实际性能和后续接受均待新 job。

## 466.8 原 full112 与终端接受责任保持

实际调用链是：新显式 runner → 新 full112 adapter → 新 height path → 新 TailClient → 原 capacity import → 新 finite-trace loader → 新 current-R273 hook → 原 worker。loader 的 manifest 同时绑定新 helper/kernel/flow/loader 四源；hook 在实际 root 与 split 已加载后核这四件并保存真实 source receipt。source 身份检查不替代数值接受。

新 full112 adapter 继续通过原当前 $H$、相同 worker 的完整 endpoint J 和原 FD，再调用未改数学正文的 full-DN。原 $453$ 个 augmented unknown、$341/112$ 左右边界、$338\times112$ 高度响应及原二阶有限差分公式全部在同一链中。

收缩统计不能证明任何未返的 endpoint J、完整 FD、最终 sensitivity 或 audit。当前 native 的原32次迭代/十档真实 noJ、$2\times10^{-9}$ 阈值、外层8方向/17档内试步以及原 RMS/BC/物理域判据均不减。helper 没有产生新的 native pass 字段，也没有用代数模型范数代替真实 noJ residual。

## 466.9 必要读回与退出语义

新统计保留原 root/line/accepted-update/complete-local-J 计数，并附：

- contraction 调用、共享形成、完整返回的实际整数计数；
- 准确 backsolve 缺陷分量与非零分量计数；
- 显式投影 changed/lost/overflow 分量计数；
- 原显式 fallback 开始/完成及实际原因计数；
- 每 engine 最近一次更新/最近一次 fallback 的真实 iteration/backtrack 与是否完整返回。

完整逐更新 fallback history 没有记录，必要 reader 明确这一范围。它只按实际整数 metadata 求和，不重算根、方向、范数或误差。每个完整原 native call 的累积统计都不被误称为新的独立当前 J。

原所有已返 native trial、失败 stage/rawCell/rawSegment、当前 QR 结果和未开始的 FD/final phase 仍由原必要选择器返回。$R,z,s,b,A,Q,\Gamma$ 和大 root tape 均只在 Actions 临时现场。唯一 ASCII 必要摘要仍须不超过90000字节；超限为传输70，既不拆包也不更改科学接受标签。

原 wrapper 新 session/实际 PID-start-time-pgid-sid 收据、同组终止、实际 reap/quiet、原 rules parent 的独立静止责任不变。只有完整同 run/source 必要 marker、真正 quiet 与原 cleanup 条件同时成立，才删除对应 namespace；否则明确保留至 runner 销毁。

## 466.10 尚未支付的数值结论

这份源码与推导没有完成一次科学求值，没有证明原一般舍入缺陷导数为零，没有给出新投影/预组装/代回 roundoff 的严格界，没有证明任何分支邻域稳定，也没有证明新旧浮点方向相同或新运行更快。

可严格使用的结论是：在R465明确的准确实名义系统中，完整结构收缩等价于三组方向方程；本源码把该收缩接到原实际接受 trace 的全部方向，并明确新数值顺序、回退、资源部分范围和原终端门。后续公开 Actions 的真实结果仍须独立写明已执行到哪一层，不能从程序 exit 或绿色步骤补填未付的科学责任。
