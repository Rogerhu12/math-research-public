# 固定645/317射击真接受；实际三jet桥仍超度量门

**有限非线性BVP已通过明确边界门；实际几何未通过1e−6门。** 本条延续 [真线性响应](2026-11-17-parallel-geometry-fast-boundary-response.md)，原标量、原 core rho、初端 Ufast、末端 L 和 target 全部固定，保留全部962个 M320/N4096 ODE。没有把有限接受或新桥登记为合格闭面父场。

## 1. 有限射击定义与实际收敛

初值为 `y0+Uη`，初端645补空间自动固定；完整右残差是
`R(η)=L(y(.997;y0+Uη)−y1_ref)−target`。接受要求到达.997且沿程正域成立，左右边界最大行均≤**1e−13**。原 target 最大行9.26039e−12，不能按宽于该值的门让原场自动通过。

首个真实IVP使用线性η，最大右残差7.66653e−12、范数8.79016e−12，未接受。随后只做一次新完整317列变分Jacobian：沿该真实轨迹的共同五次参考形成全部 A(s)，条件数179.71622，1549次Jac调用，抽样参考ODE缺陷1.32072e−11。固定BC未重选；没有删小奇异方向。

| 真实IVP | 最大右行 | 结果 |
|---|---:|---|
| 线性η首试 | 7.66653e−12 | 未过门 |
| 全Newton步 | 7.34325e−15 | 过门 |
| 同η、最大步减半 | 7.55730e−15 | 仍过门 |

仅用总3个IVP和1次新Jac，未用尽预设预算。IVP容差均为1e−13/1e−16，原最大步.000015625，精档为其一半。左右最末残差分别7.55730e−15、8.00926e−17；粗/细末系数最大差2.22045e−15。最终257节点、256胞元，沿程有限角最小H=6.73485e−5。粗档终端机器微胞按既有64ulp政策合并并保真末两jet；精档无须删除节点。

## 2. 实际三jet桥与整短段读出

父是 d6441e 原M112前缀。实际起点位置已有非零改动，故不能只用原R637的一/二阶修正。新桥使用已有Hermite构造的完整值项：

`Fnew=Flocal−p0(u)δF0−w p1(u)δFs0−w²p2(u)δFss0`，其中
`p0=1−10u³+15u⁴−6u⁵`，p1/p2沿用 [R637](../results/R637-explicit-C2-bridge-to-the-high-mode-inward-prefix.md)。选择实际第64节点，w=.0005000000000023874；起点0/1/2jet逐位绑定原父，修正终端及其后全部jet逐位保留。按 [R227](../results/R227-hermite-seam-general-reference-hessian.md) 的共同Hermite原则，每个胞元仍由同一两端六jet定义，得到真实C²接合。

桥后的图已改变，明确取消BVP标签。使用冻结公共quintic读者，8192角、每胞元4子分，共10,485,760点，直接读真实导数：

| 实际短段指标 | 未桥有限BVP | 完整值/一/二jet桥 |
|---|---:|---:|
| 最大相对Gram算子误差 | 1.13493578494e−6 | 1.13493578494e−6 |
| 最大实际主曲率 | 5.79927784062 | 5.79933926260 |
| 最小H | 6.73484893e−5 | 6.73484893e−5 |
| core见证最小距离 | .962313759112 | .962313759142 |
| 最大位置球范数 | 1.75450972035 | 1.75450972035 |
| 原cut一/二jet跳 | 5.03585e−5 / .0153374 | 0 / 0 |

两者最坏Gram都在.997、φ=.4348835534，分量 rr=−9.83793e−8、mixed=9.57441e−8、angular=−1.12609215e−6。桥没有增加最大误差，但这个新BC所得场比原R637的约5.09e−7差，故本条不通过课题当前1e−6门。数值采样也不冒充连续证书。

末端真实 m225..320 尾的8192角 `(F,Fφ,Fφφ)` 最大范数从原507cab的 `(4.62320e−9,2.57141e−6,.00144618)` 增至 `(7.05477e−8,3.95683e−5,.0222334)`。可直接对两份raw末系数保留这些m的R/T/Z后调用既有Frenet.jet复算。因此“投影到快速行后的删模目标”不等于物理高频尾变小；不据此继续旧标量延拓。

## 3. 冻结源和外部数据

- [首试源](2026-11-17-parallel-geometry-fast-shooting-trial.py)：`0303bd211178f0331f1d43035442fda52697513d246e2efa2e0aaa928a342a40`。
- [有限校正源](2026-11-17-parallel-geometry-fast-shooting-correct.py)：`afc3d47f37257bfc23e650a9fbeabe3e29a06788250c9d82189387f4b5a9f857`。
- [完整值差桥源](2026-11-17-parallel-geometry-fast-value-bridge.py)：`7ee4b4d65e57ebef8c4731ac8397e39ad2a228a4c6dcdebec89fa561132f3039`。

最终有限BVP raw `parallel-geometry-fast-shooting-corrected.json.gz` SHA `bb0ab0595257372355da28327eb67988957764daddaf464cf9c48e9b264f3f05`；射击报告 SHA `e143b0b65623a4aaf87701b4e5aa6a48d3dfecd1d228020ae8ad899f72d6985d`。桥raw SHA `7dc37086731eed110886e64dafee9f248e2e5a3741c082f863e3d5a1ddc45edf`，读出SHA `5858c39cfd1542607f438ca79fe2f8fcfb1f18f7bd65985acba6cffe3ac87d3b`。raw保留原共同场元数据，实际射击生产者由 `finite_shooting_definition.source_sha256` 标识。

复现均设 `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1`：首试传 `--topic --field(507cab) --local-report(7eb66be) --arrays(6afa687) --response(1e051e9) --out`；校正传 `--topic --reference(507cab) --local-report --arrays --initial-trial --out`；桥传 `--topic --parent(d6441e) --field(最终BVP) --out --join-width .0005 --angles 8192 --radial-subdivisions 4`。所有raw留仓库外。未重采原旧前缀，未获得全域单射/reach、闭合或固定g精化完成。
