# 同一完整输入向量的帽二阶换坐标源合同

## 1. 固定对象和新的费用

本合同只在公开仓库 Rogerhu12/math-research-public 的 Actions 中计算新费用。完整中心是 ac1 的连续 M32 修补，定义 SHA256 为
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`；
参数为仿射偏移零，即固定物理 $\eta_0$ 和原 $\nu$。

原物理帽矩阵 trial $T$ 是全部 97 个 moving orthonormal even 输入到 257 个物理状态的准确分段三次 Hermite 矩阵。它的 descriptor 为
`b9819522aceed06b73628d84b8bb80dbcc5b734971c6b3c20544e9876c23d78a`。
令 $w_0\in\mathbb R^{97}$ 为已成功 v3 方向 native
`f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c`
中的原 binary64 十六进制向量，所有 97 槽包括 even mean 均保留。每个 binary64 值视为准确二进有理数。新 trial 是准确同一列
$$
t=T w_0. \tag{H.1}
$$
它不是重新求得的帽解，也不是改变后的近似对象。

原完整 Hessian native
`cf055cac05569701ebcb0df95fb064c94cec8c18bb28121292a3836b3862be26`
给出了全部 97 列的 Hilbert–Schmidt 源上界。本次直接计算 $\mathcal E_H(t)$，从而可以改进
$\mathcal E_H(T)\|w_0\|$。原物理残差、真实边界、完整算子反馈都不重复计算。

## 2. 全部局部系数及原完整 Green 权限

[局部三角源定理](../results/R133-supplement-local-triangular-cap-Hessian-and-trial-source.md)
的 (L.7)–(L.15) 明确对单个 trial 同样成立。其原完整 local native 为
`bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd`，
包含 $[9/10,25/8]$ 上 1341 个真实源格、六个有向局部系数
$E_A,E_1,Z_{BB},Z_{BC},Z_{CC}$（连同已保存的辅助系数），四个完整物理 Green 源增益及原 Hessian resolvent。当前新消费者按原件逐项使用这些权限，既不调用 target provider，也不重新估计中心 residual、inverse angle 或 primitive。

对准确的三次 $t$，物理 Fourier Gram 因子保持为
$$
\|t_B\|_2^2=\frac12\sum_{j=1}^{128}|t_{B,j}|^2,\qquad
\|t_C\|_2^2=|t_{C,0}|^2+\frac12\sum_{j=1}^{128}|t_{C,j}|^2. \tag{H.2}
$$
方向输入已是 orthonormal 97 维，不能再对 $w_0$ 的非均值槽除以 $\sqrt2$。输出 mean 不能按非均值除以 $\sqrt2$。

## 3. 完整连续普通源和 divergence 源

每个原局部源格 $I_i$ 与实际 Hermite 片相交。全部相交片数必须仍为 1977。实际第一个数组节点是 binary64 的 $0.9$，与准确 $9/10$ 分别保留；在二者之间采用同一原首三次多项式的延拓，不移动入口。

在每个真实交格 $J$，先对完整 Hermite 系数右乘准确 $w_0$。有向区间点积保留全部舍入半径。将所得三次多项式写为
$t=\sum_{k=0}^{3}L_kP_k$，准确的径向积分为
$$
b_J^2=|J|\sum_{k=0}^{3}\frac{\|L_{B,k}\|_2^2}{2k+1},\qquad
c_J^2=|J|\sum_{k=0}^{3}\frac{\|L_{C,k}\|_2^2}{2k+1}. \tag{H.3}
$$
完整普通源满足
$$
O_B^2\le\sum_{i,J\subset I_i}\big((E_{1,i}+Z_{BB,i})b_J+Z_{BC,i}c_J\big)^2,\qquad
O_C^2\le\sum_{i,J\subset I_i}\big((E_{1,i}+Z_{CC,i})c_J\big)^2. \tag{H.4}
$$

对于 divergence 源，先逐个真实物理 Fourier 槽取三次 Bernstein 凸包上界，再在 $I_i$ 内所有交格取逐槽最大值；之后才按 (H.2) 求和。这给出 $b_i,c_i$，并有
$$
D_B^2\le\sum_i(E_{A,i}b_i)^2,\qquad
D_C^2\le\sum_i(E_{A,i}c_i)^2. \tag{H.5}
$$
(H.5) 没有径向长度因子。其依据是完整模块的逐 Fourier 槽径向上确界与 Young 不等式。有限 trial 的支撑没有截掉系数乘积或未知真解的高频。

每一原局部格及每一个源范数还有原 97 列 HS 界乘 $\|w_0\|$ 的独立合法上界。只对同一标量范数选择两者之一较小的值是合法的；该选择不改写方向多项式，也不删除其区间半径。

## 4. 特定方向的真实换方程误差

沿原完整物理 Green 的四个增益，
$$
\mathcal E_H(t)\le
G_{o,B}O_B+G_{o,C}O_C+G_{d,B}D_B+G_{d,C}D_C. \tag{H.6}
$$
这些增益已包含全部物理系数反馈、真正外图和完整 mean，不得第二次加入同一反馈。

令 $A$ 为已证残差敏感二阶换坐标反馈，$\|A\|<\chi_H<1$。同一真实完整端口下的物理解与 moving 解满足原定理的关系，故
$$
(I-A)(x_{\rm mov}(w_0)-t)
 =x_{\rm phys}(w_0)-t+A t.
$$
若原完整物理残差消费者给 $\varepsilon_{\rm phys}(w_0)$，则
$$
\|x_{\rm mov}(w_0)-t\|_{\mathfrak M}
 \le \frac{\varepsilon_{\rm phys}(w_0)+\mathcal E_H(t)}{1-\chi_H}. \tag{H.7}
$$
新输出只提供 (H.6) 及其乘原 resolvent 的加性项。完整物理普通/divergence 源、两端真边界和全部点源继续在 $\varepsilon_{\rm phys}$ 中收费。

若完整连续方向 $Z$ 的真实 cut even 输入为 $e_Z$，则原完整 moving **误差算子**范数仍负责剩余输入差：
$$
\varepsilon_{\rm mov}(e_Z)
 \le \varepsilon_{\rm mov}(w_0)
       +\|\mathcal E_{\rm old}\|\,\|e_Z-w_0\|. \tag{H.8}
$$
不能用新单方向加性项替代未知输入算子的范数。之后的 true97、独立 mean 和 known high 输出仍分别经原 cut 变换及其完整费用。$q_{\rm raw},q^*,Z$ 没有被认作同一对象；方向和背景转授均按各自已证定义执行。

## 5. 实际执行与输出范围

新 worker 只从原公开 Actions artifact 恢复准确数组和原成功 v3 native，检查整个数组 SHA；原 1341 行和完整 Green 权限从冻结公开原件读取。所有新数学仅计算 (H.1)–(H.6)。它不重算原 physical residual cells，也不重建候选、目标、原 mean 流或 exterior。

每 64 个局部行保存真实 native 前缀，包含每个原行的精确身份、实际相交片数、四个新源范数及独立旧上界。恢复时完整核验同源码、同全部输入、同 $w_0$ 和同数组。已经完成的数学 native 在原 child 真实返回 0 后可逐字节复用，即使旧外层发布失败；不要求旧 process.complete。分片恢复验证全部字节及总 SHA。新摘要逐件限制为 60000 字节，完整数学行保存在 native。

本合同本身没有宣称新上界已经通过实际数值门。成功后的权限仍是特定 $w_0$ 的完整帽 Hessian 源；完整 cut 源、有限 193 态响应误差、未知 high 反馈及完整无限维逆分别保留。
