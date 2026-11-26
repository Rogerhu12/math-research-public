# B030：从实际自然终态做工作行可行回溯

日期：2026-11-26。明确的新优化输入；**没有本地科学执行**。
来源为 run45828479581/job139938706452 的真实自然FINAL，
由只读恢复 run45844119049/job139993191345完整取回。
见[原收据](2026-11-26-r566-working-rows-natural-final-and-log-recovery.md)。

## 1. 针对实际失败原因改什么

原输入在2370.471193446秒内完成326个工作Jacobian，
322次callback因working不可行而直接拒绝；只有2次试探进入完整coarse，
没有一次进入完整fine或角定位，接受0步。
它已经减少了矩阵大小，但没有把许多接近working可行的实际试探送到完整物理资格检查。

本次保持原物理函数、子径向1536整圈meanE、所有完整约束和接受规则，
为原后端实际trial加入一条明确的可行性回溯。
从真正保留的q到这个trial按 $1,1/2,\ldots,2^{-16}$ 缩短，
同时对后端epigraph变量作同样线性插值。
只有完整working行在原容差内的点，才继续原全部coarse、
fine3072、真实角峰定位、nested FFT及几何margin检查。
缩短步若最终真的接受，立即在新实际q重启后端，不让SLSQP继续假装自己接受了原大步。

这不是把小工作违约当合格，也没有把一个小epigraph当真实eta。
回溯耗尽就保留实际q；原Phase I仍处理新物理库揭示的几何恢复。

## 2. 完整实际输入与字节身份

实际起点保持：

- 原81q binary64 SHA
  `7e708ba7a973e8505a81e94073707e8c39504d1f3285253f97e3564382992080`；
- 571个真实必要径向节点、1276个实际峰轨道、1536整圈FFT；
- 150个已经选定的working行；
- actual和proposed trust同为0.3003387451171875；
  原最后outer的trust决定未完成，本次不会再凭空适配；
- pending物理峰0，pending working行0；
- 原末q的既有fine/峰资格约eta0.25895160785933824，几何工作违约0；
  所有连续指标仍未认证。

新输入用原已发布请求191771B/SHA
`6756f5945133fd9f3f747906f43ec3befaacdde3e3404c036bb4bf1ae33cd4b4`
恢复完全相同的q、571r和1276峰，
再加原FINAL中其余的准确JSON文本，重建整个132427B FINAL并核对SHA
`913c9cfc28e19e0b237d4cbbefb080d7a70b30b545e30754706f4e1ddadd1761`。
这明确保留所有actual/候选/成本身份，避免重复复制早已绑定的物理坐标。
原最后SLSQP点和未接受trial都只留作来源记录，绝不升级为起点。

本次输入68419B/SHA
`ca077d4b2415cd79d9664c25265ec7235ad894cb35d6651ae04f164654480b13`，
只作为这个明确后继科学请求的参数，不作为独立raw/checkpoint文件提交。

## 3. 回溯基必须是真可行的epigraph

源最后实际BACKEND_START的working基epigraph是
0.25895161785933823。它与后端最后失败trial的epigraph不同。

本次把这个值作为持久实际状态：

- q和完整必要库不变时，下一outer直接复用已付选择和这个真实可行基值；
- 新物理节点/峰进入必要库后，完整扫描当前实际q，重新选择真实phase/working见证，
  并保该扫描实际给出的extra；
- 完整接受新q后，保通过全部门的实际候选 $v[-1]$；
- callback回溯基和下一outer的 $x_0$ 都使用同一值；
- snapshot显式保存它，不由fine的best_eta重新推算。

这样避免新库的coarse峰高于旧fine eta时，回溯反而朝一个不满足当前working行的基点移动。
若Phase I已恢复到几何可行，下一outer强制完整选择metric见证，不能继续只有geometry的矩阵。

## 4. 哪些算子与完整门保留

新driver按SHA绑定并直接调用原
`r566_working_rows_full_acceptance_20261126.py`
的 WorkingRows、candidate_rows、角oracle、物理参数、row键、节点追加规则、
原双层完整扫描/定位与原SLSQP。没有另写一套几何或AD。

working选择仍只限制局部矩阵，不改变真实问题。
全部571/1276原必要约束仍保留；新的物理峰仍完整记pending，
未选入小矩阵的违规仍拒步。
进入完整资格的候选必须依次完成：

1. 全必要coarse uniform行和所有真实峰轨道；
2. 全fine网与原nested均值/metric/曲率差门；
3. 原连续角bracket的全部实际定位与原几何margin/epigraph检查；
4. 原严格实际改进或真实几何恢复条件。

没有接受旁路，最后trial仍单独记录。
这里的“连续角定位”保留原数值观察口径，不被升级为连续覆盖证明。

## 5. 减少无新信息的重复成本

原自然终态q/物理库未变且已经有完整必要扫描，
本次不用它们重新做一次seed-selection baseline。
工作行或物理库真正改变、需要新phase时，才支付相应新的完整选择。
任一新接受点仍完整过所有物理门。

fine oracle只在一个新trial已经通过working和全部coarse后创建；
没有通过的点不先构建大fine对象。
原同一 WorkingRows 内部的fun/Jac key缓存保留。
前run没有输出完整Jacobian矩阵，因此不能假装旧矩阵现在可免费读用；
新优化所需的真实Jacobian照常计费。

已付restriction mapping方向观察不再执行。
本次没有新物理算子或新的径向限制映射，不重跑旧parity或旧Jac门。

## 6. 每个边界上的真实状态和费用

每次接受、实际库交换、outer完成、clock或异常都写完整快照：
实际q、资格、完整物理库、working库、pending、实际/拟议trust、
持久working基epigraph、原后端trial、具体回溯分数和完整费用。

纯working回溯失败不会改变实际q或pending库，
因此只输出小的拒绝记录和费用，不再重复打印整个未改变的132KB物理库。
最新完整状态加这些明确未改变实际状态的记录足以区分：
真实保留点、原后端提案、最后检查的缩短点和未完成的当前评价。

回溯在每个新原子评价前检查clock。
如果clock发生在子网评价中，最后记录保留pending fraction，
不会把未完成的评价记成合格或把trial当实际状态。

所有旧已知科学秒数、原未冲刷成本区间和本轮新操作分列。
原科学总下界5246.342038514秒保持为下界；只读日志恢复是0科学评价。
新的backtrack proposals/value trials/recoveries/exhaustion和完全接受的缩短步分别计数，
并保原live/retired oracle和完整Jacobian层级，不能重复加总包含关系。

## 7. 发布范围

公共单job，科学2400秒，预留30秒结束记录，job50分钟。
原物理/数值容差、最大1025r/2048峰/512working容量、1536/3072角、
原120outer/80内部步和完整角定位不变。
仅新增最多16次二分回缩的真实globalization。
根runner仍先actual pull两仓规则并核来源，科学前移除凭据。

本地只进行源代码纸读、AST、JSON/hash及原状态字节映射。
原完整FINAL恢复hash在纯元数据操作中吻合；
这不是新的几何评价或旧科学核。

这次输入仍是静态度量设计，未达到题目固定度量、完整嵌入族、宏观握持变化或reach完成标准。
它只是从具体已见的工作行不可行瓶颈继续真正求解，不会以回溯接口本身收尾。
