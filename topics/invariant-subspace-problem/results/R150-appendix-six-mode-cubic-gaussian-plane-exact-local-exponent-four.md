# R150 附录：六模式立方 Gaussian 平面的准确局部指数为四

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明。** 在前稿的正等向平面 Gaussian 点 $p_+$，所有匹配 $B_r$ 均有第四次自然幂属于完整局部梯度理想。原三个已付 first 逆的方向同时满足第三次不属于，因此其最小局部自然幂准确为四。本稿把前稿的上界五降为四；全部结论仍限定在这个标量局部环。

## 1. 原点、局部环与已经付清的归约

沿用[Gaussian 平面完整局部证明](R150-appendix-six-mode-cubic-gaussian-plane-local-nilpotence-and-cube-obstruction.md)的原 $R_3$、$B_r$ 及点
$$
y=0,\qquad (H_0,H_1,H_2)=(1,0,0),\qquad
H_{n+3}=5H_{n+2}-\frac{32}{5}H_{n+1}+\frac85H_n.
$$
令
$$
\mathcal O=\mathbb C[y,H]_{\mathfrak m_{p_+}},\qquad
I=(\nabla R_3)\mathcal O.
$$
图参数为 $T=(H_0,H_1,H_2)$；保留 $u=y_4,v=y_5$，其余十二个横向坐标为
$$
q=(y_0,y_1,y_2,y_3,H_3-h_3(T),\ldots,H_{10}-h_{10}(T)).
$$
记 $f=R_3$，$g=\partial_qf$，并置
$$
\mathcal A=\mathcal O/(g),\qquad
\mathfrak a=(u,v)\mathcal A,\qquad
\bar I=I\mathcal A.
$$

前稿已经在普通局部化中证明：

1. 十二阶块 $M=\partial_qg$ 为可逆矩阵块，其基点行列式模 $103$ 为 $81$。
2. 每个 $B_r$ 在整个三参数图上为零，且 $\overline{B_r}\in\mathfrak a$。
3. 沿整个图的 Hessian 恒等式与偶性给 $\bar f\in\mathfrak a^4$。写其四次首项为 $F_4(T;u,v)$。
4. 原三个方向的 $B_r^3\notin I$，其证明已通过保留全部十七个梯度的 Artin 商完成。

本稿只增加第四次层的完整梯度信息，不更换目标、自然幂或物理矩键。

## 2. 必须保留的三个图参数梯度

令 $b_{j,n}$ 是序列 $h_n(T)$ 中 $T_j$ 的系数，即
$$
b_{j,n}=h_n(e_j),\qquad 0\le j\le2,\quad 0\le n\le10.
$$
在上述 $T,u,v,q$ 坐标中，沿图参数的真实导数为
$$
\partial_{T_j}f
=\sum_{n=0}^{10}b_{j,n}\,\partial_{H_n}R_3.
\tag{2.1}
$$
所以它们确实是原完整梯度的线性组合。

定义保持 $(g)$ 的局部有理导子
$$
D_{T_j}
=\partial_{T_j}
-(\partial_qg)^{-1}(\partial_{T_j}g)\cdot\partial_q.
\tag{2.2}
$$
它满足 $D_{T_j}g=0$，并保持 $u,v$ 不变。与前稿的 $D_u,D_v$ 一样，
$$
D_{T_j}\bar f\in\bar I.
$$
由于 $\bar f\in\mathfrak a^4$ 是沿整个参数图成立的结论，而非单个参数值处的消失，
$$
D_{T_j}\bar f
 = E_j(T;u,v)\pmod{\mathfrak a^5},
\qquad
E_j=\partial_{T_j}F_4.
\tag{2.3}
$$
这三个四次式不能从完整理想中删去。

## 3. 四次层的完整精确矩阵

使用[精确验证器](../notes/2026-11-13-six-mode-cubic-gaussian-plane-local-fourth-verify.py)，从原 $R_3$ 逐阶解十二个原始 $q$ 梯度至四次，随后计算全部十七个原始梯度。完整有理系数保存在[有限证书](../notes/2026-11-13-six-mode-cubic-gaussian-plane-local-fourth-certificate.json)。

计算使用五个自由方向
$$
(u,v)=(1,0),(0,1),(1,1),(1,-1),(1,2)
$$
的单参数射线。有限逐阶解在每一阶的系数均是 $(u,v)$ 的齐次多项式；五个方向唯一决定一个二元四次式，因此这是一项完整有限插值证书。十二个消去梯度均严格消失到四次；另三个图参数梯度消失到三次，而其四次项全部保留。

以下各行按 $(u^4,u^3v,u^2v^2,uv^3,v^4)$ 排列，使用原 $R_3$ 的实际有理规范，未重新乘任意常数。基点处准确有
$$
F_4\equiv(37,42,84,49,85)\pmod{103},
$$
$$
\begin{aligned}
E_0&\equiv(37,42,84,49,85),\\
E_1&\equiv(20,93,43,14,91),\\
E_2&\equiv(75,14,86,53,23)
\end{aligned}
\quad\pmod{103}.
\tag{3.1}
$$
这里 $E_0=F_4$ 也在特征零准确成立。所有相关有理分母均与 $103$ 互素。

将
$$
u\,\partial_uF_4,\quad
v\,\partial_uF_4,\quad
u\,\partial_vF_4,\quad
v\,\partial_vF_4,\quad E_1
$$
作为五行，得到五阶四次系数矩阵，其模 $103$ 为
$$
\mathsf C\equiv
\begin{pmatrix}
45&23&65&49&0\\
0&45&23&65&49\\
42&65&44&31&0\\
0&42&65&44&31\\
20&93&43&14&91
\end{pmatrix},
\qquad
\boxed{\det\mathsf C\equiv1\pmod{103}.}
\tag{3.2}
$$
因此原特征零行列式非零，在图参数的基点局部环中是单位。

也可看出第五行究竟增加了什么。前四行的有理左零泛函，规范到最后一个系数为一后，模 $103$ 为
$$
(89,11,22,71,1).
$$
它在 $(E_0,E_1,E_2)$ 上的值分别为
$$
(0,96,44)\pmod{103}.
\tag{3.3}
$$
所以完整参数梯度确实杀掉了只取两个横向三次梯度时剩余的四次层。式 (3.2) 本身已经给出所需的完整非零行列式证书。

## 4. 从四次首项到整个普通局部环

在 $\mathcal A$ 中，前四个真实理想元素为
$$
uD_u\bar f,\quad vD_u\bar f,\quad
uD_v\bar f,\quad vD_v\bar f,
$$
第五个为 $D_{T_1}\bar f$。它们都属于 $\bar I$，而四次首项正是 (3.2) 的五行。矩阵在参数局部环中可逆，故
$$
\mathfrak a^4\subseteq\bar I+\mathfrak a^5.
\tag{4.1}
$$

这已经可以结合前稿的 $\mathfrak a^5\subseteq\bar I$ 结束。为直接说明余项不需要任何形式无限级数，也可令 $L$ 为 $\mathfrak a^4$ 在 $\mathcal A/\bar I$ 中的像。它由五个四次单项式生成，(4.1) 给 $L=\mathfrak a L$。将五个生成元写成 $\ell=C\ell$，矩阵 $C$ 的条目均在局部极大理想中，因此 $\det(I-C)$ 为单位，乘伴随矩阵即得 $\ell=0$。于是
$$
\boxed{\mathfrak a^4\subseteq\bar I.}
\tag{4.2}
$$
该论证完全发生在原普通局部环，不把形式归属冒充局部化归属。

由 $\overline{B_r}\in\mathfrak a$，提回 $\mathcal O$ 得
$$
\boxed{B_r^4\in I\qquad\text{对每个 }r\in\mathbb C^6.}
\tag{4.3}
$$

## 5. 原三个方向的准确最小幂与边界

原三个方向仍为
$$
r=(A,B,0,0,0,1),\qquad
A=-\frac{521d^2-46784d+271360}{160(5d-704)},\qquad B=A+d,
$$
其中 $d$ 分别取
$$
3725d^3-43931504d^2+6080833024d+52565262336=0
$$
的三个实根。前稿已逐一证明 $B_r^3\notin I$；其线性部非零的准确三次代数范数模 $103$ 为 $57$。若更小正幂属于 $I$，乘足相应 $B_r$ 因子便使第三次也属于，矛盾。因此
$$
\boxed{
\min\{N\ge1:B_r^N\in I\}=4
\quad\text{对原三个方向分别成立。}
}
\tag{5.1}
$$

这比碰撞两原子点的准确局部指数三更大，说明不能仅根据一个临界分支的局部厚度选定全局自然幂。

本稿没有证明全局第四次归属，也没有为局部 Hessian 及四次系数矩阵的行列式支付实际有界交换逆。原 $F^3$ 的完整全局 Jacobian 证书与零参数循环性仍开放；后续的主要支撑风险是尚未覆盖的非零 $y$ 临界点。
