# 完整 normal 链的同次闭合值复用、原方程重读与可见成本

## 1. 结论与范围

本件交付完整的新工作数值策略：在一次实际 `_run_chain` 的同一完整自由点、同一有序角批、同一积分数据与同一控制角 jet 字值下，复用已经由原完整公式计算并返回的闭合值。所有被请求的角 jet 分量同时保留。全 32 段的目标、控制域、Newton/回溯、角 jet 求解、原始端点条件和完整外参数 J/J* 均继续执行。

当前原 09 的 ff544 子进程不作原位修改。新源使用明确的新工作模型和来源身份，不能把原09未返回场、未知历史或新run10输入当成已实际得到。本次没有数值执行、命中率、速度或首场成功结论。

来源审查发现，原解析 J3、解析六控制 frame、同次 frame 缓存、相邻矩阵和根缓存已经存在，本件不重新登记它们。新增缓存数量是整个闭合角 jet 值 C。原 `_meridian_data` 在 `_get_roots` 前仍会重建当前积分场；本次没有把该不同层级也换成缓存，更没有由时长推定当前进程的实际热点。

## 2. 实际来源与初场顺序

完整母体 `so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py`：SHA256 `3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc`，96,558 B。

原09 driver `fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py`：`ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5`，80,726 B。

原driver先写初始report及prepared事件，然后依次 `q.residual(x)`、`statistics(x,native)`、`scan(x)`。正常第一次完整成功保存要等三者返回。statistics只消费已经得到的residual，再作完整谱/目标统计和域读数，没有另一个F/J/root入口。首次root-packet capture也在这些初始读数返回后的保存阶段，不能把尚无首场的时间直接归给packet。

原residual读全部quarter513角，默认角块8，请求order1。全geometry请求order2；根缓存对同角只补齐缺失阶数并保存已选低阶字。它不省去前面的 `_meridian_data`，也不省去一次detached链内部反复的 `_closure_jets`。

原6a803 base的 `_parent` 只对固定T0、integration/grid标签及全部角字缓存磁盘NPZ。当前omega的Fourier角值、完整integration/direct meridians、core/cap/W仍由实际方法构造。该结论来自完整6a803和3d8d函数体，只是源级成本结构，不能代实际phase/profile读数。

## 3. 完整被缓存函数

令D为同次链的全部命名数据：当前meridian实际角jet、六列W与角导数、当前及固定reference的core/cap三jet、固定reference meridian。U为实际提供的六控制角jet数组。请求阶数r时，原完整公式为

$$
 C_j(U;D)=\frac{(\Gamma_j-\Gamma_j^0)-(P_j-P_j^0)
    +Q_{\rm full}\bigl(T_j^{\rm corr}(U;D)-T_j^{\rm ref}\bigr)}{S},
 \qquad 0\le j\le r.
$$

`Q_full` 是实际原 `_total`：重排全部J−1胞及原integration_order，乘原binary64 Gauss权和 `np.diff(mesh)` 工作宽，最后用原 `torch.cumsum(...)[-1]` 归约。准确物理mesh/S、工作carrier及舍入误差仍按原模型承担；本件不把普通工作积分称为准确包围。

原 `_closure_jets` 的完整函数体只重命名为 `_closure_jets_original`。原公式、所有返回分量、原normal计数和归约调用均保。新的同名wrapper只转发完整helper。

每段实际方程仍为

$$
 C(U_{i-1}+A_{i-1}^{T}\eta_i;D)-(1-\tau_i)C(0;D)=0.
$$

缓存发生在减去 `(1-tau)*zero` 之前。原 `_stage_constraints` 每次仍读取本段tau、原zero和当前target并作原差值。因此没有缓存旧段目标，没有把不同stage当成同一方程。所有六控制角jet进入key；不以eta0或U0替代U1/U2及其他完整输入。

在数学函数层面，完整D/U/order/S/carrier/源相同，C相同。在工作浮点层面，新策略明确返回一次已经发生的完整原计算字值；不声称未执行的新并行浮点求和一定逐位相等。因此它有新的工作策略/完整来源身份。任何实际轨迹差异、命中率或加速须由完整实际运行给出。

命中只clone完整、有限、CPU float64、无图结果，返回值不共享缓存可写Tensor。部分结果、未算高阶的零占位、失败/NaN从不存为完整值。

## 4. 全部原方程检查仍是真重读

每个完成stage的actual方程检查显式使用

`force_value(..., reason='original_stage_residual_reread')`；

最终端点检查另用

`force_value(..., reason='original_final_endpoint_reread')`。

两条路径都在 `_request` 中直接旁路查表，执行全部原公式。因此原报告中stage reread/final endpoint checked仍指一次真正新执行的完整原积分，不把缓存命中改名为重算。原finite、endpoint tolerance、控制球、domain及所有失败路径保留。

全32段默认partition一段不减。原 `_solve_stage`、Armijo、`_finish_stage_jets`、阶数升级字保护、相邻J6/J9、全部角和922胞、全自由core/omega/H、完整active隐式J/J*保持。Fourier、core inverse、reference calibration、physical closure lift和六jet公式未改。任一失败仍保真实发生的成本和阶段，不能从cache计数推科学成功。

## 5. 同次scope与完整键

一个缓存只属于一次实际 `_run_chain` context manager；正常返回或异常时立即释放。没有跨链、跨点、跨角批或active图复用。

来源/模型绑定包括实际完整operator文件和全部方法、完整base、新helper、canonical model和全部partition。新helper真实读取原3d8d文件并逐方法比较；只ctor/metadata与完整声明的closure wrapper/original/run_chain允许变化。原类的两个staticmethod按实际函数对象核，不误作bound方法的 `.__func__`。

每次可缓存请求都要求同 `_current_x` 对象、同登记digest，并重读全部float64自由点字。D保留完整命名容器和每个Tensor对象/version/shape/stride/storage offset/pointer/dtype/device/layout，scope进入及退出还重读完整D字摘要。未知可变/跟踪类型使缓存不可用。

角列表保原ordered literal phi.hex，最大阶数和实际请求order另存。不开浮点wrap，不排序/合并batch。控制key包含所有实际提供槽、全部六列、shape/stride/offset及所有binary64字。即使请求order较低而实际提供三槽，三槽仍全入key；signed zero按字区分。P0/typed/物理地址原去重与角色不由本层重写。

完整归约carrier包括mesh/Gauss u/w/S/J/integration_order、固定partition实际carrier及原 `_total`、`_corrected_jets`、系数函数身份。真实原 `_total` 只依这些mesh/weight及归约公式；不能用另一working width或另一个cell order冒同计算。

可选跟踪/key/clone/storage失败走原完整公式，不给零、不删除科学请求。完整模型或自由点在应固定的链中变化是明确来源错误。退出时记录ownpoint、partial stage和实际异常，不能把失败scope显示为完整场。

## 6. 活动图及未知transform旁路

`no_grad` 单独不足以排除forward dual、functorch或dispatch。新normal先在进入内部no_grad之前捕获caller环境；来自active/unknown环境的整scope禁用cache。

每次候选请求再查reverse grad、inference、JIT trace/script、compiler、functorch transform、forward AD level、TorchDispatch/TorchFunction模式和autocast。探针缺失也只旁路。所有控制和D Tensor还要求确为原CPU float64 Tensor、无requires_grad/grad_fn、无functional/functorch wrapping、无dual tangent且version可读。

原active `_implicit_jet_value` 和完整上游frame/control/zero图仍通过wrapper走原公式，不能收到detached缓存值。没有detach活动previous/data，没有删block lower triangular的任何stage。原first outer parameter J/J*和不支持外参数Hessian的范围保持。

探针依据声明的PyTorch2.5.1原来源；相应已读主源包括：

- [forward_ad.py](https://github.com/pytorch/pytorch/blob/v2.5.1/torch/autograd/forward_ad.py)：`_current_level`、`unpack_dual`。
- [autograd/function.py](https://github.com/pytorch/pytorch/blob/v2.5.1/torch/autograd/function.py)：实际使用的functorch活动探针。
- [overrides.py](https://github.com/pytorch/pytorch/blob/v2.5.1/torch/overrides.py)：function-mode stack。
- [utils/_python_dispatch.py](https://github.com/pytorch/pytorch/blob/v2.5.1/torch/utils/_python_dispatch.py)：dispatch-mode stack。

未知状态使可选复用失效，不构成新的科学准入门。

## 7. 完整既有family的源守卫

新J3/frame/C1/detached/adjacent体只派生来源身份及完整method守卫，原数学函数体保留。旧closure guard被明示的新wrapper和完整原体共同替代；原frame需要的run_chain守卫也绑定完整新正文，不删除。

`METHOD_SOURCE_OVERRIDES` 是完整literal函数正文。纯stdlib `complete_method_ast()` 从它计算新AST身份；未变方法仍用原METHOD_AST。新pure loader须提取这些完整常量/函数以及ast/textwrap，而不是import数值源或忽略新guard。

packet registry保留已有全部完整normal身份，再加新normal；它核新closure实际代码/policy，并把真实closure counters加入capture前后科学计数不变检查。capture仍不调用closure、root升级、frame或新端点读数。scope/point/rootpacket不是连续根唯一性证明。

## 8. 真实费用与轻量进度

34个计数键区分logical请求/返回/失败、真正original尝试/返回/失败、原angle-jet请求/返回、cache hit/miss/存储、强制stage/endpoint重读、各种旁路、key/point检查、scope开闭/异常、stage完成、peak entries/bytes与进度I/O。

原normal closure计数仍只在原公式的实际写点累加。logical调用不能冒原积分，命中不能冒科学进展。original积分时间、binding/key时间和scope总时间分别记录。scope总时间还含其他normal过程，不从两项时间之差猜精确热点。key全自由点读数也有真实成本，本件未预报加速。

可选 `actual-normal-evaluation-progress.json` 位于同科学outdir，是独立、可变的最新标量观察文件。它只读取已存在field/normal/endpoint/reference/closure counters、phase、point摘要和root-cache角数；不调用q.metadata/F/J/J*/root/quadrature。普通写入节流30秒，链进入/退出可强制写。stdout仅小事件，I/O失败不重启或改变科学。

上层必须显式接到支持活动进度读取的控制器，文件名和源码存在不等于当前旧child已发布进度。原09继续按实际记录。新上层可在初residual/statistics/scan前后加同一observer，但不能为了观察而额外计算第二次F。

## 9. 九完整源与纯再生

| role | 完整 basename | bytes | SHA256 | Git blob |
|---|---|---:|---|---|
| `closure_values` | `same_chain_detached_closure_values.py` | 54143 | `e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e` | `efb44b6f7547129d3c069c46e026e2caf6803203` |
| `analytic_J3` | `analytic_local_stage_jacobian_closure_values.py` | 25725 | `9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa` | `a5bd0c7e8734c30413dd08538ae20c72d8c37a3b` |
| `analytic_frame` | `analytic_normal_frame_jets_closure_values.py` | 47272 | `8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598` | `c040a321bc4384c2a2ea974eb4fb38c3ddfd6da1` |
| `frame_C1` | `normal_frame_c1_closure_values.py` | 37361 | `1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa` | `8985fdc75ecf023939c2e983e4a057fed8fc86be` |
| `stage_matrices` | `detached_stage_matrices_closure_values.py` | 47791 | `bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45` | `da63d2c4752666fdd8f07e552d0125e972977cd3` |
| `adjacent_matrices` | `adjacent_normal_matrices_closure_values.py` | 36766 | `6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650` | `c7227964a254c6f62095b96cc767433ac75ff1f7` |
| `reference_calibration` | `reference_centred_closure_values_calibration.py` | 11898 | `b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f` | `2a09886eab40902f326d8887a9e103d9eba35048` |
| `endpoint` | `so3_reference_centred_closure_values_normal_lift_operator.py` | 98421 | `6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4` | `93e28f0ef1571d9869519b91a6b051e60d1921ab` |
| `root_packets` | `immutable_closure_values_normal_root_packets.py` | 70992 | `31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805` | `598110c9548b29fd25a79d7e2acd6928f228db35` |

完整再生器 `derive_complete_detached_closure_value_family.py`：65607 B，SHA256 `28cf735308d5cba6e805cfaf66b219e21fe7e8295118776df8eff1fedc8a338f`，Git blob `283cb204d4090429b51275354177959ada73c9b8`。

~~~sh
python derive_complete_detached_closure_value_family.py --source-directory <完整scripts/resume_20261126目录> --output-directory <新完整源目录>
~~~

核既有九体再加 `--verify-existing`。该程序只读完整源、精确替换、反向恢复、AST/compile及比较，不import NumPy/Torch数值源或执行fixture。上层必须保留真实 `closure_parent_endpoint` role，即原3d8d完整文件，因为helper实际读取它。

本次实际完成云端逐字正向再生、八个父文件的全部反向恢复及whole SHA/bytes/blob保护；环境不可用，未冒称已执行Python AST/compile。再生器提供完整可复核操作，不是科学前门。

construction已独立定点核完整helper tracking/key/scope/计数与force重读，未见其范围内阻断；未运行科学、未测命中/速度，不代替上层真实input/source绑定。

## 10. 输入与历史边界

lower family不硬造run10身份。实际warm/reference、完整fixed target、当前scalar table、chart和所有适用parent/typed历史须由独立上层从真正返回文件核。旧09未返末点或typed顺序不能替换为空；原07/08未知结果保留适用合并责任。

run10当前准确积分表实际2218叶，run09为1995叶，run05旧材料地址重建用2397叶。三种责任不可混用。本缓存不继承旧reference数值、旧误差盒或证书，也不改变准确g定义或全问题完成标准。

后继science/pure、全部参数和进度selectors另由完整入口登记。不缩减原自由空间、32段、观测/筛查/永久点或原预算，不预填paid fees。新的实际完整输出决定下一步。


## 11. 根会话完整来源复核

根完整接收九运行体、65607B完整再生器及本证明，逐件核bytes/SHA256/Git blob；全部<100000B，未截源。根完整读新helper与全部实际来源修改，核八个完整父当前公开树身份；又独立按完整manifest逐字正向重放八体并逐字逆向恢复八父，均与完整交付/原SHA一致。原residual源码确在torch.no_grad范围调用完整场；这只是可达cache语义检查，不是实际命中/速度测量。新normal全部原数学函数保留，closure完整原体仅重命名，所有32stage最终C及final endpoint仍强制原公式新重读。

本条不改正在运行的09源或任何队列参数；完整10上层/source绑定与全部科学参数由独立入口继续接，实际target/compatibility须等本次真实完整输入producer返回。root未执行AST/compile或任何数值/interval fixture，所有科学仍限本公开Actions。

云API双README核至`d5fd8296c2abec83213675d826462bac17d0b21c`无字节变化；非根git pull。实际runner仍按原规则真pull/rebase，已读提交记HANDOFF。原07/08未知场/typed、06两分支历史及真实精化/闭面责任均保。
