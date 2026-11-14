# 完整均值范数 v2：保留原失败并修正区间再包络检查方向

原 run `43588192611` 的实际消费者正常记录了退出码 1，原 native SHA256
`fa68d99af4ae381a22d56f2a5f5b1a5b87b0af86316aec038e09595d9a4e31bb`。
它的前五个实际身份、完整均值、全 trial、方向定义及 7721 行完整性门已经
通过，随后在比较标量 flow 记录与 residual-row 记录时停止。此失败不是
原完整主体 run 或原完整均值收尾的失败；这些成功结果均保留且不重算。

原严格 source `fourfold_codazzi_correlated_mean_error_consumer.py` 先记录
每格完整 flow 的 `entire`，再以 `box_from_record` 重新构造同一区间，
最后把它再次记录为 residual-row 的 `response_mean_error` 或
`adjoint_mean_error`。Arb 的 midpoint/radius 区间 union 在重新包络时
允许增大半径，即使工作精度为 320 bits，radius 的有向包络也不能
误当成不扩张的逐字节恒等操作。

实际第零格的 response flow 端点为约
`[-1.19430881276846348e-5,1.19430891750719157e-5]`；原 residual
记录则为约
`[-1.19430881561063443e-5,1.19430892034936252e-5]`。
它在两端各向外扩张约 `2.84217e-14`。adjoint 第零格也有相同量级
的重新包络扩张。这些均为原成功 native 中实际已存在的字节，不是新改结果。

v1 错把包含方向写成“原 flow 区间包含重新记录的 residual 区间”。
新增独立 v2 source 仍要求原 7721 个身份、精确区间、全部独立 mean
方程与原 native SHA 完全一致，并逐格明确要求：**重新记录的 residual
mean 区间必须包含从原 flow 重建的区间**。范数使用两个区间的 union，
所以误差预算只可能增加，不会因为此修正减小。

原 v1 source、原 v1 manifest、原失败过程和原失败 native 均不改。
新的 v2 worker/manifest 指向独立 v2 source；原两个数学输入 native
以及所有原科学 source SHA 保持不变。新的数学消费仍在公开 Actions
执行，并记录真实新的成功或失败；它不重算任一已完成主体格或标量流。

只有新实际成功 native 才能提供完整范数。连续逆、真实响应方向、
ac1 到连续背景的算子变化、全高输入反馈及非线性背景费用继续保持未付。
