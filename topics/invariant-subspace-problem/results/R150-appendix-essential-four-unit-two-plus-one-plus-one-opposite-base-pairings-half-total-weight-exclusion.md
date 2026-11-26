# R150 附录：单位 2+1+1 的相反基点配对与半总单点权支路为空

作者：Astra-ISP-347c-20261126 / unit31_general；AI-assisted GPT-6 Astra Pro。日期：2026-11-26 UTC。

**状态：本条精确范围已证明。** 在[同一原单位 2+1+1 与孤立零点支路](R150-appendix-essential-four-unit-two-plus-one-plus-one-one-zero-base-pairing-exclusion.md)中，本条排除 $p=1,q=-1$、$b+c=1/2$、$b-c\ne0$ 的全部情形。$b=c$ 的相反配对纤维已由[零基点 mean 专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-pairings-zero-base-mean-exclusion.md)排除，故两条合起来排除 $q=-1,b+c=1/2$ 的整个纤维。这里没有声称其他总单点权或整个 ISP 已解决。

## 1. 原方程和零点 mean 所给的低次相容式

继续保留原长度五除子 $2A+B+C+Z$、同一物理曲线、同一原六维非退化配对、全部原值和 jet。活跃单位代数为
$$
\mathcal B=\mathbb C[\epsilon]/(\epsilon^2)\oplus\mathbb C\oplus\mathbb C,
\qquad \tau(X)=aX_0+X_1+bX_B+cX_C,\quad a=1-b-c.
$$
设原孤立零点的配对列为 $U=(u_0,u_1,u_B,u_C)$，$m=\tau(U)$。原活跃 Gram 是
$$
K_B=\begin{pmatrix}
0&0&1&-1\\
0&A_1&r&s\\
1&r&0&t\\
-1&s&t&0
\end{pmatrix}.                                                   \tag{1.1}
$$
定义 $D_KX$ 的第 $i$ 分量为 $\tau((K_B)_{i,\bullet}X)$，并令
$$
d=D_K1,\quad f=\tau(d)/2,\quad
P(X)=\tfrac12\tau(X-\tau(X)1)^3,
$$
$$
N(X)=\tfrac12\tau((d-f1)X^2)-\tau(X)\tau(dX)
       +f\tau(X)^2+\tfrac14\tau(XD_KX).                            \tag{1.2}
$$
原 active mean 是
$$
E=e-2D_Kd-2d^2+4fd=0,
\quad e=(\tau k_0^2,2\tau k_0k_1,\tau k_B^2,\tau k_C^2),           \tag{1.3}
$$
其中 $k_i$ 为 (1.1) 的各行。写 $P_0,P_1,P_B,P_C$ 为 $P$ 在这些行的原值和一阶 jet；$N_i$ 同理。原最高式和第二梯度要求
$$
(P_0,P_1,P_B,P_C)=(-u_0^3,-3u_0^2u_1,-u_B^3,-u_C^3),
$$
$$
(N_0,N_1,N_B,N_C)=(-mu_0^2,-2mu_0u_1,-mu_B^2,-mu_C^2).             \tag{1.4}
$$

还要保留孤立零点本身的完整 mean 与最高式。在这里原 $T_2$ 为活跃二次式 $\tau(X)^2-\tau(X^2)/2$，原 $T_3=P+R^3$。完整 mean 的零点分量是 $T_2(U)$；其余项只有活跃分量。由原五个 jets 独立，得到
$$
\tau(U^2)=2m^2,\qquad P(U)=0.                                    \tag{1.5}
$$
这正是已登记[原零点 mean](R150-appendix-essential-four-unit-three-plus-one-isolated-zero-zero-base-pairing-branch-is-empty.md)的 (1.6)，也直接来自[完整低次梯度恒等式](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)的 (2.2)。该零点分量与活跃局部代数的长度分拆无关。

记
$$
\overline P=aP_0+P_1+bP_B+cP_C,\qquad
\overline N=aN_0+N_1+bN_B+cN_C.
$$
由 (1.4)，$\overline P=-\tau(U^3)$，$\overline N=-m\tau(U^2)$。所以 (1.5) 给以下完全无除法的必要式：
$$
S:=\overline P-2\overline N=0,\qquad
\Lambda_0:=2N_0^3-\overline N P_0^2=0,\qquad
c_0:=3P_0N_1-2N_0P_1=0.                                           \tag{1.6}
$$
可逐项核验的身份为
$$
S+2P(U)+m\bigl(\tau(U^2)-2m^2\bigr)=0.
$$
因此 (1.6) 保留了原零点 mean 的共同范数约束；没有把两两范数相容式当成充分条件，也没有除以 $m$ 或某个 $u_i$。

## 2. 半总单点权的完整 mean 分拆

令
$$
u=b-c\ne0,\qquad b=\frac{1+2u}{4},\quad c=\frac{1-2u}{4},
\quad a=\frac12,\quad e_*=u^2.
$$
原 Frobenius 条件 $bc\ne0$ 正是 $4u^2-1\ne0$。设 $x=d_B,y=d_C$，并写
$$
X=\frac{x+y}{2},\quad v=x-y-1,\quad w=ut,\quad T=uX.              \tag{2.1}
$$
原 $E_0=0$ 可且仅可解为
$$
f=\frac X2+\frac u2+\frac{v}{8u}.
$$
恢复原 Gram 参数的式子为
$$
r=X+\frac v2-ct,\quad s=X-\frac v2-bt,
\quad A_1=2f-X-u(v+1)+2bct.                                      \tag{2.2}
$$
这里只用了已知非零的 $u$。其余两个单点 mean 经过可逆线性组合为
$$
E_+=u^2(E_B+E_C)=(v-w)T+u^2(2w-v^2-vw)+\frac{w^2}{2},
$$
$$
E_-=u(E_B-E_C)=2(w-v)(T-u^2)+\frac{(v-1)(v+w)}2-w^2.
$$
精确恒等式
$$
2E_++E_-=-2\left(u^2-\frac14\right)(v-1)(v+w)                   \tag{2.3}
$$
和 $4u^2-1\ne0$ 给完整分拆
$$
v=1\quad\text{或}\quad w=-v.                                    \tag{2.4}
$$
下面保留两面的所有交点和原 $E_1$；这里没有用 Cramer 分母删除奇异面。

## 3. $w=-v$ 面：零纤维与非零族

代入 $w=-v$ 后，$E_+=2v(T-u^2+v/4)$。

### 3.1 $v=0$

此时 $w=t=0$，$X$ 尚自由，原式 (2.2) 是
$$
A_1=0,\quad r=s=X,\quad f=(X+u)/2.
$$
由同一原 $P,N$，相容式精确为
$$
c_0=-\frac{3X^2(4u^2-1)^2}{32}.
$$
因此 $X=0$，且
$$
P_0=\frac{u(4u^2-1)}4\ne0,\qquad P_1=P_B=P_C=0.
$$
原最高值和 jet (1.4) 给 $u_0\ne0,u_1=u_B=u_C=0$。此时完整五维 Gram 的 $B,C,Z$ 行分别为 $(1,0,0,0,0)$、其负数和它的 $u_0$ 倍，$A$ 的一阶 jet 行为零，故完整 Gram 秩恰为二。原长度五 jets 在六维空间独立；非退化配对限制到五维子空间的根基维数至多一，故限制秩至少四。这排除本纤维。

### 3.2 $v\ne0$

现在 $T=u^2-v/4$，故 $t\ne0$，(2.2) 恰化成真正的原 mean 族
$$
r=s=u,\qquad A_1=\frac{t(4u^2-1)}8,\qquad f=u.                   \tag{3.1}
$$
四个 active mean 在此全部恒为零，没有再删去任何一个。原 (1.6) 则精确为
$$
S=\frac{t(4u^2-1)\bigl(t^2(4u^2-1)-12\bigr)}{128},
$$
$$
c_0=\frac{3(4u^2-1)^2
 \bigl(t^2(4u^2-1)+4tu(4u^2-1)-16u^2\bigr)}{512}.                 \tag{3.2}
$$
利用仅有的已知非零量 $t,4u^2-1$，得到
$$
t^2(4u^2-1)=12,\qquad tu(4u^2-1)=4u^2-3.
$$
令 $e_*=u^2$，消去 $t$ 的无除法身份为
$$
(4e_*-3)^2-12e_*(4e_*-1)=-(8e_*-3)(4e_*+3).
$$
所以只剩两种完整纤维：
$$
e_* =\frac38,\quad t=-\frac3u;
\qquad
e_*=-\frac34,\quad t=\frac{3}{2u}.                               \tag{3.3}
$$
仍然把 (3.3) 代回同一原 $P,N$。第二个必要式 $\Lambda_0=0$ 的精确有理读数为
$$
u^3\Lambda_0=-\frac{135}{65536}\quad(e_*=3/8),\qquad
u^3\Lambda_0=\frac{1431}{2048}\quad(e_*=-3/4).                    \tag{3.4}
$$
二者均非零。计算在 $\mathbb Q[u]/(u^2-e_*)$ 中完成，保留了每个 $u$ 的两个平方根，没有选择符号。故 (3.1) 的全部非零族也被排除。

## 4. $v=1$ 面：保留最后两个代数纤维

这一面有
$$
E_+=(1-w)(T-u^2)+w^2/2.
$$
若 $w=1$，则 $E_+=1/2$，不可能为零。因此
$$
T=u^2-\frac{w^2}{2(1-w)}.                                      \tag{4.1}
$$
在原 $u^2E_1$ 中代入 (4.1) 后，精确得到
$$
u^2E_1=-\frac{(4u^2-1)(w+1)(w^2+2w-1)}{8(w-1)}.                \tag{4.2}
$$
$w=-1$ 属于上一节已完整处理的 $w=-v$ 面。其余必须满足
$$
Q_w=w^2+2w-1=0.                                                 \tag{4.3}
$$
把 (4.1)、$X=T/u$、$t=w/u$、$v=1$ 代回 (2.2) 和原 $P,N$。所得分母只含 $2,u,w-1$，均已证明非零。分别把化简后的 $S,c_0$ 分子对 $Q_w$ 取余，精确为
$$
\operatorname{num}(S)\bmod Q_w
 =4(4u^2-1)(8u^2w-4u^2-5w+2),
$$
$$
\operatorname{num}(c_0)\bmod Q_w
 =6(4u^2-1)^3(8u^2w-4u^2-w+1).                                 \tag{4.4}
$$
必要式 $S=c_0=0$ 迫右侧两个线性括号同时为零；二者相减给 $4w-1=0$。但
$$
Q_w(1/4)=-7/16\ne0.
$$
所以 (4.3) 的两个根均被排除。至此 (2.4) 的所有面、交点和新除数的零纤维已全部支付，得到本条结论。

## 5. 原式复算与范围

配套[自含 QQ 源](../notes/2026-11-26-unit211-opposite-half-total-weight-347c.py)直接从 (1.1)–(1.3) 的原 Frobenius 乘法重建全部 mean、原最高值和 jet、第二梯度值和 jet，精确核验 (2.3)、两面分拆、(3.2)–(3.4)、(4.2)、(4.4) 以及 (1.6) 的无除法身份。只使用有理数恒等式与二次取余，不保存计算数组。

实际执行为 Python 3.12.14、SymPy 1.14.0 下运行 `python 2026-11-26-unit211-opposite-half-total-weight-347c.py`，无需 FLINT；exit 0，程序计时 1.939650 秒，峰值 RSS 50416 KiB。源码 SHA256 为 `b4aafd09dde79b792e80d591226791b52a368be77f948bdd5fd4c0b3015f3fef`；小执行记录由主交接统一登记。

排除仅使用原完整临界性必需满足的条件；没有以这些条件反向制造真实临界点，没有改变物理配对或舍弃原 jet。全程未选有限点仿射坐标，因此同一原 divisor/jet 模型中允许的无穷远情形亦在这个参数排除内。本条关闭 $p=1,q=-1,b+c=1/2$ 的非零基点 mean 分支；一般 $q=-1,b+c\ne1/2$ 以及其他非零基点 mean 分支仍须继续研究。

**后续完整闭合（2026-11-26）：** 本条保持原已证明范围，余下相反配对一般图已由[完整相反配对专条](R150-appendix-essential-four-unit-two-plus-one-plus-one-opposite-base-pairings-exclusion.md)关闭；整个 $p=-q\ne0$ 不再是待做分支。
