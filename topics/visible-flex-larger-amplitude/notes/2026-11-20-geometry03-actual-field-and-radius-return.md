# 独立几何 worker03 的实际新场与完整首 jet / 半径终态

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

## 1. 实际场必须按本次返回识别

[公开 Actions 44772201880/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44772201880)
已完成必要输入链、全部922原胞首jet几何以及半径目标续化。
完整实际输入、命令、源提交/字节和小结见[实际第1卷](2026-11-20-public-actions-44772201880-1-part-001.md)。
这次实际最终场是 **756936ee**，与求解任务run44758209061的c4a3不同。
目录路径和同一生成配方不构成相同场身份；任何旧c4a3或97fd的界均不移用。

| 实际对象 | SHA256 |
|---|---|
| warm bundle | `6b826d9923523f7cd61498578525be39b6b640dc5b61c926b1fe6f7e83166cb5` |
| 当前 node report | `8c0aa79e011b5c98db72caa3c10b82839a9fb90b2f272d722ff079040512c0e6` |
| 当前原标量输入载体 | `8c6a694661b0ef90e4682aff1e38b1903fd52feb1a8cab3251c5aecaace8bc6f` |
| continue 父场 | `9e5faca877ba3b2ae3395fdee12d515e174e7896d96944f0625a3c243cb71cb3` |
| continue 终场，10,370,606字节 | `756936ee8b18ddace1673d02db678dd3db3c20944b82dce60af2404ddef390bc` |
| continue 完整报告，6,338,162字节 | `d114a8272f83346832b9a722de59088a14e09eaff8b98367a7ca6d84b72a3950` |

差异从本次warm字节就已出现。第一求解阶段af89的有限点max分别为
`0.5864263699217489`（run2）与`0.5864263699345016`（run3）；后续数值轨迹
继续分开。run3的6077阶段真实状态为`restoration_failed`、进程退出0且未接受新场，
后续仍按现有配方实际继续；不能把这个状态改写成run2的`iteration_budget`。
两条工作流均明确Python3.12.14、NumPy2.3.5、SciPy1.17.0及单BLAS线程；
这些相同声明不足以证明跨runner逐字一致，差异原因尚未归因。
本条不重新运行旧科学链去追求一个指定历史SHA，也不把不同输入字段或物理场混同。

run3 continue实际Phi为`1.3688214780038883e-7`，有限点max为
`0.013601420431375466`，Jw为`0.20925667575187515`，
product为`.9919049021885185`，末mu为`.012063248414946114`。
它的有限度量读数不替换run2六方向e08的更低读数。

## 2. 全922原胞首 jet 已返回

冻结R670源eaa9a579，实际源提交
`cefa3c0dea7f8ab7cc1e20c2466546db8c5313a7`；全原胞，plan
`256:1,512:2,1024:4,2048:8`，retained modes24，Taylor8，beta1/4，
support目标.14。上片全域、镜像和帽沿原完整模型解释，不截断实际场高模。
总子进程56.422252512999876秒，核报告48.68849287699959秒，退出0，无缺输出。

实际 `complete_scope=true`、`embedding_certified=true`、`target_support_paid=true`。
support下界`0.2965427454452786`，法向平方下界`0.0068563866161592225`，
完整body直径上界`4.119750108960081`，固定见证距离下界
`0.938660315233799`。原四marker条件下held/D至少
`0.2277334361424019`、grip/D至少`0.21835384877980143`，marker support
`0.23970037453183518`，报告给四固定marker的Euclidean shape distance正性。
这些结论只属于该实际场，尚无本场完整K/reach或统一metric。

首几何raw 1,298,130字节，SHA
`351fd2324b0aeae03f9eaecaea25b29f3f550cf9043d93d1161ea7f265efc563`；
非平面raw 411,924字节，SHA
`957e2ad217945efce5cb8483f7e132d1e495f33cf9b0a47f049c7a5d2062cdb6`。
raw和逐胞/数组均只留runner，完整源与实际参数已公开。

## 3. 同场半径续化已支付body直径4.1目标

冻结0faa98e源，实际源提交`b0a15a48155915a6cccaf7432c372d22cb1da907`，
只细化实际半径瓶颈胞，保留全部原完整界；plan为`2048:2,4096:4,8192:8`，
body直径目标`4.1`。子进程91.80291502199998秒，报告88.63755288599987秒，
其中新胞覆盖86.17176957399988秒。

实际状态`completed_target_paid`，`body_diameter_target_paid=true`，
`published_diameter_upper_within_target=true`。body直径上界为
**`4.099300336920071`**；加原四marker后是**`4.101300336920072`**，
没有把body的4.1目标冒作marked整体直径也小于4.1。
support与固定见证下界不变；marked held/D下界提高至
**`0.22886895328877543`**，grip/D下界提高至**`0.21944259772886254`**。

实际续化报告SHA
`343eb4384ba97a9bc512dee35a5f0f63d5facd409dbdbc341414ef1e0bcde4e9`，
1,321,562字节。后续K及R650/R661组合必须消费这个同场报告及同场全曲率。
完整K步骤沿原队列自然运行，尚未返回。R666最终同场reach编号继续保留；
不由上述首jet/直径结果预填reach、metric或课题完成。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
