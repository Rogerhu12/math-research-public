# R150：正确 Phi 的完整 N4 二矩范数、原理想身份与二次 t 头

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：完整纸面证明，无新执行。** 本文从同一个原值变量的第二矩和完整 $N_4$ 构造一个新的必要多项式
$$
C_{\rm NV}=(MZ_0+DZ_2)^2-MDZ_1^2.
\tag{1}
$$
它有直接的原理想来源，不乘 $D$，也不倒 $D$。在正确 $\Phi=0$ 的原恢复中，它关于原 $t$ 至多二次；其二次系数有一个显示的两因子公式。本文不把范数为零当成完整原系统的充分条件，不支付任何新首项，不给新的排空或有限点结论。

## 1. 同一个原值变量与完整二次型

沿[正确整个 t 参数均值图](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)，记
$$
\delta=1-Q,\quad \ell=b+c,\quad m=u-\ell,\quad
M=4bc\delta=\ell^2\delta-m^2.
$$
令 $\mathcal A$ 为当前正确 $\Phi=0$、物理 $D_{\rm phys}\ne0$ 原图已付的纯权系数环。以下原值恢复使用原单位 $\ell,M$；$\Phi^{-1}$、$D^{-1}$、新的值首项和范数都不进入 (1) 的构造。所用一般 $N_4$ 恒等式本身不要求 $\Phi$、W 或 $D\ne0$。

记
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
D=\ell A_\lambda-T^2,\qquad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,\qquad
w=\lambda-1-T.
\tag{2}
$$
取与原点相同的 $\sigma$，令
$$
h=1+\frac{T+m\sigma}{\ell}-\rho\sigma,\qquad
k=1+\frac{T+m\sigma}{\ell}+\rho\sigma,\qquad
\rho^2=\delta.
\tag{3}
$$
因此 $b(h-1)+c(k-1)=T$，没有选取单个复根或改换原值变量。

原第二、第三移位矩误差为
$$
E_2=b(h-1)^2+c(k-1)^2-A_\lambda,\qquad
E_3=b(h-1)^3+c(k-1)^3-B_\lambda.
$$
直接的原身份是
$$
q=M\sigma^2-D=\ell E_2,\qquad
H=K-2mD\sigma=(3T+2m\sigma)q-\ell^2E_3.
\tag{4}
$$
这些是[正确 I10 原值来源](R150-appendix-unit211-Phi-zero-corrected-individual-NP-full-NV-I10-and-two-decics.md) §2 的同点身份。本文的新范数只需 $q$；$H$ 留在完整原系统中，没有被删去。

令 $\mathbf V=(1,w,h,k)$。按真实 double-germ 乘法
$$
(vz)_1=v_0z_1+v_1z_0
$$
和原迹 $\tau$、原 Gram 算子 $\mathcal K$ 定义完整
$$
N_4(v)=2\tau(dv^2)-2f\tau(v^2)
-4\tau(v)\tau(dv)+4f\tau(v)^2+\tau(v\mathcal Kv).
\tag{5}
$$
[九自由变量的一般三个短式](R150-appendix-unit211-general-scaled-entire-N4-three-compact-identities.md) 给
$$
\mathcal N=\ell^2N_4(\mathbf V)=Z_0+Z_1\sigma+Z_2\sigma^2.
\tag{6}
$$
这里的三个 $Z_i$ 是完整二次型的常数项、完整极化项和二次项，而不是取某个分量或最高项。具体写
$$
\mathcal V=bX+cY,\qquad \mathcal W=bpX+cqY,\qquad c_\lambda=3-2\lambda.
$$
则
$$
\begin{aligned}
Z_0={}&\ell^2A_1+4\ell^2(1-2\lambda)f+2\ell fD
+2\ell u w(\ell c_\lambda+T)\\
&+2\mathcal V(\ell^2+\ell c_\lambda T+T^2)
+2bc\,t(T^2-\ell^2),\\
Z_1={}&2(\ell c_\lambda+2T)(u\mathcal V-\ell\mathcal W)
-2\ell Mw+4bc\,mTt,\\
Z_2={}&2\bigl((u^2-\ell^2Q)\mathcal V
-2m\ell\mathcal W-\ell Mf-bcMt\bigr).
\end{aligned}
\tag{7}
$$
(6)–(7) 的原证明没有用错误的紧凑 $R_2$，也没有用 W 的 $\Phi^{-1}$ 恢复。

## 2. 新的无 D 正乘子原理想身份

设
$$
A_{\rm NV}=MZ_0+DZ_2.
$$
由 (4)、(6)，有完整多项式身份
$$
M\mathcal N-Z_2q=A_{\rm NV}+MZ_1\sigma.
\tag{8}
$$
于是
$$
\boxed{
\begin{aligned}
C_{\rm NV}
={}&(A_{\rm NV}-MZ_1\sigma)
       (M\mathcal N-Z_2q)+MZ_1^2q\\
={}&M(A_{\rm NV}-MZ_1\sigma)\mathcal N\\
&+\bigl(MZ_1^2-(A_{\rm NV}-MZ_1\sigma)Z_2\bigr)q .
\end{aligned}}
\tag{9}
$$
展开右侧，$\sigma^2$ 项恰为
$-M^2Z_1^2\sigma^2+MZ_1^2(M\sigma^2-D)$，即得到 (1)。因此
$$
C_{\rm NV}\in(q,\mathcal N)
=(\ell E_2,\ell^2N_4(\mathbf V)).
\tag{10}
$$
(9) 是完整原式组合，不是从泛域点集消失反推理想成员。它在 $D=0$、$Z_1=0$、$A_{\rm NV}=0$ 及各个值首项零面仍然成立，也保留非约化纤维。它没有以某个形式除法将原方程除以 $D$。

另一种等价的定义是在普遍首一二次代数
$$
\mathcal B=\mathcal A[\lambda,T,t,\sigma]/(\sigma^2-D/M)
$$
中取 (6) 的乘法行列式：
$$
M^2\operatorname{Norm}_{\mathcal B/\mathcal A[\lambda,T,t]}(\mathcal N)
=C_{\rm NV}.
\tag{11}
$$
此处只有普遍二次代数 $\mathcal B$ 是自由二生成；这不表示完整原物理商自由，也不表示原三生成呈示自由。$D=0$ 时的二次代数仍保留 $\sigma^2=0$，不能将其替换成只含一个约化点的模型。

在一个原点上，(9) 直接给 $C_{\rm NV}=0$。反过来，单独的范数为零可以来自二次代数的某个根，并不保证它与 $H$、个别 N/P 或其他原条件选取同一个根。因此本文始终保留这些条件；不把 (1) 作为完整系统的等价替换。

## 3. 正确 Phi 恢复使完整 N4 对 t 仿射

为避免与原值向量 $\mathbf V$ 混淆，本节仍将权均值写成 $\mathcal V$。记
$$
s=u-1,\quad
T_0=2u-\ell Q-2u^2,\quad
J=2u(1-u)+\ell Q.
$$
在正确 Phi 图，
$$
P_f=T_0(J-Q),\qquad J-Q=-4s^2,\qquad
P_{02}=2s\ell Q
$$
均按原范围支付。真实 $E_0,N_0,P_1$ 恢复给
$$
P_{02}\lambda=Jf-Q\mathcal V+bcQt-sT_0,\qquad
P_{02}(T+\ell)=T_0(f-\mathcal V+bct).
\tag{12}
$$
令
$$
E=\frac{P_{02}(T+\ell)}{T_0}.
$$
从 (12) 严格解得
$$
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\quad
\mathcal V=f+bc\,t-E,\quad
A_1=2E,\quad
\mathcal W=T_0/2+2uf.
\tag{13}
$$
所以固定 $(\lambda,T)$ 时，$f,A_1,\mathcal W$ 均与 $t$ 无关，
而 $[t]\mathcal V=bc$。这是原双向仿射恢复的后果，不是另加 $f$ 或 $t$ 特化。

代 (13) 入 (7)，完整系数为
$$
\begin{aligned}
[t]Z_0&=2bc\,T(\ell c_\lambda+2T),\\
[t]Z_1&=2bc\bigl(u\ell c_\lambda+2(2u-\ell)T\bigr),\\
[t]Z_2&=4bc\,um.
\end{aligned}
\tag{14}
$$
最后一式只用
$M=2u\ell-u^2-\ell^2Q$。因此有特别短的原恒等式
$$
\boxed{
[t]\mathcal N
=2bc(T+u\sigma)(\ell c_\lambda+2T+2m\sigma).
}
\tag{15}
$$
(14)–(15) 是完整 $t$ 系数，不是将 $t=1$ 当原值代入，也不依赖原均值商上的自由性。

## 4. 新范数的二次 t 头及次数

由 (13)，三个 $Z_i$ 对 $t$ 均至多一次，故
$$
\deg_t C_{\rm NV}\le2.
\tag{16}
$$
对 (15) 在同一个普遍二次代数中取范数，或直接用 (14) 展开，得到
$$
\boxed{
[t^2]C_{\rm NV}
=4b^2c^2
\bigl(MT^2-u^2D\bigr)
\bigl(M(\ell c_\lambda+2T)^2-4m^2D\bigr).
}
\tag{17}
$$
例如
$\operatorname{Norm}(T+u\sigma)=T^2-u^2D/M$，
另一个线性因子同理；乘回 (11) 的 $M^2$ 即是 (17)。
没有倒这两个二次因子，其整零纤维全部保留。本文也不预判它们是否与任何已刊原必要式互素。

以 $(\lambda,T,t)$ 总次数计，由 (7)、(13)
$$
\deg Z_0\le3,\quad \deg Z_1\le2,\quad \deg Z_2\le1,
\qquad \deg D\le2.
$$
于是
$$
\deg_{\lambda,T,t}C_{\rm NV}\le6.
\tag{18}
$$
若写
$$
C_{\rm NV}=c_0(\lambda,T)+c_1(\lambda,T)t+c_2(\lambda,T)t^2,
$$
则 $(\deg c_0,\deg c_1,\deg c_2)\le(6,5,4)$。
这些是纸面已付上界；没有运行展开、系数 profile、因式分解、首项非零或准确次数结论。

## 5. 与旧 R6、Vlow 的完整关系及范围

只在已付 $m$ 的当前图，用已有
$$
R_6=MK^2-4m^2D^3,\qquad
V_{\rm low}=\frac{D}{M}A_{\rm NV}+\frac{K}{2m}Z_1,
$$
可得另一条显示多项式身份
$$
\boxed{
4m^2D^2 C_{\rm NV}
=(2mDA_{\rm NV}-MKZ_1)(2mM V_{\rm low})
+MZ_1^2R_6 .
}
\tag{19}
$$
(19) 精确说明：在物理 $D$ 开图，旧二式已推出新条件；但其已有直接组合带 $D^2$，并不等于在未倒 $D$ 的必要代数里已经有 (9) 的来源。新的 (9) 从原第二矩与完整 $N_4$ 直接取得同一个多项式。

例如形式 $D=K=0$ 时，旧 $R_6,V_{\rm low}$ 可以同时自动为零，而
$$
C_{\rm NV}=M^2Z_0^2
$$
还保留完整原 $N_4$ 的必要信息。这只是来源强弱的说明，不把该形式边界当作当前物理 $D\ne0$ 图中的点，也不据此宣布任一边界或整个 Phi 排空。

本文不改变已刊全规范维数至多一、全权十生成及每权纤维长度至多九等结论。若后续使用 (16) 与其他原 $t$ 方程作新输入，仍须保留 (17) 的所有头零、同一个 $\sigma$ 的原条件和全部未付纯权极点。既有两个 Q 主分量矩阵内存失败继续冻结；本文没有运行或续接它们。

## 6. 来源与无执行记录

本条仅逐式使用下列已刊来源并完成 (9)、(14)、(17)、(19) 的显示代数推导：

- 一般完整 N4 三短式，当前正文 blob 108e3d86b6ce6ed4bbd8dcea20adfa5c8ac4b775。
- 正确 I10 的同点二矩、三矩与完整 NV，正文 blob ef4bad0b9f5a762c57c9e54695fd4a4247111f32。
- 正确 Phi 全 t 参数原恢复，正文 blob 09d60f565189b74f88e82087ea4ba6ff4852e3c4。
- 完整 Vlow 原均值迹与两条八次式，正文 blob 5bbd08607cdf7caf06cfc1b58f93720c57de24a7。

没有新 Actions、复现门或系数载荷。日期采用 Asia/Taipei；推导发生于 2026-11-28 UTC。
