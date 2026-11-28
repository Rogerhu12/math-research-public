# R150 推论：一般 unit 2+1+1 的固定 $(\lambda,T)$、$P_f$ 图原首一三次与三个生成元

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127。日期：2026-11-28。

**状态：完整纸面推论，无新增运行。** 本文把已刊碰撞图的首一 $t^3$ 证明推广到一般固定谱参数图。先令两个 weighted N/P 目标为任意纯参数，再说明真实原值的专门化。没有把未列的 singleton 值隐藏在系数环内；没有假设 $h=k$、$\ell=A_\lambda^3/B_\lambda^2$、$\Phi=0$、$\Delta\ne0$、$2\ell-1\ne0$ 或物理 $D\ne0$。

## 1. 系数环、真实 Gram 和仿射恢复

置

$$
\begin{gathered}
a=1-\ell,\quad m=u-\ell,\quad \delta=1-Q,\quad
V_2=2u-\ell Q,\quad M=\ell V_2-u^2,\\
T_0=V_2-2u^2,\qquad J=2u(1-u)+\ell Q,\\
P_{02}=(2-3u)V_2-Qu+2u^3,\qquad
P_f=T_0(J-Q),\\
\Phi=T_0+4u-4+Q,\quad
G=\lambda P_{02}-(1-u)T_0,\\
P_c=QP_{02}(\ell+T)-GT_0.
\end{gathered}
$$

从以下明确系数环出发：

$$
A=\mathbb Q[u,Q,\ell,\lambda,T,c_N,c_P,
              (Q\delta M P_{02}P_f)^{-1}].
\tag{1}
$$

$\lambda,T,c_N,c_P$ 在这里都属于纯参数；几何变量只有后文的 $t$。结论允许任意系数扩张 $A\to A'$，只要求 (1) 中的单位继续为单位。

先在有限自由二次扩张

$$
A_\rho=A[\rho]/(\rho^2-\delta)
$$

中写真实有序权：

$$
p=1+\rho,\quad q=1-\rho,\quad
b=\frac{\ell}{2}+\frac{m\rho}{2\delta},\quad
c=\frac{\ell}{2}-\frac{m\rho}{2\delta}.
$$

于是 $pq=Q$、$b+c=\ell$、$bp+cq=u$、$bc=M/(4\delta)$，所以 $bp,cq,bc$ 都为单位。没有除以 $m$ 或 $\ell$。

取 unit $2+1+1$ 的真 Frobenius 代数与 Gram：

$$
\tau(v)=av_0+v_1+bv_B+cv_C,\qquad
\mathbf1=(1,0,1,1),
$$

$$
K=\begin{pmatrix}
0&0&p&q\\
0&A_1&r&s\\
p&r&0&t\\
q&s&t&0
\end{pmatrix}.
$$

乘法的 dual 分量为 $(vz)_1=v_0z_1+v_1z_0$。沿原 $E_0,N_0,P_1$ 图，令 $w=\lambda-1-T$，已刊原仿射身份给

$$
QV=Jf-G+bcQt,\qquad
P_ff+bc\Phi Qt+P_c=0.
\tag{2}
$$

故在整个 (1) 上，

$$
f(t)=-\frac{P_c+bc\Phi Qt}{P_f},\qquad
V(t)=\frac{Jf(t)-G+bcQt}{Q}.
\tag{3}
$$

再置

$$
W_1=\frac{T_0}{2}+2uf,\qquad
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},
$$

$$
X=x+\rho y,\quad Y=x-\rho y,\quad
r=X-ap-ct,\quad s=Y-aq-bt,\quad
A_1=2f-2V+2bct.
\tag{4}
$$

全部仅仿射于同一个 $t$。这些是已刊完整原恢复的恒等式，不是从一个必要结式任选解；正反方向只用 $Q,M,P_f$。特别没有独立的 $t_\infty=0$、$f$ 或 $V$ 无穷方向。

(2)–(4) 的一般原身份及下文原最高计算见
[固定谱碰撞图三生成正文](R150-appendix-unit211-hk-whole-fixed-spectrum-original-monic-t-three-and-three-generators.md)。
该正文的推导在这些位置没有使用碰撞值关系；本文明确扩大其系数环和目标。

## 2. 任意纯参数目标下的原理想

令 $g_0,g_1,g_B,g_C$ 为 $K$ 的四行，$d=D_K\mathbf1$、$F_2=\tau(d)=2f$。保留完整原多项式

$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)
       -4\tau(v)\tau(dv)+2F_2\tau(v)^2
       +\tau(vD_Kv),
$$

$$
P_2(v)=\tau((v-\tau(v)\mathbf1)^3).
$$

定义两个目标尚未专门化的原式

$$
NS_{c_N}=bN_4(g_B)+cN_4(g_C)-c_N,\qquad
PS_{c_P}=bP_2(g_B)+cP_2(g_C)-c_P.
\tag{5}
$$

令 $E_{B,e},E_{B,o}$ 为真原 $E_B$ 的 $\rho$ 偶、奇部分，$E_C$ 是其共轭。三个原均值在 (3)–(4) 上都为 $t$ 二次；(5) 为 $t$ 三次。所有纯参数目标不贡献这些几何最高项。

仍有全原身份

$$
\begin{aligned}
\mathcal R={}&4(f-u)(V-f)+bc\,t^2\\
 &+t\left(4bcu-\ell V+
       \frac{m(T_0+4uf-2V)}{2\delta}\right),\\
2\mathcal R+E_1-\ell E_{B,e}-mE_{B,o}
 -\left(\frac{mt}{\delta}-a\right)E_0&=0.
\end{aligned}
\tag{6}
$$

在已解 $E_0$ 图上，可用 $\mathcal R,E_{B,e},E_{B,o}$ 代替三个原均值，而不引入新逆元。记

$$
J_5=(\mathcal R,E_{B,e},E_{B,o},NS_{c_N},PS_{c_P})\subset A[t].
\tag{7}
$$

由于整个表达式在 $\rho\mapsto-\rho$ 下不变，(7) 确在 $A[t]$ 中。原 $N_1$ 及其他原值条件仍可加入 (7)；本文不把五式当成全部原问题的充分系统。

## 3. 四个实际最高系数在整个 $A$ 上生成单位理想

设

$$
L=NS_{c_N}-PS_{c_P}
   -V E_{B,e}-(mx+\ell\delta y)E_{B,o}.
\tag{8}
$$

它是完整原组合；后两项等于 $bX E_B+cY E_C$。取

$$
c_R=[t^2]\mathcal R,\quad
c_e=[t^2]E_{B,e},\quad c_o=[t^2]E_{B,o},\quad
c_L=[t^3]L,
$$

并令 $\mathfrak h=(c_R,c_e,c_o,c_L)\subset A$。

以下只核这个商环，始终保幂零结构。为简洁，将 (3)–(4) 的 $t$ 一次系数记成 $f,V,X,Y$；它们不是另添的自由坐标。由真 $E_0,N_0$，

$$
bX+cY=V,\qquad bpX+cqY=2uf,\qquad
Jf-QV+bcQ=0.
\tag{9}
$$

在 $(A/\mathfrak h)_\rho$ 中，原最高四式成为

$$
\begin{aligned}
R&=4f(V-f)+bc(1-2X-2Y)=0,\\
E_B&=c-2cY-2X^2+4fX=0,\\
E_C&=b-2bX-2Y^2+4fY=0,\\
1-2(X+Y)+2XY+2f&=0.
\end{aligned}
\tag{10}
$$

最后一式来自 $c_L=-2bc$ 乘该式，$bc$ 已付。令

$$
\xi=1-2X,\quad \eta=1-2Y,\quad P=\xi\eta,\quad S=\xi+\eta.
$$

则完整多项式推导给

$$
4f=1-\xi-\eta-P,\quad
2E_B=\eta(\xi^2+2c-1),\quad
2E_C=\xi(\eta^2+2b-1),
$$

$$
cq\,\xi+bp\,\eta+uP=0,
$$

$$
PR+P^3=-2PX^2E_C-2PY^2E_B+(S-1)E_BE_C.
\tag{11}
$$

因此 $P^3=0$；用上一线性式及 $bp,cq$ 单位，得到 $\xi^6=\eta^6=0$。于是 $(\xi,\eta)^{11}=0$。这一通用幂零推导见
[真最高原恒等式正文 §3–§4](R150-appendix-unit211-Phi-zero-corrected-whole-highest-unit-ideal-and-twenty-two-generators.md)；不使用该文从 §5 开始的 $\Phi=0$ 权关系。

模此幂零理想，$X=Y=1/2$、$f=1/4$、$V=\ell/2$，而 $R=0$ 给

$$
4bc=2\ell-1.
$$

最后 (9) 的固定 $\lambda$ 原 $N_0$ 最高线给

$$
0=\frac J4-\frac{Q\ell}{2}+bcQ=\frac{J-Q}{4}.
\tag{12}
$$

$J-Q$ 因 $P_f=T_0(J-Q)$ 为单位。因此一个单位落入幂零理想，整个商环必为零。有限自由扩张 $A\to A_\rho$ 忠实平坦，故

$$
\mathfrak h=A.
\tag{13}
$$

这是原系数环上的单位理想结论，不是只检查约化复点，也不要求显式展开四个 Bézout 系数。

## 4. 一般原首一 $t^3$ 与三个生成元

由 (13) 存在 $\alpha_R,\alpha_e,\alpha_o,\alpha_L\in A$ 满足

$$
\alpha_Rc_R+\alpha_ec_e+\alpha_oc_o+\alpha_Lc_L=1.
$$

所以

$$
q_t=\alpha_Rt\mathcal R+\alpha_etE_{B,e}
      +\alpha_otE_{B,o}+\alpha_LL
\tag{14}
$$

属于原 $J_5$，且是真首一三次。因此

$$
A[t]/J_5
\quad\text{由}\quad 1,t,t^2
\quad\text{作为 }A\text{ 模生成}.
\tag{15}
$$

每个包含 $J_5$ 的原方程商同样由三个元素生成，包括加完整 $N_1$ 的原 $I_6$ 以及进一步个别 N/P、完整 $N_4(V_{\rm phys})$ 的商。没有自由、平坦、秩恒为三或一般纤维恰三点的假设。

(14)–(15) 在任意系数扩张上保持。对于一个固定的全部纯参数纤维，原均值/weighted N/P 商长度至多三；后续原条件或该 Artin 纤维的局部化不会增加其长度。反之，在尚非零维的权环上，新增几何单位局部化一般不能无条件继续称为有限模，本文不作这个外推。

## 5. 真实一般原值如何专门化；没有隐藏 $h,k$

原 U 值坐标是 $\mathbf v=U/U_0=(1,w,h,k)$，$\lambda$ 为其原均值参数。这里的 $h,k$ 是两个 singleton 值，尚未施加碰撞。按
[原 U 值 atlas §1–§2](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)，真实矩关系是

$$
\begin{aligned}
a+w+bh+ck&=\lambda,\\
a+2w+bh^2+ck^2&=2\lambda^2,\\
a+3w+bh^3+ck^3&=4\lambda^3.
\end{aligned}
\tag{16}
$$

若定义 $T=b(h-1)+c(k-1)$，第一式给 $w=\lambda-1-T$。另两式直接给

$$
\begin{aligned}
bh^2+ck^2&=\ell+2T+A_2,\\
bh^3+ck^3&=\ell+3T+3A_2+B_3,
\end{aligned}
$$

其中 $A_2=2\lambda^2-2\lambda+1$、
$B_3=4\lambda^3-6\lambda^2+3\lambda-1$。所以真实 weighted 原值在本文中专门化为

$$
c_N=2\lambda P_{02}(\ell+2T+A_2),\qquad
c_P=P_{02}(\ell+3T+3A_2+B_3).
\tag{17}
$$

缩放完全按原 $N_4=4N$、$P_2=2P$、$P_{02}=2P_0$，故 (17) 没有混用归一。也可以先在系数扩张中显式加入 $\rho,h,k$ 及 (16)，直接令 $c_N=2\lambda P_{02}(bh^2+ck^2)$、$c_P=P_{02}(bh^3+ck^3)$；同一相对三生成结论成立。

本文因此没有把未列的 singleton 值或其自由轨道塞进 (1)。它只给固定 $(\lambda,T)$ 的原 $t$ 环境三生成，不给权空间有限性、整个原图排空、规范坐标全局点数、原矩阵点数或 $U_0$ 尺度计数。$P_f=0$ 整边界保留。

## 6. 记录边界

这是已成四头幂零证明的严格代数推论，无新算法或执行回执。没有重新运行原最高、旧 Loww、结式或大乘法门；也没有声称实际构造了 (14) 的显示系数。其适用范围由 (1)、(5)、(7)、(16)–(17) 明确限定。
