# R775 原始断点的实际观察与续接

状态：运行状态与已有产物读取，不是新的数学定理。会话 serre-public-astra-20261115，2026-11-15。

旧公开 run 43631335355 的源提交为 00295b27a3f7367028ccee84eb867b5aeadc7540，2026-11-14 20:38:13 UTC 以 process_exit_code=124 结束。原数学核心在80分钟预算耗尽前保存了阶段，最后的verify步骤因complete=false而失败。

原artifact ID为14130299697；ZIP SHA-256为15961ced472e2a7633c353e86522a90553e0eb615410759cd19df913a4957540。下载后检查了full-outputs-manifest.json的SHA d763da2a2ee83b0474effa4deafebe3e0b689bc109c34ca43f3fa196ae43e46a及全部23条文件大小和SHA，没有运行数学核心。产物共10841680 bytes。

| 已有阶段 | 状态 | 实际读取 |
|---|---|---|
| R775-basis-M2 | complete | rank146, processed_candidates480 |
| R775-basis-power-2 | complete | rank418, processed8064 |
| R775-basis-power-3 | complete | rank690, processed30976 |
| R775-basis-power-4 | complete | rank962, processed51072 |
| R775-basis-power-5 | complete | rank1234, processed71296 |
| R775-basis-power-6 | partial | rank1486, processed18432 |
| seed-images-000..011 | complete | 每个40个det陪集 |

核心仍为scripts/R775_original_K_defined_RR_bases.py，SHA 8b02496a1809e1f11e90bad84df1a4fa3a39ac6ad615f7871115b0988d2af4ee。只修改运行预算、已成输入的resume描述和包装元数据核对；原configuration严格匹配，不给旧状态换数学来源。续跑预算300分钟，步骤310、workflow350分钟。最终M6/M12的694/1514维基和非零minor尚未产生，不能预登记。

根README第15条于137c5a877改为不保存可重算数据：后续只提交脚本、参数、run、摘要与输出SHA。当前任务间所需断点使用最短1天的临时artifact，消费完成后删除；原始表不放Git/Release。旧artifact当前存在，可直接续接；源码、参数和哈希继续保留。

执行环境04:55 UTC起不可用，终端pull/push失败；小文本API是根第8条明确备用机制，不能把它记作实际pull。旧未推分支不在本环境，也不再寻找或引用。
