# 正确 Phi 第二完整 NV 头：原首一 lambda 三次、准确三行六列呈示与两个 sigma 必要式

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**本篇登记唯一首次实际返回。** 在正确 Phi、原 $D\ne0$ 的既定物理坐标图内，第二完整 NV 的 $t$ 头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0
$$
给出一个无需新头逆的原首一 $\lambda^3$ 关系。两个原矩与完整 $N_4(\mathbf V)$ 的必要子系统有准确的三行六列呈示。预定的两个三阶 cofactor 实际给出 $\sigma$ 五次、六次多项式，且各自均有完整三个原式的普通多项式乘子身份。六个最终原乘子的分母实际全为常数。

两个 $\sigma$ 头尚未支付；其整零纤维保留。本篇没有计算两个必要式的 gcd、结式、因式或共同零集，也没有证明本头支或整个 Phi 排空。物理 $t$、其余原均值、N1 和个别 N/P 条件均继续保留。

## 1. 原范围、原矩及完整 NV

沿[第二头的完整原矩纸证](R150-appendix-unit211-Phi-zero-corrected-second-NV-t-head-original-monic-sigma-and-four-columns.md)和[幂等元极化的完整小三次](R150-appendix-unit211-Phi-zero-corrected-second-NV-head-idempotent-polarization-and-small-complete-cubic.md)，置
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,\quad m=u-\ell .
$$
本次实际系数只需
$$
A_0=\mathbb Q[u,Q,(QsK_w)^{-1}].
\tag{1}
$$
这表示小多项式和证书的分母范围；物理解释仍限已经付清原 Gram 恢复的正确 Phi 图，并不把 Gram 延伸到其恢复未定义的 $M=0$ 面。

令
$$
a=\lambda-\frac32,\qquad T=\ell a-m\sigma,\qquad
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1 .
$$
两个完整原矩为
$$
\begin{aligned}
E_2&=\ell\delta\sigma^2-2ma\sigma+\ell a^2-A_\lambda,\\
E_3&=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2
       -m\delta\sigma^3-B_\lambda .
\end{aligned}
\tag{2}
$$
这里保留同一个原 $\sigma$，以及所有复根和重数。

为明确本次完整 NV 的来源，记
$$
\beta=\frac32-\lambda-\sigma,\quad T_0=-K_w,\quad
J-Q=-4s^2,\quad P_{02}=2sL,
$$
$$
e=L(1-\beta)-uQ\sigma,\quad D_0=(J-Q)T_0=4s^2K_w,\quad
F=P_{02}T_0\lambda-P_{02}e+sT_0^2 .
$$
原恢复给
$$
f=F/D_0,\qquad E=P_{02}e/(QT_0).
$$
设
$$
\begin{aligned}
C_f&=-1+2(1-\ell)\beta^2-4s\beta\sigma+4s^2\sigma^2,\\
C_u&=(1-2(1-\ell)\beta+2s\sigma)(\beta-2s\sigma),\\
P&=fC_f+uC_u+2E\beta(\beta+2\sigma)
 -T_0\sigma(1-2(1-\ell)\beta)+2\lambda P_{02}\sigma^2 .
\end{aligned}
$$
已付的完整原极化身份给
$$
P=N_4(\mathbf V),\qquad
C=QD_0P=4Qs^2K_wN_4(\mathbf V)
 \in\mathbb Q[u,Q,\lambda,\sigma].
\tag{3}
$$
源码使用前篇的五项多项式短式定义 $C$，并实际返回 (3)。$C$ 的总几何次数不超过三。本头支的完整 NV 的 $t$ 系数精确为零；这没有施加物理 $t=0$。式 (3) 使用完整 $N_4$，没有用其范数、最高项或一个分量替换。

## 2. 原首一 lambda 三次及准确子系统

从 (2) 直接相减，
$$
E_3-aE_2=-ma^2\sigma+2\ell\delta a\sigma^2-m\delta\sigma^3
+aA_\lambda-B_\lambda,
$$
且
$$
aA_\lambda-B_\lambda=-2\lambda^3+\lambda^2+\lambda-\frac12.
$$
因此普通原组合
$$
\boxed{
\begin{aligned}
q_\lambda
&=-\frac12(E_3-aE_2)\\
&=\lambda^3+\frac{m\sigma-1}{2}\lambda^2
-\frac{1+3m\sigma+2\ell\delta\sigma^2}{2}\lambda\\
&\quad+\frac14+\frac{9m}{8}\sigma
+\frac{3\ell\delta}{2}\sigma^2+\frac{m\delta}{2}\sigma^3
\end{aligned}}
\tag{4}
$$
在 $\lambda$ 中首一。其系数分母仅含 $Q$，总几何次数不超过三。式 (4) 在 $m=0$、$\ell=2$ 或 $\ell=4$ 等零面上仍是同一代数身份，未反演这些因子。等价紧凑式中 $a^2\sigma$ 的系数准确为 $m/2$。

因为 $QD_0$ 在 (1) 中可逆，且 $E_3=aE_2-2q_\lambda$，
$$
I_3=(E_2,E_3,N_4(\mathbf V))
=(q_\lambda,E_2,C)
\quad\hbox{于 }A_0[\lambda,\sigma].
\tag{5}
$$
这是三个完整条件的准确必要子系统；未宣称它已等于全部原物理理想。

单首一环境
$$
B=A_0[\sigma][\lambda]/(q_\lambda)
\tag{6}
$$
确实以 $1,\lambda,\lambda^2$ 为自由基。下文使用的是这个明确的自由环境；加入原条件后的真实商不必自由。

## 3. 六条实际原列及准确呈示

按预定顺序，在 (6) 中取六条同点余式：
$$
E_2,\quad \lambda E_2,\quad \lambda^2E_2,\quad
C,\quad \lambda C,\quad \lambda^2C .
\tag{7}
$$
每次只按首一 (4) 作普通 $\lambda$ 除法。若
$v=r+Q_vq_\lambda$，则把 (4) 的两个原矩乘子带入，得到 $r$ 对 $(E_2,E_3,C)$ 的普通原组合。实际程序逐列返回三个基坐标及其三个原式身份，六次除法全部完成。

在 $A_0[\sigma]$ 上以这些坐标为列定义 $\mathcal M$。因为 (6) 是真实的首一多项式商，$E_2,C$ 及各自的 $1,\lambda,\lambda^2$ 倍生成其整个理想作为底环模。因此
$$
\boxed{A_0[\lambda,\sigma]/I_3
 \simeq \operatorname{coker}\mathcal M,\qquad
 \mathcal M:A_0[\sigma]^6\longrightarrow A_0[\sigma]^3.}
\tag{8}
$$
式 (8) 是准确呈示，保留全部非约化结构，不需要假设真实商自由、根简单或各列独立。

六列实际返回的 $\sigma$ 次数如下，列内坐标按 $1,\lambda,\lambda^2$ 排序。

| 原列 | 常数坐标 | $\lambda$ 坐标 | $\lambda^2$ 坐标 |
|---|---:|---:|---:|
| $E_2$ | 2 | 1 | 0 |
| $\lambda E_2$ | 3 | 2 | 1 |
| $\lambda^2E_2$ | 4 | 3 | 2 |
| $C$ | 3 | 2 | 1 |
| $\lambda C$ | 4 | 3 | 2 |
| $\lambda^2C$ | 5 | 4 | 3 |

这些是本次实际次数，并与事前由总几何次数给出的上界一致。

## 4. 两个预定 cofactor 的完整原来源

仅采用执行前冻结的零起始列组
$$
[0,1,3],\qquad [0,3,4],
\tag{9}
$$
分别是 $(E_2,\lambda E_2,C)$ 与 $(E_2,C,\lambda C)$。对每个所选三阶矩阵 $M$，计算真实
$\operatorname{adj}(M)e_0$，实际返回
$$
M\operatorname{adj}(M)e_0=(\det M)e_0
\tag{10}
$$
的全部三个坐标，再合并三个列来源。于是行列式有三个原式的普通组合。

程序先清所有实际乘子的共同权分母，再约去**全部三个原乘子**的共同多项式因子；共同精除后重新返回完整原身份。仅从裸行列式约内容并不足以作这一步，本次没有这样处理。随后只剥除 (1) 中已付的 $Q,s,K_w$ 支持，把这些尺度运输到所有最终乘子，并把 (3) 的 $QD_0$ 运输到完整 NV 乘子。

最终实际得到
$$
\boxed{
\begin{aligned}
C_5(u,Q,\sigma)
 &=\Omega_{5,2}E_2+\Omega_{5,3}E_3
   +\Omega_{5,V}N_4(\mathbf V),\\
C_6(u,Q,\sigma)
 &=\Omega_{6,2}E_2+\Omega_{6,3}E_3
   +\Omega_{6,V}N_4(\mathbf V).
\end{aligned}}
\tag{11}
$$
全部六个 $\Omega$ 的最终分母实际都是常数，因而
$\Omega\in\mathbb Q[u,Q,\lambda,\sigma]$。式 (11) 作为完整原式身份成立于 (1) 的原系数环中；这句话不把 $E_2,E_3,N_4(\mathbf V)$ 本身的已付权分母错误地称作不存在。

第一组的三个乘子共同因子实际为常数 $1$；第二组的共同因子是总次数一、含两个项的纯 $u$ 多项式。两组都在共同精除后完整乘回，因此该共同因子的零纤维也由新身份覆盖。这里仅记录实际 profile，不从其次数或哈希猜测系数。

### 4.1 两个实际必要式

| 必要式 | 原列组 | $\deg_\sigma$ | $\deg_u$ | $\deg_Q$ | 总次数 | 项数 |
|---|---|---:|---:|---:|---:|---:|
| $C_5$ | $[0,1,3]$ | 5 | 12 | 5 | 16 | 225 |
| $C_6$ | $[0,3,4]$ | 6 | 18 | 9 | 25 | 626 |

规范 profile SHA256：

- $C_5$：5020a4cd05dbe94d0114486f282aca2a29989a87d58c67e90025cd03a29fca69。
- $C_6$：3aa8313b2740576418bc73fc51cead93f5d3fd0d9b50d29088dcf42cb4e706fd。

$\sigma$ 次数的事前上界分别为
$2+3+3-(0+1+2)=5$ 与 $2+3+4-(0+1+2)=6$；实际均达到该界。

### 4.2 未付的两个 sigma 头

令 $H_5=[\sigma^5]C_5$、$H_6=[\sigma^6]C_6$。

| 首项 | $\deg_u$ | $\deg_Q$ | 总次数 | 项数 |
|---|---:|---:|---:|---:|
| $H_5$ | 9 | 5 | 10 | 47 |
| $H_6$ | 18 | 9 | 19 | 118 |

其规范 profile SHA256 分别为：

- $H_5$：67a86db7d07d81eb65e8d2481046876d35b6e288351184b7bf8b1f6668885f4f。
- $H_6$：e6da2d440c8c130a171102a01f5fbbdb7eddc5a1d1340d281a6f658e86fa721b。

本次未证明任一头在原权环中为单位，也未计算它们的共同支持。所有头零纤维均继续保留。

在 $H_5\ne0$ 的权开图上，单由本篇必要子系统可先按 $C_5/H_5$ 降 $\sigma$，再按 (4) 降 $\lambda$，得到至多 $15$ 个生成元；在 $H_6\ne0$ 上同理得到至多 $18$ 个生成元。这只是 $(\lambda,\sigma)$ 必要子系统的生成界，不声称真实商自由，也不计算含物理 $t$、其余恢复坐标和尺度的完整点数。

## 5. 唯一实际执行回执

源码与预定输入：

- [源码](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-small-monic-lambda-six-columns-8542.py)，Git blob：999dcfdc3059ee6a9465f03ed555a20574fbf9a2；SHA256：11521b5532c7202582c3419dcb0a3b4283c8f72c092ad95422317b5d8512ec57。
- [首次输入](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-small-monic-lambda-six-columns-8542-input.md)，Git blob：1039f52a839a9d4e2a5c43e0ed400e4c9e8dc811。
- [实际小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-second-NV-head-small-monic-lambda-six-columns-8542-execution.json)，只含实际元数据、profiles 和来源统计，不含系数载荷。

唯一 workflow 为 invariant-subspace-8542-phi-small-monic-lambda-six-columns.yml；实际 [run 46176081967 / job 141074969574](https://github.com/Rogerhu12/math-research-public/actions/runs/46176081967/job/141074969574)，attempt 1。

| 项目 | 实际值 |
|---|---|
| source commit | 0b44296ab3ed26324259769b4adfd3f998b723d6 |
| 规则前真实 pull 后 commit | e7b0285b6d381b065814ac5456ab6ac3eb44c85a |
| 读取规则 UTC | 2026-11-28T18:29:07.335218+00:00 |
| 两 README | 均无变化 |
| 固定预算 | 120 秒 / 1 GiB；外层 135 秒 |
| driver 时间 / 峰值 RSS / exit | 0.172618653 秒 / 39956 KiB / 0 |
| 最后数学记录时间 | 0.110607670 秒 |
| stdout | 13858 B |
| stdout SHA256 | 31807a6bd81b2b93d951bfeccf9759f0df395101bbbe8fa799f7cfe4072e527c |

全部五条数学记录已读取，按日志原行恢复 stdout 后核对字节数及 SHA256；结论来自内层实际原式返回，没有仅凭 workflow 的绿色状态推断。

实际统计：2629 次精确乘法返回、两个首一原来源返回、六次新首一除法、六条原列的十八坐标、两个 cofactor 的六坐标、十次完整三原式返回，以及六个最终原分母检查，均完成。没有因失败后换组、选点或扩预算。

## 6. 结论范围

本篇付清的是第二完整 NV 头上的新首一 $\lambda^3$ 关系、准确必要子系统三行六列呈示，以及两个非零 $\sigma$ 五次、六次原必要式。式 (11) 保全部共同乘子零面和未付权头零面。

本次没有执行 scalar gcd、resultant、因式或模点测试；没有把两个必要式共同为零解释成其余原条件充分。物理 $t$ 未被删除，其他均值、N1、完整个别 N/P 及原单位范围仍须同点保持。第一 NV 头的旧泛域 gcd 已冻结，本文没有重放该输入；旧二十列和八条奇部列也未再生。整个第二头及整个 Phi 的排空均未由本篇得到。
