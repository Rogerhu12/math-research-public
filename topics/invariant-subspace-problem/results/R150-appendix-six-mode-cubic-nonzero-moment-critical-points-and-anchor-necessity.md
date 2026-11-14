# R150 附录：六个非零三次矩临界点与匹配锚的两个必要二次条件

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明。** 本稿构造原完整六模式 $F^3$ 的六个精确标量临界点；它们的一次矩非零，普通三次矩也非零。三点支撑在 $W_+$，另三点支撑在 $W_-$。六点合起来强迫：若某个匹配 Bell $S_r$ 的任何正自然幂属于原全局 Jacobian 理想，则 $r$ 必须同时满足原两个平面的二次条件。

因此，非零三次矩的临界点确实存在；不能把整个全局临界集化为 $T_3=0$ 的情形。两个二次条件仍只是必要条件，没有由本稿变成全局充分条件。

## 1. 要证明的必要条件

保持[完整第三矩 Schur 消元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)的原 $33$ 变量多项式 $\mathcal Q_3(y,H,V)$、原 $17$ 变量 $R_3$、匹配 $S_r$ 及其 Schur 剩余 $B_r$。令
$$
\mathcal J=(\nabla\mathcal Q_3)
\subseteq\mathbb C[y_0,\ldots,y_5,H_0,\ldots,H_{10},V_0,\ldots,V_{15}].
$$
仍用[两等向三平面](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md)的嵌入 $E_\pm:\mathbb C^3\to\mathbb C^6$，并记
$$
q_\pm(r)=Q_\pm(E_\pm^{\mathsf T}r).
\tag{1.1}
$$

**定理。** 对任意 $r\in\mathbb C^6$、任意正整数 $N$，
$$
\boxed{
S_r^N\in\mathcal J
\quad\Longrightarrow\quad
q_+(r)=q_-(r)=0.
}
\tag{1.2}
$$
经原 Schur 理想等价，同样有
$$
B_r^N\in(\nabla R_3)
\quad\Longrightarrow\quad q_+(r)=q_-(r)=0.
\tag{1.3}
$$
本定理只谈未局部化的完整多项式理想；不把一个在这些点消失的局部分母当成单位。

## 2. 两平面上的真实共同累积量支撑

用以下两个递推定义嵌入 $E_\pm$：前三项为任意 $(a_0,a_1,a_2)$，其余三项沿相应递推延长，
$$
\begin{array}{ll}
W_+:&
a_{n+3}=5a_{n+2}-\dfrac{32}{5}a_{n+1}+\dfrac85a_n,\\[2mm]
W_-:&
a_{n+3}=-27a_{n+2}-\dfrac{864}{5}a_{n+1}-\dfrac{864}{5}a_n.
\end{array}
\tag{2.1}
$$
对应三次多项式为
$$
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,\qquad
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
$$
其已付精确恒等式为
$$
E_\pm^{\mathsf T}KE_\pm=0,\qquad
E_\pm^{\mathsf T}Kv(z)=P_\pm(z)\psi_\pm(z),
\qquad Q_\pm(\psi_\pm(z))=0.
\tag{2.2}
$$
两个不可约二次式的矩阵分别为
$$
C_+=
\begin{pmatrix}
279&121&608\\
121&-521&-608\\
608&-608&-1024
\end{pmatrix},
\qquad
C_-=
\begin{pmatrix}
-1769&1369&5024\\
1369&-969&-5024\\
5024&-5024&-1024
\end{pmatrix},
\tag{2.3}
$$
即 $Q_\pm(u)=u^{\mathsf T}C_\pm u$。两矩阵行列式都等于 $163840000$。

在每个符号下，要求一次序列 $y_i$、二阶序列 $H_m$、三阶序列 $V_n$ 都满足该同一个递推。这样不只是 $y\in W_\pm$：全部前三级累积量张量都真正支撑在 $W_\pm$。

具体地，若 $H^\circ=(H_{i+j})_{0\le i,j\le2}$，递推逐个指标延长给
$$
H=E_\pm H^\circ E_\pm^{\mathsf T};
$$
同理，三阶张量满足
$$
V_{i+j+k}
=\sum_{a,b,c=0}^2
(E_\pm)_{ia}(E_\pm)_{jb}(E_\pm)_{kc}\,V_{a+b+c}.
\tag{2.4}
$$
所以令其余更高累积量为零后，对应有限普通矩泛函 $\Lambda$ 的整个支撑也在 $W_\pm$。

在前三坐标中，其普通三次矩为
$$
\mathsf T(u)
=(y_0u_0+y_1u_1+y_2u_2)^3
-6(y_0u_0+y_1u_1+y_2u_2)
\sum_{i,j=0}^2H_{i+j}u_i u_j
+4\sum_{i,j,k=0}^2V_{i+j+k}u_i u_j u_k.
\tag{2.5}
$$
如果
$$
\mathsf T=Q_\pm L
\tag{2.6}
$$
对某一次式 $L$ 成立，那么这是一个**完整**临界点。理由如下：

- 六个一次梯度是 $3\Lambda[F_0^2(Kx)_i]$，由于 $F_0|_{W_\pm}=0$ 而全部为零。
- 十一个二阶物理梯度的生成多项式是 $-6\Lambda[F_0(v(z)^{\mathsf T}Kx)^2]$，同理为零。
- 十六个三阶物理梯度的生成多项式是
  $4\,\mathsf T(E_\pm^{\mathsf T}Kv(z))
  =4P_\pm(z)^3 Q_\pm(\psi_\pm(z))L(\psi_\pm(z))=0$。

这同时付清了全部 $33$ 个原条件，没有仅从最高梯度消失推断完整临界性。

## 3. 六个点的精确有限坐标

对正平面，令 $\theta$ 遍历三次多项式
$$
f_+(\theta)=
21488509950\theta^3+51639754895\theta^2
-8624859280\theta-22475476032
\tag{3.1}
$$
的三个根。对负平面，令 $\theta$ 遍历
$$
f_-(\theta)=
67253624923350\theta^3+3026156669239635\theta^2
+40085972603282880\theta+165348799195327488
\tag{3.2}
$$
的三个根。

每个点的一次矩头部都是
$$
(y_0,y_1,y_2)=(1,0,\theta).
\tag{3.3}
$$
二阶头 $(H_0,H_1,H_2)$、三阶头 $(V_0,V_1,V_2)$ 以及一次余因子
$$
L_\pm(u;\theta)=
\lambda_{\pm,0}(\theta)u_0+
\lambda_{\pm,1}(\theta)u_1+
\lambda_{\pm,2}(\theta)u_2
\tag{3.4}
$$
均为 $\theta$ 的二次多项式，具有确定有理系数。全部系数保存在
[精确坐标数据](../notes/2026-11-13-six-mode-cubic-nonzero-moment-anchor-necessity-data.json)
中；每个长度为三的数组按 $1,\theta,\theta^2$ 排列。其余 $y,H,V$ 只按 (2.1) 延长，不引入新的参数或待解条件。

这些坐标是在两个明确的有限代数
$$
\mathbb Q[\theta]/(f_\pm)
\tag{3.5}
$$
中给出的。对每一组，[精确验证器](../notes/2026-11-13-six-mode-cubic-nonzero-moment-anchor-necessity-verify.py)以有理数运算完成：

1. (2.6) 的全部 $27$ 个有序三阶张量坐标等式；
2. 原 Schur $R_3$ 的值及全部 $17$ 个梯度均为零；
3. 原 $16$ 个三阶条件 $J_3^{-1}\ell+4V=0$。

第3项等价于原三阶梯度 $4\ell+16J_3V=0$，因为原 $J_3$ 的准确行列式非零。在该截面上，另外十七个原梯度与 $\nabla R_3$ 一致。所以直接原矩阵核算与第2节的支撑论证得到同一个完整结论。

这些消失是 (3.5) 中的特征零恒等式，因而对 $f_\pm$ 的每个复根都成立。没有用有限域的零值替代特征零恒等式。

## 4. 三个余因子确实张成全部一次式

写
$$
\lambda_{\pm,i}(\theta)
=m_{\pm,i0}+m_{\pm,i1}\theta+m_{\pm,i2}\theta^2,
$$
令 $M_\pm=(m_{\pm,ij})_{0\le i,j\le2}$。所有系数的分母都与 $103$ 互素。准确非零性见证为
$$
M_+\equiv
\begin{pmatrix}
91&80&20\\13&6&89\\54&85&76
\end{pmatrix},
\qquad
\boxed{\det M_+\equiv33\pmod{103}\ne0,}
\tag{4.1}
$$
$$
M_-\equiv
\begin{pmatrix}
22&96&66\\59&47&98\\21&39&17
\end{pmatrix},
\qquad
\boxed{\det M_-\equiv61\pmod{103}\ne0.}
\tag{4.2}
$$
因此两个原有理矩阵均可逆。

把 (3.1)、(3.2) 规范成首一式，其模 $103$ 分别为
$$
\bar f_+=\theta^3+96\theta^2+11\theta+97,\qquad
\bar f_-=\theta^3+36\theta^2+38\theta+24.
\tag{4.3}
$$
验证器直接计算二者的三次判别式均非零。因此两个特征零三次式各有三个不同复根。

若 $\theta_1,\theta_2,\theta_3$ 是其中一组三根，其三个一次式的系数矩阵是对应 Vandermonde 矩阵与 $M_\pm^{\mathsf T}$ 的乘积。两因子都可逆，故
$$
\boxed{
\operatorname{span}_{\mathbb C}
\{L_\pm(\,\cdot\,;\theta_1),
L_\pm(\,\cdot\,;\theta_2),
L_\pm(\,\cdot\,;\theta_3)\}
=(\mathbb C^3)^*.
}
\tag{4.4}
$$

另外，$M_\pm(1,\theta,\theta^2)^{\mathsf T}\ne0$ 对每个 $\theta$ 都成立，所以六个点各自的 $L_\pm$ 都非零。由 $Q_\pm\ne0$，其普通三次矩 $Q_\pm L_\pm$ 全部非零。它们的本质变量数恰为三：若非零方向导数湮灭 $QL$，由不可约 $Q$ 与一次 $L$ 互素，必先湮灭 $Q$；非退化 $Q$ 又迫该方向为零。

## 5. 必要条件的证明

假设 $S_r^N\in\mathcal J$。在第3节的任一个完整临界点，理想中每个元素都取零，所以
$$
S_r=0.
$$
固定一个符号，置 $u=E_\pm^{\mathsf T}r$。这组三个点的匹配 Bell 值准确为
$$
S_r=Q_\pm(u)\,L_\pm(u;\theta_j),
\qquad j=1,2,3.
\tag{5.1}
$$
若 $Q_\pm(u)\ne0$，三个值全为零就迫
$L_\pm(u;\theta_j)=0$ 对所有 $j$ 成立。由 (4.4)，必有 $u=0$，与 $Q_\pm(u)\ne0$ 矛盾。因此 $Q_\pm(u)=0$。对两个符号分别应用，得到 (1.2)。

事实上，仅就这六个已构造点而言，
$$
S_r\text{ 在六点全为零}
\quad\Longleftrightarrow\quad q_+(r)=q_-(r)=0.
\tag{5.2}
$$
反向直接来自 (5.1)。但 (5.2) 不是在整个未知临界集上的等价。

例如 $r=e_0$ 有
$$
q_+(e_0)=279,\qquad q_-(e_0)=-1769.
$$
因此该方向的任何正自然幂都不可能属于原全局 Jacobian 理想。这只排除该类标量单锚证书，不是对实际算子循环性的否定。

## 6. 与原候选和真实逆接口的关系

原平方精确证明选出的三个
$$
r=(A,B,0,0,0,1)
$$
满足两个二次条件，所以本稿没有排除它们。现在这两个条件已被真正的立方非零矩临界点证明为必要条件，不能只视为来自平方的附带选择。

最高物理导数方向 $r=Kv(z)$ 也自动满足这两个二次条件，且其 $S_r$ 本身就是完整梯度的线性组合。但[原曲线 first 的完整谱障碍](../notes/2026-11-13-six-consecutive-log-modes-curve-spectrum-and-single-layer-pure-power-obstruction-1cf.md)已经证明，原有限及无穷曲线方向的真实 first 都有整个复平面的谱和近似点谱。固定对角实化只运输这些方向；不能把该代数归属换成所需的空谱 first / Bell 有界逆。

原三个有实际逆的候选在 Gaussian 点的准确局部指数已经是四；本稿没有给出它们在所有其他临界点上的消失或统一全局第四次归属。非零三次矩的其他三维投影类型、四至六个本质变量的临界点以及局部厚度仍须继续处理。
