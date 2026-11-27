# 第18次入口第三个真实异常：geometry 的 meridian 来源常量补齐

记录：2026-11-27。本条只修正一个完整来源常量。原 query-independent meridian 生产器的计算、完整方法身份守卫、全几何点、32 stages、所有参数和预算都不变。当前无可因本修复而声称成功的场、根或费用。

## 实际错误与完整来源

第7步 callable-bound 科学入口没有返回首个完整 report。根取得的第三份完整诊断对应原日志 6,727 B，SHA256 `bf27eb1ef9a48f892e131a6a7acdfdf49be12e63627ddbec5b72c32504159048`，全日志从 byte 0 读取、两个 traceback 完整。诊断本身来自 source commit `0447302e7554a6139b8b4a12dc2e139681aaf1c0`；这个诊断来源提交不冒作原科学来源提交。原科学完整 commit 本条没有单独取得，不补造。完整失败卷及原命令由根另留原字。

真正抛出位置是当前 driver d5db 的 main line 605 构造 GeometryScreen；原 geometry c1dad 的 line 363：

```python
root_data_method = problem.detached_meridian_values.integration_data
if sha(root_data_method.__func__.__code__.co_filename) != DETACHED_MERIDIAN_VALUES_SOURCE_SHA256:
    raise ValueError('Use the complete actual query-independent meridian data producer')
```

guard 本身正确，完全保持。helper 的 `integration_data` 是该 helper 类在其自己源码中定义的实例方法，此处的 bound-method `__func__` 语义成立；不能把本次错误再误记成第二次 ordinary-function 解包错误。

实际 helper 已是 `eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de`，normal 的 MERIDIAN_VALUE_SOURCE_SHA256 已准确指向它。geometry line 46 却仍是旧 helper `7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd`。根在第二次修复的上层传播时更新了 geometry 的 ENDPOINT_SOURCE_SHA256，而漏传这一独立 helper 常量。该同源不等式因此确实拒绝当前 helper，和日志位置一致。这是来源传播缺口，不是根、均值、几何不等式或求解数值失败。

## 唯一源码变更

```text
DETACHED_MERIDIAN_VALUES_SOURCE_SHA256 = '7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd'
→
DETACHED_MERIDIAN_VALUES_SOURCE_SHA256 = 'eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de'
```

这一个 64 字符字面值替换后，完整 geometry 仍为 88,163 B。原 line 361–363 的整 guard、所有函数、全部 batch 缺角计算、逐点物理六 jet、完整空间聚合与控制预算逐字不动。source_binding 中的 detached_meridian_value_source_sha256 从同一常量读取，因此随之准确记录真实来源，没有额外改写或伪造 metadata。

V8 全文反向替换得到原 c1dad 源全部字节；这说明实际变更范围，不是本地 Python 或科学执行。其余完整 normal/helper 源保原字，新的 geometry 整文件 SHA 必须再由根传播至全部实际依赖；这里不放宽任何全 source、model、point、target 或 snapshot guard。

| 角色 | 文件 | bytes | SHA256 | Git blob |
|---|---|---:|---|---|
| 直接完整父 | `so3_fixed_fejer_batched_missing_angle_geometry.py` | 88163 | `c1dad273c31eacfd25e245927e35b07f0010441f95bc71a3dd56082c665c0e98` | `372e9da72b43c41b8c004d6e514ee8e83723415a` |
| 完整修后 | `so3_fixed_fejer_batched_missing_angle_geometry.py` | 88163 | `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135` | `c5325d3da8329547ad81e74a5da479323bfccd21` |
| 真实 helper，未改 | `fixed_fejer_detached_meridian_values.py` | 41126 | `eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de` | `2b547c08dcaeb55701f5c68ba56d405f595f5b9e` |
| 真实 normal，未改 | `fixed_fejer_detached_meridian_normal_lift.py` | 96276 | `76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d` | `fc51c16b6dbd53abf04fe9175e5421f77e25c49c` |

## 原件保全与完整文本再生

完整直接父在 source commit `f2eb4e3aaa6d9568418dd0373acb585738984823` 固定保留。新完整 source 使用相同职责 basename；根按新 SHA 完整传播与发布，不把过去真实失败输出贴上修后身份。

完整再生器 `topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_geometry_meridian_source_constant.mjs` 为 4134 B / SHA256 `e71abd38b4ef356a8b999d7a8ac035e92d273e4ce687c463f4b0520b7d88e179`。它只读两份原文件的完整 bytes/SHA，作上述唯一替换，核新 whole 身份并写另一输出路径：

```text
node reproduce_fixed_fejer_geometry_meridian_source_constant.mjs --parent-source <immutable-c1dad-parent-file> --meridian-values <actual-eaea-helper-file> --output <separate-complete-geometry-file>
```

本会话没有运行该 Node 程序、Python、AST、compile、数值、fixture 或科学；只做 V8 文本与整字身份处理并保护完整 blob。再生器不是求解或费用的额外准入条件。后续 full driver/reader/launcher/accurate-input 的身份由根实际派生，不填未来 hash。所有原157科学参数、所有目录保护、旧失败证据、完整未知历史及预算继续保留；当前求解若再次返回，以其真实日志/报告判定，不能从本单项修复推定后续通过。
