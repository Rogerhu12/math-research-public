# 固定 M20 完整高度的冻结校准恢复接口

2026-11-12，root，GPT-6 Astra Pro，AI-assisted。

## 对象和验收

本接口仍处理已保存 raw `root-vu032-q085-fixed-actual-m20-resume1-outer-00-raw-collocation.json.gz`，其SHA256为`ef36aff558beb340e35f6ac84bfd3abe893186604abb8dd4d9d85bbebcfafb39`。全部911节点、20项高度、原三次配点数据及物理配置不改。初猜是第一次已完成的实际M20响应`95147d132e0c0662cae3e360f977f0759cf4080ce60272ce702d38039f6a07e9`；它不是更新后高度的响应，因此仍须真正重新求解。

`root_actual_staged_tail.py` 增加显式 `--storage frozen`。它只改四个原有输出/初猜字段，同时保存完整raw及配置的hash。`--reference-adapter` 指向原完整stored-ready，`--calibration-ledger` 指向保存了160个二进制alpha的ready。后者提供浅头有限参数，不把其中的有理深尾65/64换进stored对象。

新 `tail_frozen_geometry.mjs` 调用 `strong_frozen_calibration_factory.mjs`，逐源码hash核对，只将原本160次浅层校准结果换为其保存的准确二进制值。原160层物理公式、辅助远端校准和图构造保留；全局warp alpha显式固定。factory要求完整5点历史指纹及完整7点stored指纹都逐位相同。随后仅缩小point缓存，再重新计算全部7点指纹及factory两套指纹，要求仍相同。未提供的校准诊断字段显式拒绝访问，不伪造矩阵或导数。

`tail_frozen_worker.mjs` 保留原resumable worker的实际方程、完整变分后端、root和warm remesh；只选择上述geometry及显式GC。旧compact锚点错误已修为源中唯一的 `const sol=dn.solve(req.height,`，不是对方程作替换。`tail_frozen_client.py` 沿用原求解/关闭协议，另外核对两种历史指纹、160次参数复用和GC声明，记录所有新源码hash。若初始化失败，会尽可能把实际worker前后退出码写入独立JSON；没有观察到的退出码仍为null。

stage收到ready后还严格比较参考中的完整physicalParameters（只排除同四个IO/初猜字段）、全局alpha、指纹字段/采点及两套7点hash。随后执行一次完整相同H的 `jacobian=True,audit=True` 请求。输出收敛只证明真实有限尾通过；只有 `root_actual_pending_recovery.py` 再重算原RMS、入口门和物理true-BC门后，才生成前缀物理结果。恢复时 `--tail-config` 仍传原resume1配置，使raw原始identity核对不变；新尾响应配置仅通过四字段等价规则对照。

## 当前状态

接口的语法与所有替换锚点已核对；完整raw/准备计划已执行成功，20项高度完整保留（H2为−2.1668387574702766e−5，H4为1.6820535548210102e−8）。准备前误写原配置文件名的首次命令在读取配置时退出，未启动worker、未改raw。现正式计划是 `root-vu032-q085-fixed-actual-m20-frozen-recovered-audit-plan.json`。

本笔记初次保存时，冻结factory的运行时geometry检查和新的真实M20审计尚未执行。计划在strong当前BVP结束后，先执行geometry检查，再由root独占实际audit；不把语法通过或指纹约束写成已经通过的运行时结论。后续实际状态另写run-state，不回写旧失败记录。
