# R150 附录：内均值的本质三空间必为全等向空间

日期：2026-11-13（UTC）。作者：normal_rebuild / Astra-ISP-1cf8c51d。

状态：**已证明的完整进一步归约。** 对原六模式立方的完整临界点，若一次矩的 $4\times3$ Hankel 秩为三，普通第三矩的本质支撑 $W$ 为三维，且 $y\in W$，则 $K|_W=0$。若物理投影为二次曲线，则 $W=W_\pm$。剩余的唯一内均值支撑类型是：$W$ 与物理曲线的交除子准确长二，$H,V$ 的最小并支撑正是该除子，均值在其外，而投影是双有理的不可约平面三次曲线。本稿保留该最后一种类型，没有将它误判为不存在。

## 1. 已付支撑归约及本稿假设

仍用原完整多项式 $\mathcal Q_3(y,H,V)$、非退化对称矩阵 $K$、物理曲线 $v(z)=(1,z,\ldots,z^5)$ 及其射影延拓。普通第二、第三矩为
$$
T_2=yy^{\mathsf T}-2H,\qquad
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)H(r,r)+4V(r,r,r).
$$
本稿的假设始终是
$$
\nabla\mathcal Q_3=0,\qquad
\operatorname{rank}(y_{j+k})_{0\le j\le3,\ 0\le k\le2}=3,\qquad
\operatorname{ess}(T_3)=W,\quad \dim W=3,\quad y\in W.
\tag{1.1}
$$
这里 $\operatorname{ess}$ 是对称张量的最小线性支撑，不是任意选定的三空间。

[共同长度三与内均值二分归约](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md)已完整证明：要么 $W=W_\pm$；要么 $H,V$ 的唯一最小 jet 支撑之并是一个准确长度二的除子 $D$，其空间 $U$ 满足
$$
H\in\operatorname{Sym}^2U,\quad V\in\operatorname{Sym}^3U,\quad
\dim U=2,\quad y\notin U,\quad W=\mathbb Cy\oplus U.
\tag{1.2}
$$
$H,V$ 可以分别降秩，但它们的本质支撑之和准确等于 $U$。

$W_\pm$ 已知全等向，故以下只处理 (1.2)。取 $W$ 的基为 $y$ 后接 $U$ 的一组物理 jet 基，以 $t,x=(x_1,x_2)$ 表示对应对偶变量。于是
$$
T_3(t,x)=t^3-6tH(x,x)+4V(x,x,x).
\tag{1.3}
$$
两种准确长度二支撑给以下允许形式：
$$
\begin{array}{ll}
D=s_1+s_2,\ s_1\ne s_2:
&H=h_1x_1^2+h_2x_2^2,\quad V=v_1x_1^3+v_2x_2^3;\\
D=2s:
&H=h_0x_1^2+2h_1x_1x_2,\quad
 V=v_0x_1^3+3v_1x_1^2x_2.
\end{array}
\tag{1.4}
$$
第二行使用 $u_0=v(s),u_1=v'(s)$，在无穷远使用局部射影参数，不除以阶乘。它们来自原 Hankel 张量的有限 jet 表示。

## 2. 完整低梯度的三维块等式

写
$$
K|_W=
\begin{pmatrix}
2F&l^{\mathsf T}\\
l&G
\end{pmatrix},
\qquad F=\tfrac12y^{\mathsf T}Ky,\quad l=K(y,U),\quad G=K|_U.
\tag{2.1}
$$
此处 $H$ 也表示 (1.4) 的二阶矩阵块。原物理 Hankel 身份给
$$
\operatorname{tr}(GH)=\operatorname{tr}(KH)=0.
\tag{2.2}
$$

[原完整低梯度公式](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)的推导对任意原 $y,H,V$ 成立；本稿使用其身份本身，不使用该文外均值的附加假设。令 $p=Ky$，原十一个 $H$ 梯度恰给
$$
N=T_{3,p}-FT_2+4HKH,\qquad
N(Kv(z),Kv(z))\equiv0.
\tag{2.3}
$$
在 $\mathbb Cy\oplus U$ 的块分解下，直接收缩 (1.3) 得
$$
\boxed{
N_{00}=F,\qquad N_{0U}=-2(Hl)^{\mathsf T},\qquad
N_{UU}=-2FH+4V_l+4HGH.
}
\tag{2.4}
$$
$V_l$ 是 $V$ 与 $l$ 收缩一次后得到的二次张量。

同一原六个一次梯度为
$$
\frac13K^{-1}\nabla_y\mathcal Q_3
=(F^2-2b+2\tau_2)y-4FHp+8HKHp
 +4V(p,p,\cdot)-8V:(KHK),
\tag{2.5}
$$
其中 $b=l^{\mathsf T}Hl$、$\tau_2=\operatorname{tr}((GH)^2)$。除第一项之外，(2.5) 的全部向量均在 $U$ 内。用 $\lambda(y)=1,\lambda|_U=0$ 收缩，完整一次临界性迫
$$
\boxed{F^2-2b+2\tau_2=0.}
\tag{2.6}
$$
因此本稿不仅使用最高第三矩的单个曲线恒等式。

## 3. 二次曲线投影的矩分解与 H 的秩

[最高矩投影分类](R150-appendix-highest-moment-essential-support-and-cubic-projection-types.md)给出：因 $T_3$ 非零且本质维数三，三个物理投影五次式的像，要么是不可约二次曲线，要么是不可约三次曲线。本节处理前者，令其非退化方程为 $Q$。

$T_3$ 必为 $Q$ 乘一个线性式。因为 (1.3) 的 $t^3$ 系数为一，两个因子的相应首系数均非零。准确归一化为
$$
T_3=(t-A(x))
\bigl(t^2+A(x)t+A(x)^2-6H(x,x)\bigr).
\tag{3.1}
$$
其中 $A$ 是 $U$ 中的向量，亦以 $A(x)$ 表示它的线性式。特别，
$$
Q=t^2+At+A^2-6H,\qquad
4V=-A^3+6AH.
\tag{3.2}
$$

先证明 $H$ 的 $2\times2$ 块可逆。

若 $H=0$，则 (3.2) 给 $T_3=t^3-A^3$，只用到至多两个本质变量，矛盾。若 $H$ 秩一，(1.4) 给出以下全部可能。

在两个不同点型中，交换两点后可写 $H=h_1x_1^2$，$h_1\ne0$。若 $A=a_1x_1+a_2x_2$，本质三维要求 $a_2\ne0$。$V$ 中两个混合单项式的系数必须为零，故 (3.2) 给
$$
a_2(a_1^2-2h_1)=0,\qquad a_1a_2^2=0.
$$
第二式迫 $a_1=0$，第一式随即迫 $h_1=0$，矛盾。

在双 jet 型中，秩一必有 $H=h_0x_1^2$。由于 $V$ 不含 $x_2^3$，(3.2) 的该系数迫 $A$ 的 $x_2$ 分量为零。这又使 $T_3$ 只依赖 $t,x_1$，矛盾。因此
$$
\boxed{\operatorname{rank}H=2.}
\tag{3.3}
$$

进一步令
$$
d=A^{\mathsf T}H^{-1}A.
$$
物理形式 (1.4) 将该值限制为
$$
\boxed{d\in\{0,4\}.}
\tag{3.4}
$$
证明如下。不同点型中 $h_1h_2\ne0$，混合系数要求
$$
a_2(a_1^2-2h_1)=0,\qquad a_1(a_2^2-2h_2)=0.
$$
恰有一个 $a_i$ 非零会与另一个 $h_j\ne0$ 冲突；全部为零时 $d=0$；全部非零时 $a_i^2=2h_i$，所以 $d=4$。双 jet 型中 $h_1\ne0$，$x_2^3$ 系数仍迫 $A=(a_1,0)$，而 $H^{-1}$ 的左上角为零，故 $d=0$。

## 4. 完整低梯度迫二次曲线型全等向

不可约二次曲线的二次关系空间是一维，故 (2.3) 给 $N=\mu Q$。由 $N_{00}=F,Q_{00}=1$，有
$$
N=FQ.
\tag{4.1}
$$
比较跨块，得到
$$
Hl=-\frac F4A.
\tag{4.2}
$$
令 $s=A^{\mathsf T}l$。将 (3.2) 收缩一次，准确式为
$$
4V_l=-sAA^{\mathsf T}+2sH+
2\bigl(A(Hl)^{\mathsf T}+(Hl)A^{\mathsf T}\bigr).
\tag{4.3}
$$
使用 (4.2)，再比较 (4.1) 的 $U$ 块，得到
$$
4HGH=(s+2F)(AA^{\mathsf T}-2H),\qquad
s=-Fd/4.
\tag{4.4}
$$
左乘 $H^{-1}$ 并取迹，用 (2.2) 得
$$
0=\frac14(s+2F)(d-4)
=\frac F{16}(8-d)(d-4).
\tag{4.5}
$$
当 $d=0$ 时，此式立刻给 $F=0$。

若 $d=4$，则
$$
b=F^2/4,\qquad
GH=\frac F4(H^{-1}AA^{\mathsf T}-2I_2).
$$
秩一矩阵 $R=H^{-1}AA^{\mathsf T}$ 满足
$\operatorname{tr}R=4,R^2=4R$，因此
$$
\tau_2=\frac{F^2}{16}\operatorname{tr}(R-2I_2)^2=F^2/2.
$$
完整一次条件 (2.6) 于是变成
$$
0=F^2-\frac12F^2+F^2=\frac32F^2,
$$
仍给 $F=0$。由 $H$ 可逆及 (4.2)、(4.4)，继而 $l=0,G=0$。所以
$$
\boxed{K|_W=0\quad\text{在全部二次曲线投影情形成立。}}
\tag{4.6}
$$

该三维全等向空间是极大全等向的，故 $W^{\perp_K}=W$。由于 $W$ 包含准确长度二的物理 jet 空间 $U$，三个物理投影式的共同因子至少含 $D$。这是包括重数的断言：若 $u_0,u_1\in W$，则所有投影式及其在该点的一阶导数均为零。

最高矩投影表对二次曲线只允许共同因子次数 $\delta=1$ 或 $3$；因此这里只能 $\delta=3$。共同除子的三个物理 jets 均在 $W^{\perp_K}=W$ 中，且线性无关，所以 $W$ 本身就是长度三 jet 空间。[全等向长度三分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)终于给
$$
\boxed{\text{二次曲线投影}\ \Longrightarrow\ W=W_+\ \text{或}\ W=W_-.}
\tag{4.7}
$$

## 5. 不可约三次曲线投影也迫全等向

现在物理像为不可约三次曲线，其上不存在非零二次关系。由 (2.3)，
$$
N=0.
$$
块等式 (2.4) 因而给
$$
F=0,\qquad Hl=0,\qquad V_l+HGH=0.
\tag{5.1}
$$

若 $H$ 秩二，立即有 $l=0$；继而 $V_l=0,HGH=0$，故 $G=0$。

只须处理 $\operatorname{rank}H\le1$。若 $H$ 秩一，(1.4) 说明它是 $h\,u u^{\mathsf T}$，其中 $u$ 是 $D$ 中的一个物理曲线点。所有物理点满足 $u^{\mathsf T}Ku=0$，故 $HGH=0$；$H=0$ 时也如此。(5.1) 遂给 $Hl=0,V_l=0$。这两个等式分别说 $l$ 湮灭 $H,V$ 的本质支撑；因其支撑之和等于 $U$，得到
$$
l=0.
\tag{5.2}
$$

以下使用最高条件 $T_3(Kv(z))\equiv0$ 迫 $G=0$。

若 $D=s_1+s_2$ 为两个不同点，秩至多一的 $H$ 至多占一个点。不妨它只占 $s_1$，或 $H=0$。因为最小并支撑确为 $D$，$V$ 在另一点的系数 $v_2$ 非零；在 $H=0$ 时，$V$ 的两个系数均非零。令 $u_i=v_{\mathrm{hom}}(s_i)$，$k_{12}=u_1^{\mathsf T}Ku_2$。在 $z=s_1$，由 (5.2) 得 $y^{\mathsf T}Ku_1=0$，而 $u_1^{\mathsf T}Ku_1=0$。最高条件准确剩下
$$
0=4v_2 k_{12}^3.
$$
故 $k_{12}=0$，即 $G=0$。

若 $D=2s$，写 $u_0=v(s),u_1=v'(s)$。秩至多一的 $H$ 只有 $h_0u_0^2$；要使并支撑准确长二，必有
$$
V=v_0u_0^3+3v_1u_0^2u_1,\qquad v_1\ne0.
$$
记 $p_j(z)=u_j^{\mathsf T}Kv(z)$、$p_y(z)=y^{\mathsf T}Kv(z)$。由 $l=0$，$p_y$ 在 $s$ 至少二重。若 $g=u_1^{\mathsf T}Ku_1\ne0$，已付精确接触表给
$$
\operatorname{ord}_s p_0=2,\qquad \operatorname{ord}_s p_1=1.
$$
于是最高恒等式
$$
p_y^3-6h_0p_y p_0^2+4v_0p_0^3+12v_1p_0^2p_1\equiv0
\tag{5.3}
$$
的最后一项准确五阶，其余各项至少六阶，且五阶系数非零，矛盾。因此 $g=0$。又 $u_0Ku_0=u_0Ku_1=0$，所以 $G=0$。

这证明三次曲线型同样满足
$$
\boxed{K|_W=0.}
\tag{5.4}
$$
这里 $H,V$ 的所有降秩可能均已覆盖。

## 6. 完整结论与准确剩余类

结合初始 $W_\pm$ 分支及 §§3–5，得到
$$
\boxed{\text{(1.1) 的每个原完整临界点均满足 }W=W^{\perp_K}.}
\tag{6.1}
$$
更准确地，只有以下两种支撑类型：

1. $W=W_+$ 或 $W=W_-$，物理像为二次曲线；
2. $W$ 为三维极大全等向空间，物理曲线与 $W$ 的交除子准确长二，$H,V$ 的最小并支撑就是该除子 $D$，$y\notin U_D$，物理投影是双有理不可约平面三次曲线，且 $T_3$ 是该三次方程的非零倍数。

第二项的“准确长二”来自最高矩投影表：不可约三次曲线型只能有 $(\delta,e,d)=(2,3,1)$。由于 $W=W^{\perp_K}$，投影共同零除子就是物理曲线落入 $W$ 的交除子，故它恰为已经包含的 $D$。

第二项尚未排除。在全等向 $W$ 上，一次、二次低梯度事实上会自动消失；真正需要继续支付的是原物理 Hankel 形式 (1.4) 与不可约三次曲线方程能否同时满足。本稿没有据此声称原三个匹配 Bell 方向在该剩余类取零，也没有给出全局 Jacobian 幂证书或实际算子的分母逆。

