# 真实18第二异常：完整 callable 来源修复与原规模续求

## RET85：终态导读与完整历史记录

**已知后继终态：** 本文 callable-bound 源实际越过静态函数错误，却在 geometry 的 query-independent producer 守卫失败；下一记录明确实际原因是 geometry 仍钉旧 helper，未删守卫。完整[producer 修复与终态](2026-11-27-run18-complete-producer-binding-repair-and-continuation.md)保后续真实进展。最终 run 46062343475/1 官方 cancelled、完整最终场未返，本文旧错误未知段仍按当时知识保留。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。1 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 21289 字节；SHA256 `618d0de64a57ba32c879c3bf5c041d214b79fe1a402d26e7c60e2d593547be2a`；Git blob `80d5855da4d011733cea0c59d6a1d638d6ecebba`；固定提交 `1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-callable-binding-repair-and-continuation.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET85 完整交付表](../computations/terminal-run15-18-narrative-retention-85-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

会话 Astra-larger-e4e2a2bf-20261126；公开 Actions 46062343475/1。**未完成；这是实际代码异常的必要修复，不是数值成功、严格几何结论或 README 完成。**

## 实际发生的事情

第一科学入口 `complete-fixed-fejer-meridian-batched-first-20261127` 在实际源码提交 `7936ae753065d6e47c1c02848551020acf5a7b2a` 以 1 返回。完整原始异常读取器确认 frame 的完整方法身份表未登记新的 `_meridian_data` wrapper；完整旧族和参数固定于 `36fb3539d71ac8826645df636359d34769f786e9`，该次修复完整发布于 `bf863c8796a36e99c175117688e692fd5009a89e`。第一修复没有改变任何数学方法、求解预算或来源校验的要求。

第二科学入口 `complete-fixed-fejer-meridian-batched-method-bound-20261127` 真正采用提交 `5a8dcd127ecb1120418b258f43fad7ada5080560`、完整 launcher `fda0da129cc1a3eaa36dac6192a1ca5c432eb77daea0312da3de9deafe057f45`；8.185087835999639 秒后以 1 返回。实际 command 50554 B / SHA256 `b55b8079fe6d0aeee2855f5edd1439d12c162f7579e1effc5e277ae1eeb164dd`；`report.json` 缺失，不能声称已进入任何几何结果、求根结果或接受循环。

同一 runner 的原始日志是 `followup-logs/0005-ec12dc9c2181.log`，7163 B / SHA256 `83e390680916537cc46ad466c734bf1075fcdb23a2491c3ac5107ea4fc4c86b5`。原 8679 B、SHA256 `5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360` 异常读取器实际返回 0，输出 11678 B / SHA256 `748ee03d35d89df6cda26e52f6e36799ace8a8981c42157b50642f5f55f1aacd`。它从 byte 0 读取完整日志；两个 traceback 各自完整，外层末行摘要的 2048 字符截取不影响第一个异常。读取器的零返回不是科学计算的零返回。

真实首栈如下；完整带字节身份的诊断保在 [part-002](2026-11-27-public-actions-46062343475-1-part-002.md) 的固定 `58c6b5ab92364fd00b1d0f24add7f72891fe327a` 版本，以及完整 lower 修复交付内。

```text
Traceback (most recent call last):
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0005-ec12dc9c2181-5a8dcd127ecb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py", line 1130, in <module>
    main()
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0005-ec12dc9c2181-5a8dcd127ecb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py", line 544, in main
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0005-ec12dc9c2181-5a8dcd127ecb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py", line 494, in __init__
    self.detached_meridian_values = meridian_value_module.DetachedMeridianValues(
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0005-ec12dc9c2181-5a8dcd127ecb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py", line 204, in __init__
    function=getattr(q.base,name).__func__
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'function' object has no attribute '__func__'. Did you mean: '__doc__'?
```

## 必要且完整的实际修复

完整原 `552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3` 基类的 `_radial` 是 staticmethod。实例读取它得到普通 function；其它已登记方法读取为 bound method。旧 helper 对八个实际方法统一访问 `.__func__`，因而在构造时抛异常。

新 helper 在构造时先读取 `bound = getattr(q.base, name)`，再使用 `getattr(bound, '__func__', bound)`；每次请求的身份复核也采用相同解包规则。保留 `function.__code__.co_filename` 对应完整源码 SHA 校验、原 `is` 身份比较及所有实际值缓存、查询、normal/frame/closure/jet 方法。实际绑定的 `q.fields_torch` 方法仍使用原身份校验；没有把所有函数检查一概取消。两处完整替换正逆逐字恢复原 41030 B helper；新体仅增加 96 B。normal 的唯一 helper pin 和 packet 的唯一 normal pin 随完整新源码更新；第一修复的 47431 B frame 保持不变。

全部上层来源联动使用固定父 `bf863c8796a36e99c175117688e692fd5009a89e` 的完整源码：九项 binder、transfer、geometry、geometry 读取绑定、完整 137 项 driver、纯读取器、launcher，以及准确场输入五项 pin。source 数值表、数学函数、接受循环、原 120 个历史 path/SHA 对全部保持。准确场输入仍为完整 32969 B 文件；只更新真实五项来源，不借初始或第一次修复后的标签冒当前场。

| 完整改变的来源 | 字节 | SHA256 | Git blob |
|---|---:|---|---|
| detached_meridian_values | 41126 | `eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de` | `2b547c08dcaeb55701f5c68ba56d405f595f5b9e` |
| endpoint | 96276 | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `fc51c16b6dbd53abf04fe9175e5421f77e25c49c` |
| root_packets | 73723 | `c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4` | `2b294ce46cf51c24c90b6e71c26d0d9c4269d28f` |
| analytic_J3_binding | 41894 | `3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68` | `d753647cfb4a0df8bc5d650cf4ca49ae1573f5f3` |
| envelope_transfer | 78920 | `b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc` | `2e112909d6937363ad0a643a2acbc1e54f7d8bcd` |
| geometry | 88163 | `c1dad273c31eacfd25e245927e35b07f0010441f95bc71a3dd56082c665c0e98` | `372e9da72b43c41b8c004d6e514ee8e83723415a` |
| batched_geometry_binding | 12136 | `21b3e81c1d8db9ea1887a76c89b1b2e915df47a970ff8fa83f55399b52d33344` | `5cc1ce1fedb66893ef0ecb65239476c4eacd1aec` |
| driver | 99313 | `d5db14d2806a99cc60a9f131d678978c9ac5eb4cef5d216869baedcca3411a47` | `b162dbc5c973ed599817f2ab0c1f4c3c721dc7ba` |
| reader | 99382 | `0d6d70b5bb0b1901216d0fb90117c36bded5e2c70d13cd6a8982d8f0a0cbf323` | `8ef06dcb06c4da94b23b36ecdf8b9569b4b9c120` |
| launcher | 22136 | `d683762cfacb24a91d0011a1a061f1e7cda992595717f3f5dc9e8d71bb3207db` | `718c4d81e058aa7b73c50ef7934ffdbf06e561f7` |
| accurate_field_input | 32969 | `38ae9e2d6a96360e21889db8be4d45ae0092b01837db04d5dc7f93cffa1d1dd3` | `259fcfac29ee34cba5a31326f8eb9052f1fe42e3` |

137 项完整 registry 和当前 18 个运行来源保在 [完整交付](../computations/fixed-fejer-meridian-callable-binding-repair-complete-delivery.json)，不是省略表。lower 完整源及两处实际替换保在 [lower 交付](../computations/fixed-fejer-meridian-callable-source-repair-delivery.json)。所有文件小于 100KB；运行源码没有为了文件大小省去方法或字段。

## 原输入、全部参数和实际续求

原第 1、2 阶段已真实分别返回 0；不重建。固定参考 bundle 894879 B / SHA256 `212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb`，参考准备报告 84971 B / SHA256 `38a5932ebe77cb8f1513c369f6f575f112bac73dc815ac1406d30ce0aa2d0be2`；maker 报告 65336 B / SHA256 `b800ec4fd4901b903a7c12eb970c14373206e6f30b0d2ebe43f0ee852b72139b`。nodes、scalar、carrier、locations、provenance、target 和 binding 的完整实际身份保在交付表。它们留在同一公开 runner；不会跨 runner 复制原始结果，也不把结果改名为输入。

完整科学参数 [science](../computations/fixed-fejer-meridian-callable-bound-science-complete-ready.json) 为 97836 B / `eea00885274638f7fe53dd126abcf17d809d73b9d5d1bdacf10fd4d6a9645be5`，完整 157 个 argv、458 个 formal selector；[pure](../computations/fixed-fejer-meridian-callable-bound-pure-complete-ready.json) 为 85264 B / `36fda0fac3ecb9b07b13aedfc8452eb656fa9f4f146974a5502072c761afd8b7`，完整 7 个 argv、445 个 formal selector。原科学 408／纯读 395 对应与新增 50 个完整来源/观测字段都保留；48 个实时映射完整保留，其 6 个数学进展与 42 个 normal 字段不混时刻、不猜缺项。所有参数逐字来自固定原完整 36fb 参数文档，唯一 argv 字符替换是完整输出 namespace。

当前完整输出为 `fixed-fejer-meridian-batched-callable-bound`，command 为同 prefix 加 `-command.json`。它与前两次失败输出分开。固定 g、M160、J923、N2048、32 stage、全部变量、支持和胞、seed fractions 1/4 和 1/32、全 15 个 line trials、原 direction/restore 预算、求根与 quadrature 预算均保持原字；不增试运行、AST、fixture、局部求根或独立审核关卡。缓存容量不作为削减科学预算的方法。

当前队列以完整科学对象 65309 B 提交；`finish_when_done=false`。前一诊断对象已实际返回 0，完整原队列固定保在 `6e9f7c6f011020aee245ce97950bf01ad109893e`；前一科学对象真实已返回 1，完整旧队列和完整 ready 保在 bf863。完整科学和纯读合并超过控制器 95000 B 参数载荷限制，所以纯读保留全对象，待真实科学自然返回后接入；没有裁预算或 selector 来容纳。提交时新的实际 source commit、运行结果、场、packet、accepted、严格 fee 仍未知；必须读真实 Actions 回传。

## 完整再生与严格责任

[上层完整再生器](../scripts/resume_20261126/reproduce_fixed_fejer_meridian_callable_binding_upper_sources.mjs) 从固定 bf863 读取八个完整父文件，保全部正逆替换、结果 SHA/bytes/Git blob。 [参数完整再生器](../scripts/resume_20261126/reproduce_fixed_fejer_meridian_callable_binding_parameters.mjs) 从固定 36fb 读取两份完整原参数，输出完整当前两个 ready。两者只是完整来源/参数保存，没有被加入实际科学步骤，也没有执行局部科学计算或把成功再生当数学证据。

当前独立 callable_R722 准确后验核、全误差包、closed/R718、R716 与全空间/频率/时间网格必须显式钉本次完整来源。旧 e10a/9da R722 数学说明不等于当前场的付费，旧 ae67/0471 的 R709 boolean 不伪造为 true；后验条件、整圆全部 1024 胞、全部 922 径向区间及 cuts、32 stage、六 jet、全部尾和 working 误差仍须实际支付。所有下游完整保留，不能用 normal.complete 冒连续分支完成。

README 所需同一固定 g 的全 t 闭连通 C² 嵌入、强 C² 连续、共同有内点 H、整像无对齐 δhold、含反射 δE、全 t reach、整面 metric 算子误差以及固定参数的实际精化都未完成。继续真正求解与证明，不在此次错误修复或来源包上收尾。


## 后续实际自然返回：第三科学入口失败，内部原因待原日志

21:17:44 UTC公开索引记录第7阶段自然返回。完整source commit `512fcefd67eb0adba7b27e654cb51bacf82c2439`、launcher SHA `d683762cfacb24a91d0011a1a061f1e7cda992595717f3f5dc9e8d71bb3207db`，8.196651488000043秒后exit1。command50558B/SHA256 `7efc2534cdaac860314581b56669ce269b8276379a2be01022f26208b10e2dcf`，report缺失。未从外层退出码猜原内部原因，未推断F/J/root次数或accepted。原同runner的完整5d25读取器已排，读 `0007-8be405c2d4f2.log`；原参数对象实际含16个argv词、45个摘要字段，逐项完整保留（按对象精确计数，旧scope的44口径更正）。原完整science/pure与既有inputs仍保。完整当次执行如下：

> **原 JSON 01：callable-bound 科学入口失败完整返回。** [固定旧版完整记录，第 78–314 行](https://github.com/Rogerhu12/math-research-public/blob/1b64c4a7e8b3c09ae6231fdd604659ca492f3ae4/topics/visible-flex-larger-amplitude/notes/2026-11-27-run18-complete-callable-binding-repair-and-continuation.md#L78-L314)。

