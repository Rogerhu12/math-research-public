# 原有限域次数门：Sage10.6 实际故障与保持全部身份的修复

日期：2026-11-20。这里只登记公开运行故障、实际已达层和兼容修复；
未执行本地数学，未把新来源的静态检查记作数学 PASS。

## 1. 已观察到的实际边界

[run44747799006/job136327515753](https://github.com/Rogerhu12/math-research-public/actions/runs/44747799006/job/136327515753)
使用 source `632cef5af919da67776803cd36346a5cc3941363`，
在2026-11-20 14:57:17 UTC的数学进程第3981.55240897秒失败。
它已完成原 cube、低权紧缩、306整环和全部原 maps；
maps result SHA256为
`bb5efdd4e44b0b3d2acdda5fb11297a6a0927045b4d602a393e3bc41dcba4247`。
完整原始日志529716 bytes，SHA256为
`03a26f5acce7039c120e060fc14c0caf1fd9a86faafc504f5c615c972fd16f67`。

随后第一张原图的 `OriginalArtinianNormTools.__init__` 在旧第105行
调用 `self.k.absolute_degree()`；固定Sage10.6的实际
`FiniteField_givaro_with_category` 没有这个方法，抛出 AttributeError。
原1530长度/非Fp范数预门尚未开始，最终范数预门及消费者 result
均未产生。故不能把前面的 maps 回执写成厚范数、四 E 或原 shadow PASS。

六P首入口 [run44759336052/job136367382447](https://github.com/Rogerhu12/math-research-public/actions/runs/44759336052/job/136367382447)
已于15:02:53 UTC在 source
`da34ea30adb8e8a8f9e6e898d2f5f3ff559fe23e` 启动，依赖同一旧初始化门。
为避免执行已定位的同一错误，曾请求取消该实例；GitHub取消接口
返回403（当前PAT无该操作权限），未成功取消，不能登记为已停止。
修正后六P入口改用独立固定运行组，旧实例仍保其原来源和实际状态。

## 2. 为什么替换不丢绝对次数门

Sage的[原生Givaro接口](https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_givaro.html)
规定其 `degree()` 为原生有限域在素域上的次数。
但[一般有限域接口](https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_base.html)
提醒某些多项式商塔的 `degree()` 可能只是相对次数。
因此修复没有无条件把一个方法名替换成另一个：

```text
n = int(actual_field.degree())
p = actual_field.characteristic()
n >= 1, p > 1
actual_field.cardinality() == p**n
```

这在同一个已构造的原域对象上严格认证 `[k:F_p]=n`。
若某对象只报告相对次数而其基域非素域，完整域大小等式不成立，
仍然拒收；不另造域、不另选根，也不改变原omega或实际常数嵌入。

基础厚范数的原k门仍准确为 degree=2 且cardinality=p²。
闭点读者以集中 `native_absolute_degree` 在原来的七个位置支付此门：
完整矩阵编码、原多项式商的native模型、Fp系数收缩、Frobenius复合指数、
原残域绝对次数等式。原polynomial.relative_degree、实际forward/backward
两向返回、`[κ:F_p]=[k:F_p][κ:k]`、全部闭点次数/厚度和原q-Frobenius
均保持原值。最终shadow消费者已有完整域大小p^(2degQ)门，
现在同处核 `degree()==2degQ`，仍是该实际native残域。

## 3. 实际修改来源与公开验证

| 数学源码 | 当前 SHA256 |
|---|---|
| original_ys_artinian_norm_tools.py | `f604ae5f862519f5ccdce609a78ef05866fd85ae81ea699fb1de06f47b550714` |
| original_ys_closed_point_tools.py | `6bcc6fd6c59d7b6d0ecd6db7a28c24d6b1bd68d0fcd166bf66a53a519e676296` |
| original_ys_normalized_shadow_consumer.py | `96ca1132d56265f8a6912d3eddb7324f40504eaedda0b250a324801895b8172c` |

| 公开入口 | 当前 SHA256 |
|---|---|
| rank2-sha-original-artinian-shadow.yml | `4652d981e73bd6ab18b2d574ed4b3e21dc040c255340a2c17c12318048ccda20` |
| rank2-sha-original-ys-consumer.yml | `5337cbb4520b0fc07216481f4e6ab6d77bc4c8d7c140a542ebe5e15b1306e772` |
| rank2-sha-original-ys-closed-local.yml | `a149b0d6641062a3668731d7f4c61868450726a4f0e7793a4844d0cd58d17319` |
| rank2-sha-original-low-p-divisors.yml | `13786e091c6ab6dd910838399dcdca44aa0b6aa41d5803605cd86c02802a663e` |

host/producer原显式源清单已含这些真实依赖，运行时重新记录每份hash。
workflow补齐直接使用的依赖触发路径；修复后的Tate、closed/local和六P
使用native-degree固定组，让修正来源能独立开始。
所有组仍cancel-in-progress=false、每job360分钟；没有借新提交改变旧实例来源。

root核故障全文和最终边界并核全部增量；global实现闭点集中门并核
其每个实际用途，theta交核相对/绝对次数、原嵌入和Frobenius。
本地仅AST、JSON、YAML、日志与hash检查；新门仍须公开Actions实际执行。
准确新source/run/job在R931§12和HANDOFF随建立补记。
