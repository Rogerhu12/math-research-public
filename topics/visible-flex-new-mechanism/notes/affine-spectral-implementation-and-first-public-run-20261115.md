# 仿射 e/f 谱模型：首公共运行接线及静态审核

日期：2026-11-15 14:02:58 UTC。本条是实现与首次执行计划；**尚未运行新开发或新科学，不报告通过，不归因旧m6，不宣完成。**

## 为什么新增这个模型

上一真实运行43716860154/a7bb0a16的m5成功SOC保持了半径，m6确实用了该半径，却仍得到约0.11484的base-total预测比值。旧输出没有原e/f导数，不能回填误差原因。本次保留原谱范数曲率，只把e/f在同一实际接受基点仿射化，所有真实几何门、159坐标与163物理系数定义保持原样。完整推导见[设计](affine-spectral-metric-model-design-20261115.md)。

## 精确冻结的五个新增源

| 源文件 | 字节 | SHA256 |
|---|---:|---|
| frame_metric_affine_spectral_model.py | 30704 | `da7fd80070f428de904ea018098a59d811a90d9d54d5ca67a8ed3d3a0b6403a8` |
| frame_selected_row_metric_observables.py | 13157 | `83ec95f6a48a01e0da7cb034a4c7615864f6e896ca088e99dcd17168de1a0754` |
| frame_metric_height159_affine_spectral.py | 38294 | `5506a1696290869f1d0d7a2ef914663c09435d5d6f17b75c94ddb6cea8aae86d` |
| frame_metric_affine_spectral_development.py | 18962 | `024d2d6e5ff2e537acf3d661931cba0d3380a89baeee19f8aee69ec0b0775482` |
| frame_metric_height159_affine_spectral_audit.py | 70899 | `a62c20944a66a04679a5ae4a156e2e64b4e9331d976125a3f23a1a2356a2df4c` |

[请求参数](../computations/request-continuation.json)绑定50份源码：47份科学源以及工作流、发布器与原结果读取器。原98个研究参数只改第49个输出名，24份解码输入SHA不变。原8个必要阶段依次为growth、strip、SOC、body103、tail154、已声明容量159、已声明容量SOC-hold、factorized-selected-J；每个仅一次用于本轮输入恢复，费用独立，不当作新科学下降。无需第三次容量reserve，不强迫历史最后系数/hash或半径。

## 求解、成本与误差账

新lane为`metric_height159_affine_spectral`，新开发flag为`--check-affine-spectral-only`。每outer最多3次primary LP、最多2轮新cuts，全部计入原共享12 LP/40值/120 active秒，每LP仍至多10秒。返回预测始终是完整norm模型的rho_aff；修复辅助量rho_hat取rho_aff与LP返回rho的最大值，连同原h变量重新验证全部原单位残差。按rho_hat加原物理步惩罚选incumbent；有限正常停止可返回合格点，抛出的错误由原外层保最后真实接受点，不冒已选proposal为接受点。

原SOC仍用同一p的最低scalar slack及其原RHS，另记录较弱affine假想RHS但不使用。每primary/SOC/arc候选的质量统一按实际浮点总步candidate−accepted-base评价同一个affine模型，原17个hold守卫还检查新observable绑定。

每已实际评价的trial分解谱norm曲率、真实e/f非线性、全网遗漏行与ε平滑偏差。只消费当前原ordinary缓存，fine未评价时只报告coarse部分，不产生额外值调用。直接norm余量与稳定恒等都保留；浮点负微量不截为零，稳定式分母舍入为零则明确不可用。紧凑summary与逐模型stdout保全部新inner-LP、误差和SOC预算分账，不能仅由成功退出推断这些量。

## 静态审核与公共首次执行顺序

root读取原outerloop、缓存布局、原SOC API、新开发与编排；mechanism独立核切平面/辅助量/预算、直接e/f观测、最后真实控制器与第八handoff。原Field/H/reference、精确159→163、完整11组池ID/历史/容量和原末验均保。源码hash和98参数差异仅作元数据核对。没有本地import、开发、求积、优化或科学测试。

首次语法编译和所有新人工检查均由公开Actions完成：新数组norm/cut/账本/异常组、真实小fixture的de/df与缓存组、新第八handoff元数据、新八输入编排字典stub。未调用已完成的旧developer入口。通过后才进行八必要输入恢复和唯一新stage；失败保原错误与此前真实输出，不启动新科学。随后按两网全部原门、精确盒、初终eta、实际费用、逐模型误差、实际hold/controller消费结果。运行号及实测结论另行即推，所有可重算payload仅runner临时，不入仓库、artifact或Release。
