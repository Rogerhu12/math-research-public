# R150 附录：单位 2+1+1 的相反基点配对且基点 mean 为零支路为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 在[同一原单位 2+1+1 与孤立零点支路](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)中，本条排除归一参数 $p=1,q=-1$ 且 $d_0=b+cq=0$ 的全部情形。这里 $bc\ne0$，所以 $b=c\ne0$。其他 $pq\ne0$ 的一般支路尚不由本条排除。

## 1. 孤立零点本身的原最高式给一个额外必要条件

保留原长度五除子 $2A+B+C+Z$、同一原物理曲线、原非退化 $K$、单位代数
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\qquad \tau(X)=aX_0+X_1+bX_B+cX_C,\qquad a=1-b-c.
$$
记原零点配对列为 $U=(u_0,u_1,u_B,u_C)$，$m=\tau(U)$。完全沿用前稿由原 Frobenius 乘法定义的 $P,N,E$。原最高式与第二梯度在活跃点的值、一阶 jet 是
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2). \tag{1.1}
$$

还须在孤立零点 $Z$ 本身使用原最高式。其零点极坐标的值为原自配对，故为零；活跃极坐标正是 $U$。因此
$$
P(U)=0.                                                \tag{1.2}
$$
定义完全由同一原值和 jet 组成的多项式
$$
J=aP_0+P_1+bP_B+cP_C-3(aN_0+N_1+bN_B+cN_C).
$$
由于
$$
\tau(U^3)=a u_0^3+3u_0^2u_1+b u_B^3+c u_C^3,
$$
$$
\tau(U^2)=a u_0^2+2u_0u_1+b u_B^2+c u_C^2,
$$
直接代入 (1.1) 得到无除法恒等式
$$
\boxed{2P(U)=2m^3-J.}                                  \tag{1.3}
$$
故完整临界点必须满足
$$
2m^3=J,\qquad 2N_i^3+JP_i^2=0\quad(i=0,B,C).           \tag{1.4}
$$
这固定了两两范数相容式所没有固定的共同范数。它是原最高式在原零点处的必要条件，不是人为添加的归一，也不将任何范数条件视为充分。$m=0$、$u_i=0$ 等情形都包含在恒等式内。

## 2. 相反配对和零基点 mean 的完整原参数

本条令 $p=1,q=-1,b=c\ne0$，故 $a=1-2c$。原活跃 Gram 为
$$
K_B=\begin{pmatrix}
0&0&1&-1\\0&A_1&r&s\\1&r&0&t\\-1&s&t&0
\end{pmatrix}.
$$
设 $x=d_B$、$y=d_C$、$f=\tau(d)/2$。原 $E_0=0$ 精确给 $y=x-1$。令 $V=x-1/2$。因为
$$
P_0=0,
$$
原最高值迫 $u_0=0$，原最高 jet 因而还要求 $P_1=0$。此式给
$$
f=\frac{(2c+1)V-ct}{2}.                               \tag{2.1}
$$
没有除以除 $c$ 之外的变量，而 $c\ne0$ 是 Frobenius 单点权假设。其余原参数为
$$
r=V+\tfrac12-(1-2c)-ct,\quad
s=V-\tfrac12+(1-2c)-ct,
$$
$$
A_1=2f-4cV+2c^2t.                                     \tag{2.2}
$$
原 mean 余下三式为
$$
E_1=2V^2-4Vct+2c^2t^2+4c^2-c,
$$
$$
E_B=\tfrac12(8V^2c-8Vct+4Vc-2V+2ct^2+4c-1),
$$
$$
E_C=\tfrac12(8V^2c-8Vct-4Vc+2V+2ct^2+4c-1).             \tag{2.3}
$$
同一原第二梯度的基点值和 jet 为
$$
N_0=-\tfrac12Vc(2c-1),\qquad
N_1=\tfrac12c(2c-1)(-(4c+1)V+2ct).                     \tag{2.4}
$$
因为已经有 $u_0=0$，(1.1) 还要求 $N_0=N_1=0$。

## 3. $c\ne1/2$ 的全部情形

由 (2.4) 及 $c(2c-1)\ne0$，先得 $V=0$，再得 $t=0$。此时 (2.3) 给 $c=1/4$，其余式也成立。原参数准确为
$$
a=\tfrac12,\quad b=c=\tfrac14,\quad A_1=r=s=t=f=0.
$$
直接由原式计算，全部八个值和 jet $P_i,N_i$ 都为零。最高值给 $u_0=u_B=u_C=0$，而 (1.3) 给 $m=0$；因 $m=u_1$，还得到 $u_1=0$。

所以完整零点配对列 $U=0$，且活跃 Gram 只有秩二。完整五维 Gram 也只有秩二，违反由原长度五 jets 独立与原六维 $K$ 非退化得到的秩至少四。这一候选已彻底排除。

## 4. $c=1/2$ 的两个完整范数纤维

现在 $a=0,b=c=1/2$，这是允许的 Frobenius 权。原 (2.3) 三式等价于
$$
(2V-t)^2=-1.
$$
写 $\iota=2V-t$，故 $\iota^2=-1$；保留两个代数共轭值，不选取某个符号。由 (2.1)、(2.2)，
$$
A_1=0,\qquad r=\frac{\iota+1}{2},\qquad
s=\frac{\iota-1}{2}.
$$
全部原值进一步简化为
$$
P_0=P_1=N_0=N_1=0,
$$
$$
P_B=-\frac{2\iota+3t-2}{4},\qquad
P_C=-\frac{2\iota+3t+2}{4},\qquad
N_B=P_B/2,\quad N_C=P_C/2.                              \tag{4.1}
$$
因此
$$
J=(2\iota+3t)/8.
$$
把 (4.1) 代入原零点最高必要式 (1.4)，在 $\mathbb Q[t,\iota]$ 中与 $\iota^2+1$ 一起精确约化。其约化 Gröbner 基恰为
$$
\left\{t^2+\frac43\iota t-\frac89,\quad \iota^2+1\right\}.
$$
于是
$$
(3t+2\iota)^2=4.                                      \tag{4.2}
$$
实际上此处也可直接验证：令 $H=3t+2\iota$，两个必要式分别是非零常数倍的 $(H-2)^2(H+2)$ 与 $(H+2)^2(H-2)$，其共同零点恰为 $H=\pm2$。配套源从原式重建并核对了整个有理理想计算。

当 $H=2$ 时，$(P_B,P_C)=(0,-1)$，所以 $u_B=0,u_C^3=1$。由 $N_C=-1/2=-mu_C^2$，得 $m=u_C/2$。又 $m=u_1+(u_B+u_C)/2$，所以 $u_1=0$。

当 $H=-2$ 时，$(P_B,P_C)=(1,0)$，所以 $u_B^3=-1,u_C=0$。由 $N_B=1/2=-mu_B^2$，同样得 $m=u_B/2$，从而 $u_1=0$。

现在必须恢复原物理几何。用 $v_0,v_1$ 表示原双点的一对完整允许 jets，用 $w_Z$ 表示原孤立零点向量；这里 $u_0,u_1$ 是与 $w_Z$ 的配对标量。已有
$$
K(v_0,v_0)=K(v_0,v_1)=K(v_1,v_1)=0,
$$
$$
K(v_0,w_Z)=u_0=0,\quad K(v_1,w_Z)=u_1=0,\quad K(w_Z,w_Z)=0.
$$
因此同一原长度三支撑 $2A+Z$ 的完整 jet 空间全等向。然而[原长度三物理 jets 的全等向分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)已证明：这类全等向空间只能来自两个指定的三点约化支撑，任何 $2+1$ 支撑都不存在，包括无穷远。矛盾。这排除 (4.2) 的两个纤维。

## 5. 范围与实际核验

$c\ne1/2$ 和 $c=1/2$ 穷尽全部允许 $c\ne0$；没有删除 $a=0$、零 $P_i,N_i$、零 $m$ 或任何局部 jet。由此本条范围 $p=1,q=-1,b=c\ne0$ 全部为空。

配套[自含 QQ 源](../notes/2026-11-26-unit-two-plus-one-plus-one-opposite-zero-mean-347c.py)直接重建原 Frobenius 运算及 $E,P,N$，验证一般权下的恒等式 (1.3)、所有参数化、所有边界值和最后两个纤维；仅依赖 SymPy 1.14.0。实际执行元数据与源码 SHA256 见[小记录](../notes/2026-11-26-unit-two-plus-one-plus-one-opposite-zero-mean-execution-347c.json)。源内计时0.734565秒、峰值49524 KiB、exit0；源码SHA256为 `46abaa66e5947384e99d149668b6f2a99c84c030583b4fa8be12877eeaf287cd`。最初一次运行只在因式形式与展开形式的结构相等断言处失败；将其改为精确有理差为零后，完整源全部通过，数学定义和目标等式未改动。

本条仍是原有限临界分支的排除，未给出全局 Bell 幂来源，也未宣称已解决 Hilbert 不变子空间问题。下一剩余范围包括 $p=1,q\ne0,1$ 的其余零基点 mean 图和非零基点 mean 图。
