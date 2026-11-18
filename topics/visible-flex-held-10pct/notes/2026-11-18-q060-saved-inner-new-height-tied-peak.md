# q060：已保存原内解后的新高度尾部终态

本条是 `2026-11-18-q060-same-height-parts16-coupled-entry.md`
所冻结入口的真实运行结果。会话 91135 正常终止，observer 的进程
退出码为 0，但原 coupler 捕获了尾部异常，最终明确
`solver_success=false`；不能把进程退出码当作数学接受。

## 1. 旧高度已通过，原内解确实保存

从本轮真实接受的 `H_old` initializer 出发，原 worker 的 call1
（audit）和 call2（Jacobian）都在迭代 0 接受
`1.835729812540257e-9`。两份实际记录的 SHA-256 分别为
`cb050d098d6b38715d288b8bf83e4c91abb368f9e0c0cfd1419e0f9dcc481b40`
和 `6761d1f70528e31f9ee28a39b7fd25a3a4ad65552d535ea03e76e8a957c01f06`。

原 affine-DN 内解随后返回 `projected_solver_success=true`，最大
collocation RMS 为 `9.977585220921287e-7`。在提交它产生的新 H
之前，两个原保存 hook 均已执行：

- `seed-inner-0000-debug.json.gz`：SHA-256
  `67112318acde56cf1c797267b2069885e50567f4b5052db008acda64cf70d84d`，
  保存原始 mesh、节点值、参数和 cubic 的原坐标、breaks、coefficients、axis。
- `seed-inner-0000-dn-anchor.json`：SHA-256
  `ec23c070f93692835d400a5f0eae60ba24669c862c1045e5184a465483877715`，
  逐项锁定上述 call2 的完整实际请求、响应、配置与来源。

它们均在 `closed_work/q060-coupled-parts16-hold-v2`，并明确标记
`actual_tail_accepted=false`。此前原内解丢失的问题在这个新运行中
已经解决；这些原始数据不冒充通过完整 metric 的物理 C2 图。
原 `sol.message` 与逐区间 RMS 向量没有保存，后续如续接必须如实
区分；已保存的是 RMS 最大值，不应补造缺失诊断。

## 2. 新 H 的原尾失败与唯一外部预算

原 call3 使用这份已保存内解的完整 candidate H。原校正到迭代 4
停在归一残差 `3.6679653943562417e-9`，随后原线搜索失败。
完整失败记录为 `seed_tail_0003.json.gz`，SHA-256
`845d89e7695d3bf158db56661632e64e38ade4c0d2ea707c32ed1f959eaef8f3`。
M8、N128、depth8、parts16、RK16 与原 `2e-9` 门没有改变。

resource-v3 随即执行原预声明的一次 candidate-only helper，显式
Node heap 为 3072 MiB。该子进程正常完成，没有此前的 heap-limit
中断。它实际评估了 3 个 trial；这三个 alpha 在 binary64 下都产生
同一标量变动：节点 86 分量 8 从 `-955.7444723972236`
变成 `-955.7444723972237`。没有选择任何 pass。

只改这一个分量后，行 85 的范数为 `3.0559280277702046e-10`，
行 86 的峰转到分量 9，仍为 `3.6679653943562417e-9`；
未受影响部分的最大值为 `1.574687590969853e-9`。
由原依赖式

$$
R_{86}=\Phi_{86}(X_{87})-X_{86},
$$

改变 $X_{86}[8]$ 不会改变 $R_{86}[9]$，故这个现有记录已确定本次
新 H 的分量 8/9 并列峰。它不同于此前旧 H 的分量 8/11；
本条没有据此猜测分量 9 的符号或 ULP 数，也没有重做全域 locator。

唯一 helper 的完整原 full-Jacobian 重放与原失败范数逐位相同，
完整状态未改变。因此 adapter 按既定预算返回原失败，未启动新的
native worker，也未再执行前缀。候选输出始终是未接受的 initializer。

## 3. 可精确续接的边界

此时已有真实原内解和真实旧 DN 锚；新 H 仍未通过原尾门。
后续若根据这个新失败态构造有根据的有限初值，仍须由原 worker
对同一完整 H 用原门、Jacobian 与 audit 真实验收。
若成功，续接点是已保存内解后的 actual-tail 查询，不能再把旧
warmup 或另一高度的响应当成这个新 H 的解。

紧凑执行记录是
`scripts/resume_transfer/q060_same_height_saved_inner_terminal.json`。
它绑定全部原 H、物理 profile、完整输入参数、source/command/hash、
observer 真终态及已保存内解。大数组只留在 scratch，仓库不提交。
