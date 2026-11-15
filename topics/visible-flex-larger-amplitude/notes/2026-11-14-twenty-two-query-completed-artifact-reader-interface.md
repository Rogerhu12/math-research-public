# 独立22-query已完成原件reader：45056行与完整7101列

分类：原报告读取及字节身份核查接口；不执行科学计算。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC。

## 1. 独立源与明确范围

新源`root_20261114_read_completed_twenty_two_prefix.py`为49975B，SHA256
`f3a3570daaac6909f22990abddd70faab9677be6f77a3a2c37dd3c17a08668db`。
它从已完成实际68读回的冻结21-reader独立派生，父源SHA
`0feeb16e350d06ed03abb93c8ff80dd6e9e10a2703d47135f3c36ee3c289ea3a`。
旧reader未改，新文件旁的`.diff`保留全部差异。

该入口只消费已经完成的22-query artifact。实际run/artifact/source必须
取真实完成回执逐项传入；本交付没有预填未来请求72的未知身份，也没有
新workflow或dispatch。先保存原status、全部trial摘录、最近拒绝、新
warm/FD和完整producer，再核原source、NPZ、raw字节。不会重跑科学run，
也不把读取层成功变成一个额外BVP接受门。

完整ZIP传输仍只调用冻结
`exact_20261114_fetch_pinned_public_artifact.py`，SHA
`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
原publicActions来源、run/source、size/SHA、成员CRC及路径安全合同保持。
实际payload根仍为`--download-out`本身。`main`仅允许本公开仓库Actions，
不导入任何科学源；NumPy只作原NPZ解码、dtype/shape、原字节转换与哈希。

## 2. 当前22-query专有身份

| 当前科学源 | SHA256 |
|---|---|
| `geometry_20261114_twenty_two_query_domain_operator.py` | `083abbf5e7f6dfede4f717d059192011e2ca4f895ff2f57e2d3760f49d06feb0` |
| `geometry_20261114_twenty_two_query_condensed_warm.py` | `2b01d4384f312a435b4e00feb9296c93a15aebe063a29fe9c588ac230aaf867a` |
| `geometry_20261114_twenty_two_query_condensed_response.py` | `08f8343b56b1f000ec2439b3d3d949260b26a3da5ad1dc6820788a1fd45be481` |
| `geometry_20261114_twenty_two_query_collocation_observer_warm.py` | `240837606d8b98214d25a6c0fe8b5546ce5b4994349bea39af32e96e22241ffa` |

原科学输出目录必须为`twenty-two-condensed-warm`，producer schema为
`exact-constraint-twenty-two-query-condensed-complete-H-warm-v1`。
完整B应为`45056×236036`，当前局部为`45056×7101`。行序为：

```text
LEFT = (466,467,468,469,470,471,472,473,475,477,479,480,481,482,484)
MID  = (473,475,477,480,481,482,485)
```

15个left-RMS后接7个midpoint，每组2048个原物理角。每个原block、query、
Gamma/Pi及全部分块必须保同一个`query_index/kind/interval/fraction/station`。
reader不会套用旧21的mid索引；B/Gamma/Pi完整组和所有beta分块均依当前
原typed顺序重组核SHA，不通过截数组满足传输尺寸限制。

实际22端点为完整nodes466–486，共21个节点，实际B block列并集7101
与R270声明连续局部7101相同。新增left484已使node484的338列成为真实
B列；当前`zero_layout_nodes=[]`，原零列identity对应空int64数组。
reader直接核保存的actual节点、整型global/local映射、完整并集及空零列
字节，并重建与producer同一完整模型metadata SHA。不会继续要求旧
6763并集或node484零块，更不会把mid484当作本轮新增查询。

这些是已保存索引和字节的核查，不调用B/BT/H，不重构或求解原H。父21
producer的历史zero484字段保持原值；仅当前22模型用新完整列并集合同。

## 3. 其他读回、字节及异常保全合同

所有其余原函数保持AST相同：

- 原status透明gzip解码及原JSON字节SHA，真实父warm双SHA、完整父producer、新warm/status/FD来源绑定。
- 原小trial/QP/FD观察先落盘；复制原完整报告到artifact，不用重复source树机械拼大摘要。
- 所有domain NPZ/NPY的文件和数组dtype/shape/byte SHA，整组B/Gamma/Pi和原base/scale/列布局。
- condensed完整数组引用与所有分块，不删basis或候选数组；14个root/affine/recovery原raw的完整size/shape/dtype/SHA。
- 原col observer返回flags/数组不变声明、带原descriptor的midpoint数组及原NaN bits。
- 原source清单；4个当前入口源必须存在且匹配，未在receipt checkout中的其他历史源明确记为未独立文件核，不冒已核。

完整QR因子仍可能只有原内存hash；没有实际导出因子payload时，reader
明确不声称做过独立因子文件审。所有数值均直接摘录，未运行新的RHS、J、
norm、dot、QR、QP、域、FD或native调用。原FD仍是保存warm上真零H全J
的affine检查，reader不能补造当前非零H的native验收。

读取或字节核失败时保真实stage、`repr(error)`及完整traceback；此前原
数值观察不删除，原science run的成功/失败不改写。完整derived报告总存
artifact；target报告较大时保专门trial/FD读数及artifact引用，不通过
connector分块转运完整大原报告。以上不是新的科学门。

## 4. 显式CLI及初始父场

新run/artifact实际完成后，由原回执提供所有`ACTUAL_*`变量：

```bash
python -u "$COMP/root_20261114_read_completed_twenty_two_prefix.py" \
  --request-number "$ACTUAL_REQUEST_NUMBER" \
  --run-id "$ACTUAL_SCIENCE_RUN" \
  --artifact-id "$ACTUAL_ARTIFACT_ID" \
  --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ARTIFACT_BYTES" \
  --expected-sha256 "$ACTUAL_ARTIFACT_SHA256" \
  --source-commit "$ACTUAL_SCIENCE_SOURCE" \
  --parent-directory parent68 \
  --parent-warm-sha256 3f45b939752cbe338ab5037a481ee2639b40783950ca4664d23c8ff168f4d535 \
  --parent-status-sha256 f4de267f1630201fb077b9d6245016760868f9a20a5b4624db08e780ce2f90e9 \
  --download-out "$RUNNER_TEMP/original-completed-prefix" \
  --out "$VISIBLE_OUT/completed-prefix-readback" \
  --repository-root "$GITHUB_WORKSPACE"
```

原first-attempt artifact命名必须为
`visible-followup-condensedqp-<actual-run>-1`。若未来own22续接，父目录
及双SHA都要传新的真实值，不能继续把parent68标签冒成新父场。
无需Node、native worker或数学准备；依赖为原transport标准库和NPZ解码
用NumPy，凭据只存在公开Actions运行环境。

## 5. 源码静态范围与输出

`twenty-two-completed-reader-static-check.json`为2711B，SHA
`d788ef68b2ba3b1719921d5bffa37435d082229495585d4c8f4a0305e97e8f85`。
它核了当前4pin、typed顺序、45056行、实际/声明完整7101及空零列。
除了`audit_domain`外，34个函数/类AST与冻结21reader相同，包括transport、
原标量摘录、source/condensed/raw/observer核、异常保全和main；全模块的
函数调用目标集合也相同。只有AST、文字、字节及整型索引核，没有运行
reader来造任何数值或伪造完成回执。

后续输出仍为`completed-prefix-readback.json`、独立trial/QP/FD小报告、
artifact中的`large-arrays/complete-original-byte-audit.json`及原报告副本。
这是实际完成后可执行的保全合同，不是新的研究结论，也不阻止第一批
真实科学原报告先行登记和后继有依据的数值推进。
