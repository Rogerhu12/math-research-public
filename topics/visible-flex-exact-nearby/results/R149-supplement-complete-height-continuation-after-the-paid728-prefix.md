# H96 全96列高度积分从实际728格前缀接续

**接续公式及完整入口已完成，后缀数学尚待本次真实执行。** 原[实际728格](../notes/2026-11-28-H96-actual728-prefix-and-rule-interruption.md)属于 run46123190757/1，child −9由根README新增模型规则触发，未完成任一最终目标。本次保留其全部96列带号积分球及uniform adjoint误差，只评价原2847格中的 `[728,2847)`。原首次source、math、worker均保持不变，由三个显式AST适配点和受限循环适配实现。

## 同一个完整积分

原前缀在精确缝 `5854679515581645/144115188075855872` 结束。对第j列记旧完整多项式积分球为 I_j，旧全域已处理部分的adjoint误差上界为 E。新循环独立从零累积后缀球 S_j，保留旧原始网格与全部交格顺序。每个新完整检查点以及最终值使用 I_j+S_j；误差使用 max(E,E_suffix)。因原canonical高度的余项为整个原P96 L1列 H_j 乘全域adjoint最大误差，完整高度仍为

`I_j + S_j + [-max(E,E_suffix) H_j, max(E,E_suffix) H_j]`。

全部96球同时带入，未选子列或midpoint。Arb按原60位保存的球向外读回；每次新的累加保存再次检查包含真球。原角度/径向度上限与交格计数采用旧新max/累加，不把前缀当零。新循环首个TC指针只按原plan的精确端点定位，不评价旧Hermite或旧高度格。

两原mean、全部8192 directed角点、真实physical-coordinate项及原whole RHI A9/x3误差均在未改原math中。后缀完成后才按原次序形成7个完整目标：canonical height96、waist-Jacobian L2 upper96、reference height96、actual-cap height96及joint radius、height-reduced phase96及joint radius。它们仍是同一原有限trial的观测，不是true PDE校正列或完整Schur成功。

## 完整输入与原成功不重算

新manifest `2026-11-28-finite-trial-height-after-728-inputs.json` 为66236 bytes，SHA256 `e730fd1e12b72356c88aa7718f8baa4e5e5c083e66a60a6612d71028d281ef69`；123个current整件及51个原历史描述，原114整件全部保留。原actual、execution、consumed与manifest全SHA、实际失败run/attempt/event/checkout、728格prefix完整SHA均准入。根会话已读并执行新#16的独立回执属于完整current输入，原旧review同样保留。

原四TC、四NP及完整2847七系数RHI缓存/全18端点与链仅作必要输入恢复；全部原whole bytes/SHA与父actual逐项相同后才进入新math。原728已成功height格以及已成功L1、phase、RHI目标不重算。旧载体提议的计算与后缀新数学分开记账，大数组只private。

公开worker在materialize两处及最终保存后均核GitHub实际父run/job已终态failure，原job `140911924186` 的 `head_sha`、`run_id`、`run_attempt`、`completed_at` 已由根会话真实API核对。新run与父run必须不同，并采用新唯一consumed路径；原旧consumed不删除。每次pull仍检查两README，后续新差异必须实际应用，原停止规则不绕过。

公开入口为 `.github/workflows/visible-exact-finite-trial-height-after-728.yml`，固定原Python容器、numpy2.3.5、python-flint0.9.0和原Haswell载体合同。原18000秒科学预算、private磁盘/内存、210000B公开总预算及topic容量门不变。原日志给恢复约68分钟、728格约52分钟；剩余2119格的预估只用于安排作业，实际全目标及返回码才决定成败。

root已核全部123 current bytes/SHA/Git blob、源码AST、原数学逐式变换及workflow YAML，代理的metadata-only原admit和3个完整AST构建均通过；未在本地调用科学。全成功后PWA96通过新真实身份和完整父链准入，不伪装原H96成功。
