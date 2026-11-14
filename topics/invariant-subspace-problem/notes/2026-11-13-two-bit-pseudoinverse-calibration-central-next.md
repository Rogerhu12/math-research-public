# 两位纯 Boolean 伪逆校准：绝对小系数不能单独吸收最高导子项

日期：2026-11-13（UTC）。作者：central_next（Astra-ISP-0c017065）。
状态：已证明的有限维校准；不作为原 Haar 模型存在非零核的证据。

## 1. 所要校准的步骤与准确范围

在真实双阶导子工具中，令 $V_N=(C_{I_N}^{r_N})^\dagger$，
虽然
$$
[\operatorname{ad}_T^{2r_N}U_N]V_N\longrightarrow I
\quad\text{强收敛},
$$
把右侧 $V_N$ 放入核向量后，完整 Leibniz 配对仍含
$$
U_N(\operatorname{ad}_T^{2r_N}V_N).
$$
本记证明：即使纯线性 Boolean 系数都趋于零，以上这一类乘积也不会仅因绝对小系数而自动变小；幅度比例会保留，甚至产生无界范数。

这里仅用两个纯平方零矩阵，不把原实际 $N_j$ 换成 $E_j$ 后声称得到原模型的核。结论不否定利用原核、真实 carry、特殊配对或不同预处理的进一步消去。

## 2. 完整两位计算

取
$$
H_2=\mathbb C^2\otimes\mathbb C^2,
\qquad
Ee_0=e_1,\quad Ee_1=0,
$$
$$
E_1=E\otimes I,\qquad E_2=I\otimes E.
$$
基按 $00,01,10,11$ 排列。令 $a,b>0$，并置
$$
T=aE_1+bE_2,\qquad C=E_1+E_2,
$$
$$
U=-\frac12(a^{-2}E_1^*+b^{-2}E_2^*),
\qquad V=C^\dagger.
\tag{2.1}
$$
跨位矩阵交换，而
$$
\operatorname{ad}_E^2(E^*)=-2E.
$$
因此
$$
\boxed{\operatorname{ad}_T^2U=C.}
\tag{2.2}
$$

Moore--Penrose 逆 $V$ 的准确作用为
$$
V\,00=0,\quad V\,01=V\,10=\tfrac12\,00,\quad
V\,11=\tfrac12(01+10).
\tag{2.3}
$$
这由 $C\,00=01+10$、$C\,01=C\,10=11$，及各正交奇异子空间直接得到。

令
$$
K=U\operatorname{ad}_T^2V
=U(T^2V-2TVT+VT^2).
$$
计算中先有
$$
(\operatorname{ad}_T^2V)00=-b^2\,01-a^2\,10,
$$
$$
(\operatorname{ad}_T^2V)01=-a^2\,11,\qquad
(\operatorname{ad}_T^2V)10=-b^2\,11,\qquad
(\operatorname{ad}_T^2V)11=0.
$$
故完整矩阵是
$$
\boxed{
K=
\begin{pmatrix}
1&0&0&0\\
0&\tfrac12&\tfrac12(b/a)^2&0\\
0&\tfrac12(a/b)^2&\tfrac12&0\\
0&0&0&0
\end{pmatrix}.
}
\tag{2.4}
$$
所有式子均为有限维全域等式。

## 3. 真空矩阵元与绝对尺度

对归一参考真空
$$
\Omega=\tfrac12(00+01+10+11)
$$
有
$$
\boxed{
\langle K\Omega,\Omega\rangle
=\frac12+\frac18\bigl[(a/b)^2+(b/a)^2\bigr].
}
\tag{3.1}
$$
特别，当 $a=b$ 时此值为 $3/4$。

将 $(a,b)$ 同时乘任意 $\varepsilon>0$，$T$ 乘 $\varepsilon$，
$U$ 乘 $\varepsilon^{-2}$，$\operatorname{ad}_T^2V$ 乘
$\varepsilon^2$，所以 $K$ 完全不变。由此即使
$\max(a,b)\to0$，(3.1) 也不趋零。

若让 $a/b\to\infty$，例如 $a=\varepsilon$、
$b=\varepsilon^2$、$\varepsilon\downarrow0$，则
$$
\langle K\Omega,\Omega\rangle\to\infty,
\qquad \|K\|\to\infty.
$$
这精确否定“所有位系数绝对很小，所以最高伪逆交换子可直接吸收”的粗估计。它不否定保持幅度比信息或利用真实核约束的估计。

## 4. 与真实研究接口的区别

(2.2) 展示双阶导子能恢复纯提升主项，但并不意味着
$(\operatorname{ad}_T^2U)V$ 可以免费改写为
$\operatorname{ad}_T^2(UV)$；完整乘积公式还有中间导子项。

这里的 $\Omega$ 没有被声称属于某个原 Haar Bell 核；
有限维 $T$ 也不是原无限模型的反例。因此本记只登记一项估计障碍，不关闭或反驳原核配对中的任何可能消去机制。
