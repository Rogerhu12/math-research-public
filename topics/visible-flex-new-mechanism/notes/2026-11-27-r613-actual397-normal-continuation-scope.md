# R613 实际397正常接续与独立固定E参考的分界

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

原337续算在60次声明上限自然返回，最后一步仍接受；
完整原收据见 `2026-11-27-r613-normal337-sixty-step-terminal.md`。
本 scope 从**实际397**正常继续原完整 S 方法，不把迭代上限写成驻点。
它使用原末态1130q，`22713 B`，SHA-256
`d76a590766b2323698053321ad84608f17f110c1711c105470d2b876b4920875`，
`amp=1e-5`、`H=.5188903877153482`、下一damping `1e-14`。

## 来源和唯一新入口

来源 run45899589237/job140181814100，commit
`59ef89bf6dd08df066fc6b8ffe4be8eec1df8207`；原337 wrapper SHA
`be14efea5d19f5b787ff4190d24e2d50b7de67989b2e0c23096e022b3b7e8cec`。
原完整 log `2407243 B` / SHA
`cec44a65e69f6ad38d002319c7c185978027208f60b98f6b36df84b3db27367b`，
原 FINAL `102883 B` / SHA
`3068d197a30082626d95c8827d3abf2af57493837b07929e7441deb5a3cf3fcc`。

新入口 `scripts/r613_full_position_resume_397_20261127.py` 仍只绑定并直接调用
原 `r613_full_position_height_20261127.py`，其 SHA保持
`6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0`。
新内容只有实际输入身份、schema和本次入口source receipt。
原模型、solver、完整J、QR/SVD、全部奇异方向、line search、物理step limit、
checkpoint、fine及成本函数全部直接调用，未复制修改。

新入口先核完整前一 scope input，再递归取出原 `reconstruction_source_JSON`。
这次需要穿过前一normal337输入的一层 `previous_scope_input_JSON`；
没有假设它顶层仍直接含 reconstruction。
复用的原重建文字仍是 `31425 B` / SHA
`14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee`。
所有原内口、canonical512高度、force、67knots与core链保留。

新原输入 stdin 为 `157609 B`，SHA-256
`79e6d6ce708687decd47fb8eb7a9668f8ca2ebf2351b2f3109fd571c6d692f9c`。
它逐字嵌入前一 `108233 B` input，SHA
`0d8e87ebab7135065c153c6c285b9d64fdff693dcd49a4c0bc20bdd9869fde22`，
并继承所有 prior ledgers。新本轮 source ledger准确保存4520.668522229001科学秒、
205trials、60接受/145拒绝、60J/67800列/60QR-SVD及全部其余计数。
此前2961.020285526秒、compact和更早科学费用不丢失、不再次计作新增。
原FINAL没有保存QR/BFGS内部态，此处不会伪称恢复；必要新分解照常计费。

## 完整原范围

保持原950×256工作网、奇频1…127的128个位置坐标/半径、
完整 `121600×1130` J、4096行分块完整增广QR和小R全SVD。
原1130参数、全部原径向点、每个compact span和完整 core六jets/参数链不删。
必要 dense/connector/core/height重建照常计费；不重做原inner DtN，
也不把旧fine、R606/R615或方向诊断作为新入场门。

新实际末态按原驱动做一次1728×512 fine、两种原实际位置步长，
所有D偶频0…128、完整At/M同步观察及共享一次系数遍历的R606/R615；
R615仍覆盖fine全部奇频1…255，并保留其条件/非连续证书边界。
仍是60次/5400科学秒/240秒fine reserve/job100分钟。
同一串行height concurrency group，不cancel原运行。
原solve从真实起点397出发，下一实际接受号398，最多正常推进到457。

新request/workflow为
`computations/request-r613-full-position-resume397-20261127.json` 和
`.github/workflows/visible-r613-full-position-resume397-20261127.yml`。
共26项source/workflow绑定，包含前一337入口/workflow及新397入口/workflow。
本地仅验证JSON/hash、全部sparse-checkout覆盖及AST；原loader/main的AST
除调用新输入reader名字外完全相同，未导入或执行科学模块。

新入口 `6075 B` / SHA
`bc4cf1bce2f62a67eac633deedf12a3fa9ba75b1758042b32c9354c87d802ff3`；
新workflow `4643 B` / SHA
`1f35c394491d8953c3e9ef7dd531dfc8bc50d04de887aeec3da16635313c2559`。
发布者按真实pull更新request中的规则已读commit，科学stdin保持不变。

## 同时冻结的R618参考

并行R618固定E增长路线明确选择这份实际397完整q、amp、H和原重建定义作为参考。
本normal scope继续原方法时，其新的H、q和设计E可按原solver变化；这些后来状态
**不会**替换R618已经选定的完整连续目标函数。
若未来需要另选目标，必须作为明确的新对象和新身份，而非暗改旧 E。
当前正常下降和这个小幅固定E参考都未达到题目宏观族、固定持帽位移或完整reach标准；
原open中的后续工作继续。
