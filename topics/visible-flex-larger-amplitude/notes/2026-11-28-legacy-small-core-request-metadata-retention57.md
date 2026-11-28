# 第57批：13份旧小核心运行请求校验包装的完整保全

日期：2026-11-28 UTC。作者：ChatGPT / construction。类型：纯文本来源、参数与字节存储整理；不是科学计算、数值复验或新数学结论。

## 1. 本批只处理什么

本批列出13份既有 `request<N>-input-and-source-identity.json`，原文共 **452401 B**。它们由各次原 workflow 在实际科学调用之前写出，内容是完整原请求、请求原字节 SHA256、实际源版本、逐来源字节核验记录、四项既有数学输入，以及请求已有的父候选声明。它们没有保存该次调用新生成的场、数组、状态或检查点。

原请求中确有先前科学运行的参数、失败说明和数值动机。这里不因为它们处在请求包装里就删去这些字段：全部原嵌套对象，包括 request99 的 `saved97_motivation`、原3×3记录、源闭包、实际参数、原停止原因及 publisher 错误，都完整保存在两份参数文件中。没有用短摘要替代完整原请求。

**不删除**原 request/config/spec、13份 `exact-diagnostic-command.json`、任何科学源码、workflow、证明、现存科学输入或数值报告/检查点。也不删除独立 request81 的包装及其 `parent78-original/request78-input-and-source-identity.json` 逐字副本。新 run22 全部源、参数和活输入明确不在本批内。ports、Nelder、canonical/parent91和先前已退对象均不扩大范围。

固定原字恢复提交：

```text
f81da9c60b476c341fc235f64744832cb131a7b1
```

最后一次只读 main 引用观察为 `16e9ac17b1b34e5d83f30537e505ce4a6eb7f820`；这不是发布或删除声明。root 在普通提交时仍只按台账所列 path/blob/bytes 匹配这13条。

## 2. 完整参数如何保留

[shared-fields](../computations/legacy-small-core-request-metadata-retention-57-shared-fields.json) 保存完全相同的顶层字段、完全相同的 request 字段及73份完整来源记录。参数A对应原 resonance / damped-search / damped-resume 入口；参数B对应原 p3-inner / inexact-restoration / 独立 eta0.01 入口。两组按真实算法来源划分，不是把某个大数值文件切块。

- [完整参数A](../computations/legacy-small-core-request-metadata-retention-57-parameters-a.json)：75、77、78、80、82、85、87、90。
- [完整参数B](../computations/legacy-small-core-request-metadata-retention-57-parameters-b.json)：92、93、96、97、99。
- [完整来源、输入恢复与删除台账](../computations/legacy-small-core-request-metadata-retention-57-provenance.json)：每件原 file record、原 workflow、原请求、保留的整命令、全部73来源及15个原输入/父status恢复身份、实际结论和旧读者合同。

重组每条时：公共 request 字段并入该行全部剩余 request 字段，再用该行有序来源索引恢复完整 `source_sha256`；按保存的原 request 键序排列。公共顶层字段并入该行全部剩余字段，加入 request 和同序 `verified_sources`；仅对原来逐对象相等的 `verified_prior_candidate` 采用指向 request 的明确别名，再按原顶层键序排列。所有其他嵌套字段原样保留。13条完整JSON对象已与读回的原包装逐字段对应。

这个整理只保存已有字面信息；没有导入科学模块、计算方程/范数/J/根/区间，也没有本地科学 replay、AST、fixture 或 benchmark。该对象对应不是新的运行前门。归并后的JSON排版不是原文件字节，**不能拿新序列化冒原 whole SHA**；原字节读者仍用原 Git 对象或明确的逐字副本。

13份原请求在各自触发 commit 下另行完整读取，其 SHA 与包装 `request_sha256` 一致，其整个 request 对象与包装一致。请求 SHA、包装 SHA和新目录文件 SHA分别记录，未混用。所有原 argv 数值、运行时版本、45/60分钟资源、原四输入、父候选、73来源、完整 scope、proofs、direction_model 和失败说明都保留。

## 3. 实际写入与消费边界

13份原 workflow 均从真实触发 commit 完整取得。精确写入语句逐条存于台账；其顺序是：读原 request，核全部来源及四输入，若声明父状态则核并保父状态，然后写本批包装，之后才建立原科学 argv 并执行。每份自身 workflow 中对应包装 basename 只出现于该写入语句一次。这是这13份已读 source 的具体事实，不扩称任何历史脚本都不会读它们。

原科学调用分别来自完整保留的：

```text
geometry_20261114_small_core_resonance.py
geometry_20261115_small_core_damped_search.py
geometry_20261115_small_core_damped_resume.py
geometry_20261115_small_core_p3_inner_root_search.py
geometry_20261115_small_core_inexact_p3_restoration.py
geometry_20261115_small_core_inexact_p3_eta_0p01.py
```

这些入口读取原四数学输入及适用的原 parent-status；13份原实际命令文件全部留在当前树。请求包装中的 `scientific_execution_claimed=false` 只说明写包装时尚未科学调用，不能据此改写后来实际完成的科学过程。

原发布器 `root_20261114_publish_actions.py` 的 `main` 遍历原输出、记录 bytes/SHA并复制小文件。该行政发布动作不把校验包装变成科学状态。原原件恢复器 `exact_20261114_public_resume.py::prepare_public_source` 仍按 `source-dependencies.json` 恢复实际78份公开数值源码，原91清单及其12份其他题目Markdown、一个未消费旧client的明确排除语义保留；本批不冒完整91执行或恢复。

73个来源记录全保其原 bytes/SHA。其准确历史 Git 对象及大小在相应触发 commit 由树元数据取得；台账明确哪些小source正文此次真读，哪些 SHA来自原实际校验记录。没有把 metadata stat 冒全source数学审查。

## 4. request78 是真实旧读者输入

原 high-core two-end workflow 确实消费 request78 包装；`exact_20261115_r259_high_core_two_end.py::bind_inputs` 先核原 whole SHA，再读完整 source_commit、request、全部 verified_sources 和 verified_original_inputs。它另读真正 status、circle、scalar；这些科学输入绝不是包装可以替代的。

因此这里没有“无人读取所以可丢”的论证。原包装：

```text
28516 B
SHA256 57a5d443b0f13193a385a40a13c5dc038dae768e97095074e08a6edca5fc5b58
Git blob 2505b117be8b0b85615ceac0cdc60ec45941d216
```

其当前逐字副本仍保留：

```text
notes/public-actions-43664236768-1-smallcoreresonance/parent78-original/request78-input-and-source-identity.json
```

旧 reader 使用原预期路径时，可以从该副本复制原字节，或从固定恢复提交取回原 path。台账记录了旧 workflow、完整 reader及所需原父四件；不将归并JSON替代其 byte guard，也不改任何旧 reader。

## 5. 输入与实际结论不被改写

不少旧 accepted/prepared/status 早在本批之前已不在当前树。本批不声称它们仍在树中，也不对它们作删除。15条准确恢复记录使用各次真实触发 commit 下的原 path/blob/bytes，保留原请求给出的 whole SHA；它们都只作树元数据查询，没有打开大文件或二进制。

先试查的统一旧镜像 `60321451…` 并不含全部这些后来输入，所以**未把它当成统一恢复提交**。最终台账逐项使用真实 source commit；四个原输入取75触发版本，后续 parent-status取其真实消费版本。artifact编号/ZIP SHA等原请求字段仍保，不保证已经过期的下载URL可用，也不以新计算替代旧原字节。

下表只概括已刊原结论，完整 note 的实际 whole record 与路径都在台账，原 note 不删不改。没有从 `scientific_execution_claimed=false` 或 workflow success 推出科学结论。

| 原请求 | 原 run | 本批包装B | 已刊实际结论 |
|---:|---:|---:|---|
| 75 | 43660412919 | 24908 | The original zero-control diagnostic completed. The three unit resonance conditions and full112 low-residual candidate condition were not met; no nonzero BVP, high-mode nonresonance or full goal was established. |
| 77 | 43661078498 | 25765 | One Newton step was accepted; the second direction exhausted the twelve permitted trials. The diagnostic completed with scientific success false; no replacement of failed trials by a new acceptance claim. |
| 78 | 43662193286 | 28516 | Eight Newton updates were accepted at alpha=2^-17, with all144 actual trials preserved by the original records. The low-three root and full BVP remained unresolved. |
| 80 | 43664043053 | 31797 | Eight original column-scaled LM candidate directions accepted at full alpha=1. This was candidate descent, not a low-three resonance root or nonzero native/BVP acceptance. |
| 82 | 43665944742 | 33404 | Eight full steps accepted with eta=0.1; diagnostic completed, scientific success false. Initial/final finite evaluations are the original run's own records. |
| 85 | 43667636063 | 34364 | Eight full candidate steps completed, but the later publisher failed the HANDOFF size/rule-read requirement. Scientific computation and artifact preservation succeeded; the publishing failure and subsequent recovery remain separate. |
| 87 | 43669359806 | 35910 | Eight full steps accepted, all workflow steps succeeded, but low-three resonance and full BVP remained unresolved. Merit descent does not assert each component improved. |
| 90 | 43670368504 | 35574 | Eight directions accepted after48 actual trials and40 rejections; smaller eta=0.01 did not eliminate backtracking and the third unit defect grew. No low-three root or full BVP acceptance. |
| 92 | 43672921972 | 37214 | An initial p3 projection and two outer updates were accepted. The third direction exhausted20 backtracks because the old algorithm's inner-root eligibility condition was not met; lower saved merits were not falsely counted as accepted. |
| 93 | 43674264245 | 36295 | Eight inexact-restoration directions accepted; the explicit outer budget ended. Actual nonzero third residual and complete current Jacobian were retained; scientific success and unit/full112 candidate flags remained false. |
| 96 | 43675493266 | 36706 | Eight alpha=1 outer steps accepted and the explicit direction budget completed. Actual unit stopping and full112 candidate conditions remained false. |
| 97 | 43676647334 | 36681 | Eight alpha=1 outer steps accepted, stopped on the explicit budget; not a line-search failure. Current derivatives/merit were actual evaluations, and scientific success remained false. |
| 99 | 43677789194 | 55267 | Eight eta=0.01 restoration directions accepted after45 outer trials/37 rejections; explicit budget stop, no scientific success, no native nonlinear BVP or high-mode proof. |

所有这13次都没有因此成为原大幅度目标的解。75的默认诊断、77及92的具体停止、85的发布层失败、后续原预算结束和各自未付的低三/高模/BVP责任均保留。新 run22 的科学状态不由本批旧材料推断。

## 6. 恢复与实施

台账的 `delete_entries` 是唯一允许root据以删除的13条完整路径；不以通配符扩展。每条都含固定 Git blob、原大小及此次完整小文本读取取得的 SHA256。取回原字节可用：

```text
git show f81da9c60b476c341fc235f64744832cb131a7b1:<完整path>
```

原源、请求或数学输入有自己的准确历史恢复提交；不能把包装恢复提交套用于所有旧原始输入。实际科学重跑使用保留的原完整 argv/source/input，但本次不要求也不执行这种重跑。

本批全部新增文件均小于100000 B；这里只保护未引用远端 Git blobs，没有改refs、队列、活进程或科学源。完整新文件字节总量和净释放量以[总表](../computations/legacy-small-core-request-metadata-retention-57-complete-delivery.json)为准。后续若有另一组合规行政元数据，会独立给出完整条目；本批不借容量目标延伸到数值数据。
