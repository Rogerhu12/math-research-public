# 同一公开运行环境中的持续材料计算

维护：Astra-held10-1b6d88ec-20261120；2026-11-20。

## 必要性和边界

第二次真实作业已经证明 H1 幅度入口可恢复 q060；材料 λ=.02 的投影 BVP 也收敛，但原 metric 未门。该 job 结束后 raw/physical 场不能继续读取，而完整角谱、均值定义与原 trueDN 校正都需要同一实际场。新入口只解决这种接续需要，不建立新的数学接受或放宽任何门。

独立 workflow .github/workflows/held10-live-material.yml 先恢复同一70源、物理输入及数值库，再运行 scripts/resume_m3/live_material_worker.py。源码 SHA256=a6f63525bc30572aa1a9b42aad3e31e5f0e9d8034fa1e7f24cd25cd5ddb3b5bd。初次发布尚未运行；首次命令必要再生已登记 H1 路径，结果不能再算一条新数学接受。

## 精确请求与可见结果

ci/live-material-start.json 只触发新 runner；ci/live-material-command.json 声明每条唯一 id、已读双 README 提交、课题脚本、字面参数和需要回报的 JSON 小字段。路径标记 @REPO@/@WORK@ 仅作路径替换，不运行任意 shell 文本。一次实际命令的物理模型、门和日志由其原脚本定义。

worker 在启动每个新 id 前真实 git pull --rebase 并比较根/课题 README 与 read_rules_commit；若不同，只回报精确差异并等读完后的新请求。运行期间至少每3500秒再真实pull和核规则；规则变更会停止当前命令，保留本地输出并回报待接点。每个 id 在启动前登记 scratch，worker 重启不会盲重跑同 id。

每60秒读取显式白名单的小JSON，内容实际改变才写 ci/live-material-result.json；没有以运行时长或heartbeat制造的重复提交。每条结束记录退出码和实际诊断，退出0不等于数学完成。结果始终 complete_surface=false，完整验收由HANDOFF/notes单独记录。

GITHUB_TOKEN仅从该workflow进程环境读取，子求解进程剔除token/secret/password环境项。结果通过Contents API提交，有并发冲突就重新读当前文件sha后重试；不force、不写用户令牌、不把令牌放进文件。其他网络/权限错误明确回报，不能冒充计算终态。

## 数据与生命周期

场、网格、矩阵、样条和native临时输出只留在单一runner工作目录；无Git/Release或Actions artifact上传。回报仅原记录的白名单小标量/短控制列表、哈希、状态；滤掉场/网格/矩阵/样条字段，整体≤64KiB。最终可复现性由已经提交的源、参数、命令和小结果提供。

worker最长5.5小时或空闲30分钟只结束该运行器，不代表课题完成；接续者继续实际任务，必要时按已经记录的命令再生输入。不得把尚未读取的作业终态编造为成功或失败。
