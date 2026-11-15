# R209：完整 canonical pure 成本的二阶 profile jet 表示

日期：2026-11-15。**完整纸面证明；没有新研究编译、profile 评价、正规化或消元。** 本稿从 R56 的真实分子恢复证明动态高 jet 的内部消项。它不是把局部第三势 N 当作 W，也不把静态段恒等式推广到变系数路径。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md)、[R208](R208-every-universal-pure-response-has-a-second-jet-representative.md)。

## 1. 结论与范围

沿 R105 记 U 为同 scalar 常值 germ、frame 恒等、$M=T=0$ 的真实 canonical 第四成本的实线性跨度，$\pi V=V_{-4}$ 为完整相位的 pure 分量。保持同一右锚、同一 canonical 目标和零传入历史。

**定理。** 对任一同 scalar 常值端口、frame 恒等的真实有限零矩路径 B，不必先要求 $T_B=0$，完整 $\pi V_B$ 都有只使用

$$
x,\quad q,\quad q',\quad q'',\quad
\text{有限乘积及同右锚有限嵌套原函数}
\tag{1}
$$

的准确 universal 表示。因此

$$
\boxed{\pi U\subset\mathscr A_2.}                         \tag{2}
$$

$\mathscr A_2$ 的定义见下节。结论保全部动态 forcing、累计二三阶历史与真实左尾。它没有证明 $\pi U=\pi R$，没有给函数维数、正性、实际负成本或完整第四 ruling。

更具体地，设 $m,n,v$ 和 N 为 R109 的真实局部生成元及第三势。存在明确的对角三次局部势 $N_*$，使

$$
N_\Delta-N_*\in\mathscr B,
\tag{3}
$$

且

$$
\boxed{
\pi v-\pi\mathcal B_m(N_*)
\equiv D_s\left(\frac{a^3q'''}6\right)
\pmod{\mathscr A_2}.
}                                                            \tag{4}
$$

这里 a 是第 3 节给出的显式二阶分子系数，常值 scalar germ 上 a 为零。式 (4) 保留端势，正是 (2) 的动态消项来源。

## 2. 同右锚代数及一个一般响应余项

固定纯输入 q，令

$$
p=q',\qquad r=q'',\qquad t=q''',\qquad
I(F)(x)=\int_{r_*}^{x}F(y)\,dy,\qquad J=-I.
$$

输入及所有原函数在同一个右 collar 为零。$\mathscr A_2$ 由 $x,q,p,r$ 经有限加、乘、I 生成，原函数 integrand 具有正 profile 次数。沿 R208 令

$$
\mathscr B=\mathbb R[x,q,p,\{I(F):F\in\mathscr A_2\}].       \tag{5}
$$

即 B 的外局部因子不需要 r；其原函数内部仍允许 r 与嵌套尾。R208 已证明

$$
W_\Delta\subset\mathscr B,\qquad \pi R\subset\mathscr A_2. \tag{6}
$$

以下“外 r 导数”只作用于所写表达式的外局部多项式，把原函数节点暂作系数。每次使用都先给出这样的原式代表，**不假设此符号操作天然下降到任意函数商**。

R208 的同锚引理为

$$
I(tF)\in\mathscr A_2\qquad(F\in\mathscr A_2).               \tag{7}
$$

证明是取 $G_r^{\rm out}=F$、r 原函数常数为零，则
$I(tF)=G-I(D_0G)$，其中 $DG=tG_r^{\rm out}+D_0G$。右 collar 使 G 的端值为零。式 (7) 不消去一般的 $I(t^2F)$。

对 $E\in E_8$，写其 R73 尾项为

$$
\Phi_E(f,g)=\text{局部项}
 +\sum_{j=0}^2 B_{E,j}(x)J(y^j f''g'')
 +2B_{E,2}(x)J(f'g').                                    \tag{8}
$$

若对角三次函数 $\tau\in\mathscr A_2$，有准确余项公式

$$
\boxed{
\pi\mathcal B_E(\tau)
\equiv\frac14\sum_{j=0}^2B_{E,j}(x)
 J\bigl(y^jt^2\tau_r^{\rm out}\bigr)
\pmod{\mathscr A_2}.
}                                                            \tag{9}
$$

这里 $\pi\mathcal B_E(\tau)=[D\tau(q)[\Phi_E(q,q)]-2\Phi_E(q,\tau(q))]/8$，只取对角即可决定 pure 响应。

证明 (9)：令 $X_E=\Phi_E(q,q)$，R208 给

$$
X_E'=S_Er-C_Er^2+\mathscr B,\qquad
X_E''=(S_E-2C_Er)t+\mathscr A_2.
$$

Fréchet 导数的原函数内部线性 t 由 (7) 降阶，故其唯一外高 jet 是
$(S_E-2C_Er)t\tau_r^{\rm out}$。另一方面，对尾项先准确用

$$
J(y^jr\tau'')=-x^jr\tau'
-J\bigl((jy^{j-1}r+y^jt)\tau'\bigr).
$$

其中 $\tau'=t\tau_r^{\rm out}+\mathscr A_2$。线性 t 积分可由 (7) 消去，留下

$$
2\Phi_E(q,\tau)
\equiv (S_E-2C_Er)t\tau_r^{\rm out}
-2\sum_jB_{E,j}J(y^jt^2\tau_r^{\rm out}).
$$

两项外局部 t 相消，得到 (9)。这是对一般局部势的公式，没有使用 $\tau\in W$。

## 3. 真实分子与第二阶的外 r 系数

几何记号为

$$
z=x+\omega,\quad e=hz-k,\quad Q=1+e^2,\quad
\gamma=h_s,\quad \omega_s=\frac{k_s}{2h},
$$

$$
\lambda=\frac{\gamma z-h\omega_s}{h^2},\qquad
e_s=h^2\lambda,\qquad
K_0=kz^2-\frac{k^2+1}{h}z.
$$

本节所有 s 导数均固定 x。令

$$
\mathbf v=(1,0,e),\quad \mathbf n=(0,1,0),\quad
\mathbf e_3=(0,0,1),\qquad
\mathbf y=hq\mathbf e_3-\frac p2\mathbf v.
$$

$\mathbf y$ 是初阶场的分子。真实协变导数为

$$
\mathbf b=\nabla_s\mathbf y
 =\left(0,h\left(q-\frac z2p\right),
 \gamma q-\frac{e_s}{2}p\right),\qquad
\dot{\mathbf v}:=\nabla_s\mathbf v=(0,hz,e_s).              \tag{10}
$$

另记两个标量收缩

$$
j=\mathbf y\cdot\mathbf v=heq-\frac Q2p,\qquad
F=\mathbf y_x\cdot\mathbf v=\frac{hep-Qr}{2}.               \tag{11}
$$

为避免与二次算子记号混淆，二阶累计 scalar 暂记为 A；其真实导数是

$$
A_s=X_m:=m(q,q),\qquad m\in E_8.
$$

A 和 $X_m$ 都在 $\mathscr B$。R56 二阶分子为

$$
\mathbf V_2=\alpha\mathbf v+\beta\mathbf n-hA\mathbf e_3,
\qquad \alpha=\frac{A_x}{2}+\frac{\eta_2}{h},\quad
\beta=zP_2+B_2.                                           \tag{12}
$$

这里 $P_2,B_2,\beta\in\mathscr B$。从 R56 的完整 $\eta_2$ 直接取外 r 部分，得到

$$
\boxed{
a:=\partial_r^{\rm out}\left(\frac{\eta_2}{h}\right)
=\frac{Q}{8h}\left(\frac{\gamma}{h^2}p-\lambda r\right).
}                                                            \tag{13}
$$

具体地，所需三项为

$$
(P_2)_x=-\frac Q{8h}r^2+\frac e4pr-\frac h8p^2,
$$

$$
(B_2)_x=-\frac e4p^2+\frac Q{4h}pr+\frac h2qp-\frac e2qr,
$$

$$
T_{s x,2}=\frac{\gamma h}{2}qp-\frac{he_s}{4}p^2
-\frac{\gamma e}{2}qr+\frac{ee_s}{4}pr.
$$

代入
$\eta_2/h=-T_{s x,2}/(2h^2)+\lambda(P_2)_x/2
+\gamma(B_2)_x/(2h^2)-(P_2)_s/(2h)$，qr 与相应 pr 项准确抵消；余下外 r 多项式是
$Q\gamma pr/(8h^3)-Q\lambda r^2/(16h)$，其导数正是 (13)。

定义

$$
u_A=\frac12\partial_r^{\rm out}(A_x),\qquad
u_m=\frac12\partial_r^{\rm out}((X_m)_x),\qquad
U=a+u_A=\partial_r^{\rm out}\alpha.
\tag{14}
$$

因此在二阶累计值 A 为零处，真实关系是

$$
U=a,\qquad U_s=a_s+u_m.                                  \tag{15}
$$

第二式不能由第一式直接微分得到；它保留 $A_s=X_m$。

## 4. 两条逐点收缩恒等式

R73 的点态 m 与 (10)–(13) 给

$$
\boxed{
-\frac{\mathbf b\cdot\mathbf v}{h^2}
-\frac{\lambda F}{h}+\frac{\gamma j}{h^3}=-4a,
}                                                            \tag{16}
$$

$$
\boxed{
-\frac{\mathbf b\cdot\dot{\mathbf v}}{h^2}
+\frac{K_0F}{h}-\lambda\left(\frac Fh\right)_s
-\frac{K_0j}{hz}
+\frac\gamma{h^2}\left(\frac jh\right)_s=4u_m.
}                                                            \tag{17}
$$

它们都是 q、p、r 的线性式，可以直接逐系数核验。为使 (17) 的来源完全明确，写

$$
X_m=A_0q^2+A_1qp+A_2p^2+\text{尾项},\qquad
C_m=B_{m,0}+xB_{m,1}+x^2B_{m,2}.
$$

则 $4u_m=2A_1q+4A_2p-4C_mr$，R73 给

$$
A_1=-\frac{kQ}{2h},\qquad
C_m=\frac{K_0Q}{8h}-\lambda\left(\frac Q{8h}\right)_s,
$$

$$
A_2=\frac{z^2}{8}+\frac{eK_0}{8}
+\frac{K_0Q}{8hz}-\frac{\gamma ee_s}{4h^3}
+\frac{\gamma^2Q}{8h^4}.                                  \tag{18}
$$

(17) 左端 q 系数是 $-z-K_0e/z=-kQ/h$；p 系数是 (18) 的四倍；r 系数是 $-K_0Q/(2h)+\lambda(Q/(2h))_s=-4C_m$。式 (16) 则直接用 $e_s=h^2\lambda$。这些身份包含真实变系数项，没有作常态限制。

## 5. 完整第三局部势必须保留的外 r 多项式

令第三 forcing 为 $H(Y_q,Z_2)$，其 scalar 累计值为 T。先对真实场求导，才取累计 A、T 的值为零；其第三局部 scalar RHS 是 $n_\Delta$。

第二分子满足
$\mathbf V_{2,x}=Ut\mathbf v+\mathscr A_2^3$。R56 的第三 normal 原函数，经一次同锚线性 t 分部积分，有一个 $\mathscr A_2$ 代表，其外 r 导数为

$$
\partial_r^{\rm out}P_3=-\frac{FU}{2h},\qquad
\partial_r^{\rm out}B_3=\frac{jU}{2h}.                    \tag{19}
$$

其余部分属于 $\mathscr B$。第一式来自
$P_3=-I(\mathbf y_x\cdot\mathbf V_{2,x})/(2h)$；所有不含 t 的 integrand 留在原函数内。第二式由 $B_3=\mathbf y\cdot\mathbf V_2/(2h)$ 直接得到。

此外

$$
\partial_r^{\rm out}T_{s,3}
=(\mathbf b\cdot\mathbf v)U_s
 +(\mathbf b\cdot\dot{\mathbf v})U.
$$

将这些式子代入完整 R56 scalar RHS，并用 (16)、(17)，得到

$$
\partial_r^{\rm out}(T_s)=2aU_s-2u_mU.
$$

在零二阶累计值处用 (15)，于是

$$
\boxed{\partial_r^{\rm out}n_\Delta=2aa_s.}               \tag{20}
$$

这也明确给 $n_\Delta\in\mathscr A_2$。定义外 r 多项式原函数

$$
\boxed{
N_*:=\int_0^r a(\rho)^2\,d\rho
=\frac{Q^2}{64h^2}
\left(\frac{\gamma^2p^2}{h^4}r
-\frac{\gamma\lambda p}{h^2}r^2
+\frac{\lambda^2}{3}r^3\right).
}                                                            \tag{21}
$$

式 (20) 意味着准确的原式代表满足

$$
n_\Delta-D_sN_*\in\mathscr B.                             \tag{22}
$$

另一方面 R109 给 $n_\Delta-D_sN_\Delta\in W_\Delta$，而 R208 给 $W_\Delta\subset\mathscr B$。因此

$$
D_s(N_\Delta-N_*)\in\mathscr B.                            \tag{23}
$$

原势采用 R190 明确保留的参考规范
$N^{[0]}(1,1,1)=0$，速度势在常 germ 为零；此处 $N_*=0$ 也成立。从这个参考 germ 沿一条真实光滑水平路径到给定路径的起始 germ，再沿给定路径积分 (23)，得到 (3)。

这里的积分只改变有限组 profile 表达式的几何系数，故仍是 $\mathscr B$ 的有限和。所需参考连接存在于 $h>0$ 的状态域。沿该辅助连接使用的是 R105 第 4 节、R109 第 7 节已经消去移动 x 分母的 **universal 多项式—Volterra 延拓**；本稿所有 $K_0/z$ 也只是 $kz-(k^2+1)/h$ 的多项式。因此不要求参考连接对原先固定的 I 物理合法，不把它插入原几何，也不为此移动原输入 q 或右锚。积分所得是同一 universal 代数中的身份，随后直接作用于原固定 I 上的原 q。没有在当前路径起点把 N 擅自重新置零，也没有把 $N_*$ 冒充 W 元素。

## 6. 第三分子的唯一外三阶 jet

第三分子写成

$$
\mathbf V_3=Ct\mathbf v+\mathbf V_{3,0},\qquad
\mathbf V_{3,0}\in\mathscr A_2^3.
\tag{24}
$$

R56 的 $T_{s x,3}$ 是对称交叉分量，t 系数为
$U(\mathbf b\cdot\mathbf v)/2$。结合 (19) 与完整 $\eta_3$，式 (16) 给

$$
\boxed{C=\frac12\partial_r^{\rm out}T-aU.}                \tag{25}
$$

T 本身在 $\mathscr A_2$：其真实导数为
$n_\Delta-m(q,A(q,q))$；前者已由第 5 节处理，后者由 R208 有序复合公式属于 $\mathscr A_2$。因此 (24) 包含全部第三分子，而非只截取一个 leading jet。

现在才在真实导数之后置 A、T 为零。由 (15)、(20)、(25)，

$$
U=a,\qquad C=-a^2,
$$

$$
U_s=a_s+u_m,\qquad
C_s=\frac12(n_\Delta)_r-2aa_s-au_m
=-aa_s-au_m.                                               \tag{26}
$$

于是出现一个关键的真实消项：

$$
\boxed{
U^2+2C=-a^2,\qquad
D_s(U^2+2C)\big|_{A=T=0}=0.
}                                                            \tag{27}
$$

右端零是先微分后取零历史所得。若先把第一式当作沿整个路径的身份再微分，就会得到错误的 $-2aa_s$，并漏掉本稿的动态相消。

## 7. 第四 forcing 的全部高 jet

原 pure 通道准确使用

$$
H_{4,-4}=-\frac1{16}H(Z_2,Z_2)
-\frac14H(Y_q,Z_3).
\tag{28}
$$

这是原完整 producer 使用的两项和；不是只取 $H_{ss}$ 或 normal 平方的一部分。由 (12)、(24)，同锚分部积分后，完整第四 normal 数据模 $\mathscr A_2$ 为

$$
\boxed{
P_4\equiv\frac{FC}{8h}t
+\frac1{32h}I\bigl(Q(U^2+2C)t^2\bigr),
\qquad
B_4\equiv-\frac{jC}{8h}t.
}                                                            \tag{29}
$$

同时

$$
T_{s,4}\equiv-\frac t4
\bigl((\mathbf b\cdot\mathbf v)C_s
+(\mathbf b\cdot\dot{\mathbf v})C\bigr).
\tag{30}
$$

为核清 (29) 中最容易漏的项，对交叉 normal 原函数只需写

$$
I\bigl(FCt'+FC_r t^2\bigr)
\equiv FCt-I(F_rCt^2)
=FCt+\frac12I(QCt^2).
$$

这里 $F_r=-Q/2$；其余线性 t 的积分由 (7) 处理。第二分子平方贡献 $I(QU^2t^2)$，与 (28) 的 $-1/16,-1/4$ 合并正好给 (29)。这一步不丢任何 $q''''$，而是把它的全部贡献准确收进了 t 与 $t^2$ 两项。

将 (29)、(30) 代入 R56 的完整 scalar RHS，用 (16)、(17)。其外局部 t 部分成为

$$
\frac t2(u_mC-aC_s).
\tag{31}
$$

其原函数高 jet 部分为

$$
\frac{K_0}{32h}I\bigl(Q(U^2+2C)t^2\bigr)
-\frac\lambda{32}D_s\left[
\frac1hI\bigl(Q(U^2+2C)t^2\bigr)\right].
\tag{32}
$$

再用真实 (26)、(27)，局部生成元 v 的 (31) 是

$$
\frac12a^2a_s t=D_s\left(\frac{a^3t}{6}\right),            \tag{33}
$$

而 (32) 变为

$$
-\frac{K_0}{32h}I(Qa^2t^2)
+\frac\lambda{32h}I\left[
\left(Q_s-\frac\gamma hQ\right)a^2t^2\right].             \tag{34}
$$

这些 s 导数固定 x，不作用于输入 q。式 (34) 尤其没有多出 $D_s(a^2)$：它已由 (27) 的真实历史导数抵消。

## 8. N 修正恰好支付原函数高 jet

R73 的点态 m 尾核，保留积分内 y 与查询 x 的区别，可写成

$$
\sum_{j=0}^2B_{m,j}(x)y^j
=\frac{K_0(x)}{8h}Q(y)
-\lambda(x)D_s\left(\frac{Q(y)}{8h}\right).
\tag{35}
$$

对 $N_*$ 用 (9) 和 $(N_*)_r=a^2$，得到

$$
\pi\mathcal B_m(N_*)\equiv
-\frac{K_0}{32h}I(Qa^2t^2)
+\frac\lambda{32h}I\left[
\left(Q_s-\frac\gamma hQ\right)a^2t^2\right]
\pmod{\mathscr A_2}.
$$

它与 (34) **逐点一致**，于是 (33) 给主身份 (4)。又因 (3)，R208 的同锚 Fréchet 引理对任意 B 表示适用，故

$$
\pi\mathcal B_m(N_\Delta-N_*)\in\mathscr A_2.
$$

因此完整实际势同样满足

$$
\boxed{
\pi\{v-\mathcal B_mN\}
\equiv D_s\left(\frac{a^3q'''}6\right)
\pmod{\mathscr A_2}.
}                                                            \tag{36}
$$

这是保留 $N^{[2]}$ 后的消项，不能用“第三势全属 W”代替。只保静态势会漏掉 (21)，进而留下错误的三阶 jet 余项。

## 9. 真实整路径与完整成本 span

对真实零总矩阵路径，R109 的准确公式为

$$
V_B=\int_B(v-\mathcal B_mN)\,ds
-\int_B\mathcal B_mH\,ds
-\frac16\int_B\mathcal B_A(\tau_{A,m})\,ds,
$$

其中 $H,\tau_{A,m}\in W$，因此后两项的 pure 均由 R208 属于 $\mathscr A_2$。首项使用 (36)；常值 scalar germs 使 $\gamma=k_s=\lambda=a=0$，所以

$$
\left[\frac{a^3q'''}6\right]_0^L=0.
$$

剩下有限个 $\mathscr A_2$ profile 表达式的真实几何系数积分，仍属于 $\mathscr A_2$。这证明 $\pi V_B\in\mathscr A_2$。R105 允许由这些 M=0、未必 T=0 的真实成本张成 U，故得到 (2)。

因此，在 R178/R179 的 single-color 规范余词中，**完整 canonical $\pi U$ 也没有真正的三阶或更高 jet 行**。某个正确处理的局部未完成表达式可以有这类项；它们必须在 (36) 的势修正、真实 s 导数和端点处理中按上述方式消去，不能在原恢复之前删去。

本结论不将 pure 与 mixed 混同，不覆盖另加独立二三阶 profile gauge，也不把二阶 jet 表示当作完整响应成员身份。剩余纯成本商与真实闭锥、实际 finite 支付、第四 ruling 仍须各自证明。
