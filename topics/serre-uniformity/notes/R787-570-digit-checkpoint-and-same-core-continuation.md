# R787 — 570位真实断点与同核续接

2026-11-16。状态：**公开执行的中间断点；原函数关系、A.1与高度未完成。**

## 已结束的实际执行

run [43809321438](https://github.com/Rogerhu12/math-research-public/actions/runs/43809321438)，job133107261923，source834098cabed1b51be700d9f0ce87086ff44363fb。
原数学core 93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04；
wrapper42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6。
预算120分钟，实际core以BudgetStop退出；run的process_exit_code=1、error=null，core receipt明确完整阶段仍可续接，不是没有core receipt的外层超时。

原artifact14204698566，serre-global-R787-original-power5-function-relation-43809321438-1，
458546401字节，SHA256 1c044998efa94381a6f9c837b8143965dd4916d120fff4a5e296540139da77f6，至2026-11-17 07:20:53 UTC。

## 实际保留的断点

|文件|字节|SHA256|
|---|---:|---|
|full-outputs-manifest.json|430709|20d5e10ff8a9503f95731af63481d30d9365d8c22bab9ee1fcc3b547e95ba818|
|R787-prime-1000000753-dixon-00000570.json.gz|80520179|d97acf14475746b520cc94c65ac2717d6f9033a28e43e52262db1b18075adb14|
|dixon-checkpoint-history.json|133262|00c503b115e2fa36d4929b8cf056f58619a6bd79886b49ff91f5e8388d110076|
|dixon-output-compaction-receipt.json|761|3b70bf85ceb057afa40278467790cf4d6455ff18ce2facf3cda54fd022662d33|
|core-receipt.json|308|ec4673e2b51e4b3e47b2fbea4ac75c34c7923e90d47ab3f80110cf35f426e8f7|
|run-receipt.json|542|fe677d9367d7a463a24051b84ae007a17c848275ccfe61b533476a8a477f0fca|
|R787-retained-producer-inputs.tar.gz|123713383|2f4371c94e36372b2eeb9291d75479ccbe2432abe741dc9ecbebab78e9046e92|

实际history有570条，最后一条的prime/digits为1000000753/570，文件名、字节、SHA与manifest及compaction的latest_complete_lifts_retained完全相同。压缩清掉的只是25份旧完整lift；其元数据仍在history，其它完整数学阶段未删除。旧518全部56格与早先拒证边界直接继承，不重算。

上述读取在本公开run43826442405/source5a21f9d9de5686e80bd029bf39749e2900857515的纯IO完成：11个必要小件、12次Range、265868实际传输字节。只对选择的小件重核SHA，**没有把80.5MB lift或全部ZIP说成已在这次读取中重哈希**。完整lift将在同核消费者恢复时读取并核定。其小源包e72d1a1a保于一日artifact14206388855，原大断点仍取原producer。

## 本次续接

只把原request的resume改为上述真实run、source、artifact与manifest。
新request为3722字节，SHA256 00802d0d68f925a53f523bcf9e080964248a307944c9eaf820d3b83d361d8115；
120分钟预算、reconstruct_every_digits=8、原producer身份、core/method/proof/两下载helper和全部原规范均不改。
同一脚本从真实570之后继续，不回545，不把dual370或七小L条件并入这条原函数关系。

本次恢复发布在真实pull/两README检查后dispatch serre-p41-original-power5-relation.yml；
新run编号由实际启动回填HANDOFF。未取得新的原函数关系、候选接受、原点坐标、eta或高度。
