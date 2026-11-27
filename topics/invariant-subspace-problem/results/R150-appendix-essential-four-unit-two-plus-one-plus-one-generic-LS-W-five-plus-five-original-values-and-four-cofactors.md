# R150：W 整余图的五条无 s 原行、五条 s 一次原行与四个参数 cofactor

**状态：完整原行变换与四个新必要参数式均已实际返回。** 本文不再形成先前 43 秒的大 D 清分母矩阵；直接使用已返回的四生成元表示，保留两谱全部个别 N/P，并用真正原行组合得到四个参数 cofactor。全部未付一次系数与 w 首项零纤维保留。结果尚不排空 W。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 同点四生成元与实际局部化

沿用原 Delta=0、W=0 当前余图，同点系数变量为 e,k,w，原 mean 坐标 Y=y-1；u=e+1、Q=ek、V=uk+2，ell=u((k+2)²-2ek)/(kV)。此前原 y=1 完整排除已支付 Y，全部权分母沿用已有完整定理。

当前准确首一塔为

$$q_Y=Y^2+\alpha Y+\gamma,\qquad
q_s=s^2-D_*/M,$$

$$s=(\ell\zeta-T)/u=-v_1,\quad m=u-\ell,\quad
D_*=\operatorname{rem}_{q_Y}D,\quad
M=4bc(1-Q).$$

原十行 E1、EBe、N1、RC、EDelta、EC、N_even、N_odd、P_even、P_odd 已逐项返回为基底 (1,Y,s,Ys) 上的四列；RC 是原第三矩行

$$R_C=\ell^2B_\lambda-3\ell TA_\lambda+2T^3-2mDs$$

在首一塔中的余式。这里所有 lambda、T、f 均来自同一点 Gram。原物理 D、lambda、s、zeta、S 的非零条件仍在同一点保留，未倒置它们的范数。

以下运算在 B0=A0[Y]/(qY) 中完成，其中 A0 为 QQ[e,k,w] 按既有已付权因子局部化的环；s 仍按 qs 处理。没有倒置任何含 Y 或 s 的新首项。

## 2. 五加五是完整的原行替换

原两谱加权恒等式和原矩给出，在 qY、qs 商中准确成立

$$\ell N_{\rm even}+mN_{\rm odd}=NS,$$

$$\ell P_{\rm even}+mP_{\rm odd}
=PS+\frac{P_{02}}{\ell^2}R_C.$$

本次源实际把等式的全部四个系数乘回，未仅验证谱加权数值。由于 ell 是已付权单位，原十行可双向替换为以下五条不含 s 的行：

$$E1,\quad EBe,\quad N1,\quad NS,\quad PS,$$

和五条含 s 至多一次的行：

$$R_C,\quad E_\Delta,\quad E_C,\quad N_{\rm odd},\quad P_{\rm odd}.$$

这样保留了两个谱各自的完整 N/P 条件；没有以 NS、PS 两个加权和丢弃另外两条个别条件。

为降低系数，使用已付纯权标量做可逆归一化：

$$\widehat R_C=R_C/(2m),\quad
\widehat R_\Delta=\ell^2E_\Delta/(2m\Phi uQ),\quad
\widehat R_{\rm comp}=E_C/\Phi,$$

$$\widehat R_N=\ell N_{\rm odd}/(4P_{02}),\qquad
\widehat R_P=\ell^2P_{\rm odd}/P_{02}.$$

所有这些标量及其逆都由源按原已付权清单检查。本文仅在原 Delta=0、W=0 图使用分别的 EDelta、EC，未将一般 Phi=0 图的 Phi 倍数关系当作原 N4(V) 的替代。

## 3. 四个准确的小 s 系数

写各归一化行为

$$\widehat R_i=A_i(Y)+B_i(Y)s,\qquad
\deg_Y A_i,\deg_Y B_i\le1.$$

置

$$R_\alpha=(4e+3)k+4e+6.$$

本次源码实际核出并逐系数返回：

$$B_C=-D_*,$$

$$B_\Delta=\frac{R_\alpha}{V}T+\ell(3-2\lambda),$$

$$B_N=\operatorname{rem}_{q_Y}\{\lambda(\ell+T)\},$$

$$B_P=\operatorname{rem}_{q_Y}
\left\{3(\ell+T)^2+\frac{4m^2+M}{M}D_*\right\}.$$

其中 T、lambda 已是同一点的 Y 一次式。第一条归一化的 BC 使用物理 D，但本次后续操作没有倒置 D；其余三个 Bi 也没有被付为单位。

这些公式由完整原谱式得到。例如 Nh 的奇系数在原第二矩商中含

$$N_{\rm odd}
=(N_4(g_2))_{\rm odd}
+\frac{4\lambda P_{02}m}{\ell M}D
+\frac{4\lambda P_{02}}{\ell}(\ell+T)s.$$

Podd 的展开同样从 hU=1+(T+ms)/ell-rs 的三次幂逐项得到。实际源又将上述紧凑公式与完整已返回四列比较，避免以局部手算替代全原 N/P。

不支付 BDelta、BN、BP 或 ell+T 的任何零面。

## 4. 真正的 s 消去原组合与两列 cofactor

对两条归一化值行 Ra=Aa+Ba s、Rb=Ab+Bb s，取

$$E_{ab}=B_aR_b-B_bR_a=B_aA_b-B_bA_a.$$

s 系数严格相消，不需要任何一次系数可逆。对右侧按 qY 约化，得到

$$E_{ab}\equiv c_{ab}+d_{ab}Y\pmod{q_Y}.$$

源对每次 B0 乘法核验完整身份

$$(a+bY)(c+dY)
=(ac-\gamma bd)+(ad+bc-\alpha bd)Y+bd\,q_Y,$$

再实际核验 s 两列为零。因全部父行和 qY 都已有原迹，Eab 的两列余式也有准确原理想来源。

取一条无 s 的原余式 R=a+bY。新的常数列 cofactor 为

$$K=d_{ab}R-bE_{ab}=a\,d_{ab}-b\,c_{ab}\in A_0.$$

源实际核这两列：常数列恰 K，Y 列恰 0。清除已付权分母后，K 的分子是原系统的必要参数式。程序还尝试仅剥已付权因子，并逐项乘回；这四个规范分子本次均没有额外可剥条目。

所选固定四项及实际规模为：

| 项 | 无 s 原行 | 值行对 | 分子次数 (e,k,w) | 项数 |
|---|---|---|---|---:|
| 1 | EBe | Delta / N_odd | (58,77,18) | 46886 |
| 2 | EBe | Delta / P_odd | (62,82,18) | 52974 |
| 3 | E1 | Delta / N_odd | (61,81,18) | 52310 |
| 4 | EBe | third_moment / N_odd | (72,96,23) | 88522 |

相应分子 SHA256 依次为：

- `8dab2e03cabb09a23bb026a4bd92cbb4b05439a9f0e169cb417e2ebf652623cb`；
- `ad880428bc94154b9b350ef83b6631d67b89fe90739beaa8c36bab91f7c7174e`；
- `9d4de6fb3d69ddcf25d3aeea90e131df04402576f4345e49835f7b810fe32701`；
- `77ee10a8cfcc2241976426b8afba3197e4c2315defb4ad1b897732a6fad8e522`。

所有相关值行必须在同一个 Y、s 上返回；本文不把分开的投影根当作共同根。上述 cofactor 只给必要条件，没有声称四个参数式足以恢复原值。

## 5. 精确边界与后续可用范围

四个参数式关于 w 的次数是 18、18、18、23，不是已经形成的低次完整权覆盖。其 w 首项的权次数分别为 (45,61)、(48,66)、(48,65)、(54,75)，项数 1606、1867、1862、2337；这些首项均未支付。小回执保留它们的大小和哈希，未把大可重算系数写入日志。

即使某个 Bi 或无 s 原行的一次系数为零，上述组合仍是原多项式身份，所以该零纤维始终保留。若整条父行在某参数上退化为零，对应 cofactor 可能不提供新约束；这不能解释为纤维被排除。

原有限代数中的 Y 真单位及存在六次首一 w 关系是另一已证明的结构结论。这里没有使用尚未构造的首一 w 系数，不能由存在性直接剥掉当前 D6 的 J19 或本稿任何首项。

## 6. 源、真实成功及此前代码错误

实际成功源：

`notes/2026-11-27-unit211-generic-LS-W-five-plus-five-original-value-fixed-cofactors-Vbar-corrected-8542.py`

源 blob `b1b72fdab28b2e8c6867206b2df769d249fe8a3d`，36450 字节，SHA256
`f9141a7560c7b26ace78f0ccc55f540591ba2494241472f557eaae378213c42c`。

实际 run45987986656/job140468378419：内层 exit 0，源 24.665596351 秒，驱动 24.779341387 秒，峰值 RSS 421204 KiB；配置 180 秒、4 GiB。stdout 31564 字节，SHA256
`5cac095b2a3a9c1a0523a8b0dd5db37c0da3aea32331564106b6fd4679faaa45`。

真实 pull 于 2026-11-27 11:08:44.276028 UTC，由
`b7dd37b31d3794f0d976c7fb889fe18f045129bc` 更新到
`b47df53119ec9912fc9c9eb04c85094dce448bb4`；两 README 无变。

各原 cofactor 的可再生完整证书为 8155090、9681976、8801792、18312191 字节；只保存源码、参数、哈希及小回执。未保存这些可重算大缓存。

旧源 d5eab088 的首次门 run45987313941/job140466144960 在原 native 前缀通过后，因新增代码 V3=scalar3(V) 使用不存在的名称而内层 exit1；实际驱动 4.400422847 秒，RSS123124 KiB。其规范变量名是 Vbar。该次未执行新的五加五身份或任何 cofactor。旧源及准确负回执保持冻结；本次只修该名称并作首次正常运行，没有延时重跑资源失败。

本次完成原行变换及四条真实必要参数式；未形成 QQ 参数单位、未排空一般 W、R150 或普通 ISP。
