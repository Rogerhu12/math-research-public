# R76：真实局部第三响应的准确 loop 与非零速度面积方向

状态：**已证明**。本稿构造新的真实零矩阵、恒等 frame、同 scalar 端口的第三响应控制。它不是只给形式密度上界；但也没有证明这些方向在 R71 的 28 维交换子跨度之外，没有声称已匹配完整第四 $P_1$、其他 phase、$P_0$ 或 ruling。

## 1. 全程保留真实 composition 与倒行二次项

沿用 R73：对一条实际路径 $B$，

$$
T_B(f;g,j)=-I_B(f;g,j)+C_B(f;g,j),
$$

$$
I_B=\int_B\Phi_{M(s)}(f,\Phi_{m(s)}(g,j))\,ds,\qquad
m(s)=\int_{s_0}^sM,\qquad
C_B=\int_B\mathcal C_s.
\tag{1}
$$

路径总矩阵记为 $m_B=M$，可非零。所有字段使用同一固定右 collar；不清左尾，不重置实际历史。R71 的 composition 是

$$
T_{B_2B_1}=T_{B_1}+T_{B_2}
-\Phi_{M_2}(f,\Phi_{M_1}(g,j)).
\tag{2}
$$

式 (2) 的下标顺序只表示先走 $B_1$ 再走 $B_2$。

取 $D=\operatorname{diag}(-1,1,-1)$。真实倒行使用同号的 $k$：

$$
k^R(s)=k(\ell-s),\quad h^R(s)=h(\ell-s),\quad
\omega^R(s)=\omega(\ell-s).
$$

若 $F(0)=I,F(\ell)=A$、$\alpha(\ell)=V$，准确框架与位置为

$$
F^R(s)=D A^T F(\ell-s)D,\qquad
\alpha^R(s)=D A^T(\alpha(\ell-s)-V).
\tag{3}
$$

所以倒行仍满足真实框架 ODE 与 $\alpha_s=h^2T$。R73 的原始 $M(s)$ 在 $\gamma,\nu$ 同时变号下为偶，故

$$
M_{B^R}=M_B=M,\qquad
m_{B^R}(s)=M-m_B(\ell-s).
$$

局部三次项反转为奇，$C_{B^R}=-C_B$；这也可由第 4 节的导数权直接核对。因此

$$
\boxed{
T_{B^R}=-T_B-\Phi_M(f,\Phi_M(g,j)).
}
\tag{4}
$$

非零 $M$ 时不能把 (4) 简写成 $-T_B$。例如一个常态段的第三 history 本身已经核对了这个额外项的符号。

## 2. 不未知化校 frame 的局部贡献

先要求 $B$ 的首末 scalar 常值 germ 相同，frame 可以不同。R72 允许在末端附上一条真实同 scalar 桥 $F_0$，其

$$
M_{F_0}=0,\qquad T_{F_0}=0,
$$

并把整体 frame 校正为 $I\to I$。由 (2)，校正后的路径 $\widehat B$ 仍有

$$
M_{\widehat B}=M_B,\qquad T_{\widehat B}=T_B.
$$

**这并不意味着 $C_{F_0}=0$。** 由 (1)，准确是 $C_{F_0}=I_{F_0}$；它是交换子组合。且

$$
I_{\widehat B}=I_B+I_{F_0},\qquad
C_{\widehat B}=C_B+C_{F_0}.
\tag{5}
$$

跨项为 $\Phi_{\int M_{F_0}}(f,\Phi_M)=0$。因此下面始终以未校正原路径的 $I_B,C_B$ 表示；(5) 中 frame 桥的两个贡献会相消，不把它漏掉。

## 3. 任意 scalar 闭路径的局部响应可以准确单独实现

**命题 1。** 设 $B$ 是有限光滑真实路径，首末 scalar germ 相同。存在有限光滑 loop $\mathcal L_B$，首末为该同一 scalar germ、frame $I\to I$、总矩阵零，并有完整三线性身份

$$
\boxed{T_{\mathcal L_B}=2C_B=2\int_B\mathcal C_s.}
\tag{6}
$$

证明如下。先按第 2 节校 frame，得到 $\widehat B$。由 R70，取一条同 scalar、frame $I\to I$ 的真实桥 $E$，其总矩阵为 $-M$。同一条 $E$ 在下面两次出现，不能重新选取：

$$
W_1=\widehat B\,E,\qquad W_2=\widehat B^R\,E.
$$

二者总矩阵皆零。用 (2)(4)，

$$
T_{W_1}=T_B+T_E+\Phi_M\circ\Phi_M,\qquad
T_{W_2}=-T_B+T_E.
$$

因此真实 loop $W_1W_2^R$ 的第三响应准确为

$$
2T_B+\Phi_M\circ\Phi_M.
\tag{7}
$$

未知的整条 $E$ 的第三响应已严格相消。

写 $M(s)=\sum_i a_i(s)E_i$、$m(s)=\sum_i m_i(s)E_i$，并令

$$
I_{ij}=\int_Ba_i(s)m_j(s)\,ds.
$$

现在端值可以非零，正确关系是

$$
I_{ij}+I_{ji}=M_iM_j.
$$

所以

$$
2I_B-\Phi_M\circ\Phi_M
=\sum_{i<j}(I_{ij}-I_{ji})[\Phi_i,\Phi_j],
\tag{8}
$$

其中 $[\Phi_i,\Phi_j](f;g,j)=\Phi_i(f,\Phi_j(g,j))-\Phi_j(f,\Phi_i(g,j))$。把 (1)(8) 代入 (7)，得到 $2C_B$ 加上一个已知交换子组合。R71 的真实零矩阵 loop 可准确消去这个组合，得到 (6)。

若改以 $\widehat B$ 的积分计算，(5) 给 $C_{F_0}=I_{F_0}$，这份额外交换子恰与对应历史项相消；等价地可一并放进 R71 的消去系数。因此 frame 桥的局部贡献没有被设零。

所有系数只依赖真实几何，不依赖选取的 profile。大系数用有限条小参数 loop 相加；在紧参数邻域预先固定重复次数。R70 的辅助完整圈数也可在小参数邻域一次选定，保证实际控制族光滑。位置位移没有被指定，仍由完整 R45 四块构造处理。证毕。

## 4. 改变真实控制长度，准确隔离导数权 3

R73 局部项有唯一分解

$$
\mathcal C_s=\mathcal C_s^{[1]}+\mathcal C_s^{[3]},
\tag{9}
$$

上标表示几何 $s$ 导数总权：$h_s,k_s$ 权 1，$h_{ss},k_{ss}$ 权 2；$h,k,\omega$ 权 0。

这不是从有限采样猜测。初阶 $Y_f$ 没有几何导数；局部二阶场为

$$
K_{gj}=\rho_{gj}N+
\eta_{0,gj}\frac{uT+wB}{h^2},
$$

其中 $\rho$ 权 0，$\eta_0$ 权 1。在 $DY_f$ 中，$N$ 分量权 0，$T/B$ 分量权 1；在 $DK_{gj}$ 中，$N$ 分量权 1，$T/B$ 分量权 0 或 2。因此 $H(DY,DK)$ 只含权 1、3。右锚 $u$ 导数配对的恢复分量权 1；其 $s$ 导数乘 $c=u_s$ 后权 3。R73 的 $\Psi$ 权 1，而点态 $\Phi_M$ 权 0 或 2，所以 $\Psi(f,\Phi_M(g,j))$ 也只含权 1、3。这证明 (9)，并同时证明两个部分在真实倒行下都取负。

取任意首末为常值 scalar germs 的路径 $C$，其端口可以不同。改变实际控制长度：

$$
(h_\delta,k_\delta,\omega_\delta)(s)
=(h,k,\omega)(s/\delta),\qquad 0\le s\le\delta\ell.
$$

这仍满足 $\omega_s=k_s/(2h)$。**每次重新按真实 ODE 积分 frame 与 $\alpha$**；它不是把原曲面做材料重参数化，因为框架里的单位系数 $B_s=N$ 没有缩放。

记

$$
C_1[C]=\int_C\mathcal C_s^{[1]},\qquad
C_3[C]=\int_C\mathcal C_s^{[3]}.
$$

由 (9) 的实际尺度，严格有

$$
\int_{C_\delta}\mathcal C_s=C_1[C]+\delta^{-2}C_3[C].
\tag{10}
$$

令 $B(t)$ 先走 $C_{\delta_0}$，再走另一实际长度的真实倒行 $C_{\delta(t)}^R$，其中

$$
\delta(t)=(\delta_0^{-2}-t)^{-1/2}.
$$

取固定小区间使根号内正。两个 scalar 端口严格相接，整条 $B(t)$ 回到初始 scalar germ。由 (10)，

$$
\int_{B(t)}\mathcal C_s=t\,C_3[C].
$$

应用命题 1，得到真实有限 loop 族

$$
\boxed{M_{\mathcal L_t}=0,\qquad
T_{\mathcal L_t}=2t\,C_3[C],\qquad
F_{\mathcal L_t}:I\to I.}
\tag{11}
$$

(11) 是准确线性身份，没有未控制的 $O(t^2)$。frame 端口的实际长度效应由 R72 处理，不能因为 (10) 就假定原 frame 也不变。不同长度路径的 $P_0$、位移与高阶项均可改变。

## 5. 权 3 的速度面积系数：明确公式

下面证明 (11) 可非平凡。只需对角 $f=g=j=q$。取一个基点

$$
h=1,\qquad d=h\omega-k=0,
$$

且共同区间位于 $x>1$，例如基点 $k=\omega=1$。记

$$
Q=1+x^2,\quad g=q',\quad p=q'',\quad r=q'''.
$$

$J_0,J_1,J_2^*$ 仍取 R73 的准确正右尾。定义

$$
\begin{aligned}
a_q={}&\frac{2Qgp-2xg^2-xQp^2+J_0-J_2^*}{16},\\
b_q={}&-\frac{Qp^2+2J_1}{16},\qquad
\rho_q=a_q-xb_q,\qquad F_q=gb_q+p\rho_q.
\end{aligned}
\tag{12}
$$

在几何变量 $(h,d)$ 下，局部二阶恢复的 $T$ 分子 $A=\eta_0/h$ 一般对速度线性。其两个系数为

$$
\begin{aligned}
A_h&=\frac{2Qgp-2he\,g^2-xQp^2+(1+d^2)J_0-h^2J_2^*}{16h^3},\\
A_d&=\frac{-Qp^2-2hdJ_0-2h^2J_1}{16h^3},
\end{aligned}
\tag{13}
$$

即 $A=h_sA_h+d_sA_d$；基点正是 $a_q,b_q$。

为核对 (13)，从 R56 的
$\eta_0=-T_{s\xi}/(2h)+e_sP_\xi/(2h)+\gamma\mathcal B_\xi/(2h)-P_s/2$
代入 R73 的 $P=J_e/(8h)+ef'g'/8$ 即得；$q$ 本身的局部项准确抵消。

加速度项只来自 $A_s$。其线性系数作用为

$$
\Sigma_{\gamma,v}(A)
=\frac{Q(\gamma g-e_sp)A-e_s\int_x^r Qq'''A}{4h^3},
\qquad e_s=\gamma x+v,\quad v=d_s.
\tag{14}
$$

这里右积分内的几何 $Q$ 和 $A$ 按积分变量评价，积分外的 $e_s(x)$ 保留为查询点值。推导 (14) 时，可先用准确右端分部积分

$$
P_{H(Y_q,K_A)}
=\frac{(Qq''-heq')A+\int_x^rQq'''A}{4h}.
$$

真实 $\Phi_M$ 只含一阶几何导数，故 R73 的 $-\Psi(q,\Phi_M(q,q))$ 不增加加速度项。

在基点，令 $\Sigma_h,\Sigma_d$ 分别为 (14) 的 $\gamma,v$ 系数。由
$d_s=\omega h_s-k_s/2$，转换回独立控制 $(h,k)$ 后，速度面积
$k_s h_{ss}-h_s k_{ss}$ 的系数是

$$
\mathfrak A[q]=\frac{\Sigma_h(b_q)-\Sigma_d(a_q)}4.
\tag{15}
$$

直接从 (12) 求导得

$$
b_q'=-\frac{Qpr}{8},\qquad
\rho_q'=-b_q+\frac{Qgr}{8},\qquad
F_q'=r\rho_q.
$$

保留积分外查询点 $x$，一次右端分部积分把 (15) 化为

$$
\boxed{
\mathfrak A[q](x)=
-\frac18\int_x^r\eta F_q(\eta)\,d\eta
+\frac1{16}\int_x^r(\eta-x)Q(\eta)q'''(\eta)b_q(\eta)\,d\eta .
}
\tag{16}
$$

特别不能把 $\int Qr\,a_q-x\int Qr\,b_q$ 误写成只含 $\rho_q$ 的一个积分；正确差额正是 (16) 中的 $(\eta-x)$ 项。

## 6. 该面积算子严格非零

先取一个紧支撑 $C^7$ 实 profile，在右支撑端点 $c>1$ 的左侧等于

$$
q(x)=a(c-x)^m,\qquad a>0,\quad m\ge8.
$$

其余左侧可以平滑截断；右侧零延拓。写 $t=c-x$、$Q_c=1+c^2$。由 (12)，

$$
b_q=-\frac{Q_ca^2m^2(m-1)^2}{16}t^{2m-4}
+O(t^{2m-3}),\qquad F_q=O(t^{3m-5}).
$$

而 $q'''=-am(m-1)(m-2)t^{m-3}$，所以 (16) 的第一项只有 $O(t^{3m-4})$，第二项给

$$
\boxed{
\mathfrak A[q](x)=
\frac{Q_c^2a^3m^3(m-1)^3}{768(3m-5)}
\,t^{3m-5}+O(t^{3m-4})>0
}
\tag{17}
$$

在足够小的正 $t$ 成立。分母来自
$\int_x^c(\eta-x)(c-\eta)^{3m-7}d\eta
=t^{3m-5}/((3m-6)(3m-5))$，与 $3m-6=3(m-2)$ 的准确抵消。

算子 (16) 对固定紧区间上的有限 $C^3$ 范数连续。用仍支撑在共同区间内部的 $C^\infty$ profiles 逼近上述 $C^7$ profile，保留某个固定点的严格正值。因此存在真正光滑紧支撑 $q$ 使 $\mathfrak A[q]\ne0$。

这也证明局部 $\mathcal C_s$ 不能对所有控制路径自动成为一个有限 jet 端点势：加速度系数中的非零反对称面积项不满足速度梯度的混合偏导相容性。它不排除某条具体路径的局部积分为零，更不排除用真实控制补偿它。

## 7. 非零的真实准确第三方向

取任意非零 $a_0\in C_c^\infty((0,\ell))$，在基点 $(h,k,\omega)=(1,1,1)$ 附近设计实际 scalar 路径

$$
h_\varepsilon=1+\varepsilon a_0(s),\qquad
k_\varepsilon=1+\varepsilon a_0'(s),\qquad
(\omega_\varepsilon)_s=
\frac{(k_\varepsilon)_s}{2h_\varepsilon},
\quad\omega_\varepsilon(0)=1.
$$

取小 $\varepsilon$ 保 $h>0$。首末 $h,k$ 回到常值，$\omega$ 的末值允许不同；第 4 节的真实倒行会准确返回，不把该增量重置。

权 3 项的积分首项由 (15) 给出：

$$
C_3[C_\varepsilon](q)=
2\varepsilon^2
\left(\int_0^\ell(a_0'')^2\,ds\right)\mathfrak A[q]
+O(\varepsilon^3).
\tag{18}
$$

原因是对称速度—加速度部分的常系数积分为零；
$k_sh_{ss}-h_sk_{ss}
=\varepsilon^2((a_0'')^2-a_0'a_0''')$，
其积分为 $2\varepsilon^2\int(a_0'')^2$；系数变化与三次速度项均为 $O(\varepsilon^3)$。

由 (17) 及光滑逼近，固定一个 $\mathfrak A[q]\ne0$ 的光滑 profile，再取足够小非零 $\varepsilon$，即可使 $C_3[C_\varepsilon]\ne0$。代入 (11)，得到一个**真实、有限、非零且准确线性**的第三 holonomy 控制方向。

共同物理区间的选择不循环：R70/R72 的辅助桥可先在小的紧 $(\varepsilon,t)$ 参数盒内统一选择有限控制词、辅助圈数与正 $h$ 下界，因此 $\omega$ 有统一有限界。先固定一个位于该界之外且 $x>1$ 的共同区间，再用任意这样的右端 $c$ 作 (17) 的 profile，最后在已固定参数盒内缩小 $\varepsilon$。所有路径使用该同一物理支。

## 8. 已付与仍欠

已付：任意 scalar 闭控制路径的真实局部第三积分可准确隔离；通过真实长度变化，权 3 的任一这种积分产生准确线性 loop；存在严格非零的光滑例子。构造保首末 scalar germs、frame 恒等与总矩阵零，全部基准补偿桥的未知第三响应已经在真实词中相消。

仍欠：这些新方向是否超出 28 交换子空间，以及能否按同一 profile、同一完整控制词匹配所需 $P_1$；其他 Fourier 模式、$P_0$、第四 ruling 与更高阶收敛；闭嵌入曲面、reach 与宏观幅度。改变控制长度是基底设计自由度，没有被说成同一曲面的有限等距弯曲。

