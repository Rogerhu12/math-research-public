# 原完整 Rφ 方程的精确约束 LSMR 初场入口

本记录是 request17 / coupling112trust 的公开 Actions 可执行接口，不是新的已接受场或存在性结论。实际 request13、14、15 分别用完整带 LU、原 separated QR、解析桥网加密，均未接受；request15 的 1073 点方向更大。因此这里改变产生初场的全局化方法，随后仍把真实初场交给已冻结完整 full-DN 入口与其全部接受门。

## 输入与有限问题

入口只使用实际 accepted96 前缀 `b4d2b98…`、实际 699 点 M112/N2048 准备场 `0f94dd88…`、完整已完成 T112 零高度响应 `e788a28d…` 与其输入配置 `01930f3b…`。不从失败的 966/1073 插值场重新开始，也不抬 1200 节点门。新计算中保留 699 个原节点和全部频率；物理节点值是优化未知量。

三个独立源为：

- `geometry_20261114_constrained_collocation.py`：精确坐标、原完整残差、原 L/R 块的矩阵自由动作与伴随。
- `geometry_20261114_constrained_trust_warm.py`：有界正阻尼 LSMR 优化，逐次保全实际下降初场。
- `geometry_20261114_constrained_trust_response.py`：在真实新初场上重新进行完整 Rφ 三步 Richardson 导数核验。

固定前三个 core 系数，其余 109 个 core 与三个标量控制各使用一个全局向量。物理初端由 `r0=1,rj=cj,tj=−2j*cj,z=0` 构造；其余节点每点保留全部 338 个物理量。每次展开都逐值复制同一 c、p，原常值 ODE 与左边界成为代数恒等，未用软罚构造变化的 c(s) 或 p(s)。当前未知和残差维数都是 `338*(699−1)+112=236036`。初端若与输入有舍入差，记录 `input_constraint_projection_max`，不声称所有源节点状态字节未改。

目标残差仍是全部 338 个物理 Hermite/Simpson collocation 行和全部 112 个 Rφ 行。每个 trial 都从真实 trial 状态和控制重算节点 RHS，再生成真实非线性 Hermite 中点、重算中点 RHS；接受优化步前还检查原两组 Lobatto RMS 查询的定义域。右边界保留原 uniform-physical-φ 密度门以及材料逆图异常的原处理范围。

## 矩阵与优化算法的身份

L/R 由原 `separated_qr_bvp.local_blocks` 和原复步长有限 ODE Jacobian 产生。共享 p 列取原两端参数列之和；首区间 core 列含初端 r/t 注入，右端保留完整物理、core 换角与控制列。没有截掉小奇异值或删除高频行。

系数尺度为 r/t 的 `(1+2j)^2`、z 的 `1+(2j)^2`。core 尺度是初端 r/t 两项二次罚的拉回 `sqrt(wr_j^2+(2j*wt_j)^2)`，因而保留 t 中的三阶频率代价。控制尺度使用其原 0/1/2 jet 样本最大值且至少为 1。这是明确的算法罚范数，不是完整物理 C² 范数证书。

每个模型固定行权重 Wr：物理 collocation 为 `1/(h*(1+abs(fmid)))`，右边界为 `1e−6/1e−11`。令 `A=Wr*J*S^−1`、`b=Wr*R`，正阻尼模型是

$$
\min_z\;\|Az+b\|_2^2+\lambda^2\|z\|_2^2,\qquad\lambda>0.
$$

实际 LSMR 操作 `[A;lambda*I]` 的列预条件形式，调用 `damp=0`，没有形成法方程。列预条件由这个矩形算子的完整列平方范数决定，未改变上述罚项。

trial 约定为 `q_trial=q+alpha*z/S`。真实 merit 是 `0.5*||Wr*R||²`，整个模型及其 trial 固定同一 Wr。所记录的真实模型斜率为 `b·Az`，预测下降为 `−alpha*(b·Az)−alpha²*||Az||²/2`。接收条件比较实际下降与这一预测，而不套用只有精确 Newton 逆才有的斜率恒等式；阻尼罚项也不计入实际非线性 merit。

每个模型先进行三组确定性伴随点积检查，以及原完整增广 L/R、右边界动作与约化动作的对照。另把仅含 free-core/global-p 的同一真实方向直接送进原非线性 complex collocation 调用，独立检查初端和中点的完整链式。每个有效步再保存实际全残差的三层中心方向差分。它们是实现核验，不是几何接受结论。

## 运行及后续完整求解

第一步：

```bash
python geometry_20261114_constrained_trust_warm.py \
  --accepted "$ACCEPTED96" --prepared "$ORIGINAL699" \
  --tail-anchor "$ZERO112" --tail-config "$CONFIG112" \
  --out "$OUT/constrained-warm" --iterations 3 \
  --lsmr-iterations 80 --damping 1 --damping-attempts 5 \
  --line-search-steps 17 --budget-seconds 1200 --jac-workers 2 --angles 4096
```

默认最多三个完整 Jacobian 模型、每模型五个阻尼尝试，每次 LSMR 最多 80 步；1200 秒是该辅助优化的计算预算，不是课题停止条件。每个实际有效下降写独立 `warm-NNN.json.gz`，始终 `success:false`、`new_coupled_finite_acceptance:false`。状态文件列出 `latest_warm_file` 与实际 SHA；可用 `--resume` 从真实已保存初场继续，仍严格绑定原输入、原 mesh、全部 scalar 设计公式和三个全局 p。无实际下降则明确失败并保留诊断。

第二步从状态文件读出真实最新 warm，实际重跑完整导数检查：

```bash
python geometry_20261114_constrained_trust_response.py \
  --accepted "$ACCEPTED96" --prepared "$LATEST_WARM" \
  --tail-anchor "$ZERO112" --tail-config "$CONFIG112" \
  --out "$OUT/physical-response" --angles 4096
```

这个核验明确把已完成的真实零高度 J 固定为 affine map，并在真实新 warm 端点及原规定扰动上实际求差分。新 warm 的 H 不必为零，报告保留 H 与 affine anchor 的区别；没有把零响应冒充这个新 H 的真实尾解，也没有重写旧 FD 报告的 SHA。原三步、两组 Richardson、收缩要求和 `5e−5` 门保持。

最后原 `geometry_20261114_physical_test_full_dn.py` 使用这个 warm 和新 `response-check.json`。其首次新 H 调用、完整真实 native J、外层回验、原 `1e−6` RMS 与冻结物理 RMS、`1e−11` 边界和最终 fresh native audit 全部实际执行。原 strict 零缓存只有逐值零 H 才能命中。只有完整入口真正接受后，才进入原物理读出、闭组装与 R249/R251/R254 等后续证明链。

本地只做源码静态核验，科学数值只在公开Actions执行。request17已于2026-11-14T13:16:20Z启动run43598917532，source4b8b2bfdd417f76574dcc2a8e2353c4c2dce3e21，job132459290659目前在warm步骤；尚未取得终态产物，不预报有效优化步或接受场。

## 本次源与执行绑定

| 新源 | SHA256 |
|---|---|
| constrained_collocation | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| constrained_trust_warm | `5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2` |
| constrained_trust_response | `7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78` |

完整有限代数的证明见 [R256](../results/R256-exact-constraint-collocation-and-damped-descent.md)。共享workflow从真实状态文件读取最新warm并核SHA，再接真实FD/原fullDN/after_accept/R249。publisher的非快进去掉旧30次截断，按用户要求立即pull/rebase/普通push至成功；其他Git错误或README变化明确报告并保全原件，不强推。

## Native tail 前独立保全 warm

后续 `coupling112trust` workflow 在 warm/实际FD步骤之后、native fullDN之前，额外上传 warm目录、完整FD回执及实际T112-config 到独立 `visible-mainline-warm-...` artifact。即使后面的新H原生尾耗时较长，已经产生的真实下降场也能及时取回、核SHA和续接；原最终完整artifact/publisher仍保留。该保存步骤用always执行，不改变warm/fullDN接受状态或任何数值源。它不会回填已经启动的request17旧workflow，也没有为取得日志重跑当前求解。
