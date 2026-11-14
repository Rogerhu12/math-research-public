# request17：真实下降 warm 与首次极小非零高度 native 失败

状态：真实执行终态，未有新完整联解或新非零尾接受。所有数值来自本仓 [run43598917532](https://github.com/Rogerhu12/math-research-public/actions/runs/43598917532)，源 `4b8b2bfdd417f76574dcc2a8e2353c4c2dce3e21`，job132459290659。

## 保全身份

完整 artifact14116526155 为25,507,381 B，ZIP SHA256 `5a0bddbd39739ed94e382d6a8b7fd74dec3ca19febbf9369d20667b9506e8242`。root已取回并逐字节保全限额内输出；[publication](public-actions-43598917532-1-coupling112trust/publication.json)列出所有输入/输出SHA及补出版来源。原bot在上传artifact后已生成本地提交9773f01，但推送遭并发main CAS拒绝；此提交不是已发布结果身份。

三冻结数值源仍分别为 constrained_collocation `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8`、trust_warm `5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2`、trust_response `7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78`。

## 1. 三次确实下降，但离原方程容差仍远

[完整warm记录](public-actions-43598917532-1-coupling112trust/constrained-warm/driver-status.json) SHA `2bcea7d39520da786a2dd649efce2b6afae928405f2abf3bf40379e1135b30c6`，总633.052012176秒。三个模型的算子/伴随及原方向检查实际通过；每次原node/mid/两RMS域通过后才保存。每个模型内Wr冻结；下表的相邻行Wr不同，不能把不同行merit直接相减当同一目标的下降。

|模型|实际阻尼|alpha|同模型merit前→后|实际/预测比|保存后原physical collocation max|
|---|---:|---:|---|---:|---:|
|0|10|2^-14|44.44787720229487 → 44.44721499298322|1.0000162700833308|.007110550938076629|
|1|30|2^-15|44.44736933003768 → 44.44719408791289|1.0000371333209068|.00711054767509256|
|2|90|2^-15|44.44724777852967 → 44.44715711179736|1.0000347877000708|.007110547307418288|

各LSMR均80步、istop7；正阻尼normr包含罚项，不能仅据它非零断言‘再迭代就能通过’。最后完整affine BC为9.606803272021844e−8，常数ODE与左入口残差均0。warm的success/new_coupled_finite_acceptance始终false。

最后 [warm-003](public-actions-43598917532-1-coupling112trust/constrained-warm/warm-003.json.gz) 的SHA为 `5d1c452291099ad18b1a619ba3794614b04a0c620b8ed0f28887a84731ef7886`，4,702,259 B。前两站SHA为 `5fcc82626f6d316df1ec7a0d96ce1ec22f5fdd1a3f828b82b3a5e46176e12410`、`c955cfb0e409582fc2303e0c29815a2be89d60faad618ee029e073b9ab9295a3`，也完整保全。

## 2. 该实际warm上的完整FD通过

[实际response-check](public-actions-43598917532-1-coupling112trust/physical-response/response-check.json) SHA `2cd0dc68993ee5b4391fc18d96729ea7a2aaacbf9764923853844035d0866bbb`。20.403676473秒，原三档中心差分/Richardson最大相对误差9.51710770488038e−10，通过原5e−5接口门。这一检查明确用原已完成真T112零H/J作affine图；没有声称当前非零H已真求。

## 3. 首次真实非零H在native尾初始化就失败

fullDN阶段1000.061549704秒，其 [driver-status](public-actions-43598917532-1-coupling112trust/full-DN112/driver-status.json) SHA `2f951f3072922876281236fab6a003a51722a49789fdaa6f889f3fd7dc37d594`；outer_history为空，尚未进入前缀inner Newton或新band分解。

[原native trace](public-actions-43598917532-1-coupling112trust/full-DN112/true-tail_trace.jsonl)记录13:28:33.638Z首次call1，jacobian=true、audit=false，完整112项非零高度传入；第一项4.1760413061806626e−17。原MaterialTrace本来就设置P[:,0]=0，故不能以z0均值泄漏为由把当前已保存非均值扰动归零。warm、fresh FD与native请求保持同一H。

13:43:22.412Z iteration0 norm=13414069.96827908，minA=.999999999975931、minD=.9999999999999858；13:44:09.985Z校正记录chartCondition=1.3312263223101865e60。原10档步长1至2^-9全部被momentum D/S/A guard拒绝，位置均rawCell0/rawSegment7、stage13或14。13:44:50.600Z报multiple-shooting line search failed。

[原失败尾包](public-actions-43598917532-1-coupling112trust/full-DN112/true-tail_0001.json.gz) SHA `ebe8932a7ba1a995f49b365344e795714bc0fdfccc606765cc69944b56a6b7a0`；原iteration/checkpoint包 SHA `e996f37aa4eb7cfb0bb8b5bb912f594af794d16146240ee6db114c22eb55de7d`。它们保全失败状态，**不是新的成功非零H锚或完整J**。没有outer联解、最终audit、after_accept或新闭面。

当前分别分析warm的真实RMS域限制与native冷启动/实际完整zero场的初始化路径；不把H阈值截成零，不用失败response替代真J，也不原样重跑699/fullDN。

## 4. 实际发布竞态已修

bot的原循环已去掉非快进次数上限，但这次服务器返回的是 `remote rejected ... cannot lock ref refs/heads/main: is at ... but expected ...`；旧字符串分类漏掉此种并发CAS推进，误当其他错误退出。root已补上这一明确并发形态，后续立即普通pull --rebase/push直到成功；其他权限或保护错误仍不伪装成并发。未强推，未重写任何科学输出。
