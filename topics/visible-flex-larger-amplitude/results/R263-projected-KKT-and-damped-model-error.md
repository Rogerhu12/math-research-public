# R263. 投影 KKT、正阻尼模型后验误差与实际 LSMR 停止

**状态：已证明（有限实线性代数定理）**。设固定正阻尼 λ>0，保护投影为精确正交投影；第3、4节给完整证明。实际浮点诊断只是独立的数值例，不冒严格舍入证书、BVP 接受或几何完成。

本条只读实际 run
[43603477207](https://github.com/Rogerhu12/math-research-public/actions/runs/43603477207)
的 `protected-warm/model-000.json` 及对应源码，并作有限线性代数推导。
没有重新计算矩阵、方向、残差或模型，没有改正在执行的三保护行主线，
也没有加入新 BVP/几何接受门。

实际模型 JSON SHA-256：
`a143788e61e16f2d9d219dd1cfef3b71a015d517f7188ba24f4962a53eddb42f`。
实际来源 driver SHA
`b126ba6a203cbf97c4c9658abe70e9bf38ad259b2eab89bfed4c6e03f4d97fad`；
projected operator 源
`geometry_20261114_hermite_domain_constraints.py` SHA
`d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce`。
实际完整数据位于
`notes/public-actions-43603477207-1-trustprotected/protected-warm/`。

## 1. 实际数字与精确定义

| 已保存诊断 | 数值 |
|---|---:|
| 正阻尼 $\lambda$ | 270 |
| LSMR `istop` / iterations | 2 / 80 |
| LSMR 内部 `normar` | 2.6137178788426586e−5 |
| 另行实际算的 preconditioned normal norm | 2.613717878864138e−5 |
| projected KKT norm | 344.9209993189766 |
| full unprojected gradient norm | 344.96458987991326 |
| 实际 $\|z\|_2$ | 0.0029047519879436046 |
| 实际 $b^TAz$ | −1.071287283217619 |
| 实际 $\|Az\|_2^2$ | 0.45618734910041925 |
| 实际 $\lambda^2\|z\|_2^2$ | 0.6150998817256035 |
| 下降恒等式缺陷 | −5.2391596283563047e−8 |

固定一个模型。令 $b=W_rR$，$A=W_rJS^{-1}$，其中 $J$ 是全部
原物理 collocation 与完整右 BC 对 exact coordinates 的导数，$S$ 是
原优化 Sobolev/控制尺度。令 $P=P^T=P^2$ 为临时保护行的正交切空间
投影，$V=\operatorname{range}P$。本次 $V$ 只有一个保护行；以下结论
对后续有限个独立保护行一样成立，但每次必须是该模型自己的 $P$。

原模型可等价写为

$$
 \phi_\lambda(z)=\tfrac12\|b+Az\|_2^2
                 +\tfrac12\lambda^2\|z\|_2^2,
 \qquad z\in V.
$$

源码使用正对角

$$
 C_{jj}=\sqrt{\|Ae_j\|_2^2+\lambda^2},\qquad
 \widetilde L=\begin{pmatrix}A\\\lambda I\end{pmatrix}PC^{-1},
 \qquad z=PC^{-1}v.
$$

这里 $C$ 是**原未投影 A 的列范数**形成的预条件，不声称是
$AP$ 的精确列范数。LSMR 的 `damp=0`，正阻尼完整保留在
$\widetilde L$ 的下半部；它没有误罚未投影的 $v$。

令

$$
 e=\begin{pmatrix}b+Az\\\lambda z\end{pmatrix},\qquad
 \gamma=A^T(b+Az)+\lambda^2z,\qquad r=P\gamma.
$$

由源码中的伴随公式，严格有

$$
 \widetilde L^Te=C^{-1}r.
$$

因此两行实际诊断分别是 $\|C^{-1}r\|_2$ 和 $\|r\|_2$，没有
互相矛盾，也没有漏掉伴随中的 $P$。它们在精确零点上等价；在固定有限
容差下不是同一精度条件。对角尺度给出

$$
 \frac{\|r\|_2}{C_{\max}}
 \le \|C^{-1}r\|_2
 \le \frac{\|r\|_2}{C_{\min}}.
$$

实际保存的未投影列范数范围为
`[0.0077880715128469105, 74620159.633333]`，故这里的 $C$ 尺度跨度
很大。小预条件残差完全允许同时出现表中的 344.921 受限梯度。

报告所说“未预条件”只指去掉 $C$：该量仍是在 $W_r$ 加权、$S$
缩放后的优化坐标中，不是未加权原 PDE/BC 残差，不能与原 solver 的
RMS 或 BC 容差直接比较。全 $\gamma$ 还含约束乘子方向；受限最优性
相关的是 $r=P\gamma$。本次 $\|\gamma\|$ 与 $\|r\|$ 都约 345，
所以不能把大的受限梯度解释成“仅有允许的法向乘子”。

## 2. `istop=2` 实际说明什么

原源调用 `atol=btol=1e-7`、`conlim=1e12`。
[SciPy 1.17.0 官方 LSMR 文档](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.sparse.linalg.lsmr.html)
把 `istop=2` 解释为满足其 least-squares 停止条件。对应测试是

$$
 \frac{\mathrm{normar}}
      {\mathrm{normA}\,\mathrm{normr}}\le\mathrm{atol}.
$$

本次三个内部记录为
`2.6137178788426586e-5`、`29.501839379909946`、`9.371394621100055`；
满足的是这条预条件模型测试。80 是实际迭代次数，返回码不是代表达到上限
的 7。保持同一停止规则而只提高 `maxiter`，不会阻止这次同样在该条件满足
时停下。当前下一三行模型改变了 $P$，不能据此预言其次数。

`LSMR_condA=4.2811076454353225` 也不是原受限 Hessian 的严格条件数界。
甚至 $\widetilde L$ 在 ambient $v$ 空间有明确冗余核
$C\ker P$，而 $\phi_\lambda$ 在真正的 $z\in V$ 上仍严格强凸。
迭代中的条件数估计不能拿来否定这个核或证明原全部方向条件良好。

## 3. 可直接使用的受限强凸后验界

在精确正交投影的有限模型上定义

$$
 H_V=\left.P(A^TA+\lambda^2I)P\right|_V.
$$

对每个 $u\in V$，

$$
 u^TH_Vu=\|Au\|^2+\lambda^2\|u\|^2
 \ge\lambda^2\|u\|^2.
$$

因此有唯一受限极小点 $z_*$。若 $z\in V$，则
$r=H_V(z-z_*)$，从而

$$
 \boxed{\|z-z_*\|_2\le\frac{\|r\|_2}{\lambda^2}},\qquad
 \boxed{0\le\phi_\lambda(z)-\phi_\lambda(z_*)
             \le\frac{\|r\|_2^2}{2\lambda^2}}.
$$

证明不需要建立 normal equations，也不需要估计 $\|A\|$：令
$h=z-z_*$，由 $H_V\succeq\lambda^2I$ 有第一式；又因二次函数

$$
 \phi_\lambda(z)-\phi_\lambda(z_*)
 =\tfrac12h^TH_Vh
 =\tfrac12r^TH_V^{-1}r
 \le\frac{\|r\|^2}{2\lambda^2}.
$$

相应的模型作用误差也有

$$
 \|A(z-z_*)\|^2+\lambda^2\|z-z_*\|^2
 \le\frac{\|r\|^2}{\lambda^2}.
$$

本次第一式给出的上界是

$$
 \frac{344.9209993189766}{270^2},
$$

它大于已保存的 $\|z\|=0.0029047519879436046$。第二式给出的上界是
$(344.9209993189766)^2/(2\,270^2)$。这是从已有实报代入的后验表达式，
没有另跑矩阵或数值模型；它不能证明本次方向已高精度接近受限最优方向，
也不能反向证明该方向确实远离最优——上界可能松。

若要以“取得了足够比例的这个模型最佳下降”作优化内层精度标准，可令

$$
 \Delta=\phi_\lambda(0)-\phi_\lambda(z)>0,
 \quad E_\lambda=\frac{\|r\|^2}{2\lambda^2}.
$$

若选择明确的优化参数 $0<\eta<1$ 并实际满足
$E_\lambda\le\eta\Delta$，则

$$
 \frac{\phi_\lambda(0)-\phi_\lambda(z)}
      {\phi_\lambda(0)-\phi_\lambda(z_*)}
 \ge\frac1{1+\eta}.
$$

这来自 $\Delta\le\Delta_*\le\Delta+E_\lambda$，是目标明确的内层后验
判据；不需要把模型 KKT 硬压到原 PDE 容差或机器精度。现有源已经计算
$r$、$Az$、$z$，不需要额外分解才能记录此诊断。

这些是有限实线性代数结论，不把本次浮点记录自动变成严格区间证书。
若要付舍入误差，需对实际受限梯度误差给出 $\varepsilon_r$，上界中用
$\|\widehat r\|+\varepsilon_r$。若实际向量只近似可行，先按声明的精确
正交投影取 $\bar z=P\widehat z$，另付 $\|\widehat z-\bar z\|$；不能
仅因浮点 leak 很小就忽略它与大算子范数的乘积。本次数值 leak/idempotence
检查是优化实现诊断，不是这类严格舍入包络。

## 4. 小的下降恒等式缺陷不代替完整 KKT

对可行 $z$，严格有

$$
 d=b^TAz+\|Az\|^2+\lambda^2\|z\|^2
   =z^T\gamma=z^Tr.
$$

所以本次 `−5.2391596283563047e−8` 只约束梯度在当前 $z$ 上的一个
内积。与 $z$ 近乎垂直的较大 $r$ 完全允许该数很小。不能用这一
近似一维恒等式替代全受限梯度，也不能反过来因全受限梯度大就否认已经
实测的严格下降。

原真正非线性 merit 没有正阻尼罚项，方向导数仍是实报的
$b^TAz=-1.071287283217619<0$。当前方向在
$\alpha=2^{-10}$ 经完整原 RHS、BC、node/midpoint/两 RMS 查询和 rho
检查后，实际 merit 从 `44.447162239996025` 降到 `44.446116127468`；
实际下降 `0.0010461125280230021`、actual/predicted ratio
`1.000144429398848`。这些真实结果不以“内层已经精确最优”为前提。

更大步长的域失败与 LSMR 截断是不同问题。已保存试探确实暴露其他角度/
interval 的坏点，给下一三保护行切空间提供了直接依据；现有 KKT 数字
不能证明“若内层多算，坏点就消失”或“坏点必由截断导致”。

## 5. 对下一停止规则的具体含义

证据支持把原 `istop=2` 视为预条件模型的停止回执，并在有必要改进**同一个
固定模型**时，以实际受限梯度及上述后验量判断是否继续内层求解。那时应
明确调节其 least-squares 停止精度，不能只盲增 `maxiter`；整个
$A,W_r,S,P,C,\lambda$ 的身份必须保持，才是在改同一模型的求解精度。

它不支持现在打断基于实际坏点的新三行模型，也不支持新增科学接受门。
原下降/ratio、全域可行性、实际 nonlinear tail、完整 BVP RMS/BC 与最终
几何完成条件继续各自判断。本次保存的 `warm-001.json.gz` SHA
`0036063ff99e7b3624e494b29430b9a3a8ec3eaae15f277447efcc71b8cc5e71`
仍是 `success=false` 的域内下降 warm，绝非新接受父场。
