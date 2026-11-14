# R134. 实际 AS 两矩与去 p Coleman 完整迹

日期：2026-11-12。**已证明的有限比较；无穷非零性仍开。**

完整证明见[实际 Artin–Schreier 两矩与 Coleman 类群迹](../notes/2026-11-12-actual-artin-schreier-moments-and-depleted-coleman-trace.md)。

R130 的原点可直接使用延拓后的
$z_Q=\log_E Q/p\in\ker N_\Gamma$：约化群无 $p$ 挠点，
故用 $p$ 单位倍延拓 log 后，这一次除 $p$ 确实整。

当 $p$ 在 $F$ 分裂且 $s=\operatorname{Art}_p=\tau^h\ne1$，
取 $\upsilon^p-\upsilon=h$ 于 $\mathbb F_{p^p}$。令
$$
 T_1=\operatorname{Tr}(\upsilon z_Q),\qquad
 T_2=\operatorname{Tr}(\upsilon^2z_Q).
$$
则
$$
 \mathcal D_2z_Q=\tfrac12(T_2-(2\upsilon+1)T_1),
\qquad \mathcal D_2z_Q\ne0\Longleftrightarrow(T_1,T_2)\ne0.
$$
两 $p$ 位按真实复共轭给 $(T_1,T_2)$ 与 $(T_1,-T_2)$。
完全分裂块则以实际共轭值 $z_j$ 取
$A_1=\sum jz_j,A_2=\sum j^2z_j$；其所有分量为
$\tfrac12(A_2-(2r+1)A_1)$。若 $F$ 在 $p$ 惰性，
$A_1^p=A_1,A_2^p=-A_2$，仍保留两个准确的 $\mathbb F_p$ 标量。
R130 的 formalizer 在这两矩上只乘一个共同单位。

在 **源 CM 域 $F$ 在 $p$ 分裂** 时，BDP 的实际 canonical
CM 商给原 Coleman 原函数 $G=\log_E\pi$ 的
$$
G^{[p]}=(1-a_pV/p+V^2/p)G.
$$
取原 $Q=\operatorname{Tr}_{H/L}\pi(x_\ell)$ 的完整类群迹，准确为
$$
\eta_{p,\ell}=\sum_{u\in\operatorname{Gal}(H/L)}G^{[p]}(x_\ell^u)
              =(p-a_ps+s^2)z_Q.
$$
其前两矩由可逆矩阵
$$
 \begin{pmatrix}1-a_p&0\\-2h(2-a_p)&1-a_p\end{pmatrix}
$$
与原两矩比较。没有类数因子、额外 $\delta$ 损失或被略去的
$p$ 分母；目标 $E$ 可以超奇异。

去 $p$ 原函数的约化有真正全局表达
$$
 g_p=\Theta^{p-2}\bar f_\pi/\mathrm{Ha}^p.
$$
在固定细模曲线上它只于超奇异点有阶至多 $p$ 的极点，
至少一处阶正好为 $p$，所以
$g_p\notin(\operatorname{Frob}-1)^2\overline{\mathbb F}_p(X)$。

这一全局障碍尚未与原 CM 轨道的两矩共同消失建立充分联系。
该轨道先作指定 prime-to-$p$ 全迹，其总 trace 已因
$a_\ell(E)=0$ 恒零；它不是任意闭点族。不能直接用一般
Chebotarev 或将本式认作既有 $\mathbb Q(i)$ 中央 $J'_p$。
原两矩在无穷实际输入中的非零性仍未证明。
