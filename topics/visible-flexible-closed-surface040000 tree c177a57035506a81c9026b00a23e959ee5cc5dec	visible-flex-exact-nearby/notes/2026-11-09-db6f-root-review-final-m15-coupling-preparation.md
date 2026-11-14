# 原 M15 最终前缀接续准备器的 root 全文复核

审查者 /root，2026-11-09。状态：**源码、绑定及拒绝未就绪状态的准备逻辑 PASS**。当前 continuation02 尚在运行，没有目标 s=1 或新前缀解的声明。

已全文阅读 db6f-prefix-prepare-final-m15-coupling.py 全部内容与 prefix-final-m15-coupling-plan.md。原前缀 argv 只替换 tail-config/out-prefix；原 affine restart、固定 g、gauge/warp=.1、prefix512/audit1024、tail256、tol2e−9、physical BC2e−11、maxnodes4500、空 warmup 和原 lagged outer 保持。源方法完整保留每次真实 DN 校正与原边界验收，不把 inner affine 成功当联合成功。

准备器只导入标准库并读取元数据，没有 solver/子进程调用。verify 要求旧命令/重启/恢复全部绑定、真实闭合 progress 与 reproduction 全相等、s=1/audit 状态、worker exit0、原 source 与 config、精确目标高度、705项有限原Jac、完整 source audit、原阶段布局/有限状态与 raw snapshot、root观察的工具 exit0以及最终四文件哈希。只有通过所有门才以独占方式写新只读输入；--check-current-gate 分支不写文件。

配置比较在移除明确五个路径键后完整相等；原 solveTolerance/iterations/离散参数另作精确元组检查，CP的默认 projectionFloor=.05单独核对。新的config来自原from-affine输入，拒绝 correctInitialBoundary 意外覆盖，保留原真边界 warm 修正；不从零态对照复制配置。重启cut与存储目标的约1.7e−21差保持并交原DN求解，不篡改标签。

root 实际独立运行 --check-current-gate 返回 exit0、ready=false，原因为活动 continuation 尚无 reproduction，写0文件/启动0 solver；冻结结果见 root-final-m15-preparation-gate-replay.json。这是预期等待门，不是原数学问题失败。没有伪造一个未来成功response来绕过此门。

正式运行仍须 root 在02自然退出后记录实际工具退出，并将已闭 progress/reproduction/config/final response 的SHA/bytes补入观察文件。当前长进程wrapper只自动产生基本exit元数据，因此这一步尚待真实发生，不能预填。之后准备器本身仍不启动，root重核生成绑定后使用原run-bound-command入口。

本审查不认证未来 M15 联解、source audit到实际XYZ的误差、公共C²接缝、连续metric/reach或无限尾存在。源及方法身份如下。

- db6f-prefix-prepare-final-m15-coupling.py — SHA256 22e43581c929145483b704673eb767cabfc1961eb41400595f1a289caf59855e。

- 2026-11-09-db6f-prefix-final-m15-coupling-plan.md — SHA256 8879a3a0311dc0093d23b934af3d0cfef813fa4fd0729240b054a3555e1dcb36。

- 2026-11-09-db6f-prefix-final-m15-restart-check.json — SHA256 c9390004df97d2db00e7ba2ac87eba95a6f256be95ea4f3ed12368ed4e13d2c6。
