# R150 附录：四重支点的二次关系只有两处，满秩外均值临界截面全部排除

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 原长度四物理支撑若为单个四重支点，则其物理投影存在非零二次关系，当且仅当支点是 $0$ 或 $\infty$；两处关系空间都恰为一维。两处的原极化接触阶又与完整临界点的最高三阶矩恒等式矛盾。因此，在 mean 的 $4\times3$ Hankel 矩阵秩三、$T_3$ 本质维数三、mean 在该本质空间之外且 $H$ 秩四的原临界截面中，**共同支撑不可能是四重支点**。本文不把该结论外推到 $H$ 降秩或其他重数分拆。

## 1. 使用的原对象与必要条件

沿用[原四次支撑矩阵](R150-appendix-quartic-support-quadric-pencil-and-codimension-two.md)的固定记号：
$$
L_g=\begin{pmatrix}g_0&g_1&g_2&g_3&g_4&0\\
0&g_0&g_1&g_2&g_3&g_4\end{pmatrix},\qquad E_g=\ker L_g,
$$
$$
\mathcal M(g)=\bigl[(Q_{ij}b_0,Q_{ij}b_1)^{\mathsf T}\bigr]_{0\le i<j\le4},
\quad (b_0,b_1)=3200K^{-1}L_g^{\mathsf T}.
\tag{1.1}
$$
原曲线的十个二次关系按字典序排列，满足
$$
x^{\mathsf T}Q_{ij}x=2(x_ix_{j+1}-x_{i+1}x_j).
$$
已证明 $E_g$ 的物理投影有非零二次关系，准确等价于 $\operatorname{rank}\mathcal M(g)<10$。

由[共同四 jets 归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)与[完整低梯度](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)，本文临界截面具有唯一长度四支撑 $g$，$H$ 秩四，且原物理投影必有非零二次关系。此外有泛函 $\lambda$ 满足
$$
H=2V\lambda,\qquad y=8V\lambda\lambda,
\tag{1.2}
$$
以及最高原梯度恒等式
$$
T_3(Kv(z))=(y^{\mathsf T}Kv(z))^3
 -6(y^{\mathsf T}Kv(z))\,H(Kv(z),Kv(z))
 +4V(Kv(z),Kv(z),Kv(z))\equiv0.
\tag{1.3}
$$
以下只使用这些已经证明的必要条件。

## 2. 四重支点降秩的完整一元判定

有限支点 $s$ 对应
$$
g_s(z)=(z-s)^4,\qquad
(g_0,g_1,g_2,g_3,g_4)=(s^4,-4s^3,6s^2,-4s,1).
\tag{2.1}
$$
令 $\Delta_1$、$\Delta_2$ 分别为 $\mathcal M(g_s)$ 删除零起始行 $(10,11)$、$(8,9)$ 的十阶子式。精确的整数恒等式为
$$
\begin{aligned}
\Delta_1(s)&=67108864000000000\,s^7 A(s),&\deg A&=30,\\
\Delta_2(s)&=20971520000000000\,s^6 B(s),&\deg B&=28.
\end{aligned}
\tag{2.2}
$$
完整整数系数保存于[可执行证明证书](../notes/2026-11-13-quadruple-jet-critical-exclusion-verify.py)及[精确输出](../notes/2026-11-13-quadruple-jet-critical-exclusion-certificate.json)。两多项式的最高系数分别是 $1125000$、$8203125$，模 $103$ 后为 $34$、$102$，均保持完整次数。按常数项在前的次序，有限域 Bézout 系数如下：
$$
\begin{aligned}
U={}&(49,102,23,76,36,101,88,13,89,77,30,63,86,90,\\
 &47,14,95,4,99,29,101,83,88,0,15,4,91,49),\\
W={}&(80,30,47,68,95,30,15,73,89,102,23,20,95,97,52,\\
 &35,86,13,22,20,58,31,97,86,101,42,24,88,96,18),
\end{aligned}
$$
且逐系数准确满足
$$
\boxed{U\bar A+W\bar B=1\quad\text{于 }\mathbb F_{103}[s].}
\tag{2.3}
$$
由于两个完整次数都保留，Gauss 引理使 (2.3) 排除任何特征零的共同非恒定因子；因此 $A,B$ 在 $\mathbb C[s]$ 互素。若 $s\ne0$，(2.2) 的两个子式不能同时为零。这已经排除了所有有限非零支点，不需要从数值采样猜测降秩集。

(2.2) 本身如何由有限证书建立也没有省略。每个矩阵条目是 $s$ 的至多四次式，故十阶行列式次数至多四十。验证器从原 $K$ 及其精确有理逆重建整个矩阵，在 $s=0,1,\ldots,40$ 的四十一个不同整数处，以整数 Bareiss 消元验证两个等式。等式两边次数均不超过四十，因此这些精确等值证明整个多项式恒等式。随后独立进行 (2.3) 的有限多项式乘加。

在 $s=0$ 与 $s=\infty$，分别取 $g=z^4$ 与齐次四次式 $g=a^4$（仿射系数 $(1,0,0,0,0)$）。准确的非零核向量依次为
$$
\begin{aligned}
n_0&=(0,0,0,0,11664,-5400,1080,-1755,135,100),\\
n_\infty&=(80,-16,20,0,-36,20,0,5,0,0).
\end{aligned}
\tag{2.4}
$$
证书逐整数核验 $\mathcal M(g)n=0$；同时两矩阵模 $103$ 的秩都为九。因此在特征零也恰为九，而不只是至多九。至此得到准确的射影集合等式
$$
\boxed{\{s\in\mathbb P^1:\ E_{4s}\text{ 的物理投影有二次关系}\}
       =\{0,\infty\}.}
\tag{2.5}
$$

## 3. 满秩收缩迫 mean 的最高 jet 系数非零

在任一支点的局部坐标 $t$ 中，把齐次曲线写成
$$
u(t)=u_0+u_1t+u_2t^2+u_3t^3+\cdots.
$$
长度四支撑的原三阶 Hankel 张量可唯一写为
$$
V=\sum_{j=0}^3 v_j [t^j]\nu(t)^{\otimes3}
 =\sum_{a+b+c\le3}v_{a+b+c}\,u_a\otimes u_b\otimes u_c.
\tag{3.1}
$$
这使用除以阶乘的 jet 系数，因此 (3.1) 中没有隐含的二项式归一化。令 $\lambda_j=\lambda(u_j)$。由 (1.2)，在 $u_0,\ldots,u_3$ 基下
$$
H_{ab}=2\sum_{c=0}^{3-a-b}v_{a+b+c}\lambda_c
\quad(a+b\le3),\qquad H_{ab}=0\quad(a+b>3).
\tag{3.2}
$$
其反对角线全是 $2v_3\lambda_0$，故
$$
\det H=(2v_3\lambda_0)^4.
$$
$H$ 秩四遂迫 $v_3\lambda_0\ne0$。再收缩一次，mean 的最高 jet 系数准确是
$$
\boxed{y_3=8v_3\lambda_0^2\ne0.}
\tag{3.3}
$$
这是原满秩条件给出的非零项；没有另行假设一个一般位置的 mean。

## 4. 两个剩余支点都违反最高梯度

令 $p_j(z)=u_j^{\mathsf T}Kv(z)$，并在支点附近使用同一个局部坐标。

在 $s=0$，$u_j=e_j$，原核给
$$
\begin{aligned}
p_0&=5z^4-z^5,\\
p_1&=-32z^3+5z^4-z^5,\\
p_2&=54z^2-4z^3+5z^4,\\
p_3&=-32z-4z^2-8z^3.
\end{aligned}
\tag{4.1}
$$
故四个消失阶准确为 $(4,3,2,1)$。在 $s=\infty$，取 $v_{\rm hom}(t,1)=(t^5,t^4,t^3,t^2,t,1)$，$u_j=e_{5-j}$，四个极线为
$$
\begin{aligned}
p_0&=-t^4-t^5,\\
p_1&=5t^3+5t^4+5t^5,\\
p_2&=-8t^2-4t^3-32t^4,\\
p_3&=5t-4t^2+54t^3,
\end{aligned}
\tag{4.2}
$$
消失阶同样准确为 $(4,3,2,1)$。

在任一处，由 (3.3) 可知 $y^{\mathsf T}Kv=\sum y_jp_j$ 的消失阶恰为一。由 (3.2)，$H(Kv,Kv)$ 只含 $a+b\le3$ 的乘积 $p_ap_b$，每项消失阶至少 $8-a-b\ge5$。由 (3.1)，$V(Kv,Kv,Kv)$ 只含 $a+b+c\le3$ 的乘积，每项消失阶至少 $12-a-b-c\ge9$。所以 (1.3) 的三项消失阶依次是
$$
3,\qquad \ge6,\qquad \ge9.
$$
第一项的三阶系数由 (3.3)、(4.1) 或 (4.2) 保证非零，其他两项无法抵消。与最高完整梯度恒等式矛盾。$\square$

## 5. 本次推进的准确范围

四重支点 $4s$ 现在已从本文满秩、外 mean、非 secant、$T_3$ 本质三维的完整临界截面中全部删除。配合[四个不同支点有基点的排除](R150-appendix-reduced-four-point-basepoint-critical-section-is-empty.md)，剩余共同支撑还包括无基点的四个不同支点，以及重数分拆 $3+1$、$2+2$、$2+1+1$ 中仍符合原二次关系与完整梯度的情况。

本文没有处理 $H$ 降秩、mean 的 Hankel 秩降落、$T_3$ 本质维数四至六，也未给全局自然幂的 Jacobian 成员关系或实际 Bell 算子逆。普通复 Hilbert 空间 ISP 仍未完成。
