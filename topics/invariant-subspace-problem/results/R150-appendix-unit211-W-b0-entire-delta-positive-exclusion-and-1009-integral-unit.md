# R150：W/b0 整个 delta 正阶边界排除及 delta 的1009整单位性

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

**结论。** 对当前正确 W、完整 $b_0=0$ 及既有物理非零图的任一原代数点，在每个1009位置都有
$$
\boxed{v(\delta)=0,\qquad \delta=1-Q,\quad Q=ek.}
\tag{1}
$$
新唯一执行在准确的剩余开图中，把同 mu 的三条完整原式返回为单位；其余所有剩余零面由分别成立的原纸证覆盖。因此排除的是整个 delta 正阶边界，不是一个选取的模点或只剩一般开图。

本结论是原权分母的1009整单位性。它不等于整个 W 空性，也没有据此宣布所有其他权分母或几何坐标已经整。m、M、ell 等其他内部边界仍按各自原来源处理。

## 1. 先行范围与完整补图

[完整六射线及 u 边界](R150-appendix-unit211-W-b0-entire-positive-e-ray-exclusion-and-e-k-u-integral-units.md)已经证明
$$
v(e)=v(k)=v(u)=0,\qquad u=e+1.
$$
所以 Q 为单位、delta 整；只需排 $v(\delta)>0$。以下假定这一正阶并令 $U=\bar u$，于是 $\bar Q=1$、$U\ne0,1$。

[统一 ell 极点排除](R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md)不要求 delta 单位，已经给 $v(\ell)\ge0$。正确 W 权公式在 Q 剩余1时为
$$
\ell_0=\frac{U(2U^2-1)}{3U-2}.
$$
若 U=2/3，分子非零而分母零，ell 必有极点，矛盾。因此 $3U-2\ne0$。

余下权的准确剩余为
$$
\begin{aligned}
m_0&=-\frac{U(U-1)(2U-1)}{3U-2},\\
(A_*)_0&=\frac{U(4U^2+2U-3)}{3U-2},\\
\Phi_0&=-\frac{2(U-1)^2(4U-3)}{3U-2}.
\end{aligned}
\tag{2}
$$
定义
$$
S(U)=U(U-1)(3U-2)(2U^2-1)(2U-1)
          (4U^2+2U-3)(4U-3).
\tag{3}
$$
S 剩余零的全部可能已经按下表分别处理，不能把物理非零自动当成首值非零：

| 剩余条件 | 独立完整原来源 |
|---|---|
| U=0 | 已刊整个 u 正阶边界；本稿先行已付 u 单位 |
| U=1 | 与 e=u−1 已付整单位直接冲突 |
| 3U−2=0 | 上述统一 ell 极点排除，无 delta 逆 |
| 2U²−1=0 | [delta 的 ell 零与 Phi 零两支](R150-appendix-unit211-W-b0-internal-delta-positive-ell-zero-and-Phi-zero-original-exclusion.md)：原 q2/R6 覆盖全部 mu 阶 |
| 2U−1=0 | [整个 u 剩余二分之一深 m 支](R150-appendix-unit211-W-b0-internal-delta-positive-u-half-entire-original-valuation-exclusion.md)：全部相对阶、M 深相消和完整 N5 |
| 4U²+2U−3=0 | [整个 Astar 正阶支](R150-appendix-unit211-W-b0-internal-delta-positive-Astar-entire-original-valuation-exclusion.md)：完整 N5 极点一阶原身份 |
| 4U−3=0 | 上述 ell/Phi 两支中的 Phi 零支：不倒 Phi，只用原 q2/R6 |

后三篇对应原纸稿 blobs **452d85ca76afb89792184941cda257f95f26db87**、**f2f29f5e4352261f071382563eea89d20ad3b24f**、**16f694e5dfab93a1e59ee91daf1d7f8809a27bb2**。它们是与本次执行独立的完整补图证明，不是从新模返回外推得到。

所以任何尚可能存在的原点必须满足 $S(U)\ne0$。新执行只针对这个准确开图。

## 2. 原整性使同 mu 剩余合法

共同原定义是 [完整 b0/N5 源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**，SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8**。

在 S 开图，u、Q、ell、m、M、Astar、Phi 都是赋值环单位，且 M 剩余为负 m 平方。原 b0 准确给
$$
T=\frac{uQ\ell}{A_*}\mu,\qquad \mu=2\lambda-3.
$$
原 q2 对 mu 的二次头剩余是 $m^2A_*$，为单位，所有其他系数整。因此原 q2 可在赋值环中首一化，**mu 必整**。这一步不假定 lambda 或 mu 的剩余非零。

取 Q=1 后，令
$$
\begin{gathered}
A_2=(\mu^2+4\mu+5)/2,\quad B_3=(\mu^3+6\mu^2+12\mu+7)/2,\\
T=u\ell\mu/A_*,\quad D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell A_2T+2T^3 .
\end{gathered}
$$
三个完整原剩余式为
$$
\mathcal Q=2A_*m^2A_2+2M\ell(-3-2\mu),\qquad
\mathcal R=MK^2-4m^2D^3,
\tag{4}
$$
以及完整 N5 的正则剩余 $\mathcal N$。

N5 的 delta 分母在取剩余之前，准确按
$$
bc\,t_s=-P_c/(Q\Phi),\qquad
mTt_s/\delta=-4mTP_c/(MQ\Phi)
\tag{5}
$$
取消。因此它在本开图确实整，不能只把一个有极点的原分式生硬代入 delta=0。其完整表示为
$$
\begin{gathered}
G=\lambda P_{02}+(u-1)T_0,\quad
P_c=P_{02}(\ell+T)-GT_0,\quad
V_s=-G-P_c/\Phi,\quad y_s=(\ell T_0/2-uV_s)/M,\\
z_1=-2(-\ell\mu+2T)y_s-2\ell(\lambda-1-T)-4mTP_c/(M\Phi),\\
z_2=-2G-4my_s,\qquad
Z_0=2(T-\ell\mu)\{\ell u(\lambda-1-T)+V_sT\}-2P_cT^2/\Phi,\\
\mathcal N=2mD(Z_0+Dz_2)+MKz_1 .
\end{gathered}
\tag{6}
$$
这仍是完整原 N5 的 f 常数表达，不施加物理 f=0。所有实际分母只含 S 支持，且执行逐项核回。

由此任何原点都给同一个剩余 mu 上的 $\mathcal Q=\mathcal R=\mathcal N=0$。不存在从互不相关范数的根集合拼接同根的问题。

## 3. 本次新的三原标量和全部乘子

在
$$
A=\mathbb F_{1009}[u,S(u)^{-1}]
$$
中，
$$
q=\mathcal Q/(m^2A_*)=\mu^2+q_1\mu+q_0
$$
是真首一二次。完整 $\mathcal R,\mathcal N$ 各除一次 q 得
$$
r=a_R+b_R\mu,\qquad n=a_N+b_N\mu.
$$
两个商余及其对三原式的全部 mu 坐标均已实际返回。

固定构造
$$
\begin{aligned}
C_\times&=b_Nr-b_Rn,\\
C_R&=(a_R-q_1b_R-b_R\mu)r+b_R^2q,\\
C_N&=(a_N-q_1b_N-b_N\mu)n+b_N^2q.
\end{aligned}
\tag{7}
$$
三者都是纯 u 标量。没有反演一次头、范数头或几何 D；全部降头情况由这些普通原身份保留。各自乘实际纯 u 分母后，程序完整回传到 $\mathcal Q,\mathcal R,\mathcal N$，得到下表三个新必要多项式：

| 新标量 | u 次数 | 实际规范 SHA-256 |
|---|---:|---|
| 同 mu 的 R/N 交叉 | 58 | ab4534fbc1a6f017c4db41b72cf632326dc9b61ff4b2d42754bd561fdaec19e8 |
| 同 q 的 R 范数 | 59 | 05481ed8d87610d46e95a08b9d493d47cd4f9f58a1f967ae21165ef9272109d9 |
| 同 q 的 N 范数 | 60 | b19a53d121bee0b0d8cba2b8dcb57f563b6770a10b8bc9be0aef56587d1c274a |

它们只是原必要式；不宣称三式本身等价于全部原解。

完整 $\mathbb F_{1009}[u]$ 累积 Bézout 的实际次数依次为
$$
58\ \longrightarrow\ 30\ \longrightarrow\ 24.
\tag{8}
$$
最终首一公共多项式 g 的规范 SHA 是
**a07d8d64be1258f5a12e667179272cf0e0fb9170bd3e87c53f0d187f557a781f**。每一步都复合回三个原 mu 多项式，未只返回裸 gcd 次数。

## 4. 实际完成的全原单位身份

对 g 只按 S 的明确剩余单位支持作重复 gcd 精除。实际记录是 u 支持8层、ell 支持6层、m 支持4层，余式为首一常数1；所有商积完整乘回。这里“层”忠实记录实际 gcd 操作，不把未核的支持层数冒称某个完整因子的幂。

因 g 的全部支持在 S 中，程序实际完成普通除法
$$
S^{24}=q_g\,g
$$
并把所有 Bézout 乘子和 (7) 的三原来源复合。最后清实际终端分母；该分母此次是首一常数1。最终返回
$$
\boxed{
S(u)^{24}
=\Omega_Q(u,\mu)\mathcal Q
 +\Omega_R(u,\mu)\mathcal R
 +\Omega_N(u,\mu)\mathcal N
}
\tag{9}
$$
于 $A[\mu]$，其中三个 Omega 自身都属于普通 $\mathbb F_{1009}[u,\mu]$。三条原式的纯 u 分母均已核只含 S 支持；再整体乘它们的共同旧单位分母，就是普通二元多项式身份。程序最后重新乘回整个原 mu 多项式，不只比较 q 的两个余坐标。

实际目标次数216，SHA
**12badf9bb661f3a122e98e820e8ae8b4dc05b65a42bfdb1616e2c45ab6335f38**。
三个终端乘子的 mu 次数分别为5、1、1，u 次数上界分别为307、301、302；实际分母次数全部为0。

任一原赋值点在 S 开图的剩余满足三原式为零，但 (9) 左侧非零，矛盾。该普通身份适用于任何剩余域扩张，不挑选一个有限域根，也不把模返回提升成任意 QQ 泛型空性。

结合第1节全部补图，delta 正阶已无原点。delta 本来整，遂得 (1)。

## 5. 唯一真实执行与保存

新源：[原同 mu 剩余输入](../notes/2026-11-29-unit211-W-b0-internal-delta-open-three-original-same-mu-residues-8542.py)，blob **b2a31315dc3eb95e969f6573adf29a3bd7072c84**，12258B，SHA
**b352d1055ddafd27be722b5d855b1bd1cbbd91c043745e07b99b8288c5d0a7c5**。

[事前固定输入](../notes/2026-11-29-unit211-W-b0-internal-delta-open-three-original-same-mu-residues-8542-input.md)，blob **f5b297ce6389bb09de3a699237b860e9c6b6b282**，SHA
**d80f2c9b4b13873a4e54633144b314939f1552d07397429873520bd8d7d6cc39**。

唯一 [run46180594208](https://github.com/Rogerhu12/math-research-public/actions/runs/46180594208)，[job141089040156](https://github.com/Rogerhu12/math-research-public/actions/runs/46180594208/job/141089040156)：

- 零依赖，固定120秒/1GiB，外135秒；真实 **10.529501826秒 / 38588KiB / exit0**。最后数学阶段10.491690435999999秒。
- 全部10条数学记录已亲读；按原行重组 stdout 为 **6890B**，SHA **73d1a36d282b277aba9f6c33af56c40989ad1321cfcb7fb5396182337d1e577f**，与 driver 完全匹配。
- 原三式的 mu 次数2、6、5；两次首一除法、三个新同 mu 标量、完整累积 Bézout及最后单位目标全部完成。
- 实际完成33507次有限域多项式商积、29709次 Bézout 坐标返回、23次系数逆乘回、33项实际分母支持检查、18次三原 mu 坐标返回、18次支持商积。
- source commit **0465476f3dbeb52b217ed78fc61d41a58349a761**；实际 pull **7b1720935556f0e3d204ec1d735b682a9b5a153c**，UTC **2026-11-28 19:20:07.020060**。两 README 未变。

[小回执](../notes/2026-11-29-unit211-W-b0-internal-delta-open-three-original-same-mu-residues-receipt-8542.json)只保存实际10记录、原来源、资源和范围；不保存或传送大系数。没有重跑旧初始理想、射线、投影、PRS、旧同点范数或失败门。

本次完成 delta 的1009整单位性。它为后续完整整模型提供一个已证明的原分母条件；其他内部边界仍须原样保留，普通 ISP 尚未完成。
