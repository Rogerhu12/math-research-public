# 首次暖交接的实际失败与坐标诊断

会话：Astra-held10-06bbeb39-20261126。状态：**原R53 M24恢复已通过；暖phase场尚无接受结果。**

## 已经观察到的实际返回

run45775899674 的 attempt-000 是同λ=.002、M24的首次暖BVP；初始域通过后实际报 `OverflowError('math range error')`，没有raw返回，run SHA为 `0636aa7be3fbaec8f2f86e7774decb9cc4f444c2218769e26e897d8037ca440a`。父链继续升M不代表已有暖锚；其 `accepted_lambda=.002` 仍指原R53源。

## 原源码确认的具体问题

原 `950f-prefix-warped-bvp.py` 的 fixed initial 先计算 `q_aux=seed*math.exp(p0)`，再检查原 `1e-7<q_aux<.124`。原 DomainNewton 只把 FloatingPointError 当域拒步；因此指数溢出能在域检查前以 OverflowError 逃出。这里只由实际异常类型和源码定位实现问题；完整实际栈仍待同runner只读probe回传，不把它称为物理无解。

继承的 `pscale=max(gauge**j,1e-9)` 与暖factory反解的 `max(gauge**j,1e-10)` 不同；默认 phase_scale=1，第8个phase坐标已有倍率差，第9个起倍率为10。实际解析input_chain与数值映射使用同一反解，因而不能从该差异断言漏了Jacobian链式导数；但原“所有d_j=phase_scale*p_j”的记录不正确，后续版本须修正或明确真实坐标。零控制仍逐位相同。

冻结δ后 fixed 构造还重设径向 `chart_join`/`chart_reference_prefix`；首入口又加入角spline所需节点并从旧physical quintic重新采样（631→694）。同物理s下完整lift保持F和两jet，并不说明新计算坐标上的collocation残差保留原RMS。不同的t坐标max_rhs也不能当成物理映射已变。

## 同runner已排入的只读检查

`warm_handoff_equivalence_probe.py` 绑定实际原run/raw/physical与attempt-000，顺序重算原raw网格的原RMS、deployed固定径向chart的RMS、冻结原chart的RHS/BC/RMS，并在同物理s比较完整六jet与mean1168导数，最后对少量实际参数列作解析J/有限差分核对。输出同时保存实际attempt异常栈。

这不是BVP，不写accepted，不宣称λ前进或几何完成。新command在当前父链自然返回后于同runner执行，既有实际场保留；不是因时长停止当前运行。若该探针显示真正方程差异，按实测修改输入/表示继续，不用同图定理掩盖离散或参数问题。

## 只读原场检查的实际终态

同runner probe已exit0。冻结原chart后，631节点上的f/fm/collocation残差/BC/physicalBC/RMS均逐位同；原RMS9.927150345213775e−7，physicalBC3.7178883222402893e−16。完整core二阶、初值投影和7个物理s点的六jet也逐位同。原631点在deployed新chart的RMS为9.92766133631121e−7，仍低于原门；首694点重Newton失败不能据此反推原同图场不合格。

六个实际参数列、两种FD步长的RHS最大差≤3.2192494079679086e−8，BC最大差≤1.6970799765481104e−10。这是有限列核对，不称连续误差定理或新暖BVP。见[实际小记录](2026-11-26-warm-handoff-equivalence-execution.json)及[完整坐标/链式审计](2026-11-26-warm-entry-domain-and-coordinate-audit.md)。下一独立v2入口将明确原solver provenance，在同图坐标重表达后重审全部原门；真实λ变化仍须新BVP。
