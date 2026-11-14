# 同 g 首轮精化：已存在的物理 DN 入口与当前 live 尾的窄接口

作者：ChatGPT（geometry 子会话）。日期：2026-11-14 UTC。

分类：冻结源码的静态接口核对。本文没有准备新场、计算 H、调用原生尾、执行 FD、重解 BVP 或生成几何读出；所有将来的数值仍须由本公开仓库 Actions 执行。actual61 已实际失败，当前没有由该 run 产出的成功非零尾锚，更没有本主线真正接受的完整 v3 父场。

## 1. 已有完整数学链，不需要重新实现精化方程

现有入口如下，均位于 computations/。

| 环节 | 既有入口 | 实际作用 |
|---|---|---|
| 完整原 scalar 冻结 | `geometry_20261114_same_metric_profile.py` | 将已接受 v3 的完整设计说明及三个 p* 逐字嵌入 v4，建立 canonical scalar SHA；后续 v4 再精化展平到同一 v3 说明，不把空 active p[] 当成原 p* |
| 全场初猜与网格精化 | `geometry_20261114_same_metric_prepare.py` | 真正接受父场与其 own final-audit response/config 先绑定；用完整物理 y、保存 RHS、既有二阶规则构成原 PhysicalQuintic，保 z0，保原全部节点，并执行原域 preflight |
| 真正当前 H/J 与原 FD | `geometry_20261114_same_metric_physical_response.py::run_response` | 为 prepared 的真实末端算 H，实际求当前尾与完整 J；只在这个实际局部 affine 图上运行原三扰动、Richardson 和 5e-5 FD 门，可保留同一个 live client |
| 同 g 完整非线性求解 | `geometry_20261114_same_metric_physical_full_dn.py::solve_session` | 通过 `existing_client` 一次移交同一个 live worker；原 v4 full solver、物理 phi 测试、原 Newton/回溯/全域 RMS/终审保留 |
| 成功后的物理读出 | `geometry_20261114_same_metric_physical_after_accept.py` | 同一个真正接受 v4、own final audited tail、完整 cut 报告、原 scalar sidecar 经既有 v4 SavedPrefix/材料角/尾/闭包读出；不继承父场 reach、幅度或 R249 修补 |

首个 v4 在固定完整 p* 之后释放所有 core：`fixed_core_modes=0`、`active_scalar_parameters=0`，M 个 core 系数全部自由。物理维数为 `3M+2`，常 core 为 M，完整 BVP 状态 `4M+2`；左边界 `3M+2` 行，右边界 M 行，`T=M`。不存在继续固定原 32 core 模式或保留三个活动控制变量的精化捷径。

`freeze_spec` 原样保留完整 v3 scalar 说明、三个 p*、所有 supports/公式/原 finite-Gauss 定义、原 port、原 accepted96 source 身份。`field_modes` 和 `tail_modes` 是新的场分辨率说明，不重写原 base_prefix_M，也不改变原完整 a(s)。原 g 的识别依赖这份完整 canonical 身份，不能用共享背景 B 的导数代替原 g。

## 2. 699 节点二分与原 1200 预算

prepare 的 `--subdivisions 2` 将每个原区间中点与所有原节点、profile knots 一并传给原 merge_mesh，不删除原节点。若父场确有 699 个彼此不同的节点，单纯逐区间二分已经产生 1397 个节点；profile knots 及原 RMS 域 preflight 还可能需要更多节点。

prepare 默认 `--max-nodes 1200`，源码在生成显式请求网格后立即检查预算，因此这组默认值会在科学求解之前拒绝 699→1397。原 `geometry_20261114_full_dn_solve.py` 的 `--max-nodes` 也默认 1200，必须在 prepare 和完整求解两次 CLI 中显式传同一个足够的实际资源预算。提高资源预算不放宽 RMS、边界残差、域守卫或原 Newton 接受规则；不能为迎合默认预算删掉父节点或把二分写成完成。

未来准备阶段的最小现有命令为：

```bash
python computations/geometry_20261114_same_metric_prepare.py \
  --parent-field ACTUAL_V3_OR_V4.json.gz \
  --parent-tail-response OWN_FINAL_AUDIT.json.gz \
  --parent-tail-config OWN_INPUT_CONFIG.json \
  --field-modes 112 --angles PARENT_OR_FINER_PREFIX_N \
  --subdivisions 2 --max-nodes EXPLICIT_NODE_BUDGET \
  --out SAME_G_PREPARE
```

这是参数模板，不存在已经接受的 `ACTUAL_V3_OR_V4` 替身。父场实际节点数、M、N 与完整 SHA 必须来自真正接受的原件。prepared 的 `success=false` 正确地表示初猜，不是新场接受。

## 3. 同 M112 的 live 尾接线只差身份适配，不差一套新 FD 方程

现有 physical response 确实能把真实非零 H/J 与后续 full solver 保持在同一 live client。它已经具备以下正确行为：

1. prepared 的实际 H 重新计算，不假设与父场 H 逐位相同。
2. FD 仅调用本次真实 H/J 的 affine 图，FD 过程中 worker call 数不能改变。
3. `solve_session` 唯一移交这个仍存活的 client 和同一个完整冻结 profile 对象。
4. full solver 首个 H 若不同，仍真实求新的 H；同 H 的原进程内非 audit 缓存保留。
5. 最终 audit 必须再实际发送原 worker 请求；完整物理 cut 审计不等同旧材料 theta 边界验收。

但旧 response 仍绑定最初的单请求 TailClient，不能直接只换 CLI 文件名。源码实际有三个需要新独立适配器明确处理的身份假设：

- `build_context` 强制 `tail-client` 的文件 SHA 为原 `true_tail_client.py` 的固定 SHA。
- `validate_live_response` 强制 `client.calls==1`，并只读取 `_0001.json.gz`。新的 current576 live client 先实际 bootstrap，随后当前 prepared H 可能是第 2 个真实请求；也可能与 bootstrap H 完全相同而在同进程缓存命中。必须按真实请求记录绑定本次实际 H/J，不能将 `_0001` 改标签。
- 旧检查将 `client.sources` 除两个 config 键外全部与父 response 的来源逐项比较。新 live client 正确地另加 R273 hook/adapter/QR 的来源身份，同时保留 `original_sources`。新的检查必须分别核不变的原 native 数学源、该次新增桥完整来源和 actual parent 的来源；不能删去来源字段或用一份旧父摘要冒新 worker。

最薄的源码扩展应复用原 `run_response` 的数学 FD 主体以及原 `solve_session`，只单列这些真实 client/请求/来源绑定，使用新的 report/入口身份。没有必要复制 PhysicalTestBoundary、重新写三扰动或新建一套 v4 求解器。最后输出仍需满足既有 v4 accepted producer 的所有原门，且明确新 finite phi 方案与原 theta 报告的区别。

## 4. 当前 224 维尾桥不能冒充更高 M/T 或不同尾网格

当前 `geometry_20261114_current576_live_tail_client.py` 及其 hook、`LiveCurrent576System` 严格绑定 M112、K224、depth576 和原物理 rawNode `[0,72,144,216,288,360,432,504,576]`。完整 H 长 112，seed 状态 577×224，返回高度/斜率/二阶及完整 J 按同一容量检查。bootstrap 的配置及 ready/图/gains/原源也逐项固定。

因此，同 M112、同尾配置下的前缀径向网格精化和前缀角求积加密，可以复用这套 native 维数；增加前缀节点不要求把原尾的 shooting 节点也加倍。这仍只是可执行接口范围，不保证新的 BVP 会接受。

若把场模式改为 M128，则同 g 虽仍可由原 scalar 身份保持，但 T 必须真为 128。此时当前 112 高度、224 维 seed、固定 576 桥数据以及原容量/ready 不能通过补零 J 或更换 metadata 充当 128 的实际尾。需要新容量下的真实 constructor/ready、完整新 H、实际尾配置和初猜、完整当前维数的 snapshot/QR adapter 以及新 final J/audit。改变 tail steps 或 shooting 分区也同理。现有 v4 原 prepare/solver 已支持一般 M；真正缺口在这个具体 live native 实现，而不是 scalar 冻结层。

此外，现有 live client 的 bootstrap 来源硬锁“已完成 native61”的成功 result、完整成功 J/audit 和 checkpoint。actual61 的真实 `native_accepted=false`，所以本次文件不满足入口条件。不能把最后失败 checkpoint 改成 completed anchor，也不能把它作为跨进程成功响应缓存。后继若采用新的成功 native 入口，需要独立明示新 producer/schema，并在新活 worker 中再次真 solve/J 建立 predictor 后才移交外部新 H。

## 5. 真正需要的下一组实际输入

开始首个同 g 非线性精化，最低限度需要：真正接受的完整 v3 父 checkpoint；它自己绑定的最终实际 native audit/J response 与 input config；完整 cut 审计和实际 live scalar sidecar；原 accepted96 source 与原 port；本次 prepared；本次完整 native 源树与真实配置；新的真实 live worker 所使用的成功初猜来源。若复用父求解进程，必须明确所有权移交，不能在原 full driver 已关闭 worker 后仍称“同一活进程”。

源检查已经排除了两个可预见的纯接线阻断：1397 节点不能沿默认 1200，新的真实 bootstrap 请求不能沿 `calls==1`。当前科学缺口是完整父场尚未接受以及 actual61 尾未收敛；本记录不创建新的审批、容差、机器精度六/九 jet 或间接证书门。成功 v4 的闭面、R249 规范形、共享 B、reach 与真实整像幅度仍逐对象按已有链实付，不能从父几何移植结论。
