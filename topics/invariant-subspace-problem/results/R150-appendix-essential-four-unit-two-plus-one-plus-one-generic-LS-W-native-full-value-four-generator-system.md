# R150：W 整余图的原值十行、四生成元与真实乘法完整返回

**状态：已证明并实际返回的完整有限模表示；W 整余图尚未排空。** 本文完成先前首一值二次塔中尚未展开返回的全部十条原行。新计算把系数放在三变量环，逐单项式保留原理想迹；没有重复旧八变量大分子约化门，也没有倒置几何 D 的范数。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 作用域、同点坐标与系数环

全文限于原一般 LS 的 Delta=0、W=0 图。沿用已经完整排除的权边界和 y=1 整支，在余图令

$$u=e+1,\quad Q=ek,\quad V=(e+1)k+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV},\quad d=1-Q,$$

$$Y=y-1,\quad x_*=1+u-u/\ell,\quad
x=x_*+Yw,\quad y=1+Y.$$

两原均值给出的同一个 t 是

$$t=\frac{2x-2dy+2e}{u}+\frac{T_0\ell d+\ell Nw}{uM},$$

其中

$$T_0=2u-\ell Q-2u^2,\quad
N=u(2-2u-Q)+\ell Q(2u-1),\quad
M=\ell(2u-\ell Q)-u^2=4bc(1-Q).$$

所有参数分母由既有完整结论支付；源逐个检查每种分母，并验证它只依赖 e,k。w 是新的自由几何参数，未把任一 w 多项式当作单位。Y、原 lambda、原 D、s、zeta、S 在原物理点的非零条件保留；这些元素的范数没有被当作单位。

记 A0 为 QQ[e,k,w] 按已付权多项式局部化所得的环。既有显式全图原组合给

$$q_Y=Y^2+\alpha Y+\gamma,\qquad \alpha,\gamma\in A_0.$$

它是三条原 Gram 行 E1、EBe、N1 的准确 A0[Y] 线性组合。alpha、gamma 对 w 的次数均为 4。其规范定义及全部原组合在本源前缀完整重建；本次实际返回 qY 的 SHA256 仍为
`00ebebbd7e0b470781046040f458e3cd73adfe984f038171c5f125cd9ee3a238`。
不要求旧头因子 D27、B239、J19 非零，它们的完整零纤维仍在本图内。

本文使用的 lambda、T、f 始终是这个同点 x,y,t 由原 E0、N0、P1 得到的值，未引入独立的第二份 Gram。

## 2. 首一值二次塔与原矩

置 m=u-ell，并以原值中心

$$s=(\ell\zeta-T)/u=-v_1,\quad
v_0=(T+ms)/\ell,\quad
\zeta=(T+us)/\ell$$

恢复

$$h_U=1+v_0-rs,\quad k_U=1+v_0+rs,\qquad r^2=d.$$

定义

$$A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,\quad
D=\ell A_\lambda-T^2.$$

原向量 Vval=(1,lambda-1-T,hU,kU) 满足第一矩 tau(Vval)=lambda。令 E2=tau(Vval²)-2lambda²，E3=tau(Vval³)-4lambda³。已发表并在本源实际重新乘回的恒等式是

$$\ell E_2=Ms^2-D,$$

$$C_{\rm orig}:=\ell^2B_\lambda-3\ell T A_\lambda+2T^3-2mDs
=\ell(2ms+3\ell+3T)E_2-\ell^2E_3.$$

把同点 D 按首一 qY 除法写成

$$D=D_2q_Y+D_0+D_1Y,\qquad D_i\in A_0.$$

则

$$q_s=s^2-h_0-h_1Y,\quad h_i=D_i/M,$$

满足准确的原组合

$$q_s=(\ell/M)E_2+(D_2/M)q_Y.$$

因此先取 qY 再取 qs 的两层首一商环

$$B=A_0[Y,s]/(q_Y,q_s)$$

有实际正规表示 1,Y,s,Ys。该两层首一商环本身是 A0 自由模；加上其余原行后的最终原解商只被四元生成，不据此声称它自由或非零。

这一构造没有使用 1/D 或 1/Norm(D)。物理 D 非零仍是原点约束。

## 3. 列明全部十条原行及其原式来源

按顺序使用

$$E1,\ EBe,\ N1,\ C_{\rm orig},\ E_\Delta,\ E_C,\
N_{\rm even},N_{\rm odd},P_{\rm even},P_{\rm odd}.$$

前三式是同一 Gram 的原行。第四式在 E2=0 时与第三矩 E3=0 等价，因为 ell 已付。

第五、第六式仍是原两线的

$$E_\Delta=\Phi N_f-S\zeta P_f,\qquad
E_C=\Phi N_c-S\zeta P_c.$$

其使用限于本文 Delta=0 图。源实际核验原 P1 和带完整第二矩余项的身份

$$\frac Q2N_4(V_{\rm val})
=N_ff+N_tt+N_c-\frac{Qf}{u^2}H_A,$$

以及

$$fE_\Delta+E_C
=\Phi\left(\frac Q2N_4(V_{\rm val})+\frac{Qf}{u^2}H_A\right).$$

这里 Phi 在本图已付。不能把该 Phi 倍数在一般 Phi=0 图当作原 N4(Vval) 的替代。

最后四式由两谱个别原条件产生：

$$N_h=N_4(g_2)-2\lambda P_{02}h_U^2,\qquad
N_k=N_4(g_3)-2\lambda P_{02}k_U^2,$$

$$P_h=P_2(g_2)-P_{02}h_U^3,\qquad
P_k=P_2(g_3)-P_{02}k_U^3.$$

源重建完整原 Gram 与正确双点乘法，并实际验证 Nk 是 Nh 的谱共轭、Pk 是 Ph 的谱共轭。因此 r 为单位时，两谱同零分别等价于偶、奇两个系数同零。这里只取偶、奇系数，没有以加权和替换个别条件。源另核验

$$bN_h+cN_k=NS-\frac{2\lambda P_{02}}{u^2}H_A,$$

$$bP_h+cP_k
=PS-\frac{P_{02}}{u^2}\{(3+2v_0)H_A-H_B\}.$$

故此前加权原 NS、PS 由保留的个别行和原矩推出，未丢弃同点条件。

## 4. 新系数表示与完整原迹

新源只在 QQ(e,k,w) 中做标量运算；Y,s 用形式单项式字典表示。每个原多项式的系数从原八变量式准确提取，提取的分母交叉乘积逐项返回。

对实际出现的每个单项式 Y^a s^b，源构造

$$Y^as^b=R_{ab}+U_{ab}q_Y+V_{ab}q_s,$$

其中 Rab 属于 span(1,Y,s,Ys)。先按 qs 降 s，再按 qY 降 Y；两者首项都是常数 1。源把等式两边每个 Y,s 系数实际乘回，并检查所有最终标量分母来自已付权因子。

随后用原系数线性叠加，得到每条原行 Fi 的完整身份

$$F_i=r_{i0}+r_{i1}Y+r_{i2}s+r_{i3}Ys+U_iq_Y+V_iq_s.$$

源对十条完整身份再次逐系数乘回。因 qY、qs 已有原迹，上式同时给出了原行与四列余式之间的双向理想返回；不是只有数值点或模素数核验。

实际十行余式的分子最高次数和分子项数如下。表中次数是四个有理系数各自约分后的分子次数上界，不是把全部分母强制统一后的次数。

| 原行 | 分子次数界 (e,k,w) | 四系数分子项数之和 |
|---|---|---:|
| Gram_E1 | (19,24,6) | 2824 |
| Gram_EBe | (16,20,6) | 1832 |
| Gram_N1 | (23,29,6) | 4118 |
| original_third_moment | (37,51,11) | 27161 |
| original_Delta_zero | (29,38,6) | 7250 |
| original_compatibility | (42,55,11) | 30563 |
| individual_N_even | (40,55,11) | 29407 |
| individual_N_odd | (38,52,11) | 26571 |
| individual_P_even | (40,56,11) | 32640 |
| individual_P_odd | (39,53,11) | 29623 |

本次处理第三矩原行仅用 0.180301 秒。此前旧输入在该行未完成返回时触及 180 秒，具体卡在约化、内容正规化或序列化的哪一步没有日志证据；本文不反推旧失败原因。新源取消可选的原始内容统一展开，改用三变量系数上的四生成表示。

## 5. 真乘法及最终商的限制

采用行向量系数，对有序基底 (1,Y,s,Ys)，真实乘法矩阵为

$$M_Y=
\begin{pmatrix}
0&1&0&0\\
-\gamma&-\alpha&0&0\\
0&0&0&1\\
0&0&-\gamma&-\alpha
\end{pmatrix},$$

$$M_s=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
h_0&h_1&0&0\\
-\gamma h_1&h_0-\alpha h_1&0&0
\end{pmatrix}.$$

本次八个基底乘法全部由上述单项式原迹实际核验；两矩阵的交换乘积也实际逐项相等。任何已返回原行与 Y、s 的乘法因而由标量线性直接给出，不需要重复展开二十份原八变量大分子。

在真实点上四列向量 (1,Y,s,Ys)^t 非零，全部十行均作用为零。可继续取真实行及其乘法的常数列 cofactor 作为参数必要式，但本文没有计算这种新 cofactor，更没有根据矩阵的一般秩宣称原图为空。

Y、lambda、D、s、zeta、S 本次也各自按同一 qY、qs 逐系数返回。它们必须在同一个原点取非零值；未据此倒置整个首一商中的范数。其余原物理不等式仍随原模型保留。

## 6. 实际运行、源与可再生证书

自含源：

`notes/2026-11-27-unit211-generic-LS-W-native-coefficient-full-values-four-generators-8542.py`

- 源 blob：`a4a911d3f76f36398319bb7fc9eb729288a9aa74`。
- 源 SHA256：`f9409e5f1675e94af9ed1b7d7d09fef6abb9897dc484c9758af97c847e581bfb`。
- 实际 run `45983891305`，job `140454454441`；内层 exit 0。
- 源实际 4.880988445 秒；驱动 4.954936787 秒；峰值 RSS 122460 KiB。
- 源限制 180 秒、4 GiB；没有提高旧门时限。
- stdout 23893 字节，SHA256 `252d2a2143a3b2b96058eb622ec8262e245d76c9bb1ddfe9c19630299711d9f2`。
- 实际检查 52 种标量分母、10 个单项式身份、全部十条原行和八个基底乘法。
- 完整十行及乘法矩阵的规范序列化证书为 7062089 字节，SHA256 `0c6ece9db8184cb65ea4c4da39353a4feab0bc3dbaf88b1e1a4ec1c3934e21c5`。证书由源码再生，未存储可重算大缓存。
- 真实 pull 时间为 2026-11-27 10:39:20.729596 UTC，前后提交均为 `8e3f1c066253f0a6b913b36095dcb786d936fad9`；两 README 无变化。

[准确小回执](../notes/2026-11-27-unit211-W-native-four-generator-full-value-receipt-8542.json)单独保存各行的次数、项数、字节数、原迹哈希和实际驱动信息。旧 7681 源及其真实 180 秒负回执保持冻结。本结论完成原值十行的四列表示，不声称 W、R150 或普通 ISP 已完成。
