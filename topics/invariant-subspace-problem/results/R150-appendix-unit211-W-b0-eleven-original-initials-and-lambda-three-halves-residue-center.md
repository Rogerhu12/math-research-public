# R150：W/b0 的十一原首项返回与 λ=3/2 剩余中心

日期：2026-11-29（Asia/Taipei；实际运行于2026-11-28 UTC）。会话：Astra-ISP-8542378f-20261127。GPT-6 Astra Pro（AI-assisted）。

**状态：已证明必要剩余中心，唯一首次完整返回；射线没有排空。** 对当前 W/b0 剩余 (-1,0) 权射线，十一条完整原必要式在全部五个非零 t 估值 cell 以及 t=0 中都实际返回
$$
(2\bar\lambda-3)^2=0
$$
的原初始理想身份。因此任何允许的剩余点均有 $\bar\lambda=3/2$。没有一个 cell 返回单位，$(\bar k+2)^{1,2,3,4}$ 均没有返回；全部权候选继续保留。

本次原输入新增完整 $R_6,N_{\rm low},P_{\rm low},V_{\rm low}$，没有重跑旧七式独立算法。所有结论来自本次完整输出，不根据 workflow 颜色、猜测秩或模数值图形推断。

## 1. 原图和新增完整条件

沿[本次输入](../notes/2026-11-28-unit211-W-b0-negative-e-full-I11-original-initial-two-positive-targets-8542-input.md)，仍在原 W、整 b0、物理 D 非零的已付权图上。原 q2/R6/N5 首项结论已限制
$$
v(e)<0,\quad v(k)=0,\quad \lambda\ne0,\quad v(\lambda)=0,
\qquad p=1009.
$$
本条只处理该射线，其它五条权射线不变。

原权定义为
$$
u=e+1,\quad Q=ek,\quad \bar V=uk+2,\quad
\delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k\bar V}.
$$
同一点 b0 恢复给 $T=(uQ\ell/A_*)(2\lambda-3)$，$A_*=4uQ-J$。$f,V,x,y$ 均按真实原 E0/N0/P1 恢复，整个四行 Gram 使用真 double-germ 乘法；特别 E1 独立构造。

七原式
$$
E1,\ EBe,\ EBo,\ N1,\ NS,\ PS,\ q_2
$$
全部保留。根据[完整低 D 次身份](R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)，新加入
$$
R_6=MK^2-4m^2D^3,\quad N_{\rm low},\quad P_{\rm low},\quad V_{\rm low}.
$$
这里
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2,\quad
K=\ell^2(4\lambda^3-6\lambda^2+3\lambda-1)
-3\ell T(2\lambda^2-2\lambda+1)+2T^3.
$$
$N_{\rm low},P_{\rm low}$ 保留原 singleton 完整奇部。完整 NV 使用同一原二次型
$$
V_0=(1,\lambda-1-T,1+T/\ell,1+T/\ell),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho)
$$
以及真正三个系数
$$
Z_0=N_4(V_0),\quad Z_2=N_4(V_1),\quad
Z_1=N_4(V_0+V_1)-Z_0-Z_2.
$$
本次全部偶/奇身份和已付权分母均实际返回，$D$ 未反演。即使 D 的首项在某个 cell 为零，新四式的完整最低项仍保留。

四条新必要式的实际整数本原分子为：

| 原式 | (e,k,lambda,t) 次数 | 总次数 | 项数 |
|---|---:|---:|---:|
| R6 | (13,15,6,0) | 29 | 1141 |
| Nlow | (25,28,5,3) | 48 | 9370 |
| Plow | (26,31,5,3) | 51 | 10778 |
| 完整 Vlow | (17,20,5,1) | 35 | 2972 |

这四个参数的完整 SHA、三个 Z 的 profile，以及原七式 profile 见小回执；不保存系数载荷。

## 2. 从十一式重新确定的完整分区

每条原有理式先清完整旧权分母，只剥已付纯权内容和非零有理常数；程序逐项返回它与同一点原式的准确尺度关系。由整数本原分子中每个项
$e^ik^j\lambda^lt^r$ 的几何权
$$
-i+r\tau,\qquad \tau=\frac{v(t)}{-v(e)},
$$
对**全部十一式**重新取下包络，实际断点为 -1 和 0。所得完整范围是
$$
\tau<-1,\quad -1<\tau<0,\quad \tau>0,\quad
\tau=-1,\quad \tau=0,
$$
另加原式先专门化后的 t=0。

这次算出的分区恰仍有五个非零 t cell；程序没有把旧五分区当作输入。66个原最低面均含1009单位系数，没有使用“全最低面都被1009整除后擅自跳层”的做法。

在代数闭剩余域中统一规范 e 的非零首系数后，非零 t cell 的初始理想位于
$$
\mathbb F_{1009}[\bar k^{\pm1},\bar\lambda^{\pm1},\bar t^{\pm1}].
$$
t=0 的计算没有 t 逆。此处初始理想是旧已付尺度归一后的**原必要式**的初始理想；旧权在原点为单位，并不强迫其初始值为非零。

## 3. 六个范围的真实目标返回

固定新算法先放入四条新值行，再放入原七行，一次完成新的十一源 Laurent 行约化。全部原多项式返回均附十一维来源向量。预定目标是1以及
$$
(\bar k+2)^n,\quad(2\bar\lambda-3)^n,\qquad n=1,2,3,4.
$$
目标本身不除其单项式、内容或未知因子。

真实结果为：

| 范围 | 原单位1 | $(2\bar\lambda-3)^n$ 首个返回指数 | $(\bar k+2)^{1,\dots,4}$ |
|---|---|---:|---|
| $\tau<-1$ | 未返回 | 2 | 全未返回 |
| $-1<\tau<0$ | 未返回 | 2 | 全未返回 |
| $\tau>0$ | 未返回 | 2 | 全未返回 |
| $\tau=-1$ | 未返回 | 2 | 全未返回 |
| $\tau=0$ | 未返回 | 2 | 全未返回 |
| t=0 | 未返回 | 2 | 全未返回 |

“未返回”只描述本次固定算法的实际非零余式；本文不据此宣称对应目标不属于原 Laurent 理想，也不宣称存在剩余点。特别第一幂的非零余式不被当作该类恰有幂零指数2的证明。

六次成功目标的归一乘子均已重新复合到未归一原最低式，并完整乘回。实际上只有原第6坐标，即 q2 坐标非零；同一乘子准确是
$$
63\,\bar k^{-6}.
$$
所以六个范围都返回
$$
\boxed{\quad
(2\bar\lambda-3)^2
=63\,\bar k^{-6}\operatorname{in}(\widehat q_2).
\quad}
\tag{1}
$$
等价地，$\operatorname{in}(\widehat q_2)
=-16\bar k^6(2\bar\lambda-3)^2$，因为
$63(-16)=1$ 于 $\mathbb F_{1009}$。

这里乘子不是猜测：其规范15字节小定义
$[[[-6,0,0],63]]$ 的 SHA256 为
cc9e35c040d798e735c5802fd0b64ec3d014b5296c6b777e616a8fa9d8a50581，
与六个实际未归一终端乘子完全相同。该识别只比较小参数定义的哈希，没有重新执行任何原初始理想或投影。

新四个值条件全成，但(1)的最终短来源只用 q2。本文如实保留这一事实，不声称每个新输入都在末组合中非零。

## 4. 剩余中心和仍然开放的范围

在任意剩余域点上，(1)迫
$$
\bar\lambda=3/2=506\in\mathbb F_{1009}.
\tag{2}
$$
不能把(2)写成特征零原点的 $\lambda=3/2$，也不能由当前 W 已支付 $3-2\lambda$ 就删掉这个剩余中心：原单位在赋值环中仍可有正估值。

[整个原 W 的 lambda=3/2 排除](R150-appendix-unit211-W-lambda-three-halves-complete-original-exclusion.md)已独立支付
$$
\mu:=2\lambda-3\ne0.
$$
结合(2)，当前剩余射线上的实际原点只能满足
$$
v(\mu)>0,\qquad
\eta=\frac{v(\mu)}{-v(e)}>0.
\tag{3}
$$
这是一个合法的新中心坐标，供后续不同的原输入使用。未将 mu 正估值假装成 mu=0 专门化；其全部正有理 eta 仍要保留。

本次没有迫 $\bar k=-2$，没有关闭任何一个 cell，更没有建立原权有限整模型或排空整个 W。其它五条未闭权射线不变。D 的首项零面、原全部权分母退化、t各区间/断点及当前新中心均按实际边界保留。

## 5. 唯一实际记录

源：[2026-11-28-unit211-W-b0-negative-e-full-I11-original-initial-two-positive-targets-8542.py](../notes/2026-11-28-unit211-W-b0-negative-e-full-I11-original-initial-two-positive-targets-8542.py)。

- Git blob c55c2aa7a11099914626844ce203f2a64c726b91；21072 B。
- 源 SHA256 9f16b2f6490f948211850595d653166c20fbc4d452e5b5848c0cc26c99083187。
- 唯一 run46162974839/job141034199881，attempt1，内层 exit0。
- 源提交 c8bfd50d7c0b1018445e6733b0286be486a83a02。
- 真实 pull 到 b88647b2c2b422c21488bc2b479cd266076d82db；规则读取2026-11-28T16:02:24.028854+00:00，两 README 未变。
- driver 3.326495765秒，数学最后3.249418411秒，峰值60380KiB。
- 240次旧权精除乘回、11条整数本原尺度、66个原最低面、269个新 S-pair、383个完整来源返回、6个复合后的完整十一源目标返回。
- 36次固定正幂目标尝试；6次成功，单位 cell 数0。
- stdout66447B，SHA256 e6915c4a0d0ad780a6bd00f0c7a2917a4208882f15e51dd0deaa591976b08b41。

[小执行回执](../notes/2026-11-28-unit211-W-b0-negative-e-full-I11-original-initial-two-positive-targets-8542-execution.json)只保存实际 profile、SHA和执行状态，不保存可重算系数或基缓存。资源界为180秒/4GiB、外层195秒；没有失败重跑、改素数或改点。普通 ISP 仍未由本条解决。
