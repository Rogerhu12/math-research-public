# recovered-r1 独立同H尾：正式进程失败

session25906已实际poll到exit1；worker在close之前已为−9，close之后仍−9。
wall451.358396s、wait4 peak384420KiB、user82.555358s/system1.566188s。
仅据这些资源数字不能认定OOM、墙钟时限或数学不可达，原因仍未知。

所有91源和历史profile指纹已通过。首个完整variational评估实际返回norm
3.781007387546619e−7，尚高于原2e−9门；request后286.307秒有真实iteration事件，
随后进入correction，chartCondition约24528.2937。没有完整响应，没有新前缀解。

最新iteration-recovery-only包仍是iteration0的此一基点，未出现新的接受试步。
它包含577×48全状态、9个raw节点和全部24H，hash与元数据见同名failure.json。
旧r1的已推暖点和本次失败数据都保留；绝不把丢失的旧29674成功包补造回来。

下一次fresh恢复只改资源：Node heap384→256MiB、每胞元point cache8→2。
`tail_frozen_geometry.mjs`显式允许1…96且每次检查完整五/七点历史指纹；
`closure_bounded_point_cache.mjs`只淘汰memoized点，逐点公式与操作顺序保留。
这些资源键通过CLI/环境传入，不进入数学cfg。原M24/N512/depth8/steps12/parts8、
全Jac/audit、tol2e−9、原g、全部H保持，并仍执行完整参数/指纹守卫。
这不是以更少模式、层数或更松门槛换取成功。
