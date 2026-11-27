# Run18 第二次真实初始化失败：基底静态函数与绑定方法的精确来源修复

日期：2026-11-27。本文与完整源码一同保存；发布、队列和实际执行由主线程处理。本次是已经发生的 Python 接口失败修正，不是新的科学结果。全部候选源已保存为远端完整 Git blob；没有本机科学、AST、编译、fixture 或性能运行。

## 1. 原始返回与诊断范围

实际 run `46062343475/1` 的 `complete-fixed-fejer-meridian-batched-method-bound-20261127` 使用执行提交 `5a8dcd127ecb1120418b258f43fad7ada5080560`，在 8.185087835999639 秒返回 code 1。它只有 50,554 字节的 command，SHA-256 为 `b55b8079fe6d0aeee2855f5edd1439d12c162f7579e1effc5e277ae1eeb164dd`；没有 report，不能作为返回场、父末点、完整方向或误差证据。

同 runner 的第 6 步使用原完整诊断源码 `5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360`，在 6.021356374999868 秒返回 code 0。完整公开卷为 [实际 part-002](2026-11-27-public-actions-46062343475-1-part-002.md)，本次读取版本是 17,115 字节，SHA-256 `aec4338b8396ead6a9797d5abda7f5a709598895fafb67b28ea264d10055cc40`，Git blob `205edb648e24bf8e4eab710282046e3040a774ee`。该文件以后可能继续追加，固定 blob 保留本次完整观察。

诊断输出是 11,678 字节，SHA-256 `748ee03d35d89df6cda26e52f6e36799ace8a8981c42157b50642f5f55f1aacd`。原日志 7,163 字节，SHA-256 `83e390680916537cc46ad466c734bf1075fcdb23a2491c3ac5107ea4fc4c86b5`，由 reader 全部捕获；首、末完整 traceback 摘录均未裁剪。末尾单行另有裁剪标志，不将该单行误当完整诊断。完整小卷和参数、输入记录随本次 manifest 保留。

实际首栈从 driver `5b0dc357…` 的 main 第 544 行，进入 normal `33c269f3…` 第 494 行，再到 helper `7aa760ba…` 的构造第 204 行：

```python
function=getattr(q.base,name).__func__
```

异常为 `AttributeError: 'function' object has no attribute '__func__'`。本次已越过先前 analytic-frame 的 `_meridian_data` 精确来源断言；不将这个事实扩大为场、根或费用已经成功。

## 2. 真实基底接口

完整读取的实际基底是 `fixed_fejer_supported_so3_meridian_operator.py`，40,840 字节，SHA-256 `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3`，Git blob `1d9e435bb68374b71c3d7361771c28f47838d59e`。

helper 原循环绑定八个完整基底方法：

```python
('_unpack_torch','_angular_nodes','_radial','_meridians','_parent',
 '_parent_tensor','_integrate','make_query')
```

其中 `_radial` 在该完整源码中明确声明为 `@staticmethod`。读取实例的该属性得到原 Python function；其余七项是绑定到实例的方法。无条件访问 `.__func__` 因此会在真实构造中失败。这里不推断张量、形状、数学定义或精度有错，也不改八项列表或任何原来源断言。

## 3. 唯一两处可调用对象提取改动

构造时改为：

```python
bound=getattr(q.base,name)
function=getattr(bound,'__func__',bound)
if sha(function.__code__.co_filename)!=BASE_SOURCE_SHA256:
    raise ValueError('The complete original meridian base method differs: '+name)
self.methods[name]=function
```

绑定方法仍取其原 `__func__`；静态函数保留其自身。后续 `__code__.co_filename` 的完整文件 SHA-256 检查逐字保留。没有给缺失代码对象的任意可调用对象开放旁路，也没有在来源不符时忽略异常。

每次请求的 `_source_binding` 中，用同一提取规则与构造时保存的原函数做 `is` 比较：

```python
or any(getattr(getattr(q.base,name),'__func__',getattr(q.base,name)) is not fn
       for name,fn in self.methods.items())
```

若只修构造而保留这里的无条件 `.__func__`，首次真实调用仍会失败。因此两处属于同一个实际接口修正，不能省略后者。基底对象、完整 base/model/identity、完整父 provider、校准对象、normal 方法对象及 closure 的来源检查全部原样保留。

normal 自身的 `fields_torch` 是完整绑定方法，其既有 `.__func__` 读取没有改变。本次没有全局替换所有 `__func__`，也没有增加方法白名单别名。

## 4. 三个完整新运行源

路径均在 `scripts/resume_20261126/`，使用原 basename 的明确新 SHA。原字节固定保存在上一轮公开提交 `bf863c8796a36e99c175117688e692fd5009a89e`；不能用新 hash 代表旧失败源码。

| 完整文件 | 字节 | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| `fixed_fejer_detached_meridian_values.py` | 41126 | `eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de` | `2b547c08dcaeb55701f5c68ba56d405f595f5b9e` |
| `fixed_fejer_detached_meridian_normal_lift.py` | 96276 | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `fc51c16b6dbd53abf04fe9175e5421f77e25c49c` |
| `fixed_fejer_meridian_root_packets.py` | 73723 | `c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4` | `2b294ce46cf51c24c90b6e71c26d0d9c4269d28f` |

helper 从 41,030 增为 41,126 字节，只上述两处改动。normal 的完整 96,276 字节只更换 `MERIDIAN_VALUE_SOURCE_SHA256` 一处，所有类/函数正文原字不变。packet 的完整 73,723 字节只更换当前 normal 的整源登记一处；其父表没有 helper 的直接身份项，没有伪造额外项。packet 原值、顺序、点身份、32 阶段记录、实际角矩阵有无及报告钩子全部不改。

另外七个下层完整运行源原字共享：

| 完整文件 | 字节 | SHA-256 |
| --- | ---: | --- |
| `fixed_fejer_meridian_closure_values.py` | 59440 | `2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0` |
| `fixed_fejer_meridian_analytic_stage_jacobian.py` | 25697 | `223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811` |
| `fixed_fejer_meridian_analytic_normal_frame.py` | 47431 | `d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd` |
| `fixed_fejer_meridian_normal_frame_c1.py` | 37361 | `c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246` |
| `fixed_fejer_meridian_stage_matrices.py` | 61280 | `f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791` |
| `fixed_fejer_meridian_adjacent_matrices.py` | 36766 | `bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564` |
| `fixed_fejer_meridian_reference_calibration.py` | 11872 | `aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3` |

尤其第一轮已经修正的 analytic-frame `d3cf0106…` 仍保完整精确 `_meridian_data` 来源。没有退回原错误 frame，也没有重写其全部方法检查。

## 5. 保留的科学与身份边界

该改动不改变固定数学 recipe、全部变量、固定参考、Q/γ、原积分与查询公式、32 个 normal 阶段、角根升级、原每阶段与最终方程复读、完整物理六 jet、active J/J* 链、工作精度或任何执行预算。

meridian 缓存的完整点/不可写 owner、当前模型、ordered φ/order、control/data words、plain-detached 判据、全部旁路、容量与淘汰、异常回退、计数及 metadata 均没有改。两处来源提取不构成缓存命中、加速、bitwise 科学结果或正确数值的证据。

所有 137 个科学来源角色与原 120 对父路径/SHA 的保存责任由完整上层家族继续承担。需要更新的当前下层身份就是上表三件，随后主线程按精确依赖传播 binder、geometry、transfer、driver、launcher、pure 与准确 input。没有为本次修复添加未消费的历史 peer CLI 支持，也没有删掉未知旧分支义务。

## 6. 完整字节复现与固定父版本

完整可选构造器是 [reproduce_fixed_fejer_meridian_callable_source_repair.py](../scripts/resume_20261126/reproduce_fixed_fejer_meridian_callable_source_repair.py)，8593 字节，SHA-256 `04130f0048d3085c7dd35b940d74389ee2e35d6af581ccafb9950e57d8befb1e`，Git blob `38dafd4d1e6fe6943b4f5aca6fb69fecf5a848b9`。

它从固定提交 `bf863c8796a36e99c175117688e692fd5009a89e` 读取三个原完整源码和真实基底来源，逐体核完整 bytes、SHA-256 和 Git blob，再按 manifest 内的两处源码提取改动及两处精确 pin 替换产生完整新文件。每个输出均可逆恢复原完整字节。它不从可能已被覆盖的当前同名源猜父身份。

```text
python3 topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_meridian_callable_source_repair.py \
  --repo /absolute/path/to/checkout \
  --outdir /absolute/path/to/separate-source-scratch
```

构造器只读 Git 源对象并写不同 scratch 目录，不修改 refs 或队列，不导入科学模块。它拒绝覆盖不同的已有输出。未将此可选源码工具设置成新科学执行前门。

本次实际已完成的是 V8 内的完整 UTF-8 文本替换、三份完整输出正反替逐字核、SHA-256/字节计数和完整远端 blob 保存。没有宣称执行过该 Python 构造器、AST、编译、科学测试或性能测量。

## 7. 已保存的历史与尚未返回的工作

第一轮 `_meridian_data` 来源修复及其完整父包、参数、失败报告均保留在固定历史提交；第二轮原失败栈/command/诊断也完整保留。本次三份新字节不会改写这两次真实失败记录。

截至本说明成文，修后真实 report、完整点、packet、数值结果、费用、可行性、收敛或用时均未返回，相关字段保持 null。源修复可立即由主线程联动发布执行，无需等待费用包或本说明成为前门。

独立 R722 准确费用分支的数学/API 候选已经另行完整保存，但其早先版本绑定的是本次失败的 `5b0d/79375/33c/45dd/fd299` 家族。它们必须按这轮实际新身份形成明确后继；不能把旧候选改称已消费新场，不能把旧 R709 条件改成 true。闭面/R716/mesh 后继同样只接受各自完整实际来源与返回。这里只完成真实初始化接口的必要修复。
