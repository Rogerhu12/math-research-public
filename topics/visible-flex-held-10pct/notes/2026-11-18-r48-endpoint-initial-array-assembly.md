# 真端点升模的单次初值组装接口

**可信度：源码准备；尚未构造新模型或执行数值初值。** 本条把已登记的 R47 动态模式工厂与 R48 完整参考补偿接成原实际 coupler 可直接消费的接口。它不是另一条初猜扫描，也不是新高模解。

## 一次构造与坐标

`scripts/resume_closed/r48_endpoint_initial_arrays.py` 的 `assemble(endpoint_binding, modes, angular, linear_port_path)` 要求真正完成的字面 $\lambda=1$ 物理读器。它通过原 R47 工厂构造新维模型，只调用一次该新模型的原 `initial(p)`，再使用 R48 的完整三块补偿。旧七个控制参数和尺度逐位继承，额外控制从零开始；原实际 $\delta$ 只在冻结 profile 中吸收一次。

旧物理 quintic 的节点 $s_i$ 先经过新 fixed-profile 的原 `inverse_chart` 得到 $x_i$。由于浮点反算未必逐位往返，新初值必须取在实际的 $\widehat s_i=\operatorname{chart}(x_i,p_0)$：

$$
Y_i=Z_N(\widehat s_i),
$$

而不能把 $s_i$ 上的值与稍有不同的 $\widehat s_i$ 混配。接口保留原 inverse-chart 门并记录真实前向差，不强制该差为零。初值来自保存的完整物理 quintic；没有拿 raw cubic 或 raw.y 代替它，也没有再投影旧有限场。

原 R48 转移包含 $a\chi$ 及其物理两阶导数。本组装只取实际 BVP 所需的状态值；它不额外修入口、不制造一个新 quintic。原 inlet 的有限差作为紧凑诊断保存，之后由真实原 BVP 处理。

## 完整端口与参数口径

返回的 $H$ 是全部新维数的 Dirichlet 请求。切口参考补偿及其两 jet 为零，因此接口检查前八项与原物理 quintic 的 cut H 逐位相同，新增 Dirichlet 项为零。这不提供任何新高模的动量、实际 DN 响应、Jacobian、audit 或接受结论，不能把旧八维数据补零后称完整真尾。

新 `fixed=True` 只冻结物理 profile，原求解方程仍把 $p_0$ 和全部控制作为未知。实际核心主振幅为

$$
q_{\rm actual}=q_{\rm seed}\exp(p_0),
$$

不是 gauge $0.06$ 乘以 $\exp(p_0)$。入口记录完整物理参数，后续高模 runner 也须按这个公式记录终态，不能把参数漂移称 README 第 5 条的全参数固定加密。

R49 证明的是精确完整场抵消下的原 Frenet 均值等变；本次跨模式浮点评估并未得到该恒等式的数值误差界，因此接口没有复制旧 mean，也不跳过未来实际候选的原 height-integral 与 audit。

## 交给实际 runner

返回对象具有 `environment/model/obj/transfer/x/s/y/p/H/inlet/descriptor`。高模 runner 使用这些现成对象进入其原流程；`write(directory)` 只把已经形成的数组与记录保存到 scratch，不重新构造初值或做 RMS 探针。数组、完整矩阵和物理网格不入仓库。

紧凑文件 `scripts/resume_closed/r48_endpoint_initial_arrays_preparation.json` 保存源码及依赖的 SHA-256、明确的操作与未付范围。本条仅 AST 解析和来源读取，没有 import 任何模型，也没有调用初值、尾或 BVP。实际初值只能作为未来真实高模运行所需的一次构造执行并记录；不能提前把本条 source-only 标记升级为执行结果。
