# R926：七个原连接的有界多项式分子实际认证

日期：2026-11-16。状态：本篇登记公开 Actions 的实际完成结果；七个原连接的多项式分母、分子和完整全局恒等式已完成。目标代数上的分母单位、七连接目标值、Gal7/cY 数值作用与最终高度均不在本次完成范围。

## 1. 实际来源与执行身份

原数学证明为 [R922 §§2–4](R922-original-bounded-connection-numerators-and-whole-Hecke-evaluation.md)，准确全文 SHA256 为 75e0e04e986203598b556403b4ea8eec3706da838e934ae11810c5abda569731。执行方法见 [R926 method](../notes/R926-original-seven-bounded-connection-polynomial-numerators-method.md)，SHA256 为 c4d05c61187dfcc5997e737f3a072d40b540e67d81bbe899089fb0120b9506c2。

本次真正运行：

- [公开 run 43916091665](https://github.com/Rogerhu12/math-research-public/actions/runs/43916091665)，数学 job 133470621197，结果 success。
- 源提交 665dd92b8703fa7118d90fbee0eba7f07e2d60ee；core SHA256 970a539931f7d101b8c624b2c7fc56b74b96b75e727e65fe22808de37af9583d；wrapper SHA256 a1b5ec8e061cc91e6427adf6311a4ba2d0ea711db7b290aef9c9fac9d61a698d。
- 实际请求 SHA256 29dd4349fd7bd1b6ee36d40ddea76a5b4bc7db94908df4af626fcc1208c0369d；workflow SHA256 e496f246c93673ba48b8cbbf3b229964a170f40fafece01f821089ac21b9dd85。
- 数学 configuration SHA256 8d865612158629b0241e9a0f0799ad6ae4270fd934a43af2d3782e040cc697ff；core 实际时长 5.079957719000049 秒，exit 0。
- 实际完成 288 个完整 stage、全部七个原除子；另保存一个 current。不是根据请求 scope 推定完成计数。

规则 job 133470520432 在 2026-11-16T17:13:36.593344+00:00 真正 pull main 至上述源提交，两 README 的完整 SHA 分别为 6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9 和 35f82f3d96f1e07d1b7c3f0320398fdc0cd68d0c0e55ac17881c9f976299646d，无变化。

唯一旧数学生产者是 [R905 的七原连接](R905-certified-original-seven-trace-dual-connections-and-five-Picard-inputs.md)，实际 run 43893738459/source f4589d2b0d8f5e2a914ca165a601351d09c303a9，configuration fe220a1b3216cd28a16d0d3c1916f4660b7708c39a129e8696ba285c2c9e7136，FINAL 24045a35dcd878cad48d28aea20bce7077161b0eb9dc86113a54ba83bc71d4a4。每个除子只取原准确连接 DAG、完整 bundle unit graph、完整 quotient/division model 和原 full-principal-parts solution，再加原 FINAL 与四个元数据成员，共33件。原544×670主部矩阵、原逆和原 primitive 特征式均未重算。

## 2. 原连接、基和系数完整保持

原次序固定为 $D_1,D_2,D_3,D_4,D_5,X,D_N$。七个实际辅助值都为 $a=0$。原完整272维 bundle 矩阵 $F_D(z)$ 的前146列 section weight 为2，后126列为3；不能将旧 column_weights 的 splitting weight 误作这两个数。

原微分基和670个系数写作

$$
t^k\theta_i\,dz,\qquad 0\le k<n_i,\quad t=z-a,\qquad
c_i(t)=\sum_{k=0}^{n_i-1}c_{ik}t^k.
\tag{926.1}
$$

沿真实 DAG 的 basis.indices 逐一对应，原543选行列、所有未选坐标及其零值、原帧 $dz$ 都保持不变。所求仅是同一连接的表达

$$
F_D(a+t)^t x_D(t)=c_D(t).
\tag{926.2}
$$

实际 IO 已核原每个 full-principal-parts rank 均为543。七个原 $F_D(0)$ determinant 如下；它们是已成输入的实际值，本次未重算其逆。

|原除子|原 determinant 模 $\ell$|
|---|---:|
|$D_1$|69734280|
|$D_2$|168135538|
|$D_3$|994658365|
|$D_4$|651677365|
|$D_5$|289814217|
|$X$|340087577|
|$D_N$|217513425|

全部有限数组仍在原辅助域 $\mathbf F_\ell$、$\ell=1000000753$ 中；它们不是41进数值，也不是展开的特征零系数。

## 3. 全部 degree-272 除子上的新范数

从旧 quotient $Q_D$、原 $h_a$ division $L_a$、原正常坐标中的乘 $\tau$ 及 literal free-row embedding，形成新算子

$$
Z_D=Q_D L_a T_\tau E_D.
\tag{926.3}
$$

它是整个 $H^0(\mathcal O_D)$ 上的乘 $\tau/h_a$，并实际核其作用于原代数单位的坐标。新算子的一次完整 characteristic polynomial 给

$$
d_D(a+t)=\det(I-tZ_D)
=\frac{\det F_D(a+t)}{\det F_D(a)},\qquad d_D(a)=1.
\tag{926.4}
$$

这里保留完整272维，包括零特征部分、除子与 $H$ 的交点、非约化重数；不选几何点，不假定 $D\cap H=\varnothing$。若倒序多项式最高系数为零，只如实记 $d_D$ 的较低次数，不删除原特征式中的零特征部分。此新范数与旧 primitive element 的 characteristic polynomial 不同。

## 4. 仅复用原逆的274个新向量

用原已经认证的 $F_0^{-1}$，写 $F_D(a+t)=\sum_{m=0}^3F_mt^m$，实际递推

$$
x_r=F_0^{-t}\left(c_r-\sum_{m=1}^{\min(3,r)}F_m^t x_{r-m}\right),
\qquad 0\le r\le273.
\tag{926.5}
$$

每16个新向量为一个不可变 stage，最后一块含两个向量，共18块；各块保留真实前块引用、原逆和原系数来源。七个 $a=0$ 不发生额外平移算术。形成

$$
y_D=(d_Dx_D)\bmod t^{274}.
\tag{926.6}
$$

所有272个分量的界

$$
\deg y_{D,i}\le271+\epsilon_i
\tag{926.7}
$$

均在实际运行中通过。输出同时保存 $t=z-a$ 与原 $z$ 的坐标，不引入新标量。

### 完整数学出口

七个除子都通过完整多项式恒等式

$$
\boxed{\ F_D^t y_D=d_Dc_D\ }.
\tag{926.8}
$$

核的是全部272行、所有 $t^0,\ldots,t^{276}$ 共277个系数，包括右侧次数上界之外的最后两个零系数。完整左右乘积保存在原子系数块中。这不是把274项 Taylor 前缀当成全局证明，而是用有界多项式的完整乘回证明它确实表示原同一有理函数。

准确特征零对象仍明确为

$$
d_D=\det F_D/\det F_D(a),\qquad
y_D=\operatorname{adj}(F_D^t)c_D/\det F_D(a).
\tag{926.9}
$$

原 $F_D(a)$ 在实际处为单位，故本次数组是该准确来源表达式在指定剩余处的像。特征零表达式已定义并保留，未声称其全部系数已经展开。

## 5. 真实证书与必要来源载体

|实际成员|字节|SHA256|
|---|---:|---|
|p41-original-seven-bounded-connection-polynomial-numerators-certificate.json|12088|e60d5ebbe3c4a6b3632db30856c5f697130ba41fb26f352b72983616fea6bb54|
|full-outputs-manifest.json|40833|9f1be86937b3cb48554b7f47801c15250e55e8cda87c32a83bffa2576a48c8c9|
|R926-retained-original-inputs.tar.gz|19671600|33c988ac2f94cf719f2a7813fe3faf5a9c75fbe73e1c121d1e54e9aabf7ea18a|
|R926-original-source-inventory.json|16258|bcb54f73e1008c6018a3bed1c6723905ebf65b2a9a2720b0c52de038950d02ff|

七个完成证书均为 R926-{label}-complete-bounded-connection-certificate.json.gz；它们指向该除子的真实分母、分子、18个新向量块、完整乘回块及准确表达式。

|label|字节|SHA256|
|---|---:|---|
|D1|4978|3ee158cf4b47011a258cba1640afa2c1a7e8124f9724e1e1c67ad2bb3f2dc158|
|D2|4989|5ded42d6ddae3614d3b81e9e582ce2a8e314615e952ccf88375e15a0215b2e81|
|D3|4990|5900e82e656ad084e8350bb02be29386b1991e40e5ef3451a8b1f70ac9372023|
|D4|4978|90bc50a5dc92c3ad6c5fc1ff13be4716399288de27827a4b551158ba6239146e|
|D5|4978|5ba1fb1b8b7b4b7c4f52933946cd9e643e7b5da98358b145f54a902014cbe150|
|X|4995|4bb484856066f126049ffb5358dd7233e424a5dc0237d3770c5133bcbc418571|
|DN|4997|72f971fb223a512a9608b6592b5394e370829101efa211fdf24972ea3dfb1618|

Actions artifact 为 serre-global-R926-seven-connection-polynomial-numerators-43916091665-1，ID 14251085383，大小31075923字节，平台返回 archive SHA256 03c783c6cab1f2b68315155b8d3cce97091a0e2e5cdad34c49e2e5be43b8b6b9，到期时间2026-11-17T17:14:40Z。这里区分平台 archive digest 与运行中逐成员 SHA；未声称在外部环境重新哈希整个 ZIP。新数学全部仅在该公开仓库 Actions 内执行，外部只读源码和实际 IO/receipt。

## 6. 接续与严格边界

[R922 共享 $R$ 实际结果](R922-certified-original-shared-polynomial-trace-dual-multiplier.md) 已另行完成。后继可直接消费其低权矩阵和本篇七组多项式，不重旧 $F$、Gram、$M_g$、Krylov、主部解或 primitive 特征关系。

不过 $d_D(a)=1$ 并不保证 $d_D(U)$ 在整个原目标代数 $E$ 可逆。目标消费者必须逐个取得真实全 $E$ 单位证书，保留所有因子与幂零。若不单位，保存真实失败因子和相应数据，不能只删坏分支后声称原目标值已成。

目标坐标仍是 $V=K(U)/P_U(U)$。R928 只新增八个 $\delta K$ 并保完整商法则，求真目标 $g_t,h_t$ 和 $J$；未来七连接评价消费这一真实结果。原 Gal7、$c_Y$、主函数修正、$\kappa,\nu$、canonical dual7、两端帧、非 $p$ 项、period 与 height 都不能由本篇自动推出。绝对 Serre 一致性主目标仍 OPEN。
