# R174 — 准确末切口的可积角二导与实际 body 两 jet 极限

本结果适用于 [R172](R172-accurate-last-cell-completion-on-the-unchanged-metric.md) 明确的准确末格，允许尾参数取 [R170](R170-dyadic-Bernstein-box-for-the-same-flat-tail.md) 的整个八段 Bernstein 子盒。它给出角一导的真实 cut 迹，以及角二导的径向可积上界。由此 [R124](R124-fixed-material-angular-variation-geometry.md) 实际标架/位置的角两导有 cut 极限，能作为 [R126](R126-finite-two-jet-collar-gluing.md) 的真实输入。

没有要求 $II_{uu}$ 在 cut 一致有界或连续，没有给 $h=0$ 强行指定径向导数，也没有声称已取得两片的准确拼接、同 $g$ 后验或强目标闭曲面。

## 1. 准确输入和命题

设准确物理末点为 $S$，$\tau=S-s$。在某个 $0<\tau\le\tau_0$ 的末段，使用 R172 的定义

$$
 B(s,u)=C(s,u)+\eta(s)T(a(s),u),\qquad
 C(s,u)=\frac{\tau}{\ell}C_0(u),\quad \ell=S-b>0,
 \tag{1}
$$

其中 $C_0=(C_n,C_m,C_l)$ 是真实保存的有限 Fourier 行；$\eta$ 是 R172 中 $\eta(\sigma(s))$ 的简写，满足 $0\le\eta\le1$ 且 $\eta\to1$。半径和 $K$ 始终在**物理 $s$** 处求值，不能改成 $a(\sigma(s))$。

尾函数为

$$
 T(a,u)=\kappa(a\sin u)(\cos^2u,-\sin u\cos u,\sin^2u),
 \tag{2}
$$

$\kappa\ge0$ 来自 R170 的准确子盒。末段角图是 $u=\xi$，seed/coast/bumps 全为零，R155 权重为一。准确 $K$ 满足

$$
 k_-\tau^3\le K(s)\le k_+\tau^3,\qquad k_->0.
 \tag{3}
$$

第 3 节直接为当前三次 phase bridge 给出 (3) 的可消费有理常数。

对 $B=(N,M,L)$ 定义

$$
 d=N-L,\quad v=(d,2M),\quad h=\sqrt{|v|^2+4K},\qquad
 (n,m,l)=\left(\frac{h+d}{2},M,\frac{h-d}{2}\right).
 \tag{4}
$$

**结论。** 可从实际有限系数计算有限非负常数 $C_0^*,C_1^*$，使全角满足

$$
 |h_{uu}(s,u)|\le C_0^*+C_1^*\tau^{-1/2}.
 \tag{5}
$$

因此 $\alpha=(m,-l,0)$ 的角二导在径向上可积，且完整 $(n,m,l)$ 的值和角一导在 cut 统一趋于 (2) 在 $a=4/5$ 的真实值和角一导。对于 R124 的真实初值和固定材料 $u$ ODE，$F,F_u,F_{uu},X,X_u,X_{uu}$ 都有统一 cut 极限；这些极限确为边界函数的角导。所得位置图具有所需的 $C^2$ 单侧延拓。

## 2. 新尾域的有限系数常数与 Glaeser 估计

令 $w=23/50$，$a_c=4/5$。对 $q\in(0,1)$，

$$
 \kappa(y)=\frac{630}{w}q^4(1-q)^4P(q),\qquad
 q=\frac{|y|-17/50}{w},
 \tag{6}
$$

区间外为零。R170 给每段 $I_j=[j/8,(j+1)/8]$ 的准确次数 15 控制 $c_{ji}\in[0,6/5]$。记 $A=j/8,B=(j+1)/8$。

在局部参数 $t$ 中，$q^4$ 的次数 4 控制为 $A^{4-r}B^r$，$(1-q)^4$ 的控制为 $(1-A)^{4-r}(1-B)^r$。两个 Bernstein 多项式的准确乘积规则是

$$
 (p\star q)_k=\sum_{i+j=k}
 \frac{\binom ni\binom mj}{\binom{n+m}k}p_iq_j.
 \tag{7}
$$

证明只需将 $B_i^n B_j^m$ 展开成对应 $B_{i+j}^{n+m}$。由 (7) 得 $q^4(1-q)^4$ 的次数 8 非负控制，再与 $c_j$ 相乘并乘 $630/w$，得到 $\kappa$ 的次数 23 准确非负控制 $e_{jk}$。这里全部运算是有限有理运算。

因此可取

$$
 \begin{aligned}
 Q_0&=\min\left(\frac{4725}{736},\max_{j,k}e_{jk}\right),\\
 Q_1&=\frac{8\cdot23}{w}\max_{j,k}|e_{j,k+1}-e_{jk}|,\\
 Q_2&=\frac{64\cdot23\cdot22}{w^2}
      \max_{j,k}|e_{j,k+2}-2e_{j,k+1}+e_{jk}|.
 \end{aligned}
 \tag{8}
$$

准确 Bernstein 求导和其非负单位分解证明 $0\le\kappa\le Q_0$、$|\kappa_y|\le Q_1$、$|\kappa_{yy}|\le Q_2$。全局多项式在段界的导数共同；$q^4(1-q)^4$ 保证外端所需导数与零支共同，$|y|$ 的尖点附近则处于固定零 collar。因此这是整个实轴的界，不仅是各开段内部的界。

若 $a(s)\le a_*$，令

$$
 k(s,u)=\eta(s)\kappa(a(s)\sin u),\quad
 M_0=Q_0,\qquad M_2=a_*^2Q_2+a_*Q_1.
 \tag{9}
$$

则 $0\le k\le M_0$ 且 $|k_{uu}|\le M_2$。

**Glaeser 引理。** 任意非负、周期、$C^2$ 函数 $f$ 若 $|f''|\le M$，则

$$
 |f'|^2\le2Mf.
 \tag{10}
$$

若 $M=0$，周期性给 $f'=0$。若 $M>0$，在整个实轴上应用 Taylor 不等式
$f(x+t)\le f(x)+tf'(x)+Mt^2/2$，取 $t=-f'(x)/M$ 并用左侧非负，即得 (10)。所以

$$
 |k_u|^2\le2M_2k.
 \tag{11}
$$

该证明不要求全局 $b_i\ge0$，也不依赖 R162 中原控制盒所用的特定 $3/4$ 次幂估计。允许曲率在内部角度归零。

## 3. 当前三次末相位的严格 $K\asymp\tau^3$ 常数

设准确 phase bridge 长度为 $L_\phi$，两端相位导数为零，末相位为 $-\pi/2$，起相位为 $p_0$。记 $\Delta=p_0+\pi/2>0$、$x=\tau/L_\phi$。准确三次 Hermite 公式为

$$
 \phi(s)=-\frac\pi2+\Delta x^2(3-2x),\qquad
 -\phi_s=\frac{6\Delta\tau}{L_\phi^2}(1-x).
 \tag{12}
$$

所以 $a_s=-\cos(\Delta x^2(3-2x))$，且

$$
 K(s)=\frac{6\Delta\tau}{L_\phi^2a(s)}(1-x)
       \sin\bigl(\Delta x^2(3-2x)\bigr).
 \tag{13}
$$

取准确 $\Delta_-\le\Delta\le\Delta_+$，令 $x_0=\tau_0/L_\phi\le1/2$、$\theta_*=3\Delta_+x_0^2\le1$。由 (12)，$a_c\le a(s)\le a_c+\tau_0$。用
$\theta(1-\theta_*^2/6)\le\sin\theta\le\theta$，可取

$$
 \begin{aligned}
 k_-&=\frac{6\Delta_-^2(1-x_0)(3-2x_0)(1-\theta_*^2/6)}
             {L_\phi^4(a_c+\tau_0)},\\
 k_+&=\frac{18\Delta_+^2}{L_\phi^4a_c}.
 \end{aligned}
 \tag{14}
$$

当前 R172 的 $L_\phi$ 是保存 `.026` 的准确 dyadic，$p_0$ 是保存 `-1.45` 的准确 dyadic，末 raw 格长度约 $0.001625$；故上述选区严格可用。实际脚本从绑定的 R171 包读取准确 $L_\phi,p_0$，从 R172 定义读取 $S-b$ 的严格 dyadic 上下端，不把显示十进制或浮点 $E$ 当成准确 $S$。

程序中的 $\pi$ 也不靠浮点显示给界。令 $A=\arctan(1/5),B=\arctan(1/239)$。准确倍角计算给 $\tan(4A)=120/119$，进而 $\tan(4A-B)=1$；又 $0<4A-B<0.8<\pi/2$，故 $\pi=16A-4B$。对 $\arctan z=\int_0^z(1+t^2)^{-1}dt$ 使用有限几何级数，其交错余项大小不超过下一项。分别使用 8 项和 4 项即可得严格有理 $\pi_\pm$，从而得到 (14) 所用的 $\Delta_\pm$。

## 4. 实际 raw 行的全角常数

记 $\rho(s,u)=(C_n-C_l,2C_m)$，并令

$$
 e(u)=(\cos2u,-\sin2u),\qquad v=k e+\rho.
 \tag{15}
$$

设 $\ell\ge\ell_->0$。对真实 $C_0$ 行，先将 $n-l$ 的相同频率系数准确相减，再取各系数绝对值乘频率 $j$ 次幂的和；加上 $2m$ 的对应和并除 $\ell_-$，得到 $B_j$，$j=0,1,2$。于是

$$
 |\partial_u^j\rho(s,u)|\le B_j\tau,\qquad j=0,1,2.
 \tag{16}
$$

这是有限 Fourier 的全角不等式，没有角采样，也没有将计算角与材料角混用：R172 已保证整末格 $u=\xi$。

## 5. 角二导的可积估计

由 $e\cdot e_u=0$、$|e_u|=2$、$|e_{uu}|=4$ 及 (11)，

$$
 |v_u|^2\le A k+2B_1^2\tau^2,\qquad A=4M_2+8M_0,
 \tag{17}
$$

并且

$$
 |v_{uu}|\le V_2:=M_2+4\sqrt{2M_0M_2}+4M_0+B_2\tau_0.
 \tag{18}
$$

严格内部 $K>0$，所以 $h>0$，准确微分给

$$
 h_{uu}=\frac{v\cdot v_{uu}}h+
 \frac{|v_u|^2h^2-(v\cdot v_u)^2}{h^3},
 \qquad |h_{uu}|\le |v_{uu}|+\frac{|v_u|^2}{h}.
 \tag{19}
$$

第二项的分子非负，且 $|v|\le h$，所以最后一个界同时控制正负部分。记 $H=2\sqrt{k_-}>0$。由 (3)，$h\ge H\tau^{3/2}$。

当 $k\ge2B_0\tau$ 时，$|v|\ge k-B_0\tau\ge k/2$，所以 $k/h\le2$。当 $k\le2B_0\tau$ 时，$k/h\le(2B_0/H)\tau^{-1/2}$。若 $B_0=0$，$k=0$ 的点直接取 $k/h=0$。因此全域

$$
 \frac{k}{h}\le2+\frac{2B_0}{H}\tau^{-1/2},\qquad
 \frac{\tau^2}{h}\le\frac{\sqrt\tau}{H}.
$$

代入 (17)–(19)，(5) 可取

$$
 C_0^*=V_2+2A+\frac{2B_1^2\sqrt{\tau_0}}H,
 \qquad C_1^*=\frac{2AB_0}{H}.
 \tag{20}
$$

尤其对 $0\le\varepsilon\le\tau_0$，

$$
 \int_{S-\varepsilon}^S|h_{uu}|\,ds
 \le C_0^*\varepsilon+2C_1^*\sqrt\varepsilon.
 \tag{21}
$$

这包含 $k$ 与 raw 项在 $k\asymp\tau$ 尺度相消的情形，没有误用 $h\ge k$，也没有除以 $n$。

## 6. 真实值与角一导 cut 迹

令 $D=B_0+2\sqrt{k_+\tau_0}$。对三维向量 $(v,2\sqrt K)$ 使用反三角不等式，得

$$
 |h-k|\le |\rho|+2\sqrt K\le D\tau.
 \tag{22}
$$

令 $V=\sqrt{2M_2+4M_0}$。对 $k>0$，单位向量比较给

$$
 \left|\frac{(v,2\sqrt K)}h-(e,0)\right|\le\frac{2D\tau}{k}.
$$

当 $k\ge\tau$ 时，将此式与
$|k_ue+ke_u|\le V\sqrt k$ 相乘，得
$|h_u-k_u|\le2DV\sqrt\tau+B_1\tau$。
当 $0\le k\le\tau$ 时，直接用 $|h_u|\le|v_u|$ 和 (11)，得
$|h_u-k_u|\le(V+\sqrt{2M_2})\sqrt\tau+B_1\tau$。所以全角

$$
 |h_u-k_u|\le J\sqrt\tau+B_1\tau,\qquad
 J=\max(2DV,V+\sqrt{2M_2}).
 \tag{23}
$$

$a(s)\to a_c$、$\eta(s)\to1$，且 $\kappa\in C^2$，保证 $k,k_u$ 一致趋于 cut 尾函数的对应导数。结合 (16)、(22)、(23) 与 (4)，完整三个分量的值及角一导均一致趋于 (2) 的真实 cut 迹。此论证包括 $\kappa(a_c\sin u)=0$ 的所有角点和开弧。

角二导的统一极限没有由此推出。仅由 (18)–(20) 得

$$
 |m_{uu}|\le V_2/2,\qquad
 |l_{uu}|,|n_{uu}|\le(C_0^*+V_2)/2+(C_1^*/2)\tau^{-1/2}.
 \tag{24}
$$

故 $\alpha=(m,-l,0)$ 可取

$$
 |\alpha_{uu}|\le A_{20}+A_{21}\tau^{-1/2},\quad
 A_{20}=C_0^*/2+V_2,\quad A_{21}=C_1^*/2.
 \tag{25}
$$

同时可取有限常数

$$
 \begin{aligned}
 A_0&=\tfrac32M_0+\tfrac12(D+2B_0)\tau_0,\\
 V_1&=V\sqrt{M_0}+B_1\tau_0,\qquad A_1=\tfrac32V_1,
 \end{aligned}
 \tag{26}
$$

使 $|\alpha|\le A_0$、$|\alpha_u|\le A_1$。这些保守常数足够完成存在性与后验尾积分，未称它们是实际最大值。

## 7. R124 实际角变分到 cut 的极限

R124 的实际系统为 $F_s=F[\alpha]_\times$、$X_s=Fe_1$，以及体变量

$$
 \begin{aligned}
 r_s&=r\times\alpha+\alpha_u,&
 b_s&=-\alpha\times b+r\times e_1,\\
 v_s&=v\times\alpha+r\times\alpha_u+\alpha_{uu},&
 c_s&=-\alpha\times c-\alpha_u\times b+v\times e_1.
 \end{aligned}
 \tag{27}
$$

这里体变量 $v=r_u$ 与第 1–6 节的二维向量 $v=(d,2M)$ 不是同一个对象；本节及程序 `body_variation_bounds` 中始终使用 R124 的体变量意义。

令在 $s_0=S-\tau_0$ 的真实体变量范数上界为 $R_i,B_i,V_i,C_i$。记

$$
 I_2(\varepsilon)=A_{20}\varepsilon+2A_{21}\sqrt\varepsilon.
$$

每个叉积齐次项都是反对称的，不增加欧氏范数。依次积分得到

$$
 \begin{aligned}
 R&=R_i+A_1\tau_0, & B&=B_i+R\tau_0,\\
 V_b&=V_i+RA_1\tau_0+I_2(\tau_0),&
 C_b&=C_i+(A_1B+V_b)\tau_0.
 \end{aligned}
 \tag{28}
$$

它们分别界定 $|r|,|b|,|v|,|c|$。由 (27)，在长度 $\varepsilon$ 的终端区间内，增量范数分别至多

$$
 \begin{aligned}
 d_r&=(A_0R+A_1)\varepsilon,&d_b&=(A_0B+R)\varepsilon,\\
 d_v&=(A_0V_b+RA_1)\varepsilon+I_2(\varepsilon),&
 d_c&=(A_0C_b+A_1B+V_b)\varepsilon.
 \end{aligned}
 \tag{29}
$$

右端趋零，所以四个实际体变量具有全角统一 cut 极限。$F\in SO(3)$ 且 $|\alpha|$ 有界，也给出 $F$ 的统一极限。

在每个截断区间 $[s_0,S-\varepsilon]$，R124 的变分等于实际角导。由

$$
 F_u=F[r]_\times,\quad
 F_{uu}=F([v]_\times+[r]_\times^2),\quad
 X_u=Fb,\quad X_{uu}=F(r\times b+c),
 \tag{30}
$$

得到它们的统一极限。周期紧区间上函数及其前两导的一致收敛，保证极限确是 $F(S,\cdot),X(S,\cdot)$ 的前两角导，而不是独立命名的边界数组。

另由 $X_s=Fe_1$ 的角微分，直接有更简洁的真实位置尾界

$$
 |\Delta X|\le\varepsilon,\qquad
 |\Delta X_u|\le R\varepsilon,\qquad
 |\Delta X_{uu}|\le(V_b+R^2)\varepsilon.
 \tag{31}
$$

结合真实 $l$ 和角一导的连续 cut 迹，$X_{ss}=F(0,0,l)^T$、$X_{su}=F(r\times e_1)$ 也连续延拓。这正是位置图所需的 $C^2$ 单侧结构，没有加入径向 $C^3$ 要求。

## 8. R126 消费范围

在 cut 上，$F$ 是角向 $C^2$，而准确尾给出的 $l_c(u)$ 至少为角向 $C^2$。因此真实边界 jet 函数

$$
 J_0=X(S,u),\qquad J_1=F(S,u)e_1,\qquad
 J_2=F(S,u)(0,0,l_c(u))^T
$$

都有 R126 所需的角两导，其公式就是 R126 的式 (8)。**这不要求内部 $l_{uu}(s,u)$ 一致趋于 $l_{c,uu}(u)$**：这里对已经证明存在的边界函数求角导，未互换一个不受控的内部高阶极限。

要使用 R126 仍必须真实支付两片的位置/标架对齐、二 jet 失配及其全角上界。本文只保证真实输入存在，并给终端求值余项入口，不将形式 II 等式冒称位置拼接，也不将有限 ODE 容差冒成严格几何后验。

## 9. 可消费实现

`scripts/fd2d_gc_terminal_angular_majorant.py` 由实际有限控制和末 raw 行计算 (8)、(14)、(16)、(20)、(23)、(25)、(26)。所有主要常数是准确有理数；平方根以整数平方根产生明确向外 dyadic 端点。`terminal_integrals(packet,epsilon)` 给 (21)、(25) 的终端积分；`body_variation_bounds(packet,initial_bounds,epsilon=...)` 只在调用者提供真实初值上界后给 (28)–(31)，不暗填一个 body 初值。

标准 $κ$ 新域是 R170 的准确子盒，所以本入口支持全局负控制。R172 原 `AccurateLastCell` 的旧控制盒 guard 和已闭源码不因此修改；新的完整场 interval reader 必须显式选择新域 adapter，不能偷偷绕过旧 guard。当前准确 R172 输入上的常数计算不运行任何 body、BVP 或 whole F/J，其实际报告/退出和源码身份由对应闭存 manifest 绑定。
