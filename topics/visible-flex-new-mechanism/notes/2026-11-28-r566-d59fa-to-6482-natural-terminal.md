# B030：已知违反早退后，真实 d59fa 到 6482 的自然终态

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。
run `46119106791` / job `140899461067`，source 与公开运行时 pull 均为
`41cf3c8fe34fb5cde32a7223b0c39b0450f02727`；私有规则 pull
`ab476225264f1086dd2c00fd80dcfa7a874ac8f1`。原规则 blob、队列会话通过。
06:59:33 UTC run 启动，科学 07:00:02.293880→07:39:33.131748；
07:39:35 自然 `completed/success`，数学状态仍为 cooperative clock checkpoint。

## 1. 实际保留态及真实改善

新科学 `2370.041308173` 秒，实际 **4 metric + 1 restoration 接受**。
末保留 q 的 binary64 SHA256 为
`6482fbfda68f034db9b23bbb47a3e0103f24368cece129059c21e7b2d5bde375`，
原 accepted eta `0.195138934664774`，准确原几何 margin 状态 g=0。
这是真正从源 d59fa 的 eta `0.1966187824246114` 改善而来的已接受态；
未把 raw optimizer trial 或辅助 epigraph lift 算作改善。

末已合格 fine 是 **1724 个半径 × 3072 角**，包含实际完整观察峰定位；
当前库已扩为 870 coarse / 1742 fine 半径、1943 physical peak orbits、
695 working field rows，原统一角数 1536。1724 的资格不会自动转给新增 1742
库；末 `current_complete_library_values_known_for_retained_q=true` 仅表示当前
完整 required 值库已付，不等于新 fine/峰定位全资格。
physical pending 与 working pending 当前均为空。

末 phase 为 metric，当前 working 可行辅助 epigraph
`0.195138944664774`；actual/proposed trust 均 `0.45050811767578125`。
已合格 fine 坐标哈希为
`6f6fccdd3832ada60284e857a2cc46593e1be5379f9527a048f6b8a52e4e977b`；
当前 required fine 哈希为
`6161c6aced776c8c610db72065b426b3ae16a71a40cc1e369b8bec1295cf4766`。
全部旧/新增径向坐标须继续精确保留。

## 2. 末试探已完整拒绝，没有待补局部化

末 callback trial `369e5c495bd1b3e1100ebcdb4f74c518fcf56371ab1a4c68318692c8e4ea7bf9`
来自 outer14。它 coarse/fine/nested/localizer 全部完成，876 个候选全部闭合，
7326 次局部 point objective；真实 eta `0.19780607039034218`，几何违反为零。
它比保留态更差，所以 **accepted=false**；末 raw backend 的辅助数
`0.19422043784085538` 不能替换真实 eta，后续 lift 也不能算改善。
这个 trial 已完整拒绝，不存在为它追加未闭括号的任务。

源 309b8 的已知真实违反早退策略按声明执行：0 旧候选重放，0 个源剩余括号
新执行。其已付 4465 个峰与 **未执行 8635** 个括号，仍由原绑定输入
`request-r566-native-d59fa-known-violation-20261128.json.gz` 保留。
剩余队列 canonical SHA256
`293358a9cbe347606c181be21fc06a4f22e7d9250ec8566a54c37df6ef38773e`；
没有把未执行改成已闭，也不为已被反例拒绝的候选继续花费。

## 3. 准确在途位置、H 与费用

原循环完成 15 个 outer 后开始 outer15，已进入第 16 次 backend 调用，但
尚未有第 16 次 native/QP。该次构造新 Jacobian 已付 **20 个方向块和 1 个
working value**，完整 J 尚未完成。证据是 outer14 的累计 1002 blocks 加其
当轮 90，末累计 1112；完整 J 由 14+当轮1 得到末15，未增加到16。
这些未完成费用计在总 elapsed 中，不能冒完成；响应矩阵没有输出，下一次
必要完整 J 重建也不能假称旧 20 块已可直接恢复。

完整累计为 15 J、1112 direction blocks、46 coarse、13 fine、13 完成定位，
55671 个候选全部闭合、511366 次 localizer point objective。
工作 J 秒数 `479.0775690790006` 只累计完成调用；最后不完整部分仍由总
elapsed 和已付块数承载，不能从 elapsed 中剔除。

真实 native H 为 82 维、packed LDL 长 3403；metric row-function signature
`505f8cbcb0a22bc114da97754d0903cee340381ff6237c868c947f04e71452c5`。
pending frozen-multiplier secant 保留 22 个非零乘子，完整 QP 锚/梯度/行身份
随 checkpoint 保存。上一次实际 H 准备使用 21 个非零旧乘子，不能混为末
pending 数。模型身份仍为
`8a1abe70f785c8c1d8e80b884aa58299598846c716c1be63b0d7b3e9421414a7`。

outer15 没有自然 backend return，也没有完成 post-backend trust 决策。
不能把“当前没有接受”偷换为原规则中的“无接受且 backend 自然返回”并缩
trust；从原 `.45050811767578125`、当前库及实际 H/pending 恢复未完入口。
完整旧 native workspace 和 J 没有保存，H 仍只是原物理 QP 的声明启发初始化。

## 4. 可重取的真实身份

源请求 gzip 405111 字节，SHA256
`f4129275801f71c0be36a860ff8eca8409967056b499b5b336dced8e566ab86a`。
原完整 job log 22292289 字节，SHA256
`4351305365b945a76a859a53e0c818837842d5295a8ea01df926b5e06af6c713`。
唯一 `WORKING_ROWS_FINAL` literal 528713 字节，SHA256
`9433333053c92fcdbdfcdf464dc93834ffc4f6f7d635be41147b737c4642b534`。
后续输入消费这一完整 FINAL 以及已付当前 BACKEND_START 的 3093140 required
scalar rows，不重跑旧 retained fine、旧完整定位、旧拒绝 trial 或旁支。
可重取原日志不提交；必要的精确 q、库、H/pending 与完整费用随续接输入保留。
