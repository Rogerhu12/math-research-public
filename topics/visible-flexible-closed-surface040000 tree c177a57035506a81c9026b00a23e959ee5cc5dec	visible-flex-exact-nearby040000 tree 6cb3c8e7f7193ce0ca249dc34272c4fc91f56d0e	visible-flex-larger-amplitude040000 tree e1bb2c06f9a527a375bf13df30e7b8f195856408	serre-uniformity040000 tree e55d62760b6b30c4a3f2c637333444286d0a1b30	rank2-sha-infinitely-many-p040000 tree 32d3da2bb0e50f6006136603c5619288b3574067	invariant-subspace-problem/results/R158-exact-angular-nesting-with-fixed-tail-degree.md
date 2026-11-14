# R158 — 保留完整尾函数的准确角阶嵌套

**状态：已证明，并已实际消费保存实体。** 本文把 raw/中央阶数从 $k$ 增到 $k'>k$，尾 Bernstein 控制数单独保持不变。注入前后是同一完整 II 函数、同一物理度量、同一角 atlas 及同一中央初始曲线。它不是一次新的 BVP 解，也不宣称新有限残差数值与旧有限残差相同。

## 1. 把三个维数明确分开

固定径向节点 $s_0<\cdots<s_{N-1}$。每个节点的 raw correction 顺序为
$$
y_i=(n_0,n_2,\ldots,n_{2k};\ m_2,\ldots,m_{2k};\ l_0,l_2,\ldots,l_{2k}),
$$
所以每节点有 $q_k=3k+2$ 个系数。各系数在相同物理 $s$ 节点间作准确 P1 插值；偶场使用 $\cos(2j\xi)$，奇场使用 $\sin(2j\xi)$。

另外记中央曲率控制为 $c\in\mathbb R^k$，尾控制为 $p\in\mathbb R^t$，物理 bump 参数为 $\delta\in\mathbb R^J$。尾的 Bernstein 次数是 $t-1$，不必等于 $k$。本次 $t=16,J=7$。

保持以下对象全部不变：

- 原 candidate、基准物理 coast 参数、准确 bump 支撑及 $\delta$；
- 全部径向节点及 P1 定义；
- 固定材料角 atlas $u=U(s,\xi)$，包括 frozen ruling 参考及其完整数据；
- seed、平尾和 coast 的完整函数 lifting 与全部径向窗；
- R153 正 $n$ coast 代换及 R155 末端正 trace 代换，包括准确 cut 的尾迹分支。

这里“完整函数”不指某个有限角表的重新拟合。旧 source 中 $k$ 同时控制尾度数只是实现耦合，并非几何方程要求。若照旧一并改变 Bernstein 度数后把新控制舍入，尾函数一般会改变；那不是本文的准确嵌套。

## 2. 准确注入及原始场恒等

定义线性注入 $I_{k,k'}$：

1. 三个 raw Fourier 块的全部旧系数放到相同物理波数的位置，新增系数全置零；
2. 中央向量变为 $c'=(c_1,\ldots,c_k,0,\ldots,0)\in\mathbb R^{k'}$；
3. 尾控制 $p$ 和物理参数 $\delta$ 原样复制。

因为新增基函数的系数准确为零，每个节点、每个角上的三个 raw 函数相等。P1 插值是对各系数作同一个线性组合，因此该恒等式在完整径向区间成立，不局限于节点。对角任意次微分、在每个开 P1 格内对径向微分，也保留相同的函数；节点处两侧 trace 与单侧导数各自一致。

中央族为
$$n_c(\xi)=n_{\rm seed}(\xi)+\sum_{j=1}^k c_j\bigl(\cos(2j\xi)-\mu_j\bigr).$$
新增零项不改变它。材料角映射、准确加权均值、初始平移/转角约定不变，因此相同曲率函数的切向积分和位置积分给同一中央曲线、标架和各已定义 jet。保存的加权均值证书涵盖 $j=1,\ldots,95$；本次 $k'=31$ 在其范围内。零填充本身也不依赖新项的均值精度，因为新项系数就是零。

尾控制数 $t$、每个控制值及正 Bernstein 基均不变，所以尾的角度原函数、曲率、位置积分、所有角/参数 jet 都是同一个数学对象。物理 $\delta$、candidate 与 bump 支撑不变，所以 $a_\delta,c,K$ 也是同一函数。atlas 不变，故完整 lifting 的每一项不变。于是 lifting 后、非线性代换前的三场恒等。

## 3. 非线性表示也准确保留

R153 在其固定窗内作
$$l\longmapsto(1-w_c)l+w_c\frac{K+m^2}{n}.$$
输入 $n,m,l,K,w_c$ 全部相同，且正 $n$ 的定义域条件也完全相同，因此输出逐点相同。本文没有把这个未付的连续正值域自动称为已付；只证明旧新表示具有同一个域，不能借零填充修复旧场的定义域失败。

R155 令
$$h=\sqrt{(n-l)^2+4m^2+4K},\qquad E=w_t(h-n-l)/2$$
并同时加到 $n,l$。这些输入及窗同样全部不变，所以输出逐点相同。准确 cut 直接取同一完整平尾值和允许参数 jet，也不需要在 $h=0$ 执行一般平方根微分。

因此整个实际三场
$$S_{k'}(I_{k,k'}z;s,u)=S_k(z;s,u)$$
在其完整共同定义域上恒等。所有实际点态 Gauss/Codazzi 缺陷及形式曲率也作为函数相同。若按 R119/R129 从该实际场和中央初始数据重建固定材料角的位置/标架，两边满足同一个线性标架 ODE 和位置 ODE、具有同一个初值，由唯一性得到同一个重建映射；这没有把原未收敛字段升级为满足目标度量的曲面。

在普通可微内部点，对旧允许参数方向求导还得到
$$D S_{k'}(I_{k,k'}z)\,I_{k,k'}=D S_k(z).$$
在准确 cut 的全零迹处，这个等式指沿准确尾族的直接参数变化，而不是在平方根原点臆造任意方向导数。这样原 JVP 的列有准确嵌入；新列提供新的角向自由度。

## 4. 精确 gauge 与边界保留

R153 只有完整 P1 hat 支撑落在 $w_c=1$ 平台时，其相应 raw $l$ 列才完全无效。这个判定只依赖真实径向节点和窗口，角阶改变不改变节点集合。

R155 平台上输出只依赖 $d=n-l,m$。完整 hat 位于该平台时，raw $(n,l)$ 的共同增量是准确零方向；取 raw $n=d/2,l=-d/2$ 是一个代表。旧系数的这个关系原样保留，新增零系数也满足它。消元后导数列为 $J_n-J_l$，与现有有界 Schur 实现一致。平台邻边的 hat 若越入 rim，仍不能删除。

本文的注入不重新调用边界投影或 gauge 规范化来改写旧数值；直接复制旧系数。若旧实体满足准确中央柱和 cut correction 条件，新实体也满足。若旧实体原来有某种不相容，准确注入同样保留它，不能静默“修正”后仍声称同场。

## 5. 同一完整函数与新有限离散必须分开

完整残差函数相同，并不意味着两个有限残差向量相同。新角空间保留更多 Fourier 行；其正交补也随之改变。默认角求值格从 256 变为 512 时，同一低模积分的有限求积值也可能变化。径向已知 lifting 求积若重新评价，同样必须报告实际新数值，不能以恒等函数为由复制旧残差。

正确关系是：新旧读者先定义同一完整函数，再分别施加各自明示的有限投影、求积和行选择。新空间中的零填充点是合法初值，后续真正改变新增系数才可能改善方程；本文没有据角阶提高就宣称残差降低或解已存在。

物理方程行数由 Codazzi、保留的 Gauss 行和原边界/幅度条件决定，不应为了参数数看起来匹配而增补或删去条件。基础 raw 方程在未删恒等行时仍为 $Nq_k+2k+2$，而参数维数是 $k+t+J$。R153/R155 只按其准确恒等式删除相应平台 Gauss 行。这样的有限系统可以是矩形；独立尾维数不会创造新的几何边界条件。

## 6. 独立实现及明确布局

新源 `scripts/fd2d_gc_nested_angular_positive_trace.py` 提供：

- `zero_extend_angular_arrays`：纯数组准确注入，检查所有旧 raw/central/tail/profile 系数的字节都未改变；没有投影、径向插值或 Bernstein 升阶。
- `FixedTailDegreePositiveTraceDAE(..., modes=kprime, tail_parameter_count=t)`：继承现有实际函数和方程，仅把中央/raw 与尾控制数分开；不修改活动旧源。
- `inject_saved_field(saved_arrays)`：逐项绑定相同 candidate、mesh、支撑、固定物理参数及全部完整函数定义包，然后注入。
- `checkpoint_arrays`：保存明确的 `central_parameter_count`、`tail_parameter_count`、`nested_angular_definition` 和 `angular_embedding_definition`。

新 schema 为 `fd2d-independent-tail-angular-nesting-v1`，表示标识为
`ruling_atlas_coast_Gauss_l_terminal_positive_trace_fixed_tail_degree_v1`。
本次参数切片准确为
$$c=[0,31),\qquad p=[31,47),\qquad\delta=[47,54).$$
旧 native reader 把尾长度写死为 $k+1$，不得用于解码本实体。新 reader 应按三个显式切片消费；不能把最后一个物理 $\delta$ 误认成 coast $T$，也不能把 16 个尾控制重新升阶。这是准确身份要求，不是新的求解或批准门。

## 7. 本次真实实体和小局部消费

实际输入是已完成初始化检查的
`notes/2026-11-12-fd2d-positive-trace-warm04-warm.npz`，
SHA256 `a0ebb07b210d373b5a9aced7b79137f28fc5f7ffa6a797ea960113f9ee3980ac`。
它仍是旧 $d,m$ 的未收敛正 trace 初猜；本文没有把它替换为 R157 后来的新初猜。
其绑定 provider `fd2d_gc_raw_bump_positive_trace.py` 的 SHA256 为
`582e85efb95f3f735b6fd19e47a94182462368c1f16aeb75399fa81729cc6e61`，未修改。

本次 $N=123$，实际尺寸为：

| 对象 | 原空间 | 新空间 |
| --- | ---: | ---: |
| raw/central 阶数 | 15 | 31 |
| 最大物理 Fourier 波数 | 30 | 62 |
| 每节点 raw 列数 | 47 | 95 |
| 尾控制数及 Bernstein 次数 | 16 / 15 | 16 / 15 |
| 物理 bump 数 | 7 | 7 |
| 总参数数 | 38 | 54 |
| 总未知数 | 5819 | 11739 |
| 原保留方程数，不含额外 merit 行 | 5637 | 11397 |

检查源 `scripts/fd2d-nested-angular-positive-trace-check.py` 只实例化两个读者，在 11 个真实物理位置（包括 coast、末窗内部和准确 cut）及同一组 128 个角上评价完整函数。没有装配 Jacobian、解 BVP、积分 body 或重新拟合任何场。实际执行 session **30902**，初始 chunk **3ddcb5**，完成 chunk **8a7711**，自然 exit **0**，耗时 **4.905615567 s**，RSS 峰 **96732 KiB**。

该共同格上的 raw 值/角 jet、完整 lifting 值/角 jet、最终 R153/R155 字段值/角 jet、$a,a_s,K,U,U_s,U_\xi$、中央 $n,n_\xi$，旧新最大显示差均为 **0**。这是实际实现的有限读数；完整同函数结论由第 2–3 节的代数证明给出，并非由这组有限点推出。

新实体为
`notes/2026-11-12-fd2d-nested-angular-k31-tail16-01-field.npz`，61242 B，SHA256
`19cffa6028804219373ed20be8e29d3d11938b3ebdae16ed8caee2aeb79554c9`。
对应报告 `notes/2026-11-12-fd2d-nested-angular-k31-tail16-01-report.json`，SHA256
`9e3acd3494c732e2010dbe4175deea29bbfe28b8c1ee4caedd0af85be5ee2ae0`。
新 provider SHA256 为
`f61c95a57a88d2fee99c6e57241110f8c3ee453ded1060e02ba31f77912f868c`。

输入读取前后 SHA 相同。本组只提供准确嵌套及可继续求解的高阶初值；新的完整有限残差、真实 nonlinear 进展、连续后验和强目标仍须继续实际支付。
