# 原有限 shooting 的 literal JVP 与背景分块预条件：完整方向方程

本条把结构性省时入口写成具体原方程的方向导数，不把未实现的算法或未返回的 J 当结果。当前生产 M24/.5 原 solve 继续，未改 source、二进制、root/Frenet/domain、完整残差或 audit。后续 JVP/GMRES 即使实现，也先仅生产明确未接受的完整初猜；真正终态仍交原 worker 的 fresh full stage J、原 full height J 与 audit。

## 1. 每一个原角节点的完整方向方程

记有限 Fourier 模数为 M，J=M+1，K=2M。原 native `frozen_flow_production.cpp` 的 `root` 返回近似根 L=(L_0,...,L_M)，并保留每个原角节点的 row。把 `q_partials` 的三个原 partials 记为 q_L,q_P,q_Pt，把 `flux_partials` 记为 f_K,f_P。这里都是现有 literal implicit derivative：不对 Newton 停止规则求导。

对任意完整方向 (δQ,δΠ)，令 a_j=g.pnum[j]/g.pden，m_j=spacing·(j+1)，原 literal basis 为 c_i(n)、s_j(n)，其中 c_0=1。则

\[
\delta P_n=\sum_j a_j\delta Q_j s_j(n),\qquad
\delta P_{t,n}=\sum_j m_j a_j\delta Q_j c_{j+1}(n).
\]

原 literal 矩阵与方向右端是

\[
B_{ik}=\delta_{ik}+\frac1{n_q}\sum_n q_L(n)c_i(n)c_k(n),
\]
\[
b_i=\mathbf1_{i\ge1}g.target\,\delta\Pi_{i-1}
-\frac1{n_q}\sum_n[ q_P(n)\delta P_n+q_{Pt}(n)\delta P_{t,n}]c_i(n).
\]

调用原 checked Cholesky/triangular solve 得 **全部 J 个 δL**；不能漏掉零模 δL_0，也不能复用原 Newton 的不同 B 来冒充 literal B。接着

\[
\delta L_n=\delta L_0+\sum_j\delta L_{j+1}c_{j+1}(n),\quad
\delta K_n=\delta L_n-\delta P_{t,n},
\]
\[
\delta U_n=\sum_j[-m_j\delta L_{j+1}+(m_j^2-1)a_j\delta Q_j]s_j(n),
\]
\[
\delta N_j=\frac1{n_q}\sum_n\{\delta U_n f_n+
 U_n[f_K(n)\delta K_n+f_P(n)\delta P_n]\}s_j(n).
\]

完整的 K+2 个方向 RHS 是

\[
\delta Q'_j=g.\sigma[(m_j^2-4)\delta Q_j+g.qlnum\,\delta L_{j+1}/g.r3],
\]
\[
\delta\Pi'_j=4g.\sigma\,\delta\Pi_j+
 g.pref\,m_j[-m_j\delta L_{j+1}+(m_j^2-1)a_j\delta Q_j+\delta N_j],
\]
\[
\delta\mathrm{mean}'=g.mean\,\delta L_0,\qquad
\delta\mathrm{backgroundMean}'=0.
\]

这些式子就是现 `literal_jacobian` 各列乘完整方向后按线性性收集；没有 Fourier 截断、入口投影、频率冻结、弯曲数据替换或有限差分。实现时允许方向集合有 b 列，保每列全部 K+2 个分量。它是每点的原 literal JVP；在完全相同 RK4 中推进即可得到整段方向输出。

## 2. 哪部分能省，哪部分仍然昂贵

当前 full-J 路径每个 RK 点既构造 literal B，又解 K 个右端、构造全列 dN，然后计算 K×K 变分乘积 J·T。一个方向把后两者换成 O(n_q M)+O(M²)，并避免 J·T 的 O(M³)；但**原 root 及 B 的 O(n_q M²) 构造仍在**。若每个 GMRES matvec 都从头重跑 state/root/B，多次 matvec 足以吃掉节约，不能声称得到 M 倍提速。

有效路径需在固定 Newton 状态上缓存同一 RK4 的 state/root 轨迹及 literal B 的 Cholesky。新 trial 或状态改变后整套缓存失效，所有原 root/Frenet/domain 门重付。保持原 long-double 轨迹身份需存 canonical 80-bit 有效字节，不能悄悄把中间 state 降成 binary64 后称同一 literal RK derivative。

当前实测整批有 1152 段、18,460 RK steps、73,840 个 RHS/root 调用。若 M=80，J=81，每点存三角 Cholesky 的 native 16 字节 long-double，单这一项约 3,923,562,240 字节；state/root 另约 0.29 GB。不要再缓存每点的所有角数组，否则 N=2048 时又会超过十 GB。方向应用时可由缓存的完整 state/L 重新计算角量，O(n_q M)，并复用 Cholesky；或把逐段 factor 缓存放仓外文件、按完整段顺序流式读。缓存自己的 hash 必须绑定全部状态、完整原 frozen coefficients、原网格和源身份。

现生产 M24/N512 首 J 的真实 process wall 为 **527.832000633 s**，从 request 到迭代 trace 为 **529.224 s**；它替代此前仅按低 M 外推的 20–35 分钟估计。一次实测并不等于高 M 性能保证。

## 3. 原背景 2×2 分块预条件可直接构造

原零背景 Q=Π=L=0 时，q 的一阶导和 nonlinear flux 导为零。每个 Fourier 模独立；用同一 frozen g 和同一 RK/cusp 网格积分 2×2 线性系统

\[
A_{11}=\sigma(m^2-4),\quad A_{12}=\sigma\,qlnum\,target/r^3,
\]
\[
A_{21}=pref\,m(m^2-1)\,pnum/pden,\quad
A_{22}=4\sigma-pref\,m^2\,target.
\]

积分得到每段每模的完整 2×2 background transfer，仍应用原输出 Π 行的 portRatio。保原 first-mode node scales s_n，令 r_n=s_{n+1}/s_n。实际全节点矩阵乘积是

\[
(Av)_n=v_n-r_nD\Phi_n v_{n+1},\quad n=0,...,S-1,
\]

加上**全部 M 条左端 δH 行与全部 M 条深端 Robin 行**。预条件器只把 DΦ_n 换成上述背景 block；它不替换原 residual/JVP。按 Fourier 模和端点边界行重排后，每模是大小 2(S+1) 的窄带 BVP，可用带 pivot 的带状 LU。不要把 1152 段相乘成长传递矩阵，这会重新引入强不稳定方向的溢出/病态。

这给出具体右预条件 GMRES/FGMRES 路线；此段写作时迭代数尚未实测，随后完整矩阵探针已得到零背景停滞、±4 实际模带预条件 14 步收敛，见同日 `tail-gmres-preconditioner-actual` 记录。真实 native JVP 速度收益仍未实测。原 sparse helper 使用 normwise backward error<1e-11。matrix-free 时不能用未知 ||A||∞ 的随意大上界放大分母使门失真；可用 ||A||∞≥1 得到更严格的充分检验 `||b−Az||∞/(||z||∞+||b||∞)<1e-11`，或最终用原完整 J 验证同一线性系统。JVP 模型与 binary64 保存 J 乘法的舍入差也需单列，不能声称未比较的字节相同。

## 4. 实现入口与接受边界

原 ABI1、`vf_run_stage` 及 full-J CLI 保留。新独立接口可为 `vf_run_stage_directions(config,stage,b,directions,...)`：完整原 state、K×b 个初始方向、(K+2)×b 个方向输出，源/状态 token 和原 finite/root/literal-pivot 诊断。持久进程提供“固定原状态建轨迹”和“对该 token 应用方向”两步，避免每次 GMRES 重新启动所有 native 段。

当前 native 和 `parallel_native_batch.py` 硬限定 M≤64；M80 及以上需明确扩维审查，不能在默认 ABI 下传入被拒的维数或截到 64 后称 full-M。内部状态大多是动态 vector，但协议/reader/controller 的一致边界仍要整体更新。

终态 `heightJetJacobian` 当前依赖完整 shooting tangent 和原 cut-jet 差分。JVP/GMRES 生产了好初猜，也不等于它已返回。当前最小合规实施是：新算法只返回**完整未接受 checkpoint**，最终由原 worker 原 fresh full stage J、全部 height-J 列、full H、原 audit 真正验收。相应成本必须实际支付，不能藏在“矩阵自由”名称后面。

本条首次写作时未执行新的 JVP kernel、GMRES 或 M80 尾。后续已执行的完整矩阵 GMRES 探针详见同日 `tail-gmres-preconditioner-actual`，仍未实现 native JVP 或求 M80 尾。全节点切向预测见同日 `tail-full-state-tangent-predictor` 记录；原 M24/.5 已真实接受，其 E 后继正在求完整 H。本条及后续线性探针均不构成 full-H/闭图接受。
