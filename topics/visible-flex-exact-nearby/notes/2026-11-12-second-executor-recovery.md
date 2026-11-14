# 第二次执行环境丢失后的实际恢复

2026-11-12，visible-exact-astra-f6a2。主目标仍未完成。

## 已推基准与规矩

10:52 UTC 已成功推送 `0162a1a1512cf235534c6dc251eb8e39d159164d`，
该批统一清单为 `2026-11-12-true-beta-defect-step5-and-collar-frozen-manifest.json`，
SHA256 `6a883c4eba31e6f8e9575a74ad1c7ed981555e477c2cf5cf9bc8f505f89b11e6`。
恢复分支 e 的提交为 `8b0191cf4ad5c057ff9a3826db09087f06a00501`。
推后 HANDOFF 更新到该 SHA 的本地修改没有来得及推送，现据实际推送记录补记。

约 10:59 UTC 执行环境失效，11:04 新环境出现，工作目录没有原仓库、依赖或数值报告。
恢复时已有一份新写的 entry 源，因此在原目录 `git init`，保留该文件，用部分 fetch
及稀疏 checkout 恢复本题。随后实际 `git pull --rebase origin main` 到
`b988cbb19c8fdb2784f8a9dd0d14e55fd75b8438`；两 README 相对上次已读
`38e35bfd5b46c86af6fa1e03b822113cf34e128d` 无差异。此前连接器的 targeted
blob 比较只算中断期只读检查，没有代替本次终端 pull。

## 恢复来源与报告身份

逐字恢复的源码及其 SHA256：

- `scripts/fourfold_phase_full_angle_time_domain.py`：`d681614326efacb0c256037d2c7e995eb895d8f77ce4281720f44c76a896548e`。
- `scripts/fourfold_phase_uniform_field_time_grid.py`：`7c5b0f94aa4e4008b23c1e30443454ad21d3885206206dddcbb7a834e1451c32`。
- `scripts/fourfold_phase_uniform_field_time_grid_fast.py`：`30655319d9172b0ac8de857f24329d944f5ec9d87b08ee283ee0292f90159aa8`。
- `scripts/fourfold_phase_positive_family_outer.py`：`6c06be00ba05a57a767fb30c56264dc1d6d837a936957cc194e8612d33e9d158`。
- `scripts/fourfold_phase_positive_family_collar.py`：`9ea8a5fd0d554de6ffc700ca4f1c407d70c68c634065bda0b13f71887e67edf5`。
- `scripts/fourfold_phase_exterior_entry_jet.py`：`9c522b37a84e78251d195d9d821db31e7b5aa3915c14e6adb7e38bb2af7d3c9e`。

这些小文本还通过 GitHub create_blob 备份；只有终端不可用时使用该通道，
没有通过工具传输大数据，也没有把令牌传给连接器。旧数值报告不由摘要重造。
全角度复时间域已重新启动完整命令；positive-family 的 A/B/C 旧 partial 均作废，
从零计算。entry 旧尝试在 import 阶段终止，新环境的首次真正运行才产生报告。
实际重算报告分别记录此次源哈希和命令；elapsed 改变引起的报告哈希变化不等于
数学结果变化，但仍使用新的清单，不伪称保留了旧 JSON。

`noise`、`real`、`actual_field_fourier_package` 没有完整原字节缓存，
将以明确的新恢复版重建、重新执行。旧 actualfield 只到节点 jet 计算，未完成
连续预算，也没有保存可复用有限 P；新版本先加入准确 dyadic 系数分片及读回定义。
native-series FFT helper 也重建为新版；旧 12% 提速只作丢失前的历史观察，
重新运行后才保存新的结果。不得把恢复摘要当作任何计算证书。

## 可重建的大中间量

完整 δ₄1032 两腿 trace 和 δ₅ retarget reference 的大分片再次丢失。
已推的原输入、源、精确参数、命令、逐分片 SHA 及 manifest 保留，按各自重放
入口重建。不能从已推的少量汇总数值反填 trace。当前全角度域及有限场系数构造
只需要已推的 time-grid manifest 和 descriptor，不必等待约 47 分钟的旧浮点 trace。

接下来仍是同一 δ₅ 的全时间/全圆真实场、参考复合及连续残差、参数费用、
真实 KAM、全反馈算子、实际闭帽与固定 H，以及同一个精确族的几何完成条件。
任何局部域通过、有限系数保存或正族子区间通过均不是课题完成。

## 本次已经实际重算的记录

全角度419域在此次环境真正重跑完成，三个共同germ均通过，D及−K的下界与
丢失前输出一致；新报告 SHA `e1a2c3f327c3a36e33c412e76c70eebd185f224ea938dcdea93ee30ab9a05f90`。
入口和完整依赖见 `2026-11-12-step5-whole-angle-domain-replay-frozen-manifest.json`，
该清单 SHA `37f1430a6bbc1b876e20ca4fa6ba1a66720a3d1b01271068eacfd33064949eea`。

正族准确根领口也从零55/55通过；新报告
`2026-11-12-positive-family-root-collar.json`，SHA
`f796e89e61f45ffba22c2aa2ab145a40ec4a80fe39abe30bc797dc0b06b966cc`。
外段两项全覆盖仍在运行，不提交 partial 作为完成报告。新entry首次真正完成，
报告 SHA `6748eb485a77031a3f50caccea5111d913e58aa32ac428e30a7689354cfd8f26`。

重建 native-series FFT 在 N=2048、m=53、3 fields、320 bits 实际重跑。
全部有限系数与旧蝶形算法相交，逆DFT包含所有准确输入，四点符号约定通过。
本次CPU旧2.15975s、新1.21730s；只比较有限线性计算，没有用速度或有限测试
替代完整解析误差。源和新报告均保存；它不是旧源字节复刻。
