# 独立24-query完成原件读取器

分类：公开Actions既有产物的只读运输、原标量摘录及字节审计。  
作者：ChatGPT（amplitude，AI辅助）。日期：2026-11-15 UTC。

## 1. 独立适配与冻结身份

本入口只读取已经完成的24-query原件，不运行新的数学计算。原23
读取器不改；当前副本仅严格更新producer schema、四源pin、16LEFT
加8MID的typed行序、49152行维数及新增left-RMS485的范围说明。
运输、原报告摘录、父场绑定、错误保全及其他33个函数的AST均相同。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `root_20261114_read_completed_twenty_four_prefix.py` | 50285 | `1aa4da4e721aa12a9f4d6257e3a6b6a7b328059de217ba42268d73a018e9828c` |
| `root_20261114_read_completed_twenty_four_prefix.py.diff` | 8166 | `999fb3421dc2c5889a95cd68ddcfb44951dcb09f1dfb7b2d5f553b408afd6672` |
| `twenty-four-completed-reader-static-check.json` | 3151 | `b7a2f0d2c6b298d5fed982c5aff15dc11785218aec5d913dc233758f0dfd1c1b` |

交付目录为`/tmp/visible-larger-twenty-four-readback/`。完整diff相对
冻结`root_20261114_read_completed_twenty_three_prefix.py`，50265B，SHA
`528e5024d875a476fb5761db9d4adb6991d6e252d010117e273c1f35b93eba60`。
仅`audit_domain`函数的严格当前typed验证发生变化；其余33个函数
AST不变。语法、四源SHA及整数布局静态核过；未导入科学模块、构造
数值fixture或执行本读取器。

四个当前源精确pin为：

- domain：`06933e9341664d63b5a9eaeb00998daa1be7b1c1d143a60f1ae2ef05efa9db36`；
- warm：`b453b53d4ae759e0bc50d5d789beb04e53c18903adaf427c2a28c0382827d452`；
- FD：`87261854684d5844c97d59b328db2aa070b015b565baf46dfb7e811808b3bb87`；
- collocation observer：`f6639751ea97bd857ad05ad0a36d38d11024dac25f6ecc0610fef2d9fe90cf35`。

原计算合同见[24-query接口](2026-11-14-twenty-four-query-condensed-interface.md)。
本读取器不会改这些计算源、其门槛或保存的科学结果。

## 2. 真实身份、完整运输与父场

本入口只允许在`Rogerhu12/math-research-public`的公开Actions运行。
实际run/artifact/source/ZIP大小及SHA均为必需参数；代码没有预填
尚未发生的run或artifact身份。父pair也必须显式传入并严格绑定原件。

运输调用原`exact_20261114_fetch_pinned_public_artifact.py`，精确SHA
`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
完整artifact metadata、ZIP大小/SHA、所有成员安全路径/CRC/size/hash
检查路径不变。解包根是`--download-out`本身，没有隐含的`files/`
或`artifact/`层。实际source另与GitHub artifact中
`workflow_run.head_sha`绑定。

依赖仅原Python标准库和NumPy。NumPy只用于已有NPZ/NPY的解码、
dtype/shape、原字节序列化和SHA核验；不执行RHS、J、ODE、边界、
矩阵动作、范数、内积、QR、QP或FD。运输成功不冒作计算接受。

首次24计算的父场是实际74：

| 父原件 | 原字节SHA256 |
|---|---|
| `warm-001.json.gz` | `204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3` |
| 解码后原`driver-status.json` | `09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73` |

原status透明gzip恢复后按原字节核验，不能重序列化JSON来替代原SHA。
后续own24完成场仍须实际显式新父pair，读者不放宽原producer验证。

## 3. 当前typed行与完整字节范围

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485)
MID  = (473,475,477,480,481,482,484,485)
```

16个left-RMS及8个原中点，每组2048物理角，总B为49152×236036，
完整local B为49152×7101。left分数为`0.17267316464601146`，mid为0.5。
新增left485为query15；所有mid索引从16开始。mid485独立保留为query23。
每个manifest block、query、Gamma/Pi及NPZ分块都核当前
`query_index/kind/interval/fraction/station`和完整global/local列身份。
旧23的行号不能冒作新24的mid语义，旧父23字段仍完整保留。

实际与声明local列均为nodes466至486的21个338维物理节点及3个control，
共7101列；zero-layout为空。新增left485复用既存endpoint485/486，
不扩大捕获支持。读取器核原保存整数映射和完整字节，不重算任何B行，
也不因更早历史曾有zero484而删除历史记录。

读取范围包括所有domain NPZ/NPY、各B/Gamma/Pi及完整beta拼接SHA；
原base/mesh/y/RHS/S；原mid输入和原端点J/P；全部condensed引用数组
和分块；局部root/affine/recovery原raw文件；原midpoint及collocation
observer描述器；当前四源及实际checkout内存在的全部历史源。
四当前源缺失会报身份错误；其他历史源若不在checkout，只记录原
producer声明并明确未独立核文件，不伪报已验证。

完整chain QR因子未被原producer导出时，报告保持
`full_factor_files_independently_audited=False`。原Actions打印的
residual、dot/complex和FD读数只复制，不重新执行；字节核验不将其
变成严格浮点包络或新科学验收门。

## 4. 精确CLI与原数值优先保全

真实计算完成后以其实际元数据填入下列必需变量；不得以候选或猜测
run/artifact值调度：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261114_read_completed_twenty_four_prefix.py" \
  --request-number "$ACTUAL_REQUEST" --run-id "$ACTUAL_RUN" \
  --artifact-id "$ACTUAL_ARTIFACT" --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" --expected-sha256 "$ACTUAL_ZIP_SHA256" \
  --source-commit "$ACTUAL_SOURCE_COMMIT" \
  --parent-directory parent74 \
  --parent-warm-sha256 204b208393218923f8abf9a36b6f03d29306409155447f561b2c2f4c373001a3 \
  --parent-status-sha256 09d944723fb6be152e90ba283fc44d33d455f1a52bc73787a329fcdc7d97ea73 \
  --download-out "$RUNNER_TEMP/original-completed-prefix" \
  --out "$VISIBLE_OUT/request-readback" --repository-root "$GITHUB_WORKSPACE"
```

输入要求真实首attempt原artifact名称
`visible-followup-condensedqp-<actual-run>-1`；当前warm目录
`twenty-four-condensed-warm`，producer schema严格为
`exact-constraint-twenty-four-query-condensed-complete-H-warm-v1`。

读取顺序先保存原status/model/全部trials/FD/候选报告副本和必要小摘要，
再进行byte审计。输出`completed-prefix-readback.json`、trial-table、
FD/QP小报告及`large-arrays/`内完整原件和审计。不重新计算merit、
下降比、域、范数或最大物理残差。

若主summary超过90000B，完整原件仍留artifact，主summary省略大型
accepted/nearest/FD子树并明确引用。不能只凭文件名认定trial-table
小于100KB；取件前检查真实size。大报告不通过小文本connector整取
或机械拆块搬运。任何读取/byte审计异常都保具体`repr`、traceback及
此前已提取的原报告，不能因附加读取错误抹除原科学结果。

实际文件数、数组数、已核源码数和所有PASS必须由本读取器真实运行
后填写，本稿不预言未来成功。原24求解无需等待该独立读者才继续。
