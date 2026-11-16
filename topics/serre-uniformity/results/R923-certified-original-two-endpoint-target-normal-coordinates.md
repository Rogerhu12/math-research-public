# R923 — 已认证的原两端272个目标正常坐标

日期：2026-11-16。状态：**实际公开 Actions 已成功完成。** 本结果把 R917 的两个原秩八正规阶接到原循环七对应的全部272个目标正常函数。两个端点的目标 $w$ 与正常坐标均实际得到267项可靠展开；共享分母的实际阶均为0。以下数值及完成标志来自原运行证书和纯 IO 核验，没有重新执行数学。

## 1. 实际运行与原来源

原生产者：

|项目|真实身份|
|---|---|
|数学 RESULT|R923-original-two-endpoint-target-normal-coordinates|
|run / construct job|43915625047 / 133469002048|
|源提交|8f02956cf5e1bea1716ff96add3267f4f36aafda|
|核心 SHA256|4aef4b448338f62216d3ce44135ace89f83c5be966acb6f90dc47adaed4d334c|
|原 R917 helper SHA256|c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d|
|纯 IO wrapper SHA256|d6bda530f750d8c7bdf8d4f302ea83ad2bcf23e116d4dcf364d98983bffeeddf|
|执行方法 SHA256|dfd781d304b1d0fbb8de6b7267b1cbc543403ce47e1226316e97893a62c48cef|
|数学配置 SHA256|68cdf0129572392d596afafe61fb240d37f15c3c244f75c6323c97dfd6013660|
|核心 exit / complete|0 / true|
|实际完成数学阶段|655|
|FINAL 中数学用时|708.3958209120001 秒|
|core receipt 总计时|708.396783051 秒|

两种计时分别照原字段记录，不互相替换。实际规则 job 为133468855237。最终活跃请求仅更新规则读取提交；其9331字节请求 SHA256 为
0dfbba7aa8bba6f03a04cce565c937d7fa81e39bff9cb4b1b3c6275140e3fe5e。
数学核心、方法与 helper 没有在本运行中改动。

准确证明见 [R923 原证明](R923-original-target-normal-coordinates-in-certified-endpoint-orders.md)，
SHA256 d0c2ceada8d5d2888efe8258a390d4625ad4193958d840332f3830733ef9fc97；
执行定义见[原方法](../notes/R923-original-two-endpoint-target-normal-coordinates-method.md)。
本结果不重述其中的整性证明或把模数组改称特征零重构。

原317个输入件的真实组成是：POLY279、R827六件、R873七件、R917二十五件。
POLY 是已成 R885 全局特征多项式及完整单左伴随行；R827 只提供已成原 $W$ 与地方来源；
R873 保原 $P,K$ 的准确单位解及 dual-seven；R917 保已成两端正规阶、primitive 数据和原帧。
这些旧对象都按原 tag 和原 bytes/SHA 消费，没有重新计算旧 $272$ 维矩阵、273个插值节点、
Krylov 逆、2058单位解或正规化。

## 2. 两端得到的实际值域和精度

原素点及嵌入始终为

$$
\ell=1000000753,\qquad
\zeta=549966761,\qquad s=99932770.
\tag{923R.1}
$$

两端参数仍是

$$
\rho_0=z-z(P_0),\qquad
\rho_1=\iota^*\rho_0=z-2\beta_{72}-z(P_0).
\tag{923R.2}
$$

本次没有把 $\rho_1$ 改成 $z-z(P_1)$，没有将普通 $z=0$ 纤维的数组挪到两个端点。

|实际字段|原 $P_0$|原 $P_1$|
|---|---:|---:|
|R917 正规阶输入可靠项数|271|271|
|目标 $V=q^*w$ 的可靠项数|267|267|
|共享 $r_0$ 乘法 determinant 的实际阶 $d_\epsilon$|0|0|
|全部272个 $\gamma_i=q^*\beta_i$ 的可靠项数|267|267|
|完整272×8原方程乘回|true|true|
|原完整八维代数及幂零保留|true|true|

“267项”指每个原正规基坐标的 $\rho_\epsilon^0,\ldots,\rho_\epsilon^{266}$，
即模 $\rho_\epsilon^{267}$。它不表示新增了267阶特征零系数，也不把旧273项无损改名为新273项。

先以原 primitive 273项及原判别式阶6，按 R923 的“先运输正规基，再作已证明的整除”恢复

$$
V=\frac{\widetilde K(U)}{\partial_U\widetilde P(U)}
\quad\text{至绝对精度267}.
\tag{923R.3}
$$

共同清分母在分子、分母原样保留。随后将已成全局伴随行
$r_i(z,T)$ 代入 $(U,V)$，并用同一个八维分母 $r_0(U,V)$ 归一。
本次两个 determinant 的实际阶都为0，故全部坐标的可靠精度仍为267。
这个 $d_\epsilon=0$ 是实际运算结果，不是由原普通纤维的单位性预设。

## 3. 完整乘回与函数身份

两端完成证书保存了目标 $w$、两个乘法算子、全部17组正常坐标块、共享分母、
原特征关系和完整原方程验证。原正常基中

$$
\gamma_0=1,\qquad \gamma_1=V,
\tag{923R.4}
$$

且对每一个原列 $j=0,\ldots,271$，在整个八维正规阶中实际核

$$
\sum_{i=0}^{271}\gamma_i W_{ij}(U)=V\gamma_j
\pmod{\rho_\epsilon^{267}}.
\tag{923R.5}
$$

每条式子的八个坐标及全部267项均保留；不是只核一个几何点、一个简单因子或约化商。
原 $\widetilde P_U V=\widetilde K$、原 $\chi(U,V)=0$、
全部 $r_0\gamma_i=r_i$ 与 (923R.4) 同时在其阶段中验证。

R917 的两个长度三部分完整留在乘法表中。R923 没有要求 $\widetilde P_U$ 在特殊纤维为单位；
它使用原判别式和已证明的目标整性。后继对任意新分式函数仍须独立检查真实分母和精度，
不能把本次目标正常函数的整性自动赋给 $\Phi$、连接或任意 Laurent 商。

这些数组是原准确函数与原单位解在同一合法剩余地方的实际取值。准确特征零的
$P,K,W,r_i,\beta_i$ 来源仍原样绑定；本次没有将其系数作新的特征零展开。

## 4. 可直接消费的原文件

最终证书：

- p41-original-two-endpoint-target-normal-coordinates-certificate.json：
  57910字节，SHA256
  5de47282ab645a18c820d1522e765f1315debf0535ea093a7bbdb3d3912fe528。
- R923-target-stage-manifest.json.gz：
  53243字节，SHA256
  77465abfb34a3d5bb3348b8691453a0bb5aee2cbfe602016749b394557972453。

两端完成证书：

|端点|原文件|字节|SHA256|
|---|---|---:|---|
|$P_0$|R923-target-P0-complete-target-normal-coordinate-certificate.json.gz|22015|f234b7484d46a898c844393dca751ad5597cc7c0872cfa85bb92dcf069161426|
|$P_1$|R923-target-P1-complete-target-normal-coordinate-certificate.json.gz|22033|a58e0a0c0362b2338f7b6dfd24045fc85a3e332ff69b3b38142afda1df42978a|

目标 $w$ 小文件：

|端点|原文件|字节|SHA256|
|---|---|---:|---|
|$P_0$|R923-target-P0-target-w-normal-coordinates.json.gz|45121|6ab1cd2dda9e31850231566c477a592d03bde2a49c59464d55a74fc541268dd0|
|$P_1$|R923-target-P1-target-w-normal-coordinates.json.gz|45134|97751b6f7847189e368e1176a213aa267a1466183caabb36b884069e94a3bdc1|

全部正常坐标沿完成证书的 complete_target_normal_coordinate_blocks 逐项取源，
文件名为 R923-target-Pe-target-normal-first-stop.json.gz，实际 $e=0,1$，
每组最多16个连续原正常行。字段
normal_values_in_original_endpoint_order_mod_prime 的顺序是“正常行、原正规阶八坐标、递增参数阶”；
其来源和原 \(\tau\) 归一不改变。

实际 full-outputs-manifest.json 为119902字节、666个原 entry，SHA256
1d619081ded7437e9b79e8fc6b20b8a2c084b66754e0e3912a999b210f3afba3。
对应原 reference 为237字节，SHA256
1f390ed85c8695d2edada27e2328944e4a208f4667393e3a99697fd57f3fbc29。

原317件输入载体为 R923-retained-original-inputs.tar.gz：
56113313字节，SHA256
e2d3320618fb6d0fb472c1ddcd64dd755a793b4c7254e271bf487a01423a59c4。
其 R923-original-source-inventory.json 为107383字节，SHA256
a6e49120d1306ff0b648f3896dbd59e4035ed148d218bb3370d9457cb7dddc15。
后继按完整 inventory 和各原组身份取需要的旧文件；不为一个小叶重新求任何旧矩阵。

## 5. 原参数和帧继续沿 R917

本次引用的两个原帧是：

|端点|原文件|字节|SHA256|
|---|---|---:|---|
|$P_0$|R917-endpoint-P0-primitive-and-original-t-determinant-frames.json.gz|5242|af8612924918b42091891f979cf91f2d9d9a7e2ec08dec2d407e8f7e1e599f0f|
|$P_1$|R917-endpoint-P1-primitive-and-original-t-determinant-frames.json.gz|5244|7a20c3244907866e2c0033a8eb82c2d08234802654711896f787b70d2efef1cf|

原 $t-\epsilon=c_\epsilon\rho_\epsilon+\cdots$、$c_1=-c_0$、
正规阶相对于 primitive 幂基的 determinant 以及原 dual7 的两 determinant 输运都不变。
原 $\nu$ 的定义与几何反射固定性仍保留；本次没有新增 $\nu/d\rho$ 的数值或连接求值。

因此，后继现在可在这两个真正的完整八维端点代数上评价任意已给的原正常多项式，
并按其实际需要截取至多267项。特别是 R927 的原参考分支只需低阶数据的条件，
现在有实际足够的目标坐标输入；该后继本身的理想、参数和范数首项仍须新运行。

## 6. 公开产物、核验范围与未完成对象

原 artifact14250662137，
名称 serre-R923-two-endpoint-target-normal-coordinates-43915625047-1，
平台记录197804394字节，ZIP SHA256

d4b23f024a63114cddea7f71cd986db04a3916b858c3af34a89194e05ee23f55。

记录到期时间为2026-11-17T17:24:18Z。该 ZIP 身份来自平台记录；
本篇纯 IO 读取和选择文件的哈希核验不冒称重新下载并重算了整个 ZIP。

后续纯 IO run43918900454、read job133480609844、source
00cac5ddccbbb8198b03c3019d3952a625cfee1d 已实际成功，选择八个原 metadata，
保留的 tar 为223323字节、SHA256
4ba2c178248a2386bf6b0d828e8155aebb04461804f0cf54a9b134459b0c53ce。
该小包不是全部655个数学阶段的替代载体；完整坐标仍按原 manifest 和两端证书逐件取源。

原运行的 R923_COMPLETE_IO_REVIEW 明确报告655个完成数学阶段、317个原输入件、
两个实际 $d=0$、全部272×8方程为真，并报告 mathematics_reexecuted_by_wrapper=false。
核心 receipt 的 endpoint_target_NormPhi_frames_or_height_computed=false 保持。

本次准确完成的是两个原端点上的全部目标正常坐标。五个目标局部理想、
完整 $\operatorname{Nm}(q^*\Phi)\det U$ 与参考的数值标定、
原 Picard 活跃支持、theta/Poincaré period、非 $p$ 项和高度都没有由本次宣称完成。
未来 R903/R907 来源仍按它们自己的真实终点接入，不能因 R923 成功而填造。
