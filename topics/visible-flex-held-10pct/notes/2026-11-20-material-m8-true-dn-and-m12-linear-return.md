# 旧 λ=.02：原真实 DN 校正与 M12 未知空间的实际对照

维护会话：Astra-held10-1b6d88ec-20261120。

## 1. 原 M8 真尾已取得终态

此前 loader 覆盖错误已经按原 native guard 处理。本次重试在同一个
run44720589640 runner 上实际完成，corrector 返回2，原因是最终前缀
metric 门不合格；不是启动错误或尾射击不收敛。

源场仍为 `material-lam002-linear`，λ=.02、τ=0、原S=.21/b=.25、
q=.06和原物理profile/tail不变。实际输出目录为
`WORK/material-runtime-retry01/corrector-actual-00`，WORK沿用live工作目录。

| 项目 | 实际返回 |
|---|---:|
| 原 BVP 节点 | 605 |
| collocation RMS | 9.994103825385873e−7 |
| 第一外迭代 true-BC / tail残差 | 1.544040987219283e−6 / 7.2276365976222e−10 |
| 第二外迭代 true-BC / tail残差 | 1.827555864236694e−12 / 9.165499601207053e−10 |
| 最终 seam 请求 tail残差 | 1.0118582511856337e−9 |
| 最终 prefix metric_l1 | 2.392882822893711e−5 |
| mean 一阶 / 二阶 seam差 | −4.936797040611118e−9 / 1.1526253862470526e−7 |
| 非mean 一阶 / 二阶 seam差 | 3.6508527259405644e−14 / 7.441353943634708e−8 |

实际 BVP 共两次call、三次全Newton步，零域/merit拒绝。末端非线性DN
和原射击门已通过；完整metric、完整Cartesian C²接缝及闭合没有因此通过。
该场不能作为已验收的圆化节点，λ未继续推进。

最终 raw 为 `inner-01.npz`，SHA256
`82e594a7e0fe1aec54d04123a7efc4894ba8d5595a493412d17885023ade1c59`；
run.json SHA256
`0f0e090af51e0e0d49889e8ebbe226ad39244a464bd395899052da9a0ef1fe75`。
实际请求 tail_0008.json.gz 是末seam响应；所有原场和尾数组只保留在runner。
重现入口是已提交的 retry_material_runtime_and_transfer.py 和其原参数。

## 2. M12 原 linearDN 校正实际完成

从同日已验证完整参考传递的 M12 初猜与真实新port出发，实际
`WORK/material-lam002-m12-linear` 原 BVP 一次call、两次全Newton步
成功，零拒绝、零no_step。全部原tol、节点预算与物理边界门不改。

| 项目 | 实际返回 |
|---|---:|
| 节点 | 605 |
| collocation RMS | 9.99081085735273e−7 |
| metric_l1 | 7.6113375582238974e−6 |
| flow_defect | 9.236253815842251e−5 |
| 物理linearDN残差 | 2.39455150833467e−14 |
| 原审计节点 | 1358径点 × 592角点 |
| Frenet正根最小样值 | .0024848867264321006 |

原M8 linear场的metric_l1为2.3928678464055847e−5，约降低3.14倍，
仍超原1e−6门。l1指标单独超门不是新场的operator超门证明，因此下一步
对这个真实 M12 场作完整相对operator检查，固定mean规则，不把节点l1
或core投影的指标替换为真实度量认证。

M12 raw `inner-00.npz` SHA256为
`4f27506c169e31b40513317c13921f59414a75a27b6132d04f38d4bede8d1dc8`。
精确命令在已提交的 held10-material-m12-linear-01请求中：M12、angular384、
原full lift初猜、新256角求积port、λ=.02、q/warp=.06、maxnodes6000。
完整小参数与返回见同名JSON。

这里的δ与新增support控制仍参与设计求解，不能把这次降误差称作
README要求的全部物理参数冻结后的收敛。新控制越出先前M8有限控制盒，
旧盒常数不自动适用；实际Frenet数值门通过也不是全参数严格正性证明。
两个比较都不宣称完整10%族存在。


## 3. M12 同场实际 operator 已核对

随后 held10-material-m12-operator-01 实际exit0。以同一完整物理五次场、
1358径点和固定mean512规则，N512/N1024的算子峰分别为
6.8295052851007935e−6、6.851340731034565e−6；对应完整FFT-l1分别为
7.611337499763785e−6、7.6113375532854506e−6。公共节点分量差为零。
故当前实际样点已超门，不能把原l1失败仅归于其保守性；这仍是浮点
同场诊断而非外向连续证书。该M12场保留，下一步从它做完整M16参考
传递及真实新维port，原λ与门限不变，仍属于设计延拓。


## 4. M16 实际降误差及下一层入口

随后M16原linearDN实际exit0：605点/RMS9.990833344890345e−7，
一次call、两次全Newton步、零域/merit拒绝。原metric_l1继续降至
1.787664669180367e−6，仍未过1e−6门。原raw SHA256为
`dca4d0d92d9b4b3647ce8698ff308adf656fe57d8d640d0d58bea464f8a6e51a`。
实际输入源为上条已验证M16 full lift，新控制和完整小指标追加同名JSON。
这还没有M16 trueDN或连续operator证书。

同物理尾的另一实际M24 port导出已发现原unshared引擎在2048MB Node堆耗尽。
下一层因此使用已有仅allocation的shared installer，在新源副本导出同物理
M24/角求积512端口；原heap和原方程/门保持。模型重建及完整lift仍读取
原来源，不把生成port所用的内存优化误作物理修改。

新 `extend_material_mode_stage.py` 只顺序调用已有完整transfer、原portable
BVP、固定mean512的relative operator审计，保源命令的全部原门和背景参数。
它把真实状态和失败原因写成小摘要；源码已经py_compile实际通过，登记时
M24尚未实际返回。该入口不运行真尾，也不把可变δ/c设计称作固定g精化。
