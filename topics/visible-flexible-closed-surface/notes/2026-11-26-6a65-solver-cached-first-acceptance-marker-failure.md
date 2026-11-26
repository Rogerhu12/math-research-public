# cached 首步真实完成后，重复 HANDOFF 回执使发布退出

**可信度：实际 job 日志/API、已知输出 SHA 和本地真实 Git 回放。首步仅重生早已登记的 cold 接受，不计新的科学接受；没有第二个非零续步。**

## 纠正静态状态和真实时序

`run 45825253169` / `job 139927634135` 的主体在 **2026-11-26 13:34:59 UTC** 退出 1。它不是一直运行到 13:50：13:34:33 的 jobs API 仍 in_progress；随后监测只读取未更新的预处理 scalar 文件，未立即再读 jobs，导致把陈旧 running 标记继续描述为活动状态。13:50:04 的新 jobs API 已核实 `completed / failure`，这里明确更正。

decoded job 日志 30102 字符、256 行，SHA-256 `f16278c887257179662a53d62bd99fc98cabc0230427cf024494303259c0c0cf`。完整可重算日志不入库。

## 实际数学进程已经完成的部分

源为本 run 自己真实生成的 public recipe no-z INITIAL，accepted 0：

- 原 source SHA-256 `363e6d6af81de7b7bb7483e2ba27ae7bf67c86a732793473e8db4a4a62586cbc`。
- 原同场 observer SHA-256 `ca03fc1c9f25ac1b79653720e2262eb55d877c7d44ceaa08ac4f6dc0572b0e77`。
- 首 Cartesian baseline 在 13:22:39 真实返回：7760 列、323584 训练点、4,206,592 行；完整 R²=69144.79134082646，metric=2.491842255552956，曲率=655322.4740563247。
- 实际初态 SHA-256 `2ad8dcce763b2effe40c8eb39be6974fbc9d8f7ee3a926a52e662f83b7185002`。

13:23:10 的完整 LSMR 80 次返回 `istop=7`，31.14726253999993 秒，不报告线性收敛。13:23:11 全目标试步 alpha=1 真接受：R²=16795.946474434848，metric=2.3871653285124586，曲率=358035.05895042024，held=.6004407459257044。

- 实际接受 state SHA-256 `4a5d847e282b4d046dee5c4a0e85e4e7f04adc0e40662e2914d44ab50a8b4daa`。
- 13:34:56 真正完整密观察：432128 点，metric=2.387477496393237，曲率=171535.8011964779，held=.6004373058382321。
- 实际独立 observer SHA-256 `2410ab39d64a75c811bfd4abed4b9fefea3f9c94465c429576ef408799523d97`。
- 实际完整 report SHA-256 `bf2ca1c1848b883bb8e47247ef06324767d794094cc8a02a5be23b58e7e78bd2`；入口内部总用时 1281.406877922 秒。

生产入口已打印 `independent_cartesian_experiment_complete`。控制器随后通过它的实际进程 exit 0、source child 自然 exit 0、完整报告与两状态文件字节校验，才进入题为 `actual attempt 1 exit 0 accepted True` 的本地提交。即失败发生在其后发布，不能反称数值试步没有发生。未直接获取的过程 stdout 文件 SHA 保持未知，不由日志片段拼造。

这些值重生此前 `run 45812620369` 已见的同一首步；本 run 的 priorScientificallyObservedAcceptedSteps=1，所以新增科学接受数仍为 0。训练和密观察径向网格不嵌套，密观察较小的曲率不能覆盖训练已见的 358035。强目标仍远未合格。

## 实际发布故障

13:34:57 控制器做本地 scalar commit（日志短号 `672c52a34`），随后真实 pull/rebase 至 `5932d52dc1967161044f78add98ed9dcaf34d700` 成功。在该上游的 HANDOFF 第 2 和 42 行，实际存在逐字一致的两条 `6a65-cartesian-continuation-ci-rules` 回执，都是本 run `45825253169/1`、同一已读 commit `caf0ed46862848810e2181f8089abdf89ee2e801` 和时间 `13:13:33`。

冻结 v4 publisher 第 219 行见多个自己的 marker 便抛 `Duplicate own HANDOFF markers`。因此普通 push 尚未调用；外层失败回执也在同一重复 marker 处失败。第二个日志短号 `6e48181d2` 同样只是未推的本地失败提交，不冒充可从远端恢复的 commit。root 后来约 13:35 在 `e8c60d49` 将两条同文回执合并，晚于本次失败；不是非快进循环或数值模型问题。

没有 attempt 2，未验证云端同 cache 的第二步复用；先前小型接口核不替代这一缺失。结束 job 的 raw 不作为新的可用输入。

## 最小修复及真实本地核

新另名 v5 controller 只自动合并**逐字一致**且以自己完整 marker 开头的重复行，记录移除数及原行 SHA，然后写本次真实 pull 回执；其他 HANDOFF 文本不改。不同内容的重复 marker 保留原字节并明确拒绝静默选择，不以删历史的方式过关。活着的旧源没有热改。

新控制器 `scripts/6a65-actions-cartesian-channel-block-v5-20261126.py` SHA-256 `5055b47a891bb106557842976a6f4766121edf893605fd7a551a39c223283d29`。

真实本地 bare-Git fixture：`scripts/6a65-cartesian-channel-block-publisher-fixture.py`，7895 字节，SHA-256 `a78996abc97af415641bca83e991040edeb87bdc73e34f3c199cf96852614c0c`。实际命令：

```bash
python scripts/6a65-cartesian-channel-block-publisher-fixture.py --directory /tmp/channel-block-publisher-fixture
```

本次真实自然 exit 0，内部 .6069802860001801 秒；报告 SHA-256 `36540a74542d517aa460a9be219e49491695ecec3fa4e0ba7f41c60cd623a496`。它实际制造竞争本地 push、真实 NFF/HANDOFF 冲突，再注入同文 duplicate upstream，最终正常 pull/rebase/push；新的 pull SHA 写入 H，只剩一条自身回执，root 其它文字保留，工作树干净。另一次真实 README 变化在发布未审回执后停止 numerical continuation。四次实际 pull 都有记录，permission/network 不误归 NFF。它没有访问公有 main、没有实际源或科学接受。

新 v5 数值求解和新的 run 必须用自己的实际 source/cache、完整非零续态和新回执；不能借本结束 runner 的 raw。原 v4 receiver 只允许同一 frozen entry/source/recipe 的继续或 release，故不能通过其后继包暗换 v5。
