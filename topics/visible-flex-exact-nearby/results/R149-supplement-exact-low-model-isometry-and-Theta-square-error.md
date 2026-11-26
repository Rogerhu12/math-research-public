# R149 TQL：原 low96 model 等距与真正 Θ 方阵误差

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**新增完整限制公式。** [TQ](R149-supplement-original-Theta-restriction-and-joint-Schur-row-consumer.md)
的第一张 signed 方阵 $T=\Theta E_{96}^a$ 可以直接使用 OT 的完整
$V_Q$ 联合 $L^2$ 误差，因为原 low96 model reference 是精确等距。
无需为这个有限输入再支付 high model 的 $K_G=512$ one-loss。
完整 phase 和96×96 formal coefficient 的 joint rounding 仍须另外支付。

本条没有重算旧范数，没有把 OT 的全频误差变小，也没有声称任何门已过。
它给下一消费者一个不同而完整的候选，必须与 TQ 原 global 候选一起
保存后再选择整个 upper。

## TQL1. 精确 low model 的完整 source/target 单位

采用 [WFI](R133-supplement-graph-domains-and-finite-index-ledger-for-the-reflected-waist-row.md)
和 [TM.2–5](R149-supplement-original-model-adjoint-on-complete-finite-Theta-rows.md)
的原归一实基

\[
v_n^a(x)=\sqrt2\cos(4nx-2na),\qquad
u_n^b(x)=\sqrt2\cos(4nx-2nb-\pi/4),\qquad b=a+\Omega.
\tag{TQL.1}
\]

两边各自在原 normalized $L^2(dx/(\pi/2))$ 中正交归一。
原 $\overline M$ 的 low96 reference 被定义为
$\overline M u_n^b=v_n^a$，$1\le n\le96$，不是一个没有证明的
physical inverse。因而若 $E_{96}^b$ 插入这些 source modes，

\[
S_0:=\overline GE_{96}^a=E_{96}^b,
\qquad \|S_0:\ell^2_{96}\to X_b^0\|=1.
\tag{TQL.2}
\]

真正 source phase $b$ 仍完整保留；等距只来自同一 phase 的正交实基，
不要求 $a=b=0$。这个陈述不涉及 $n\ge97$ 的 Cayley denominator，
故该段的 norm512不进入 (TQL.2)。

## TQL2. 先限制输入，再用整个 VQ 误差

令 $\widehat V$ 为 DT/OT 原 exact finite row operator：从原 IR
exact dyadic $z_j^a$ 和完整 AS exact dyadic $\widehat\alpha$ 形成
$\mathcal A_{\widehat\alpha}^*Gz_j^a$，按原同号投影次序保留全部模式。
它不是 formal interval midpoint 替代的另一个 operator。

[TP.10](R149-supplement-complete-alpha-error-products-for-original-Theta-rows.md)
与 OT 第7条完整输出给

\[
\|V_Q-\widehat V\|_{X_b^0\to\ell^2_{96}}\le e_V.
\tag{TQL.3}
\]

这个 $e_V$ 已经付全部 IR 高/低、无限 residual/model 误差、完整
same-sign $\alpha$ product、两种 norm 候选和原 source factors；
并非96个单行误差的未认证集合。新的限制不会丢失其中任何 tail。

定义真实矩阵与有限参考矩阵

\[
T=V_QS_0=\Theta E_{96}^a,\qquad T^f=\widehat V S_0.
\tag{TQL.4}
\]

由 (TQL.2–3)，

\[
\|T-T^f\|_2\le e_V.
\tag{TQL.5}
\]

这没有乘512，也没有按96行另乘 $\sqrt{96}$。输出仍为原 source/root
96坐标，输入为原 true target low96坐标；两项 physical mean 和真
$\nu$/phase 不是此方阵的输入。

## TQL3. 原完整 model balls 给新的 whole low square 费用

OT 的整张 `private_model_rows_receipt` 包围所有96×2240 entries。
对 $1\le j,n\le96$，其 formal ball $\mathbb T_{jn}$ 包围 (TQL.4)
的真正 $T^f_{jn}$：这正是原 TM.6 在 low $\gamma_n=1$ 时的

\[
T^f_{jn}=\sqrt2\operatorname{Re}
       \left(p_{jn}e^{i(2nb+\pi/4)}\right).
\tag{TQL.6}
\]

$p_{jn}$ 是同一个有限 $\widehat V$ row coefficient。原 whole $b$ ball
和所有 DT/model directed evaluation 都留在 $\mathbb T_{jn}$。
未使用只显示的 phase 中心，也未由 signed $\mu$ 改写这个 low reference。

令 $\widehat T_{jn}$ 为 OT **原整个**96×2240 exact dyadic trial 的
相应前块。形成新的完整 finite-square bound

\[
r_{jn}\ge\sup_{t\in\mathbb T_{jn}}|t-\widehat T_{jn}|,
\qquad
e_{\rm low,model}
 =\operatorname{up}\sqrt{\sum_{j=1}^{96}\sum_{n=1}^{96}r_{jn}^2}.
\tag{TQL.7}
\]

全部9216个 signed balls 与原 dyadics 都参与。由完整 Frobenius
bound，$\|T^f-\widehat T\|_2\le e_{\rm low,model}$。因此

\[
\boxed{\quad
\|T-\widehat T\|_2
 \le \xi_{\rm low}:=e_V+e_{\rm low,model}.
\quad}
\tag{TQL.8}
\]

新的 (TQL.7) 是这个完整96×96 restriction 的目标。原 OT 完整
96×2240 rounding norm 不重跑、不修改；其整张载体和原 SHA 仍全部
恢复并验证，不能仅核前块或换一组新的 finite rows。

TQ.5 的 $\xi_{\rm global}=e_\Theta$ 同样包围这个**同一**
$T-\widehat T$。实际 owner 先完整保存读回
$e_{\rm low,model}$、$\xi_{\rm low}$ 以及 verbatim copied
$\xi_{\rm global}$ 的来源，再选择

\[
\xi=\min\{\xi_{\rm global},\xi_{\rm low}\}
\tag{TQL.9}
\]

的整个 saved upper。将它代入 TQ.6 的 $r_0+b\xi$ 是合法新门；
不选择不同分解的局部项，也不从某个旧 norm upper 中扣减费用。

## TQL4. 完整消费者合同

纯模块是
[fourfold_codazzi_low_model_Theta_square_error.py](../scripts/fourfold_codazzi_low_model_Theta_square_error.py)。
其输入必须含 OT 的完整10记录、原 whole model-ball carrier 和原 whole
dyadic carrier。metadata/whole SHA/phase/mean/source qualification 由
同一个 public owner 在科学前完成，不用一份新的旧 norm 计算代替。

新自然目标仅是 (TQL.7–8) 及同一 TQ signed square 的完整 gate。若
选择 global 候选，旧 $e_\Theta$ 作为完整 copied record 使用；它不再
计作一个新科学结果。所有后继仍保持 TQ 对 full physical Schur、真实
high residual、target $\mathcal B^{-1}$、两 mean 和真参数列的原义务。
