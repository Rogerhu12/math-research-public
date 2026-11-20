# 实际 warm .25 尾的共享物理 R 图：cusp 邻段与跨 cell 接口

维护：Astra-held10-1b6d88ec-20261120，n4_continue 分工。

## 1. 已实际完成的结论及范围

对同一已接受 `.25` 检查点的 stage 128、143、144，先选择明确的共同物理
半径节点及 Cartesian/Fourier 值、一阶、二阶数据，再用精确有理五次 Hermite
插值定义图。以下均是每段 **所有物理半径、所有角度** 的连续界：

| stage | 原 locator | 五次区间数 | 相对 Gram 算子误差上界 | 主曲率绝对值上界 |
|---|---|---:|---:|---:|
| 128 | cell 0 / segment 0 / x∈[15/16,1] | 16 | 8.716665715219653e−12 | 8.000105479294158 |
| 143 | cell 0 / segment 0 / x∈[0,1/16] | 16 | 8.687424201658619e−12 | 8.000105420376210 |
| 144 | cell 1 / segment 8 / x∈[15/16,1] | 16 | 7.807771160004470e−12 | 8.000105411328140 |

三者均通过原 `1e-6` 度量门。每段实际核对 14,688 条精确端点标量等式，
三段共 44,064 条。stage 127/128 与 143/144 两个实际输出接口的半径及全部
Cartesian 两 jet 已逐字相同。此前已认证的 stage 127 **整个数学图** 保持不变，
未再计算其连续证书。

本次仍是既有 `.25` warm 分支，未获得 full-H、全尾或 prefix—tail 的实际
非零模接缝结论。共用背景是 R58 的首 valley 4.625 真积分归一背景，不是旧
3.125 背景。没有新的 BVP、shooting、Newton 或原尾 Jacobian 调用。

## 2. 输入、唯一均值链与节点选择

原检查点 SHA-256 为
`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`，
原响应 `converged=true`，残差 `1.8946163107633334e-10`，含 1153×48 状态。
实际原 full-J call 9 的既存 native 输入/输出提供每段的两个均值增量。
`extract_q060_native_mean_chain.py` 复用原二进制 parser，核对全部 1152 个段的
输入前 48 槽与检查点逐字相同，两附加均值入口槽均为零；之后按原由内向外的
确定求和次序分别累计扰动均值和旋转背景均值。cut 两槽是
`[3.681650775547157e-7, 0.02277202492794494]`。

有限图的竖直扰动零模使用第一条均值链；第二条只记录原背景 primitive，
不重复加到扰动图。新图的背景改用已明确选择的同一 R58 真 primitive，
扰动均值及其所选 nodal jet 保留。没有换均值 provider、重新选择竖直常数或
在段接口重置零模。上半图同时反射背景高度和全部扰动高度，度量与曲率界不变。

批量入口只 assemble 一次原背景。默认内部 node k 取其外侧 stage k−1 的
内端数据为唯一共同值；每一接收段都实际复制同一半径和全部两 jet。
另有明确优先级：stage 0 全部已认证节点保留；stage 127 的**两端**固定，
故 node 127 由 stage 126 复制 127 外端，node 128 由 stage 128 复制 127 内端；
最深 node 1152 使用已认证圆领的 stage 1151 内端。不能让默认规则覆盖 127 外端。

所有 `radiusJS` 都明确选择为精确 binary64 实数节点，之后在真背景的同一
物理 R 坐标中定义图；不是把真 R 区间的中点当作未声明的新节点。
源 height 先按 `H=r_JS^4 u` 还原物理值。平面二阶有限差分输出只是所选有限
节点参数，不被称为原 PDE 的精确二阶导数。实际 Cartesian 发展保留原 Ω
角 primitive 修正。有限角基保留全部 `m≡1 (mod 3), |m|≤192` 平面项和
高度 `m=0,3,…,72` 项，没有删掉原小高频再验收另一张图。

本次相邻段实际修补的最大单系数差如下；所有半径差、均值值差和物理 H 值差为零。

| 接收段 / 节点 | 值最大差 | 一阶最大差 | 二阶最大差 |
|---|---:|---:|---:|
| 128 外端 / 128 | 0 | 0 | 1.6574292673132954e−13 |
| 143 外端 / 143 | 0 | 0 | 5.041810840257318e−14 |
| 144 外端 / 144 | 1.550963648536927e−25 | 6.3527471044072525e−21 | 4.840644172680043e−13 |

这些差不是“足够接近所以已 C²”的判定。复制之后，节点数据本身相同；
每一端的有理 Hermite 恒等式又完全等于该共同数据，所以新的物理 R 图确实 C²。
原 x 图在 `|w_x|` cusp 处的二阶跳量结论仍保留，未被此新图消除或改写。

## 3. 真背景覆盖与连续度量证明

对每个 literal-R 区间，程序在原 source locator 两端扩张 `1/1000000`，
必要时进入邻 segment/cell。用真部分积分的严格上下界验证：左侧真 R 严格
小于最小 literal R，右侧真 R 严格大于最大 literal R；R 单调性给出整段覆盖。
得到的真 w 范围分别包含于：

| stage | source 覆盖 | 真 w 的外包 |
|---|---|---|
| 128 | (0,0):[.937499,1]；(0,1):[0,.000001] | [.011254032847027338,.011254351849435379] |
| 143 | (1,8):[.999999,1]；(0,0):[0,.062501] | [.011258817902909621,.011259136926692243] |
| 144 | (1,8):[.937499,1]；(0,0):[0,.000001] | [.011259136919783322,.011259249716582102] |

完整证书存有严格有理区间端点。显示十进制仅作外包显示。α 始终是 R58 定义的
唯一真积分归一值，未从其区间中选中点。选取辅助常数 w0，只用于恒等分解
`w=w0+(w−w0)`，并用上述真范围支付后项。

记真旋转背景为 `X0=(R cosθ,R sinθ,h(R))`，`h_R=w`，`E=1+w²`，
扰动为 V。归一 Gram 误差三个分量的精确分子是

\[
 A_N=2(e_r\cdot V_{R,xy}+w V_{R,z})+|V_R|^2,
\]
\[
 B_N=e_r\cdot V_{\theta,xy}+R e_\theta\cdot V_{R,xy}
       +w V_{\theta,z}+V_R\cdot V_\theta,
\]
\[
 C_N=2R e_\theta\cdot V_{\theta,xy}+|V_\theta|^2.
\]

相应除数为 `E,R sqrt(E),R²`。各五次系数及其导数使用精确有理运算；
所有相同频率的线性项先合并，再转 Bernstein 系数取全区间界，最后取全角
Fourier l1。`w−w0` 项按真范围保守估计。对本次三个段，保留全部线性相消、
以范数控制全部二次项已足够通过；**本次没有执行低模二次精确合并分支**。
通用入口提供同 stage 0 证明的低模二次合并及高模余项，以供后续较大外端段，
不把它写成本次已执行的分支。

每一区间设 `vr≥|V_R|, vt≥|V_θ|`，保守分量界包括 `vr², vr vt, vt²`；
以 `E≥1,R≥R_left` 控制除数。对称 2×2 矩阵的算子范数不超过
`max(|A|,|C|)+|B|`。由此得到表中全区间、全角度度量界，不使用有限 DFT
误差替代连续角度控制，也不借原 PDE 约束取消已有残差。

## 4. 曲率与实际成本

同一范数计算给归一一 jet 扰动 `eta` 和目标 Levi-Civita 协变 Hessian 扰动
`beta`。R58 已付 `|w|≤.41, |k_i(X0)|≤8`，故逐项可用

\[
 H_{11}\le v_{RR}+3.28v_R,\quad
 H_{12}\le(v_{R\theta}+v_\theta/R_{min})/R_{min},\quad
 H_{22}\le v_{\theta\theta}/R_{min}^2+v_R/R_{min}.
\]

`beta²=H11²+2H12²+H22²`，`eta²=vr²+(vt/Rmin)²`；因此
`|k_i(X0+V)|≤(8+beta)/(1−eta)²`。三个新段最大 `eta<2.004e−6`，
最大 `beta<7.351e−5`，给出已显示曲率界。这里只用 C² 图及真目标的连续
一阶 connection，不要求 x 图 C³。

单次 assemble 的四段批量导出（含只复用的 127）实际 14.599215027 秒，
三段连续证明实际 75.1432858900007 秒，均 exit 0。首次真背景覆盖占主要
积分成本，后两个段复用同一已算真积分。源、参数、命令和小实录见同名
`execution.json`。大数组、逐区间证书、均值链及批量缓存只保存在 scratch，
不提交可再生数据。

## 5. 再生命令与当前后续

在工作区根目录执行；三个旧组件输入可由各自已冻结入口及 `.25` 检查点再生：

```bash
OPENBLAS_NUM_THREADS=1 python math-research-public/topics/visible-flex-held-10pct/scripts/resume_n4/extract_q060_native_mean_chain.py \
  --checkpoint m3-work/newg-wide-lambda0p002-m24-actual/tail_0001.json.gz \
  --native-record m3-work/newg-native-m24/runs/actual-lambda0p002/0009-jac-record.json \
  --out n4-work/q060-tail-geometry/warm025-native-mean-chain.json

OPENBLAS_NUM_THREADS=1 node math-research-public/topics/visible-flex-held-10pct/scripts/resume_n4/export_q060_shared_r_tail_batch.mjs \
  --input n4-work/q060-tail-geometry/warm025-native-mean-chain.json \
  --stages 127,128,143,144 \
  --anchors n4-work/q060-tail-geometry/warm025-shared-stage-anchors.json \
  --outdir n4-work/q060-tail-geometry/shared-pair-batch

OPENBLAS_NUM_THREADS=1 python math-research-public/topics/visible-flex-held-10pct/scripts/resume_n4/certify_q060_shared_r_tail_batch.py \
  --manifest n4-work/q060-tail-geometry/shared-pair-batch/manifest.json \
  --constants n4-work/q060-tail-geometry/constants.json \
  --normalization-certificate n4-work/q060-tail-geometry/tight-integrals-certificate.json \
  --outdir n4-work/q060-tail-geometry/shared-pair-certificates --stages 128,143,144
```

anchors 的完整小定义保存在 execution 实录，所有 path 均指向既有小组件导出。
对全尾，同一冻结批量源用 `--stages all` 及新的 outdir；必须保上述显式锚。
本结论完成后已实际启动全 1152 段批量展开，并继续认证已导出的深端整 cell，
不将当前三个局部段当作全尾或 README 完成标准。
