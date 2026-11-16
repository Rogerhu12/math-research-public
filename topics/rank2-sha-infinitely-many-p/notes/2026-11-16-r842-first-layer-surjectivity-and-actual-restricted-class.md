# R842 增补：第一层总可延拓与唯一剩余的原受限类

日期：2026-11-16。**状态：以下原强窗中的精确收缩已证明；最后指定类的零或非零仍未知。**

本注只使用 [R842](../results/R842-original-gres-double-ramification-transpose-and-joint-prefix-extension.md)
的同一有限向量 $(\lambda_0,\lambda_1)$ 和真全局格。
保持 $T>2\kappa$，记
$$
\mathcal Q_T=H^0(C,\omega_CN^{-1}(TP)),\qquad
\mathcal Q'_T=H^0(C,\omega_CN^{-2}(TP)),\qquad
\mathscr V_T=H^0(C,N^3(-TP)).
$$

## 1. 第二个全局延拓等式总能先解

精确序列
$$
0\to\omega_CN^{-2}(TP)\xrightarrow{e}
\omega_CN^{-1}(TP)\to(\omega_CN^{-1})|_Z\to0
$$
的第一项满足
$$
H^1(C,\omega_CN^{-2}(TP))^\vee
=H^0(C,N^2(-TP))=0,
$$
最后一步是实际次数 $2\kappa-T<0$。
因此
$$
\boxed{\mathcal Q_T\longrightarrow
H^0(Z,(\omega_CN^{-1})|_Z)\ \text{满射}.}
\tag{1}
$$
这包括全部固定边界和非约化点，不只非固定简单分歧。

取任一真正全局 $\omega_1^0\in\mathcal Q_T$，
使其 $Z$ 限制等于 $\lambda_1$ 的第一层。
原有限正合列
$$
0\to\mathscr Z^\vee\xrightarrow{\iota^\vee=e}
(\mathscr Z^{(2)})^\vee
\to H^0(Z,(\omega_CN^{-1})|_Z)\to0
$$
给唯一
$$
\boxed{
\nu_0=(\operatorname{res}_{2Z}\omega_1^0-\lambda_1)/e
\in\mathscr Z^\vee.
}
\tag{2}
$$
于是 R842(19) 的第二式已经成立。
(2) 只在原有限概形中除去已知的理想因子，不是除去一个物理非单位前缀。

## 2. 只剩一个原仿射成员性

定义实际行
$$
b_0=j_T^\vee(\lambda_0-\mathfrak d^\vee\nu_0)
\in\mathscr V_T^\vee
$$
及原全局映射
$$
\boxed{
\mathcal L_T:\mathcal Q'_T\to\mathscr V_T^\vee,\qquad
\mathcal L_T(\sigma)(V)
=\langle D_3V,\operatorname{res}_Z\sigma\rangle_Z.
}
\tag{3}
$$
改变第一步的延拓，准确只能写为
$\omega_1=\omega_1^0+e\sigma$，$\sigma\in\mathcal Q'_T$。
同一个有限向量因而变成
$\nu=\nu_0+\operatorname{res}_Z\sigma$。
R842 第一式可解，当且仅当
$$
\boxed{b_0\in\operatorname{im}\mathcal L_T.}
\tag{4}
$$
证明直接使用 R842(16)：
第一式等价于
$j_T^\vee(\lambda_0-\mathfrak d^\vee\nu)=0$，
代入上述同一个 $\nu$ 正是 (4)。
所以 $[b_0]\in\operatorname{coker}\mathcal L_T$
不依赖任选的 $\omega_1^0$。

这里所有 $\sigma$ 都是真正
$H^0(\omega_CN^{-2}(TP))$ 的截面；
不能把其在 $Z$ 上的值当作任意向量。
其维数虽可由原 Riemann–Roch 准确读为
$$
\dim\mathcal Q'_T=T-\frac{3\kappa+\chi}{2},
$$
但本注不用这一数值预判 (4)。

## 3. 它正是 R836 的原兼容核，不是一个新环境核

因为 $T>2\kappa$，
$$
\iota_T:\mathscr V_T\to\mathscr Z
$$
也单射。相同的 Serre 序列给
$$
0\to H^0(C,\omega_CN^{-3}(TP))
\to\mathcal Q'_T
\to\mathscr Z^\vee
\xrightarrow{\iota_T^\vee}
\mathscr V_T^\vee\to0.
\tag{5}
$$
故 $\operatorname{res}_Z\mathcal Q'_T$
恰为 $\iota_T\mathscr V_T$ 的湮没子。

于是 (3) 的转置之核准确为
$$
\boxed{
\mathscr W_T
=\{V\in\mathscr V_T:
D_3V\in\iota_T\mathscr V_T\}
=\ker A_T,
}
\tag{6}
$$
即原 R836 的同一个受限空间。
有限维线性代数给自然识别
$$
\boxed{\operatorname{coker}\mathcal L_T\simeq\mathscr W_T^\vee.}
\tag{7}
$$
所以 (4) 的最后类就是指定原 trace 在原兼容高前缀对上的真实行，
没有增添局部 $V_1$ 或任意补列。

若 $V\in\mathscr W_T$，其伴随 $V_1\in\mathscr V_T$
由 $D_3V=\iota_TV_1$ 唯一确定；
在此识别下，
$$
[b_0](V)=
\langle V|_{2Z},\lambda_0\rangle_{2Z}
+\langle V_1|_{2Z},\lambda_1\rangle_{2Z}.
$$
因此单独尝试以第一层分歧值不能延拓来排除来源，
在本强窗没有障碍；真正未知是 (4) 的第二层耦合。

原三长核还须通过 R840 的唯一 $V_2$、同 $cF^3$ 的第三尾和第四短行。
所以即使 (7) 中的行非零，也不能未经限制便认它在更小真实核上非零。
整个 $\mathcal W_D$ 的余列、原同 $R$、余因子的各 Euler 项、
全部低行和十三 carry 继续保留。
