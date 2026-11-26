# 2026-11-26：实际 theta 末态与完整 pending 库的 513 容量续接

这是对自然完成的 `45785004209` 两 lane 的明确续接实现，不是旧 joint 输入复跑。原单 lane 收据分别为 `2026-11-26-theta-peak-b030-first-real-angle-receipt.md` 和 `2026-11-26-theta-peak-b038-first-real-angle-receipt.md`。仅做本地源码、AST、源绑定和已付日志的小配置一致性核对；本地没有导入科学模型。

## 输入与唯一容量变化

| lane | 原实际 radial / 峰轨道 | 原未采用 radial / 总峰轨道 | 本次起始采用 | 原 actual trust | 原 next trust |
|---|---|---|---|---:|---:|
| B030 | 257 / 258 | 275 / 287 | 全部275 / 287 | .533935546875 | .533935546875 |
| B038 | 250 / 213 | 303 / 268 | 全部303 / 268 | .2669677734375 | .2669677734375 |

所有 actual 的完整1536角均匀约束保留；全部 pending 真实角峰轨道也保留，峰库不清空。q 逐项取原 `actual_terminal_state.q`。特别 B038 原最后trial虽eta约.5993，但因几何违规被拒，本次不取它，取原保留q（eta约.6505887）。原actual trust和原next trust各自保留；初始求解采用已登记next trust，没有任意重置。

容量参数只从257径向提高至513，支付本次已经明确发现的275/303位置提议；extra-peak上限1024、1536 FFT规则、角定位、硬几何、工作余量、所有交换/接受规则、局部盒规则和2400秒时钟都不变。新径向初始网格的重建、完整细扫与后续运算全部计入本次科学成本。

## 源码结构与未改的计算

新入口 `scripts/inverse_r566_theta_peak_resume_20261126.py` 绑定原 driver `6094c15ff2696d6b64e9eac09ce60b54a59a64c545cb88fb7734df8bb185f757`。全部物理、FFT、参数AD、CombinedRows、真实角定位、实际/细网比较等函数直接使用该已发布模块，不复制或更改其公式。

主循环是原 main 的静态源码副本，没有动态exec、AST修改运行器或隐藏hook。差异只在：真正 theta 末态的source loader、恢复 actual+pending 峰库、513默认容量、声明复用已支付的接口核，以及早期退出时保留来源actual状态的初始化。回调、接受、立即交换、pending批量、trust变化及最终扫描算法与原循环相同；静态比较可将这些明确入口差异还原后与原main逐AST比较。

loader 拒绝旧 joint schema；绑定来源run/job/source、原FINAL和原日志摘要；核查物理预算、全部actual/pending径向位置与实际角轨道、1536规则，以及分别记录的trust。它先打印 `THETA_PEAK_CONTINUATION_INPUT`。在新模型尚未构造完成的早期边界，仍保留来源actual配置；只有本轮 `make_oracles` 成功后，才把新采用网格记作actual。

## 已付接口核不重复

本次两lane source里分别保留原检查记录的字节数/SHA256和紧凑数值字段：原uniform parity逐项0，offgrid方向差B030 `2.56613526384312e-10`、B038 `2.796342280792686e-10`，各自91点坐标身份。它们来自同一原driver、同一oracle、同一1536 FFT规则的正式run。

本次对该同一算子不再执行parity或方向差分，声明 `new_interface_checks_executed=0`。最终字段使用 `source_interface_check_previously_passed`，不冒称本次重做。来源检查的原日志行仍只在scratch；请求只含摘要与所需字段，不存原日志。

## 公开执行与末态口径

新请求 `computations/request-inverse-theta-peak-resume-20261126.json`，新workflow `.github/workflows/visible-inverse-theta-peak-resume-20261126.yml`。传递依赖包括原hard-resume，完整10个源码/workflow绑定都进入sparse checkout。沿用真实公/私两仓pull及规则核查，Python3.12.14/numpy2.3.5/scipy1.17.0，两个固定Actions SHA，2lane/max2，50分钟job、2400秒科学段、只stdout，不artifact/cache/Git写入。

每次新actual、pending、保留q、最后backend trial及自然OptimizeResult仍严格分开。旧run已经闭账，容量变化不会把旧pending改成已采用；只有新run真实执行才更新该身份。全部计算仍为可变设计g，持续欠固定g精化、连续全域误差与全部reach/闭体门，不作README完成声明。
