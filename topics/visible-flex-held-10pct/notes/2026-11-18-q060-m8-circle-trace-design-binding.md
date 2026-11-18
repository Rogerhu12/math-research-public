# q060 真余弦锚到 M8 圆弧 trace 空间：设计身份与唯一幅值

**状态：定义与参数映射已确定；本条只执行 metadata/source 绑定，没有新核心求值、初猜投影、DN 或 BVP。**

## 原锚及固定物理表示

复用已登记的 `resume_closed/q060_cosine_reference.py`，
绑定真正接受的 q060 原余弦锚：

- CP `closed_work/q060-saved-inner-resume-v1/seed.json.gz`，SHA
  `4755143bb3c02c28669eebaa2db53ad97142acec799afd4136125db4277350d9`；
- 完整 physical quintic 分块 SHA
  `a3434077ca4b42effcfdb80ce196f6e3bb52f37501f8d5319674ad66e2dc8249`，
  1934 个物理径向节点、`6×1933×25` 系数，禁止外推；
- 原全尾 `seed_tail_0003.json.gz`，SHA
  `ae01f13ad7b28b82481a3417471c4fd5511b145bb50bd2be73a4386897a0db1e`，
  原残差 `1.8339313038213144e-9`，返回完整 208 项有限 Jacobian 与 audit。

原核心是字面的

$$
h_{\rm old}(\phi)=1+.06\cos(3\phi)+\sum_{j=2}^{8}c_j\cos(3j\phi).
$$

它没有 raw/circle 同伦元数据，原 Flow 也没有新 integral lift。
原 q gauge、实际 q、warp reference 都为 `.06`；M8 对应全部 25 个状态分量。
完整物理图还包含原 `flow.height_integral` 所定义的平均高度原函数，不能将它置零。
以后投影只计算 `geo+全部25态表示场`，因为竖直均值没有对应的状态列；
这与声称复制完整三维图不同。

原最终物理轮廓为
`delta=.06104275721220832`，`vu=.45,vd=.5,ramp=.4,ramp_eta=.05`，
`ShortBridge(curvature=4,peak_fraction=.2)`，
物理 meridian length 为 `1.3602524132788236`。
完整原 chart payload SHA 为
`22274daadd4119eae96401d277fec28017c01b468c714d2b41ce7b993a13e8cb`，
原 chart 文件 SHA 为 `14f326e2b63f681616ee2391671f029d5da5fb8e20f8d204b3298d0d66d50a0e`。
这些定义和原完整物理 tail port 都保留。

## 旧 p0 的语义

原求解采用 `fixed=False`，历史参数
`p0=-8.84429295772251e-6` 是原输入轮廓的 delta 增量。
CP 的 `frozen_profile.delta` 已经包含它。
新的设计从该最终 frozen profile 开始，**新初猜 `p0=0`**；
不把旧历史 p0 再加一次，也不把它误作固定度量下 q 的指数参数。
现成 native reader 直接用最终 profile 构造原 Flow，不实例化旧 BVP 或调用旧 restart。

## 唯一主矩幅值

旧余弦主系数恰为 $.06$，故旧因子 $P_{\rm old}=1$；
所有原七个高次余弦系数都不进入主矩。
目标主核仍是 `lambda=1,a=.21,bp=.32,bc=.4`，
使用前条已经证明为正的同一真实主矩因子 $P_{\rm new}$。
于是唯一新幅值为

$$
q_*={.06\over P_{\rm new}}
\in[.0521056555062767062867881206225292015918,
     .0521056555062767062867881206225292015919].
$$

这里 `.06` 按原 binary64 的精确实数取值。
独立 Fraction 区间严格落在一个 binary64 的邻中点之间，因此新入口选择

$$
q_{\rm new}=.05210565550627671,
\qquad \texttt{hex}=\texttt{0x1.aad97acac1567p-5}.
$$

没有扫描 q，也没有把旧 q060 先当作 raw `lambda=.02` 再乘另一因子。
这是新物理设计，不是同 g 精化。

## M8 新空间与完整两jet规则

新七维控制空间按 R44 为

$$
\operatorname{span}\{B_2,B_3,B_4,B_5,B_6,T,U\},
\qquad T=S_A-S_B,\quad U=S_B.
$$

保留原 $c_2,\ldots,c_6$ 的物理数值；旧 $c_7,c_8$ 的位置改为 trace 坐标。
这改变有限空间，不是原七列的换坐标，也没有预先升为 M16。
原**全部七个**系数仍进入源核心中心值：

$$
\begin{aligned}
h_{\rm old}(\pi/3)&=1-.06+\sum_{j=2}^8(-1)^j c_j,\\
\rho_{\rm old}(\pi/3)&=1+8(.06)+\sum_{j=2}^8(1-9j^2)(-1)^j c_j,\\
h'_{\rm old}(\pi/3)&=0.
\end{aligned}
$$

用记录的实际 binary64 系数作有理算术，前两者分别位于
`.9405029417351825496480038924438333173346…` 与
`1.4606246268051886525704434749090874105033…`。
后一个量是反射中心值，不是原全角 rho 最大值。

新保留的 $B_2,\ldots,B_6$ 在保护弧恒零。
未来唯一两jet初猜因此采用

$$
t=\rho_{\rm old}-(1+8q_{\rm new}),\qquad
u=h_{\rm old}-h_{{\rm base,new}},\qquad (A,B)=(t,u-t).
$$

实际有限求值时从原 native core 和新的 zero-trace integral core 读取中心值，
另报与上述完整源公式的关系；本条尚未调用这些对象，也没有选择数值 t/u。
物理控制与数值参数的链条仍为 `c=p[1:]*pscale`，
最后两列的导数分别为 T 和 U。原新的组合解析 guard 保留抵消，
`rho>1e-5`、每扇区上限 32768 不变。

## 已准备但未执行的最小初猜入口

`q060_circle_trace_design.py` 默认只生成本条 metadata plan。
只有显式 `--evaluate-initializer --evaluation-plan <冻结plan>` 才进入另一个执行分支：

1. 用原 reader 构造余弦 Core、原 Flow 和全部 25 态物理 quintic。
2. 在新的独立 Flow 类上安装新 integral core lift 一次，使用原 `(.5,.9)*prefix_end` 窗；旧 Flow 不添加 lift。
3. 在不变 chart/warp/frozen profile 上做表示场回投和共享 C² 入口修复。
4. 将原完整 H 以 `H_old/(sigma*q_new)` 重编码，完整记录实际乘回值的浮点差。
5. 仅用原真实 response/Jac 的 affine 锚读取初始 domain、BC 与 RMS；不调用实际尾或 BVP。

冻结 plan SHA 为
`ce2533b9bb0342fdcb6a7c81560281e8ef47ace3798e0e9e79fc1b44a176d1fc`，
定义身份 SHA 为
`19d09a8199b4f91ab2479f736dc7763d506b8eae1af671ea5369927cbc80171a`。
默认 metadata 命令的工具 chunk `0e6330` 真实返回 `exit 0`，
`native_reference_constructed=False`、`new_core_constructed=False`、`initializer_projected=False`。
以后若执行实际初猜，执行段会另记 `native_reference_constructed=True`；
不会把静态旧 binding 的 False 字段误当作新运行状态。

本条源与紧凑记录为
`scripts/resume_m3/q060_circle_trace_design.py`、
`scripts/resume_m3/q060_circle_trace_design_record.json`。
不继承旧 R38/R40/R41 的圆弧正性、保护窗或握持比例。
