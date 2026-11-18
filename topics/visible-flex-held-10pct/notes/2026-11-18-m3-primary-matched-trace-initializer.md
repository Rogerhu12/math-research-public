# 唯一主矩幅值下的完整两jet初猜：原域通过，尚非解

## 新结论

在已独审的唯一主矩映射
`q=.03469511580330426` 下，R44 的 M16 新空间
`span(B2,…,B14,T,U)` 可以使用完整自然中心两jet初猜而通过原核心正性及初始 Frenet 域。
这是对先前同旧 q 的完整步确有负 `rho` 的不同物理设计，
不是同 `g` 精化，也没有沿用先前 `.5` 回退因子。

本次只运行 271 节点的原初始 collocation/domain 诊断；
RMS 为 `1.441695291093024`，没有 BVP 求解、实际新尾调用或完整 metric 结论。
下一执行不应把这条初猜登记为接受锚。

## 完整参数映射

源仍是 raw `lambda=.02 / M16` 的有限原门锚，CP SHA
`6f5a973c746e1112f827e5478432b9abe9d14931df90157f2a19381cc670b91e`。
旧图按其记录的数值尺度 `.04` 和完整物理 quintic 场重建；
实际旧 core 参数为 `.03991248545080898`。
新 q 来自前条真实主矩定义的唯一值，未使用原 `restart` 的 `ratio**j`。

新核参数为 `lambda=1,a=.21,bp=.32,bc=.4`，保留原五个字面设置
`center=pi/3, eta=0, lock=True, precision=80, positivity_grid_max=32768`。
控制空间保留 `B2..B14`，用 `T=SA−SB,U=SB` 替换最高两列。
前十三个**意图物理系数**保持原值；在新 `pscale` 下实际乘回时最大差
`2.710505431213761e-20`，不能称与旧系数逐位全同。

令无 trace 新参考的中心值为 `h0,rho0`，原完整旧核中心值为 `h_old,rho_old`。
本次仍只采用自然完整两jet：

$$
t=A=\rho_{\rm old}-\rho_0,
\qquad u=h_{\rm old}-h_0,
\qquad B=u-t.
$$

| 参数或中心量 | 实际读数 |
|---|---:|
| `t=A` | `.029183467095160287` |
| `u` | `−.00023407056347723998` |
| `B=u−t` | `−.029417537658637527` |
| 原中心 `h` | `.9602647565933892` |
| 原中心 `rho` | `1.3067443935215943` |
| 新完整核的中心 `h` 差 | `0` |
| 新完整核的中心 `rho` 差 | `0` |

上表零值是实际浮点构造读数；没有新增连续误差包围。
新真圆弧的定义半径为 `1+8*q+t`，其数值读数为 `1.3067443935215943`。
新低矩定义、半径和圆心 trace 都已改变，旧几何比例和 reach 预算不能直接继承。

## 原门与回投读数

原数值核心 guard 未改 `rho>1e-5`、原格点上限或已有值余量。
合并 T/U 物理组合后再取解析导数界，保留 `SA−SB` 的抵消。

| 有限诊断 | 实际结果 |
|---|---:|
| 数值 `rho` 充分下界 | `.6689847248235957` |
| 原每扇区格点数 | `512` |
| `rho` 采样最小 / 最大 | `.6703228628992194 / 1.3067443935215943` |
| 原初始 Frenet margin 采样最小 | `.0029624959541680873` |
| 初始 collocation RMS | `1.441695291093024` |
| 初始 collocation residual 最大 | `.004482201206826741` |
| 初始 boundary residual | `1.679806517631379e-8` |
| C² 窗修复后的入口系数差 | `1.3552527156068805e-20` |

新参考完整回投沿用 4096 个角点和原共享 C² 入口窗。
修复前所比较的是 `geo + 全部有限 Fourier 系数场` 的表示部分，
位置、角一阶和角二阶分量差分别为
`3.6853968875252482e-6`、`2.0722012976906456e-4`、
`.012206182181357605`。
这小于此前同旧 q 的半步初猜对应表示差，但两者是不同设计，不能解释为同 `g` 收敛。

状态中不含平均高度的原函数；真实三维图的平均高度轨迹仍须由原
`flow.height_integral` 重建。
因此上述回投读数不声称已经复制整张物理三维曲面，也没有算新完整 metric。

## 完整尾高度与实际锚的区别

原实际全 H 先按 `H_old/(sigma*q_new)` 在新数值尺度中重编码，
再按原 `sigma*q_new*y_z` 计算实际候选 H。十六项全部比较后，
只有零基索引 `6`、即第七项发生一个正邻数差：

- 原值 `4.2289609859217e-12`；
- 新值 `4.228960985921701e-12`；
- 差 `8.077935669463161e-28`，collector 以 `math.nextafter` 核为真正相邻浮点数。

原全 H binary64 SHA 为
`69b841ac1ad0131947ac5ec7ceeda32ccfa3f78d81557b400cf9b287244a0870`，
新全 H 为
`97159805df91db9c7c029a3bc70d195e1dba2bb030f70deb16e6e9f42b69480e`。
原接受尾的 H、response 和完整 Jacobian 只作为此次初始残差的 affine 锚；
没有宣称新舍入 H 已有实际非线性尾接受。

## 来源与复现

新执行源只对冻结的完整两jet探针作有断言的独立字面派生。
新定义 guard、原投影、collocation、Frenet 公式和停止门没有修改。
以前完成的基函数 primitive 与保留列检查按来源哈希复用；
其中旧 17 点 zero-trace 核比较仍只对应当时的旧 q，没有扩大其有限数值结论。

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/probe_circle_trace_primary_matched_initializer.py \
  --reference-run /workspace/scratch/7322d0dee069/m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2guard \
  --primary-mapping /workspace/scratch/7322d0dee069/m3_work/circle-trace-primary-match-v2.json \
  --constructor-check /workspace/scratch/7322d0dee069/m3_work/circle-trace-primary-parameter-identity.json \
  --interface-probe /workspace/scratch/7322d0dee069/m3_work/circle-trace-replacement-initializer-v1.json \
  --nodes 257 --projection-angular 4096 \
  --out /workspace/scratch/7322d0dee069/m3_work/circle-trace-primary-matched-initializer-v1.json
```

终态工具 chunk `0c9ccc` 直接返回真实 `exit 0`，探针约 `5.2978 s`。
本次没有独立 resource observer；退出码来源按实际工具观察登记。
原始输出 SHA 为
`7c12d4471f6df73ef8fdbdf2aa4919d8178d85d8f325285008564d14e766eaef`。
`collect_primary_matched_initializer.py` 只读取该完成输出、核哈希及具名 H 邻数，
未重跑数值探针；紧凑结果为 `circle_trace_primary_matched_initializer_record.json`。
