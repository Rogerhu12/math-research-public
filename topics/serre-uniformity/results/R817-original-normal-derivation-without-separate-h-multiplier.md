# R817：由两个列条件和嵌套交换子认证原正规导子

日期：2026-11-15。状态：**已证明的准确认证准则；尚无新的矩阵计算结果。**
本篇把 R815 的实际重构目标从三个算子缩为 $M_g,\Gamma$ 两个，
省去没有独立下游需求的 $M_h$ 重构。
它不撤回 [R813](R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md)
在已知 $M_h$ 时的六点非齐次认证；本篇的新终验需要七点。

## 1. 固定原函数、基与实际输入

沿 [R805 原正规基](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)、
[R806 实际乘法](R806-certified-original-primitive-multiplication.md)和 R813，令
$$
 \mathcal R_\tau=\bigoplus_{a=0}^{271}\mathbf Q[z]\beta_a,\qquad
 \beta_0=1,\quad \epsilon=(0,1^{144},2^{127}),
$$
$$
 W=M_w,\qquad z=\sigma/\tau,\quad w=w_0/\tau,\quad
 \delta=\tau^{-1}D_0,\quad g=\delta z,\quad h=\delta w.
 \tag{817.1}
$$
所有矩阵采用输出行、输入列约定。
$W$ 是原函数域的 primitive 乘法矩阵，
$$
 \deg W_{ba}\le1+\epsilon_a-\epsilon_b.
 \tag{817.2}
$$
原 R806 的非零循环行列式已经保证 $e_0,We_0,\ldots,W^{271}e_0$
在 $\mathbf Q(z)$ 上为一组基。

R813 的两个原 S3 右端分别给 $v_g,v_h$，保留原 column denominator
和 original target rational scale。此处要求其真实源认证已经完成；
只知道 Wronskian 理论公式不能代替实际输入。

先准确恢复 $M=M_g$：
$$
 Me_0=v_g,\qquad [M,W]=0,\qquad
 \deg M_{ba}\le3+\epsilon_a-\epsilon_b.
 \tag{817.3}
$$
R813/R809 的原 cyclic 唯一性和七个固定准确点已给该步骤的充分证书。
本篇以下把这个经过准确认证的同一个 $M$ 作为输入。

原导子在正规基上的真实矩阵 $\Gamma^\delta$ 存在，并满足
$$
 \deg\Gamma^\delta_{ba}\le2+\epsilon_a-\epsilon_b,\quad
 \Gamma^\delta e_0=0,\quad
 [\Gamma^\delta,W]=M_h-MW'.
 \tag{817.4}
$$
这里 $M_h$ 仅作为理论上的真实乘法算子出现；无需先计算其全表。

## 2. 有界 commutant 的唯一性

若矩阵 $T\in\operatorname{Mat}_{272}(\mathbf Q(z))$ 与 $W$ 交换，
则 $Te_0$ 唯一决定 $T$。确实
$$
 T W^j e_0=W^j T e_0\qquad(0\le j\le271),
$$
而这些输入列是一组基。
特别地，若 $Te_0=v_h$，则 $T=M_h$，因为原乘法 $M_h$
也交换 $W$ 且有同一个首列。

此论证在 $K(z)$ 和 $L(z)$ 的原基变换后仍成立：
原非零循环行列式不会因扩标量变为零。
它不要求幂环 $\mathbf Q[z,w]$ 整闭，也不更换正规基。

## 3. 不独立重构 Mh 的准确准则

对待认证矩阵 $G\in\operatorname{Mat}_{272}(\mathbf Q[z])$，
只作一个符号定义
$$
 T_G=[G,W]+MW'.
 \tag{817.5}
$$
实际终验可以逐点构造 $T_G(t)$，不必把这个多项式矩阵完整物化或另行 CRT。

**定理817.1。** 假设 $G$ 满足：

$$
 \deg G_{ba}\le2+\epsilon_a-\epsilon_b,\qquad
 Ge_0=0,\qquad T_Ge_0=v_h,\qquad [T_G,W]=0.
 \tag{817.6}
$$
则 $T_G=M_h$ 且 $G=\Gamma^\delta$。

**证明。**
第二节先由 $T_G$ 的交换子和首列得到 $T_G=M_h$。
所以(817.5)给
$$
 [G,W]=M_h-MW',
$$
与(817.4)相同。两式相减得到
$[G-\Gamma^\delta,W]=0$，并且
$(G-\Gamma^\delta)e_0=0$。
再用同一个循环基，得到 $G=\Gamma^\delta$。证毕。

这里 $T_G$ 并未被假定为乘法矩阵；
它的完整交换子与真实首列证明它就是 $M_h$。
也没有由 $Ge_0=0$ 误判整个 $G$ 为零。

## 4. 两个列条件与本次实际 e2 的简化

记 $v_w=We_0$。在 $Ge_0=0$ 后，
$$
 T_Ge_0=Gv_w+Mv_w'.
 \tag{817.7}
$$
这是可逐多项式系数核对的向量恒等式。

本次 R806 实际给 $w_0=e_2$，而 R805 的第一个正次正规基元是
$\beta_1=e_2/\tau=w$。因此
$$
 We_0=e_1,\qquad W'e_0=0.
 \tag{817.8}
$$
这里右侧 $e_1$ 是正规坐标单位列，不是原 M2 截面的 $e_1$。
消费者必须先根据实际 R805/R806 来源，准确断言 $W$ 的首列
就是这个常数单位列，再使用简化。

于是(817.6)的两个列条件准确变为
$$
 \boxed{Ge_0=0,\qquad Ge_1=v_h.}
 \tag{817.9}
$$
首列为零、第二列为原 $h$ 向量都必须逐系数验证。
$v_h$ 的原 $1/82$、整尺度、content 和 column scale 沿 R813 保持，
没有改成一个比例相同的向量。
若未来实际 primitive 源不同，则回到(817.7)，不能照抄(817.9)。

## 5. 为什么仍可用有限个准确点

由(817.2)、(817.3)和 $G$ 的带权界，
$$
 \deg(T_G)_{ba}\le3+\epsilon_a-\epsilon_b.
 \tag{817.10}
$$
这里
$\deg(W')_{ba}\le\epsilon_a-\epsilon_b$；
若该界为负，相应导数条目就是零。
矩阵乘积的中间 $\epsilon$ 准确抵消，所以
$$
 \deg[T_G,W]_{ba}\le4+\epsilon_a-\epsilon_b\le6.
 \tag{817.11}
$$
故在固定的七个互异整数
$$
 t=0,1,2,3,4,5,6
 \tag{817.12}
$$
处，逐 $272\times272$ 矩阵、逐行块在特征零准确验
$[T_G(t),W(t)]=0$，便证明整个多项式交换子为零。
这些点不要求循环、无分歧或矩阵可逆；
它们是准确恒等式证书，不是概率筛。

**七点不能减成 R813 的六点。**
已知独立 $M_h$ 时，原非齐次残差的最大次数是5。
省去独立 $M_h$ 后，本篇检查的是再与 $W$ 作交换子的残差，
最大次数升为6，因此需要7点。
模恢复 $G$ 仍只需其本身次数界给出的5个好点。

若写
$$
 G=A/a,\qquad W=B/b,\qquad M=C/c
$$
且 $a,b,c$ 是准确的正整数公共分母，令
$D=\operatorname{lcm}(ab,cb)$。在每个点形成
$$
 T_{\rm num}
 =\frac D{ab}(AB-BA)+\frac D{cb}CB',
 \tag{817.13}
$$
则只须准确核
$$
 T_{\rm num}B-BT_{\rm num}=0.
 \tag{817.14}
$$
乘法次序始终是 $CB'$，即 $MW'$，不能换成 $W'M$。
分母只是非零整数，清分母不损失特征零等价性。
可逐点保存小证书和源矩阵 SHA，而不另存 $T_G$ 的全系数。

## 6. 模 Krylov 恢复本来也不需要 Mh

在一个实际好点记
$$
 k_0=e_0,\quad d_0=0,\quad
 k_{j+1}=Wk_j,\quad d_{j+1}=W'k_j+Wd_j.
$$
这里 $d_j=(W(z)^je_0)'(t)$。原微分规则给
$$
 G(t)k_j=jW(t)^{j-1}v_h(t)-M(t)d_j
 \quad(0\le j\le271);
 \tag{817.15}
$$
$j=0$ 的右端为零。
全部右端只使用实际 $M_g$、$v_h$、$W,W'$。
把这些列右乘已保存的有限域 Krylov 逆，就得到 $G(t)$ 的模像；
从始至终没有需要 $M_h$ 的原坐标矩阵。

五个好点插值后仍核每一个带权支撑零、首列和第二列，
再作源绑定的 CRT 与严格有理重构。
最终只有(817.9)、(817.11)--(817.14)的全部准确检查通过，
才能宣告原 $\Gamma$ 已完成。模像通过不代替这一步。

## 7. 真正下游及执行改动

[R814](R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md)
的零理想与降重数只需要 $\Gamma,M_g$：
$$
 \mathcal C=\operatorname{im}[\Gamma,M_g],\qquad
 N(I)=\operatorname{im}[H_I,\Gamma H_I+M_gH_I'].
$$
原函数的导数坐标同样是
$\Gamma v_f+M_gv_f'$。
因此这两个算子已经满足当前实际消费者；不为没有消费者的全表作独立重构。
若以后确实需要 $M_h$ 的全系数，可由(817.5)准确导出并单独认证来源；
本次不把该可导出性写成“已计算并保存 Mh”。

R815 的新范围应明确标成：

- 实际重构目标只有 $M_g,\Gamma$；
- $M_g$：6个模好点、7个固定准确终验点；
- $\Gamma$：5个模好点、7个固定准确嵌套交换子终验点；
- 原 $v_h$ 始终是必要输入，不能因为省去 $M_h$ 而省掉第二个 Wronskian；
- $M_h$ 不作独立 CRT，也不默认物化其全系数；
- 两图仍用 R814 的正则 $\delta_\sigma=t\delta_\tau$，保原负号和连接修正；
- 极理想、$\eta$ 和高度仍在后继，不由本篇预填。

由原带权存储界，$M_g$ 有295936个有理系数位置，$\Gamma$ 有221952个，
合计517888；独立 $M_h$ 的295936个位置被省去。
这些是有界存储位置数，不是实际非零系数统计，
也不是对实际 CRT 次数、用时或成功运行的预言。

本篇只有纸面证明。所有新算术仍只在本公开仓库 Actions；
完成阶段不重算，raw/证书仅作必要的一日活跃传输，
仓库保脚本、参数、source/run/SHA及真实结论。
