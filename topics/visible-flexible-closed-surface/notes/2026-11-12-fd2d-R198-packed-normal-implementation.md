# 完整位置/曲率 normal 的 packed 累加接口（R198 工程闭包）

本件是 R195 求解层的存储改进，未另立几何存在结论。独立新源保留已验 R190/R191 完整公式，仅换 H 的分配、逐对累加和两份 normal 合并。原源未覆盖。

## 1. 实际成本与没有改变的对象

旧程序已按每个实际径向点的 local indices 做 outer product，并不是每行遍历全 n²。旧剩余的大对象为 n×n H 的分配、metric 与 curvature 两矩阵合并、以及 R195 对 dense 输入的全矩阵扫描。

新源只存对称径向 band 和一个 cutHeight border。所有 theta、phi、Z、rho 和 global cutHeight 列保留。完整角 primitive/一阶矩、真实位置两 jet、真实 Gram/主曲率 hinge、参数域、行权重与累加顺序均来自原冻结公式。定义中的 rho 在不同设计迭代改变 g 的事实没有消失。

新 factory 的数学 definition 与原相同；独立 normalStorageDefinition 明记实现与原源 SHA。normal 只返回 bandNormal、g、diagonal，没有伪造空 dense H，也不让旧 dense LM误消费。

## 2. 准确累加与合并

原某行的 metric 梯度、normal 贡献为
$$
g_i\mathrel{+}=w(e_i r_E+2f_i r_F),\qquad
H_{ij}\mathrel{+}=w(e_ie_j+2f_if_j).
$$
曲率三分量的贡献为
$$
g_i\mathrel{+}=w\sum_{\nu=1}^3 J_{\nu i}r_\nu,\qquad
H_{ij}\mathrel{+}=w\sum_{\nu=1}^3J_{\nu i}J_{\nu j}.
$$
新源没有改这些乘积和括号。对每个原实际 pair，仅把同一个 value 加入其唯一对称 packed 地址。原对称的两个 dense 地址接收相同 value、相同顺序，故一个地址足以表示二者；原 g 路径原样保留。

metric 与 curvature 的两个独立 normal 仍先各自累加，再在相同地址做一次加法。由有限加法归纳，每个有效地址与原 dense 对应元素相同；空白带位为零。不能把两者逐行穿插以假称相同浮点顺序，现实现没有这样做。

带宽由 factory 的 halfBandwidthBlocks 明确指定。每一次非零 pair 超出该宽度立即抛错，包含极小浮点项；零贡献可以记录而不占位置。保存 packet 的无效 padding 位必须准确为零。J27 的实际 distance4 细尾通过明确 width4保留，绝非阈值删除。

preparePackedBandBorderNormal 只扫描 packed 地址，按原 Hjj 尺度、两次明确对称化和原梯度构造冻结 R195 v2 prepared packet。其原矩阵 lower/upper 缩放分别保存，仍能计算未平均原方程残差。正阻尼、边框 Schur、真实非 SPD 拒绝和后续实际 Armijo全部沿用。

## 3. 可直接运行的完整接口

源：scripts/fd2d_packed_band_normal_provider_R198.cjs。

~~~javascript
const core = createR190BandProvider(engine, bundle, {
  ...originalOptions,
  halfBandwidthBlocks: 4
});
const guided = createR191BandCurvatureProvider(
  engine, core, originalGuide, createR191Algebra()
);
const backend = createPackedBandNormalBackend(kernelV2, {
  halfBandwidthBlocks: 4
});
const lm = createBandBorderLM(backend, guided.definition);
const normal = guided.normal(actualZ);
const step = await lm.lmStep({
  z: actualZ, normal, value: guided.value, lambda
});
~~~

这里使用 R195 的独立 adapter；除一次真实 normal 和 trial 本身外没有额外求值。传入与旧分支相同的完整 options，尤其不能只由浮点 centralGap 反推新 gap。

通用薄接口还包括：

- positionBandLayout(definition,width)：读取明确五段 stateLayout、J/K和dimension；
- createSymmetricBandAccumulator(layout)：给 add(originalI,originalJ,value)、packet()、diagonal()；
- mergeBandPacketsInPlace：只合并同一 layoutBinding；
- bandDiagonal / preparePackedBandBorderNormal；
- expandBandNormalForCheck：仅供明确的小核，需要时才创建 dense 矩阵。

这些函数不依赖 uniform knot公式。geometry 的独立非均匀 factory 可保留其新 radialBasisDefinition 和旧五段范围，只接相同 H 存储 hooks；当前 uniform 源没有冒已完成非均匀 packed实际运行。

## 4. 唯一实际 normal 和一个真实点的对照

使用 R195 同一 immutable R191 state（J12/K7/N64，193维）。本件只新组一次 packed normal；原 dense normal 直接读既有保存数据，没有重组旧 normal。全16405行的 R²、展开 H、g、diagonal 最大数值差均为0；packed prepare/同lambda方向对已有 dense方向最大差也为0。

在同一实际 active curvature 点 s=.20611069331622553,u=π/2 比较完整位置两 jet、实际曲率残差和参数 Jacobian，共758个数值全部差0。列族明确包括 theta14、phi14、Z2、cutHeight1、rho2，五族 Jacobian 作用均非零，未以旧局部曲率近似代替完整链。

width4 raw matrix 为124424B，对应 dense H为297992B；这只比较193维该对象，不是整体内存或速度 benchmark。prepared存储/真实原方程残差另在报告。主张是去掉 n² normal存储、合并、准备扫描；不夸大旧 local outer loop 的复杂度。

首次实际执行在最终报告阶段报 Dimension mismatch：functions.store 把旧 Float64Array 变成无 length 的数字键对象。新 packed normal 已保存；只显式恢复这些数组，没有重组 normal。为了恢复尚未保存的摘要，那个小的两点包比较又执行一次。原失败及原因单独保留；首次wall4.3s包含normal与检查，已丢失的局部normal计时不补造。恢复检查的 prepare+solve实际68ms。

公开 add 对 distance5 的 $10^{-300}$ 非零明确拒绝。没有全 JVP、真实 nonlinear trial或OS进程；不填 shell exit0。

## 5. 保存与复现

跨 functions.store 保存 typed array 时，显式将 g、diagonal、bandNormal.lower、bandNormal.border 用 Array.from；否则数字键对象会丢 length。同一 exec 内正常使用无需转换。这是序列化层限制，不是数学失败。

scripts/fd2d_packed_band_normal_R198_check.cjs 给可复现检查函数，接收已求得的两个 normal和可选实际点包，不自行调用 F/J/normal。它在实际内联检查之后整理并编译；实际执行证据对应报告所列内联过程，不冒其文件在当时已存在。

说明与检查均不认证全域 metric、reach、闭合或强幅度。它们只保证这次实际有限 normal 消费的数学和数值一致。
