# R142 补篇：保原 GM 中点的真子域半径缩放与单调协方差上界

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

**已证明并给出纯 adapter；未启动新的科学。** 本篇保留原 exact GM midpoint $M$ 和原误差 diagonal $D$，只对完整真子域的 radius 费用作一个可验证的 scalar 缩放。所得准确 PSD majorant 不大于同一个原 GM 母格 majorant。这个数学单调性不等于最终 interval scalar 一定更小，不是速度承诺，也不是已付的逆门。

配套：[fourfold_codazzi_low_centre_child_fixed_midpoint_moment_provider.py](../scripts/fourfold_codazzi_low_centre_child_fixed_midpoint_moment_provider.py)。它是独立纯模块，不修改当前 R142，也不替换已登记的 [全 source 对角方案](R142-supplement-genuine-child-diagonal-covariance-and-parent-moment-reuse.md)。

## CM1. 同一 whole-parent source 的原 exact midpoint

保持原 [R142](R142-low193-parent-moment-continuation.md) 的比较模型、actual $S$、exact dyadic 内部 balance、全部参数、五 source roles、原193输出坐标和全部独立输入列。在一个母格和一个 varying role 上，令 $\mathbb U$ 是原 whole-parent balanced source matrix ball。

严格采用 [GM 纯模块](../scripts/fourfold_codazzi_low_centre_exact_cell_moments.py) 中 whole_source_covariance_majorant 的定义：

$$
 M_{ij}=\operatorname{mid}(\mathbb U_{ij}),\qquad
 R_{ij}=\operatorname{mag}(\mathbb U_{ij}-M_{ij}),\qquad
 A_{ij}=|M_{ij}|.
 \tag{CM.1}
$$

$M$ 是该原区间球的准确点中点，不是从实际场取一个采样值，也没有把实际径向系数改成常数。$R,A$ 为原 directed magnitude 的固定非负 upper points。于是整个母格、原 full family 都有 $U=M+E$、$|E|\le R$。

原 GM 定义

$$
 F(R)=AR^{\mathsf T}+RA^{\mathsf T}+RR^{\mathsf T},\qquad
 d_i\ge(F(R){\bf1})_i,\qquad
 D=\operatorname{diag}(d_i),\quad C=MM^{\mathsf T}.
 \tag{CM.2}
$$

本篇的 $d_i$ 不是重新选一个更方便的 diagonal，而是原 GM 的确切 directed row upper。配套函数逐项复制原 operation order：cross=$AR^{\mathsf T}$；covariance_error=cross+cross$^{\mathsf T}$+$RR^{\mathsf T}$；随后逐 entry 取 upper，逐行求和再取 upper。midpoint covariance 同样调用原 constant_source_covariance。没有从两个 interval diagonal 的差反推 $d_i$。

因此比较对象始终是同一个 $M,R,D$ 的准确 $C+D$。一个以后运行若有不同的 arithmetic、whole-parent ball 或 midpoint，必须明确采用那一次对应的 GM split；不能据本篇声称它自动逐字等于一个未保存的旧私有 split。本篇没有把缺失的私有数组改称已恢复。

## CM2. 真子域只收缩相对于固定 M 的半径

[CC](R141-supplement-genuine-child-coefficients-and-unchanged-hybrid-sources.md) 的完整 true-child source ball 给每个 entry 的另一条合法 radius。以同一个 $M$ 定义

$$
 R^{c}_{ij}=
 \min\left\{R_{ij},
   \operatorname{mag}(\mathbb U^c_{ij}-M_{ij})\right\}.
 \tag{CM.3}
$$

两者都是相同 $|U_{ij}-M_{ij}|$ 的有效上界，所以对整个声明 child 和原参数全族，

$$
 |U_{ij}-M_{ij}|\le R^c_{ij}\le R_{ij}.
 \tag{CM.4}
$$

这里没有把 $M$ 换成 child midpoint；也没有对两个 PSD 矩阵取 entrywise minimum。要相交的是同一 source entry 的 scalar radius。完整 source 的193列或128列都保留，不能只对某个已知 RHS 的一列计算。

## CM3. 误差 diagonal 的准确支撑，不能删 constant 行

设 $J=\{i:d_i>0\}$。若 $d_i=0$，(CM.2) 的非负性给

$$
 0=(F(R){\bf1})_i
 =\sum_j\left(A_{ij}\sum_kR_{kj}
             +R_{ij}\sum_kA_{kj}
             +R_{ij}\sum_kR_{kj}\right).
 \tag{CM.5}
$$

最后一项大于等于 $\sum_jR_{ij}^2$，所以整条 radius row $R_{ij}=0$。第一项又给：对每个 $j$，要么 $A_{ij}=0$，要么整列 radius 为零。于是该 error covariance 的整行、整列均准确为零；同结论由 $R^c\le R$ 传给 child。

**这不说明 $M$ 的第 $i$ 行为零。** 该原 physical 坐标可能有非零常值 source，必须完整留在 $C$ 和它的准确矩中。这与前一篇对整个 source 作 diagonal 时的零支撑含义不同。

如果 $J$ 为空，则 $R=0$，实际 $U=M$ 准确恒定；只省掉 error moments，不能把整个 source 置零。如果 $M=0$ 则只省掉 center moments。两者皆零才是完整零源。配套代码仍保193行、所有原输入列、mean 和端点格式，没有通过支撑判断删 physical 坐标。

## CM4. 一个 σ 同时控制完整 covariance error

令

$$
 q_i^c=(F(R^c){\bf1})_i,\qquad
 \sigma_{\rm exact}=
 \begin{cases}
  \max_{i\in J}q_i^c/d_i,&J\ne\varnothing,\\
  0,&J=\varnothing .
 \end{cases}
 \tag{CM.6}
$$

因 $F$ 对非负 $R$ 逐 entry 单调，$0\le\sigma_{\rm exact}\le1$。对任意真实 $x$，准确分解 $U=M+E$ 给

$$
 UU^{\mathsf T}-C
 =ME^{\mathsf T}+EM^{\mathsf T}+EE^{\mathsf T}.
$$

此对称差的 entrywise absolute value 被 $F(R^c)$ 包围，故

$$
 \begin{aligned}
 x^{\mathsf T}(UU^{\mathsf T}-C)x
 &\le |x|^{\mathsf T}F(R^c)|x|\\
 &\le\sum_iq_i^c x_i^2
 \le\sigma_{\rm exact}x^{\mathsf T}Dx .
 \end{aligned}
$$

中间不等式是非负对称矩阵的 row-sum diagonal 恒等式，亦见 CD3。于是完整结论为

$$
 \boxed{\quad
 U(t,\delta)U(t,\delta)^{\mathsf T}
 \preceq C+\sigma D
 \preceq C+D
 \quad(\hbox{整个 child 和原 full family}).\quad}
 \tag{CM.7}
$$

计算 $q_i^c$ 不必形成三个193方阵。记 $c_{A,j}=\sum_iA_{ij}$、$c_{R^c,j}=\sum_iR^c_{ij}$，则

$$
 q_i^c=\sum_j\left(
 A_{ij}c_{R^c,j}+R^c_{ij}c_{A,j}+R^c_{ij}c_{R^c,j}\right).
 \tag{CM.8}
$$

$c_A$ 只在母格准备一次，child 运算为两次完整行/列求和，成本为行数乘原列数。

代码向上包围每个 $q_i^c/d_i$ 再取最大，得 $\widehat\sigma$，实际取 $\sigma=\min(1,\widehat\sigma)$。此 cap 合法，因为 $C+D$ 和 $C+\widehat\sigma D$ 各自已经包住同一个真实 covariance，且两者只沿同一个 PSD $D$ 的 scalar 方向变化。零 $d_i$ 必须核其 child error row 确为零，然后略过除法，不执行0/0。

## CM5. 两份母格准确矩，child 保完整 signed 两三角

对同一 GM 的 $H,Q$ template，source moments $Z(V),Y(V)$ 都对 covariance $V$ 准确线性；observation moment $U_{\rm obs}$ 不依赖 source。每个 varying role 的每母格至多准备两份：

$$
 (Z_C,Y_C)=\operatorname{moments}(C),\qquad
 (Z_D,Y_D)=\operatorname{moments}(D).
$$

child 使用

$$
 Z_c=Z_C+\sigma Z_D,\qquad
 Y_c=Y_C+\sigma Y_D,\qquad
 U_{{\rm obs},c}=U_{\rm obs}.
 \tag{CM.9}
$$

代码对相应完整矩阵球作 directed addition/scale，因此包含准确 (CM.9)。这不是声称两次浮点例程逐字线性。

原 packet 仍用各 child 独立 certified node frame、真实 $h,h^2$、全部 source columns、原 $I_L,I_R,O_L,O_R$，以及完整 signed 两三角。不能只缩一个最后的 scalar，也不能对 $Y$ 或其中负的 signed cross term 作 entrywise 单调比较。

ordinary_raw_low_source 和 transformed_low_source 两个真正 constant roles 直接沿用原 ParentMomentProvider。其余三 varying roles 各有独立 $M,R,D,\sigma$；真 child cache 绑定完整 box 和 template token，不能把一个 child 的半径给 sibling。统计与缓存只留当前母格三 source plans 和当前 child 三组合矩，不存全部旧 boxes。

## CM6. 准确 PSD 单调性与 interval 结果是两个陈述

固定同一个比较 Green 和同一真实 source单位，任一 output/source 完整 Gram 的准确被积函数对 covariance 是正线性映射。因此 (CM.7) 保证：以当前 child 的 $C+\sigma D$ 代入后，准确 covariance-based 全 body/atoms 费用不大于以同母格 $C+D$ 代入的费用。相同真实 lengths、全部 source columns 和全部 triangles 均在这个比较内。

然而实现给的是矩阵球和最终 scalar upper。分别准备两份 moments、线性组合，以及 signed triangle formula 会产生不同的区间相关性和舍入宽度；Gershgorin 的数值外包也不是一个随任意 Loewner 比较自动单调的函数。因此本篇**不承诺最终已保存的 HS上界、$\varepsilon$、point bound 或任何严格门必改善**。特别不能据 (CM.7) 直接改写原 R142 实际记录。

与前一篇全 source 的 $\sigma D$ 不同，本篇确实保留 $MM^{\mathsf T}$ 的原 signed 列结构，并证明对同一 GM exact majorant 的不扩大；两种 pure provider 是不同可用输入，不能把它们的数值成果混成同一个完成目标。

## CM7. 实施范围和静态工作量

配套 pure factory 显式接收原 ParentMomentProvider、GM module、same model 和 WholeChildSignedCoefficientProvider，不 monkeypatch 原定义。它复制原 GM split 的确切操作，随后只新增 child radius 和上述线性 moments。没有 import-time work、数值库导入、IO 或 public entry point。

按现155母格/1424细格，一个 varying role 的 dense source moment calls 至多310次，少于逐 child1424次；若 center 或 error 准确为零还可省去相应调用。这是代码结构的计数，不是 wall-time 实测，也不豁免原 coefficient、frame、Green products 和全 point boxes。原母格 template 与共享 output covariances仍各自付费。

它同样不改比较生成元 $H_{\rm parent}/n$。固定 midpoint comparison 与真实径向系数的确定性差不会因为 radius 更细而消失；若该误差主导，须换真正新比较模型并认证其 BVP，不能把旧 Green 身份据为新模型证据。

本篇保持 R142 正在运行；是否实际使用由其完整结果及之后的必要目标决定。本篇自身不宣称任何 source、逆、物理58门、原端口或非线性目标数值完成。
