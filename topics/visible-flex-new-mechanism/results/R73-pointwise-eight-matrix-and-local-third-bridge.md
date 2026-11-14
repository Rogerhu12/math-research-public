# R73：二阶密度的逐点八矩闭合与真实第三桥的局部余项

状态：**已证明**。本稿把 R56 的原始二阶 range 密度逐点化为同一八维算子，并把任意零矩阵桥的第三历史部分准确分离到 R71 已可达的交换子空间。它不声称剩余局部三次密度是全导数，不声称真实不同 scalar 端口桥的全部第三响应已清零。

## 1. 约定与结论

在实际几何参数 $s$ 上取 $h>0,k,\omega$，满足

$$
\omega_s=\frac{k_s}{2h}.
$$

令 $\gamma=h_s,\nu=\omega_s$，并在一个共同紧区间上固定 profile 坐标 $x=\xi$，使 $z=x+\omega$ 一致不为零。记

$$
d=h\omega-k,\quad e=hx+d=hz-k,\quad
Q=1+e^2,\quad Q_d=1+d^2,\quad
\lambda=\frac{\gamma x+d_s}{h^2}
       =-\left(\frac zh\right)_s,
\quad
K_0=kz^2-\frac{k^2+1}{h}z.
$$

这里 $d_s=\gamma\omega-h\nu$，$e_s=\gamma x+d_s$。所有 profile 光滑并在共同右 collar 恒零。右积分为正尾 $\int_x^r$；不预设左尾或总矩为零。

对静态 $f,g$，设 $r_s(f,g)$ 是 R56 原始二阶密度 $R[H(Y_f,Y_g)]$。下标 $s$ 在此标示实际几何位置；对一个表达式求导另用 $\partial_s$ 明写。

**逐点结论：** 存在一个真实的 $M(s)\in\mathfrak{sl}_3(\mathbb R)$，只依赖 $h,k,\omega,h_s,k_s$，使

$$
r_s(f,g)=\Phi_{M(s)}(f,g)
$$

在每个 $s,x$ 都成立。不是只在 $s$ 积分后成立；不需要端点导数消失。

定义三条不随几何移动的尾基

$$
J_0(f,g)=\int_x^r f''g'',\quad
J_1(f,g)=\int_x^r\eta f''g'',\quad
J_2^*(f,g)=\int_x^r\bigl(\eta^2 f''g''+2f'g'\bigr).
$$

$\Phi_M$ 采用 R69/R71 的八坐标约定：

$$
M=
\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix},
\qquad t_0=p_0/4+s_1/2.
$$

本稿随后给出其全部点态系数以及真实第三密度的精确分解。

## 2. 从 R56 的原始场直接展开

取有向正交框架

$$
T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,\qquad
\alpha_s=h^2T.
$$

原带为 $X(s,u)=\alpha(s)+uN(s)$，特征坐标为 $u=h/z$。初阶场的分子为

$$
Y_f=\frac1zF V_f,\qquad
V_f=\left(-\frac{f'}2,0,hf-\frac e2f'\right),
\qquad F=(T,N,B).
$$

固定 $x$ 的协变导数分子为

$$
\nabla_s V_f=
\left(0,h\left(f-\frac z2f'\right),
       \gamma f-\frac{e_s}{2}f'\right).
$$

令

$$
\mathcal J_{fg}=V_f\cdot V_g,\quad
T_{\xi,fg}=V_f'\cdot V_g',\quad
T_{s,fg}=(\nabla_sV_f)\cdot(\nabla_sV_g),
$$

以及

$$
P_{fg}=\frac1{2h}\int_x^rT_{\xi,fg},\qquad
\mathcal B_{fg}=\frac{\mathcal J_{fg}}{2h}.
$$

R56 的原始密度准确是

$$
r_s(f,g)=
\frac{T_{s,fg}}{2h^2}+K_0P_{fg}
-\lambda\,\partial_s P_{fg}
+\frac{K_0}{z}\mathcal B_{fg}
-\frac{\gamma}{h^2}\partial_s\mathcal B_{fg}.
\tag{1}
$$

$K_0/z=kz-(k^2+1)/h$ 本身是 $x$ 的多项式。定义

$$
J_e(f,g)=Q_dJ_0+2hdJ_1+h^2J_2^*
=\int_x^r\bigl((1+e(\eta)^2)f''g''+2h^2f'g'\bigr).
$$

一次真实右端分部积分给

$$
P_{fg}=\frac{J_e(f,g)}{8h}+\frac e8f'g'.
\tag{2}
$$

边界项只使用右 collar 零；左端取值保留。把 (2) 与上面的分子代入 (1)，可先对 $f=g$ 展开，再极化，得到

$$
r_s(f,g)=A_0fg+\frac{A_1}{2}(fg'+f'g)+A_2f'g'
+B_0J_0+B_1J_1+B_2J_2^*,
\tag{3}
$$

其中

$$
A_0=\frac{ke}{2},\qquad
A_1=-\frac{kQ}{2h},
\tag{4}
$$

$$
A_2=\frac{K_{0,x}Q}{8h}
-\frac{\gamma e e_s}{4h^3}
+\frac{\gamma^2Q}{8h^4},
\tag{5}
$$

$$
\begin{aligned}
B_0&=\frac{K_0Q_d+\lambda(\gamma Q_d/h-2d\,d_s)}{8h},\\
B_1&=\frac{K_0d-\lambda d_s}{4},\\
B_2&=\frac{hK_0-\gamma\lambda}{8}.
\end{aligned}
\tag{6}
$$

为便于核对 (5)，直接展开的局部 $f'g'$ 系数也可以写为

$$
\frac{z^2}{8}+\frac{eK_0}{8}+
\frac{(K_0/z)Q}{8h}
-\frac{\gamma e e_s}{4h^3}
+\frac{\gamma^2Q}{8h^4}.
$$

前面三项等于 $K_{0,x}Q/(8h)$，用 $hz=e+k$ 逐项展开即可验证。式 (4) 中的 $\gamma^2,\gamma e_s$ 项在 $T_s$ 与 $-\gamma\partial_s\mathcal B/h^2$ 之间准确抵消；没有做 $s$ 方向分部积分。

## 3. 全部八矩关系均逐点成立

定义

$$
C=B_0+xB_1+x^2B_2,\qquad W=B_1+2xB_2.
$$

由 (6) 直接收集得

$$
C=\frac{K_0Q}{8h}
+\frac{\gamma e_sQ}{8h^4}
-\frac{e e_s^2}{4h^3},\qquad
W=\frac{K_0e}{4}-\frac{e_s^2}{4h^2}.
\tag{7}
$$

因 $e_x=h$、$(e_s)_x=\gamma$，(7) 给

$$
A_2=C_x-W,\qquad A_0=-\frac12A_{1,x}.
\tag{8}
$$

展开 $A_1=p_0+p_1x+p_2x^2$，则

$$
p_0=-\frac{k(1+d^2)}{2h},\qquad
p_1=-kd,\qquad p_2=-\frac{kh}{2}.
\tag{9}
$$

(6) 的二次项恰为

$$
B_0=r_0+r_1x-\frac{p_0}{4}x^2,\quad
B_1=s_0+s_1x-\frac{p_1}{4}x^2,\quad
B_2=t_0+t_1x-\frac{p_2}{4}x^2.
\tag{10}
$$

式 (8) 随即重建

$$
A_2=r_1+(s_1-p_0/2)x+(t_1-p_1/2)x^2-p_2x^3/2,
$$

正是八矩算子的局部系数。最后核 trace 条件。写

$$
K_0=kx^2+a_1x+a_0,\quad
a_1=2k\omega-\frac{k^2+1}{h},\quad
a_0=k\omega^2-\frac{k^2+1}{h}\omega,
$$

且 $\lambda=\lambda_x x+\lambda_0$，其中 $\lambda_x=\gamma/h^2,\lambda_0=d_s/h^2$。则

$$
4\left(\frac{p_0}{2}+s_1-2t_0\right)
=-\frac{k(1+d^2)}h+d a_1-h a_0
-\lambda_x d_s+\gamma\lambda_0=0.
\tag{11}
$$

末两项逐点抵消；前三项用 $d=h\omega-k$ 展开为零。故 $\operatorname{tr}M=0$，完成逐点八矩闭合证明。

这同时给出可直接实现的八维第二 history：

$$
m(s)=\int_{s_0}^sM(t)\,dt,\qquad
W_{fg}(s,x)=\Phi_{m(s)}(f,g)(x).
\tag{12}
$$

(12) 保留真实累计历史；没有分段重锚，不把 profile 冗余基的系数当作独立未知函数。

## 4. 变化 profile 的必要链式项

这里第三个 profile 暂记为 $j$，避免与几何 $h$ 混淆。若 $\psi=\psi(s,x)$，则

$$
R[H(Y_f,Y_{\psi(s)})]
=\Phi_{M(s)}(f,\psi(s))
+\Psi_s(f,\partial_s\psi),
\tag{13}
$$

而不是只取第一项。

记 $c=\partial_su|_x$，$\rho_{fg}=P_{fg}+\mathcal B_{fg}/z$ 为右锚恢复的 $N$ 分量。直接对真实向量场求导，额外项是

$$
\Psi_s(f,g)=
\frac{(\partial_sY_f|_x)\cdot Y_g}{2u^2}
-\frac{c}{u^2}\rho_{fg}.
\tag{14}
$$

由于 $c=e_s/z^2$，代入 $Y,\rho$ 后所有 $z^{-1}$ 余项消去，得到

$$
\boxed{
\Psi_s(f,g)=
\frac{\nu-\gamma k/h^2}{4}\,f'g
-\frac{\gamma Q}{8h^3}f'g'
+\frac{h\nu-\gamma z}{8h^3}J_e(f,g).
}
\tag{15}
$$

等价地，设 $b=(d/h)_s=\gamma k/h^2-\nu$，则

$$
\Psi_s(f,g)=
-\frac b4f'g-\frac{\gamma Q}{8h^3}f'g'
-\frac{e_s}{8h^3}J_e(f,g).
$$

它一般不对称，也一般不为零；常 $h,k,\omega$ 时才为零。特别在常 $h$ 的变化段，

$$
\Psi_s(f,g)=\nu\left(\frac{f'g}{4}
+\frac{J_e(f,g)}{8h^2}\right).
$$

因此不能把 R62 常段的静态二次公式直接用于真实连接段。

## 5. 真正第三桥的准确分解

令 $\eta_{0,gj}$ 为 R56 的真实局部恢复系数，

$$
\eta_{0,gj}=
-\frac{T_{s\xi,gj}}{2h}
+\frac{e_s}{2h}\partial_xP_{gj}
+\frac{\gamma}{2h}\partial_x\mathcal B_{gj}
-\frac12\partial_sP_{gj},
$$

其中 $T_{s\xi}$ 为两个分子协变导数与 $x$ 导数的对称配对。设 $w=h^2-ku$，并定义不含累计 history 的局部场

$$
K_{gj}=\rho_{gj}N+
\frac{\eta_{0,gj}}{h^2}(uT+wB).
$$

形式右锚二阶恢复准确为

$$
Z_{gj}=K_{gj}-Y_{W_{gj}}.
$$

这里的“形式”只意味着仍须另付左 collar/ruling/period 条件；没有把这些条件自动宣告成立。所有字段和导数都保持同一真实右锚。

记

$$
\ell_s(f;g,j)=R[H(Y_f,K_{gj})],\qquad
\mathcal C_s(f;g,j)=
\ell_s(f;g,j)-\Psi_s(f,\Phi_{M(s)}(g,j)).
\tag{16}
$$

$\ell_s$ 中要对整个 $K_{gj}$ 真正求 $s$ 导数。由 (12)(13) 得整个桥的第三响应

$$
\boxed{
T_B(f;g,j)=
-\int_B\Phi_{M(s)}(f,\Phi_{m(s)}(g,j))\,ds
+\int_B\mathcal C_s(f;g,j)\,ds.
}
\tag{17}
$$

第二项是明确的局部三次密度，仅依赖当前几何及其有限阶导数和右端 profile 原函数，不含累计矩阵 $m$。本稿没有证明它是全导数，没有证明它落在 28 个交换子中。

## 6. 零矩阵桥的全部历史部分已经在可达空间内

取固定八基 $\Phi_i$，写 $M(s)=\sum_i a_i(s)E_i$、$m(s)=\sum_i m_i(s)E_i$，$m_i'=a_i$。若桥的总矩阵为零，$m(s_0)=m(s_1)=0$，则

$$
I_{ij}=\int_{s_0}^{s_1}a_i(s)m_j(s)\,ds
$$

满足 $I_{ij}+I_{ji}=[m_im_j]_{s_0}^{s_1}=0$。因此 (17) 的第一项是

$$
-\sum_{i<j}I_{ij}
\left\{\Phi_i(f,\Phi_j(g,j))-\Phi_j(f,\Phi_i(g,j))\right\}.
\tag{18}
$$

这恰在 R71 的真实第三交换子可达空间内，且 (18) 是完整三线性算子身份，不限于对角 $f=g=j$ 或有限个测试 profile。

在桥端插入 R71 的零矩阵、同 scalar、frame 恒等小 loop，可准确消掉 (18)。任一有限目标系数可用有限条小参数 loop 相加；在紧参数邻域上可以预先固定重复次数。因所插入 loop 的总矩阵均为零，第三 composition 的交叉项也为零。原桥的 frame/scalar 端口保持，位置位移仍可改变并由整个 R45 四块组装处理。

共同物理区间必须覆盖所有有限插入路径；依 R70/R71 的构造可在全部路径选定后固定一个共同区间。本稿不声称任意预给的狭窄区间自动容纳所有插入。

**于是：任一零矩阵桥的真实第三匹配问题，可以准确缩到局部项 $\int_B\mathcal C_s$，而不是继续追逐冗余累计 history。** 这仍没有支付局部项本身、$P_0$、第四 ruling、有限等距族、闭嵌入或主课题的厚度及幅度指标。

来源：R56 原始恢复公式；[R71 第三 holonomy 与完整第四 $P_1$](R71-third-holonomy-commutators-and-complete-fourth-P1.md)。证明以上述逐项恒等式为准。

