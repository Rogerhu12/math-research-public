# R150：正确 h=k、Delta 零覆盖的三个小因子原排除与 4788 个规范点上界

> **坐标范围澄清（2026-11-28）：** 本文的4788只计明列的 $(\lambda,u,Q,z,\rho)$、恢复的Gram及比值 $w,h,k$；不包含独立 $U_0$ 或物理矩阵轨道。新[约化权基与Artin包络](R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md)已将同一坐标的界增强为含重数长度≤4788；若明确加入 $U_0^3=-P_0$，相应包络长度≤14364。本文旧运行与不同点论证不改。

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 当前完整结论

在对称归一的原 $h_U=k_U$ 碰撞图，整个 $\Delta=0$ 原解集的不同有序规范坐标点至多
$$
\boxed{4788=399\cdot2\cdot3\cdot2.}
$$
准确剩余谱支持只有已刊正确固定十七阶行列式中的两个不可约因子
$$
F_{99}(\lambda)F_{300}(\lambda)=0.
\tag{1}
$$
所有原候选还须返回同一点的全部 Gram、N/P 条件；本篇没有排空 (1)，没有处理 $\Delta\ne0$，也没有声称原商长度为 4788。

这不是恢复旧 848、578 或“七个 lambda 覆盖”。本篇只把三个**附加小因子条件下**的独立真 Gram 排除，接到新的正确十七阶覆盖。全文为既有源及实际回执的完整静读和一个新的计数推论，没有重新执行已成或冻结的数学门。

## 2. 整个碰撞图的合法单位范围

记
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,
$$
$$
S=2\xi+3-2\lambda,\qquad \eta=\xi+3-2\lambda.
$$
[完整原 Pf 来源静审](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)已经逐全文核查四个等权前置源及四个直接 T0/JQ 源：它们使用真正的 $\operatorname{vm}(d,d)[1]$，不借错误 compact 均值，也不把不同值的 W 单位搬到碰撞图。因此整个当前碰撞图上
$$
P_f=T_0(J-Q)\ne0.
$$
原 $Q(1-Q)bcP_{02}$、$u(u-1)$、$A B\lambda(2\lambda-1)$ 以及 $S,\xi$ 的支付也沿该原图既有结果。

在本篇的 $\Delta=0$ 支上，准确原定义给
$$
\Delta=\Phi N_F-S\xi P_f=0,
\qquad
\Phi N_F=S\xi P_f\ne0.
\tag{2}
$$
所以这里的 $\Phi,N_F$ 非零直接来自 (2)。不需要恢复一个未经核定的“一般 h=k 的整 Phi 零排除”。

两个真实仿射原条件仍是
$$
P_c+P_f f+bcQ\Phi t=0,\qquad
N_C+N_F f+bcQS\xi t=0.
$$
它们在同一点给
$$
T_{\rm num}=P_fN_C-P_cN_F=0.
\tag{3}
$$
以下三条小支只使用这些合法范围。

## 3. C1 的完整条件排除

加上 $C_1=3\lambda-1=0$。原兼容源 86acc6 的完整 BigInt 身份为
$$
\Delta=\frac{2T_0}{225}D_{\rm lin},\qquad
T_{\rm num}=\frac{QT_0}{44100}T_{\rm lin},
$$
$$
D_{\rm lin}=196(u-1)(u-3)-71Q,
$$
$$
T_{\rm lin}=-392u(u-1)(19u-2)+(250-1457u)Q,
$$
$$
71T_{\rm lin}+(250-1457u)D_{\rm lin}
=-2940(u-1)^2(277u-50).
\tag{4}
$$
只用已付 $QT_0(u-1)$，(4) 覆盖整个条件支并唯一给
$$
u=50/277,\qquad Q=489412/76729.
$$
没有倒置一个依赖 u 的新头。

415f7e 的独立真原 Gram 源在这个有理权点保留整个自由 $f$，由原 P1 恢复同一个 t，再构造完整八条
$$
E_1,E_{Be},E_{Bo},N_1,N_{Be},N_{Bo},P_{Be},P_{Bo}.
$$
真正双点乘法返回的前四条 f 次数为 2，后四条为 3；完整 $\mathbb Q[f]$ Bézout 为
$$
a(f)E_1+b(f)E_{Be}=1.
\tag{5}
$$
两个原标签的完整乘积已在原运行返回。因此整个 C1 原支排除，包含所有复 f 和两个 $\rho^2=1-Q$ 符号。准确来源见[原 C1 条件页](R150-appendix-unit211-equal-singleton-Delta-zero-entire-lambda-one-third-exclusion.md)。

## 4. C2 的完整条件排除

加上 $C_2=3\lambda^2-3\lambda+1=0$，保整个二次域。a26a11 的真 $\Delta,T_{\rm num}$ 源给
$$
N_F=(4\lambda-3)(J-Q),
$$
$$
\Delta=(J-Q)\xi(\eta\Phi-ST_0),
\quad
T_{\rm num}=Q\eta(J-Q)
\{T_0wu-\xi P_{02}(\ell+T)\}.
$$
其中
$$
\eta\Phi-ST_0
=2(u-1)(\xi u+2\eta)+(T+\eta)Q,\qquad
T+\eta=(12-20\lambda)/7
$$
的最后一项在整个二次域有真实 Bézout 逆，故全支唯一恢复
$$
Q=3+3\lambda+(5/2-15\lambda)u+(-11/2+12\lambda)u^2.
\tag{6}
$$
实际后续仅从 Tnum 内式剥去一次 $u-1$，没有删 Phi 等其它支持；余式准确为
$$
133u^2+(-132+234\lambda)u+20-108\lambda=0.
\tag{7}
$$
该次运行没有进入源码中只适用于线性余式的原 Gram 后段。

置 $A_h=133u^2-132u+20,\ B_h=234u-108$。$B_h=0$ 时
$u=6/13$ 而 $A_h=-2128/169$，因此整个 (7) 上可恢复
$\lambda=-A_h/B_h$。准确整数身份
$$
3A_h^2+3A_hB_h+B_h^2=399\Psi_4(u),\qquad
\Psi_4=133u^4-30u^3-32u^2-24u+16
$$
覆盖所有原根。

独立 fbf53f 源在整个 $\mathbb Q[u]/(\Psi_4)$ 工作，保 (6) 同一 Q 与整个自由 f，从真实 Gram 返回八原行及 (5)。常数逆全部在整个代数上乘回，未选嵌入。故整个 C2 条件支排除。来源见[完整 C2 兼容页](R150-appendix-unit211-equal-singleton-C2-Delta-zero-complete-original-quartic-cover.md)及[原 Gram 排除页](R150-appendix-unit211-equal-singleton-Delta-zero-entire-C2-lambda-exclusion.md)。

## 5. C4 的完整条件排除及错误紧凑行隔离

加上
$$
C_4=8\lambda^4-24\lambda^3+24\lambda^2-12\lambda+3=0.
$$
在整个 $K=\mathbb Q[\lambda]/(C_4)$ 中 $\ell=1,T=\xi$。记
$$
c_0=3-4\lambda+\xi\eta,\qquad
H=(c_0+S\xi)u-2c_0,\qquad
C_0=2\xi u(u-1)(\xi u+2\eta).
$$
f2d555 源直接从原定义得到
$$
\Delta=-2(u-1)(HQ+C_0),\qquad
\gcd_{K[u]}(H,C_0)=1.
\tag{8}
$$
整个 Bézout 已返回，所以原支没有 $H=0$ 点，且 $Q=-C_0/H$。

同一个原 $T_{\rm num}=P_fN_C-P_cN_F$ 在这个 Q 图上只删除已付支持。实际为 u 的三层、u−1 的三层和 Q 分子的一个 gcd 层；最后一层不等于整个 Q 多项式的幂。其完整首一三次
$$
g_3(u)=u^3+g_2u^2+g_1u+g_0
$$
已在 62.418906039 秒返回，系数为
$$
g_0=\frac{-1935968-582832\lambda+2333440\lambda^2-734336\lambda^3}{377807},
$$
$$
g_1=\frac{86116+82696\lambda-151584\lambda^2+33024\lambda^3}{10211},
$$
$$
g_2=\frac{-1726012-2265096\lambda+2999120\lambda^2-176192\lambda^3}{377807}.
\tag{9}
$$

这份源另构造了旧错误 compact R。完整静读确认用于 (8)、(9) 的原 Delta、Tnum 在错误紧凑行之前独立定义；后算的 g3 只从该 Tnum 取分子并剥已付支持，数据流没有读取或被错误行改写。因此保留的是 (8)、(9) 的原必要性；**不保留旧“四紧凑原行”的整体原来源**。第一个有理 cofactor 没有返回，120 秒 SIGALRM 仍冻结，不重放。

独立 c52031 源以 (9) 的全部系数进入整个十二维
$$
\mathcal A=K[u]/(g_3),
$$
不假定 g3 不可约，不选根。在整个代数内返回 $Q=-C_0/H$、全部实际所需逆和原相容式；若出现非单位则必须保留两个因子继续，原实际不需要分裂。随后从真双点乘法构造同一个自由 f 的八原行，完整 $\mathcal A[f]$ Bézout 再给 (5)。

所以整个 C4 条件支为空。这个结果不使用 f2d555 的错误 R，也不使用旧七 lambda 的全覆盖。详见[保留的 Q 图和三次](R150-appendix-unit211-equal-singleton-C4-Delta-zero-complete-Q-graph-and-cubic-u-cover.md)及[条件 C4 原返回](R150-appendix-unit211-equal-singleton-entire-Delta-zero-exclusion.md)。

## 6. 正确剩余覆盖及新计数

[正确十七阶定理](R150-appendix-unit211-h-equals-k-corrected-fixed-seventeen-lambda-cover-and-5640-points.md)以真原必要
$$
P(\lambda,u),\ M_{\rm true}(\lambda,u),\qquad
\deg_{\lambda,u}P=(28,3),\quad
\deg_{\lambda,u}M_{\rm true}=(110,14)
$$
的固定 Sylvester 矩阵 S 返回次数 716 的非零行列式。仅删原已付谱支持后，准确完整因式分解为
$$
R_{\rm rem}=\kappa C_1^{19}C_2^{14}C_4^6F_{99}F_{300},
\qquad \deg R_{\rm rem}=470.
$$
本篇第 3–5 节已排 C1/C2/C4 的所有原点。因此保留 (1)，剩余次数
$$
470-19-2\cdot14-4\cdot6=399.
$$
F99、F300 是不同的 QQ 不可约因子，均只出现一次；特征零保证它们没有重根。

对每个剩余物理 $\lambda_0$，两个正确输入没有共同曲线，因而不可能同时在该值成为零的 u 多项式。若其不同共同有限 u 根数为 r，固定十七列的 Vandermonde 核列给
$$
r\le\operatorname{nullity}S(\lambda_0)
 \le\operatorname{ord}_{\lambda_0}\det S.
$$
已付谱因子在物理点非零，而剩余 F99/F300 只出现一次，所以右端为 1。每个剩余 lambda 至多一个原 u，故不同 $(\lambda,u)$ 至多 399。

[完整 Q 纤维](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Q-fibers-1444-cover.md)已经证明原 $\Delta(Q)$ 在任何允许 $(\lambda,u)$ 上都不恒零，次数至多 2；没有遗漏 Q 首项同时为零的纤维。
[完整 Loww 纤维](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Loww-fibers-8664-cover.md)则给每个 $(\lambda,u,Q)$ 上至多三个 $z=Qt$，其常数项
$$
-\frac{2P_{02}\lambda^2(2\lambda-1)^2}{B}
$$
非零，不要求 z 首项非零。

$\rho^2=1-Q$ 至多两个符号，给定 $(\lambda,u,Q,z,\rho)$ 后，原 P1 与均值恢复全部 f、t、X、Y 和 Gram 坐标，未留额外自由参数。因此依次为

| 当前不同原点 | 上界 |
|---|---:|
| $(\lambda,u)$ | 399 |
| $(\lambda,u,Q)$ | 798 |
| $(\lambda,u,Q,z)$ | 2394 |
| 有序规范完整坐标 | 4788 |

这里不是商的重数长度，也没有把必要条件说成充分条件。

## 7. 精确来源与未执行边界

本次完整静读的六份直接源码及既有实际范围为：

| 源 git blob | SHA256 | 已有实际返回 |
|---|---|---|
| 86acc608830f3e761cbef4c621c07b005c9a76b4 | a4a88b461b08b3f9fc793dcf019c25ebc88c133646ebb81d13879d50d6f5d9d3 | C1 三原 BigInt 身份；0毫秒低于计时分辨率，无伪造 exit/RSS |
| 415f7eb06f1b5dfa5e2953bbd3b2e4627dee4300 | e355e8b8e8ffcba91e1ae98627b618993c453c9df37abb027365d4e00129fb23 | run46029194247/job140608350964，0.103730850秒/34128KiB/0 |
| a26a11cf0b3df26655f4d4f6ee0b107ade4bebf9 | 6769f67d9d34995be4e4f90ad8d93d122b608a3312144d5822a5aa6b89a06f5a | run46030198815/job140611767985，0.092380266秒/34420KiB/0；只到原二次覆盖 |
| fbf53f44847f4cc1e81795882aedf6ede455afc0 | 74cfb3839c05301c57f8dbcaaf304181f0fa10e5a5ac806eb1cac1dced8618b5 | run46031135735/job140614937541，0.138608538秒/37736KiB/0 |
| f2d555ac62e231023c27962e75f82533a7020498 | 5b2b2fcd2706e2bbe6761b38055cd42ac6ccd63e944f8e4f8a7fd5cf5503d0aa | run46032150195/job140618367875，120.070572019秒/41680KiB/−14；只保正确 Q/Tnum 三次 |
| c52031f323be7923be2ce6328f56618d81ad2672 | 3b4e352d11a1fefdf496f481c6e1317c72221caef9e8ab90e63d00bbb157600d | run46033224090/job140622042399，1.906244035秒/37028KiB/0 |

C2 原兼容小回执 blob d523ec22e20b774f2f2a88e8a5f885c8f850be9d 与 C4 已成前段回执 blob 1a2aa3017407abfa1dbb2762a721ca963b1e4e0f 的实际因子、时间、系数均与后续原输入逐项一致。C4 的错误 compact 行不向这些独立前段传依赖。

正确 F99/F300 的唯一再生定义和全部输入乘积见十七阶原源 a12ac66b99fb8bc239cd303259c21a705dd02fab。其参数 SHA256 分别为
e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e、
5bfbc9ddc3b558dbef77fc19cd495175a1c8ad16461e6166c44cb982a1dca7ea。

没有启动新复现门，也没有搬回旧系数缓存。后继继续整个 F99/F300 的同点原返回及 $\Delta\ne0$；普通 Hilbert ISP 未完成。
