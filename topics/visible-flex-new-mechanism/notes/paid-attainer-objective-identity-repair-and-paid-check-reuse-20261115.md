# 同m7评估身份引用修复与已付十六检查复用

## 为什么首入口停止

[首次实际收据](paid-attainer-first-checks-and-identity-stop-20261115.md)保留
run43771970034/source68f92b9cb16677278dfbc7f8e13bdf7189e41d9c的真实失败：
16条人工检查全过，真实构造器在评估定义哈希比较停止，LP11尚未调用。
其失败和准备费用不删除。

随后逐行只读冻结源码定位：首次transfer把原
complete_original_grid_model.summary.binding.full_grid_oracle_binding
中的ordinary_evaluation_definition_sha256，错误地用作完整objective的旧哈希。

原SelectedRadialJacobian把digest(field.evaluation_definition())写入
ordinary_evaluation_sha256；原CompleteDirectionalMetricOracle再以
ordinary_evaluation_definition_sha256保留此值。047cefae968152d170387cf64a9f7b0f132089685472c10868de9379967d93e9
属于这个底层field几何定义，不含objective上的配置、策略、controller及来源增量。

因此首入口比较的是两个不同对象的SHA。前设计/接线/失败记录将047cef简称
“原epoch evalSHA”的说法不准确；以本说明的两个明确域为准。尚不能仅凭这一
定位声称真实恢复必成功；其它原严格绑定仍在公开执行中核验。

## 两个身份各自对照原已付记录

原MODEL7同时保存正确的完整objective哈希。准确路径为：

    model7["linear_program"]["complete_original_grid_model"]["summary"]
      ["binding"]["selected_observable_binding"]
      ["external_current_cache_binding"]

这是coarse、fine的两项缓存绑定，各项evaluation_sha256由原
AffineSpectralHeight159Objective.primary_observable_model直接写入
self.evaluation_sha256。原AffineSpectralModel保留这个列表，完整模型再保留
selected_observable_binding，所以无需恢复旧LP10、旧p或执行新观察去寻找它。

修复只把原epoch_evaluation_sha256的来源改为这两网一致的完整objective哈希：
先核原网格标签/次序与两个值相同，再保留resume原来的精确比较。
047cef另以ordinary_field_evaluation_sha256命名，并与当前factorized的
ordinary_evaluation_sha256逐项比较。两种身份都不能跳过、互相替代或改成新值。
失败时输出两个域的expected/actual小标量，避免用大载荷猜原因。

完整objective定义仍由冻结父类、同一cfg/原sampling/source/pools/controller
元数据重建。历史initial375仍是原epoch开始的事实，当前恢复438仍另列；
两者不混标。实际A/J/targets/RHS、final factories、池、学习状态、bank438
和模型binding的原等值门保持。

## 十六条只复用，原依赖闭包继续冻结

修复入口明确移除developer_check调用；不把复用事件写成一次新开发执行。
先读取首失败job的固定日志并核：

- run/job均completed failure，source相同、run/job互相绑定；
- 原log430490B及SHA ba23313fae7855266456502ea1b5ac1f6b8d3799d5a833c6adbc749a1b3bd69d；
- 原REQUEST、DEVELOPMENT、PRIOR、COMPLETE四条JSON+LF各自原字节和SHA；
- 四组16条全true，原执行计数realLP/geometry/JVP/old-suite均0、
  仅5次新stub调用；
- 原真实错误确是定义比较，科学入口0、无MODEL、无新accepted。

首153文件绑定中只准许本次transfer/resume/audit/workflow四件有声明的文本改动；
其余149件，包括core、development、recovery及旧140Python/6workflow，必须同原。
当前全部153件仍按新request的逐文件SHA核验。
这不使用新的主LP、真实几何或符号执行来验证旧已完成研究。

成功源run43767357527仍只读其固定日志一次，旧18/20/19/26/cache继续原链回执复用；
不下载更早已失败的旧guard日志，不重播前六模型、旧LP10或任何旧方向。

## 失败费用继承与唯一未支付接口

原source snapshot计数单独保存，不改写成新的执行事实。
新inherited账在旧active35.54239845799998上加入首失败恢复
0.08626015199990889秒，即35.62865860999989秒；此后当前缓存、J、
新JVP、supports、trial及SOC都进入同一剩余120秒预算。

首失败prepare14.667315975000065秒累进初始化，当前必要准备的实际时间也
累进同一初始化字段。首失败进程总18.621493514000008秒另列，不因其中
元数据/读日志等工作不属于优化active而隐去。每次报告保原source计数、
既有失败成本、当前准备和当前恢复分段。

原共享值仍14、LP仍10/12、SOC0，未重置任何限额。
原一次接口仍只允许≤4合法unit-ball支持附于全部438旧行，
没有新支持0LP；最多一次新的primary ordinal11，必要时保原SOC12，
不开m8、不增加per-model3/全12/40value/120active/单LP10秒。
原十四物理门、修复候选门、SOC RHS、学习更新和controller全部保留。

## 验证范围与后续读取

本修复是在实际已发生的身份错误后对来源路径的最小修正；
新增代码仅做有来源的收据读取、两种定义域核对与累计成本。
原人工16条已经通过，不再执行。首次修复运行仍须先实际pull并核双README、
核私有QUEUE，再进入尚未调用的同m7接口。

以该公开运行的真实恢复、完整模型绑定、LP/JVP/trial及门收据判断结果。
无论该有限接口结局如何，都不将其视为主课题完成：
同固定g、全时嵌入、连续reach、1e−6 metric精化及宏观握持幅度仍按README逐项支付。
