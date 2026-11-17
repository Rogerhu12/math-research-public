# 新补弧控制的第一批真实前缀

五条执行链：q=.005/M6 的圆化同伦，以及λ0上的q=.01/M8、.02/M12、.03/M12、.04/M16设计。使用真实n4线性端口，未联合非线性尾。`completed_runs.json` 保留所有有限终态，包括q=.005在λ=.3的maxnodes失败。

核心三文件来自相邻 `complementary_controls` 冻结包；其完整系数/导数定义、审计、旧基对照独立保存。初版driver在参数变化时重复构造相同的只读basis；cached版本只缓存该对象，默认quadrature_order仍64，不改任何函数、正性门、Jacobian或BVP接受条件。调用方不修改缓存数组。

`prepare_runtime.py --repo REPO --dest NEW_SCRATCH_RUNTIME` 调用已验的窄弧空目录恢复链，再复制冻结核心和driver、实际再生原worker port24，写出五条按依赖顺序执行的命令。它不执行BVP。所有端口、chart、状态/位置数组只在scratch生成。

这些旧运行保存了底层原源hash，但没有顶层运行时driver hash；包中明确为captured source。后续driver已增加启动时完整来源记录，不把后来的记录追填成历史事实。三组差分参数Jac的步长、误差和尺度均保留；没有把浮点差分叫作严格区间证书。
