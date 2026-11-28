# 第 66 批：六份旧完整准备描述的来源及恢复

日期：2026-11-28。状态：完整记录已保护为未引用 blobs，主线实施由 root 另记。

## 1. 范围和实际身份

本批只处理六份旧 `-actual-three-control-adapter.json` 生成描述，毛大小合计 **732,004 字节**。每份大于等于 100,000 字节，因此本次没有整读其正文；六个 SHA-256 都取自已经完整读取的旧发布/恢复小清单，Git blob 和大小来自固定树元数据。没有通过猜文件名、截断内容或读取大 raw 补身份。

固定候选恢复提交为 `c5be3d5556d8a4f5d1200574567d30d764e4b72c`。六条原路径及完整三重身份见 `legacy-large-generated-adapters-retention-66-provenance.json` 和交付总表；发布只删除这六个路径，不顺带清理同前缀的其它数据。

| 原分支末段 | 字节 | 原运行事实 |
|---|---:|---|
| coarse-response-m32-full-entry-prepare-r1 | 119,048 | 完整原命令含 `--prepare-only`，实际退出 0 |
| native32-stale-warm-original-production-source-prepare-r1 | 131,814 | 完整原命令含 `--prepare-only`，实际退出 0 |
| q106-eager-hermite-production-prepare-r1 | 116,867 | 完整原命令含 `--prepare-only`，实际退出 0 |
| q126-m32-tail2-actual-r1 | 119,353 | 原完整科学进程退出 0；描述仍是它启动时生成的准备记录 |
| q126-m32-tail2-production-prepare-r1 | 119,441 | 完整原命令含 `--prepare-only`，实际退出 0 |
| stale-coarse-warm-production-prepare-r1 | 125,481 | 完整原命令含 `--prepare-only`，实际退出 0 |

这些是旧生成描述，不是本批删去 accepted raw、tail solution、warm checkpoint 或实际结果报告的许可。独立的配置、base-profile、plan、resource、ownership、发布清单和接受报告都原字保留。当前 19–27 运行及任何新源/参数都不在本批。

## 2. 实际 writer 说明了文件边界

已完整读取 `computations/strong_actual_three_control_bvp.py`。其 `main` 在第 261–286 行构造 `status='prepared-only'` 的 provenance；第 287–293 行把它写到 `out_prefix + '-actual-three-control-adapter.json'`，同时独立写 config 和 base-profile。已有文件若 JSON 值不同会拒绝覆盖。

原程序已有的 `--prepare-only` 分支在第 294–297 行立即返回。实际数值导入和完整求解分支在其后。因此本批对生成类型的判断来自真实写入位置和六条完整原命令，不来自 adapter 这个名字。

生成描述包含完整源 SHA、源代码替换、原参数、target、unknown counts、原节点数量、批次、tail I/O 和 warm/reuse 来源。它可能有科学含义，但不保存所引用 raw state 或 tail response 的完整数值正文。这些数值输入仍是另一套完整文件，来源表逐一保其固定恢复关系。

coarse-response 入口先从完整原输入构造初猜记录，再把该记录和完整 source transform 交给原 initial-laws/full-tangent/fresh-resource 包装链，最终由上述同一 writer 写描述。stale-coarse/native32 是明确额外来源变换；eager Hermite 是明确 first-warm 绑定。没有拿一个入口的源码替代另外三个入口。

## 3. 完整原源、全部参数和输入

新 source/input registry 保 **65 份完整小源码记录、40 份完整原配置/资源/结论文件记录和 35 份直接输入及伴随文件恢复记录**。65 个源码正文均已完整读取。原完整 plan 给出的 47 个不同源码、共 51 条原 hash 绑定与相应全字文件一致。其它实际 writer/reader 依赖也保存完整固定快照身份，没有把未找到的旧 hash 编造出来。

provenance 对六个 case 保留完整原 resource 对象，其中包括原 command 数组、实际开始/结束时刻、退出码、wait4、信号、资源、原 wrapper 身份和原进程记录。原 command 的顺序、十进制字面值、所有 cache/heap/node/tolerance/batch 参数和绝对路径均未删改。配置和 base-profile 的完整文件另以 whole identity 引用，且继续留树。

原准备和实际命令的区别照实保留：q126 实际命令不带 `--prepare-only`；不能为了叙述方便把它改成当时只作准备。该 actual 分支生成描述之后确实执行了其完整原科学程序，实际结论由独立接受清单给出。

以前已经退役的原输入，固定恢复提交是 `60321451c058c6a51da58c37ae5ec6f2d1145f74`。每个 direct input 给出其原 Git blob、大小和已有 SHA-256 证据。raw 索引所引用的伴随数组不能省掉；若要重新执行旧数值，须按完整历史 topic 树和原恢复记录恢复共享/嵌套数据，而不是仅取一个压缩索引。

本次没有读取或解压任何 gzip、NPZ、NumPy 数组、ZIP，亦未整读大于等于 100,000 字节的输入或候选输出。缺少独立 whole SHA 的原伴随文件保持 null，并保精确 Git 身份；本批六个候选输出本身均已有完整旧 SHA-256。

## 4. 六个 whole SHA-256 的真实出处

完整保留并引用以下原清单：

- coarse-response 的 `strong-coarse-response-m32-full-entry-preparation-manifest-r1.json`；
- native32 的 `strong-native32-stale-warm-preparation-manifest-r1.json`；
- Hermite 的 `strong-eager-hermite-input-preparation-manifest.json`；
- q126 准备的 `strong-q126-m32-tail2-production-launch-manifest-r1.json`；
- stale-coarse 的 `strong-stale-coarse-warm-preparation-manifest-r1.json`；
- q126 actual 的 `strong-q126-m32-accepted-recovery-manifest-r1.json`。

每个 SHA 的源清单 path/blob/size/whole SHA 也登记在 provenance。原 q126 launch 清单在当时尚未观察实际终态；后来的 accepted-recovery 清单则明确记原 owned exit 0、原 actual acceptance complete、完整 H 和原 full-J 身份。两个不同时间的记录均保留，不把后知的终态写回早先清单。

原 accepted-recovery 还明确 `infinite_closure_or_closed_held_or_reach_claim=false`，本批不改变它。stale 来源清单里尚未实际测试不同 g/不同 raw 网格的范围也照原保留。五个 prepare-only 的退出 0 不被当成新数值解或 runtime 性能改善。

## 5. 原字恢复与生成再现分开

任何需要旧描述的消费者可以从固定提交取回完整原字：

```sh
git -C REPOSITORY_ROOT show c5be3d5556d8a4f5d1200574567d30d764e4b72c:FULL_REPOSITORY_RELATIVE_PATH
```

原字节的 SHA-256、Git blob 和大小须按清单保持。该路线不需要原科学运行环境。

从原 producer 再生成描述则须恢复原完整 source、全部输入、cwd 和原命令参数，并使用原程序已有的准备停点。描述包含路径敏感字段；不同机器上若改了原绝对路径，就不能声称生成了同一字节流。完整科学重跑还有原外部 `--source-topic` 和运行状态责任，不能以同名较大文件冒充旧 4,752 字节 client。

本批没有执行任何生成命令，也没有执行科学、导入模型、AST、fixture、benchmark 或重新求解。完整原 resource 仍记录当时究竟有没有 `--prepare-only`。清理不是一次原科学重执行，也不要求为此另开 Actions 验证门。

## 6. 历史读取者不能漏掉这些文件

完整原 `strong_archive_accepted_fullflow_actual_v2.py` 会在接受恢复包中复制/哈希 actual-three-control 描述；其部分收集逻辑使用文件是否存在来选取成员。若要再次运行它，必须先恢复它请求的确切旧路径，不能让缺失文件静默跳过后仍宣称恢复包完整。

`archive_current_gap_release_warm.py` 也收录原 warm-adapter 描述。其它旧命令或 manifest 若引用这些路径，同样要先取回原字，不得用另一个 run 的文件代替。

相关 r3 first-request 诊断确实会读取 failed adapter；第 65 批已经保其完整字节恢复合同。本批没有再删它，也没有把“生成描述”概括成永远不被科学输入消费。第 65 批七个 canonical 和全部差分材料仍原样保留。

对六个具体文件名进行的来源搜索有五个返回已保的完整小 manifest；q126 actual 那次搜索工具限流，未把错误当成无消费者的证据。该分支的完整 archive 源和 accepted manifest 是直接读取的。本批不声称做过全仓库无引用证明。

## 7. 实施范围

本 agent 只保护完整小文件为未引用 Git blobs，没有写 ref、删文件或改队列。root 发布时只匹配并删除总表的六个 exact path/blob/size；其余源、配置、输入、数值文件、证明和实际结论保持原有存储与恢复义务。

精确新增字节和净容量见交付总表。本批不为凑数增加其它大结果、不碰已知 Nelder/ports 缺口、不读未知唯一原始数据。后续批次若扩大，必须另有完整来源和明确删除清单。
