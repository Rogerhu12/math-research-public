# R170 实际新域的完整 R173 区间接入

## 实际输入与接口

本条将 [R173](../results/R173-complete-current-field-intervals-and-zero-end-posterior-interface.md) 的完整准确字段和零端 primitive 接到 R170 扩大尾域，使用真实 dyadic30 已接受 archive，SHA256 为 3bceef937899fad65e512e56d3bd747a6d225b20301b64ed9d04582a4f6db981。保存 mesh 为 131 节点；参数明确分为中央 [0,31)、固定尾 [31,47)、物理 profile [47,54)。所有原始系数和窗口都原样读取。

新源是 [fd2d_gc_dyadic_tail_complete_arb.py](../scripts/fd2d_gc_dyadic_tail_complete_arb.py)，SHA256 为 fa39d247e561812a50dba36a91b9754cbb32ce27549ad78336e7e5b151fd667b。三个明确构造器分别是：

- DyadicTailIntervalPieces：读取实际 R170 archive 的完整 raw P1/Fourier、标量权和 bumps；
- DyadicTailCompleteInteriorArb：完整准确 atlas、affine、R153/R155 以及三条 Gauss–Codazzi 缺陷；
- DyadicTailAccurateDomainFieldArb：加入准确 R172 末格，并继承真物理长度的零端 primitive 接口。

完整新层直接消费 geometry 已闭存的 [native30 definition](2026-11-12-fd2d-dyadic-tail-accurate-last-cell-30-01-native-definition.json)，以及 [准确新 profile packet](2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-packet.json.gz)。它没有从旧 positive-control reader 修改数组、补零或跳过 guard；旧构造器完全不调用。继承方法所属五个冻结源均逐项核 SHA。

## 为什么继承的完整公式仍然适用

R170 的实际 $P$ 是同一个 degree-15 Bernstein 多项式，改变的是允许的系数域。本次全局 Bernstein 系数中有 6 个负项，索引 1、3、6、9、11、13，因此旧全局系数盒明确不通过。但将同一多项式准确细分为 8 段后，128 个局部系数全部在 $[0,6/5]$ 中。准确有理证书由对应 archive reader 重新核对，且必须与保存的 domain definition/certificate 一致；只看 tail_kind 中的 basis 名称不构成域身份。

R173 的尾曲率公式

$$
 \kappa(y)=\frac{630}{23/50}q^4(1-q)^4P(q),
 \qquad q=\frac{|y|-17/50}{23/50},
$$

在 $17/50<|y|<4/5$ 上成立，在补集为零。有限多项式的 de Casteljau、全部导数和区间乘法并不要求全局控制系数非负。R170 证明准确函数 $P\ge0$，从而保留准确 PSD cut 和原几何条件；本条的局部区间算术仍保留所有原控制系数，并没有把负系数删去或截到零。

同样，raw P1/Fourier、完整 seed/reference/tail affine、R153 商式和 R155 正 trace 公式不依赖旧全局系数盒。条件分母的处理完全保留：若请求盒不能证明活动 $n>0$，或不能证明平方根所需正性，返回未决；有限 solver floor 不进入连续证明。

因此本条只需重新证明定义身份与接口接合：严格 R170 decoder 给实际所有数组及证书；准确 profile packet 必须绑定同一 archive SHA 和同一七个 $\delta$；准确完整 atlas 仍由保存 inlet/seed 定义；其余每个被继承公式的数学假设由这些明确输入或逐盒正性支付。R173 的包含性证明随后逐步原样适用。

## 准确物理域和 cut

物理目标是重绑定后的准确 R171 $a_\delta(s)$，不是旧27的参数。R175 只改变同一 bump 多项式的包围后端，不能改变 target binding。

保存的 binary64 cut 标签仍记作 $E$，准确相位积分端点为 $S$。完整层沿原 R173 约定，在最后 P1 格使用 geometry 的 DyadicTailAccurateLastCell：

$$
 \sigma(s)=b+(E-b)\frac{s-b}{S-b},\qquad
 C(\sigma(s))+\eta(\sigma(s))T(a_\delta(s),u),
$$

然后用准确 $K(s)$ 作 R155。尾半径、固定弧半径与宽度是准确 $4/5,17/50,23/50$。不把 $a(s)$ 换成 $a(\sigma)$，不把保存 float $E$ 默认提升为 $S$。

准确 cut 查询只返回真实值与角一、二 jet；径向 II jet 和完整 forcing 保持未赋值。继承的 R174 一侧可积估计是另一明确消费项，本次没有把 bypass 解释成 $E_s=0$。

## primitive 与物理角

零端 primitive 继续以实际 cell 的准确长度 $L$ 定义：

$$
 q=L\int_0^t(P-\bar P)\,dt,\qquad
 q(0)=q(1)=0,\qquad q_s=P-\bar P.
$$

最后一格的长度是 $S-b$，而非其浮点中点。实际 forcing $H=(-aR_n,aR_m,-aG)$ 由完整字段给出。预算中的

$$
 E=\bar P+(H-P)+\frac{U_s}{U_\xi}q_\xi+q\times\alpha
$$

保留完整移动材料图的项以及 Gauss 第三分量。任何拟合样本只定义有限准确有理多项式 $P$；误差由后来真正的区间 $H-P$ 支付。

## 已完成的一次必要小核

[check source](../scripts/fd2d-metric-dyadic-tail-complete-arb-check.py) 的真实进程 session 37799，首块 7c42fa、末块 d35444，exit 0。耗时 1.1578619509964483 秒，峰 RSS 96020 KiB。[完整 report](2026-11-12-fd2d-metric-dyadic30-complete-arb-01-report.json) 和 [准确 definition](2026-11-12-fd2d-metric-dyadic30-complete-arb-01-definition.json.gz) 已闭存。

这一次只消费三个小正宽盒，覆盖 coast、coast 出口附近和 terminal 窗；每盒求完整五 jet、三条微分缺陷及真实 $U_s/U_\xi$。与正确 R170 binary native 在同一点的求值差上界，绝对最大为 $1.282\times10^{-11}$，按 $1+|\text{numeric value}|$ 归一的最大为 $1.601\times10^{-13}$。这些差是准确函数与近似程序的实际对照，不是用点值替代区间包含性。

还在 cell 69 消费一个实际完整 forcing secant 的精确零端 primitive；两端 $q,q_\xi$ 均准确为零，完整小盒给出 $E$ 范数上界 0.36276229215884087。这个数并不满足全域小误差目标；它只证明实际接口保留了 known/unknown、角漂移和三分量的全部项。没有宣称整格或全域 forcing 已闭，也没有运行新的 BVP、F/J 或 body。

新完整 binding 为 c6194df9c29463973465784e4657672a706330bad3cb99eb7255196fe09cb791；准确 profile target binding 为 5994cdb58d4d09a98e01dbd313b34480ed2eb89ced9a293c7d593d45ed276f7b。

## 可复现命令

从本课题目录运行，输出 stem 需为未存在的新名字：

~~~sh
PYTHONPATH=/workspace/scratch/fd2d-recovered-deps/python-flint-0.9.0 \
python scripts/fd2d-metric-dyadic-tail-complete-arb-check.py \
  --native-definition notes/2026-11-12-fd2d-dyadic-tail-accurate-last-cell-30-01-native-definition.json \
  --profile-packet notes/2026-11-12-fd2d-metric-dyadic30-accurate-profile-rebind-02-packet.json.gz \
  --out-prefix notes/2026-11-12-fd2d-metric-dyadic30-complete-arb-replay
~~~

后续实际 posterior 仍需全域未知分母正性、forcing/primitive 余项覆盖和累计、准确初值项、真正重建的接口及几何界。本条补齐新 R170 域的可重建连续消费者，没有把尚未完成的实际场变成解。
