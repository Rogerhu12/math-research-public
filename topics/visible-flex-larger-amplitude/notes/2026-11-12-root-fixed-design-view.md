# 接受设计态的真实固定度量视图

## 实现与目前实际验证的范围

`root_actual_freeze_design_view.py` 是第二次执行器切换后重新实现的版本；没有冒用丢失旧版本的SHA。它将来用于接受的27参数实际设计端点，取最终物理profile并只去掉三个设计offset，同时保留原24个核心参数。当前只对已固定的q095 M24输入完成了身份核验；**实际27→24分支尚待新的接受端点出现后运行**。

该入口通过真实 bounded/fixed/actual 工厂构造对象，恢复原 numerical reference knots，加载原完整x/y/cubic与p，不做pullback重采样。使用原始数值三次多项式重新计算配点RMS；用同一完整H处的真正已审计尾端响应检查全部97条固定边界条件，包含未缩放physical BC。禁止启动尾worker，也不调用Newton或大Jacobian。

所有物理五次系数块按原SHA共享，完整x/y/cubic块不复制也不改变。若参数或重新计算的RMS确需新块，只写对应的小块。新raw identity由真实Fixed对象生成；新文件明确记录它是接受态的表示转换，不是新物理解、精化或无限尾闭合。

## 正式核验

会话27791正式exit0，171.5999904秒、wait4峰值126476KiB；CPU约33.44秒。M24/N768、2004节点，八项物理数据、原数值图、全核心和完整H均保持。

| 原门或身份 | 实际结果 |
|---|---|
| 原RMS最大值 | 9.976296746350968e−8 |
| 原完整RMS数组之差 | 逐位相同，最大差0 |
| 全部缩放边界最大值 | 3.0200516839669565e−12 |
| 真实physical BC最大值 | 3.0200516839669564e−14 |
| raw恢复 / 原残差检查 | 各1次 |
| worker启动 / 新Newton / 新Jacobian | 均0 |
| 原x/y/cubic及物理五次块 | 原SHA共享，未改变 |

新视图 `2026-11-12-root-q095-fixed-view-identity-r1.json.gz` SHA
`925994ffa7a015d13a84b98b0545e1992e4463f74307e9a05e9ff815cd4eb6b9`；新raw manifest SHA
`db41c63096e97b8e1dfda606d583f9a62fd96a315477518b41073a10d1df8db2`。

随后现有 `strong_actual_fixed_control_response.py --metadata-only` 实际exit0，确认新视图可以通过现有完整固定输入协议：M24/N768/2004节点、原完整H逐位同、参数布局与真实尾源/配置匹配。该后续检查只有标准库数据读取，没有新RHS、Flow、Jacobian或BVP。

## 后续使用与限制

接受27参数端点后，用其最终完整main/raw/tail和原tail-config运行同入口，不把p末三项再加到已经最终化的profile上。原始门不能放松；通过后才能用于固定g的M28加密与完整控制响应。当前q095的Darboux、C²粗细差和无限闭合缺口完全保留，本次身份核验没有改变这些误差。
