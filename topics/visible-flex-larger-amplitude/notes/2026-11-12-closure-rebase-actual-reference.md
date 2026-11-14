# 将完整实际节点高度接入已付真实46列

2026-11-12，exact_closure。

`computations/closure_rebase_actual_reference.py` 是独立入口，用于
实际新有理深g的depth12/far225完整响应。它只将保存的node12
高度Q作为准确binary实数边界，再以同一真实线性算子建立参考。
这不把保存的径向轨道、动量或节点位置当成已经认证的实解。

入口要求实际求解已收敛、有完整checkpoint和endpointCanonicalTrace，
请求中全部M个高度及trace中全部M个Q/Xi均存在。M不能超过46，
物理频率必须为2j。前M个参考高度全部保留，其余参考高度选0；
允许校正的低深参数仍有完整46维。

为复用R29真实列，入口逐项核对原source ready与新ready的数学
模型键、全部实际几何参数及完整160行浅层冻结表。固定warp、
源revision/SHA、深alpha65/64、真实cuff参数和head fingerprint
全部相同才可继续。真实R26外半径与旧名义cut不在这里作同一性
替换；保存Q只是本参考问题在真实node12上的指定高度值。

对每一真实浅端非零增益G，准确参考幅度为Q/G。程序用保留符号
的上下端点包围该比值，逐cell重新计算plateau2强范数、完整R23
源/mean上界与far角宽转换。没有重新积分几何或线性流，也没有
只复用M列后以零填充缺少的高列。所有46个列组的SHA均检查。

## 已执行的入口一致性检查

用原q003实际响应作为新入口的同输入测试，会话31367正式exit0，
resource亦记录exitcode0，1.90253秒、峰84300KiB。
`closure-rebase-q003-check.json` 中全部213行强范数、源界、mean界、
far参数界及转换常数与原plateau2参考逐值相等。比较结果为
`closure-rebase-q003-check-comparison.json`。

```bash
python computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-rebase-q003-check-resource.json -- \
  python computations/closure_rebase_actual_reference.py \
  --columns notes/2026-11-12-closure-real-linear-q003-low46-recovered.json.gz \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --new-ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --new-response notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-response.json.gz \
  --out notes/2026-11-12-closure-rebase-q003-check.json
```

这次检查只支付入口与已知参考的等价性，不是强H求解成功声明。
实际强H作业完成后，改用其完整ready/response并使用新输出prefix，
再由同一Green重新核销盒与真实深图反馈。新的强参考能否通过
这些门由实际输出决定，不能沿用q003的小幅结论。
