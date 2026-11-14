# 实际全 H 尾的 M+3 三控制入口与基点检查

2026-11-12。新增独立入口，不改原 actual、fixed、provider 或正在运行的共享源码。当前真实局部检查通过；尚无由此入口接受的新 BVP 曲面。

## 参数与方程

M24 的场维数为 73，参数共 27 个：前 24 个保留已有 fixed-core 的全部核心系数参数，末 3 个是实际 delta、boost_length、boost_speed 相对基准物理 profile 的偏移。前两项核心参数仍为 `log(actual c2/gauge)` 和 `(actual c4-reference c4)/scale[0]`，后续高模按原固定 scales；gauge `.09` 不随实际 c2 增长。尾边界高度始终是原桥接约定 `H = sigma*gauge*Yz`，sigma = -1，本支不另加相位翻转。

边界残差共 100 个：73 个入口位置系数，24 个完整 actual nonlinear-tail 坡度边界，再加三条实际 c2/c4/c6 约束。三条约束按固定 `gauge, scale[0], scale[1]` 归一，原 bc_tol=1e-7 保留。所有 24 个核心系数均是边界未知量；前三个由约束确定，高模由完整场与实际尾共同解出。

物理 profile 随末 3 个控制变化，输出 `fixed_metric=false`。参考材料角、数值 reference_t、gauge 与尾物理/数值问题固定；`chart(t)` 映射到当次物理 knots，几何参数导数包含 `s(t)` 与 `ds/dt`。新完整切向 warm 把旧固定-J 数组尾部解释为全部核心参数变化，另外附加物理控制导数，不能把它误读成旧 triple 的前三项。

最终 Actual 类会覆盖继承来的 BC Jacobian，因此入口在完整类生成之后显式挂载 100×27 的增广边界 Jacobian。入口只把 actual client 显式选择为已核对 frozen 客户端；原 full-H outer 重解、每次候选接受前的真非线性尾复核、最终 audit 与指定物理 BC 门保持。

每个内层接受 Newton 步保存为**未验收**恢复对象：数值 x/y/p/cubic 全部保留，唯一分块文件名，读回所有块后原子更新 latest 指针，保留前一个完整点。空 RMS 和 `success=false` 阻止把中间点当成 postprocess-only 成果。真正已接受的候选仍需完整新 H 真尾检查，最终原始/raw/物理包沿用主入口提前保存。

## 标准库准备与真实局部检查

标准库 prepare-only exit0，14.7MB 峰，无 NumPy/Flow/worker。真实基点来自 `root-q095-design-fixed-actual-m24-tol7-frozen-r1`：实际 c2 `.09499996014428179`，gauge `.09`，M24/N768，2004 节点。

第一次 r0 检查实际 exit1，wall20.96s/250788KiB。最大端点方向差分误差 `.0017721473028930298`，原日志和资源保留。这是局部实现检查的失败，未启动 BVP/Node，不是分支不存在的证据。

r1 检查在同一个真实端点方向使用三个差分步长，并保留失败尺度：

| h | 端点方向相对误差 |
|---:|---:|
| 2e-7 | .0017721473028930298 |
| 2e-8 | 1.759454544247018e-5 |
| 2e-9 | 1.759329464402725e-7 |

误差按 h² 下降；原高频随机方向的 h=2e-7 尚未进入足够小的差分尺度。没有修改场方程、实际尾条件或生产验收。

r1 真实全基准复现及局部 FD：

- 整组 2003 个 RMS 残差逐位同，最大 `9.976296746350968e-8`，数组最大差 0。
- 实际完整 H 与官方响应逐位同；原真物理 BC `3.0200516839669564e-14`。
- 核心系数、reference_t 与原基准完全同；三条新核心约束恰为 0。
- 状态方向 complex-step 相对误差 `4.420592659795242e-15`。
- 核心及末 3 个真实控制列 FD 最大相对误差 `4.6481749716608344e-8`；全部核心直接 RHS 列恰为 0。
- 实际形状 RHS Jac 73×73×5、参数块 73×27×5、BC 块 100×73 与 100×27。
- session74786 已实际 poll exit0，wait4 exit0/无 signal，wall71.18s、峰252484KiB；零 worker 尝试，无全局 Jac/BVP。

这证明所检查的真实基点加载、参数转换和局部导数一致，不等于所有新参数态的全域数值证书。后续六个完整全场暖态将记录原 RMS、全部均值与物理 cubic 几何；暖边界只用已接受真尾的局部切线，正式新态仍需生产实际尾求解。

## 源版本重现

r0 入口原文 28688 bytes 已逐字重建，SHA `f3c890ab0c9689e5173efe1419a8e7ad6c09c6ff8818bfdd222a993bf67429b5` 与当次记录完全一致，保存为 `strong-actual-augmented-r0-entry-source.py.gz`；反向精确替换列表在 `strong-actual-augmented-r0-source-reconstruction.json`。r1 验证入口也单独压缩保存，原文 SHA `7ff94e3a02d1d51cfeb98a0b732d947d1cc9db55b710d27cb4bf41a816eef9ec`。工厂与 Newton 观察模块在两次检查之间没有变化。
