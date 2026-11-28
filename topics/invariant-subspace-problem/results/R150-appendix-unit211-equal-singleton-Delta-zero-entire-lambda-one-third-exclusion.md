# R150：h=k、Delta零的整个lambda=1/3原纤维排除

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27（Asia/Taipei）。

**结论。** 在既定原 h=k、Delta=0 域，整个lambda=1/3纤维为空。此结论只带附加条件 lambda=1/3；旧七 lambda 全覆盖已撤回，不能由本页宣称只余六个 lambda。与新的正确覆盖合并见[三个小因子及4788界](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)。本页不处理Delta非零，也不宣称整个h=k关闭。

## 1. 两条原相容式只留一个权点

沿用[原U值图](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)与碰撞图的准确记号。[完整 Pf 静审](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)支付整个碰撞图的 T0、J−Q 及等权互补；Q、u−1、S、xi 是原单位。在本页 Delta=0 上，准确原关系 Phi·NF=S·xi·Pf 直接支付 Phi、NF；不需要借一般碰撞 Phi 零排除。lambda=1/3时
$$
\ell=\frac{125}{196},\quad T=-\frac{25}{42},\quad
\xi=-\frac{14}{15},\quad w=-\frac1{14},\quad
S=\frac7{15},\quad\eta=\frac75.
$$
原两条仿射方程仍为
$$P_c+P_f f+bcQ\Phi t=0,\qquad
N_C+N_F f+bcQS\xi t=0,$$
并保持同一个自由f、t。直接从完整原定义，有
$$N_F=-\frac{98}{75}T_0,$$
$$
\Delta=\frac{2T_0}{225}D_{\rm lin},\qquad
T_{\rm num}=\frac{QT_0}{44100}T_{\rm lin},
$$
其中
$$D_{\rm lin}=196(u-1)(u-3)-71Q,$$
$$T_{\rm lin}=-392u(u-1)(19u-2)+(250-1457u)Q.$$
两个原因式及以下完整消Q身份均以BigInt多项式逐项返回：
$$
71T_{\rm lin}+(250-1457u)D_{\rm lin}
=-2940(u-1)^2(277u-50).
$$
由于Q、T0、u-1已付，Delta=Tnum=0强制
$$u=\frac{50}{277},\qquad Q=\frac{489412}{76729}.$$
全过程没有除250-1457u或任何未付参数首项；Dlin的Q首项是非零常数。故这个候选点覆盖整条lambda=1/3原相容纤维，而非从纤维中挑出的一个点。

## 2. 在同一个候选点保留整个自由Gram参数

在此有理点原A、B、lambda、u、u-1、u-ell、ell、P02、T0、J-Q、u+Q-1、Q、1-Q、bc、Phi、Pf、S均逐个核为非零。取
$$d=1-Q,\qquad r^2=d,$$
$$b=\ell/2+\frac{u-\ell}{2d}r,\qquad c=\ell/2-\frac{u-\ell}{2d}r.$$
这保留两个实际共轭单点的完整原权，不选取数值平方根。

保留f为自由不定元，严格由原P1解
$$t=-\frac{P_cf^0+P_ff}{bcQ\Phi}.$$
这里f^0=1。原另一仿射式在同一个f,t上恒为零；完整Delta、F、Tnum都逐式返回零。没有倒Delta或NF。

使用原双点代数的单位向量(1,0,1,1)、迹和Gram算子，从原E0/N0的准确仿射解重建全部Gram行。再次返回E0、N0、P1、NV和同一值V的一、二、三矩；两个单点的N、P目标都使用同一个h=k=1+xi。

全部八条尚需原方程在QQ[f]上实际得到：

| 原行 | f次数 |
|---|---:|
| E1 | 2 |
| EBe | 2 |
| EBo | 2 |
| N1 | 2 |
| NBe | 3 |
| NBo | 3 |
| PBe | 3 |
| PBo | 3 |

EBe/EBo、NBe/NBo、PBe/PBo来自原两个共轭行的偶奇系数，且r非零，故所有原解必须同时令这些系数为零。没有把抽象Gram根当作物理解。

## 3. 原QQ[f]单位身份

实际全多项式扩展Euclid已经返回
$$a(f)E1(f)+b(f)EBe(f)=1,$$
其中a、b都是一次有理多项式。完整八原行和两个Bézout标签的可再生证书为1927字节；两项完整乘回为常数1。当前仅保原源、定义和小回执，不另存可重算系数载荷。

因此原E1=EBe=0没有任何复f解；其余原条件无法恢复被排除的点。结合第1节整相容纤维覆盖，整个lambda=1/3、Delta零的h=k原纤维为空。

这同时覆盖f任意代数或超越值以及平方根r的两个嵌入。未使用模根、抽样或近似数值。

## 4. 准确源与真实回执

原三身份小源：
[2026-11-27-unit211-equal-singleton-lambda-one-third-Delta-Tnum-identities-8542.js](../notes/2026-11-27-unit211-equal-singleton-lambda-one-third-Delta-Tnum-identities-8542.js)，SHA256
a4a88b461b08b3f9fc793dcf019c25ebc88c133646ebb81d13879d50d6f5d9d3。
实际V8记录0毫秒（低于毫秒计时分辨率），没有独立进程exit/RSS，原小回执如实保留。

唯一候选点的新八原行源：
[2026-11-27-unit211-equal-singleton-lambda-one-third-Delta-zero-original-Gram-8542.py](../notes/2026-11-27-unit211-equal-singleton-lambda-one-third-Delta-zero-original-Gram-8542.py)，SHA256
e355e8b8e8ffcba91e1ae98627b618993c453c9df37abb027365d4e00129fb23。

实际run46029194247/job140608350964；源0.041650272秒、驱动0.103730850秒、驱动最大子进程RSS34128KiB、exit0。完整证书SHA256
5a7c1639ad4817324fa1706f7d778653bad36e0083787feb1f228ceb8d2e3fb0。
stdout4127字节，SHA256
6ae240cf001a6d12e6276f359f056db57c325350b6e97930c0c4fd5612896cfc。

真实pull为2026-11-27 15:56:00.010854 UTC，读到bc8bbd0e280183b25f698b83f820c7d4f69ea4d5，两README未变。该源只构造新单点原Gram，没有重跑此前578次覆盖或Q=1-u投影。

当前整个 Delta 零图还须处理正确覆盖中的 F99、F300；本页只保 C1 条件排除。普通复Hilbert ISP未完成。
