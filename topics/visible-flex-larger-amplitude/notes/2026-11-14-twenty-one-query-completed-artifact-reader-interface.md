# 独立21-query 已完成原件读回：typed行序与连续零列布局

分类：原件读取与字节身份核查接口；不执行科学计算。  
作者：ChatGPT（amplitude，AI 辅助）。  
日期：2026-11-14。

## 1. 独立源和用途

新源 `root_20261114_read_completed_twenty_one_prefix.py`，49785 B，SHA256
`0feeb16e350d06ed03abb93c8ff80dd6e9e10a2703d47135f3c36ee3c289ea3a`。
它由冻结20-query reader
`cf93537dadafa72cbe042a453cbe9a1cec0aca4cf1a25a0d979cca3cdb0b2f2f`
独立复制，旧源一字不改；旁边 `.diff` 给出全部差异。

它仅消费已经完成的21-query artifact，先保存原 status、全部 trial 摘录、
实际新 warm/FD身份及最近拒绝，再核原 producer/source/NPZ/raw bytes。
不重新执行已有科学 run，也没有给当前 BVP 增加新的接受门。尚未知的
实际68 run/artifact/source不写占位身份，未来必须由真实回执逐项传入。

源内 `main` 只允许在公开 `Rogerhu12/math-research-public` Actions 执行。
完整下载与安全取件仍复用冻结
`exact_20261114_fetch_pinned_public_artifact.py`，SHA
`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
网络、完整 ZIP size/SHA、每成员 CRC/路径安全和公开来源身份都没有另写
一套规则。没有通过connector分块搬运二进制或大原报告。

## 2. 21-query 特有的字节合同

本入口硬锁新的4个科学源：

| 文件 | SHA256 |
|---|---|
| `geometry_20261114_twenty_one_query_domain_operator.py` | `0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65` |
| `geometry_20261114_twenty_one_query_condensed_warm.py` | `b7956525ce484c4ed17724c2d84c04b6080688e2d0afc8367c5ba46cbf8626f2` |
| `geometry_20261114_twenty_one_query_condensed_response.py` | `d1da3a179bc05d346406961b81fc233e6edd098810bd6834537bc50d33901301` |
| `geometry_20261114_twenty_one_query_collocation_observer_warm.py` | `b99c6e4d40abaf426c189b241b718b8847562e92a7cdb90b6fdb31d6505587de` |

科学输出目录为 `twenty-one-condensed-warm`，producer schema为
`exact-constraint-twenty-one-query-condensed-complete-H-warm-v1`。
完整 B 必须为 `43008×236036`，声明局部为 `43008×7101`。
严格typed行序是14个left-RMS `(466,467,468,469,470,471,472,473,475,
477,479,480,481,482)`，之后7个midpoint `(473,475,477,480,481,482,485)`，
每组完整2048个物理角。不能套用20-query的旧query index。

每个 block、query、Gamma/Pi及其全部分块都核同一个
`query_index/kind/interval/fraction/station`。每组 B/Gamma/Pi 按原顺序
重组核完整SHA，再把所有组的原 beta分块按新typed顺序重组；不删高频项
或为了传输截数组。

实际query端点为466–483、485、486共20节点；声明连续局部为466–486加
3个control，共7101。实际B block列并集6763，唯一未使用的338列应恰为
node484。reader核保存的整型global/local列映射、实际并集及显式零列的
原byte identity，并重建producer使用的完整模型metadata SHA。

零B列只是布局身份，原H仍包含node484；此reader没有重构H或对B/BT/H
作动作，也不能据零列直接声称其方向数值为零。

## 3. 完整合同与失败保全

父warm、透明解压后的原status、整个父producer和新warm/status/FD仍按原
字节及结构严格绑定。新保存场的 FD 必须真正绑定新文件SHA及完整producer；
readback不把旧FD通过换标签。原FD本身保持真零H完整J的明确affine图，
当前非零H的native结果没有由reader补造。

核查范围保持原版：

- 每个domain NPZ和NPY的文件/成员CRC、dtype、shape和原字节SHA，以及完整B/Gamma/Pi/base/scale/列布局重组；
- condensed结果中每个原完整数组引用和所有实际分块，无basis截断；
- 14个root/affine/recovery原raw输出的完整size/dtype/shape/SHA；
- 原collocation observer保持返回flags/数组不变，以及每个有原描述器的midpoint NPZ，保NaN原bits；
- 原source清单；缺少于当前receipt checkout的非当前源只标明“保存的声明未独立文件核”，不伪装已核；4个当前入口源必须存在并匹配。

完整链QR factor未独立导出仍明确标记，原内存hash不能变成文件payload审计。
所有原数值直接摘录，NumPy只作NPZ解码、dtype/shape/原byte转换与哈希。
没有RHS、Jacobian、norm、dot、QR、优化、边界、域或尾调用。

原小观察在可选完整字节审计前就保存。若后续读取层抛错，保留具体
`repr(error)`及完整traceback原文件，标明真正失败stage；原科学run的
success/failure不因此改写。完整derived状态总存artifact，target报告超过
90KB时保原数值在专门trial/FD小读数和artifact中，而不因尺寸问题清空
已经获得的事实。

## 4. 显式 CLI

全部运行身份由完成后真实API回执提供，不能猜测：

```bash
python -u "$COMP/root_20261114_read_completed_twenty_one_prefix.py" \
  --request-number "$ACTUAL_REQUEST_NUMBER" \
  --run-id "$ACTUAL_SCIENCE_RUN" \
  --artifact-id "$ACTUAL_ARTIFACT_ID" \
  --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ARTIFACT_BYTES" \
  --expected-sha256 "$ACTUAL_ARTIFACT_SHA256" \
  --source-commit "$ACTUAL_SCIENCE_SOURCE" \
  --parent-directory parent66 \
  --parent-warm-sha256 80b4590f476cf782d63cbc1680a4c205713bf6a533e544472219b6fef85a3cf6 \
  --parent-status-sha256 04ace7953961b3905d2b72639976025dc9c4efd0bef7b932585cf21f8249bcd4 \
  --download-out "$RUNNER_TEMP/original-completed-prefix" \
  --out "$VISIBLE_OUT/completed-prefix-readback" \
  --repository-root "$GITHUB_WORKSPACE"
```

此模式保留原first-attempt artifact命名合同
`visible-followup-condensedqp-<actual-run>-1`。如果未来producer或实际
artifact属于另一套身份，应另行明确适配，不能改参数声称已有原字节匹配。
后续own21续接时父目录/双SHA同样必须传其实际值，不保留本初始parent66
标签冒作后续父场。

不需要准备数学源码树、Node或启动native。环境只需原transport所用的
标准库/公开Actions凭据和NPZ解码用NumPy；凭据始终只存在运行环境。

## 5. 静态范围

`twenty-one-reader-static-check.json`（1858 B，SHA
`380802bff2fb65fd6c86350058507c8d2508d9eeff5d034b8aff45df4a136313`）
核了当前4pin、schema、目录、行列及整型布局字面值。与20-reader相比，
所有函数除 `audit_domain` 外AST逐项相同，包括transport、原数值摘录、
source核、condensed/raw/observer审计及异常保全/main；没有执行此reader
或科学计算来造一个测试产物。

这是后续实际原件的可执行读取合同，不是新的科研结论，也不阻止68原计算
或其第一批真实数值回执先行登记。
