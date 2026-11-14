# 1150 个真实低模式方向进入完整中高球的条件接口

作者：exact_closure（GPT-6 Astra Pro，AI-assisted）；2026-11-13。

## 1. 结论及已经实际验证的范围

固定 R126 的同一 R100 参数域、同一真实低中心 C_L、25 块、17361 个有限正偶中频和全部 |m|≥34816 偶高频，以及原共同条带和全部物理/frame 权。取 root 的 `low-frequency-r1-conditional-images.json.gz` 中全部 25×46 个逐模低帽的准确两倍为条件半径 u_{j,n}。这些只是完整联立问题的候选低球，尚未声明其自身方程闭合。

在这组固定的条件低球上，本次实际构造并证明了完整非低映射的 50 个严格自映门、25 个完整复物理域门及 50 个条件距离门。实际最大物理球帽为 2.018369496869698e−12，严格小于原 R*=2^(-34)；没有改动原 Hessian 域。有限像/半径最大显示为 0.9443226093966106，高像/半径最大显示为 0.9999994683453407。距离全部准确小于 1/2，最小半距严格余量约 2.9089715473222155e−30。极小的严格余量以准确 Fraction 判断，不能凭显示小数 0.5 判定失败或通过。

本条同时给出任意非负距离方向 (du_{j,n},dr_j,dh_j) 的完整非低 Jw。1150 个低输入先保留模式，再支付纯低 Q 的和频卷积；没有先把它们压成 25 个总量投到近频。完整 mean、逆、所有三材料、block5 balanced 费用与 block21 正 profile 费用仍在。

## 2. 记号和完整源分解

逐模 u_{j,n} 及 L_{ij,n}、19 个 Gamma 窗口的定义、四个真和频系数和 alpha_kn 见同目录 `2026-11-13-exact-resume-low-quadratic-middle-proof.md`。记

\[
 U_j=\sum_nu_{j,n},\qquad k_T=270\,2^{-34},\qquad k=23/9+k_T.
\]

有限非低半径为 r_j；高半径为 h_j，普通块按 physical localV，block5 按 balanced physical，block21 按原 balanced positive profile。完整源严格拆成

\[
 N(C_L+u+Z)-N(C_L)=
 \Pi_\perp\{Q(C_L+u)-Q(C_L)\}
 +T(C_L+u)-T(C_L)
 +N(C_L+u+Z)-N(C_L+u),\quad Z=v+H.
\tag{I1}
\]

纯 Q 中频项是

\[
 q_{ij}(u)=\sum_nL_{ij,n}u_{j,n}
 +\frac12\sum_{k+n\ge94}\Gamma^{(2,w(k+n))}_{ij}\alpha_{kn}u_{j,k}u_{j,n}.
\tag{I2}
\]

所有有序对都保留；纯 Q 在更高中频和无限高频严格为零。完整 T 的两个接收值分别是

\[
 G^2_{ij} k_T(10U_j+U_j^2/2),\qquad
 A^2_{ij} k_T(10U_j+U_j^2/2).
\tag{I3}
\]

这里 A 是 R126 的实际 high physical-source 核，已含 weak-to-strong、frame 和目标输出权。T 没有被当成有限支撑多项式。

## 3. 同一三材料形式统一全部高空间

对每个 j≤i，把 R126 原六列和 profile 两列记为以下六个非负核 (g,c,s,a,d,t)：

| 源块 j | g,c,s | a,d,t |
|---|---|---|
| 普通块 | G²,G²,G² | A²,A²,A² |
| block5 | G²,BG¹,B²G⁰ | A²,DQ¹,DBQ⁰ |
| block21 | G²,Gc,Gs | A²,Ac,As |

其中 B=18555、D=257，Q¹、Q⁰ 是原 already-divided-by-frame high 源列；Gc、Gs、Ac、As 是已实付的 V·R、R² profile 源核。此处的 Q¹/Q⁰ 是核记号，不是二次分子。所有核沿用 R126 原数值和共同 σ，未重作窗口或 ODE。

令 C_j=10+U_j。第三项 (I1) 的有限与高接收界为

\[
 F_{ij}=k\{g(C_jr_j+r_j^2/2)+c(C_j+r_j)h_j+s h_j^2/2\},
\tag{I4}
\]
\[
 H_{ij}=k\{a(C_jr_j+r_j^2/2)+d(C_j+r_j)h_j+t h_j^2/2\}.
\tag{I5}
\]

加入 R126 同一真实 head/完整纯中心常量、(I2)、(I3)，并按 j≤i 求和，即 `images` 的完整像。head/纯中心只支付一次。

完整物理域必须逐块核准

\[
 (10+U_j+r_j)V_{max,j}+h_j H_j<R_*,\qquad
 H_j=\begin{cases}B,&j=5,\\R_{profile,max},&j=21,\\V_{max,j},&\text{其余}.
 \end{cases}
\tag{I6}
\]

这个门控制 [0,C_L+u] 和 (C_L+u)+tZ 所需的全部复线段/球；所有均在同一 R116 适用域内。没有只检查中心或现实参数后把结论推广到复整球。

## 4. 任意 1200 分量方向的完整 Jw

对非负逐模方向 du，记 dU_j=sum_n du_{j,n}。纯二次导数为

\[
 dq_{ij}=
 \sum_n L_{ij,n}du_{j,n}+
 \sum_{k+n\ge94}\Gamma^{(2,w(k+n))}_{ij}\alpha_{kn}u_{j,k}du_{j,n}.
\tag{I7}
\]

这是有序整系数，不能再乘或除 2。两个纯 T 导数为 G² k_T(10+U_j)dU_j 与 A² k_T(10+U_j)dU_j。

第三项对 u 的微分严格等于

\[
 [DN(C_L+u+Z)-DN(C_L+u)]du,
\]

沿 Z 线段积分完整 D²N 即得有限/high 两个费用

\[
 k(gr_j+ch_j)dU_j,\qquad k(ar_j+dh_j)dU_j.
\tag{I8}
\]

不存在 k·10 的纯低直注高频项；10 只在合法纯 T 小项和非低自身导数中出现。这一分解及所需球域已由 geometry_audit 独立核对。

对非低 (dr_j,dh_j) 的 2×2 导数块是

\[
 J_{ij}^{NN}=k\begin{pmatrix}
 g(C_j+r_j)+ch_j&c(C_j+r_j)+sh_j\\
 a(C_j+r_j)+dh_j&d(C_j+r_j)+th_j
 \end{pmatrix}.
\tag{I9}
\]

`action` 的两行就是 (I7)、纯 T 导数、(I8) 与 (I9)(dr,dh) 的完整因果和。它使用完整导数证明，非形式微分某个并不保证导数的像上界。

## 5. 可调用接口与数据格式

`2026-11-13-exact-resume-nonlow-lowmode-interface-v1.py` 无额外数学包依赖，可由 importlib 导入。所有正式调用的数值使用 Python `Fraction`；浮点数仅可另用于诊断，不属于本接口证书。

```python
model = NonlowInterface(joint_path, near_path)
p = model.prepare(low_caps)                # 25 rows ×46 Fraction modes 2,4,…,92
image = model.images(p, r, h)               # each r,h has25 Fraction coordinates
Jw = model.action(p, r, h, du, dr, dh)       # du25×46; dr,dh each25
conditional = model.solve(p)               # only finds/verifies the nonlow ball
```

`image` 和 `Jw` 都返回 `finite[25]`、`high[25]` 和 `domain[25]`。调用者必须严格付 (I6)，且不能把 `solve` 成功解释为低方程或 cut 已闭合。`prepare` 没有把 u 的条件半径当成已存在的解。

实际 conditional primary 的 `low_mode_radii` 保存全部 1150 个准确候选。`rows[i]` 保存新 r/h、两个准确条件距离值、selfmap/domain、全部原 NN 因果导数；`complete_low_input_derivative_columns[j]` 保存有限输出的 46 个真实低输入列。高输出同一源块的纯 T/混合上界与 n 无关，故只存一个 `high_same_for_each_low_input`，消费时乘 sum_n du_n，不漏计模式。所有保存的正导数列向上取 dyadic，原准确 Jw 仍可直接调用，不必保存 1200² 稠密矩阵。

## 6. 实际主运行和独立校验

主数据 `2026-11-13-exact-resume-nonlow-lowmode-twice-r1.json.gz` 为 610200 字节，SHA256 `c06b4fe15fc5cc4ccf774fab4ef76a08db5f17219936f5f0b3f20ee2df2f0c21`。实际命令正式 exit 0，4.022879123687744 秒，wait4 peak RSS 53088 KiB。全部原 R126、near-Q、独立 R126 certificate 和实际输入 SHA 由 producer 核准。

独立程序 `2026-11-13-exact-resume-lowmode-interface-certificate-v1.py` 不复用 producer 的分窗口质量公式，而直接遍历全部有序 (k,n) 对重新支付 (I2)、(I7)，重算所有自映、整球和距离门。它还取全部 1150 个非零、非恒定方向

\[
 du_{j,n}=u_{j,n}(1+n)/95,\quad dr_j=r_j/(j+1),\quad dh_j=h_j(j+2)/29,
\]

逐行准确核对独立 Jw 与接口结果完全相等，并核对所有保存正列的方向作用确为上包。25 行全部 225 个独立门通过；实际正式 exit 0，34.60418152809143 秒，wait4 peak RSS 62728 KiB。原 2×低候选身份也逐项准确核准。

本条完整解决低模式进入非低方程的条件源与导数接口；仍须把真实低接收像、低方向导数和切口费用一起接入，才能宣称完整 1200 分量不动点、46 个 cut 或外场/闭合曲面结论。
