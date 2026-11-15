# R834 — 原四块目标的三个长 Euler 窗与完整分歧理想的单位像

日期：2026-11-15。**状态：下列同来源三长窗单射、原物理单位输运及整单位秩下界已证明。主目标仍未完成。**

本篇在 R821 已定义的完整原四块目标上，使用三个真实满块，而不是把旧三块目标的最后短块补长。核心结论是：在下述准确窗口内，原整个
$F\mathcal H_2+(\mathcal EF)\mathcal H_2\subset\mathcal H_3$
没有三长窗首核。它包括 R550 的全部分歧理想，也包括原两长窗中由 $\ker\alpha_\eta$ 产生的镜轴核；第三条实际长 Euler 行把这个子格的镜轴核全部排掉。

结论只针对已经整返回同一 $\mathcal W_D$ 的来源。原 $P_{134}/U_0$、总 charge 平移四十和三个十三行跨界带均保留。它不证明全 $\mathcal W_D$ 单射，不把四条完整中央零变成一个深核，也不把四次幂候选或它的完整修正免费加入来源。

## 1. 原曲面、截面及准确长度

沿用 R495、R550、R833 的原十九角曲面 $X$。令 $C=(F=0)$ 是原几何整曲线，$P=(0,1)$ 是其原光滑点，置
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\qquad
N=\mathcal O_C(C),\qquad
\kappa=C^2,\qquad\chi=-K_XC.
\tag{1}
$$
这里 $\mathcal E=Y\partial_Y$ 是原相对 Euler 算子。十九角的逐框公式已经证明
$\mathcal E\mathcal H_j\subset\mathcal H_j$；
本篇不以总算子 $\mathcal E+40$ 代替这个几何算子。记
$$
e=\mathcal EF\in\mathcal H_1,\qquad e(P)\ne0.
\tag{2}
$$
所用剩余特征满足 $p>3$。实际四源范围采用 R821 的更强素数门。

由原光滑条件，$C$ 在 $P$ 附近有唯一支 $Y=\psi(t)$，
$\psi(0)=1$。原实际低轴记为 $Y=g(t)$，并令
$$
h=\operatorname{ord}_tF(t,g(t))>0.
$$
在本文读取的截断中写 $g=\psi e^\eta$，其中
$\operatorname{ord}\eta=h$。这只使用有限 Taylor 恒等式：
也可先令 $v=g/\psi-1$，在模 $t^{2h}$ 下取 $\eta=v$；
所需系数为 $1,1/2,1/6$，没有假定完整特征 $p$ 对数存在。

固定整数 $T$ 满足
$$
\boxed{h<T\le2h,\qquad T>2\kappa.}
\tag{3}
$$
于是 $h>\kappa$ 自动成立。特别，R550 的旧强窗
$h>\kappa,\ T-h>\kappa,\ T\le2h$ 蕴含 (3)，但本篇不需要单独的
$T-h>\kappa$。

定义原三长行映射
$$
\mathcal J_{3,T}:\mathcal H_3\longrightarrow
  \bigl(k[[t]]/t^T\bigr)^3,\qquad
G\longmapsto
 \bigl(G(t,g),(\mathcal EG)(t,g),(\mathcal E^2G)(t,g)\bigr).
\tag{4}
$$
固定单位 Gaussian $a_p$ 给各行乘 $1,a_p,a_p^2/2$ 不改变其核。

## 2. 三长窗与整个 $F\mathcal H_2$ 的交核为零

**定理 1。** 在 (1)–(3) 的原来源范围内，
$$
\boxed{\ker\mathcal J_{3,T}\cap F\mathcal H_2=0.}
\tag{5}
$$

**证明。** 取同一个 $H\in\mathcal H_2$，假设 $G=FH$ 的三行都为零。
在局部 Euler 法向坐标 $\zeta=\log(Y/\psi)$ 中写
$$
F=e_0\zeta+\frac{f_2}{2}\zeta^2+\frac{f_3}{6}\zeta^3+\cdots,
\qquad
H=h_0+h_1\zeta+\frac{h_2}{2}\zeta^2+\cdots.
\tag{6}
$$
这些是原 $F,H$ 在同一支上的 Taylor 系数；
$e_0=e|_C$ 在 $P$ 为单位，$h_0=H|_C$ 是 $N^2$ 的真实全局截面。
由于 $\eta^2=0\bmod t^T$，三条完整长行逐项给
$$
e_0\eta h_0=0\pmod{t^T},
\tag{7}
$$
$$
e_0h_0+\eta(2e_0h_1+f_2h_0)=0\pmod{t^T},
\tag{8}
$$
$$
2e_0h_1+f_2h_0+
 \eta(3e_0h_2+3f_2h_1+f_3h_0)=0\pmod{t^T}.
\tag{9}
$$
首先 (7) 给 $\operatorname{ord}h_0\ge T-h$，
所以 $\eta h_0=0\bmod t^T$。因此 (8) 化成
$$
h_0+2\eta h_1=0\pmod{t^T},
\tag{10}
$$
特别 $h_0\in t^h k[[t]]$。将 (9) 模 $t^h$ 读取，所有其它项消失，
而 $2e_0$ 为单位，故 $h_1\in t^h k[[t]]$。
再代回 (10)，因 $2h\ge T$，得到
$$
\operatorname{ord}_P h_0\ge T>2\kappa=\deg N^2.
\tag{11}
$$
整曲线上非零截面的零除子次数等于其线束次数，故 $h_0=0$。
同一真实截面序列遂给 $H=FL$，其中 $L\in\mathcal H_1$；
没有在来源外另选局部修正。

现在 $h_1=e_0L|_C$。上面的 $h_1\in t^h$ 以及 $h>\kappa=\deg N$
迫 $L|_C=0$。所以 $L=cF$，$c\in k$，并有 $G=cF^3$。
但原第三长行的完整首项是
$$
(\mathcal E^2(cF^3))(t,g)
 =6c\,e_0^3\eta\pmod{t^T}.
\tag{12}
$$
因为 $h<T$、$6e_0^3$ 为单位，(12) 只有 $c=0$ 才消失。
这证明 (5)。证毕。

这里最后一步是关键：旧两长窗容许的 $F^3$ 本身在第三条长行上非零。
本篇并未从旧两长窗推出这条新行。

## 3. 全部分歧理想的单射，不只是 $F\mathcal H_2$ 子块

令
$$
\mathcal I=F\mathcal H_2+e\mathcal H_2\subset\mathcal H_3,\qquad
Z=V(F,e).
\tag{13}
$$
R550 的同一完全交和整返回给
$$
\mathcal I=H^0(X,\mathscr I_Z(3C)),\qquad
\operatorname{length}Z=\kappa,\qquad P\notin Z,
$$
$$
\dim\mathcal I=1+\frac{7\kappa+3\chi}{2}.
\tag{14}
$$
所有固定角、奇异交点及非约化结构仍在 $Z$ 内。

**定理 2。**
$$
\boxed{\ker\mathcal J_{3,T}\cap\mathcal I=0.}
\tag{15}
$$

**证明。** 取同一 $G=FH+eK$，$H,K\in\mathcal H_2$。
若其前两条长行消到 $T$，则有限反向 Taylor 展开给
$$
G|_C=G(t,g)-\eta(\mathcal EG)(t,g)=0\pmod{t^T};
\tag{16}
$$
余项含 $\eta^2$，由 $T\le2h$ 消失。
另一方面 $G|_C=e_0K|_C$，故 $K|_C$ 消到 $T>2\kappa$。
因此 $K=FK_1$，$K_1\in\mathcal H_1$，并有
$$
G=F(H+eK_1)\in F\mathcal H_2.
$$
括号是同一真实 $\mathcal H_2$ 截面。
第三长行再由定理 1 迫 $G=0$。证毕。

所以不是把两个各自单射的块相加后猜测仍单射；
(16) 先把它们的整个联合核压回同一个 $F\mathcal H_2$，
再用定理 1 排掉。

## 4. 原 $\Gamma^{(4)}$ 中的三个真实长块

令 $p=6s-1$，并用 R821 的原目标
$$
\Gamma_{L_4+13}^{(4)}
=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3),
\quad L_4=3s+\ell,\quad1\le\ell<s-13.
\tag{17}
$$
相对 $J_4$ 的前三块准确为
$$
\begin{pmatrix}
[P_0]_{<s}\\
[a_pP_1+p\mathscr SP_0]_{<s}\\
[\frac{a_p^2}{2}P_2+pa_p\mathscr SP_1+
 p^2\mathscr S^2P_0]_{<s}
\end{pmatrix}.
\tag{18}
$$
这里 $\mathscr S$ 是原 $s$ 阶系数移位。所有带移位的项在约化时均消失，
所以 (18) 模 $p$ 的三个满块确实是
$P_0,a_pP_1,a_p^2P_2/2$；没有把移位项在更高精度丢掉。

完整原物理映射保
$$
M^{\rm orig}=c_*U_0m_{13}J_4,\qquad m_{13}=w^{13}.
\tag{19}
$$
其三条跨界带仍是原下标
$$
s-13,\ldots,s-1;\quad
2s-13,\ldots,2s-1;\quad
3s-13,\ldots,3s-1,
\tag{20}
$$
每次跨界付一个 $p$。约化后，每个长块只能读除公共 $w^{13}$ 后的
严格前缀 $<s-13$。本篇不逆转 $m_{13}$，而只使用这些真正已经读到的行。

设原 R495 的整来源返回已经给出
$$
q_{\rm src}(t,Y)t^r\mathcal H_3\subset\overline{\mathcal W_D},
\qquad q_{\rm src}(0,1)\ne0,
\tag{21}
$$
其中 $q_{\rm src}$ 保完整 $d^{-C_D}Q$ 和真实角帽。
则三个物理长块对这个子格的共同可读长度准确为
$$
\boxed{T_M=s-r-13.}
\tag{22}
$$
相对 $J_4$ 的同一长度为 $T_J=s-r$。
二者相差十三；全文不把它们互换。

为显写普通单位和 charge 平移，令 $u_0(w)$ 是原 $G_0/w^{13}$
在去 Gaussian 后的完整普通单位，并将 $c_*$ 并入它。
令 $t(w)=w\tau(w)$，$\tau(0)\ne0$。
按 R821 的原逐列 charge 规范，前三个长块在去掉已读公共
$w^{13+r}$ 后为
$$
\left[
 u_0(w)\tau(w)^r\,\frac{a_p^i}{i!}
  (\mathcal E+40)^i(q_{\rm src}G)(t(w),g(w))
\right]_{<T_M},\qquad i=0,1,2.
\tag{23}
$$
若把公共 Gaussian $e^{40a_p\epsilon}$ 已收入完整 $U_0$，
先乘其实际整逆，再读 (23)，得到同一公式的等价行规范；
四十只处理一次。

用真正乘积法则，
$$
(\mathcal E+40)^i(q_{\rm src}G)
=\sum_{j=0}^i\binom ij
 ((\mathcal E+40)^{i-j}q_{\rm src})\,\mathcal E^jG.
\tag{24}
$$
因此 (23) 与 (4) 之间的矩阵是下三角，其 $(i,j)$ 项为
$$
u_0\tau^r\frac{a_p^i}{i!}\binom ij
 ((\mathcal E+40)^{i-j}q_{\rm src})(t,g),
\quad j\le i.
\tag{25}
$$
三个对角分别为
$u_0\tau^rq_{\rm src}$、
$a_pu_0\tau^rq_{\rm src}$、
$(a_p^2/2)u_0\tau^rq_{\rm src}$，
都在 $k[[w]]/(w^{T_M})$ 中为单位。
这给真正的有限下三角整逆，保 $q_{\rm src}$、$u_0$ 的全部低尾。
再用 $t/w=\tau$ 的单位坐标变换，正好得到 (4)。

R821 四高轴变形的全部额外项分别含 $p,p^2,p^3$，
末端四次项也含 $p^3$。所以本篇约化单位块对所有那里的实际高轴取值相同。
完整 $M\bmod p^4$ 仍保 R821 的末端
$p^3\epsilon^3w^{s-3}P_3^4J_4\mathcal E_{\rm tot}^4/24$；
它不是由 $\epsilon^4=0$ 删掉，只是不影响约化单射。

## 5. 原物理单位块及贴边的准确门

**定理 3。** 假定 (21) 是已付的真实整来源返回，且
$$
\boxed{
h<T_M=s-r-13\le2h,\qquad T_M>2\kappa.
}
\tag{26}
$$
则原整个四块矩阵 $\bar M^{\rm orig}$ 在
$$
q_{\rm src}t^r\bigl(F\mathcal H_2+e\mathcal H_2\bigr)
$$
上单射。因此其完整整矩阵至少有
$$
\boxed{1+\frac{7\kappa+3\chi}{2}}
\tag{27}
$$
个单位 Smith 因子。

证明由 (23)–(25)、定理 2 直接得到。
选取 (13) 的一个 $k$ 基，再取 (21) 已付原整来源中的任意提升，
约化评价列线性独立，故存在同阶原单位子式。
这里单位子式的存在来自真实目标 $p$ 上的单射；
没有使用辅助素数，也没有从来源端饱和猜物理像饱和。
其它原 $\mathcal W_D$ 列仍全部保留，加入它们不会减少已得单位秩。

在原常用贴边 $s=2h+r$，(22) 成为 $T_M=2h-13$，
所以 (26) 准确化为
$$
\boxed{h>13,\qquad 2h-13>2\kappa.}
\tag{28}
$$
按整数写即
$$
h\ge\max(14,\kappa+7).
\tag{29}
$$
原 R550 的较强物理门 $h-13>\kappa$ 自动满足它。
相对 $J_4$ 则 $T_J=2h$，只需 $h>\kappa$；
这个较小门不能搬成原 $M$ 的门。

(21) 是必要的来源假设：即使某个四次幂候选已在 $\mathcal W_D$，
仍不能在未付返回时自动把另一套完整 $\mathcal H_3$ 当成本篇子格。
本结论不增加中央等式，也不扩大原角预算。

## 6. 整个三长窗首核还剩什么

记 $K_{3,T}=\ker\mathcal J_{3,T}$。
同一 (16) 给所有 $G\in K_{3,T}$ 的 $G|_C$ 消到 $T$；
由定理 1，限制映射的核为零。因此有实际单射
$$
\boxed{
K_{3,T}\hookrightarrow H^0(C,N^3(-TP)).
}
\tag{30}
$$
再限制到原 $Z$ 仍单射，因为其核为
$H^0(C,N^2(-TP))=0$。所以
$$
K_{3,T}\hookrightarrow H^0(Z,\mathcal O_Z(3C)).
\tag{31}
$$
这里的像是同一个 $G$ 的限制像，不是任意 $Z$ 值；
还必须通过第三条长行和原第四短行。

原两长窗的 R550 精确式为
$K_0\cap\mathcal I=F K_{\rm mir}$。
本篇证明三个长窗与这整个空间的交为零，
故不再需要先解 $\alpha_\eta$ 才能判这个子格。
但旧三块矩阵只有两条长行和一条短行，
其短端点没有由 (26) 被加长；
本篇不消除旧镜轴问题，也不声明旧原 $d_2$ 障碍已非零。

在原四块全来源上，仍未付的是
(30)–(31) 中非零限制能否满足所有原列关系、第四短行及同一个修正的
$p^2,p^3,p^4$ lifting。新增的确定输入是完整原分歧理想的单位像，
不是全部剩余核的消失，也不是主目标完成。
