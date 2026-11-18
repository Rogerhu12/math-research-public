# n4：原有限流的 native 扩展精度及一致隐式 Jacobian 方案

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 当前决定及已执行范围

下一候选只选 **native C++ `long double` 内核**，沿原 formed-moment 点根和原 RK，不继续组合补偿，不加入移根 A/B。它把全部原 binary64 系数精确提升到扩展格式，只提高 state-dependent 算术精度；以既有 MP90 的同一有限定义为参照。

本条只完成本地编译能力静态检查、既有源码/数据读取和下述数学/接口方案。没有实现或执行新的 native 流、Jacobian、全尾或 DN，没有新的接受结果。`scripts/resume_n4_tail/inspect_native_extended_precision.py` 的真实执行只调用编译器版本、宏预处理和 `-fsyntax-only`，没有生成或运行数学可执行文件；证据保存在 `native_extended_precision_capability.json`。

## 实际平台能力

本机为 x86_64，GCC/G++ 14.2.0。编译器报告 `LDBL_MANT_DIG=64`、`sizeof(long double)=16`、最大指数 16384；NumPy 独立报告 63 个显式尾数位、连同首位共 64 位，epsilon 为 `1.084202172485504434e-19`。这是带存储填充的 80 位扩展格式，**不是 binary128**。

`std::sqrt`、`std::log1p`、`std::expm1` 的 `long double` 重载声明，以及以下编译选项的静态语法检查均成功：

```text
-std=c++17 -O2 -fno-fast-math -ffp-contract=off
-fexcess-precision=standard -frounding-math
```

该检查不等于已经验证链接后的数学函数精度。正式最小 probe 还应记录运行时舍入模式、扩展格式有效精度、实际链接库及可执行文件哈希。禁止 FMA 合并、fast-math 或编译器代数重排，不把 11 个额外有效位自动解释为误差改善的定理。

已检查的常用 Node addon 头文件位置没有头文件，因此方案不依赖未安装的 N-API/JSON C++ 库。探针用同一内核的 C ABI；全尾用一个二进制 batch CLI，每次完整 `evaluate` 调用一次，避免每个 stage 启动子进程。

## 必须冻结的有限定义

原 `capsule-coefficients.json.gz` 已保存三个 stage 的 42 维初值、全部 grid 和每个 RK 采样点的原几何/系数。native 导入时先读原 double 位串，再精确提升为 `long double`；不从十进制短串重建，不重新算 trig/profile，也不把 double 常数改写成不同值的 `L` 后缀常数。

应保留独立冻结的 $E,w^2,r^3,r^4,\mathrm{TF},\mathrm{pref},\sigma,pNum,pDen,qLNum,\mathrm{meanFactor}$，全部 state trig、域 floor、点根容差、fallback 容差、scale floor 和减半因子。保留原 `moments - target` 停判、30 次迭代、20 次减半、原 Cholesky 迭代矩阵及原 RK 操作次序；实际分支可以因精度变化而不同，必须记录。

这点对 Jacobian 也有实质影响。只读旧 capsule 已确认：state 和 fast-Jac 的 cos 表有 628/2688 项 double 位串不同，sin 表有 623/2560 项不同，最大差约 $2.0097\times10^{-14}$、$2.0081\times10^{-14}$。三个 stage 各 48 个固定点的 $E-(1+w^2)$ 精确有理差全非零，最大绝对值约 $1.11\times10^{-16}$。原 fast-Jac 还用过 $\mathrm{pref}\,\mathrm{TF}=\sigma$ 的数学约简。因此，不能把那份快速 Jacobian 原样提升精度就称为冻结字面 RHS 的导数。

以上只指出定义不完全相同，不断言这些差异已经解释原 DN 失败，也不构成误差下界。

## 一致的隐式点根与流 Jacobian

以下所有字母系数均代表独立冻结的原常数。以 $c_i(n)$、$s_j(n)$ 表示 **state** trig，$c_0=1$，$a_j=pNum_j/pDen$，$m_j=4(j+1)$。每个角点定义

$$P=\sum_j a_jQ_j s_j,\quad P_t=\sum_jm_ja_jQ_jc_{j+1},\quad
L_v=L_0+\sum_jL_{j+1}c_{j+1},$$
$$K=L_v-P_t,\qquad
U=\sum_j[-m_jL_{j+1}+(m_j^2-1)a_jQ_j]s_j.$$

原 `evaluateL` 的字面局部修正记为 $q(L_v,P,P_t;E,w^2)$，按其已有 $T,u,D,S,\sqrt D,f_c,g_c$ 运算树定义，不合并 $E=1+w^2$。完整有限根方程为

$$F_i(L,Q,\pi)=L_i+\frac1{n_q}\sum_nq(L_v,P,P_t)c_i(n)-t_i(\pi)=0,$$

其中 $t_0=0$，$t_{j+1}=\mathrm{TF}\,\pi_j$。

在每角使用三个局部变量 $(L_v,P,P_t)$ 的解析微分或小型一阶 dual，得到字面 $q_L,q_P,q_T$。这样不用对 40 个状态方向分别重算点根，也不引入有限差分。相应矩阵为

$$B^{\rm exact}_{ik}=\delta_{ik}+\frac1{n_q}\sum_nq_Lc_i c_k,$$
$$C_{ij}=\frac1{n_q}\sum_n\left(q_Pa_js_j+q_Tm_ja_jc_{j+1}\right)c_i.$$

全部 40 列隐式导数由同一个分解求出：

$$dL=(B^{\rm exact})^{-1}\,[\,-C\ \mid\ \mathrm{TF}\,\mathcal E\,],$$

$\mathcal E$ 在非 mean 的 $j+1$ 行嵌入 $\pi_j$。**原 Newton 矩阵仍只作原求根算法的迭代矩阵**；$B^{\rm exact}$ 是本条另外推导的字面方程导数，不能把二者无条件当成同一个浮点矩阵。

接着对原 split RHS 的字面非线性通量求导。写

$$f(K,P)=\frac{K+u/(1+\sqrt D)+w^2P^2\sqrt D}{S\sqrt D},\quad
N_j=\frac1{n_q}\sum_nU f(K,P)s_j.$$

每列先由 $dL,dQ$ 得到 $dP,dP_t,dK,dU$，再计算

$$dN_j=\frac1{n_q}\sum_n\{dU\,f+U(f_KdK+f_PdP)\}s_j.$$

RHS 导数必须按原字面式保留系数乘积：

$$dQ'_j=\sigma\{(m_j^2-4)dQ_j+(qLNum/r^3)dL_{j+1}\},$$
$$d\pi'_j=4\sigma\,d\pi_j+\mathrm{pref}\,m_j
\{-m_jdL_{j+1}+(m_j^2-1)a_jdQ_j+dN_j\}.$$

两个 mean 的导数分别为 $\mathrm{meanFactor}\,dL_0$ 和 0。此处不替换 $\mathrm{pref}\,\mathrm{TF}$，不沿用另一套 fast-Jac trig。由此得到 $42\times40$ RHS 矩阵，按原同一 RK stages 推进 $T'=J_{\rm rhs}T$，初值为前 40 行单位矩阵及两行 0。

这个公式是在**原停止规则返回的近似根处评价根方程的隐式 Jacobian**，不是对有限 Newton 次数、分支或 roundoffFallback 算法求导。没有残差到真根的误差界时，不称其为返回算法的精确导数或连续 ODE 证书。m3 同行已只读核对这一区分和上述字面隐式微分路径。

## 最小 probe 与已有 MP trace 的利用

源审通过后，第一阶段先实现同一 native 核的 double 验证模式。它沿原 formed-moment 根/RK，double 标量数学函数通过已有 V8 bridge 回调，以排除 glibc 与 V8 的 `log1p/expm1` 实现差异。必须复现原 3×42 输出字节及已记录原 trace；任何不一致先停在移植定位，不能用误差容忍代替这一基线。

基线通过后才运行同三段的 `long double` 状态及全部 40 列 Jacobian。提高的只是 state-dependent 算术，使用 native 扩展数学函数，不保留 V8/Python 标量回调。保存 native 扩展值的精确编码和返回 binary64 值，分别对既有 MP90 比较全部 42 输出、两个 mean 和原物理归一误差，记录所有实际 root 次数/停止值。

40 列 Jacobian 的独立高精度参照可以利用**已保存的 MP90 RK trajectory**：每个 `rk_field` 后已有对应 `root_start` 的完整 state；成功 `root_stop` 对应之前的 `evaluate_start` 保存了被接受的 $L$。严格按事件及 profile/x 配对，核 64 个根身份后，只在这些已保存的 state/$L$ 上重新评价上述字面隐式导数，再推进变分 RK。这样不重复原 MP90 非线性流或点根求解；新评价的导数应明确标为新计算，不冒充旧观测。

全部 40 列及两 mean 行都应比较，按 $Q/Q,Q/\pi,\pi/Q,\pi/\pi$ 分块保留绝对/相对尺度，另记完整矩阵哈希。不能用原快 Jac 的非零差直接判 native 错，也不能仅凭与自己同源的一个输出通过就称导数已验证。若独立高精度变分参考尚未完成，记录必须保留这一缺口。

## 可连接真正全尾的协议

同一个已验证 C++ 标量内核提供两种外壳：三段 probe 的 C ABI，以及每次完整 `evaluate` 一次调用的二进制 batch CLI。二者必须编译自同一冻结源，不另维护一个数学实现。

binary 包含版本/维度/源与原系数包身份、原 grid、每个采样点的冻结 double 系数、全部输入 42 状态及 `withJac`。immutable 系数包在一个固定物理 DN 设置下只导出一次；每轮只写新的完整节点状态，不能在 native 内另构造新 profile、graph 或 cut 数据。CLI 遍历原全部 stage，返回全部 42 状态、可选 $42\times40$ tangent、域及根诊断。state-only 与 full-Jac 共用同一个状态算术路径，Jac 工作不能改变状态值。

对现有 Node 边界的转换必须显式：**在每段完成后只把最终 42 状态及 tangent 转回 binary64**，原 `cellFlow` 继续按原 double portRatio 换算，原 `evaluate` 继续用 double 做 `out - node`、除原 scales、左 target 和远端 Robin 条件。不能把高精度内部残差直接交作原 $2\times10^{-9}$ 门的验收，也不能用更高精度节点偷偷改变 checkpoint 编码。

全尾接入前先做同一完整既有状态上的 state-only/full-Jac 一致性及完整残差诊断，随后才考虑原 Newton/DN。原 sparse correction、线搜索、全部边界和最终审计门不改。最终 audit 的 RK32 采样也必须明确采用同一 native 状态推进及其对应原采样系数；现有 metric/jet 审计公式与门保持，不能把只接入 RK16 shooting 而仍混用另一状态推进的结果当成已经完成接口。

批处理接口还需保留真退出码、stderr、完整输入/输出哈希，所有失败状态另存，不覆盖原失败 CP；没有精度或资源终态时不推断 OOM/数学失败。

## 全 2304 段的成本计划

既有真实 observer 时间为：原全 Jac residual locator 150.172 秒；原 state-only/full-Jac 双路径核对 178.191 秒；一次原 DN 失败续跑 857.071 秒。这些含初始化/导出，不能当纯内核 benchmark。既有 MP90 三段 state-only 126.108 秒，若只作同成本线性外推，一次 2304 段约 26.9 小时且尚无 Jac，因此 Python MP 只适合作有限参照。

原 $42\times40$ tangent 的稠密乘法，每段 64 次 RHS 有 4,300,800 个乘加项，全 2304 段为 9,909,043,200 项；这是运算计数，不是 wall-time 预测。全 $42\times40$ binary64 输出约 31 MB，原 $40\times40$ 物理块约 29.5 MB；按现有每段 48 点、每点 32 个系数计，完整冻结系数约 28.3 MB，另加 grid/元数据。native 工作区可以按段复用，不应为每段复制一个完整引擎或为每个角点分配对象。

三段 probe 必须分别记录只算状态、带 40 列 tangent 的内核时间与编解码时间；与旧 150 秒整体量级比较后，给出带范围的 2304 段估算。不能预先声称扩展精度必然更快。若量级不可用，先定位确定的矩阵/投影成本，不能把三个 Python/长浮点漂亮输出当成全尾完成。

本条的下一实施对象仍只是冻结原三段的 native 源、完整字面 Jac 和协议验证；生产安装、完整新 DN 及闭合构造都需要后续真实结果。
