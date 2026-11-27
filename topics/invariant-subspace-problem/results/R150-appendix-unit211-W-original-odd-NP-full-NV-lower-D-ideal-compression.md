# R150：全余 W 个别 N/P 与完整 N4(V) 的低 D 次原理想压缩

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。AI-assisted GPT-6 Astra Pro。

**状态：原理想压缩已证明。** 在已经建立的首一 T³/F² 六列环境及原 D 非零物理域中，已返回的十三条原行准确等价于十一条更低次数原行。四个 D²N、D³P 偶奇行可由两个仅含一次 D 清除的奇部行替代；完整 N4(Vval) 也可降到一次 D 清除。证明保留 NS、PS、R6；不除 D 的范数，不丢掉未付首项零面。

## 1. 沿用的原输入

沿用[十三条完整原六列行](R150-appendix-unit211-W-global-monic-three-two-thirteen-original-rows-six-columns.md)的记号和严格作用域。旧 D 非零权结论不外推到一般 hU=kU 图。令

$$A_0=(\ell+T)/\ell,\qquad M=\ell^2d-m^2,$$

$$D=\ell A_\lambda-T^2,\quad
K=\ell^2B_\lambda-3\ell TA_\lambda+2T^3,\quad
R_6=MK^2-4m^2D^3.$$

原值为

$$s=K/(2mD),\qquad
h_U=A_0+(m/\ell-r)s,\quad
k_U=A_0+(m/\ell+r)s,\qquad r^2=d.$$

原 Gram 的单点 N、P 多项式记作

$$N_4(g_2)=n_a+r n_b,\qquad P_2(g_2)=p_a+r p_b.$$

另一个单点与其共轭；此前实际源已经准确核验。

记旧 D² 个别 N 行的偶、奇部为 EN、ON，旧 D³ 个别 P 行的偶、奇部为 EP、OP。它们均为六列环境中的实际多项式像，没有引入 D 逆。

## 2. 两条更低次的完整个别原条件

定义

$$
N_{\rm low}=Dn_b+
2\lambda P_{02}\left(
\frac{KA_0}{m}+\frac{2mD^2}{\ell M}
\right),\tag{1}
$$

$$
P_{\rm low}=Dp_b+
P_{02}\left[
\frac K{2m}\left(
3A_0^2+\frac{(3m^2/\ell^2+d)D}{M}
\right)
+\frac{6A_0mD^2}{\ell M}
\right].\tag{2}
$$

这些分母只含已付 ell、m、M。原个别行与 (1)、(2) 之间有准确恒等式

$$O_N=DN_{\rm low}+\frac{\lambda P_{02}}{m\ell M}R_6,\tag{3}$$

$$
O_P=D^2P_{\rm low}+
\frac{P_{02}R_6}{M}
\left[
\frac{3DA_0}{2m\ell}
+\frac{(3m^2+d\ell^2)K}{8m^3\ell^2}
\right].\tag{4}
$$

可直接由

$$Dh_U=DA_0+K/(2\ell)-rK/(2m)$$

的平方、立方奇部展开得到 (3)、(4)。新自含源在自由整系数多项式环中清除上述权分母，实际逐项核出两个完整身份，而不是仅检查其最高次。

在 R6=0 和原 D 非零域中，ON=0 等价于 Nlow=0，OP=0 等价于 Plow=0。这里的等价使用原物理 D 非零；计算 (1)、(2) 的多项式像时并不需要求 D 的逆。

## 3. 已保加权原式恢复两个偶部

按原 b、c 权重，两个共轭个别行的加权和为

$$b(E_N+rO_N)+c(E_N-rO_N)=\ell E_N+mO_N,$$

P 行同理。

原值第二矩与第三矩给出

$$
\ell E_N+mO_N
=D^2NS-\frac{\lambda P_{02}}{2m^2\ell}R_6,\tag{5}
$$

$$
\ell E_P+mO_P
=D^3PS-\frac{P_{02}[3D(\ell+T)+K]}{4m^2\ell^2}R_6.\tag{6}
$$

为明确 (6) 的完整来源，令 q=Ms²−D、H3=K−2mDs。原两个平移值的第二矩偏差为 q/ell，完整 h³ 加权偏差为

$$\{(3\ell+3T+2ms)q-H3\}/\ell^2.$$

代入同一个原 s=K/(2mD) 后，H3=0、q=R6/(4m²D²)，即得 (5)、(6)。这保留了原第二矩、第三矩和同一值符号；没有将两个不同根的条件混配。

NS、PS、R6 都留在新输入中，ell 是已付权单位。因此 (3)–(6) 在 D 非零原域准确恢复 EN、ON、EP、OP 四行；不是以加权和代替两个谱。

## 4. 完整 N4(Vval) 的低 D 次返回

写

$$V_{\rm val}=V_0+sV_1,$$

$$V_0=(1,\lambda-1-T,A_0,A_0),$$

$$V_1=(0,0,m/\ell-r,m/\ell+r).$$

原 N4 对向量为齐次二次，所以完整表达式唯一为

$$N_4(V_0+sV_1)=Z_0+Z_1s+Z_2s^2,$$

其中

$$Z_0=N_4(V_0),\quad Z_2=N_4(V_1),$$

$$Z_1=N_4(V_0+V_1)-N_4(V_0)-N_4(V_1).$$

这是完整原二次形式的系数提取，不选取某个 N4 分量或 Phi 倍数。定义

$$V_{\rm low}=DZ_0+\frac K{2m}Z_1+\frac{D^2}{M}Z_2.\tag{7}$$

则有完整原恒等式

$$N_4(DV_{\rm val})
=DV_{\rm low}+\frac{Z_2}{4m^2M}R_6.\tag{8}$$

新源对 (8) 清除权分母后，也实际做了全部整系数乘回。因此，在 R6=0 和原 D 非零域，保留 Vlow=0 与保留整个原 N4(Vval)=0 等价。

## 5. 十三行到十一行的准确理想等价

令 J0 为原六条 Gram 行

$$E1,\ EBe,\ EBo,\ N1,\ NS,\ PS$$

与完整 r2、R6 生成的理想。上述八行都原样保留，不剥除 r2 的首项或其他未付参数因子。在原 D 非零局部化中，(3)–(8) 逐项给出

$$
J_0+(E_N,O_N,E_P,O_P,N_4(DV_{\rm val}))
=
J_0+(N_{\rm low},P_{\rm low},V_{\rm low}).\tag{9}
$$

左边正是已经实际返回的十三行原系统，右边为新的十一行。每个逆仅为既定原域的 ell、m、M、D；右侧三个新多项式的构造本身没有 D 逆，也没有任何范数逆。

新输入总次数更低：旧个别 N 乘 D²、P 乘 D³、完整 NV 乘 D²；(1)、(2)、(7) 都只作一次 D 清除，并利用原 R6 保留了等价关系。首一 T³/F² 的同一六列环境可以直接容纳其余式。

本页证明的是 (9) 及三个新原式的准确来源。新的十一行实际系数构建另有独立冻结源；在它真正返回之前，不把这项构建记为已经执行。整个 W 也尚未据此排除。

## 6. 实际小恒等式证书

自含源：

[2026-11-27-unit211-W-original-odd-NP-full-NV-D-power-lowering-identities-8542.js](../notes/2026-11-27-unit211-W-original-odd-NP-full-NV-D-power-lowering-identities-8542.js)

源 5841 字节，SHA256：

f083869fe46a453e014dabd0a8b3079ed0a5fa80d956d1694e9d2813075064df。

实际 functions.exec V8 执行 3 毫秒，使用 BigInt 整系数多项式，完整 (3)、(4)、(8) 的清分母身份均返回。规范证书 936 字节，SHA256：

449378fcc9294c062314bc1b020a88f5fe58db5bbae5c3627664942c44495057。

V8 无独立进程退出码或 RSS，均不猜测。前一份十三行成功源保持原字节，不重跑其 40 MB 系数作为新结果门。
