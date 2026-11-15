# R395：whole-E 与全自然通量共同核中的十一条独立内部门

日期：2026-11-15。**纸面来源核对与线性模块推论；没有执行新积分、消元、人工测试或研究计算。**

[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md) 在实际 whole-$E$ 与全自然通量零的前提下，仍保留内部部分通量。本稿证明这不是冗余保留：在 [R391](R391-analytic-simple-degeneracies-and-complete-selected-inverse-germs-on-the-rational-circle.md) 的同一实际 profiles 和原对应点上，已有十一维响应模块全部落在
$$
\ker(E,\Lambda_{\rm all}),
$$
但其至多十一个指定部分通量仍独立。于是总通量全零不能代替这些内部像条件。

这是**原成本空间中的实线性结论**，不是在固定旧几何上免费加入 signed 成本，也不宣 whole-$E$、全部 $\Lambda$ 与新通量已获实际联合实现。

## 1. 精确来源：十一列本身就在原响应层

[R345 §§1—4](R345-local-whole-E-kernel-orbit-and-eleven-corresponding-degenerate-fluxes.md) 使用
$$
P(a,b)=J(a''b''),\qquad S(a,b)=J(xa''b''),\qquad
\tau_S=[P,S]=-J(a''b''c''),
$$
$$
K_0=\frac13\mathcal B_P(\tau_S),\qquad
K_n=\delta^nK_0\quad(0\le n\le10).
\tag{1}
$$
其真实来源是
$$
\mathcal R_{71}=\mathcal B(E_8,W_{71})\subset\mathcal R.
$$
R247/R345 已付 $E_8,W_{71}$ 的原等变作用和 $\mathcal R_{71}$ 的闭合；所以每个(1)都是原完整响应的有限实线性组合。不要求整个 $\mathcal R$ 对 $\delta$ 闭合。

特别，不需将这些列解释为某个未核的正规 H 或 Abar 成本加响应：其正规商部分准确为零。R382 的完整 H 自然通量零可保留为另一结论，本稿不依赖它。

R345 已证明
$$
\mathscr K=\operatorname{span}\{K_0,\ldots,K_{10}\}\simeq V_{10},
\quad\dim\mathscr K=11,\quad
\mathscr K\subset\ker E,
\quad E=(\pi,\mathcal Q).
\tag{2}
$$
这些是 universal 完整成本身份。原 $\delta$ 作用于输出与全部输入，不是实际几何的免费非仿射变化。

## 2. 整个模块对全部自然读出为零

[R344(38)](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md) 及 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 给
$$
\Lambda_u|_{\mathcal R}=0
\quad\text{对每个实紧 }u.
$$
由(1)立即得到
$$
\boxed{\mathscr K\subset
\mathcal R_{71}\cap\ker E\cap\ker\Lambda_{\rm all}.}
\tag{3}
$$
全自然读出包括原 ordered Green 修正；没有把它一般地替换为裸 self 积分。

对此特定模块还可用 R345 的已付原式独立核对。对任意实紧 u，
$$
K_n(u^2,0)=-P_n(x,u,u',u'')/3,
$$
是完整局部紧输出，且 $\pi K_n=0$。原同 collar 分部积分给
$$
\Omega_u(\delta V)
=-D_u\Omega_u(V)[x^2u'-2xu],\qquad
\Omega_u(K_0)=-\frac13\int u'''(u'')^4=0.
\tag{4}
$$
因此所有 $\Omega_u(K_n)=0$。此时因为完整 $\pi K_n=0$，R352 才给 $\Lambda_u(K_n)=\Omega_u(K_n)$。这没有借用任何单包 primitive 左紧假设。

## 3. 同一 R391 圆上的真实部分通量仍满射

先固定 R391 的最后有限 N、全部纠正、宽度和实际副本。取一个最细包及其原点 $x_*$，满足
$$
A_u(x_*)=0,\qquad u'(x_*),u''(x_*)>0.
$$
R391 还使这个零点简单。按 R345 选择该点在 $m\le11$ 个不同完整副本中的对应点 $x_j$；这些是实际点，不是母近似或数值网格。其原幅度非零，且 $a^2-b^2\ne0$。

原查询在全部 U 上是
$$
\mathcal F_j(V)=
\int_{\ell_j}^{x_j}f'V(f^2,g)''
-\{f(x_j)-f(\ell_j)\}V(f^2,g)''(\ell_j).
\tag{5}
$$
平台项先保留。对(1)的完整局部输出它准确为零。

R345(18)—(20)已经证明(5)在 $K_0,\ldots,K_{m-1}$ 上的矩阵可逆，其真实共同副本幅为第五次，点位置与 $g$ 翻号均已计入。本文不重新计算那个 Vandermonde，也不由点数授秩。结合(3)得到新的共同核表述：
$$
\boxed{
(\mathcal F_1,\ldots,\mathcal F_m)
\bigl(\mathcal R_{71}\cap\ker E\cap\ker\Lambda_{\rm all}\bigr)
=\mathbb R^m,\qquad m\le11.
}
\tag{6}
$$
例如对每个 $1\le\ell\le m$，存在一个准确实线性组合
$L_\ell\in\operatorname{span}\{K_0,\ldots,K_{m-1}\}$，使
$$
E(L_\ell)=0,\quad
\Lambda_u(L_\ell)=0\ \text{对全部 }u,\quad
\mathcal F_j(L_\ell)=\delta_{j\ell}.
\tag{7}
$$
系数由原矩阵的线性逆定义，没有执行评价。

## 4. 在简单退化点，(7)给完整局部不可解例子

固定原非零第三系数 $\tau$，把(7)的完整原输出作为目标函数
$$
G_\ell=-L_\ell(f^2,g)/(2\tau).
\tag{8}
$$
这是当前 profiles 上的真实光滑函数。响应的所有尾仍按原定义使用；对本模块输出甚至在各包之外准确为零。

由(4)和 R345 的逐包局部式，全部整包通量为零。由(3)、R389，whole-$E$ 和自然总通量条件也全部通过。然而在第 $\ell$ 个指定点，
$$
F_j(x_j;G_\ell)
:=\int_{\ell_j}^{x_j}f'G_\ell''
=-\delta_{j\ell}/(2\tau).
\tag{9}
$$
R391 的原逆公式为
$$
k'=p\left(C+\int\frac{F_j(x;G_\ell)}
{A_f(x)p(x)^2}\,dx\right),\qquad p=f'.
$$
在 $x_\ell$，$A_f$ 简单、$p\ne0$，所以(9)给准确非零 logarithmic 系数
$$
-\frac{1}{2\tau\,A_f'(x_\ell)p(x_\ell)}
\log|x-x_\ell|
\quad\text{于 }k'.
\tag{10}
$$
任何齐次 $Cp$ 都不能消去它。因此该目标在此点没有光滑逆 germ。其他已选点的通量为零，按 R391 恰满足那些点的完整局部条件；未选点仍不作声明。

(8)—(10)证明的是原函数像问题中的反例，以及(6)的线性独立门。它没有把 $L_\ell$ 冒称为在保持所有实际基准、同一保护芽和 whole 联合约束下已经实现的整个闭路径成本。

## 5. 增强线性接口不增加新的响应商，但实际基准仍须支付

令
$$
J=(E,\Lambda_{\rm all}),\qquad J^+=(J,\mathcal F_1,\ldots,\mathcal F_m).
$$
虽然 $\Lambda_{\rm all}$ 按 profiles 写为一个函数族，它在原有限 U 上的像仍是有限维；本稿不评价其维数或给出新的基。

由(6)，对任何原成本或原响应，都可用一个(3)中的线性组合单独修正显示的 m 个读出。因此
$$
\boxed{
J^+(U)=J(U)\times\mathbb R^m,\qquad
J^+(\mathcal R)=J(\mathcal R)\times\mathbb R^m.
}
\tag{11}
$$
增强后的响应商与 $J(U)/J(\mathcal R)$ 同构。任何杀掉原响应的线性字符，其新 m 个坐标系数必须为零；这不代替实际正锥或 signed 零基准实现。

若未来已建立原 J 的真实紧目标 $C^1$ 截面，(6)可作为 R222/R345 三角增强中的右下块；但真实 prototype、桥、倒行和 Klein 成本必须重新进入同一个方程。当前稿不据(11)宣布这个前提成立，也不把 R392 已付的两个固定自然读出扩大为全部 $\Lambda_{\rm all}$。

因此，R394 的内部条件即使在 universal whole-$E$ 与全自然通量零下仍有实质内容。原十一列确可改变这些部分门而不改变那些全局线性观察；是否把它们连同剩余商基准实际同时支付，是不同的实现问题。
