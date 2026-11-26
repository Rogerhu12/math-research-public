# h487 同 job 重生到 M48 暖续的完整执行合同

本入口尚未执行或触发真实 M48 job。四个数学源及非零接口核已登记 R243；本批是保持同一原 g、物理范围和完整端迹的执行连接。先前 h487 实测 field 为 `cdcbbd53c4019d0b4df88043662c13c736b65429575e6276ac44bb482375aa12`，作为比较身份。

## 冻结文件

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `6a65-m12-h487-to-m48-angular-warm-cold-run.py` | 14186 | `c536819dc2647f19b2aae8e9ba4c6a702fb24acfe3ae4e78ede7a4a9d03ae7ce` |
| `6a65-m12-angular-warm-rules-supervisor.py` | 12226 | `338e0347d06d3dd90135c800b5a2790f34ce7d9c595de104516a7bae397ae5aa` |
| `6a65-m12-angular-warm-summary-publisher.py` | 15519 | `4f2803c5831d037bd8258ebcb0c4343f7c6b1e2b6bf718becf5cf8fdfcb18b09` |
| `6a65-m12-h487-angular-warm.yml` | 12879 | `654a36bf116261cf613915d80b040b3457105e3876be4f54760ad79e8cde8bd3` |
| `6a65-m12-h487-angular-warm.json` | 2197 | `bc51a29c90e96cc87da1ce92957f2772e49051b8f2ef2189ac1d800b2b2d1006` |

workflow 安装为 `.github/workflows/6a65-m12-h487-angular-warm.yml`；request 安装为 `topics/visible-flexible-closed-surface/ci-requests/6a65-m12-h487-angular-warm.json`。三个 Python 源安装到本题 scripts。R243 的四个数学源逐字沿用，fixture 为修正后的 SHA `6008812ae985de806a9f030bac158896ae2fcd5e591156136c7409f511850ef6`。

## 实际执行链

新 workflow 首先检查所有 shell 和 Python payload；冷入口再 compile 四个数学源及自身，执行明确的非零有限接口核。然后以原 80/64/depth12/M32/N384/G6/800LSMR/1Newton/block24 及原元190、176插点规则重生完整 h487，并实际执行其 R236 和三相位 STL。重生本身不算新的数学下降。

随后保持全部 487 径向元、精确 query recipe、原 g 与 Gauss 规则，仅升到 M48/N768；将同 job 的旧完整系数精确零填充作为暖初场。新 warm solve 的完整三行 Gram 目标、全列、全部内部自由接口、中央与真 cuff 两 jet、实际能量/峰值试步验收均保留；没有加入 lambda 正则。默认暖续 800 LSMR、1 Newton，dispatch 只能改变暖续求解预算，不能改基态重生参数。

保存暖初场和新场在 G8/N1536 的完整观察。两者分别执行双原始微窗和全部祖先观察点并集；新场重新执行 R226、全时间 reach/held/非全等传递，外层 supervisor 再实际执行新 R236 和完整三相位 STL。固定原源的 tail cache 和 C_X 报告只按 SHA 逐字复用，所有依赖新 W 的报告都重新计算。

历史 field SHA 只用于比较。若同 job 重生因浮点末位而产生不同 field 字节，记录该事实并继续消费自己的真实 field/grid/所有预算，不挪借旧证明、不仅因这个 SHA 差异阻断。原 g、源定义、径向节点和 query 在本次两层之间仍严格锁定。

## 发布与时限

新 workflow 的窄 push 路径只含自身与该 topic request；无 raw artifact、Release 或 Git raw。数值源在 RUNNER_TEMP 的冻结副本执行；独立发布工作树每 2700 秒 literal pull，立即检查两个 README 差异并记录实际 SHA 到独立 `6a65-m12-angular-warm-ci-rules` 行。有差异时停止数学进程组并 exit42，末端 publisher 同样拒绝绕过。job 上限 350 分钟；令牌仅来自 github.token 的进程环境，除已核原 blob 恢复子步骤外均从数值子进程移除。

严格执行根 README 第 15 条：完整报告、可重算证书、场、STL 与 Actions 输出都只留 RUNNER_TEMP / Actions logs，不再用多个 JSON 分件存回仓库。新增 `6a65-m12-angular-warm-summary-publisher.py` 只生成一个小 Markdown 实际结论，列明冻结源、参数、run、真正退出、基态/暖初场/新场身份、完整残差和正规残差、双微窗/祖先并集、连续几何/metric 的关键指标，以及完整输出 SHA；不复制完整 stage report、certificate 或 top rows。完整 `cold-receipt.json` 的哈希还绑定所有 raw 输入及输出；它本身不入库。

规则 supervisor 在首次 pull 之前设置本工作树持久 Git 作者身份，供 rebase --continue 使用；每次 literal pull 后立即看双 README 差异，写本 job 独立 marker 前检查 HANDOFF UTF-8 总大小不超过 10000 字节。若 README 改变，立即停止数值进程组，普通提交/推送记载“README changed; root application pending”的实际 SHA，然后 exit42。只有 H 的并发冲突保留 upstream 全文再补本 marker；空补丁用 rebase --skip。真实并发 ref 拒绝使用已发布 v5 的精确判定，权限/保护分支拒绝不进入无限并发循环。

末端 publisher 复用同一规则 monitor：先 literal pull / 差异检查 / 普通发布 H，再生成并普通提交唯一 Markdown。若该摘要推送遇 NFF，只在严格核实 HEAD、单 parent、唯一目标路径、own subject、无其它 tracked 修改、且该 commit 未记入 upstream 后，撤回这个本 job 唯一未发布摘要提交；完整输出及待发摘要已保 RUNNER_TEMP。随后立即再次 literal pull / 规则检查，再普通重发。故新规则出现时只会发布 H 的实际变化记录，不会把旧规则下的未发布数值摘要夹带过去；不改写已发布提交，不 force。

## 已执行的本地检查

新发布接线实际 YAML 解析、9 段 bash -n、5 段 Python AST、7 个新源 compile 均 exit0。R243 的四数学源逐字不变，非零 fixture 的既有实际 exit0 沿用，不为此次发布接线改动重跑数学。先前七分件格式预算已弃用，不是当前发布方案的证据。


没有运行新的原 M12 暖续，没有提前登记新非线性接受、machine/solver 收敛或 README 完成。实际结果由这个新 job 的完整输出决定。
