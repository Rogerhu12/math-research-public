# G11 独立源的第二次真实内层门失败与433行回执恢复

这是G10失败/primitive修复之后的另一份独立source进程回执。原Gauss11/256错移角观察源并未完整成功：`polar-independent-G11-cache-exit.json` 记自然OS exit=1，1730.640628563秒，peak child RSS208580KiB。失败是side0、角索引170、外层角残差1.8918200339612667e−13、括宽8.881784197001252e−16，仍是内层material默认2e−13与外层5e−14的同类冲突。

原正式日志最后完成433/540个新径点；数组虽有437行非零，后4行不作为完成证据。新入口仅复用前433个正式完成行，余107行重做，逐行flush并记journal。完整观察源仍是668径点×256错移角，原G3共享128行逐字保持；没有改观察节点或为过门删除失败点。

新文件 `2ecf-polar-c2-independent-g11-resume-observe.py`，新prefix `polar-independent-G11r-shifted256`。G10恢复入口和 `2ecf-polar-tight-source-evaluator.py` 保持已登记字节，不以改动活动producer的方法扩功能。新G11consumer复用同一独立fallback：实际失败才收紧内层到2e−15、仍须外层5e−14成功，并对真实返回根分别付longdouble Gauss16/Gauss32局部primitive原位检查；失败则拒绝本行。

该新G11入口还显式区分原固定g状态与新的log-radius设计状态。后一种观察必须读保存的全部87参数，以a0 exp(B alpha)的同一个明确临时目标评估；单列metric-design计数，不能把设计状态误当原g，也不能把设计过程当固定g收敛。这只是消费规则；本条并未声称已有设计大场接受。

新恢复进程正在实际运行，最终源exit、完整哈希和第三方观察数值需结束后另行登记。原失败cost和进程exit不被覆盖，不算成任何LM尝试或接受。G11数据不进入G10的128/192角训练objective；仍需记录与G10实际径节点的交叠数，不能因为称“独立”就假定所有径点均不同。

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-c2-independent-g11-observe.py` | `0427a082dc7c795fb511c8048a20f090682be790de9a1d098938b2ea795d5284` |
| `polar-independent-G11-cache-exit.json` | `768f7e75b08bfd3da27946d358eeb77024b2aab3ebc35bf56d0163646b5c6d26` |
| `polar-independent-G11-cache.log` | `97fba158ed9664f4b11f211e544e35b8b2d65f2e341e59fc2ba97ccae7d07ece` |
| `polar-independent-G11-shifted256-new-jets.npy` | `8b54c048c8cd8c43219ba99e085bd555b64c2e73af8ef79cf938395c83b0b407` |
| `polar-independent-G11-shifted256-new-radius.npy` | `c05984d24fd7a2236681e44594186b992e2f2d9b774e769f197577a1a4b68b50` |
| `2ecf-polar-c2-independent-g11-resume-observe.py` | `13510aae185c0840293fb1957206be30cb27a285271ff82b66fac37f5682f4f9` |
| `2ecf-polar-tight-source-evaluator.py` | `5d91140712ca78df5bf8e62392ad9ddb86915a0b0197d7f3804d4d4a9fe4435a` |
| `2ecf-polar-c2-g10-resume-prepare.py` | `d0af059771db8d39b84eba498a73d3154872a5be69a3218dbea340e38f1cd1b6` |
