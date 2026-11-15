# 独立23-query完成原件读取器

分类：公开Actions既有产物的只读运输、标量摘录与字节审计接口。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC。

## 1. 唯一变化与冻结身份

本入口供真实完成的23-query计算原件使用，不运行新的数学计算。它在
冻结22读取器基础上保留完整运输、父场/producer绑定、原报告提取和
逐文件/数组字节核验，仅严格适配当前23-schema、四源pin、typed行序、
47104行维数和新增原collocation midpoint484的说明。原22读取器不改。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `root_20261114_read_completed_twenty_three_prefix.py` | 50265 | `528e5024d875a476fb5761db9d4adb6991d6e252d010117e273c1f35b93eba60` |
| `root_20261114_read_completed_twenty_three_prefix.py.diff` | 7862 | `21945be1e4fa3f347cd703bc72ee6b8c69bade349f99ebd1da537707474dc037` |
| `twenty-three-completed-reader-static-check.json` | 3146 | `03beb3808d3d571cd768ffc9b1904c6e23cf2fa050f963b592f911050681be5f` |

文件目录为`/tmp/visible-larger-twenty-three-readback/`。完整diff相对
`root_20261114_read_completed_twenty_two_prefix.py`，后者49975B、SHA
`f3a3570daaac6909f22990abddd70faab9677be6f77a3a2c37dd3c17a08668db`。
33个非`audit_domain`函数的AST逐项相同；`audit_domain`仅更新所核
typed集合、行数和当前范围说明。语法编译、原源SHA、四新pin和整数
布局检查通过，没有导入科学模块、构造数值fixture或执行读取器。

当前四科学源精确pin为：

- domain：`755d9bf2a01c5c417b28bfd265ee76712bba54a9fdeddf34ea56c4668abefe98`；
- warm：`1fe5b698e452112583ee82a81ab7890095c7f3f31de05cdfb60c79e35039721c`；
- FD：`1eb07544b30abdce43599d3297c5f7732c3d19f4c74bf5aedd15ae008fa87e8a`；
- collocation observer：`06ed3a98c48cbb2feffbc319f08c6509012f5ab9f7a460a5af3d6f74e73fc697`。

这些源的完整名称和计算契约见
[23-query实现接口](2026-11-14-twenty-three-query-condensed-interface.md)。

## 2. 严格输入及运输

入口只允许在`Rogerhu12/math-research-public`的GitHub Actions运行。
全部真实run/artifact/source/父warm/status身份仍为必需CLI参数；本稿
没有预填尚未发生的run、artifact、ZIP大小或digest。默认值也不猜测。

运输复用原`exact_20261114_fetch_pinned_public_artifact.py`，SHA
`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
原完整metadata、ZIP SHA/size、成员安全路径与CRC/size/hash路径不改；
解包根仍是`--download-out`本身，不假定额外`files/`或`artifact/`层。
源commit额外绑定到实际GitHub artifact的`workflow_run.head_sha`。

依赖保持Python标准库和NumPy；NumPy仅用于已有NPZ/NPY的dtype、shape、
内存次序、原字节转换和SHA核验，以及已验证整数索引的序列化。没有
RHS、Jacobian、ODE、边界、矩阵动作、范数、内积、QR、QP或FD调用。
不下载新的科学数据来替代原件，不把运输成功冒作计算接受。

首次23计算的真实父场为72：warm
`f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213`，
原JSON status
`73a0c0148f6166608ce47ecd4831b6e09a013e50907bfe7aae7468b687ce857f`。
后续own-schema实际计算仍须显式传入其真实父pair，读取器不放宽验证。
原JSON和透明gzip均按解码后原字节验证，不重序列化后代替原文件SHA。

## 3. 当前typed B与字节审计范围

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482,484)
MID  = (473,475,477,480,481,482,484,485)
```

15个left-RMS及8个原中点，每组2048角，总B为47104×236036；完整
local B为47104×7101。left分数`0.17267316464601146`，mid分数0.5。
新增mid484与原left484分别保留kind/query_index/fraction，mid485
当前索引后移。每个manifest block、query、Gamma/Pi和NPZ分块都核
相同typed身份、站点、完整global/local列映射。

声明局部nodes466–486及3个control共7101列，实际B列并集同为7101；
所有声明列均实际使用，zero-layout为空。node484已在父22有真实B列，
本次新增中点不新增端点捕获。读取器核原整数映射及保存数组的完整
字节，既不据此重新计算B，也不因旧父历史曾有zero484而删除该历史。

完整审计依次保留：domain所有NPZ/NPY及B/Gamma/Pi/全beta拼接身份；
原base、mesh、状态、RHS及全局尺度；原mid输入和原端点J/P；condensed
完整数组/分块引用；局部root/affine/recovery的原raw文件；原中点和
collocation observer描述器；当前四源及实际checkout中存在的全部
历史源SHA。当前四源缺失会报身份错误；未出现在读取checkout中的
其他历史源码只能保留producer声明并单列，不能冒独立文件核验。

完整chain QR因子仍未由原producer导出时，报告明确
`full_factor_files_independently_audited=False`。原Actions打印的残差、
dot/complex检查等只复制已保存值，不在这里重新执行，不将浮点后验
变成严格认证，也不把字节检查增加为原科学接受门。

## 4. CLI、输出及错误保全

实际产物完成后使用其真实值调用；以下环境变量均须由实际元数据赋值：

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261114_read_completed_twenty_three_prefix.py" \
  --request-number "$ACTUAL_REQUEST" --run-id "$ACTUAL_RUN" \
  --artifact-id "$ACTUAL_ARTIFACT" --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" --expected-sha256 "$ACTUAL_ZIP_SHA256" \
  --source-commit "$ACTUAL_SOURCE_COMMIT" \
  --parent-directory parent72 \
  --parent-warm-sha256 f59e8c64399a9fed392a8f8c3976209aaa3fa662c5c6ea65d864342cca697213 \
  --parent-status-sha256 73a0c0148f6166608ce47ecd4831b6e09a013e50907bfe7aae7468b687ce857f \
  --download-out "$RUNNER_TEMP/original-completed-prefix" \
  --out "$VISIBLE_OUT/request-readback" --repository-root "$GITHUB_WORKSPACE"
```

必须是原first-attempt artifact名称
`visible-followup-condensedqp-<actual-run>-1`。输出当前目录为
`twenty-three-condensed-warm`，producer schema严格为
`exact-constraint-twenty-three-query-condensed-complete-H-warm-v1`。

先保存原status/model/完整trials/FD/候选报告副本及必要小摘要，再开始
字节审计。输出`completed-prefix-readback.json`、trial-table、FD和
QP小报告，完整原件与完整审计放`large-arrays/`供artifact保全。
摘要只摘既有字段，不重算merit、下降比、范数、域或物理残差。

摘要若超90000字节，完整status仍保在artifact，主summary省去大
accepted/nearest/FD子树并明确引用；不能据文件名认定trial-table一定
小于100KB，读取前核真实size。大原件不通过小文本connector整取或
机械拆块搬运。读数/byte审计失败保存具体异常`repr`及完整traceback，
保留此前已取得的原数值和原件，不重新归类原科学成功/失败。

源码只是适配已知23输出合同；实际文件数、数组数、已核源码数和全部
检查结果须由真实运行产生后填写。本稿不预言未来计算成功，也不延迟
23优化主线等候这份独立只读审计。
