# R150：全余 W 的原 α、χ 十行二列模型与三条完整标量关系

日期：2026-11-28（Asia/Taipei）。作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。

**结论。** 在已刊全余 W 的真实 $D\ne0$、$t\ne0$ 原图上，新的纯权分母坐标 $(\alpha,\chi)$ 给出完整原 $I_6$ 的十行二列表示。本次首次执行实际返回了全域首一 $\alpha$ 二次、全部十行，以及三条非零原标量关系；它们的 $(e,k,\chi)$ 次数分别为 $(85,89,8)$、$(134,143,12)$、$(75,77,8)$。所有未知 $\chi$ 首项、内容及零纤维保持。

这三条关系尚未排空 W。本篇不声称它们互素，不由多变量 gcd 推断无解，也不把物理局部化的商称为有限自由模。

## 1. 准确范围与原坐标

沿用[全域原 α、χ 坐标定理](R150-appendix-unit211-W-global-original-alpha-chi-polynomial-coordinates.md)的权环 $A_W$。这是此前原单位已支付的当前 W 图；其单位来源限于该图，不外推到 $h=k$ 或其他权面。令

$$
u=e+1,\quad Q=ek,\quad \delta=1-Q,\quad \overline V=uk+2,\qquad
\ell=\frac{u((k+2)^2-2ek)}{k\overline V},
$$

$$
m=u-\ell,\quad \widehat U=u-\ell Q,\quad
M=\ell(2u-\ell Q)-u^2=4bc\delta,
$$

$$
Z_w=u(u-1)+\ell(1-\ell)Q,\quad
R_w=2u(1-u)-uQ+(2u-1)\ell Q.
$$

上篇已完整支付

$$
R_w=-\frac{ue^2}{\overline V}(4ek-k^2-4k-8).
$$

因此 $R_w$ 与 $m$ 都是这里的原权单位。$m$ 的来源是当前 $D\ne0$ 图的整等权排除；没有向碰撞图借用这一结论。

新的变量满足

$$
\alpha=4\delta(f-u)-\widehat U t,\qquad
\chi=\frac{2\delta A_1}{t}-Z_w.
$$

逆恢复是

$$
t=-\frac{\alpha\chi}{mR_w}-\frac{2\delta\ell}{m},\qquad
f=u+\frac{\alpha+\widehat U t}{4\delta},
$$

$$
V=f+\frac{(M-Z_w-\chi)t}{4\delta},\qquad
A_1=\frac{(\chi+Z_w)t}{2\delta},
$$

$$
W_1=\frac{T_0+4uf}{2},\qquad
x=\frac{\widehat U V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\tag{1}
$$

这些恢复式没有几何分母；只倒此前已付纯权。原坐标到 $\chi$ 的反向映射使用已付 $t\ne0$。因而原图与新图的双向等价始终保留 $t(\alpha,\chi)$ 的相应局部化，而不是忽略 $t=0$ 的多项式边界。

源再次逐式返回正确原均值差、$A_1$、$V,W_1,x,y$ 和原 $\lambda,T$ 的同一点身份。恢复多项式对 $(\chi,\alpha)$ 的次数是：

| 量 | $\chi$ 次数 | $\alpha$ 次数 |
|---|---:|---:|
| $t,f$ | 1 | 1 |
| $V,A_1,x,y$ | 2 | 1 |

所有身份也在 $\alpha=0$ 的多项式专化上成立；本次不以 $\alpha$ 或旧 $\gamma$ 为除数。

## 2. 三条原二次与实际首一二次

原 native 源使用真实 dual 乘法

$$
(vz)_1=v_0z_1+v_1z_0
$$

构造完整 Gram。这里的 $E_1$ 采用 $-2(vm(d,d))_1$，与已隔离的错误 compact 均值不同。

将四原二次 $E_1,E_{B,e},E_{B,o},N_1$ 同时按 (1) 拉回，令

$$
E_W=\ell E_{B,e}+mE_{B,o}.
$$

正确原均值差已被坐标关系消去，完整恒等式实际返回 $E_1=E_W$。因 $\ell$ 为原权单位，四条原条件精确化为

$$
P_0=E_W,\qquad P_1=E_{B,o},\qquad P_2=N_1.
\tag{2}
$$

三者都是 $\alpha$ 二次，系数属于 $A_W[\chi]$。本次实际分子 $(e,k,\chi,\alpha)$ 次数是 $(24,17,4,2)$、$(26,19,4,2)$、$(26,20,4,2)$。

使用已刊 native 六规则，但不执行旧十八乘法或旧行列式。取原线性齐次形式

$$
L_\alpha=\frac{2\delta}{u}(ux+\widehat U y)-\widehat U t.
$$

原六规则给出

$$
L_\alpha^3-R_2=\sum_{i=0}^3 H_i E_i,\qquad
\deg_{x,y,t}R_2\le2,\quad \deg_{x,y,t}H_i\le1,
\tag{3}
$$

其中右侧仅使用四原二次，完整原乘回成立。设 $d(\chi)$ 是 (1) 中 $(x,y,t)$ 的 $\alpha$ 方向，则实际返回 $L_\alpha(d)=1$。比较 (3) 的 $\alpha^3$ 系数，得到四个原二次头的 Bézout 身份；再用 $E_1=E_W$、$E_{B,e}=(E_W-mE_{B,o})/\ell$ 合并，得到

$$
\sum_{i=0}^2 c_i(\chi)[\alpha^2]P_i=1.
\tag{4}
$$

本次已实际生成全部 $c_i$ 并逐式乘回 (4)，不是仅使用存在性。于是

$$
q_\alpha=\sum_{i=0}^2 c_iP_i
=\alpha^2+q_1(\chi)\alpha+q_0(\chi)
\tag{5}
$$

是原均值理想中的首一二次。完整检查给出 $\deg_\chi q_0=3$、$\deg_\chi q_1=4$；两者所有分母均为纯权原单位，没有新的 $\chi$ 头开集。

$q_0$ 分子/分母 SHA256 为

- 109959dcbb54d9ee8b4739c7c3f8de5c47bfc3cc12b5438e8c29502de7bea69c；
- 2f4dcbe963875f22269efd0e769a57d664ace6eb3cd41c24f36f7986eaee9813。

$q_1$ 分子/分母 SHA256 为

- c8cce89f9a944cbd841503fcf0ace119809b6929e3f005d655cb0572e68bb3c8；
- 83ca772c279093cd1fd6fd5bb615212d9e80ff3af9b8ad3dd4c3bef164f907ad。

精确系数由冻结源 (3)–(5) 定义，不保存可重算载荷。

## 3. 完整 NS、PS 以自身系数一返回

对原 $NS,PS$ 各用 native 六规则约化。余式属于

$$
\operatorname{span}_{A_W}\{1,x,y,t,y^2,yt\}.
$$

其原来源含对应 $NS$ 或 $PS$ 的系数恰为一、另一原三次的系数为零。将余式与四个均值乘子都按同一点 (1) 拉回，得到

$$
P_3=NS+\sum_{i=0}^2 a_iP_i,\qquad
P_4=PS+\sum_{i=0}^2 b_iP_i.
\tag{6}
$$

全部 $a_i,b_i$ 的分母仍为纯权原单位，(6) 的完整多项式身份实际返回。因此五条 $P_0,\ldots,P_4$ 与完整原 $I_6$ 在新图内给出相同理想；它们不是只保必要条件的截断。

两条新余式均满足 $(\deg_\chi,\deg_\alpha)=(4,2)$。分子 $(e,k,\chi,\alpha)$ 次数均为 $(47,48,4,2)$，项数分别14698、14687；同一分母的次数为 $(39,45,0,0)$。准确指纹在小回执中保存，正文不附这些可重算大系数。

## 4. 十行二列的精确模表示

令 $C=A_W[\chi]$，先定义自由秩二的多项式环境

$$
B=C[\alpha]/(q_\alpha),\qquad \text{基 }(1,\alpha).
$$

对每条 $P_i$ 写

$$
L_i=P_i-[\alpha^2]P_i\,q_\alpha
=r_{i0}+r_{i1}\alpha.
\tag{7}
$$

全式短除和两坐标实际乘回。真实乘以 $\alpha$ 的两坐标是

$$
\alpha L_i\equiv
-r_{i1}q_0+(r_{i0}-r_{i1}q_1)\alpha \pmod {q_\alpha}.
\tag{8}
$$

所以完整十行依次为

$$
L_0,\alpha L_0,L_1,\alpha L_1,L_2,\alpha L_2,
L_3,\alpha L_3,L_4,\alpha L_4.
\tag{9}
$$

每行只乘已付权尺度清分母，未除未知 $\chi$ 内容。源逐行返回 (7)、(8) 和清分母尺度。

这十行的 $C$ 行空间正是 $B$ 中五个 $L_i$ 生成的理想：它显然包含各 $L_i$，而再次乘 $\alpha$ 由
$\alpha^2L_i=-q_1\alpha L_i-q_0L_i$ 保持在同一行空间。因此其 cokernel 精确表示五原式的商。合 (5)、(6)，这是完整原 $I_6$ 的表示，未要求原商自由，也没有把不交换的矩阵项直接置零。

每个未乘 $\alpha$ 的行，两列 $\chi$ 次数是 $(7,8)$；每个 $\alpha$ 倍行是 $(11,12)$。所有系数都属于 $C$。这里自由的是环境 $B$；进一步的物理 $t,D,\lambda$ 等局部化不据此自动称为有限自由 $C$ 模。

## 5. 三条原标量与整内容零面的保留

对已经清分母的两行 $r_i=(a_i,b_i)$、$r_j=(a_j,b_j)$，取两个真实乘子 $(b_j,-b_i)$。令其完整多项式公因子为 $g$，逐项精确除掉这个共同乘子，得到 $\mu_0,\mu_1$。源码实际检查

$$
\mu_0r_i+\mu_1r_j=(C_{ij},0),
\qquad
\mu_0(a_i+b_i\alpha)+\mu_1(a_j+b_j\alpha)=C_{ij}.
\tag{10}
$$

这一步约除的是两个实际乘子的共同因子，而不是把原方程除以 $g$；(10) 在 $g=0$ 上也成立。此后仅剥去已付纯权支持，得到三个非零必要多项式。

| 固定行对 | 原来源 | 最终 $(e,k,\chi)$ 次数 | 总次数 | 项数 |
|---|---|---:|---:|---:|
| $(6,8)$ | native NS、native PS | $(85,89,8)$ | 136 | 40194 |
| $(6,7)$ | native NS、其 $\alpha$ 倍 | $(134,143,12)$ | 218 | 146769 |
| $(0,6)$ | $E_W$、native NS | $(75,77,8)$ | 121 | 30440 |

规范 SHA256 分别为

- c6efb116e47b11c72571745d0ccd87c8483b84799fc30d84738e613ba86c92e8；
- ca620838ae402362880ec4e9741a255ad9986f06cedeb24822c347bc39617396；
- 9e45f89dfb25d8174b65b53f0de781fd61bb6a21d7960a710f8eef16e51eb448。

每条都是同一点原理想关系。三条均非恒定；没有新增单位、没有丢任何未知首项零纤维，也没有据此宣称全 W 排空。不能由这三个多变量多项式的形式或未作的 gcd 推出有限候选或空集。

## 6. 唯一首次实际执行

冻结源：[2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py](../notes/2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py)。

- Git blob a96d94c6305d08fc5802ca19b42acd23d81eebcf；14136 B。
- SHA256 18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b。
- Actions run46117628927 / job140894896622，内层 exit0。
- 驱动101.965228015秒，峰值RSS766372 KiB；固定预算180秒/4GiB。
- 原坐标0.008874664秒；三原二次1.277028431秒；实际首一组合11.462781565秒。
- 原 NS、PS 完整返回13.401171557、15.299410205秒。
- 全十行完成78.899654961秒；三标量分别84.249768333、98.766164882、101.847666965秒完成。
- 末 checkpoint101.847844874秒；6330次完整精确除法乘回、41项记录的新原身份乘回。
- stdout13311 B，SHA256 71392627cee544a3f1c14dd23f5b160b9517558c9172bde203887931f90dc49d。
- 源提交和真实pull均为b95d1349d16d4db7cf79f826fdc034b0d9523dd6；pull时间2026-11-28 06:39:52.105494 UTC，两份README无变化。

唯一固定依赖是原 C9 源的14656 B必要定义前缀，SHA256
88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。
完整依赖源SHA256为
10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1，
规范名为2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py。

没有再执行旧gamma十行尾、旧十二阶结式、十八行模块或native大行列式。所列大多项式只有定义、次数、项数、字节数和SHA回执；没有缓存或传送系数载荷。

[小回执](../notes/2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-execution-8542.json)保存这次完整返回及准确范围。
