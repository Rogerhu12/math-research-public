# R150 附录：当前无穷远187维二次头线性倍注入与1632个标准Koszul来源独立

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

**新结论：** 直接在当前物理无穷远的原17式上，17个二次头乘以11个变量得到的187列，在 $\mathbb F_{31}$ 与 $\mathbb Q$ 上都线性独立。因此136个原标准Koszul关系及其1496个一次变量倍，作为原6188来源向量，在这两个域上均组成一个1632维真核子空间。这不是将有限物理参数处的泛秩外推至无穷远。

## 1. 同一原输入与实际187阶子式

写原17式为
$$
f_i=L_i+Q_i,\qquad 0\le i\le16,
$$
其中 $L_i$ 为线性部分，$Q_i$ 为齐次二次部分。输入仍是同一17×77整数模型：87459 B，SHA256 为
97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074。

考虑完整线性映射
$$
\mu:k^{17}\otimes k[m_0,\ldots,m_{10}]_1
\longrightarrow k[m_0,\ldots,m_{10}]_3,\qquad
(\ell_i)_{i=0}^{16}\longmapsto\sum_{i=0}^{16}\ell_iQ_i.
$$
其原整数矩阵为286×187。列的零基编号为 $11i+j$，对应 $m_jQ_i$；行依 $m_a m_b m_c$、$0\le a\le b\le c\le10$ 的字典序排列。

[实际小回执](../notes/2026-11-15-r150-infinity-quadratic-linear-multiples187-789f.json)保存187个升序原行号及全部187列。该精确整数子式模31的行列式为28，故非零。于是
$$
\operatorname{rank}_{\mathbb F_{31}}\mu
=\operatorname{rank}_{\mathbb Q}\mu
=187.
\tag{1.1}
$$
特别地，17个二次头自身也独立：若 $\sum a_iQ_i=0$，再乘以任一变量就与式(1.1)的注入性矛盾。

本次是[小源码](../notes/2026-11-15-r150-infinity-quadratic-linear-multiples187-789f.mjs)的纯 analyze 函数在 functions.exec V8 环境中的实际精确模运算，完整选行和直接子式复核共0.151秒。Node CLI 是同函数的可复现包装，未声称它已经在 Actions 执行。没有重算大正常形、来源 DAG 或任何 Dixon 位。

## 2. 原标准Koszul族的精确来源

令 $e_i$ 表示原第 $i$ 个方程的来源方向。对每一对 $0\le i<j\le16$，取
$$
s_{ij}=f_j e_i-f_i e_j.
$$
再将每个 $s_{ij}$ 分别乘以
$$
1,m_0,\ldots,m_{10}.
$$
所得来源多项式次数至多3，恰可装入原6188个来源坐标；不增加任何新方程或新来源。每个向量的原多项式乘积严格恒为零，因为
$$
f_i f_j-f_j f_i=0.
$$
总数为
$$
\binom{17}{2}(1+11)=136\cdot12=1632.
$$

这些零身份在整数中成立。它们覆盖全部4367个原输出，不仅覆盖某个所选4354输出方阵。

## 3. 为什么这1632个来源确实独立

取 $k=\mathbb F_{31}$ 或 $\mathbb Q$。给上述族一个 $k$ 线性组合，等价于给一个17×17斜对称矩阵
$$
C(m)=C^{(0)}+C^{(1)}(m)
$$
以来源向量
$$
r_i=\sum_j C_{ij}(m)f_j.
$$
这里 $C^{(0)}$ 的项为常数，$C^{(1)}$ 的项为齐次一次多项式。

假设该来源向量本身为零，即每个 $r_i$ 都是零多项式。比较每个分量的三次齐次部分，得到
$$
\sum_j C^{(1)}_{ij}(m)Q_j=0.
$$
由式(1.1)，每个 $C^{(1)}_{ij}$ 都为零。再比较二次部分，得
$$
\sum_j C^{(0)}_{ij}Q_j=0.
$$
17个二次头独立又迫全部 $C^{(0)}_{ij}=0$。故原1632个来源向量独立。

令其来源矩阵为
$$
\Phi\in\mathbb Z^{6188\times1632}.
$$
现在已经严格证明
$$
A_\infty\Phi=0,\qquad
\operatorname{rank}_{\mathbb F_{31}}\Phi
=\operatorname{rank}_{\mathbb Q}\Phi
=1632.
\tag{3.1}
$$
这是一条实际当前无穷远、原方程缩放和原来源字典中的结论。

## 4. 同一4354来源支持的下一精确小接口

令 $J$ 为当前选定的4354个原来源编号；其补集有1834个编号。取
$$
\Phi_{\rm out}=\Phi_{J^c,*}\in\mathbb Z^{1834\times1632}.
$$
则
$$
\Phi\bigl(\ker_k\Phi_{\rm out}\bigr)
=\operatorname{im}_k\Phi\cap k^J,
$$
而式(3.1)的注入性给出
$$
\dim_k\bigl(\operatorname{im}_k\Phi\cap k^J\bigr)
=1632-\operatorname{rank}_k\Phi_{\rm out}.
\tag{4.1}
$$
因此若后继实际算得 $\operatorname{rank}_{\mathbb F_{31}}\Phi_{\rm out}=r$，即可得到准确的特征零上界
$$
\dim_{\mathbb Q}\bigl(\operatorname{im}_{\mathbb Q}\Phi\cap\mathbb Q^J\bigr)
\le1632-r.
$$

这个小接口只测试标准Koszul真来源中哪些能保持当前选列支持。它不把 $\mathbb F_{31}$ 的外支持核直接当作 $\mathbb Q$ 组合，也不预判该上界是否达到。若要把现有23个真核归入这个标准Koszul空间，还需实际原来源表示；只有维数或模31成员关系不够。

本篇尚未计算 $\Phi_{\rm out}$ 的秩，没有重做任何所选大矩阵消元，也没有据1632个原真核宣称所选无穷远秩已经闭合。
