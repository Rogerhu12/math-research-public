# 独立21-query lambda27原件reader：严格新producer，原B合同不变

分类：已完成产物的只读提取和字节核查接口。  
作者：ChatGPT（amplitude，AI辅助）。  
日期：2026-11-15 UTC。

## 1. 独立源

`root_20261114_read_completed_twenty_one_lambda27_prefix.py`为49810B，SHA
`42fb5d0f97c2cee619e2ac1b7e6ee2b9249ee42a518a23cdc9d4c462e0d3c3fa`。
它是原21-reader `0feeb16e350d06ed03abb93c8ff80dd6e9e10a2703d47135f3c36ee3c289ea3a`
的独立严格身份适配，原reader未改。只有当前目录、producer schema、
readback schema、源pins与说明改变；所有35个函数/类AST逐项相同。

新科学目录为`twenty-one-lambda27-condensed-warm`，producer必须是
`exact-constraint-twenty-one-query-lambda27-condensed-complete-H-warm-v1`。
没有放宽原21reader以同时接受多个不确定schema，也没有通过旧source
标签替换来把阻尼27产物写成原270。

| 必须存在的当前源 | SHA256 |
|---|---|
| 原21domain `geometry_20261114_twenty_one_query_domain_operator.py` | `0007a3dd345cb60172c75ef6490fa3f0bbcfdc178be90e532120302fc6c15a65` |
| `geometry_20261114_twenty_one_query_lambda27_condensed_warm.py` | `a8dd293b4b10ab45a2e69dd1e3e37a2032e4af3eb4d5f21eefa556277cb0d64c` |
| `geometry_20261114_twenty_one_query_lambda27_condensed_response.py` | `270797569ecff1e3b895d8bb5482c6c9f3c2a4e11d29ebc980c3cfd8bcd88bb0` |
| `geometry_20261114_twenty_one_query_lambda27_collocation_observer_warm.py` | `12437f6887b7fb6a7d5ea91214b95227056238054cd73e6db8c123f2aa49e881` |

完整transport仍为冻结
`exact_20261114_fetch_pinned_public_artifact.py`，SHA
`51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。
完整原ZIP size/SHA、来源run/source、每成员CRC/路径安全及异常保全均
沿原代码。入口只允许本公开仓库Actions运行，无科学源import。

## 2. 原21查询与完整字节范围

原14left、7mid的typed顺序、完整`43008×236036`B及声明局部7101全部
保持原合同。实际B并集6763；node484的338列仍为原21连续布局零块。
不能误用新22-query的45056行/全7101实际并集或声称该对照已加入left484。

所有domain NPZ/NPY、完整B/Gamma/Pi分块重组、原base和列映射，所有
condensed完整数组引用和14个root/affine/recovery raw仍逐原byte核。
完整父producer、实际新warm/status/FD、新科学源账及只读observer保全
与原reader相同。原source未在checkout时明确报未独立核；4个当前pins
缺失或不匹配会报告读取层失败。未导出完整QR因子的事实继续保留，不
把内存hash冒作独立因子文件审。

原小trial、最近拒绝、候选/FD标量先落盘，再审大payload。后续读取异常
保repr/traceback、失败阶段及已提取原数值；不改原science run状态。
NumPy只用于解码、dtype/shape、byte转换和哈希，不算新的RHS/J、norm、
dot、矩阵动作、QP、FD或native，不增加科学接受门。

## 3. 同基点对照的范围

阻尼27分支与实际68都以实际66同一个warm/status为父。比较时可复用
已完成68-reader artifact中的`complete-original-byte-audit.json`，SHA
`2e5b678efa113789649c15b893e07d93fdd94fef4ab44086e308a1d11e0e8abb`，
无需再次读取590MB原68包。新70payload只需读一次；后续比较已有审计的
科学数组hash和原报告，不重算原模型。

应分别核同父base、原Wr/S、b/g/c与完整B/Gamma/Pi等字节，并明确九项
完整A输入hash是原Actions报告身份：L/R等若未独立导出，不能把报告
hash对照升级为两份完整矩阵payload独审。阻尼改变的H/root/方向与新的
source/model provenance无需相同；不能以model SHA不同声称B改变。
有限预算下方向和QP精度也必须读取原实际回执，不能预设27更优。

本reader本身不重做两轮科学比较；它保留完整可对照的已审字节清单。
同基点解释应在两个真实原回执齐全后写结论，不跨不同权重模型减merit。

## 4. 完成后真实CLI

实际artifact身份尚未由此源填入；所有`ACTUAL_*`必须来自真实完成回执：

```bash
python -u "$COMP/root_20261114_read_completed_twenty_one_lambda27_prefix.py" \
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

输出名称、原报告artifact副本和小target报告保持原reader。不需要Node或
native worker；只有标准库transport和NPZ解码用NumPy。凭据仍只在原
公开Actions运行环境。first-attempt artifact命名仍严格核为
`visible-followup-condensedqp-<actual-run>-1`。

旁附完整`.diff`和`twenty-one-lambda27-reader-static-check.json`，后者
2384B，SHA`c32aea4d74489b9de6f00b03e718bf57496be2c8df3794f1c75192f924bb70d0`。
只完成源码AST/字节pin核；未执行reader，未构造任何科学fixture或未来
完成结果。该身份适配不阻止先行登记实际70的小原报告。
