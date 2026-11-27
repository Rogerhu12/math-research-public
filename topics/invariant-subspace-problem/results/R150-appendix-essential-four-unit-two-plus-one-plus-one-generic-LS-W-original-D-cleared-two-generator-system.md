# R150：W 整余图的原 D 清分母与十条两列方程

**状态：已证明并实际完整返回。** 在原 Delta=0、W=0 的当前整余图上，利用原物理单位 D，把值中心 s 从完整十行中唯一恢复。只剩同一个 Y 的首一二次式与十条一次式，并且全部原非零条件在同一点返回。本结论没有倒置 D 的范数，也不声称 W 已排空。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 已付图与完整原四列输入

完整原四列输入见[十条原值四生成表示](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-native-full-value-four-generator-system.md)。

沿用同点坐标

$$u=e+1,\quad Q=ek,\quad V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV},\quad
Y=y-1,\quad w=(x-x_*)/Y,\quad x_*=1+u-u/\ell.$$

原两均值已经准确恢复同一点 x,y,t；原 E0、N0、P1 给同一点 lambda、T、f。既有全图原组合给

$$q_Y=Y^2+\alpha Y+\gamma.$$

令 m=u-ell，M=4bc(1-Q)。ell、m、M 及前面坐标所用权分母均有既有完整支付；Y=0 整支也已完整排除。旧 D27、B239、J19 零纤维仍全部保留。

记 A0 为 QQ[e,k,w] 按这些已付权因子局部化的环。原物理值的第二矩给

$$\ell E_2=Ms^2-D,\qquad
s=(\ell\zeta-T)/u=-v_1,\qquad
D=\ell(2\lambda^2-2\lambda+1)-T^2.$$

原三值互异和 b,c 非零通过已核身份

$$D+\ell E_2=bc(h_U-k_U)^2$$

支付 D 在原合法点的非零性。该论证支付的是实际点的 D，不是 D 在首一商中的范数。

定义同一个 qY 余式

$$D_*=D_0+D_1Y=\operatorname{rem}_{q_Y}(D),\qquad
q_s=s^2-D_*/M,$$

$$C_*=\operatorname{rem}_{q_Y}
\{\ell^2B_\lambda-3\ell T A_\lambda+2T^3\},$$

其中 A_lambda=2lambda²-2lambda+1，B_lambda=4lambda³-6lambda²+3lambda-1。第三矩原行在四生成元 1,Y,s,Ys 中恰为

$$R_C=C_*-2mD_*s.$$

它与原第二、第三矩的准确身份在前稿和本源均重建：

$$C_{\rm orig}
=\ell(2ms+3\ell+3T)E_2-\ell^2E_3.$$

前稿已实际完整返回的十行是 E1、EBe、N1、RC、EDelta、EC、N_even、N_odd、P_even、P_odd。每行有完整的 qY、qs 原理想迹。这里分别保留两谱个别 N/P，适用范围始终是原 Delta=0、W=0。

## 2. 不使用范数的唯一值恢复

以下所有乘法先在 A0[Y]/(qY) 中进行。原点的 m、D_* 均非零，因此 RC=0 唯一给

$$s=\frac{C_*}{2mD_*}.\tag{1}$$

把 q_s 返回为单个等式

$$F_M=\operatorname{rem}_{q_Y}
\{M C_*^2-4m^2D_*^3\}=0.\tag{2}$$

令 b_*=2mD_*。其原组合身份为

$$M C_*^2-b_*^2D_*
=M(C_*+b_*s)R_C+b_*^2(Ms^2-D_*).\tag{3}$$

故 (2) 是原式的准确必要条件。反向，若 (2)、qY 和 D_* 非零成立，则 (1) 使

$$s^2-D_*/M=F_M/(4m^2M D_*^2)=0.$$

这里等式按 qY 商解释；没有把 1/D_* 换成任何范数逆。因而 (1)—(2) 对原两个值矩和 RC 给出完整双向返回。

## 3. 其余六条原行的两列返回

将每条含 s 的已返回原行写为

$$R_i=A_i(Y)+B_i(Y)s,\qquad \deg_Y A_i,\deg_Y B_i\le1.$$

i 依次为 EDelta、EC、N_even、N_odd、P_even、P_odd。直接做原行组合

$$2mD_*R_i+B_iR_C
=2mD_*A_i+B_iC_*.\tag{4}$$

右侧不含 s。定义

$$F_i=\operatorname{rem}_{q_Y}
(2mD_*A_i+B_iC_*).\tag{5}$$

(4) 没有新增除法；本次源逐个核验两次乘法的完整 qY 商与余式，并实际核验 s 两列严格相消。全部最终标量分母仍只来自已付权因子。

在原 D_* 非零的同一点，(1)、(5) 也反向给 Ri=0。因此用前三条 Gram 两列余式、(2) 及六条 (5)，得到**十条两列方程**。与原 qY、qs 及完整十行相比，它们在上述物理图上双向等价，且 s 唯一恢复。

没有把某个实际参数点的线性系数当作单位。特别地，两列方程的一次首项可以为零；本结论逐一保留这些纤维。

## 4. 首一乘法核验与实际大小

对 r=a+bY、v=c+dY，使用精确公式

$$rv=(ac-\gamma bd)+(ad+bc-\alpha bd)Y+bd\,q_Y.\tag{6}$$

本次所有新乘法都由 (6) 的完整系数乘回核验，包括 C_*²、D_*²、D_*³、六条 (4) 和物理单位分子。相应 qY 商也保留在再生源中；不通过采样或多变量模理想判空。

七条新两列行的实际分子次数界与项数为：

| 原行 | 分子次数界 (e,k,w) | 两系数分子项数之和 |
|---|---|---:|
| 矩返回 | (83,111,26) | 245671 |
| original_Delta_zero | (57,75,16) | 68175 |
| original_compatibility | (70,92,21) | 133338 |
| individual_N_even | (67,92,21) | 131432 |
| individual_N_odd | (67,91,21) | 130559 |
| individual_P_even | (69,94,21) | 138428 |
| individual_P_odd | (68,91,21) | 132119 |

这些次数是两项各自约分后的分子次数界。它们说明本结论完成了几何变量消去，同时展开系数仍较大；不能把“两列”误写成系数已经低次，也不能从这一表示直接宣称参数图有限或为空。

## 5. 原物理非零条件在同一点保留

对任一个已返回的原单位 U=A_U+B_U s，定义

$$U_*=\operatorname{rem}_{q_Y}
(2mD_*A_U+B_UC_*).\tag{7}$$

由同一个 (1)，在原点 U_*=2mD_*U。因 2mD_* 已付，U 与 U_* 非零完全等价。

源对 Y、lambda、D、s、zeta、S 六个原元素全部实际完成 (7)，各自保留小哈希回执。其它原物理不等式也仍随原模型保留。不能用这些元素在真实点非零，推断它们在整个首一二次商的范数非零。

固定一个合法参数点 (e,k,w) 后，Y 必须是 qY 的根，s 再由 (1) 唯一恢复。这只给该参数点至多两个候选值；本文没有把 D 局部化后的整个原商宣称为 A0 自由模或已构造全参数单位证书。

## 6. 自含源与真实运行

自含源：

`notes/2026-11-27-unit211-generic-LS-W-native-coefficient-D-cleared-two-generators-8542.py`

- 源 blob：`4c26c8f10ad0ed3079e98ad6237612fd3f8d78d1`。
- 源 SHA256：`dc36564994eeec8cf3182200e792fb43b898ac566c493510d1a32d65e2e7b526`。
- 实际 run `45985219969`，job `140458996539`；内层 exit 0。
- 源 42.921846320 秒，驱动 43.083613055 秒，峰值 RSS 609648 KiB；配置 180 秒、4 GiB。
- stdout 31821 字节，SHA256 `ce3d8ec6ddddfcb7aa3fd36dc3e2d51754b4b6235afb82a5d7035f8d2e3a45d5`。
- 完整新矩阵的可再生规范序列化为 48335190 字节，SHA256 `853a31360d7de56b56c3f98ee79fbf5f8c0b84f4ace548becd1fadabfc86ed40`。只保源码、参数、字节数与哈希，不存该可重算大缓存。
- 真实 pull 于 2026-11-27 10:48:52.852579 UTC，由 `4e0939224bfb63a8df4ae19b18fbd4aa4ea75ead` 更新到 `a4e66e2d32dba6d46a74c1f7ce6c220e5d3ac762`；两 README 无变。

本次没有计算参数 cofactor，也没有给出任何 QQ 或模素数单位。下一输入可以对同一两列原行取真实常数列 cofactor，并继续原同点返回。W、一般 LS、R150 与普通 ISP 仍未完成。
