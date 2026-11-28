# 真完整 full-H 闭图的默认查询已实际返回

## 真正返回的对象

冻结 `actual_closed_map_v2.py` 的完整查询已实际 exit 0：λ=0.002/M24 原真实前缀、新 factor1 raw H 尾的全部1152段、完整全局 mean、真实 deep zero-jet collar及两端 regular disks，共同进入一个明确有限图。这里仍未声称 λ=1、coupled physical H 或 README 完成。

实际 report：`/workspace/scratch/7c4e33ee17de/held10-design-work/actual-closed-fullH-20261128-b/report.json`，SHA256 `374b6d60e7baaa48f57c3e2912ab3e9d448a8a6cc8018ba4c36e540d02903d0b`。完整 bundle 与真实分批 anchor 组装来源见 `2026-11-28-tail-actual-complete-geometry-bundle.md`，本次再次实际重验全部公共节点，索引逐项相同。

在3个 phase（0、0.17、π/3）、上下两侧及5个角度，总共30处 cut 比较的六jet样本最大差，按 `(F,F_s,F_ss,F_θ,F_θθ,F_sθ)` 顺序为：

`[2.5438405243138006e-16, 2.2366973658179873e-16, 5.289967607552062e-16, 8.326674449340461e-17, 1.2412670766236366e-16, 2.9307840470773572e-16]`

最大分项为5.289967607552062e−16。42个尾/内collar/极点查询均返回有限值。tail cut 的数值重参数差为0；严格的完整源半径恒等由独立证书入口另付。

本次使用默认 marker=0、中心柱半长=0。因此 report 中中心柱比较数组的零值只是未执行分支的初始化，**不作为新增中心柱验收证据**；同一源的中心共享定义沿已有前缀证明。默认 marker=0 的图也没有获得严格非全等结论。

## 数值评估和实数定义分清

极点高度数值评估为 `0.8699871644620787`。其数学定义是

`Zcap = zcut + mu_cut + ∫[a,Rc] w(R) dR`，

其中背景采用已固定的 R58 真积分函数；`self.Zcap` 和 report 的 approximate 字段只是该表达式的数值评估器，不能另把圆整后的高度当定义常数。cut 的 `ap/app` 同样沿冻结v2文档给出的唯一实数表达式解释。

## 真实失败与最小独立报告修复

第一条真实查询在完成几何查询后、序列化 report 时 exit 1：NumPy `longdouble` 样本差不能直接交标准JSON。旧退出、日志和完整71.67062375300156秒墙钟均保留；墙钟包含真实128MiB写门等待，未测得单独纯计算耗时，不把相减估计当实测。

独立 `actual_closed_map_numeric_report_v3.py` 调用未改动的 v2 `main()`，只将JSON无法展示的有限NumPy浮点诊断转换为Python float；原数学source SHA仍为 `3742d3041daad388cc26d63fb7e4300732459f076327938a39ef92b7f3603ee5`，全部几何运算、源核验和原门不变。记录实际发生12次 longdouble 展示转换（写出与打印同一6项）；它不是向外舍入上界或连续证书。必要重查的真实墙钟25.103583432999585秒，观测子进程maxRSS252024 KiB。

## 当前继续做的工作

实际完整图可查询和共享两jet的定义已经具体化。连续全尾metric/curvature/deep collar、同图physical-R cut补偿、全局reach/held/非全等以及固定同一g的加密仍需各自实付。原全尾证书正在运行，已出现局部上界未过的真实结果；不会用上述样本差替代连续门。source与命令、真实返回、旧失败及小标量详见同名JSON，数据留在scratch。
