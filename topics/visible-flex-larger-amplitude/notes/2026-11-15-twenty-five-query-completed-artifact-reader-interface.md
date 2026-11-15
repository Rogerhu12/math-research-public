# 独立25-query完成原件读取器

分类：已有公开Actions产物的运输、原标量摘录与字节审计；无新数学。  
作者：ChatGPT（amplitude，AI辅助）。日期：2026-11-15 UTC。

## 1. 冻结源及与24读者的差异

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `root_20261114_read_completed_twenty_five_prefix.py` | 50404 | `9239b31016fde72f55961bc33e36dd014d8cf051df8aaca1fb3f475f8494e8cb` |
| 同名`.py.diff` | 9818 | `cd6dcf9fea9bdf17256588085c898d8f9c9aa0ebf75301f7d10a21c9b4d0cde1` |
| `twenty-five-completed-reader-static-check.json` | 3246 | `70c12b5f30b1b23f434e5b2b4b6b80d78efd389e3fdd0bbd14ef70692130341a` |

目录`/tmp/visible-larger-twenty-five-readback/`。冻结24读者
`1aa4da4e721aa12a9f4d6257e3a6b6a7b328059de217ba42268d73a018e9828c`
保持不变。本副本只更新当前producer/schema、四源码pin、typed顺序
和实际完整支持。`audit_domain`做严格25布局验证，其他33函数AST
保持完全相同，包括完整运输、父场绑定、原结果优先保全、完整raw/
NPZ审计、具体异常保存。仅AST、整数索引、源码bytes校验；没有运行
读取器、导入科学模块、生成数值fixture或预填未来artifact身份。

四个实际计算源锁定：

```text
domain   55fe72b1bad9cf3ee26b1d29a1a6cefb7f0f62f2570d7703bb8f3dfcd01b2260
warm     5dbd5948f815a1fcf4eaf2a08f7d130407ce52c96b25240738d26c6476b48b0c
FD       8d55ce7f29520318db39de5dcdb0790cdce43452dc29085ec26cbfe042dfa75d
observer be6815071387c34fb25b4f064508af2ab65691bba4ff512d1fa999236a1f4d55
```

科学入口合同见[25-query接口](2026-11-15-twenty-five-query-condensed-interface.md)。

## 2. 完整原运输及实际父场

只允许在`Rogerhu12/math-research-public`公开Actions内运行。实际
run、sourcecommit、artifact ID/name/bytes/SHA及父pair全部由必需
CLI参数指定；不猜测尚未完成的run/artifact值。

完整运输仍调用原`exact_20261114_fetch_pinned_public_artifact.py`，
SHA`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
官方metadata/source绑定、完整ZIP大小/SHA、每成员路径/CRC/size/
hash及安全解压原样。实际payload根为`--download-out`本身。

首次25父为实际79原pair：

```text
warm SHA    565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504
status SHA  e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0
status gzip aea13404a1cd1109f207cbb2a6f3c46fb885518ab7e29c480ba332ea21d756b6
```

父status透明gzip只恢复原JSON字节，不重序列化。未来own25完成场
仍传显式真实新pair，读者不放宽schema/source/producer验证。

## 3. Typed布局与完整审计范围

```text
LEFT=(465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485)
MID=(473,475,477,480,481,482,484,485)
```

17LEFT后8MID，每组原2048角，总B为51200×236036，local B为
51200×7439。新增left465是query0，mid473从17开始。当前所有block、
query、Gamma/Pi、NPZ块的index/kind/interval/fraction/station和
global/local列身份均严格核。父24typed记录完整保留。

实际查询端点与声明连续布局均为465至486的22个338维物理节点加3
control，实际B列并集7439；zero-layout为空。新增端点465来自同一次
完整原A捕获；读者只验证保存的原数组和整数映射，不评价J/B或新增
捕获。远档mid487不是本模型查询。

审计包含所有domain NPZ/NPY和完整B/Gamma/Pi/beta拼接；原base
mesh/y/rhs/S、typed中点输入、原端点J/P；全部condensed数组引用和
分块；R270局部root/affine/recovery原raw；midpoint/collocation
observer描述器；当前四源及checkout中存在的历史源。历史源缺失
只明确保存原声明，不能冒独立核过；当前四源必须存在并匹配。

完整chain QR因子未导出时，继续明确没有独立完整因子文件审计。
原打印residual、complex、dot、FD只复制，不重新求值或变成严格
浮点包络。依赖仅Python标准库和NumPy，后者限NPZ解码、dtype/
shape、原bytes和SHA；不调用RHS/J/ODE/边界、范数、内积、QR/QP
或科学FD。

## 4. 原值优先保全与CLI

```bash
python -u "$VISIBLE_COMPUTATIONS/root_20261114_read_completed_twenty_five_prefix.py" \
  --request-number "$ACTUAL_REQUEST" --run-id "$ACTUAL_RUN" \
  --artifact-id "$ACTUAL_ARTIFACT" --artifact-name "$ACTUAL_ARTIFACT_NAME" \
  --expected-size "$ACTUAL_ZIP_BYTES" --expected-sha256 "$ACTUAL_ZIP_SHA256" \
  --source-commit "$ACTUAL_SOURCE_COMMIT" \
  --parent-directory parent79 \
  --parent-warm-sha256 565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504 \
  --parent-status-sha256 e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0 \
  --download-out "$RUNNER_TEMP/original-completed-prefix" \
  --out "$VISIBLE_OUT/request-readback" --repository-root "$GITHUB_WORKSPACE"
```

输入目录为真实首attempt`visible-followup-condensedqp-<run>-1`，
warm子目录`twenty-five-condensed-warm`，producer schema严格
`exact-constraint-twenty-five-query-condensed-complete-H-warm-v1`。

原status/model/全部trial/FD/候选副本和必要小摘要先写入，再做byte
审计。输出为`completed-prefix-readback.json`、trial/FD/QP摘要和
`large-arrays/`内完整原件/审计。真实size超过限额的摘要会明确指向
artifact完整原件，不因额外读取失败清空已获得的科学结果。所有
异常保具体repr/traceback；不能凭文件名假定其小于100KB。

大原报告只通过CLI或Actions，不能经小文本connector整取/机械切块。
实际文件数、数组数、已核源码数和PASS都等本读者真正执行后报告。
该只读回执不是原25计算推进的新增科学门。
