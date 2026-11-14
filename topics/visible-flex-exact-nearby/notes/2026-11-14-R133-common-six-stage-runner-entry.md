# 最终 ac1 中心的公共六步 runner 入口

2026-11-14。**已完成可执行恢复入口；实际检查了已成功重放的完整六步和全部分片。** 本条不是新一次六步求解，更不宣称精确 PDE 解或主体逆成立。

入口为 [fourfold_codazzi_final_replay_chain_runner.py](../scripts/fourfold_codazzi_final_replay_chain_runner.py)。它只编排已发布的 `final_replay_first_accept`、`final_replay_stage`、`preserve_accepted_checkpoint_v2` 和 `replay_historical_identity`；所有数学参数逐字取原 [六步清单](2026-11-13-R133-final-moving-replay-chain.json)，不另造近似 seed。

前两步只能在原 producer 已打印完整 accepted 检查点 SHA 后停止。接着使用该检查点的**全部节点、状态及径向导数**重建原 SciPy Hermite 插值。原 accepted SHA 必须相同；第二步及最后一步还从完整重生数组重建历史 gzip 字节，验证全科学字段、初值位模式、所有片的 SHA 和长度之后才可恢复历史元数据。第三至六步必须保原 finite BVP 成功门。任一步失败都会保留实际新文件和失败记录，不继续套用旧 native。

运行时严格要求 Python 3.12.14、numpy 2.3.5、scipy 1.17.0、python-flint 0.9.0、sympy 1.14.0，BLAS 单线程。这不能保证不同硬件必然复现逐位结果，因此**最终身份检查始终保留**；它失败时产生的是待另行认证的新中心。

根 README 第14条的 runner 可使用：

```bash
python -m pip install -q numpy==2.3.5 scipy==1.17.0 python-flint==0.9.0 sympy==1.14.0
python -u topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_final_replay_chain_runner.py \
  --topic topics/visible-flex-exact-nearby \
  --work "$RUNNER_TEMP/visible-final-replay" \
  --out-dir "$OUT_DIR/replay" \
  --candidate-path-file "$RUNNER_TEMP/visible-final-candidate-path.txt" \
  --address-space-mib 6144
candidate=$(cat "$RUNNER_TEMP/visible-final-candidate-path.txt")
```

队列的 `python` 应明确取 `3.12.14`。完整 topic 检出已包含原 M128 索引及五片、两个 q 向量、原几何对象及其两个 NPZ、六步过程与两个重构清单。大状态、导数、QR 文件和所有候选分片留在 `RUNNER_TEMP`；`OUT_DIR/replay` 只接小过程/身份报告。消费器使用路径文件指向的真正 ac1 候选，不把重构清单误当数组。

同一 runner 中已完成的阶段可以继续消费；不完整阶段不会猜测退出原因或覆盖现有检查点。`--validate-existing` 只检查完整既有六步，不启动原 producer。它仍逐阶段核原输入/源/接受门及每片完整字节。本次实际使用该模式，六个历史索引依次恢复为 `45923b…`、`9891fa…`、`a6b691…`、`6c3bab…`、`5a3fec…`、`ac1d5b…`，最后完整6145节点、65状态、五片全部通过。

完整本次小报告见 [runner-existing-chain-native.json](2026-11-14-R133-common-six-stage-runner-existing-chain-native.json)。此报告明确 `validate_existing_only=true`；没有把它写成远端已执行、重新求解或已得到主体连续逆。
