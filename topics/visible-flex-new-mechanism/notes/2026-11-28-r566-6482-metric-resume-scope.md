# B030：从真实 6482 的未完 metric Jacobian 入口续算

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。
消费 [d59fa→6482 自然终态](2026-11-28-r566-d59fa-to-6482-natural-terminal.md)，
run `46119106791` / job `140899461067` 的唯一完整 FINAL。
新范围不重启旧 d59fa，不补已经判败的旧 trial，也不改原物理/metric 目标。

## 精确入口

保留 q `6482fbfda68f034db9b23bbb47a3e0103f24368cece129059c21e7b2d5bde375`、
已接受 eta `.195138934664774`、准确 g=0、metric 阶段、原 trust
`.45050811767578125`、working epigraph `.195138944664774`。
870 coarse / 1742 required fine、1943 physical peaks、695 working rows 原样
保留；原已合格 fine 仍是 1724，不能把其资格扩到 1742。
当前完整 required value 库及 3093140 scalar rows 已付，故不重做选行 baseline。
当前两 pending 列表均空；后来有新真实 witness 时仍按原交换规则消费。

真实 H 为 82 维、packed LDL 3403，metric row signature `505f8cbc…` 与
22 个非零 pending frozen multipliers 保持，完整 QP 锚和梯度随输入保存。
阶段/行函数含义改变时仍由原 helper 重置，不能把同一 H 换名当另一阶段的 H。

## 未完工作与 trust 语义

源 outer15 是第16次 backend 入口，在构造完整 J 时达到科学时钟边界；
已经付了20个方向块和1个 working value，但只有15个完整J与15次 native/QP。
响应数组和完整 J 没有保存，故新范围需要重建当前完整 J；旧20块仍计旧费用，
不冒称恢复了其矩阵，也不做旧 identity/方向探针。
完整旧 native workspace 同样不存在，恢复的是实际 H/pending，仍只作为
原新物理 QP 的启发初始化。

没有自然 backend return，就不满足原“无接受、无pending、且outcome非空”
的 trust 收缩分支。新入口保持原 trust，并保留 post-backend 决策尚未完成；
后续真正返回或交换后，继续原循环的原 trust 判断，不补造一个零接受结局。

## 拒绝分支及历史未执行队列

末369e试探已经完成coarse/fine/nested和876/876定位，真实eta
`.19780607039034218`更差，保持拒绝。它没有待补localizer，不作为新seed。
更早309b8的已付4465和未执行8635仍留在绑定的原
`request-r566-native-d59fa-known-violation-20261128.json.gz` 中，哈希
`f4129275801f71c0be36a860ff8eca8409967056b499b5b336dced8e566ab86a`；
新输入记录该完整来源及原未执行队列哈希，不删除、不重付、不改成已闭。

## 不变的后续真实接受门

正常 outer、callback、工作回溯、auxiliary lift、coarse/fine/observed localizer、
nested比较、原物理盒、margin与metric改善规则保持原代码。native raw iterate
与 retained physical best 仍分轨；epigraph lift不算eta改善，有限定位不算
连续全峰/全对reach证明。
新科学沿原2400秒时钟，保留30秒终态输出；一段结束继续消费真实新终态。
全部旧费用、未完20块、精确当前库与H/pending随必要压缩stdin保留。
无固定g家族或README完成声明。
