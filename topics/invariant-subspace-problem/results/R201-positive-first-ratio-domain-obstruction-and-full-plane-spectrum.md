# R201：独立正一阶的比例商、正总锚的域障碍与全平面连续谱

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R201。

状态：完整实际证明。本文研究真实 Haar 表示中的有限组不交支持正一阶。
结论包括正总锚不能共同正则化独立分量、一个确切最大闭商及其原参数图核心、
无扰动比例商的全平面连续谱，以及定义域内循环性的双向保持。
最后把这个比例商与 R196 的双逆核方程精确连接。
不从这些全空间结论推出未知不变限制上的单核消失。

## 1. 设置与已证的实际输入

在原 Hilbert 空间 $H=L^2(\mathbb Z_2,\mu)$ 上，固定 $m\ge2$ 条实非负系数列
$$
b^{(i)}=(b^{(i)}_j)_{j\ge0}\in\ell^2\setminus\ell^1,
\qquad 1\le i\le m,
$$
其非零支持两两不交。零坐标允许；每个支持上的系数和发散。

记
$$
T_i=X_{b^{(i)}},\qquad
T_c=X_{\sum_i c_i b^{(i)}},\qquad
S_d=X_{\sum_i d_i b^{(i)}},
\tag{1.1}
$$
其中
$$
c=(c_1,\ldots,c_m)\in[0,\infty)^m\setminus\{0\},
\qquad d=(d_1,\ldots,d_m)\in\mathbb C^m.
$$
这里所有 $X$ 都是 R125 的真实闭第一阶实现，常数项取零。
(1.1) 不是先把无界算子的域作形式相加：
在共同有限柱核心上有相应线性式，其闭包就是所记的实际第一阶。

下文的非平凡情形为
$$
d\notin\mathbb C c.
\tag{1.2}
$$
这时 $d\ne0$，且对每个 $\lambda\in\mathbb C$，
$d-\lambda c$ 非零。

使用如下已经证明的实际结论。

1. R125 给每个复 $\ell^2$ 第一阶的 $C$ 自伴闭实现、有限柱图核心、
   全部有界 $A'$ 的域交换，以及每个非零第一阶向量的循环性。
   特别，非零系数第一阶的每个标量移位都单射、稠密像。
2. R128/R138 给每个非负非 $\ell^1$ 第一阶为空谱。
   所以
   $$
   L_c=T_c^{-1}\in A'
   $$
   全域有界、单射、稠密像、拟幂零。
   后两项也可由 $T_c$ 空谱及
   $I-\lambda L_c=(T_c-\lambda)T_c^{-1}$ 直接得到。
3. R186 给有限组第一阶的共同正则器。本文只用其一次版本：
   存在 $R(t)\in A'$，$t>0$，使
   $$
   R(t)\to I\quad\text{强},\qquad
   T_iR(t)\in A',
   \tag{1.3}
   $$
   且对每个固定 $t$，
   $$
   R(s)=R(t)U(s,t),\qquad U(s,t),U(s,t)^{-1}\in A'.
   \tag{1.4}
   $$
   $R(t)$ 单射、稠密像；它的任意正整数幂在每个有限放大不变子商上
   都具有强闭主理想单位。特别
   $$
   I\in\overline{R(t)\mathbb C[A]}^{\mathrm{SOT}}.
   \tag{1.5}
   $$
4. R125 的真实 carry 分解为
   $$
   T_i=T_i^0+K_i,\qquad
   T_i^0=\overline{\sum_j b^{(i)}_j S_j},\qquad
   S_j=I-2E_j,\qquad K_i\in B(H),
   \tag{1.6}
   $$
   且有限柱属于两端的共同域。可以取
   $\|K_i\|\le8\|b^{(i)}\|_2\|\eta\|_2$。
   本文不把 $K_i$ 设为零。
5. $A'$ 为交换代数，其中每个有界算子都 $C$ 对称并属于
   $\mathbb C[A]$ 的强算子闭包。因而它们保持所有闭 $A$ 不变空间，
   也逐分量保持有限放大中的闭不变图。

为避免重复，$R$ 未带参数时表示一次固定的 $R(t)$。

## 2. 有限乘积态的中心及一致真实余项

### 2.1 单个位的数值圆盘

物理基下
$$
S=I-2e_{10}.
$$
对单位向量 $v=(v_0,v_1)$，
其数值范围恰为
$$
W(S)=\{z:|z-1|\le1\}.
\tag{2.1}
$$
这是因为 $2v_0\overline{v_1}$ 遍历闭单位圆盘。
同时 $\|S\|=1+\sqrt2<3$。

真空向量 $\Omega=(e_0+e_1)/\sqrt2$ 满足
$$
\langle S\Omega,\Omega\rangle=0.
\tag{2.2}
$$

### 2.2 同一支持上指定总中心

固定一条 $b=b^{(i)}$、实数 $t_i$ 以及 $R_0>0$。
设希望第 $i$ 条第一阶的总中心为
$$
z_i=1+iR_0t_i.
$$
利用 $\sum_j b_j=\infty$，可选有限 $J_i$，使其总质量
$$
B_i=\sum_{j\in J_i}b_j
\ge\frac{1+R_0^2t_i^2}{2}.
\tag{2.3}
$$
于是
$$
\zeta_i=\frac{1+iR_0t_i}{B_i}
$$
满足 $|\zeta_i-1|\le1$。
在每个 $j\in J_i$ 选同一个具有期望 $\zeta_i$ 的单位位向量；
其余位仍取 $\Omega$。

注意：局部期望是 $\zeta_i$，不是通常在圆盘外的 $1+iR_0t_i$。
后者只在加上全部所选系数后成为总中心。

由于各支持不交，可以同时为所有 $i$ 作此选取，得到一个单位有限柱乘积向量
$x_{R_0}$。选位可以全部位于任意预先指定的有限头之后。

### 2.3 中心余项正交

对乘积向量，在第 $j$ 位减去其自身期望后的局部输出与原位向量正交。
因此不同位的中心余项两两正交，包括未选位的真空余项。
对每条支持有
$$
\left\|T_i^0x_{R_0}-z_i x_{R_0}\right\|^2
=
\sum_j (b_j^{(i)})^2
\left(\|S_jv_j\|^2-|\langle S_jv_j,v_j\rangle|^2\right)
\le9\|b^{(i)}\|_2^2.
\tag{2.4}
$$
无限未选尾在 $\ell^2$ 意义下收敛，且有限柱确在 $T_i^0$ 域中。

加回 (1.6)，置
$$
C_i=3\|b^{(i)}\|_2+\|K_i\|,
$$
得到真实算子估计
$$
\boxed{
\|T_i x_{R_0}-(1+iR_0t_i)x_{R_0}\|\le C_i.
}
\tag{2.5}
$$
常数与所选位数、所选总质量及 $R_0$ 无关。
这里保留的是有界真实 carry 误差，不是形式张量近似。

更一般，对任意 $e=(e_i)\in\mathbb C^m$，
共同核心上的实际线性式给
$$
\left\|S_e x_{R_0}
-\left(\sum_i e_i+iR_0\sum_i e_it_i\right)x_{R_0}\right\|
\le\sum_i|e_i|C_i.
\tag{2.6}
$$

## 3. 正总锚不能共同正则化独立分量

### 3.1 选择真正横向的实方向

若 $d\notin\mathbb C c$，存在 $t\in\mathbb R^m$ 使
$$
\sum_i c_it_i=0,\qquad \sum_i d_it_i\ne0.
\tag{3.1}
$$
否则 $d$ 作为复线性泛函在实超平面 $c^\perp$ 上为零，
其实部、虚部都与 $c$ 成比例，从而 $d\in\mathbb C c$，矛盾。

应用 §2 的有限柱向量，(2.6) 给
$$
\|T_c x_{R_0}\|
\le \sum_i c_i+\sum_i c_iC_i,
\tag{3.2}
$$
而
$$
\|S_d x_{R_0}\|
\ge R_0\left|\sum_i d_it_i\right|
-\left|\sum_i d_i\right|-\sum_i|d_i|C_i
\longrightarrow\infty.
\tag{3.3}
$$
因此在真实共同有限柱核心上不存在有限常数 $C$ 使
$$
\|S_dx\|\le C(\|T_cx\|+\|x\|).
\tag{3.4}
$$

### 3.2 实际乘积的无界性与严格域缺口

定义真正自然乘积
$$
Z_{d/c}=S_dL_c,\qquad
\operatorname{Dom}Z_{d/c}
=\{y\in H:L_cy\in\operatorname{Dom}S_d\}.
\tag{3.5}
$$
它闭：若 $y_n\to y$ 且 $S_dL_cy_n\to z$，
则 $L_cy_n\to L_cy$，用 $S_d$ 的闭性即可。

它的域稠密。有限柱是 $T_c$ 图核心，而 $T_c$ 满射，
所以 $T_c$ 的有限柱像在 $H$ 中稠密；这些像全属于 (3.5) 的域。

令 $y_{R_0}=T_cx_{R_0}$。
由 (3.2)，$y_{R_0}$ 有界；而
$$
Z_{d/c}y_{R_0}=S_dx_{R_0}
$$
范数发散。因此
$$
\boxed{d\notin\mathbb C c\ \Longrightarrow\ Z_{d/c}\text{ 无界}.}
\tag{3.6}
$$
因为它闭，闭图定理还给
$$
\boxed{
\operatorname{Dom}Z_{d/c}\ne H,\qquad
\operatorname{Dom}T_c\not\subseteq\operatorname{Dom}S_d.
}
\tag{3.7}
$$
这不是一般无界算子相加的抽象反例，而是在本题的真实有限柱上完成的估计。

若 $d=\lambda c$，则 $S_d=\lambda T_c$（$\lambda=0$ 时分子为零），
故乘积在全空间为 $\lambda I$。
所以
$$
\boxed{
S_dT_c^{-1}\text{ 全域有界}\quad\Longleftrightarrow\quad d\in\mathbb C c.
}
\tag{3.8}
$$

### 3.3 任意有界交换子扰动仍有同一相对域判据

设
$$
\mathsf C=T_c+H_c,\qquad
\mathsf D=S_d+H_d,\qquad H_c,H_d\in A'.
\tag{3.9}
$$
$H_c,H_d$ 均有界。$\mathsf C$ 仍为空谱：
对任意 $\lambda$，
$$
\mathsf C-\lambda
=
T_c\bigl[I+L_c(H_c-\lambda)\bigr],
$$
括号为单位，因为 $L_c$ 拟幂零且与 $H_c$ 交换。
其逆
$$
L=(\mathsf C)^{-1}
=[I+L_cH_c]^{-1}L_c\in A'
\tag{3.10}
$$
有界、拟幂零。

在 (3.2)—(3.3) 加上 $\|H_c\|,\|H_d\|$ 后，
同一有限柱测试给
$$
\boxed{
\mathsf D\mathsf C^{-1}\text{ 全域有界}
\quad\Longleftrightarrow\quad d\in\mathbb C c.
}
\tag{3.11}
$$
在比例情形 $d=\lambda c$，准确公式为
$$
\mathsf D\mathsf C^{-1}
=\lambda I+(H_d-\lambda H_c)L.
\tag{3.12}
$$
非比例情形的乘积仍闭、稠密定义、无界且定义域不是全空间。
这一节没有声称任意有界 $A'$ 扰动后的分子都单射。

## 4. 最大闭图、原参数核心及正锚分母的普遍性

本节允许 (3.9) 的任意有界 $A'$ 扰动。
取一次固定共同正则器 $R$，令
$$
F_c=\mathsf C R,\qquad F_d=\mathsf D R.
\tag{4.1}
$$
两者均为有界 $A'$ 元素，且
$$
F_cL=LF_c=R.
\tag{4.2}
$$
特别 $F_c$ 单射；其像包含 $RH$，所以稠密。

### 4.1 分母的强闭主理想单位

由 (1.5)、(4.2) 和 $L\in\overline{\mathbb C[A]}^{\mathrm{SOT}}$，
得到
$$
I\in\overline{F_c\mathbb C[A]}^{\mathrm{SOT}}.
\tag{4.3}
$$
确切地，先用 $Rp(A)=F_cLp(A)$ 逼近恒等，
再在每个指定的有限向量集合上，用多项式逼近固定的 $Lp(A)$。
只需选择有限精度；不要求同一个序列对所有多项式一致。

同理 $R=LF_c$ 给
$$
I\in\overline{L\mathbb C[A]}^{\mathrm{SOT}}.
\tag{4.4}
$$
这些结论可同时用于任意固定有限放大。
把相应闭不变子空间及商提升回原有限放大空间后，
它们仍给强闭主理想单位、单射、稠密像和不变子空间饱和性。

### 4.2 与自然乘积完全相同的最大图

记
$$
Z=\mathsf D L
$$
为 (3.5) 相同方式定义的自然乘积。则
$$
\boxed{
\operatorname{Graph}Z
=
\{(x,y)\in H^2:F_dx=F_cy\}.
}
\tag{4.5}
$$

正向：若 $y=\mathsf D Lx$，$F_c$ 与 $\mathsf D$ 域交换，
所以
$$
F_cy=\mathsf D F_cLx=\mathsf D Rx=F_dx.
$$

反向：若 $F_dx=F_cy$，乘 $L$ 得
$$
F_dLx=Ry.
\tag{4.6}
$$
实际闭算子 $\mathsf D$ 的最大正则化图为
$$
\operatorname{Graph}\mathsf D
=\{(v,w):F_dv=Rw\}.
\tag{4.7}
$$
这里可直接复证：由 $F_dv=Rw$，
令 $v_s=R(s)v$，则 $v_s\in\operatorname{Dom}\mathsf D$，
且
$$
R\mathsf Dv_s=F_dR(s)v=R(s)Rw.
$$
消去单射 $R$ 后 $\mathsf Dv_s=R(s)w$。
$s\downarrow0$ 时两端强收敛，闭性给 $\mathsf Dv=w$。
(4.6) 应用此式即得 $Lx\in\operatorname{Dom}\mathsf D$、$\mathsf DLx=y$。

### 4.3 原参数图确为图核心

原参数图是
$$
\{(F_ch,F_dh):h\in H\}.
\tag{4.8}
$$
它包含于 (4.5)，因为 $LF_c=R$。

若 $(x,y)$ 属于最大图，令
$$
h_s=L\,U(s,t)x.
$$
则
$$
F_ch_s=R(s)x,\qquad
F_dh_s=R(s)y.
\tag{4.9}
$$
第二式由 (4.6)、交换性和 $R(s)=RU(s,t)$ 得到。
所以 (4.8) 在图范数中稠密。

也可直接在最大图这个闭 $A\oplus A$ 不变空间上应用 (4.3)：
$F_c$ 的对角作用把 $(x,y)$ 送到 $(F_cx,F_dx)$，
而该对角作用有稠密像。
这给同一个原参数图核心。

因此改变共同正则器、改变其参数或添加无关的正则器因子，
都不会改变这个闭算子。本文的分式没有依赖未证明的形式除法。

### 4.4 全空间 C 自伴与域交换

$F_c,F_d$ 为有界 $C$ 对称算子。
用原参数图计算伴随：
$$
u\in\operatorname{Dom}Z^*,\ Z^*u=v
\quad\Longleftrightarrow\quad
F_d^*u=F_c^*v.
$$
这等价于 $(Cu,Cv)\in\operatorname{Graph}Z$，故
$$
\boxed{Z^*=CZC.}
\tag{4.10}
$$
此处先有实际原参数图核心，再识别完整伴随域。

任意有界 $B\in A'$ 与 $F_c,F_d$ 交换，
故 (4.5) 直接给 $B\operatorname{Dom}Z\subseteq\operatorname{Dom}Z$，
且 $ZB=BZ$ 于该域上。

### 4.5 有限放大子商中的准确范围

在任意有限放大闭 $A$ 不变子商 $Q$ 上，
有界算子 $R,F_c,F_d,L$ 均真正下降。
(4.3) 保证 $(F_c)_Q$ 单射、稠密像，
所以
$$
Z_Q=\{(x,y):(F_d)_Qx=(F_c)_Qy\}
\tag{4.11}
$$
是稠密定义的闭算子，原参数图仍是图核心。

同样，把 $\mathsf D_Q$ 定义为其标准最大正则化图
$(F_d)_Qx=R_Qy$，则
$$
\boxed{
\ker Z_Q=\ker\mathsf D_Q=\ker(F_d)_Q,\qquad
\overline{\operatorname{Ran}Z_Q}
=\overline{\operatorname{Ran}\mathsf D_Q}
=\overline{\operatorname{Ran}(F_d)_Q}.
}
\tag{4.12}
$$
这里只用分母单射和两个原参数图核心。
没有给商空间引入 $C$，也没有由分母的普遍性推断混合分子在所有子商上单射。

## 5. 移位的真实域、核及闭像

先继续允许 (3.9) 的有界扰动。
对 $\lambda\in\mathbb C$，置
$$
\alpha=d-\lambda c,\qquad
\mathsf D_\lambda
=S_\alpha+H_d-\lambda H_c.
\tag{5.1}
$$
其共同正则化分子是
$$
F_\lambda=F_d-\lambda F_c.
$$

由最大图直接得到
$$
\boxed{
Z-\lambda I=(F_c)^{-1}F_\lambda
=\mathsf D_\lambda L
}
\tag{5.2}
$$
作为同一个闭算子；其定义域仍为 $\operatorname{Dom}Z$。

最后一个实际乘积域等式可单独核对。
在 $\operatorname{Dom}\mathsf C$ 中，
$$
x\in\operatorname{Dom}\mathsf D
\quad\Longleftrightarrow\quad
x\in\operatorname{Dom}\mathsf D_\lambda,
\tag{5.3}
$$
且 $\mathsf D_\lambda x=\mathsf Dx-\lambda\mathsf Cx$。
对任一方向，用 $R(s)x$ 在两个已知图范数中逼近，
再用第三个闭算子的闭性即可。
因 $Lx$ 总在 $\operatorname{Dom}\mathsf C$，(5.3) 给所需同域。

两个最大图以同一个 $F_\lambda$ 为分子，故有准确恒等式
$$
\boxed{
\ker(Z-\lambda)=\ker\mathsf D_\lambda,\qquad
\overline{\operatorname{Ran}(Z-\lambda)}
=\overline{\operatorname{Ran}\mathsf D_\lambda}.
}
\tag{5.4}
$$
它也逐个成立于 §4.5 的有限放大子商。
这里的核相等比只写
$\ker(\mathsf D_\lambda L)=L^{-1}\ker\mathsf D_\lambda$
更强；额外输入正是普遍正则器的最大图与饱和性。

在无扰动情形，$d\notin\mathbb Cc$ 保证 $\alpha\ne0$，
所以 $S_\alpha$ 的系数列非 $\ell^1$。
由 R125 和 (5.4)，
$$
\boxed{
\ker(Z_{d/c}-\lambda)=0,\qquad
\overline{\operatorname{Ran}(Z_{d/c}-\lambda)}=H
\quad(\lambda\in\mathbb C).
}
\tag{5.5}
$$
也可由全空间 $C$ 自伴从单射推出稠密像。
(5.5) 不被外推到任意未知子商。

## 6. 无扰动比例商的全平面连续谱

### 6.1 每个分子只有两种第一阶谱类型

对任意非零 $\alpha\in\mathbb C^m$，
其系数列在第 $i$ 支持上为 $\alpha_i b_j^{(i)}$。
对于固定相位 $\theta$，
$$
\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)
=
\sum_i
\left(|\alpha_i|-\operatorname{Re}(e^{-i\theta}\alpha_i)\right)
\sum_j b_j^{(i)}.
\tag{6.1}
$$
每一行的后一个和都为无穷。
因此有限相位缺陷当且仅当
$$
\alpha=e^{i\theta}u,\qquad
0\ne u\in[0,\infty)^m.
\tag{6.2}
$$
零分量没有妨碍。

由 R138：
- 若 (6.2) 成立，$S_\alpha=e^{i\theta}T_u$ 为空谱；
- 若 (6.2) 不成立，$\sigma(S_\alpha)=\mathbb C$，且全部为连续谱。

### 6.2 全平面分子不允许比例商有有界预解

假设对某个 $\lambda$，$Z_{d/c}-\lambda$ 有全域有界逆 $G$。
由 (5.2)，
$$
S_\alpha L_cG=I,\qquad \alpha=d-\lambda c.
\tag{6.3}
$$
若 $S_\alpha$ 的谱为全平面，它单射；
于是 $L_cG$ 是其全域有界逆，
与 $0\in\sigma(S_\alpha)$ 矛盾。

### 6.3 空谱分子仍被相对域障碍阻断

若 $\alpha=e^{i\theta}u$ 如 (6.2)，则
$S_\alpha^{-1}=e^{-i\theta}L_u$ 有界。
由 (6.3) 及单射性，
$$
L_cG=S_\alpha^{-1}.
$$
所以 $S_\alpha^{-1}H\subseteq\operatorname{Dom}T_c$，
并且
$$
G=T_cS_\alpha^{-1}=e^{-i\theta}T_cL_u.
\tag{6.4}
$$
但是 $c\notin\mathbb C u$：
若 $c$ 与 $u$ 成比例，则
$d=\lambda c+e^{i\theta}u\in\mathbb Cc$，违 (1.2)。

现在把 §3 的正锚换成 $u$、横向分子换成 $c$。
它严格证明 $T_cL_u$ 无界且非全域，和 (6.4) 矛盾。

### 6.4 结论

两种分子类型都排除有界预解，结合 (5.5)：
$$
\boxed{
d\notin\mathbb Cc
\quad\Longrightarrow\quad
\sigma(Z_{d/c})
=\sigma_{\mathrm{continuous}}(Z_{d/c})
=\mathbb C.
}
\tag{6.5}
$$
全部点也属于近似点谱：
若某个 $Z_{d/c}-\lambda$ 有正下界，
其像将闭；由稠密像变成满射，闭图定理给有界逆，矛盾。

因此每个 $\lambda$ 有单位近似特征序列。
因为核为零，这些序列必弱趋零：
任意弱收敛子列与误差趋零一起给图的弱极限，
闭线性图弱闭，极限只能在零核中。
不需要把有限乘积态测试误称为所有复参数的直接近似特征序列。

## 7. 定义域内的循环性双向保持

本节对无扰动的任意 $Z_{d/c}-\lambda$ 成立。
更一般，只需全空间分子与分母均单射、稠密像，
并且具有 §4 的原参数图核心。

令 $Z=F_c^{-1}F_d$ 为这样的商。
若 $x\in\operatorname{Dom}Z$，则
$$
\boxed{
x\text{ 对 }A\text{ 循环}
\quad\Longleftrightarrow\quad
Zx\text{ 对 }A\text{ 循环}.
}
\tag{7.1}
$$

先设 $x$ 循环。
令 $\mathscr G_x$ 为
$$
\{(p(A)x,p(A)Zx):p\in\mathbb C[z]\}
$$
在 $H\oplus H$ 中的闭包。
它是包含于 $\operatorname{Graph}Z$ 的闭 $A\oplus A$ 不变空间。
$F_c$ 为强多项式极限，故其对角作用保持 $\mathscr G_x$。
因此 $\mathscr G_x$ 包含
$$
(F_cp(A)x,F_dp(A)x).
$$
$x$ 循环，且 $F_c,F_d$ 有界，
所以这些向量的闭包包含整个原参数图。
由原参数图核心，$\mathscr G_x=\operatorname{Graph}Z$。
于是 $Zx$ 的循环空间包含 $\operatorname{Ran}Z$ 的闭包，等于 $H$。

反过来，若 $Zx$ 循环，则 $F_cZx$ 循环：
$F_c$ 与 $A$ 交换且有稠密像。
而
$$
F_cZx=F_dx\in[x]_A,
$$
因为 $F_d$ 为强多项式极限。
所以 $x$ 也循环。

本节没有证明一般向量的两个循环子空间相等，
也没有假定 $F_d$ 在每个未知 $A$ 不变限制上像稠密。

## 8. Acal 有界扰动：仍为全平面谱，点谱边界必须保留

现在假定 (3.9) 中
$$
H_c,H_d\in\mathcal A,
\qquad d\notin\mathbb Cc.
\tag{8.1}
$$
§§3–5 的闭图、无界性、最大域与核/闭像恒等式全部保留。

对于 $\alpha=d-\lambda c$：

- 若 $\alpha$ 各非零分量同相位，则 $\mathsf D_\lambda$ 为空谱，
  因为它是一个旋转正空谱第一阶的有界交换扰动。
- 若不同时相位，R181 的一次、最高系数为 $I$ 的情形给
  $$
  \sigma(\mathsf D_\lambda)=\sigma_{\mathrm{ap}}(\mathsf D_\lambda)=\mathbb C.
  $$
  该结论不预先排除它的核。

假如 $Z-\lambda$ 有有界逆 $G$，
(5.2) 仍给 $\mathsf D_\lambda LG=I$，所以 $\mathsf D_\lambda$ 满射。
它是全空间 $C$ 自伴算子；
满射迫 $\ker\mathsf D_\lambda^*=0$，
继而迫 $\ker\mathsf D_\lambda=0$。
因此它将有有界逆。

在第二分支这直接矛盾。
在第一分支，$G=\mathsf C\mathsf D_\lambda^{-1}$，
又被 §3.3 的有界扰动相对域障碍排除。
故
$$
\boxed{\sigma(Z)=\mathbb C.}
\tag{8.2}
$$

但此时不能把 (8.2) 自动升级为全部连续谱。
准确结论是：
$$
\alpha=d-\lambda c\text{ 各非零分量同相位}
\ \Longrightarrow\
\lambda\text{ 属于 }Z\text{ 的连续谱}.
\tag{8.3}
$$
其他 $\lambda$ 的核由 (5.4) 与相应真实一阶加有界项的核完全相同，
可能仍是未解决的慢共振核。
(7.1) 只在已知相应分子全空间单射、稠密像时使用。

## 9. 两条正支持的平衡商与 R196 的双逆关系

取 $m=2$，写 $T_+,T_-$，并取
$$
c=(1,1),\qquad d=(1,-1).
$$
定义
$$
T_\Sigma=T_++T_-\quad\text{的真实闭实现},\qquad
L_\Sigma=T_\Sigma^{-1},
$$
以及
$$
Z_0=(T_+-T_-)L_\Sigma.
\tag{9.1}
$$
则
$$
\boxed{
Z_0\text{ 闭、}C\text{ 自伴、无界，}
\quad\sigma(Z_0)=\sigma_{\mathrm{continuous}}(Z_0)=\mathbb C.
}
\tag{9.2}
$$
特别
$$
\operatorname{Dom}T_\Sigma
\not\subseteq\operatorname{Dom}(T_+-T_-).
\tag{9.3}
$$
正总和的逆不是两个正分量的共同图正则器。

令
$$
L_\pm=T_\pm^{-1},\qquad
q=L_++L_-,\qquad p=L_+L_-.
$$
R197 的正余因子恒等式为
$$
qL_\Sigma=p.
\tag{9.4}
$$
这里可直接核对 $p$ 的强闭主理想单位，而无需推测其值域：
取共同正预解
$$
R(s)=(I+sT_+)^{-1}(I+sT_-)^{-1}
=p\,U_s,\qquad
U_s=(sI+L_+)^{-1}(sI+L_-)^{-1}\in A'.
\tag{9.4a}
$$
$U_s$ 及其逆均有界。$R(s)\to I$ 强，
而每个 $U_s$ 可在有限组向量上用 $A$ 的多项式强逼近，
所以 $p$ 具有强闭主理想单位。
由 (9.4) 再作同一强多项式逼近，
$q$ 也具有该性质，故在全部有限放大不变子商上单射、稠密像。

有准确的最大闭图
$$
\boxed{
Z_0=q^{-1}(L_--L_+).
}
\tag{9.5}
$$
不是只在核心上形式约分。

证明：在共同自然域上，
$$
(T_+-T_-)p=L_--L_+,\qquad T_\Sigma p=q.
$$
故参数图
$$
\{(qh,(L_--L_+)h):h\in H\}
$$
属于 $Z_0$ 的图。
反向可用 §4 的共同 $R$ 乘两端并消去单射因子，
或直接在最大关系中以 $p$ 的对角作用正则化：
$R$、$p$ 均为全有限放大图上的稠密正则器，
而 $pH$ 在 $T_\Sigma$ 和 $T_+-T_-$ 的共同一次图中是核心。
最后这个核心性由正逆与共同正预解的单位比给出，
等价地可用 $R(s)H$ 的共同逼近以及 $R(s)=p\,U_s$、
$U_s\in A'$。
因此上述参数图的闭包正是 $Z_0$ 的图。
$q$ 具有普遍图密度，参数图又是其最大关系的图核心，
所以两闭图一致。

若 $Y\in\mathcal A$ 有界，令
$$
X=T_+-T_-,\qquad
Z_Y=(X-Y)L_\Sigma,\qquad
K_Y=L_+-L_-+L_+YL_-.
$$
同一个论证给
$$
\boxed{
Z_Y=q^{-1}(-K_Y)
}
\tag{9.6}
$$
作为实际最大闭商，保留原参数图核心。
因此
$$
\boxed{
\ker Z_Y=\ker K_Y=\ker(X-Y),\qquad
\overline{\operatorname{Ran}Z_Y}
=\overline{\operatorname{Ran}K_Y}
=\overline{\operatorname{Ran}(X-Y)}.
}
\tag{9.7}
$$
这与 R196 的分母 $p$ 实现
$X-Y=p^{-1}(-K_Y)$ 相容：
两个分母都是已证明的普遍分母，而不是任意可消因子。

§8 还给 $\sigma(Z_Y)=\mathbb C$。
在本例中，$\alpha=(1-\lambda,-1-\lambda)$ 同相位恰当且仅当
$$
\lambda\in(-\infty,-1]\cup[1,\infty).
$$
故这些实参数必为连续谱；
特别不能把这个结论用于位于 $(-1,1)$ 内的 $\lambda=0$，
那里正是原慢分支可能保留的单核。

## 10. 对未知有界分支的准确后果与剩余点

若 $M$ 是非零闭 $A$ 不变空间，且
$$
M\subseteq\operatorname{Dom}(T_+-T_-),\qquad
(T_+-T_-)|_M=Y_M\in B(M),
$$
则 $L_\Sigma$ 保持 $M$，且对每个 $x\in M$，
$L_\Sigma x\in M\subseteq\operatorname{Dom}(T_+-T_-)$。
所以
$$
\boxed{
M\subseteq\operatorname{Dom}Z_0,\qquad
Z_0|_M=Y_M(L_\Sigma|_M)\in B(M).
}
\tag{10.1}
$$
两因子交换；$L_\Sigma|_M$ 拟幂零，因此这个有界限制拟幂零。

这给一个真实的归约：
未知有界第一阶分支会成为一个全平面连续谱闭比例商的有界拟幂零限制。
它没有构成矛盾。
全空间无点谱、全平面连续谱或比例商的自然域严格缺口，
均不能未经额外论证传成任意不变限制无核。

R196 中两个正分量在特定 $M$ 上的同域结论仍然有效；
§3 反而说明不能用它推断整个 $H$ 上的共同域。
R197/R198 的高位边界也不会自动保留未知核投影。

原慢二次共振单核、一般不变限制像，以及本课题完整不变子空间问题仍未解决。
