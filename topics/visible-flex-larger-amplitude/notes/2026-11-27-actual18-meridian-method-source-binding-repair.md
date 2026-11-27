# Run18 实际方法来源拒绝：完整 meridian wrapper 守卫修复

本次修复针对 Run18 已真实返回的一个构造阶段错误：analytic normal frame 的严格方法表仍保存旧 `_meridian_data` AST 身份，却没有为新完整 meridian wrapper 登记其准确源码。修复只把这个真实 wrapper 加入既有完整方法源码字典，再更新必要 whole-source pins。完整科学算法、所有变量、32 阶段、原角/径向域、预算、残差复读和所有其他守卫不变。

这是同一组原18 basenames 的明确新 SHA 版本。原失败源/参数并未被改写成成功版本：完整原字固定保存于 `36fb3539d71ac8826645df636359d34769f786e9`；原科学实际执行 commit 为 `7936ae753065d6e47c1c02848551020acf5a7b2a`。新可逆再生器从前一固定 Git 提交读取全部原字，不要求当前工作树仍保留旧版本。

## 1. 实际返回证据与故障范围

实际公开小卷完整对象为 42,893 B，SHA-256 `ac49f5b0f00b2a7185be88b7a0c0593e74d67978b172e5c2a2e72c062ac463ab`，Git blob `b4c479790c2d90184be6f42d77322affca66af5b`，记录 Run18 `46062343475/1` 的步骤1–4。前两必要输入真实 exit0。首科学步骤真实 exit1，elapsed `8.147090872999911` 秒，只有完整 command record：

- 50,540 B；
- SHA-256 `491c172cebc830da4af9449b669ebd3f6b684dd0887357755c099b71778b07d3`；
- 实际路径 `/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-meridian-batched-first-command.json`。

随后原runner真实异常读回 exit0，诊断报告 11,675 B，SHA-256 `85cbea9228c60fd15a6c6e7397bd3a3e39e6e33bc349d8305657588abdbe131b`。完整原日志 7,167 B，SHA-256 `1baa32787375046913bdb762ff4d57db990e0e8567d75cd8b03f13834d5d190d`。first/last traceback excerpts 完整，不用截短 final-line 字段判断故障。

真实栈从 driver 的完整 `ZeroClosureOperator` 构造，进入 normal `388c` 的 line489，再到 analytic frame `ab282` 的 line372，报：

```text
ValueError: A full original method or the explicit frame wrapper changed: _meridian_data
```

这个栈定位为来源表不匹配，不是一个返回的几何、mean、normal 根或准确费用失败结论。缺失 report 仍缺失；command、已完成 reference、缓存数值或未来点都不替代完整场。该修复不猜后续科学结果，也不把本地文本工作当作新的构造成功返回。

## 2. 实际缺口及精确修法

原 analytic frame 的 `METHOD_AST` 保留旧 `_meridian_data` 摘要 `e5244b9fc2e68bee33692e76f7e5aa09422564d1b38bd59cf146646bc8530e9e`。既有 `METHOD_SOURCE_OVERRIDES` 对 `_closure_jets`、`_closure_jets_original` 和 `_run_chain` 已保存完整派生源码；`complete_method_ast()` 用同一 `_ast_value`/canonical 算法把这些完整源码转换成准确的方法身份，再覆盖父方法摘要。

实际388c中的新完整方法恰为：

```python
    def _meridian_data(self, x, query, phi, curvature, query_label):
        return self.detached_meridian_values.meridian_data(x,query,phi,curvature,query_label)
```

新版本只把上面这段完整函数作为 `"_meridian_data"` 第四项加入同一个 `METHOD_SOURCE_OVERRIDES` 常量。原三项源码字符串逐字不变；原 `METHOD_AST` 全父摘要也保留。执行期仍通过原完整 `ast.parse(textwrap.dedent(source))`、单一 FunctionDef/准确名称约束、原 `_ast_value` 与 canonical 定义得到唯一的新期望。

`complete_method_ast`、`definition`、`AnalyticNormalFrame.__init__`、后续实参/对象检查和整个解析 frame 算法没有改动。没有删除方法、绕过循环、吞掉 ValueError，或把任意新方法列为允许。被允许的只有已实际完整读取的这个 wrapper；它指向的完整 meridian helper 仍由 normal 和 helper 自身的 whole-source/model/对象检查约束。

只向已有静态字典添加 literal，因此既有 pure policy 提取的 `METHOD_SOURCE_OVERRIDES` 常量接口不增加符号、不需要容许动态猴补；source binder 仍按完整新 analytic-frame 文件身份读取该常量及原函数。这个修复没有在本机运行 Python AST，也没有预填该期望 AST 的计算结果。

## 3. 三个必要完整运行体

| 文件 | 原完整 SHA-256 | 新完整 SHA-256 | 新字节 |
|---|---|---|---:|
| `fixed_fejer_meridian_analytic_normal_frame.py` | `ab282ea02ce774b6f2aa044c700389369d05d1ff6105cdc9a0dbdae33a4db544` | `d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd` | 47431 |
| `fixed_fejer_detached_meridian_normal_lift.py` | `388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4` | `33c269f3cd04c9435ccb5144984124c8a0b6ae348f95c8bd71ac92a334c51cf4` | 96276 |
| `fixed_fejer_meridian_root_packets.py` | `910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15` | `45dd618adaa5262002bfb9d1979b6f555fe5233a57ec0f75abcec2ab7633a5be` | 73723 |

analytic frame 只增加上述完整来源项，共187字节；normal 只在原位置替换唯一 `ANALYTIC_FRAME_SOURCE_SHA256`；packet 只替换当前18 registry 行的 normal key 与 analytic-frame 值。normal完整方法类、packet全部函数与其余历史 registry 原字不变。没有把 failed388c/ab282身份贴到新字节，也没有增加 prererepair source aliases。

三者完整 source/schema/API 保持原家族合同，新 source SHA 如实进入当前模型与 packet 归属。模型完整 identity 因 source/implementation policy 变化而改变，不伪称工作文件或模型字节仍等于旧版；固定数学 g、seed 数学定义、原物理场表达式和求解算法没有因此重新定义。

## 4. 七个完整下层源为什么原字共享

新 meridian helper7aa、closure2889、C1c977、stagef98b、adjacentbd65、analyticJ3223a 和 calibrationaa40 保留各自完整原源。全文检索旧 frame/normal whole摘要的实际引用后，只有上述 normal 和 packet 需要递归换 pin。

其中 C1、stage、adjacent、analyticJ3、calibration 没有这次新增 `_meridian_data` 的旧方法摘要入口；closure 已有当前完整 wrapper 的明确源码比较，且保持全方法集合/完整父体检查；meridian helper 则动态读取实际 normal whole source，并同时约束 model、全部实际方法对象、base/provider/calibration/source。它们不是“不检查”，而是其现有严格接口没有本次漏项，故不能为了修一处来源表而重写它们。

所有 original stage/final closure reread、32共同分段、全部隐式 solve、C1上游图、全control words、immutable point owner、完整同point/ordered-angle/order缓存键、active/transform旁路、内存回退与原counter归属全保。该说明不声称一次 source-only 修复已经证明运行速度、根成功、全局唯一性、精度或几何目标。

## 5. 上层完整联动与原身份保留

root 负责当前 source binder、batched geometry、batch pure helper、memory transfer、driver、launcher、reader和全参数的必要新 pin。既有137角色数量不变；原120对完整父路径/SHA不删，不额外塞入 failed18角色造成接近100KB的完整入口溢出。旧失败体、全参数、原manifest及原执行记录按固定 Git 版本完整恢复。

科学 wide-seed `1/4`、`1/32`，M160/J923/N2048、全部自由量、32normal阶段、所有角/径向域、原预算和原求解循环保留。新输出 namespace 由root的完整实际参数决定；本修复包不生成或改队列、不重复必要 inputs、不偷填 future report/point/final/packet。

准确费用、closed/R716、R722 后继必须明确读取修后完整 driver/reader/normal/packet/input 身份。不能把旧18已锁费用模型改标签成新模型，也不能把一个修复 source guard 的工作冒成准确root/mean费用已付。本次源修复与R722后验数学不同，后者仍是独立完整分支。

## 6. 固定 Git 父体的完整可逆再生

配套 `reproduce_fixed_fejer_meridian_method_source_repair.py` 对每个父源执行：

```text
git show --no-textconv 36fb3539d71ac8826645df636359d34769f786e9:<完整原路径>
```

它核完整字节数、SHA-256及Git blob SHA-1，按显式完整替换产生完整新源，再逆向恢复每个父体全部字节。旧工作树路径可以已经被新版本覆盖；再生器不读它们充当旧父体。新source输出要求单独scratch目录，拒绝覆盖不同既有文件；source构造不导入数学module或AST，不执行F/J/root，不是实际求解前门。

命令为：

```text
python3 topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_meridian_method_source_repair.py --repo {repo} --outdir {scratch}/actual18-method-source-repair
```

本次已经做的是V8纯字符串的三源完整forward/inverse等号、完整source哈希和实际小卷/守卫文字读取。没有在本机执行上述Python、科学源、AST/compile、fixture或benchmark；也不把这些另设为root实际运行的前置行政条件。

## 7. 真实状态

原18第一science的exit1/缺report/完整异常属于永久真实历史。修后的实际science是否完成、能否返回完整场、后续优化方向和准确费均取决于新的真实Actions返回；本包没有这些数值。它完成一个有具体运行证据的严格来源表修复，保留原所有数学责任。
