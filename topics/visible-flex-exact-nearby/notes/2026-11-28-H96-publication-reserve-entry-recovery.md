# H96 首次公共入口失败与同七目标恢复

日期：2026-11-28 UTC。责任会话：`visible-exact-astra-b0d5a16-20261128`。

## 已观察到的完整失败身份

首次 [Actions run 46122740303/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46122740303)
的 job 为 `140910568178`。完整 job log 是 `218380` bytes，whole SHA256：

`3e8c0d842359105c54cc8703be492523310c82708b0be6d6b2558bf27d0d4af6`

在 `2026-11-28T07:47:01.9029471Z`，日志实际报告：

```
File "<H96 complete public worker>", line 112, in main
File "<H96 complete public worker>", line 22, in require
ValueError: original actual topic capacity rule
```

整份日志未加入仓库。这里保留真实 run/job、完整日志的 bytes/SHA 和准确
错误位置，不用缺失的 actual 数值对象替代科学证据。

首发清单位于不可变提交
[`cba22d03038b41fd02bc6858b52b39f796492ed1`](https://github.com/Rogerhu12/math-research-public/blob/cba22d03038b41fd02bc6858b52b39f796492ed1/topics/visible-flex-exact-nearby/notes/2026-11-28-finite-trial-height-complete-inputs.json)，
`61916` bytes，whole SHA256：

`0bf3e4abe612c744cba56cfb2161528cb34171351414885d2761349e61a70073`

## 原因与修复的精确范围

H96 继承的完整 RHI public worker 在执行入口保留了
`RESERVE=120000`，而 H96 已声明的 publication reserve 是 `210000`。
上述 `require` 在创建科学状态及启动科学 child 之前检查两者相等，所以
这是确定的执行入口失败：科学 child 未启动，七个新数学目标执行数为 0。

唯一公共 worker 行为修复是：AST 对原全局 `RESERVE=120000` 赋值做一次
受计数保护的 `210000` 替换。原 topic limit、容量计量、完整输入恢复、
README 定时 pull、真实 failure 保存和非快进 rebase/push 循环保持原行为。
manifest generator 新增静态检查，核对实际编译后的 `LIMIT/RESERVE`
与所生成 manifest 的 `topic_maximum_bytes/reserve_bytes` 完全一致。

完整准入重建通过：`114` current inputs、`51` historical inputs、七目标。
本地没有导入数值库或运行科学目标；此前九项 Fraction 比较未重算。
proof、math、科学 owner、carrier recipe 及数值参数均未修改。

恢复后的 [current manifest](2026-11-28-finite-trial-height-complete-inputs.json)
为 `61916` bytes，whole SHA256：

`60f1e7ca8d83f986d7020e786a0f1ed7dd1958634039c5bdb7c5952a28ea1483`

工作流绑定该新 SHA。恢复继续首次尚未执行的原七个完整目标：canonical
height96、true waist-Jacobian L2 upper96、reference height96、actual-cap
height96、actual-cap joint radius、height-reduced phase96、reduced-phase
joint radius。此记录只准入未开始的原计算；它不宣称 actual 数值成功，
也不把任何 prefix、载体恢复或入口修复算作课题完成。
