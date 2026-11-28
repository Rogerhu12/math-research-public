# 整个 b0 的同步四乘五原二次矩阵：同一伴随头、三个纯权相容式与原 D 恢复

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 状态：完整纸面恒等式与局部化后的原理想等价；没有执行新伴随矩阵、没有预记头或三个权式的非零性、因式、单位性或排空。
- 原范围：当前 W 的原 distinct-singleton、物理 $D\ne0$ 图及整个 $b_0=0$ 分支。所有既有原条件保留。

## 1. 五个原二次与系数环

沿[整个 b0 的五个原二次和六条权关系](R150-appendix-unit211-W-b0-inverse-slope-five-original-quadrics-six-weight-conditions.md)使用全支可逆权坐标 $(u,\nu)$；记 $A_W$ 为其原已付纯权单位的局部化环。本篇先在多项式环 $A_W[\lambda,f]$ 工作，不倒置任何新伴随头。

该结果的五个原式为

$$
J_5=(E_1,E_{B,e},E_{B,o},N_1,q_2)
=(q_f,r_1,r_2,r_3,q_2).
\tag{1}
$$

其中

$$
q_f=f^2+(a\lambda+b)f+c\lambda^2+d\lambda+e_0,
\qquad r_i=A_i(\lambda)+B_i(\lambda)f,
\tag{2}
$$

$a,b,c,d,e_0$ 为纯权系数，$\deg_\lambda A_i\le2$、$\deg_\lambda B_i\le1$。式 (1) 的双向来源已经由同一点真 Gram 与首一 $f$ 二次式证明；独立 $E_1$ 使用真 dual 乘法，不借错误 compact E1。

第五式 $q_2$ 由完整原值在物理 $D\ne0$ 域必要，但本篇所有多项式运算只正乘 $D$。$q_2$ 的首项没有被支付；它的全部二次降一次、一次降常数纤维仍保留。

这里的 $J_5$ 是原系统的必要子理想。原 $I_{11}$、原几何非零条件及剩余值关系仍保留；本篇不把 $J_5$ 单独称为充分物理系统。

## 2. 同步四乘五矩阵，不先消 lambda

令

$$
v=(1,\lambda,f,\lambda^2,\lambda f)^{\mathsf t}.
$$

取四条式子 $r_1,r_2,r_3,q_2$。它们都不含 $f^2$，也不含更高几何单项式。因此清除各行原已付权分母之后，恰可写成

$$
F=L v,\qquad
L=[\,c_0\mid B\,]\in A_W^{4\times5},\quad B\in A_W^{4\times4}.
\tag{3}
$$

$F$ 的每行都有相对于 (1) 左端五原源的纯权组合。各行清分母是原单位，不改变四条原式所生成的理想。这里先保四条同时的全部系数，不使用旧六个固定 Sylvester 投影，也不使用已冻结的 primitive PRS。

设

$$
h_{\rm raw}=\det B,\qquad
v_{\rm raw}=\operatorname{adj}(B)c_0.
$$

伴随矩阵的两个完整恒等式给

$$
\operatorname{adj}(B)F
=h_{\rm raw}
 \begin{pmatrix}\lambda\\ f\\ \lambda^2\\ \lambda f\end{pmatrix}
+v_{\rm raw},
\qquad
B\operatorname{adj}(B)=h_{\rm raw}I.
\tag{4}
$$

式 (4) 是完整多项式身份。此处没有 $h_{\rm raw}^{-1}$，所以整个 $h_{\rm raw}=0$ 面仍在原范围内。

## 3. 必须同时取消全部二十个实际原乘子

为减小后继系数，可以把 (4) 的四行各自复合到五个真正原源。记实际乘子为 $\gamma_{ij}\in A_W$，$1\le i\le4$、$1\le j\le5$。

令 $\Delta$ 是这二十个实际乘子的分母 LCM，只含旧已付纯权单位。令 $c_{\rm com}$ 为全部二十个分子 $\Delta\gamma_{ij}$ 的多项式共同因子，统一除掉这个同一个 $c_{\rm com}$，得到

$$
H_i=\sum_{j=1}^5\frac{\Delta\gamma_{ij}}{c_{\rm com}} F_j^{\rm orig}.
\tag{5}
$$

这里每个实际乘子都精确整除，故 $H_i$ 由 (5) 直接属于 $J_5$。没有把原方程除以未知单位。

这一步必须同时处理四行，不能分别归一而使它们得到四个不同的头。置

$$
h=\frac{\Delta}{c_{\rm com}}h_{\rm raw},\qquad
K=-\frac{\Delta}{c_{\rm com}}v_{\rm raw}
=(K_\lambda,K_f,K_{\lambda^2},K_{\lambda f})^{\mathsf t}.
$$

虽然此写法最初可在权分式域中理解，但 (5) 的右侧在 $A_W[\lambda,f]$。对四条不同单项式和常数项逐系数比较，便得 $h,K_j\in A_W$；后继实际源必须将其所有最终分母付回旧原权单位，不能凭上述分式写法另倒 $c_{\rm com}$。

于是四行准确变成

$$
\begin{aligned}
H_\lambda&=h\lambda-K_\lambda,\\
H_f&=hf-K_f,\\
H_{\lambda^2}&=h\lambda^2-K_{\lambda^2},\\
H_{\lambda f}&=h\lambda f-K_{\lambda f},
\end{aligned}
\qquad H_j\in J_5.
\tag{6}
$$

相应仍有

$$
BH=hF.
\tag{7}
$$

式 (6)、(7) 全部在原系数环内成立。全体共同因子 $c_{\rm com}=0$ 的权点并未丢失，因为新行本身有显示的 (5) 原组合。如果所有二十个乘子整式为零，只得到零伴随关系，不能宣称恢复或排空。

## 4. 三个纯权相容式的完整原来源

定义

$$
\begin{aligned}
S_1&=hK_{\lambda^2}-K_\lambda^2,\\
S_2&=hK_{\lambda f}-K_\lambda K_f,\\
S_q&=K_f^2+(aK_\lambda+bh)K_f
      +cK_\lambda^2+dhK_\lambda+e_0h^2.
\end{aligned}
\tag{8}
$$

它们都是纯权元素。其完整原来源不需要任何新头逆：

$$
\begin{aligned}
S_1&=(h\lambda+K_\lambda)H_\lambda-hH_{\lambda^2},\\
S_2&=h\lambda H_f+K_fH_\lambda-hH_{\lambda f},\\
S_q&=h^2q_f-
       (hf+K_f+ah\lambda+bh)H_f\\
   &\hspace{20mm}
       -\{aK_f+c(h\lambda+K_\lambda)+dh\}H_\lambda.
\end{aligned}
\tag{9}
$$

逐项展开即可核出 (9)，故三个 $S$ 都在 $J_5$。第三式保同一个首一 $q_f$ 的完整相容性；前两个单项式关系不能代替它。

后继若要约小 (8)，仍只能对复合 (9) 后的五个真正原乘子共同精除，然后把完整五源组合重新乘回。不能把 $S_i$ 自身的未付内容直接删掉。取消后新核在 $J_5$ 内，而原 $S_i$ 是该新核的多项式乘积乘旧单位，因此不会破坏下面的双向包含。

## 5. h 非零图上的完整 J5 消元

本节只描述明确的 $h$ 主开图，不把它外推到 $h=0$。若 $h$ 不是零多项式，则在 $A_W[h^{-1}]$ 上，由 (7) 可反向恢复原四行 $F$，所以

$$
J_5=(H_\lambda,H_f,H_{\lambda^2},H_{\lambda f},q_f).
\tag{10}
$$

再由 (9) 的反向式

$$
\begin{aligned}
hH_{\lambda^2}
   &=(h\lambda+K_\lambda)H_\lambda-S_1,\\
hH_{\lambda f}
   &=h\lambda H_f+K_fH_\lambda-S_2,\\
h^2q_f
   &=S_q+(hf+K_f+ah\lambda+bh)H_f\\
   &\hspace{20mm}
     +\{aK_f+c(h\lambda+K_\lambda)+dh\}H_\lambda,
\end{aligned}
$$

得完整原理想等价

$$
J_5=(H_\lambda,H_f,S_1,S_2,S_q)
\quad\text{于 }A_W[h^{-1}][\lambda,f].
\tag{11}
$$

于是该开图的多项式商恰为

$$
A_W[h^{-1}][\lambda,f]/J_5
\cong
A_W[h^{-1}]/(S_1,S_2,S_q),
\tag{12}
$$

其中

$$
\lambda=\frac{K_\lambda}{h},\qquad f=\frac{K_f}{h}.
$$

这是完整原商的同构，保全部重数；不是只给一个点集参数化，也不假设原有限环境自由。原物理系统还要在 (12) 上施加其余 $I_{11}$ 与原非零条件。

只有后继实际证明 $h$ 的所有支持都已由旧原单位支付，才可把 (11)、(12) 用到整个当前 b0。尚未执行任何这种支付或因式判定。

## 6. h 零面完整保留

由 (6) 直接得

$$
K_\lambda,K_f,K_{\lambda^2},K_{\lambda f}
\in J_5+(h).
\tag{13}
$$

所以在 $h=0$ 整面，四个 $K$ 也是必要纯权约束。但它们单独不取代原五个方程；此面继续保全部 $J_5$ 与 $I_{11}$。

若 $h$ 整式为零，根本没有第 5 节的开图。本篇仍只给四个直接原权关系 $-K_j=H_j$；它们可能全零。所有 rank-drop 或共同乘子零纤维均由这个准确分支处理，没有从函数域秩推出原全支为空。

## 7. 原 D 的直接恢复关系

在本篇 $T=-\kappa(3-2\lambda)$ 的整 b0 图，原

$$
D=\ell(2\lambda^2-2\lambda+1)-T^2
=d_2\lambda^2+d_1\lambda+d_0
$$

的三个系数都是纯权元素。定义

$$
C_D=d_2K_{\lambda^2}+d_1K_\lambda+d_0h.
$$

无需任何新逆，完整原身份为

$$
hD-C_D
=d_2H_{\lambda^2}+d_1H_\lambda\in J_5.
\tag{14}
$$

这提供与未知纯权常数相连的直接原 $D$ 目标。后继须按实际输出区分：

- 若 $C_D$ 不是零式，(14) 只是准确恢复关系，不能称 $D$ 已为零。
- 若 $C_D$ 整式为零，则 $hD\in J_5$；在本来就要求 $D\ne0$ 的物理原域，只有 $h=0$ 还能保留。
- 若在后一情形还真实证明 $h$ 仅含旧已付单位，才可排除整个当前 b0。
- 无论哪种情形，都不能因模 $D$ 幂零、函数域一次采样或未知权范数而替代 (14) 的完整原返回。

## 8. 执行边界

本篇已完成的是 (3)–(14) 的显示代数推导。矩阵参数由旧五二次必要定义唯一给定，但本篇未计算其新伴随系数或三个 $S_i$，不预记非零、多项式次数、共同支撑、完整纯 u 覆盖或任何排空。

后继若实例化，只能从已成真 Gram、$q_f,r_i,q_2$ 的必要定义前缀进入这个新的同步四乘五输入；不重放六个旧 Sylvester 投影、原 PRS、旧 $C_{74},C_{78}$ 或其 gcd。所有原五源逐项乘回、共同取消及最终分母支付都必须随这个新输入实际给出。
