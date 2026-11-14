# 成功增广 actual 的 27→24 固定问题视图接口

这是对已发布源码的静态接口说明，不是新的转换实现或数值验证。root 负责恢复
`root_actual_freeze_design_view.py`；旧完整源码不在 strong 的保留上下文中。
转换对象必须已完成原 actual 三控制联解、完整尾 audit 和所有原门。

## 原布局及必须保持的对象

`strong_actual_augmented_core.py` 的 M=24、n=73：

- p[0:24] 是全部核心未知量；p0=log(c2/gauge)，
  p1=(c4−reference_c4)/pscale[0]，p[2:24]=c6…/pscale[1:]。
  pscale=max(gauge**arange(2,M+1),1e−9)，gauge=.09。
- p[24:27] 是相对本轮 `self.cfg` 的 delta、boost_length、boost_speed 偏移。
  最终物理profile已经把它们加进去；冻结后不能再次加偏移。
- 新物理曲线记录 `parameters` 原为27长，`core.coefficients` 为24长，
  `central_correction_scales` 为23长；核心高阶p大不表示物理高模大。
- 最终 `frozen_profile`、
  `actual_augmented_continuation.final_physical_profile`、
  `raw.identity.profile` 应逐项相同。raw记录最终真实Flow profile。
- final的 `numerical_meridian_chart.reference_t` 与 raw的
  `identity.numerical_reference_knots` 同一；physical_s是最终Flow.breaks。
- 原raw x/y/cubic/rms是数值坐标数组。物理mesh/五次PPoly属于另一坐标对象。

`root_fixed_chain_audit.py` 的八项固定物理/表示数据恰为：
`frozen_profile`、`physical_tail_parameters`、`physical_tail_cut`、
`angular_chart`、`chart_reference_coefficients`、
`chart_reference_frequencies`、`gauge_amplitude`、`meridian_length`。
原tail depth、shootingParts也需保持。另为逐位raw重放，保留旧reference_t。

## 构造与回调

可沿现有 bounded.adapter.module 的 root_dual factory hook：
先让 `utility.make_fixed(SimpleNamespace(make_dual=source_factory), adaptive,
charts, chart, saved.chart_reference_coefficients,
saved.chart_reference_frequencies)` 构造真正Fixed，再外包Actual的完整尾方法。
不要让27参数Augmented继续冒充fixed。

父init会立即调用make_flow；外包子类须预置ref_coeff/reffrequencies，并在make_flow
入口坚持保存的角参考（Dual父构造会临时写其默认ref_coeff）。构造用最终profile、
原port、gauge、M/N；完成后显式恢复旧_neck_knots/chart_breaks，清Flow/core/initial
缓存，再确认Flow.breaks与saved physical_s及总长一致。旧普通fixed adapter只
从当前profile重新生成归一knots，不会自动复原原reference_t。

取 `p_fixed = p_augmented[:M].copy()`，不从核心系数反算log再增加舍入；复核由
Fixed.initial得到的完整core与保存core逐项同。x/y/cubic保留，不调用
`restart_fixed` 的pullback/入口correction；该方法是后续真正更换离散网格时用的。
RHS前24个参数是边界数据，无直接profile导数；几何完全冻结。

用记录的真实尾包切出 `slope` 及
`JH=heightJetJacobian.reshape(3*M+2,M)[:M]`。
`H=-gauge*y[2*M+1:,-1]` 必须逐位等于 final真实尾request.height，才允许在这个
单点复用slope/JH。转换无需启动Node。真实Fixed+Actual BC为73入口+24尾端=97行；
删掉原末三条低核心目标约束；这不是更改保存解，而是把它置于其最终固定g问题。
最终Actual.bc_jac需要M列，不能保留Augmented覆盖的M+3版本。

## 原门实际重算

以原raw cubic构造 `PPoly.construct_fast(cubic,x,extrapolate=True,axis=1)`。
在同一数值坐标及同一个最终物理profile上，执行原
`scipy.integrate._bvp.collocation_fun(fun,y,p_fixed,x,diff(x))`，再执行
`estimate_rms_residuals(fun,raw_spline,x,h,p_fixed,1.5*col_res/h,f_middle)`。
记录全部RMS数组差、最大值和原tol；只做必要RHS，不装配Jac/解BVP。

入口残差使用原bc_tol（raw identity记录1e−7）。未缩放真实尾门直接算
`gauge*flow.fun(end,yb,p_fixed)[iz:] - slope/sqrt(E)`，仍要求≤1e−10；
不能把除bcweights后的量当物理门。并确认完整H、核心、physical knots、
八项物理数据与数值坐标一致。参数布局变更有明确数学映射，所以新raw.identity
须由真实Fixed对象重建；旧identity固定标志不能直接抹改后声称重放通过。

只有全部复核通过，才写新的独立fixed-view物理metadata与M参数raw恢复包。
物理mesh、五次coeff和原actual尾数据可原样引用，并记录其SHA；x/y/cubic/rms
可复制且逐位核对。保留原设计包及其来源、完整设计历史、原接受记录；新视图
不是新Newton解、不是已完成同g精化，而是后续真正M28等同g求解的合法基准。
原raw coupling_context中的actual_augmented/target字段保存作历史provenance；
新的context与layout从真实fixed对象取得，确保未来raw.read身份守卫可重现。
