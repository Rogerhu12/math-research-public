# R83：全层 Witt 鬼分量与实际两步整格

日期：2026-11-12。状态：全部恒等式和精度界已根端独审。
完整证明见[实际全层 Witt 笔记](../notes/2026-11-12-full-witt-ghosts-and-actual-cm-halflines.md)。

## 1. 深鬼层的有限精度模型

对原来的两个归一单位 $R\in1+Z\mathcal O[[t,Z]]$ 分别取唯一整展开

$$
R=\prod_{n\ge1}(1-w_nZ^n)^{-1},\qquad
\lambda_{R,r}=p^r[Z^{p^r}]\log R
=\sum_{j=0}^rp^jw_{p^j}^{p^{r-j}}.
$$

构造 $w_n$ 不需除法，故全部坐标整。
模 $p^s$ 只需 $j\le\min(r,s-1)$；其 $t^D$ 截断只需同阶的
$w_{p^j}$，绝对精度 $p^{s-j}$。
所需原单位的纤维次数至多 $p^{\min(r,s-1)}$。
这控制了深度与精度的关系，没有把随精度增长的输入说成固定维数。
两个单位完成各自的乘法 Witt 展开后，才作实际偶、奇线性组合。

## 2. 每一层的准确半线交换

取 $\Phi(t,Z)=(t^p,Z^p)$ 并包含系数 Frobenius，
$B_R=p^{-1}\log(\Phi(R)/R^p)$ 整。
准确有

$$
\lambda_{R,r}=\phi_t\lambda_{R,r-1}-p^r[Z^{p^r}]B_R.
$$

对实际 $h_e,h_o$，记 $\Lambda_{\bullet,r}=p^r[Z^{p^r}]h_\bullet$，
$b_{\bullet,r}=[Z^{p^r}]B_\bullet$，以及
$A=\left(\begin{smallmatrix}0&c_e/c_o^\sigma\\c_o/c_e^\sigma&0\end{smallmatrix}\right)$。
则

$$
\Lambda_r=A\phi_t\Lambda_{r-1}-p^rb_r,
\qquad
\Lambda_r=A A^\sigma\phi_t^2\Lambda_{r-2}
-p^{r-1}A\phi_t b_{r-1}-p^rb_r.
$$

两步余项直接落在 $p^{r-1}$；迭代两次不自动多给一个 $p$。
R82另已核定此处 $A A^\sigma=I$，但这不消去显示的整格代价。

## 3. 全层模参数首项非零，指定中央投影仍待约束

对 $r\ge1$，令 $z=\int\omega$，$a_r=p^r[Z^{p^r}]z$，
$\mathsf H_p=a_1\bmod p=h_pt+O(t^3)$，$h_p$ 为单位。
Cartier 迭代准确给 $a_r\equiv\mathsf H_p^{q_r}$，
$q_r=(p^r-1)/(p-1)$。
因此实际去不变微分余项

$$
W_{e,r}=p^r[Z^{p^r}](h_e-M_ez)
\equiv\eta_r M_{\epsilon_r}(t^{p^r})-\mathsf H_p^{q_r}M_e
\pmod p,
$$

其中奇层取 $\epsilon_r=o$、偶层取 $e$，规范标量
$\eta_r=c_e/c_{\epsilon_r}^{\sigma^r}$ 全部保留。
由 $M_e=t^4+\cdots$、$M_o=t+\cdots$ 及 $q_r+4<p^r$，得

$$
\operatorname{ord}_t(W_{e,r}\bmod p)=q_r+4,
\qquad [t^{q_r+4}]W_{e,r}\equiv-h_p^{q_r}\ne0.
$$

这说明每层实际函数都非零；模 $p$ 各层仍由第一层和 Cartier 决定。
指定中央行另含真实 GM 权重，R78 的首层单位相消依然存在。
应以此整格代入完整 Hecke/isogeny 关系，约束 R77/R81 的中央深度证书；
本结论没有证明无穷素数命中。
