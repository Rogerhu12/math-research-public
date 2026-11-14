# 完整变分段的精确持久化：备用实现状态

本组是尚未接入生产的备用实现。当前 strict exactraw-r1 不使用逐段缓存；原完整
Jacobian、残差及审计正在独立运行。这里没有新的物理解或全尾残差结果。

`strong_exact_stage_flow_store.mjs` 保存一次已完成的完整变分段输出。输入键包含
完整 Float64LE 状态字节、段号、完整身份以及 Node/V8/平台；五个返回字段
out、J、meanHeight、minA、minD 全部保留原 Float64 字节。临时文件原子改名，
完整长度/头部/校验和/有限性守卫拒绝损坏记录。非 Jacobian 路径原样调用原函数。
13 项小型纯数据夹具已正式 exit0，包括单 ULP、正负零、配置/源/段号改变、
临时半文件、截断及校验和损坏。夹具没有构造 physical、求 RHS/Jacobian 或解 BVP。

`strong_exact_stage_engine.mjs` 是独立的实验性接入层，未在数值计划中使用。
它锁定原 resumable 模板 SHA，保留原 residual/correction/line-search/acceptance，
只把 cellFlow 包在精确键存取器中；请求必须显式给缓存目录。身份包括两棵固定
数学源树和本课题 MJS 源的实际字节 SHA、两个冻结校准输入 SHA、全部展开物理
参数、实际 warp alpha、resolved M/N/steps/parts/engine、每段 mu/portRatio 与
每个 profile 的 integrationBreakpoints。原 split 入口在 core 构造后替换 engine，
因此身份明确包含实际 split engine 及它的全部源码，不能只靠 core 或几何采样。

原 cellFlow 每次复制完整 K 维输入进新的 K+2 零向量，末两个 mean 通道初值恒0；
返回五字段齐全。target/scales/graphs 在段外参与原全局残差与边界装配，不可从
历史全局 norm 推断这次通过。split engine 的诊断调用计数不会在缓存命中时重放，
须把本次实算与历史恢复分列，不能报告两次独立的 Jacobian 重算。

接入层目前仅外层语法检查通过；虚拟变换层、真实单段逐位比较及完整 evaluate
对照仍须另行实际验证。即使其后验证通过，任何缓存命中也只能称相同完整输入
下已完成变分段的恢复，最终全局残差、物理正性与原 full audit 仍全部需要执行。
所有中间 stage 二进制目录保留在专用临时工作目录，不提交多代可再生缓存。
