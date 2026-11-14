# R133：固定 eta0 的物理系数域细化与完整分解 pilot

2026-11-14。新计算针对完整帽 $[9/10,25/8]$ 中已经完成的同一 $w_0$ 方向，只改变显式注明的**包络域**：原参数半宽 $10^{-9}$ 缩到仿射偏移 0（即固定物理 $\eta_0$），并细分所选原径向格。实际中心、$\nu$、原候选、原连续修补、物理帽试解与其 Fourier 槽完全不变。

## 1. 原源及待收紧组件

原物理消费器对已知 $B,C$ 保留
$$
 V_B=B_r+2\beta B,\qquad
 F_B=\gamma K s^2 C-\gamma(Q_BB+Q_CC), \tag{P.1}
$$
$$
 V_C=C_r+\beta(Ks^2+1)C-\beta(Q_BB+Q_CC),\qquad
 F_C=-\gamma B. \tag{P.2}
$$
其有限模型以 $V+\partial_\theta F$ 读取全部已解析 Fourier 输出，非 mean 用原 $M^{-1/2}$ 源范数，两个完整 mean 单列。scalar 和真实逆角 Fourier 系数的无限余项仍按原 ordinary/divergence 合同收费。

特别 $d_B$ 是系数余项的 divergence module，不是一个已知有限函数的角导数。本 pilot 不将它免费改成 ordinary 源，也不删除 Fourier tail、alias、model rounding 或第三径向 Taylor 余项。

## 2. 准确旧输入与新的有限请求

基线直接取实际 run 43615251195 的四个成功 one-column range 和原成功 v3 pilot 的 16 格。四范围的原 native 与 artifact process 必须逐一符合 complete1977 native 的 range receipts；恰 1977 格、无缝覆盖和无重计数都重新消费。

每个直接 one-column 行的八项
$$
 (f_B^2,f_C^2,f_{B0}^2,f_{C0}^2,
   r_B^2,r_C^2,d_B^2,d_C^2) \tag{P.3}
$$
作为**同一个系数模型的完整分解**接收。该基线不需要断言旧 97-column 算法和新 one-column 算法的内部浮点中心逐 bit 一致。

按这些实际原行的 $d_B^2$ 上界选最大 16 个父格。选择只影响效率，不影响界的有效性。每个父格有三个新请求：fixed eta0 的整个父格、4 等分和 16 等分，共
$$
 16(1+4+16)=336 \tag{P.4}
$$
个显式新域。它们都留在原候选 cubic、真实 scalar germ 和原 Hermite 片内。新 target 调用只为这些新的参数/径向域产生严格 whole/midpoint jet；不重跑原半宽 $10^{-9}$ 的同一格。

## 3. 每个新域的完整身份

每域使用原真实逆角、512 个有向 FFT 节点及 cutoff 127；帽试解保留全部 128 非 mean 模和物理 even mean。有限卷积总支持仍为 $128+127=255$，完整无限系数输出由原 joint Wiener 误差支付。输入为原准确 97 槽 $w_0$，不会先删掉输入 mean。

原三大数组、两侧导数、endpoint graph 的字节 SHA 必须保持；第一格从准确 $9/10$ 到 binary64(.9) 的极短原 Hermite 延拓完整保留。固定 eta0 不解释成物理参数等于零。

每个新域保存完整 provider 行、scalar remainders、八项累计量和真实时间。成功前缀按同一 source、全部输入、确切请求顺序恢复，不重新计算已完成的新域。

## 4. 新旧模型的整组选择

新域使用的 Fourier/Taylor 系数多项式可能与原模型不同。因此 finite 项与 remainder 项的分解也可能改变。**不得独立对八个分量各取 min 后拼成一份从未被证明的分解。**

先将一个细分策略的所有子格八项各自求和，得到该父格的一个完整合法表示。旧直接 one-column 行也是一个完整合法表示。以
$$
 \sum_{\ell=1}^8 G_\ell\sqrt{s_{\ell,i}} \tag{P.5}
$$
作为选择分数，整组选择某一个表示。这个局部分数只作选择，不冒称最终全径向误差。

所有父格选定后，对各源种类按原规则在全 1977 格上平方和、开方并乘原完整 Green 增益。divergence module 没有多乘径向格长；ordinary/finite 源的原格长保持。六个真实边界/jump 负荷沿原完整方向结果复用，总共原 14 项全部保留。

另计算全旧直接 one-column 基线的完整总界。最后可在**两份完整总误差**之间取 min。此前出版的 mixed 数字仅作比较记录，不替代本篇明确构造的完整分解。

## 5. 实际输出和范围

原完整 cut native 为
8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5；
原固定方向 pilot 为
f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c。
两者都通过真实 run、source、worker、manifest、全部门和原字节核验。

新主 summary 只列全部门、完整总预算、原14通道分解和所选16父格。每个父格有单独小诊断，列旧系数各误差、完整策略八项以及全部新子格的 coefficient/scalar error，所有新 plaintext 写前都核小于 60,000 bytes。完整 native 不删任何原请求和新 provider 行，超过大小限制则原字节 lossless 分片。

本结果仍是已知同向物理帽误差的合法完整上界。它不自动付 Hessian、true cut source、未知 high 输入、finite193 响应或全 PDE 逆。是否全帽扩展到所有父格，应由此次真实组件诊断决定；所有成功新子格必须保留供后续复用。
