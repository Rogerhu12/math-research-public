# R251：完整面积槽在非共振小偶端芽上仍强迫四次矩为零

日期：2026-11-15。**已证明。** 本稿是 [R249](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md) 的准确参数推广；没有新的 profile 求积、符号运行、参数扫描或几何计算。

来源：[R73 原八矩密度](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R227 可实现例外端芽](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R245 完整 Gaussian history](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)及 R249。本稿不重复 R249 的真实函数独立性证明，也不处理全相位外槽中的额外 hook 项。

## 1. 取消共振假设，保留同一个真实 germ

取

$$
\kappa\ne0,\qquad h_e>0,\qquad \varepsilon>0,
$$

$$
H=e^{\varepsilon\sigma^2},\qquad
h=h_eH,\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\frac{\kappa}{h}.
\tag{1}
$$

仍保持原 I、右锚、物理支及真实共同初值。现在不要求
$\varepsilon=\kappa^2/4$。记

$$
j=2\varepsilon\kappa\sigma^2,\qquad
v=2\varepsilon\sigma,\qquad
\eta=\frac{2\varepsilon}{\kappa},\qquad
u=\kappa^2>0.
$$

则

$$
v^2=\eta j.
\tag{2}
$$

字母域与同锚原函数不变：

$$
\mathbb F=\mathbb R(\sigma,H),\qquad
E_r=\int_0^\sigma H(t)^r\,dt,\quad
r\in\{1,-1,-2,-3\}.
$$

R249 的原函数独立性只要求 $\varepsilon\ne0$。R245 的完整奇偶、四 Gaussian 及其二重词归约亦未用共振。因此整个 $A_{-2,-3}$ 槽的唯一来源与完整因子保持准确。

## 2. 两个 Gaussian 原函数系数的全参数式

R73 的 raw 坐标直接给

$$
\begin{aligned}
8h^2r_1={}&-j^4+\eta j^3
+(\kappa^2-2-4\kappa\eta)j^2+\eta j+\kappa^2-1,\\
4h^2s_0={}&-\kappa j^3+\kappa^2j^2
-(\kappa+4\kappa^2\eta)j,\\
8h^3r_0={}&-\kappa j^4+(\kappa^2+2\kappa\eta)j^3\\
&-(2\kappa+8\kappa^2\eta)j^2
+(\kappa^2+2\kappa\eta)j-\kappa.
\end{aligned}
\tag{3}
$$

其中没有删除 $h_s,k_s$ 项。对 $r=-2,-3$，同一有限分部积分仍给

$$
\text{E}_r\text{ 在 }\int_0^\sigma j(t)^nH(t)^r\,dt
\text{ 中的系数}
=\frac{(-1)^n(2n-1)!!\,\kappa^n}{r^n}.
\tag{4}
$$

把 (3) 代入，写

$$
B_{-2}=a\Phi_{r_1}+b\Phi_{s_0},
\qquad B_{-3}=c\Phi_{r_0},
$$

得到

$$
a=
\frac{\varepsilon(16-36u)-93u^2-8u-16}{128h_e^2},
\qquad
b=-\frac{u(9u+4+32\varepsilon)}{32h_e^2},
\tag{5}
$$

$$
\boxed{
a+3b=
\frac{\varepsilon(16-420u)-201u^2-56u-16}{128h_e^2},
}
\tag{6}
$$

$$
\boxed{
c=
\frac{\kappa\{\varepsilon(36-84u)-20u^2-9u-27\}}
{216h_e^3}.
}
\tag{7}
$$

令 $\varepsilon=u/4$，(5)—(7) 准确返回 R249 的共振系数。这只是原式一致性的代入，不是用共振结果外推新参数。

## 3. 完整 pure 面积系数保持同一形式

对合法三矩圆 $q=f+ig$，保留 R249 的真实 profile 量

$$
\tau_q=-J((q'')^3)/3,\qquad
M_4(q)=\int_I(q'')^4,
$$

$$
m_2^*(q,\tau_q)
=\int_I\{x^2q''\tau_q''+2q'\tau_q'\}.
$$

R249 已逐项证明：原 $Z^2$ 只产生对称二重乘积；第三局部和 chain 项不能产生反对称面积；整个指定面积槽的系数准确为

$$
\boxed{
2c(a+3b)\mathcal E_\sigma(q,\tau_q).
}
\tag{8}
$$

所有真实负 Gaussian 原函数的中心常数尾保留。整个第一场能量在当前参数下仍是

$$
\mathcal E_\sigma(q,\tau_q)
=-\frac j8M_4(q)+\frac{h_eH}4m_2^*(q,\tau_q).
\tag{9}
$$

因 $\varepsilon>0,\kappa\ne0$，H 与 $\sigma^2$ 不成常数比例。只要

$$
c(a+3b)\ne0,
\tag{10}
$$

完整 pure 偶 ruling 属于同一 $\mathcal W_e$ 就必迫

$$
\boxed{M_4(q)=0,\qquad m_2^*(q,\tau_q)=0.}
\tag{11}
$$

R249 对真实前缀、独立二阶 gauge、第三 gauge 及第四 Fourier 规范的证明逐字适用。本稿没有把 (11) 当作整个 ruling 的充分条件。

## 4. 所有小正 $\varepsilon$ 都没有这条面积槽的退化

对 $0<\varepsilon\le3/4$，式 (7) 的大括号满足

$$
\begin{aligned}
\varepsilon(36-84u)-20u^2-9u-27
&=(36\varepsilon-27)-84\varepsilon u-20u^2-9u\\
&<0,
\end{aligned}
$$

因为 $u>0$。式 (6) 的分子同样满足

$$
\begin{aligned}
\varepsilon(16-420u)-201u^2-56u-16
&=(16\varepsilon-16)-420\varepsilon u-201u^2-56u\\
&<0.
\end{aligned}
$$

故

$$
\boxed{
\kappa\ne0,\quad 0<\varepsilon\le3/4
\quad\Longrightarrow\quad c(a+3b)\ne0.
}
\tag{12}
$$

因此 R249 的完整面积障碍覆盖整个小正 $\varepsilon$ 族，并非只覆盖一次共振选择。特别 R227/R241 在共同外参数小邻域中安装的这类小端芽，不能仅通过离开共振线来避开该指定的完整 pure 条件。

本节只是 germ 障碍。它不重新给任意大参数的真实全局安装，也不改变先前固定的目标度量和物理支。

## 5. 正参数中的两条准确例外曲线

由 (6)、(7)，指定槽的因子只能在以下两条正参数曲线上退化。

第一条是 c=0：

$$
0<u<\frac37,\qquad
\varepsilon=\varepsilon_c(u)
:=\frac{20u^2+9u+27}{36-84u}.
\tag{13}
$$

当 $u\ge3/7$ 时，分母非正而分子严格正，不存在正 $\varepsilon$ 解。并且

$$
\varepsilon_c(u)-\frac34
=\frac{20u^2+72u}{36-84u}>0.
\tag{14}
$$

第二条是 $a+3b=0$：

$$
0<u<\frac4{105},\qquad
\varepsilon=\varepsilon_b(u)
:=\frac{201u^2+56u+16}{16-420u}.
\tag{15}
$$

当 $u\ge4/105$ 时也没有正解，而且

$$
\varepsilon_b(u)-1
=\frac{201u^2+476u}{16-420u}>0.
\tag{16}
$$

除 (13)、(15) 的并集外，(11) 对全部正参数成立。在曲线上，准确结论仅是本稿指定的 $A_{-2,-3}$ 对角面积系数不再给这一非成员证据；不能由此推其他面积、局部项、完整四次谐波、period 或 joint 已清。

尤其 $a+3b=0$ 只使该对角交换子为零。它不意味着完整三槽交换子为零，也不能在全相位外槽中擅自删除仍可能存在的 hook。相应全相位问题与本稿的 pure 对角推论分开处理。

## 6. 对现有圆的严格结论

R249 已证明，对未旋转的逐微包 $g_0=\pm f_0$ 完整 block，

$$
M_4(f_0+ig_0)
=-4\sum_i a_i^4\int_I(u_i'')^4<0.
$$

R239 最终双 block 在 R248 已付的角范围内还有
$\operatorname{Re}M_4(q)<0$。这些是同一冻结 profiles 的准确恒等，与 $\varepsilon$ 无关。

所以这些圆在所有满足 (10) 的 (1) 端芽上都不能完成第四 ruling，特别包括 (12) 的全部小正 $\varepsilon$。这不是重新测试六个已付能量，而是同一完整面积函数证据的准确参数范围。

普通复四次矩在一般圆上仍可相消。两条例外曲线只留下一个具体的新完整函数问题，未被当作可行构造；其他 germ、其他 circle 及主课题的完整解均不由本稿否定。
