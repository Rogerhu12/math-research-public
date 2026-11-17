# q=.060 原联立续跑：旧H尾过门，新H实际尾仍失败

2026-11-18，Astra-held10-7322d0de-20261118。

本条接已登记的 `q060-local-relaxation-tail-acceptance`：原局部初值松弛使旧H的实际有限尾通过2e−9门，随后以该尾为初值接回原 q=.060 前缀—尾联立。完整进程36748已真实exit0，资源观察终态为2026-11-17 23:13:58 UTC；原wrapper捕获了下述异常，所以exit0不等于联立成功。**没有新的 q=.060 accepted prefix，没有最终全metric。**

## 同一新幅值设计，恢复已有实际尾初值

原 q=.060 输入 profile 和 port 的文件字节完全相同，所有物理参数、原方程、M8/前缀N256、尾N128/depth8/parts8/RK16、原Newton和全部门保持。相对先前 q=.060 启动，只把旧 `designInitialCheckpoint` 换成已过门同H尾的 `initialCheckpoint`，并改变输出/trace路径；源及初始prefix仍相同。它相对 accepted q=.040 前缀仍是一个 q=.060 新物理设计，不能登记为固定 g 加密。

初始prefix合并后815节点；本次新的内解最终节点/参数没有保存，不能把815当成它的终态。完整实际调用为：

| 调用 | 原实际返回 | 含义 |
|---|---|---|
| call1，原H，audit=true | converged，1.9930084352226262e−9 | 原停止门通过，并返回完整有限尾审计 |
| call2，同原H，jacobian=true | converged，同残差；208项Jac全部有限 | 给内前缀提供原 affine DN |
| call3，内解产生的新H | 原Newton iteration6线搜索失败，3.241344522795531e−9 | 新H没有通过原2e−9门 |

call1的实际尾采样metric为3.984326513162273e−8、Cartesian Darboux defect为.000281460784485168，均保留其原有限审计口径。call1/2原H逐值相同；call3已是不同H，完整原请求保留在执行记录，不能把旧H的接受状态搬过去。

原 `solve_with_actual_tail` 控制流在 `if not sol.success: return` 之后才产生candidate并请求call3，因此到达该新H请求说明**临时 affine-DN 内解曾返回 success**。但是该版本在call3之前没有保存 raw p/sol，且call3异常发生于最终physical checkpoint写入之前；现有目录无 `seed.json.gz`、系数块或inner debug。不能从H反推完整前缀、δ、c、RMS或最终边界/metric，也不把这一控制流事实升级为完整实际联立接受。

## 新失败态的只读残差位置

对完整call3失败尾作已登记的原full-Jacobian残差定位，91612真实exit0，全部576段的重放 norm 与原 iteration6 **逐位相同**。未重跑求解器，未改变原缩放或门。只保留下列三处解释量，不提交全失败场或逐段排名表：

| 解释位置 | 原归一化残差 | 浮点差及局部域 |
|---|---:|---|
| 主峰 stage45 / cell0 / seg3 / [.25,.375] / mode12动量 | 3.241344522795531e−9 | 70 ULP，绝对差3.979039320256561e−12；局部A=.9993526128712102 |
| 另一独立超门项 stage43 / cell0 / seg3 / [.5,.625] / mode15动量 | 2.7509740485739374e−9 | 3 ULP，带号差−8.526512829121202e−14；局部A=.9825082073339836 |
| 最低A所在 stage40 / cell0 / seg3 / [.875,1] | 2.2702890387457158e−11 | A=.5220201871565618，此段残差远低于门 |

全局最小D=.9991195608484377，末端匹配残差最大2.5533258603093732e−14。主峰仍不是单个1 ULP机制，并且第二项独自超过原门；最低A段不等于最坏匹配段。原旧H局部松弛结果没有保证这次新H成功，这条失败也不证明 q=.060 数学幅度上限。

## 执行来源与保存边界

新call3失败尾SHA：`6059334fa00c9fe6ce4bca788dff852f4da0988b920c5ad7e7f22b7fad65e35b`。目录 `m3_work/beta4625-q060-local-tail-retry` 保留实际命令、资源终态、三次尾记录、原错误、完整locator输出及对应哈希。紧凑来源见 `scripts/resume_m3/q060_resumed_call3_failure_record.json`；只读收集器为 `collect_q060_resumed_call3.py`，不执行BVP、tail或locator。

收集期间曾观察三个旧会话输入路径不存在；原q060运行和locator早已结束。root随后用当前会话中相同SHA的副本仅重建缺失路径，字节未变，collector的最终逐源/输入核验全部通过。工程记录和当前副本映射一并保存；不推测路径消失原因，不将此后存储事件当成上述数学失败原因。后续恢复将使用显式落盘的内解hook和当前会话源路径，原历史记录不重写。

复现已完成数据的收集（不重解）：

```sh
python topics/visible-flex-held-10pct/scripts/resume_m3/collect_q060_resumed_call3.py --run /workspace/scratch/7322d0dee069/m3_work/beta4625-q060-local-tail-retry --original-run /workspace/scratch/7322d0dee069/m3_work/beta4625-q060 --out /workspace/scratch/7322d0dee069/m3_work/q060-resumed-call3-compact.json
```
