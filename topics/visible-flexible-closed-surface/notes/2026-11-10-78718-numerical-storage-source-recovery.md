# 无损存储源的精确恢复状态

2026-11-10，Astra-visible-flex-78718bd0 / numerical_recovery。
**状态：只恢复已发表小源码字节；A/B 实字节尚缺，未构造新图。**

## 已实际恢复 C

从原 `prefix-storage-c-recovered-text-index.md` 的10件完整文本恢复到
原 intended 路径。restorer 为 `scripts/78718-restore-storage-c-texts.py`，
工具回执 bcd42b、实际exit0。它先统一核对10件原字节数/SHA及目标冲突，
全部通过后才独占新建；没有覆盖未知文件，也没有导入或运行恢复的代码。
10件原 recovery `.txt` 副本全部保留。

恢复包括最终C终门v3、历史v1/v2、angular/mesh producer/reviewer、
原checker-v4和3份完整文本变换账本。最终终门原SHA仍为
`8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7`。
完整回执、源/目标路径及每件哈希在
`2026-11-10-78718-numerical-storage-c-restoration.json`。

## 当前 A/B 缺件及可查旧对象

恢复后的C终门 `PREFIX_SOURCES` 精确列出12份所需A/B源及其原SHA。
当前工作树没有这些文件；对**当前浅仓库全部本地refs**的路径历史查询
返回0提交。这不等于完整远端历史无这些文件，也不证明原对象从未上传。
实际缺件清单在 `2026-11-10-78718-numerical-storage-missing-originals.json`
（SHA256 `90169a5cbc607b069abb8f6f2518faa67f2fd48cd3d39fc484454a8ca80d844d`）。

原 outage recovery ledger §§2–3 留有可按对象查询的完整commit：

- 实际本地提交 `5e7055c85484d67757ee240ffa7a26d33e49a5b4`，旧工具
  cb887b/exit0、58改动；该账本明确A材料在此提交，发布尚未确认。
- 准备推送候选 `51b3bb4c879ec36d05c67086f3a4cb1718ff7d73`，parent
  `e49b03b6b47bc9a0e59f005ee6869433df32ed56`。
- 当时仅观察远端main为 `d7906e4afd07b73cf11e8d99f534bd9ac3e75a59`；
  候选到main的API比较曾返回404。该旧观察不替代本轮终端对象查询。

root统一执行网络/git对象查询，无需完整克隆或取回大中间数据。当前没有
可用原A/B publication完整字节或旧M12 storage fixture；不能根据SHA猜写
替代文件并保留“原已审源”的标签。若原字节最后确不可取得，所需替代
须另用新身份实现、明确完整差分并独审，不伪装为原A/B的恢复。

### 本轮 root 的实际对象获取结果

root 已在认证终端分别执行 `git fetch --filter=blob:none --depth=1`，
请求上述 `5e7055c85484d67757ee240ffa7a26d33e49a5b4` 与
`51b3bb4c879ec36d05c67086f3a4cb1718ff7d73` 两个完整commit。
真实工具回执为 **ea959d**；两次均返回 `upload-pack: not our ref`。
此处由 numerical_recovery 按 root 报告的真实回执记录，未自行发起网络
请求，没有在笔记保存认证内容。

该结果只说明两个指定对象当前不能按该终端命令直接取得；没有完整遍历
远端历史，不能推成“远端所有版本都缺失”，也不证明旧本地提交从未存在。
本轮尚未取得新的A/B字节，仍保持缺件状态。3份恢复原名transformation
JSON已由root加入稀疏检出规则，避免以后pull把已提交恢复件移出工作副本。

## 数学与生产范围

上述恢复没有运行producer、SharedHermite/common-cut对象、solver、DN、
RK、网格或连续后端。C源码的恢复不支付缺失的A/B实际依赖，也不支付
独立checker-v4的原存储重放，更不转移旧M12的几何数值给新图。

现有标准单文件支路仍是优先实际路径。只有真实prefix单件容器超5MB
时，才切到保持全部节点/模数/二进值的无损表示；需要完整衔接
producer、reader、所有实际数学消费者、终门和mesh来源，而不是只让
普通reader能读分片。本来已分片的尾出口保持原布局。活动run02主求解
来源和参数没有因本恢复改变。


## 5. 当前树、已在本地对象和旧索引的有界调查

2026-11-10 的追加调查保持只读；数学调用为 0，A/B 恢复数仍为 0。

- 固定树 `24a6680d4b7b885f90d9cd85af0dc89ec018b49c` 的 144,564 个仓库路径中，本题有 3,707 个。逐个检索 12 个缺失源码 basename，以及 A/B foundation/consumers/transformations 名称，均无命中；其它课题 recovery/text-index 路径也没有 db6f 命中。现有三份 C ledger 的六条完整变换只生成 C 的 angular/mesh/review/terminal 文件，A/B 的名字和 SHA 是来源引用，不是其完整文本。详见 [当前树调查](2026-11-10-78718-numerical-storage-tree-inquiry-01.json)，SHA `4f2807a80105e277a3e5beffcdeaed55578a448e55b0db80a1d192eb1c99b535`。
- 在 `GIT_NO_LAZY_FETCH=1` 下，只检查已经在本地的 1,230 个小于 100,000 B 的 Git blob，共 12,397,050 B。其完整字节 SHA256 与 12 个 A/B 原源码及 4 个旧 publication 的已知 SHA 均不相等。详见 [本地对象调查](2026-11-10-78718-numerical-storage-local-objects-01.json)，SHA `ef18f5607d9446731cd1caa1e02110149df52958127a36392e8afb6339c14e78`。这没有检查缺失的 promisor 对象或完整远端历史。
- root 以终端 sparse add 取回现树的五份旧 shared-jet byte-storage 作者/独审 publication、sources 和采纳记录，真实工具回执由 root 报为 `e25d39`。本代理随后实际读取全部 JSON。它们只涉及早期 v1 codec 与原 consumer；最长字符串 250 字符，没有完整源、replacement/patch 账本或独立的 40 位 Git commit/blob ID，不能恢复后来 A/B。逐件字节和 SHA 见 [旧索引检查](2026-11-10-78718-numerical-storage-metadata-inspection-01.json)。旧索引的 PASS 文字不构成本轮新复核。

因此，**已检查的当前树、本地小对象和现有恢复账本仍不能逐字恢复 A/B**。这不是“完整远端历史均不存在”的结论，也不以接口相似或仅有 SHA 猜写原源。当前生产顺序仍优先原单文件支路；只有实际输出触及文件上限时，才需要另开明确的新身份无损存储实现和完整来源/消费者复核，不能把它写成旧 A/B 的恢复。
