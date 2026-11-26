# h487 到 M48：完整 H 右预条件的独立受控 job

**状态：新执行接线已完成并通过实际语法检查，尚未触发或执行这个真实全半面 full-normal job。** 完整 77 非零列核及专用协方差证明已单独登记；本批不重跑它，不把该核的谱或误差外推到大场。

## 对照定义

原 H1 右预条件的 M48 run 为 `45847254548`，source `3046ad8c20d2d64c435ad9b0bd50cde5e31c0798`。新 job 不等待、不读取、不借用它尚未返回的终场；在同一个新 runner 从原公共输入独立重生 h487，按 R243 的准确 Fourier 零填充得到自己的 M48/N768 暖初场，再用完整三行 Gram 法矩阵右预条件完成一次真实求解。

固定参数为：基态 80/64/depth12、原元190和176的 h487、M32/N384/G6、800 LSMR、1 Newton、block24；新层 M48/N768、原487径向元、原G6、800 LSMR、1 Newton；完整H预条件器 eta=1e-6、assembly block8，物理 lambda=0、LSMR damp=0。新的 eta 只影响右坐标，不添加物理正则项。原目标 g、完整真 cuff 范围、所有内部自由接口和中央/真 cuff 两 jets 均不变。

历史 h487 field `cdcbbd53c4019d0b4df88043662c13c736b65429575e6276ac44bb482375aa12` 仍只是比较身份；同 job 的真正基态、暖初场和所有连续预算均各自记录 SHA。若浮点重生改变最后几位，记录差异并消费自己的真实场，不挪借旧场证书。两个 job 的同输入受控比较最终还须核对其实际基态和暖初场身份，不能凭任务名称认定逐位相同。

## 完整执行图

沿已发布的 angular-warm cold graph 保留全部14阶段：R243输入接口核、完整 h487 重生、基态 R236/STL、准确频率包含、实际 M48 solve、R226六jets、新场全相位几何、暖初场双微窗/祖先并集、新场双微窗/祖先并集。最外层 supervisor 再做新场 R236 与完整三相位 STL。没有删掉旧观察点、缩小物理区间或以内部 r=.6 seam 替代真 cuff。

唯一数学求解改动是把 M48 solve 的入口换成 `6a65-m12-full-normal-warm-refinement.py`，并显式给上述 eta / assembly 参数。它绑定已发布 R243 core `e58d4f3c036a1ec4b78a3c7022ac6e6677e9b7bac4c3be8eea43ed8665a2ae81`、新 M12 完整H helper `f19a09b0d4efbb9f6f8122de446f371306d291dfa47cf0dfeb7727fe0e0b18f9`、R244 通用 helper `1fdaa80e4a56631c858c1a0f4f31557ec8a72254170b6b1df4ec16cbe6437361`。

实际坐标接线已逐行核对：旧 `LinearOperator` 保存的 bound `matvec/rmatvec` 仍调用该实际实例的 `unpack/transpose_precondition`，所以替换这两个实例方法即可使用新的 $T$，完整物理公式和缓存数据未替换；正规梯度恢复明确换成 $D^{-1}Lq$，而不是旧H1恢复。每个Newton步骤绑定自己的完整H装配回执。R243 core执行完后，adapter把主报告及暖初场报告标为实际adapter来源，同时保存原core和全部helper身份；更新暖初场报告SHA，再交给微窗/祖先/连续消费者，避免元数据改写后下游还绑定旧报告。

## 发布与规则同步

独立窄push触发只含新 workflow 和本题的新 request；数学源冻结在RUNNER_TEMP，与发布工作树分离。350分钟上限、每2700秒 literal pull 后立即核双README；使用独立 `6a65-m12-full-normal-ci-rules` marker，首次pull前持久Git作者身份，H写入前10000字节限制，README变化则先停数值并普通发布H-only实际SHA，再exit42。NFF循环、只处理本marker冲突和空rebase skip全部沿用已审实现。

最终只提交一个小Markdown实际结论。所有完整证书/数据/Actions报告/STL仅在RUNNER_TEMP或Actions logs，公开只列实际关键指标、来源/参数/run和完整输出SHA，严格执行根README15。摘要推送NFF时只撤回严格验证的本job唯一未发布摘要提交，再立即重新pull/规则检查；不强推、不改写已经发布的历史。

## 文件与实际检查

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `scripts/6a65-m12-h487-to-m48-full-normal-cold-run.py` | 15238 | `481f31ee8336d9eb51659aab044778a1979fffe33f0f3a4afa6dd81365c7994f` |
| `scripts/6a65-m12-full-normal-rules-supervisor.py` | 12495 | `eee1188b712e71d2af4ce51b8a586fa2816e770050f1bec14c118ff69e8bbbe4` |
| `scripts/6a65-m12-full-normal-summary-publisher.py` | 16709 | `679cc6498176eb79ab03df4037471e1d8260f7d4af3b4e7e6fa77c45e804d593` |
| `scripts/6a65-m12-full-normal-warm-refinement.py` | 6665 | `bec17da0df0ea018902c743e2805703904736368de0098d25023e2cfa9d220b7` |
| `workflow/6a65-m12-h487-full-normal.yml` | 13709 | `1e95c63adfe8296beea752320af18e0292707229ed22266874304acca57ac3dc` |
| `workflow/6a65-m12-h487-full-normal.json` | 2656 | `477ffecb9f4508adf100739d757ef6922aa6d09ceba4070c89f8eef00b38121f` |

workflow安装为 `.github/workflows/6a65-m12-h487-full-normal.yml`，request安装为本题 `ci-requests/6a65-m12-h487-full-normal.json`，四个Python源安装到本题scripts。其余数学依赖均已提交，不复制或修改。

本地新接线实际：YAML解析、9段bash-n、5段Python AST、4个新Python compile全部exit0；request默认值明确核为M48/N768/800/1/eta1e-6/block8、lambda0/damp0。没有执行新大场，也没有为这次接线重跑已证完整H数学核。后续是否收敛、条件数如何、是否接受和全域几何是否保持，均由这个新的实际job决定。
