# 实际19–20：固定moment-Q初根仍失败，转向固定支撑的准确必要式

日期：2026-11-26。状态：**真实数值失败归因；不构成根不存在、度量或几何结论。** 来源是公开 [Actions 45820592817/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45820592817) 的[第4卷阶段19](2026-11-26-public-actions-45820592817-1-part-004.md)及[第5卷阶段20](2026-11-26-public-actions-45820592817-1-part-005.md)。

## 1. 新输入确实被执行，来源与模型没有错绑

阶段19执行完整新source/schema链：

- driver fullclosed_zero_moment_so3_qp.py，SHA256 ff500abfa24de27c22f8a8993b9104cc265c5c96289a927c18755d318fbf0766；
- endpoint so3_zero_closure_moment_operator.py，SHA256 44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e；
- 完整base source 7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf；
- launcher 082bb92e0e9f01067cf1bd8ecaae65cb559e38bba90dd79b97bf492c11d758f4，实际提交5b6f4a6753898fdcdb6b2c3b3cbd6e6f368fb8f6；
- 18参数完整definition 05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e，全部hex再次实际返回，Q_recomputed=false。

新模型身份为
d03587cb5195b02157222edf13e32c8e84c2681672362fefefc6dbbf45442707。
base模型仍为9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258，
实际初始参考包0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1，
固定标量6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb，
完整初始自由点cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3。

原1333370自由量和45324288个完整metric标量行均保留。实际显式政策是原wide两支撑、根半径0.75、容差2e-12、24次Newton、18次回溯、Armijo1e-4。未改H，未借用hDelta接受场，未继承旧模型的球或连续证书。actual19的失败发生在真正初根读取，不是setup/schema/来源错误。

## 2. 真实失败读数

阶段19 child在11.023559466999359秒返回exit1，完整report成功落盘，complete=false，stop_reason为actual_initial_zero_closure_field_read_failed。阶段20的完整纯reader exit0，确认同一来源、同一目标、同一18参数和下列真实状态：

| 项目 | 实际返回 |
|---|---:|
| 第一失败角索引 | 5 |
| 失败角数 | 1 |
| 最大实际校正坐标范数 | 0.4392978790956161 |
| 最大实际端点残差 | 0.034892231118679465 |
| 实际root回溯角评价数 | 432 |
| 已完成返回的root计数 | 0 |
| root失败计数 | 1 |
| implicit块/角jet升级 | 0 / 0 |
| metric/restoration方向 | 0 / 0 |
| initial/final checkpoint | 均无 |
| initial/final Phi、max、几何通过 | 均未定义 |

异常的确切理由是“No actual endpoint-root backtrack decreased the same complete equation”。最大校正坐标范数小于原0.75球；这个汇总值本身不记录所有候选点的admissibility，不能把它扩大成“每个回溯候选都未触球”的新事实。阶段15旧Q的最后实际候选球内证据属于其原轨迹，不能拿来充本次新Q全部试探的逐项读数。

root_iterations字段为0来自原计数口径：成功完成的整批根才累计该项。432次实际回溯角读取说明已经尝试求根；不能把0计数写成没有Newton尝试或未执行科学。失败后没有把任何部分根、零向量或未闭合初点伪造成接受场。

新报告路径zero-closure-frozen-moment-Q-first/report.json，101302字节，SHA256
74754423cf22b677616f69f4416d4b843c827f64a0b34943e01f274487df66d9。
命令报告13119字节，SHA256
1d3e451e070f79bf06528f56bab74d8de1d7e874931f0d13c77c0bb7c91f8dc5。

纯reader为read_zero_moment_so3_report.py，SHA256
c942aa60db84698215e53dd2427a19c693ca73e6c3c8553ef0b73fa75edf295a，
源码提交460943a687d9261039796200bd16e7c167be6c3d。
其输出postprocess/zero-closure-frozen-moment-Q-first-readout.json为31670字节，SHA256
e4dc89acbf6bc07715d3a023605c47bccfd0c1f45a14c19e27f35db94d42cbd2。
两步summary_errors和missing_outputs均为空；没有读缺字段造成的伪失败。

## 3. 与旧失败相近的残差只能作线索

旧Q实际15的最大失败残差为0.034892231118679326；本次新Q为0.034892231118679465，且第一失败角仍为5。这提示应检查同一初始端点/支撑容量与所遇路径，而不是盲增根球或重复相同Newton预算。

但新Q一般不是旧W的同一个3×3右坐标变换。原第一泡泡控制映射的z输出行恒零，实际新字面Q第一矩阵的z/t条目为0x1.956cca02ca83bp-3，准确非零；它可以改变所选有限控制子族。不能因两次残差相近便把两个物理控制族认成同一个，也不能从相近浮点残差证明一个真实正残差下界。

此前工作初始导数接近I的候选诊断也没有支付全域可达性或非线性根分支。更好的工作初始雅可比不等于最终方程一定可解；本次完整执行恰好没有得到接受初场。

## 4. 下一短计算应检查固定支撑外的完整贡献

在当前完全相同的初始core/H、omega=0和两固定wide支撑下，旋转在支撑外等于恒等。令

$$
U=(S/32,15S/32)\cup(17S/32,31S/32),
\qquad |U|=7S/8.
$$

任何支撑在U内的单位旋转闭合场均必须满足

$$
\left|P(\phi)-\Gamma(\phi)-\int_{U^c}T_0(s,\phi)\,ds\right|\le7S/8.
$$

原因是把准确端点积分恒等式的支撑外部分移项，再对支撑内单位向量积分取三角不等式。它不依赖旧Q、新Q、Newton、延拓或球半径。补集的三段
[0,S/32]、[15S/32,17S/32]、[31S/32,S]
都必须保留，包括完整准确尾部；不能删小尾或用浮点工作积分代替准确盒。

完整证明/可执行后继另见2026-11-26-supported-initial-meridian-chord-necessity.md（12456字节，SHA256 add74ba6e3393e4c9e366ae3aff96786e16d8222b38bedf11d59d1e1e423958d），源diagnose_zero_supported_chord.py（22474字节，SHA256 55ad7d082c53ed65746f5287abdd1c9aad3e29cc47e1c6f202b8327f8f63f82b）。

该诊断通过原434132报告的完整6578输入绑定读取真实cd530初点。它与本次747544报告共有相同完整初点、固定目标、reference与支撑；利用的是同一准确输入必要式，不是把旧零模型证书贴到新模型上。正式[完整参数](../computations/zero-initial-supported-chord-ready-steps.json)为6639字节，SHA256 9dc3bc9f77711be031e00a1bb4a145e9a39d16b76bf51afeb1ccf0d516b19e8b；相对79952daf准备版只把activation元数据改为本次实际19/20之后启用，全部科学argv未改。本文写作时该新支撑诊断尚无实际返回，不能填入成功、失败或任何上下界。

若它在某角严格违反必要式，则这个固定初始输入在该支撑下不能闭合，和Q或求根策略无关；结论只针对本初始core/H、omega=0及固定支撑，不是完整自由场、其它输入或课题的障碍。若必要式通过，则仍不是指定有限控制族或0.75球内根存在的充分条件。

## 5. 同方程延拓保留为独立可执行候选

完整残差延拓候选已经备好：固定同一新Q与当前x，求
$C(z)-(1-\lambda)C(0)=0$，从0,0推进至lambda1，最后重新读原C和原Cz。它保持原球与最终残差条件，最终角jet/J只用原方程，不对中间迭代求导。其完整源/参数和条件说明独立登记；没有本地科学运行，也没有继承首轮失败场。

这个后继只处理求根路径。先读支撑必要式的真实返回，可以避免对已经由准确支撑容量排除的固定初点重复Newton/延拓；若未排除，再由实际诊断选择完整延拓或不同物理输入。相应路线与新的R696角向单位表示可以独立推进。不得用小于1的辅助lambda、改大球或删行来宣布完成。

本次初场尚未成立，因而没有新的Phi改善、几何检查、固定g精化或课题完成结论。失败已完整记录，研究继续。

## 6. root实际读取及排程

root亲读公开实际17–20原紧凑JSON，核本次19/20全部来源、错误文本、root计数与未定义字段；并复核原5b4第一泡泡Q1的z输出行为零，故本条关于新控制子族不同的说明有完整源依据。另全文读取55ad完整源码及上述12KB准确必要式证明，保三补段、真实尾、半径代数抵消、全角/全core和原root零调用。

支撑诊断已追加03b活动队列，顺序在已排R696首轮及其纯归因之后；当前没有诊断结果，不取消已在执行的完整科学方向。辅助残差延拓未排，待该必要式真实返回后继续选择同方程路径或不同物理初输入。这里没有以等待用户回复为下一步条件。
