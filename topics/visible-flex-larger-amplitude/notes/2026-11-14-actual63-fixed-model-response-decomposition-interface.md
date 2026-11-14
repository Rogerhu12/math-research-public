# actual63 固定完整模型：未约束中心与局部条件恢复的响应分解

分类：**计算接口；源码已完成，仅静态检查，尚无本入口的科学回执。**

作者：ChatGPT，exact_refinement。日期：2026-11-14。

本入口承接
[actual63 已保存 row155819 读数](2026-11-14-actual63-stored-row155819-response.md)。
该原件读数已经确认：区间461、radial1、完整加权残差行155819
的微小预测修正，在原条件恢复时已经存在。它未提供完整未约束中心，
不能据此唯一归因于阻尼或角域约束。本入口补齐这一项并分别保留其余贡献。

## 1. 冻结源码与范围

文件：computations/exact_20261114_actual63_model_response_decomposition.py。
字节：57,165。SHA256：

    10aeaa14b20651d87cecca67db6acb6bb3fd78663aa6dfe07897aa9c04ca1e6a

顶层 schema：actual63-fixed-complete-model-response-decomposition-v1。

本地仅作 AST 和既存 JSON 的字段、父 producer 子树检查；
未 import 数值生产者，未算矩阵作用、范数、QR、RHS 或有理误差。

fetch 只取已钉原件；analyze 只在 GITHUB_ACTIONS=true 且
GITHUB_REPOSITORY=Rogerhu12/math-research-public 时科学执行。
没有新的 LSMR、QP、非线性试步、native 请求、FD、约束或验收门。
唯一使用的步长是原63实际接受的 alpha=0.0078125。

## 2. 唯一实际原件和外部小输入

| 项目 | 实际身份 |
|---|---|
| run | 43646179305 |
| source commit | db6d728f30ee2d0c9ea62c96c622d8d85d2354b2 |
| artifact ID | 14134662698 |
| artifact name | visible-followup-condensedqp-43646179305-1 |
| 完整 ZIP 字节 | 494657224 |
| 完整 ZIP SHA256 | c90869cdcc317eef9b23a8a17755a7679ea5ce6dc41c2c143216524b481c6653 |

直接使用原已运行 transport：

- exact_20261114_fetch_pinned_public_artifact.py；
- SHA256：51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859；
- 原 schema：pinned-public-actions-artifact-fetch-v3。

只在内存换固定 PIN、当前 schema，并在原 metadata 核验中补查
workflow_run.head_sha。HTTPS、跨主机去 Authorization、
流式 ZIP 大小/SHA、完整 CRC、路径/符号链接/重名拒绝、
不覆盖既有目录等内核代码一字不改。只在 fetch 步设置
GITHUB_TOKEN；不在 analyze 步传令牌。

外部科学输入只有：

| 输入 | 公开仓库相对路径 | SHA256 |
|---|---|---|
| accepted96 | topics/visible-flex-larger-amplitude/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| 完整真实 T112 zero/J | topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |

以下全部直接取该 ZIP 内原件：

- preparation112/prepared.json.gz，原699节点；
- T112-config.json；
- parent62/warm-001.json.gz，SHA
  dffaa532026e07357d5115089d968c1be4472c44d9a5f5da25ebcb3e2291ac73；
- parent62/driver-status.json，SHA
  4f8239522cef511aca6721ddc9c4541cc9d4e65db3e7260d277b090ad226c054；
- eighteen-condensed-warm/ 的原 result、summary、完整 live binding、
  intent、status、model、B manifest/NPZ、condensed archive/NPZ 及14个 root 原数组。

**重建的基点是 actual62 原 warm，即原63固定模型的输入；
不是 actual63 输出的新 warm。** 完整父 producer 子树逐 dict 相同；
不是只看相同 schema。

## 3. 运行环境与最小 CLI

和原63相同：Python3.12.14、NumPy2.3.5、SciPy1.17.0；
OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1；
原 jac-workers=2，物理角 N2048、边界角4096，全部 M/T112。

仍须先从 exact_20261114_public_resume 调用现有
prepare_public_source，恢复原公开78文件，
设置 VISIBLE_SOURCE_TOPIC 指向恢复的
topics/visible-flexible-closed-surface。没有新增 source-root 参数，
不使用私有仓库。入口会按原 ZIP 内
public-source-preparation.json.restored_files 核全部78文件的字节/SHA。

当前 topic 的 computations/ 应完整 sparse 检出。原输入的
optimization-intent.json.source_sha256、condensed producer 的
frozen_dependencies、observer 原 source ledger 和原 full-DN
FROZEN_SOURCES 都逐一核对。实际执行的数学核心为：

| 核心 | 冻结 SHA256 |
|---|---|
| geometry_20261114_constrained_trust_warm.py | 5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2 |
| geometry_20261114_constrained_collocation.py | 70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8 |
| exact_20261114_regularized_block_qr.py | 596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722 |
| 保存的 R270 root/恢复定义 | 84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b |

示例：

    python "$TOPIC/computations/exact_20261114_actual63_model_response_decomposition.py" fetch \
      --out "$RUNNER_TEMP/actual63-original"

    python "$TOPIC/computations/exact_20261114_actual63_model_response_decomposition.py" analyze \
      --artifact-directory "$RUNNER_TEMP/actual63-original" \
      --accepted "$VISIBLE_ACCEPTED" \
      --tail-anchor "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz" \
      --out "$VISIBLE_OUT/actual63-model-response" \
      --budget-seconds 1200 \
      --jac-workers 2

原 fetch 完成目录就是 artifact-directory，没有额外 files/ 层。
读 _pinned_public_artifact_receipt.json 并核完整 PIN、ZIP SHA 和成功状态。
两个输出路径都必须新建；不修改输入、原 artifact 或原 warm。
建议 lane=modelresponse。

## 4. 重建的唯一完整模型

令原完整 scaled-z 算子为

$$
A=W_r J S^{-1},\qquad b=W_r R,\qquad g=A^\mathsf T b,\qquad
H=A^\mathsf T A+270^2 I.
$$

入口执行一次原 baseline.setup(accepted,current,anchor,4096,2)，
一次原 CompleteResidual.evaluate(...,require_rms=True)，
一次原 weights 和一次原 CompleteLinearization。原 LSMR、
随机验证方向、domain derivative 构造和 QP 都不再运行。

实际比对：

1. 原完整 mesh699、state/rhs699×453、S236036；
2. 原 Wr/b/g 全部236036坐标；
3. 原 L/R698×338×338、完整 P698×338×3；
4. 完整 BY112×338、BC112×109、BP112×3 及 inlet338×109；
5. 原 C 对角来源，作为历史/模型身份；新 QR 仍不用 C 列变换；
6. 完整 B 的18×2048行、13个原区间、17物理节点和全3控制；
   不把 baseline C 的4059支持误用于完整 H。

这些原模型数组必须逐 SHA 相同，才称为原63模型。
这属于来源/对象核，不是对一个不同模型新增数学验收门。

完整 QR 只重建一次，使用原冻结596356源。
原63 factor metadata 明确为 memory-only、四数组 file:null；
因此报告称**本次重建**。四个完整因子摘要与原摘要逐项比较。
若因子摘要不同，明示其差异；不以假称同一因子继续。
所有逆作用仍回到同一个、已逐字核回的原 A/AT 读完整残差。
没有 normal matrix、截秩或替换约束。

## 5. 分解和精度账

直接读原保存的 R270 root $\widehat R$、局部梯度
$\widehat g$、实际最终局部候选 $u$ 和完整恢复 RHS $r$。
重放原浮点顺序

$$
\ell=\widehat R^\mathsf T(\widehat R u)+\widehat g,\qquad
r=\operatorname{fl}(-g+\operatorname{embed}\ell)
$$

并分别核原 actual_local_force SHA 和原完整 RHS 字节。
该 $\ell$ 是**实际原局部求解与修复后的候选**所产生的力，
不冒精确 QP 最优解的 KKT 力。

重新计算的完整逆作用为：

- $z_c \simeq H^{-1}(-g)$：完整未约束中心；
- $z_B \simeq H^{-1}\operatorname{embed}\ell$：实际局部力的完整响应；
- RHS 加法的精确 dyadic 损失
  $e=r+g-\operatorname{embed}\ell$ 的每个非零 binary64 展开分量的完整响应；
- $z_r^{\rm new}\simeq H^{-1}r$：对原保存 RHS 的独立重放，
  与原保存 $z_r^{\rm old}$ 逐字对照。

每个局部 $e_j$ 由三个原 finite binary64 数的精确有理值相加得到；
其完整有理数与所有展开分量、残余都归档。展开在8轮内完全表示才可
称“精确 RHS 加法误差账”；这个有限实现预算不成为原科学门。
原 report 中浮点求得的 rhs_embedding_error 只作原报告转述，
不悄悄当作这个 exact error。

再显式定义有限向量：

$$
d_{\rm inv}=z_r^{\rm new}
 -\operatorname{fl}\!\left(z_c+z_B+\sum z_{e,j}\right),\qquad
d_{\rm replay}=z_r^{\rm old}-z_r^{\rm new},\qquad
d_{\rm select}=z_{\rm selected}^{\rm old}-z_r^{\rm old}.
$$

分别以同一完整 A 作用，保留全部向量和 A-actions。
$d_{\rm inv}$ 是有限求逆/累加闭合项，不能简单叫“真实物理效应”；
$d_{\rm replay}$ 明列新旧重放差；$d_{\rm select}$ 保留原全局选择影响。
所有数值加减的操作次序均在源码中固定。

原 row155819 及 interval461 全部338行，逐行保存：

- 原 b、每一 A-action 的数值/float64 bits；
- 原条件恢复、原最终选择与本次重建读出的 A-action；
- **对这些已返回的 binary64 数值作精确有理求和**所得的剩余差；
- 原 alpha 乘各分量，以及从原 b/Az/alpha 得到的精确数值线性预测。

这里的“精确”只指已返回数值的有理加法，**不将 A、QR、局部 root 或
原 ODE/J 升格为精确实计算**。全 H 逆的原 A/AT residual、factor residual、
两者差以及局部 center 与完整 center 限制的差均明列。

聚焦行另外按原 L/R/P 分别读节点461、462和全部3个 global p 的贡献。
这些单独乘积之和不承诺与原 A.matvec 的浮点汇总顺序逐位相同；
原完整 action 始终是主要读数。

同次以原保存的全部 B 行块读取完整中心和局部力的全角作用/余量，
并重读原恢复与原选择的 B-actions。只是固定模型内的半空间余量，
不替代连续角、完整非线性域或原原生尾验收。

精度提示复用 $H\succeq270^2 I$ 的真实代数式：

$$
|a_i H^{-1}\rho|\le \|a_i\|_2\|\rho\|_2/270^2.
$$

程序实际返回的行和 residual 都含普通浮点形成误差，
因此相应输出只叫精度诊断，不叫严格包络，不据它新增通过门。
不预写“唯一原因是 lambda”“约束一定主导”等结论。

## 6. 输出、预算与发布

主目录仅小 report/manifest：

- summary.json：小于100KB，包含来源、重建核、目标行、全部 inverse
  原 residual 摘要、原 alpha 和边界范围；
- result.json.gz：完整主报告，输入/旧报告和细节以描述器引用；
- array-manifest.json：所有新原数值 raw 数组的 shape/dtype/SHA/角色；
- large-arrays/：全部新方向、原 H residual、factor residual、
  全 A/B action、完整有理加法账、全338行表、完整输入/源/读回账。

所有科学大件都置 large-arrays/，只留 artifact，沿既有 publisher 排除；
不产生 large-audit/ 等未被现 publisher 排除的新大目录。
完整重建因子保持内存方式，导出四个全字节摘要，不再复制约1.49GB因子。
没有删除旧输入或原 archive 的步骤。

资源预估（接口预算，不冒执行实测）：

- 原下载约495MB；一次原完整 L/R 约1.276GB，
  四个完整 QR 因子约1.486GB，另原 local root约264MB；
  加原状态、方向、压缩解码与局部 front，16GB runner 仍有余量；
- 新向量/行账通常远小于因子；按源码实际输出保全，失败也留部分结果；
- 默认1200秒为诊断 work budget，factor 原有逐 front/solve 启动截止保留；
  已开始的 inverse 仍完成其强制原 A/AT readback；
- 三次固定完整 H solve（center、局部力、原 RHS replay），再加每个非零 RHS
  加法误差展开分量的一次；完整数目以实际 report 为准；
- 一次原基点 evaluate、一次完整 J、一次 QR，没有第二场、参数扫描或优化。

失败只写本诊断 failure/traceback 和全部已保存数据，
不改写原63的优化成功或全 BVP/native 状态。
本接口不阻止 prefix64 或 native61 的已有计算。
