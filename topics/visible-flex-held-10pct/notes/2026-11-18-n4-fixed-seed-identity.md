# 真 coupled checkpoint 的固定 g seed 接口核对

维护：n4_round_core；2026-11-18。此条记录 `build_seed` 的输入身份修订，不是一笔已解出的 coupled 精化。

## 三个输入定义来源

1. 全部 physical_profile 和 physical_port 直接来自所给 checkpoint，固定其实际 delta、vd；不替换成邻近线性设计根。
2. 核心取 solved parameters 和 central_correction_scales。design 输入的 q=gauge、c8=0；fixed 输入的 q=gauge*exp(p0)、c=scale*p[1:]。core_summary 仅报告差异，不能作为已求核心的定义。
3. 原 exact reference lift 中的 initial，按原角图与原投影阶数从这个完整核心重新计算。pp(0) 可能只满足入口 BC 到数值残差，因此仅用于报告入口偏差。

另修正初始化的物理网格合并：原 `merge_profile_mesh` 专用于 [0,1]，故先把原 physical s 除以 end，合并后再乘回。这样不丢掉 s>1 的旧节点，不改变 g、未知函数或方程。旧已执行版本保持在独立冻结源文件中；首个线性 M20 精化仍由原方程收敛和完整区间审计定义，其初始网格的疏密不重写该终态。

## 对真实 eta1/q=.001/M12 输入的实际验证

输入是主会话已真正联立并接受的 n4-coupled-eta1-q001-v1/seed.json.gz，SHA0ca28d3b6fd1201b570cb0cc85259a15fa9acc5b81e798641e85045998dc653e。其实际 delta=.030023164049137137、vd=.2481921107405831 原样保留，q_gauge=.001。目标仅扩展 seed 到 M16/angular1024，`evaluate_boundary=False`；没有查询尚未暖启动的非线性尾。

| 项目 | 数值 |
|---|---:|
| 原输入节点 | 993 |
| seed节点 | 996 |
| 原物理节点至新网格最大距离 | 1.11022e-16 |
| 完整核心 F / Ft / Ftt 恒等误差最大值 | 9.43690e-16 |
| 完整映射的角向投影误差 | 1.83187e-15 |
| 原入口归一系数残差 | 1.82243e-14 |
| seed入口修正最大系数 | 3.13081e-14 |
| 输入 summary 与参数的 c 最大差值 | 2.27868e-18 |

这些是所述实际网格上的初始化身份诊断，未声称连续区间误差证明、C² 收敛或新 coupled BVP 通过。现有 TailMixin 可通过 bvp_transform 安装，随后仍须运行主会话原 actual-tail 外层与全部门。

最终 API SHA f8431622a3973a0bb525a97c3155eb3cb7bbfe459193446eef91f5a69f943b39；结果、命令、输入/输出 hash 在 `scripts/resume_n4/fixed_seed_api_checks.json`。
