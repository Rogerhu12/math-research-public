# 三重对称小cut：真实非线性联合、同g径向对照与独立开放前缀延拓

维护：Astra-held10-f00f08c9-20261117。分类：**有限数值结果；尚无本题10%闭候选**。

## 1. 原方程的q02真联合

使用原950f worker、全部非线性均值及原接受门；cut r=.3/w=.08，原m3六个谷控制，spacing3，8圈、144stage，projectionFloor=.05、shootTol2e−9不变。前缀vu=.45/vd=.50，flat ramp .4/eta.05，ShortBridge K4/p.2，实际联合δ=.06105607686781097。正zr尾消费完整−H，反射整个尾z与mean后接上片，切口角是材料角。

暖路径并非一次冷启动：先用fast55 q02的完整H到−.3，直接−1的Newton line search失败；再换fast45完整H，由−.4…−1逐步接受。真正联合随后重算prefix、完整tail和高谐波，不是缩放线性端口。

| 实际有限结果 | 设计q=.02/M8 | 同完整g固定M8 |
|---|---:|---:|
| 实际核心q | .02 | .020001225073149356 |
| prefix节点 | 743 | 983 |
| prefix tol | 1e−6 | 3e−7 |
| prefix metric FFT l1 | 2.7467254e−8 | 4.9706313e−9 |
| prefix全Cartesian tensor FFT l1 | 2.9745911e−4 | 9.0149823e−6 |
| tail fullD | 2.3438393e−6 | 2.3453588e−6 |
| tail实际metric | 3.1843594e−10 | 3.1863756e−10 |
| tail minA | .442031289 | .441994328 |
| tail形式K | 8.04068687 | 8.04069205 |
| 完整mean/nonmean高度二jet缝 | 4.01644e−9 | 6.16551e−12 |

两行全物理g descriptor SHA均11a9de4da186d04dd1e925678582b0f6861425b4e0e2217937ec53ba052db125。固定行既加密径向tol，也按原fixed源码把全部角样条分段点加入径向mesh；不能将33倍tensor下降单独归因其中一个改变。两层不证明收敛，尾M8未改所以二阶误差未下降。

## 2. 实际接缝及插值缺口

512同材料角，只有一次全局Rz/平移，设计q02的X/Xs/Xu/Xss/Xsu/Xuu最大接缝差为4.113e−12、3.556e−10、7.704e−12、8.601e−9、3.453e−9、2.667e−11。tail平面rr仍为原四阶差分h1e−4；不是区间界。最外stored momentum严格按原cutJets乘2^a。R12提供精确结构，本批只是实际数值核验。

设计前缀的最大tensor在s=.1062754286的单元中点，单元跨过角样条结点5L/64=.1062770425；所有已存节点tensor≤1.044e−9，而真实C²五次插值的该中点Gauss缺陷1.289e−4。投影ODE二jet给小值只是诊断，不能替掉实际插值。固定M8含断点后该峰消失，但末端bridge仍有约7.34e−6的Gauss缺陷。仍须改进真实C²代表。

前缀采样maxNorm1.145729193、support .803179078、K8.050355；有限尾增高.0225432431、maxNorm.841287496、support .787232472、实际K8.029307、全tensor1.1354e−6。2×prefix maxNorm=2.291458385只是采样包围值；无限尾/连续几何未付。核心相位支撑差约.04是绝对长度，除该D仅约1.75%，更不是完整整像见证。

## 3. 独立的线性DN开放q04/q06

同一类小cut设计的q04从q02成功；q06的两次单态缩放初值分别在Frenet域失败，保留完整错误。用q02/q04成功点作secant只改初值，原方程/guard/tol不变后q06通过：metric1.14360e−7、K9.41070、高.78267573。这些是**线性DN**开放前缀，δ随q变；既不是同g精化，也不是q06真尾成功。完整q02/q04/q06原argv与hash已冻结。

## 4. 恢复与局限

实际联合入口：scripts/nonlinear_tail/m3_coupled_seed_deliverable/notes.md和replay.py；21文件manifest SHA707fc801979a9629b6612563f9d415b03e4217a794a2975399d0f20fb4c31aea。开放secant入口：m3_secant_deliverable/README.md；manifest SHAf58cc2bfad2d99f7ab4f24b9fd3f2d6e78fddb29870b6eca73f1dbeb585a07f9。

70份源在空目录恢复后，原worker canonical8逐字同SHA2b036a6f926503f46dddf41c8e141c215dc45340c556641d2fd2b6c192b62365。另实际Cartesian exporter也与原源逐值相同。所有DN/H/chart/mesh/checkpoint数组只再生到scratch。fast55早期初始nodes/restart未存，其已核数值设置保留；重放明确选冷401节点/max4000，不伪称原历史argv。

M16固定g的最新原shoot暖启动已经终态失败，残差6.87e−7未过原2e−9门；这是逐stage Riccati校正图条件数约1.28e11导致的数值分支失败，minA仍.44095，不归因A零或几何不存在。该失败另包登记，现尝试M12及不消去局部Riccati图的全shooting校正；原方程和接受门保持。所有闭合/全时reach/10%完成缺口仍在。
