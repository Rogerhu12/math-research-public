# R917 执行契约：原两端完整八维正规阶与参数行列式帧

日期：2026-11-16。状态：本文件冻结一个可公开执行、可逐阶段续接的消费者。来源均为已完成的原生产者；本次的新两端正规阶、实际判别式、行列式首项必须等实际 Actions 输出，不预填成功。

数学依据是 [R917 原两端正规阶证明](../results/R917-original-two-endpoint-normal-orders-and-source-contract.md) 与 [R912 完整八维端点格](../results/R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md)。完整几何对合与 273 项原局部展开采用 [R914 实际结果](../results/R914-certified-original-full-V1-involution-and-P1-jets.md)。原对应、同素点十七系数和 $t$ 帧分别采用原 R873、R882、R883；原 $\nu$ 来源采用 R860。本文件不改变上述定义或原 $-3$ 下降。

## 1. 本次的实际范围

固定辅助素数 $\ell=1000000753$、原 $\zeta$ 根 $549966761$、原 $s$ 根 $99932770$。两端分别使用

$$
\rho_0=z-z_0,\qquad \rho_1=\iota^*\rho_0=z-2\beta_{72}-z_0.
$$

R914 已经完整认证原 $146\times146$ 几何 $\iota$ 作用、全部 560 行乘回以及 $P_1$ 的原 273 项展开。这里只读其原字节，不求新的 143 个右端，不重新计算 R872 的 Hensel 递推，也不把算术共轭当几何对合。

首 scope 输出两端各自的完整八维整数阶、实际判别式阶 4、含幂零的完整特纤维及相对于 $1,U,\ldots,U^7$ 的行列式帧。由原对应已有几何分支长度 $1+1+3+3$，正规阶判别式阶为 4；本消费者必须从真实有限精度乘法表得到这个判据，不能只引用已知长度而跳过计算。

本次不计算原目标 $272$ 个正规坐标的端点 Laurent 值，不计算五个目标理想的端点格，不计算 $\operatorname{Nm}(\Phi)\det U$ 或九范数的端点标定。相应字段始终为 `false`，未来 `R903`、`R907` 来源始终为 `null`。这些边界不阻塞本次独立的两端几何正规阶。

## 2. 原来源的最小闭包

新的数学输入载体共有 **40 个原文件**，分为五组。每组保原 `result/run_id/source_commit/core_sha256/manifest_sha256`、原完整配置指纹、实际证书及选中原文件的长度与 SHA。新载体不改原生产者标签。

| 组 | 原文件数 | 实际消费 |
|---|---:|---|
| R873 | 7 | 原对应 DAG、准确十七系数 unit-solve 表达式、证书和三元数据及 manifest |
| R882 | 8 | 同素点 $2058\times17$ 坐标、同素点接口、原审计、证书/元数据/manifest |
| R807 | 7 | 原 $\theta$ 和 $N_{692}$ 准确坐标、证书/元数据/manifest |
| R883 | 7 | 已成 $\theta,N_{692}$ 前三项、旧分母逆、$t/\rho_0$ 帧及证书/元数据/manifest |
| R914 | 11 | 完整对合矩阵与乘回、$P_0/P_1$ 的 $273\times146$ 叶矩阵、$P_1$ 点核对及原 $t_1$ 帧、证书/元数据/manifest |

R873 的 2050 个原 V8 单项式、八个补列的原 V2 配方和原 $N_{692}$ 的 V4 配方都在其准确 DAG 中，故不再搬原长 Fourier 前缀或重求 2058 阶逆。原 $e_i=82^2T_{1,i}$ 的整数尺度已经含在这些来源中；本次不再乘 $82^2$。

R807 的七个文件从仍有真实平台身份的 R883 一日载体中读取。具体运输包为 `R807-t-frame-intake-selected-original-sources.tar.gz`，原长度 1796873、SHA `9651935f5ec01ff23c66db88f81b2f8aab464a2ef74d416457c1e571905600fb`。包装器逐个核验其中全部 11 个原成员，再仅保留本次所需七个；R883 的原 inventory/receipt 显式绑定这份 tar 与原 R807 身份。不会请求过期原 R807 artifact，也不改运输来源为新的数学生产者。

四个直接原 artifact 只按完整 manifest 及平台 ZIP 元数据核实后 Range 读取选件。该读法只声称已读取成员的逐字节 SHA，不声称没有下载的整 ZIP 已重新哈希。新 flat tar 的布局为 `R873/<name>` 等五组；所有 live 数学输入在该 tar 中闭合，原运输路线仅作为历史回执保存。

## 3. 实现、配置和数学身份

算术入口：

```text
R917_original_two_endpoint_normal_orders.py
  --config expanded-job.json --out output --budget-minutes 300
```

小型算术模块为 `R917_endpoint_order_arithmetic.py`。两文件的真实 SHA、`python-flint==0.9.0`、七份 proof SHA、执行方法 SHA、五组来源指纹、14 个具名输入 plain specs 及固定策略全部进入数学配置。

独立 `RESULT` 为 `R917-original-two-endpoint-normal-orders`，FINAL 为 `p41-original-two-endpoint-normal-orders-certificate.json`。全部数学阶段名以 `R917-endpoint-` 开头，并使用 `.json.gz`。核心在入口要求 `GITHUB_ACTIONS=true` 及原公开仓库身份；导入自己的已绑定 helper，不导入旧数学核心、不改其他模块全局变量。

运行时间预算、可继续增大的 idealizer 步数上限、绝对目录、运输路线和规则读取 commit 不进入数学身份。选中原文件指纹采用按键排序的 **文件名到 plain-spec 字典**，不是历史某些包装器的列表编码。包装器、核心和续接都使用同一字典定义。

## 4. 十七条正则函数及原精度

令 $\theta_0=\theta/\tau$、$A=N_{692}/\tau^4$。对原十七条函数中的每一条，沿已有 V8 部分和八补列写成

$$
c=V_{8,c}+(A/\theta_0)^2V_{2,c}.
$$

计算的真正正则函数是

$$
\widetilde c=\theta_0^2V_{8,c}+A^2V_{2,c},\qquad
\widetilde P=\theta_0^2P,\quad\widetilde K=\theta_0^2K.
$$

这十七条函数均为原权 10 截面在 $\tau$ 图上的函数。$\theta_0$ 的端点零不被伪作单位；实现没有求 $\theta_0^{-1}$。原目标分式仍严格为 $K/P_U=\widetilde K/\widetilde P_U$。

从 R873 原配方取真正需要的叶单项式，按原叶下标排序去重，每 64 项保存一个完整 273 项 block。重复配方只读同一 block。V8 的十七个线性组合也按 64 列分块原子保存，最后与八个补列的完整乘积相加。$P_0$ 的 $\theta_0,A$ 前三项直接复制 R883，新的线性组合只计算阶 3 至 272；$P_1$ 计算阶 0 至 272。旧有理分母的单位逆同样从 R883 已成记录读取。

准确特征零定义依然是原 R873 的 unit-solve 与原 R807 准确坐标。此次计算给该定义在指定同素点上的截断函数值，不把辅助模数组改称展开的特征零坐标。

## 5. 原首一阶和 273 项输入的真实损失

在每端实际读取 $a=v_\rho(\widetilde P_8)$，再选择使

$$
v_\rho(\widetilde P_i)+h(8-i)\ge a\quad(0\le i<8)
$$

成立的最小非负整数 $h$，令 $\Theta=\rho^hU$。所有可能出现的负阶系数必须逐项确认为零。单位除法使用已移去 $\rho^a$ 的真正首项；所有八个商都完整乘回。

输入有 $N=273$ 项时，统一可靠精度是 $N-a$。若 $\widetilde P_8$ 在已知区间没有非零项，或损失后不足以判断阶 4，返回实际 `NeedPrecision`，记录端点、已有精度与所需界；不把零截断当准确零。

原始阶 $\mathcal O_0=\mathbb F_\ell[[\rho]][\Theta]$ 保完整 $8^3$ 个结构常数和单位坐标。对全部八个基向量核验左右单位，并核完整原首一关系。

## 6. 小 idealizer 核、精度与停止

每步从当前完整表得到真实八维 trace Gram。判别式使用除法自由 Berkowitz，不在截断系数环中执行非法非单位 Gaussian 除法。

令 $N_0$ 为模 $\rho$ trace radical，选完整常数基 $C$ 后

$$
J=C\operatorname{diag}(I_r,\rho I_{8-r}).
$$

对 $v$ 的乘法矩阵，`vJ⊂ρJ` 必须同时包含以下四块：$N/N$ 的常数项、补空间/补空间的常数项、补空间/$N$ 的常数和一次项都为零，$N$/补空间无额外条件。只这些原表 0、1 次系数产生一个真正的小有限域核，不拆分重数或分支。

若核维 $k>0$，新的常数完整基前 $k$ 列除以 $\rho$。乘法表的最坏位移为 $-2$；每一项可能的负阶都必须实测为零，随后统一精度减 2。完整 Laurent 多项式基变换及双向逆保持为有限原数组，并核全部乘回，不仅记录 determinant 的幂。

设累计 index 长为 $I$、常数 determinant 单位为 $u$。每步验证

$$
d=d_{\mathrm{initial}}-2I,\qquad
\operatorname{lc}(\operatorname{disc})=
\operatorname{lc}(\operatorname{disc}_{\mathrm{initial}})u^2.
$$

只有真实完整表的判别式阶达到 4 才停止。特纤维仍是完整八维代数，另保 trace radical 维 4、平方维 2及立方全部为零的实际验证。原 $1+1+3+3$ 几何长度由原对应来源保证；这里不以其约化商替代八维表。

若有预算、步数或系数精度阻断，保留已成阶段并诚实退出。步数上限不是数学成功旗标。

## 7. 原参数及 determinant 帧

累计基相对于原 $U$ 幂基的行列式为

$$
u\,\rho^{28h-I}.
$$

原 $t_0=t$、$t_1=t-1$，$t_\epsilon=c_\epsilon\rho_\epsilon+\cdots$。R883/R914 的真实 $c_0,c_1$ 均原样读取，$c_1=-c_0$；于是 $t$ 首项是

$$
u\,c_\epsilon^{-(28h-I)}.
$$

保存原 $U$ 在最终正规基中的八个 Laurent 坐标、完整基及逆、原 $K/\partial_UP$ 分式定义和原 dual7 输运。dual7 的分子、分母两个 determinant 因子都保留。原微分仍为 $\nu=82\tau\,dq_Y/q_Y$ 且 $\iota^*\nu=\nu$；这条准确来源不产生本次尚未求出的 $\nu/d\rho_\epsilon$ 数值。

注意此处普通字母 $u$ 是基变换 determinant 单位，和固定微分 $\nu$ 不同。本次帧只是正规阶与原 primitive/t 参数的帧，绝非五目标线丛或九范数截面的完整帧。

## 8. 原子恢复及真实终点

每个数学阶段以同目录 `.tmp` 写完、flush/fsync 后原子改名；只完整阶段有 `complete=true`。`current` 明确为 `complete=false`，实际阶段 inventory 只枚举本次原目录中全部完整阶段，排除自己和 current。

恢复只接受同一数学配置、同一 core/helper/proof/input SHA。读取先前真实平台 manifest 后逐 SHA 恢复全部同前缀完整阶段与 current。旧不完整 FINAL 仅是历史搜索/精度回执，不复制成新终点，也不拿它对旧 current 的 SHA 约束后来已推进的 current。真实成功 FINAL 才检查全部引用闭包。

每端先保存完整系数、primitive 阶、每步判别式、小核、完整新表，再保存最终特纤维、原帧和端点证书。即使第二端精度不足，第一端真证书也保留。核心只在两端都真实认证后返回退出码 0。`NeedPrecision`/预算退出码 2，其他实际错误退出码 1；包装器外层硬超时明确为 124，允许真实缺 core receipt，不伪造缺失证书。

## 9. 公开执行及 IO 审读

stdlib 包装器仅运输、哈希、读 schema、调用独立核心及保存回执。Range 使用冻结 R824 工具，选源打包使用冻结 R837 工具；不导入任何数学核心。源码 AST/SHA 检查与算术同一次公开 Actions 运行，安装固定 `python-flint==0.9.0`。每次运行先真实 pull/rebase main 并比较两份 README SHA，改变时停止且展示规则差异。

成功 IO 审读逐个读两端证书、完整表形状、实际判别式字段、完整特纤维、primitive/t 帧及所有 live 引用，只核已输出证据而不再次做算术。日志打印实际两端初始 $h$、扩大次数、剩余精度、判别式阶与原帧首项；没有实际输出之前不填值。

一日 artifact 保本次原选源载体、所有完整数学阶段、当前断点、源码身份及真实退出回执。新原始数学数据不写 Git。新的真实 source/configuration 只能由本次完成的公开运行产生。
