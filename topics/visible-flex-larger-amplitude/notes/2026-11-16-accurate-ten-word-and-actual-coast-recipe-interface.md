# R599 — 准确十词及实际 coast 配方的来源边界接口

作者：OpenAI ChatGPT（geometry 协作线）。日期：2026-11-16。  
可信度：已证明（限来源边界与准确转换的条件命题）。本源库未执行；后继 R597 的实际来源注册与实验结果另行承担。

## 1　交付与适用对象

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `computations/geometry_20261116_accurate_ten_source_boundaries.py` | 8620 | `236c24d0f8e101240c9469f29180c05e71838734cc76b4d35f383c27073a59b7` |

完整条件证明为
`results/R599-accurate-ten-word-and-actual-coast-recipe-boundaries.md`。
本接口与证明一起形成独立三件交付。展开后的 driver/closed-entry 不在本次冒充已运行源。

本组件只解释已经由原72c/3bc实际绑定的准确参数报告，并定位当前真实 launcher 的 coast-base recipe。原数值对象、十词、C、DAG、材料、profile、current H、RHS/J/native、全部门、原 namespace 和 deadline 均不改变。没有 CLI、输出目录、accepted 标志、数值预算或自动 dispatch。完整链由后继 R597 显式调用；不允许仅把本源加进来源表就声称调用已经发生。

schema：
`R599-actual-accurate-ten-word-and-coast-recipe-boundaries-v1`。

## 2　已核原来源

| 角色 | 实际来源 |
|---|---|
| 准确报告生产者 | `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py`，46691 / `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` |
| 完整 report/definition binder | `geometry_20261115_continuous_ten_same_metric_profile.py`，30299 / `3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6` |
| R503 实际 coast-base candidate | `geometry_20261116_actual202_coast_base_zero_linear_gzip_accurate_ten_candidate.py`，34123 / `237882e9fee9943e11b897c52118087753eb1d63e5c917e7382f14b5e8cb9399` |
| actual238 已读 driver | `geometry_20261116_actual202_coast_base_zero_linear_gzip_ten_full453_frozen450.py`，34462 / `b754fc536d00e90e8e18ecb1f160bb01f635b0ba2b77b2f685a942b7df942d6c` |
| R597 采用的已刊 capture-driver 祖先 | `geometry_20261116_request239_same_call_cubic_full453_frozen450.py`，35203 / `51960b100c5d14bb8f8790fca161051e61df8aab93273c59fbec19d4ab91953f` |
| 该 capture-driver 的真实 launcher | `geometry_20261116_request239_same_call_cubic_full453_frozen450_launch.py`，20615 / `3d6e12241230707ff38567be204d46c059c3aca35f8360d6d90a68d3e0ae865d` |
| R597 采用的已刊 closed-entry 祖先 | `geometry_20261116_request239_actual202_bound_coast_closed_postsolve.py`，47503 / `ba8c49fa3894e745557ae9d04e3ae4eb09307ef227e792dbe331e963958b696f` |

上述生成源来自完整已刊 literal plan，并非按 basename 假定其来源；后继必须继续核其实际字节。actual238 与 capture239/241 是不同源合同。R568 只证明 actual238 真实错误，R599 对后者的同一残留语句是源码事实，不能预填仍在运行的241/247结果。

## 3　参数字 API

```python
factory_parameter_words(values) -> bytes
```

`values` 是已绑定的
`target_owner.data["report"]["starting_parameters"]`，必须完整十项，顺序为：

```text
p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3,xi
```

输出恒为十个八字节小端字拼接；某项错误即整体报错，没有部分成功数组或省略项。函数要求实际
`GITHUB_ACTIONS=true`、指定 public repository、非空 run/source 环境。

接受的标量类型与解释：

- 非布尔原整数：准确整数；
- `Fraction`：准确有理数；
- 原字符串：与原72c相同的 `Fraction` 语法，包括完整 `n/d`；不先进行浮点除法；
- 原 `float`：保其原 binary64 字，明确排除非有限数；
- 其他类型、无效字符串、零分母、非有限浮点或准确有理溢出：明确异常。

准确有理转换采用全整数 RN ties-to-even；正规、次正规、underflow、二者交界和 rounding carry 见完整证明。该实现没有调用 `float(numerator)/float(denominator)`，也没有把准确串转成有位数限制的小数。

原浮点负零逐位保留。字符串准确值为零且原文显式以负号开始时，保负零；无符号数学零的 `Fraction`/整数零给正零；非零负数向零下溢保负号。本组件不为已丢失的负零来源猜符号。R503 的三个改变分量明确为正零，因此当前来源不存在该符号歧义。

### 实际 driver 的最小修改

以下是调用合同；具体新 basename、输出SHA和递归引用由后继完整来源计划记录。

1. 在 driver 的原 PINS 中增加本源 basename→完整SHA；
2. 用原 `load(name,digest,alias)` 加载到 `d.accurate_source_boundaries`；
3. 原 runtime 遍历 PINS 时，本源进入原实际 `d.closure`；
4. 只替换 factory 参数侧的表示转换。

原语句：

```python
if raw_words(full_p)!=raw_words(target_owner.data['report']['starting_parameters']):
```

新语句：

```python
if raw_words(full_p)!=d.accurate_source_boundaries.factory_parameter_words(
        target_owner.data['report']['starting_parameters']):
```

原 ValueError 文义、recipe侧八十字、已绑定 `CurrentTenProfile`、active/frozen 索引、原 source/candidate/core identity 与完整453→450顺序都保留。未来 source-view 必须声明这条完整 literal 的实际出现次数为1；若真实基线不符，应报来源差异，不能按模糊关键字改写。

driver 对完整 H 的 `raw_words(H)` 不改；same/union driver 和 native client 的原浮点字函数不替换。本 helper 不接受一份 H、DY、J 或 native 数组来重新解释。

## 4　实际配方路径 API

```python
actual_coast_recipe_path(base, descriptor) -> pathlib.Path
```

`base` 是原实际 namespace；`descriptor` 是已完成原 launcher run/source/schema核验的 `launch["recipe"]`。它必须具有：

```json
{"file":"绝对实际路径","bytes":25338,"sha256":"完整64位小写十六进制"}
```

上面的25338仅展示 R568 已返原件的字段类型，不是库常量或未来配方大小。库接受原实际非负整数 bytes；真正内容核验仍由原 `read` 负责。

唯一合法相对位置：

```text
actual202-ten-BVP-input/actual202-coast-base-ten-full453-frozen450-recipe.json
```

必须是原 namespace 中真实普通文件；不接受 `..`、绝对路径逃逸、文件 symlink 或通过中间 symlink 改向的预期目录。函数不创建缺失文件，不复制到旧名，不搜索备用recipe，不用cwd推断base。缺失/路径不符是原来源未付，原异常应完整保留。

caller 随后必须原样调用：

```python
recipe, recipe_id = read(recipe_path, launch["recipe"])
```

该 `read` 的实际 receipt 与完整bytes/SHA核验不省略；不能仅因路径存在而接受。原 deadline 中的 `recipe_sha256` 也继续对应同一配方。

### 实际 closed-entry 的最小修改

用现有 `load_pinned(self.comp, descriptor, role)` 加载本源到
`self.accurate_source_boundaries`，descriptor为本库实际 basename/bytes/SHA。仍在本次真实 computations 目录，不改变GITHUB_WORKSPACE或创建另一份科学源副本。

将且仅将：

```python
recipe_path = self.base / "actual202-ten-BVP-input" / "actual202-accurate-ten-full453-frozen450-recipe.json"
```

替换为：

```python
recipe_path = self.accurate_source_boundaries.actual_coast_recipe_path(
    self.base, launch["recipe"])
```

原完整 `read`、schema、request_number、deadline、resource、accepted450、owner quiet、八原科学角色及独立held控制流不改。路径修复不使尚未接受的初猜成为下游场。

## 5　注册与必要读回责任

本库只有两个实际边界，不要求另起科学阶段。后继 R597 将：

- 显式保留全部旧 public/generated祖先来源；
- 实际生成新 driver、launcher、policy、closed-entry及其真正传递消费者所需的新名/新SHA；
- 先核完整 literal baseline，再生成；不在旧文件名下覆写；
- 原prepare/source/readback记录保完整新源身份；
- 原 BVP、closed、refinement、same-C necessary 的成功和失败路径保真实新tuple，不仅改顶层来源标签；
- 继续原90000/70、原 quiet/marker/raw保留与唯一总clock。

若某来源字段尚未在后继注册，本接口不能被用作“已支持该family”的代替。本库不具有 accepted checkpoint reader，也不会把原字段误差变成一个忽略异常的 fallback。

原大文件、原science necessary body与原raw不会写入Git；本次Git交付只有作者源码、证明和接口。

## 6　未运行及完成边界

已完成的是严格输入语义、准确有限字算法、真实路径合同及完整源文本。未执行该库、任何数学运算、源码导入、AST/编译、fixture或solver。未创建新run，未改变原正在运行入口。

新源能解释当前合法 `n/d` 并读取真正回执，是原完整算法可以继续的工程条件；它不保证7200秒内求解成功、32GiB门始终满足、accepted450返回、误差下降或全闭面证书完成。原所有条件继续由本次真实调用结果决定。
