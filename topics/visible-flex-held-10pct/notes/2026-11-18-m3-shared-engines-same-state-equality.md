# 当前 sparse 尾的同 mu 引擎复用：完整有限态逐值一致

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：最小分配补丁与一个真实完整有限态的逐值验证；不是新的
数学解、普遍性能保证或此前进程中断的根因证明。

## 最小改动

`install_shared_tail_engines.py` 从原 sparse source 创建独立副本，
只在 stage-core 创建阶段把同 mu 的 engine 缓存到当前 DN 内。
同一 DN 中 modes、spacing、quadrature、orientation、projectionFloor
都是同一组常量；缓存不跨 DN 或物理设计。stage-split 用 Set
只替换每个共享对象一次，仍使用原 `Object.assign(cell.engine,engine)`，
保留 cutJets 与隐式物理 jet evaluator 捕获的对象身份。

未整换历史shared-core：当前 `sparseGlobalSolve`、稀疏输入组装、
完整ODE/RK、浮点运算与求和顺序、所有root/D/S/A、line search和
最终2e-9门均逐字不动。installer反向去掉缓存块后要求核心文件
与原件完全相同。两个stage模块以外，仅给原Python client增加
stderr文件及returncode事件记录，EOF异常类型和原判断仍保持。

源检查表明共享对象保留的是固定求积/三角数据和函数闭包；root、
RHS/Jacobian及flow state/tangent均在每次调用中建立。下面另对
返回数组的跨stage变异和重入做了实际检查，避免只依赖说明文字。

## 同一个完整接受态的对照

输入为 raw λ=.02/M8 的真实 final tail，SHA-256
`1db6a909142bdde5f71d3b35ba8b574eb0537dac0608444fbade6b31f1f0c51f`。
其原接受残差1.375444292097049e-9。固定相同physical对象、
全部checkpoint状态、target、scale、M8/N128/depth8/parts16/steps16，
分别调用原与缓存版本的完整 `tail.evaluate(...,true,...)`。

- 全部1152个stage均计算，包括完整flow Jacobian；engine实例数
  从1152降为8（每个唯一mu一个）。
- 共比较350224个标量：每个残差块、输出、每个flow Jacobian、
  全部graph/gain及deep graph，最大逐值差全部为0。
- 两边归一化残差均为1.375444292097049e-9，minA均为
  .7420033682728756，minD均为.9994281510655263。
- 全部残差/输出/Jacobian的原始Float64字节哈希都为
  `e088dd254e155ce16cb2d3ec5ed700de0ea4dae481d28c15f371cb4766b68941`。
- 在stage0调用后再调用同engine的stage1、不同engine的stage144，
  原返回root/RHS/Jac数组没有变异；回到stage0重算也逐值差0。

这些正是原全局稀疏线性系统的所有有限数值输入，加上未变的
原稀疏组装，说明本输入上完整残差与Jacobian等值。该记录未
使用线性尾代替实际态，也不由一个样本推导所有浮点执行必然
bit相同。一次完整evaluate耗时原14.59秒、新15.24秒，不申领
加速；此改动的具体作用是减少重复engine分配。

## 复现和实际恢复

复现脚本 `compare_shared_tail_state.mjs` 接收旧source、新owned
source、实际tail checkpoint和输出路径。完整参数/hash见
`shared_tail_full_state_record.json`；installer来源与派生hash见
`shared_tail_install_manifest.json`。三个派生源码快照在
`shared_tail_modules/`，不包含场数组。原源码未改。

实际恢复继续同一raw λ=.02的M16固定g问题，只替换为这个已对照
的owned source并启用诊断。旧v2没有退出码，仍只登记worker中断；
新client在响应EOF/关闭时记录returncode和stderr字节数，不把
SIGKILL、OOM或数学失败互相混称。最终M16数学终态另记。
