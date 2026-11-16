# R919 实际认证：原九导数、完整八维 Hecke 微分迹及 272 个正常基目标像

日期：2026-11-16。状态：公开仓库实际运行完成。这里只登记本次已真实生成的完整有限代数结果和原特征零表达式来源；主目标仍 OPEN。

## 1. 实际运行与不可变身份

[公开运行 43904104159](https://github.com/Rogerhu12/math-research-public/actions/runs/43904104159) 的数学 job 为 133428298451，原源码提交为 1e0ecf187b6e282226833c6c45c5e94661a0a9b1。退出码 0，core receipt 为 complete；没有外层超时。核心 receipt 记录时间 1.7841667400000034 秒，终证内部记录 1.7838980530000015 秒，两者各按其原计时范围保留。共完成 66 个数学阶段，另有一个不冒成功阶段的 current。

| 项目 | 实际绑定 |
|---|---|
| result | R919-original-whole-Artin-Hecke-differential-trace |
| 原问题层、辅助素数、源纤维 | $p=41$、$\ell=1000000753$、$z_s=0$ |
| core SHA256 | 379083fd253ec82af43d185ddd6aed6f33ca6985d70e9864bab8f0a5ce1ef7ee |
| wrapper SHA256 | 0c5b7cc64a0cb8c0d12c0a953f430291c6ae3fc921c1f4f3245ce66992484ad4 |
| 原 R885 helper SHA256 | e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d |
| method SHA256 | 2024a082f600a9296786575d59d5694082ac21a43569fe4d8a5caca96a6a6b60 |
| active request SHA256 | 8cc51f4b2aa84abff97bcd71bb62afcae448a27413f1fb7db523d959990393cc |
| 数学配置 SHA256 | cb2e457199bc9856e16fbebcfc1cfecbb0a94388bbee274e65047499ea0e3ede |
| core receipt SHA256 | 6421e098699d344c84e30f63575c80c12ed7725d20b4a9d7b73c87668665ccc2 |

执行契约为 [R919 方法](../notes/R919-original-whole-Artin-Hecke-differential-trace-method.md)。数学证明采用 [R915 原 Euler 泛函](R915-original-Hecke-differential-trace-and-Euler-coefficient-functional.md)、原 R873 对应、R882 同素点十七系数及 R885 完整 Artin 目标坐标。本次没有更换原曲线、原 $-3$ 下降、原 $82$ 尺度或源/靶方向。

## 2. 完整对象和原导数

本次始终在原完整代数

$$
A_0=\mathbb F_\ell[X]/(\chi(0,X)),\qquad
E_0=A_0[U]/(P(U)/a_8)
$$

中工作，维数分别为 272 和 $8\cdot272=2176$。没有选择一个几何根、只取平方自由商、丢弃其他因子或删除幂零。

原导数是

$$
\delta=\nu^{-1}d=g\,\frac d{dz},\qquad
\nu=82\tau\,\frac{dq_Y}{q_Y}.
$$

它首先指原函数域上的导数，先作用于原函数，再减到 $z_s=0$；没有冒称为商代数 $A_0$ 上的导子。源 $z$ 的导数为原 $g$，不因代入 $z=0$ 而变零。

原 R827 的全部 17 个 $\Gamma$ 块、$W/g$ 与 Krylov 逆，R807 的 $\theta,N_{692}$，R882 的 $2058\times17$ 常数坐标矩阵，以及 R885 的完整目标正常基和原 $a_8,P_U$ 逆均直接复用。原 unit-solve 的系数属于常数域，导数为零；只对其原 2058 个基函数应用乘积法则及商法则，再合成前九列。八个 $K$ 系数没有新求导。

实际得到全部

$$
\delta P=\sum_{i=0}^{8}(\delta P_i)U^i,
\qquad
(\delta P_0,\ldots,\delta P_8)\in A_0^9.
$$

对应数组为 $9\times272$，完整消费全部 2058 行，不截取部分方程或基函数。

## 3. 完整八维迹行

沿原源映射，输入为 $h\,dU$ 的微分。本次生成的 $A_0$ 线性行是

$$
\mathcal L(h)
=-a_8^{-1}[U^7]\bigl(h\,\delta P\bmod(P/a_8)\bigr).
\tag{919c.1}
$$

输出微分为 $\mathcal L(h)\nu_s$。只有当 $h=\pi_t^*A$ 时，才把输入写成原靶微分 $\pi_t^*(A\,dz_t)$；任意 $h\in E_0$ 的延伸没有被写成不存在的靶函数拉回。

实际保存了 $\delta P$ 在 $E_0$ 中的完整余式及 $U^j\delta P$ 对 $j=0,\ldots,7$ 的全部余式，由此得到八个完整 $A_0$ 系数。行形状为 $8\times272$，余式形状为 $8\times8\times272$。原 $a_8^{-1}$ 从已成完整纤维直接读取。

实际还逐一给出八个幂基输入的等式

$$
\mathcal L(U^j)
=
\operatorname{Tr}_{E_0/A_0}
\left(-U^j\,\delta P\,P_U^{-1}\right),
\qquad 0\le j\le7.
\tag{919c.2}
$$

右侧用原已成 $P_U^{-1}$ 和完整八维乘法迹计算。全部等式在整个 $A_0$ 中成立，证书的 all8_basis_identities_in_entire_A0_verified 为 true；没有只比较标量迹、约化点值或若干坐标。原 nilpotent multiplicities 保留，new_inverse_computed 为 false。由于 $1,U,\ldots,U^7$ 是完整自由基，这些实际等式与 R915 原证明认证整条泛函。

公式 (919c.1) 本身不需要新逆 $P_U$；本次 (919c.2) 复用旧逆是对原实际输入的完整恒等式验证。不能据此消除其他靶函数中的真实分母。

## 4. 全部 272 个原正常基微分像

将 R885 已成的全部原靶正常基函数 $\beta_i^{(t)}$ 代入上述行，实际计算了

$$
\operatorname{Tr}_{\pi_s}\bigl(\pi_t^*(\beta_i\,dz_t)\bigr)
=
\mathcal L(\beta_i^{(t)})\nu_s,
\qquad 0\le i<272.
\tag{919c.3}
$$

输出按连续的 17 个区间 $[0,16),[16,32),\ldots,[256,272)$ 保存；每块含全部 272 个源坐标。索引证书同时绑定 R885 的全部目标方程与原正常基行索引，所以这是完整 $272\times272$ 表的分块表示。

这里是原正向正常函数基，不是七个 R905 连接的 trace-dual 系数。R905 的有理系数还需在靶函数域代入，并验证其全部分母在整个 $E_0$ 上的实际单位条件。不能将 (919c.3) 当作七连接目标求值或 canonical Hecke 投影已成。

## 5. 特征零表达式与原刚性数据

新的表达式 DAG 保存原九个 unit-solve 列、原导子及 Euler 公式，准确引用原 R873 特征零 unit-solve 的 69078 字节文件，SHA256 为 d14c134fb887f36034f3805d13184c097162f3b37ca07f8174e47e1894a7c793。此次完成的是该原表达式在指定有限纤维的值；未展开特征零导数坐标、原 $\Gamma$ 的特征零数组，也未从一个模值推出全局系数重构。

原 Hecke 方向仍为

$$
\operatorname{Nm}_{\pi_t}(\pi_s^*I).
$$

原 dual7 对合同时运输分子、分母 determinant 帧，其平方通过原 level 群中的标量 $7I$ 恢复恒等。标量 7、diamond、原 $-3$ 下降及真 $c_Y$ 均保留，特别是 $z\mapsto z-2e_{73}/\tau$，不把 $z$ 改称 $\mathbb Q$ 固定。原 $P_0/P_1$ 刚性化、$\kappa_\nu$、$\nu$ 和两端常数没有被有限纤维迹行替换。

## 6. 实际输出绑定

以下均属于同一实际 run 与配置。长度为原文件字节数。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| p41-original-whole-Artin-Hecke-differential-trace-certificate.json | 17249 | c5b5a3a4f2a7b221d1b10bfbbc4a8f092690cbdeb30f83cc36135d23c91608ca |
| R919-nine-original-delta-P-coefficients.json.gz | 19655 | f3e9b88bb1110b6bc5f05b4004d985b9732e2e916acfcf3a8fb2394a6785883d |
| R919-complete-Euler-row.json.gz | 117875 | f9ba6aaace00dbd4f33ddde9517a982e817321be88eca49c6af917eb4d8ba6e0 |
| R919-complete-eight-basis-trace-identity.json.gz | 6613 | 7a9e90075eafc3993ba27d441fea42f39c919adf98156c6da3742f7df2a56f71 |
| R919-all272-target-normal-differential-traces.json.gz | 7251 | ee54c27e4580003ebd575b2a30e52058d56768dc95d4594cbe2ae3473a69e229 |
| R919-original-characteristic-zero-differential-expression-DAG.json.gz | 7521 | 9403c6523804f687a9e25d1105f54178abf7ac47f3214f3bdbbb17033d3b6cce |
| R919-source-audit.json.gz | 6436 | 9f96587c803c6b5491c042d741d5c2642c54c2ad6bb0d9b26995c19ad0728edd |
| R919-original-leaf-derivative-values.json.gz | 215433 | d61b4e079b55478291661b2ce6658e313ce56bdfe44dc31d5d220d48ce15bc73 |
| R919-basis-derivative-index.json.gz | 8217 | 9f09e49ced19a6db80903b81ee7a7ee6ea244eddc45ee902c91f0bbf72a978ae |
| full-outputs-manifest.json | 11229 | 3caecf7914afb5763ada21ae04300456bf99f483e3755e03cca6f3f956140ed3 |
| R919-retained-original-inputs.tar.gz | 14612930 | fb4af55fd04a6eef10029ef913953e07c3bd9d40c798a31c58774a7886620813 |
| R919-original-source-inventory.json | 32091 | 068b51a93b681a7f94de062d4f92648933da336a67ff313903a3cb120647e911 |

66 阶段 manifest 名为 R919-stage-manifest-96c84635095c15ff71b5ca521f458e7921b8b27feafbd6c8f794d422473e7f61.json.gz，9866 字节，SHA256 f7d9bf81c1e9d1bd3ac90573cab5290b6eeeb86f92d804f0942f7b3118915528。外层 manifest 有 77 个条目，ZIP 另含 manifest 本身和 reference。R919-current.json.gz 为 10227 字节，SHA256 fbb90154f27ef179cb4919059e2f72f0ff4d89f8dc69693d62ec7a28895676b8，不计入 66 个 complete 阶段。

一日原 artifact 的 ID 为 14245060474，名称 serre-global-R919-whole-Artin-Hecke-differential-trace-43904104159-1，ZIP 长度 19073395，SHA256 863b68d79df7398937d2e56832dc772ee29c4420999448c5e12a2bb57017fa82，到期时间 2026-11-17T16:09:19Z。

root 已通过纯 IO 读取完整小 ZIP，核其长度/摘要、manifest、全部 77 个原条目的长度/摘要，再读终证、九导数、完整迹行、八基等式、272 目标块索引及特征零 DAG。该过程未执行数学核心或重新做矩阵运算。后继从这个真实 artifact 或其受绑定的必要载体读取原件，不将原始数组写 Git。

## 7. 原输入与规则记录

实际输入只有 73 个必要原文件：R885 为 27、R827 为 26、R882 为 7、R873 为 6、R807 为 7。原 run 分别为 43848870181、43734420663、43839076365、43832703159、43707939269，完整 source commit、原 core/config/manifest/逐文件 pins 在 active request 和新 source inventory 中固定。

R827 整次历史任务在预算处退出，只有其早已 complete 的原 $\Gamma/W$ 阶段被消费，没有改写该历史 run 的结束状态。R807/R827 的数学 result 位于配置内，按真实 schema 读取，不制造新标签。全部原 $82$ 尺度只使用一次。

规则 job 133428211469 于 2026-11-16T16:08:17.517411+00:00 完成真实 git pull --rebase origin main，读过提交为 1e0ecf187b6e282226833c6c45c5e94661a0a9b1，两 README SHA 与现行规则相同。后续 R917 于 16:10:22.305718 UTC 真实 pull 读到 64228da6693769dcf70fb8bcaec4a72ad0faa445，两规则仍相同，root 已读回执并记 HANDOFF。

## 8. 保留的真实缺口

终证保持以下为 false：七连接分子目标求值、原 Hecke projector、端点标定、nonp/Poincaré/period/height、特征零导数坐标及原 $\Gamma$ 完整特征零展开。成功不改变这些边界。

下一消费者直接使用本次完整 Euler 行和原九导数；R905 七连接须保 trace-dual 的正确右伴随列和全部靶分母，再做整个 $E_0$ 的实际单位检查与求值。R917 两端正规阶与 R903/R907 目标线丛/范数按各自真实来源继续。绝对 Serre 一致性主目标未完成。

