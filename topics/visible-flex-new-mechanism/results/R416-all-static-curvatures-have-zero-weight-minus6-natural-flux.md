# R416：任意静态曲率下权负六的完整自然通量恒零及正字符静态项消失

日期：2026-11-16。**完整纸面原式证明；只读已付来源，没有执行新的积分、符号程序、原根恢复、profile 评价、秩、人工检查或研究计算。**

本稿把 [R415](R415-two-anchor-negative-character-multiplier-and-complete-static-tail-cancellation.md) 的一个静态锚点恒等推广到所有实 $k$。仍使用同一原始静态系数
$$
F_0=v_0-\mathcal B_{m_0}N_0-\Gamma(m_0),
$$
全部原势、参考归一化和同锚有序尾均保留。结论为
$$
\boxed{
V_6(k):=[h^{-6}(\log h)^0]F_0(h,k,0)\in U,\qquad
\Lambda_u(V_6(k))=0
}
\tag{1}
$$
对每个 $k\in\mathbb R$ 和每个真实紧光滑 $u$ 成立。

因此，在 [R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md) 与 R415 所定义的共同有限自然查询商上，剩余权 $\sigma=-6$ 的任何正仿射字符必满足
$$
\boxed{a(k)\equiv0,\qquad a_1=0,\qquad\mu=0,\qquad
\lambda F_0(h,k,\omega)=0.}
\tag{2}
$$
这消去的是完整字符 action 的静态部分。三个速度二次系数尚未由本稿消去，权 $-4$ 的全 $k$ 静态项也未由本稿支付。

来源为 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)、[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)、R413 及 R415。

## 1. 同锚定义和所取的真实系数

固定原合法正窗口及共同右 collar，
$$
0<\ell<r_*,\qquad
JF(x)=\int_x^{r_*}F(y)\,dy,\qquad
u\in C_c^\infty((\ell,r_*);\mathbb R).
$$
取静态状态
$$
h>0,\qquad k\in\mathbb R,\qquad\omega=0.
$$
于是 $z=x>0$，不因改变 $k$ 穿过坐标极点。记
$$
s_0=1+k^2,\qquad e=hx-k,\qquad Q=1+e^2,
$$
$$
v=u',\quad r=u'',\quad t=u''',\quad
L=v-xr,\quad G=u-xv/2,\quad M=x^2r-2xv+2u,
$$
$$
P=J(r^2),\quad J_1=J(xr^2),\quad
C=J(x^2r^2+2v^2),\quad
R=v^2+xP,\quad T=x^2v^2+xC.
\tag{3}
$$
$s_0$ 在本稿仅是正标量 $1+k^2$，不是几何积分起点。$R,T$ 是原二次输出，不表示响应空间或第三算子。

自然读出使用 R402(3) 的完整定义
$$
\Lambda_u(V)=
\int tV(u^2,0)-\frac{16}{5}\int t\,\pi V(u)
-\frac{32}{15}\int t\,\mathscr G_{V,u}(\mu(u)),
\tag{4}
$$
其中
$$
\mu(u)=\left(\int r^2,\ \int xr^2,\
\int(x^2r^2+2v^2)\right).
$$
$\mathscr G$ 是正式 pure 对一个实际右包的有序 $2+2$ 三矩尾映射。先完成这个线性映射，最后才代入 $\mu(u)$；不要求一个右包本身与 $u$ 有相同的三个矩。

有限 Laurent/log 值跨度定理 R130 保证本稿的完整系数 $V_6(k)$ 属于原 $U$。单个系数属于 $U$ 不等于它有独立的正时间路径实现。

## 2. 原静态二阶场的最低幂

从 R73(2) 与原 normal 分子 $b=xP_{uu}+\mathcal B_{uu}$，直接得到
$$
\begin{aligned}
b={}&\frac{s_0}{8h}R
+k\left(\frac{uv}{2}-\frac{3xv^2}{8}-\frac{xJ_1}{4}\right)\\
&+h\left(\frac{G^2}{2}+\frac T8\right).
\end{aligned}
\tag{5}
$$
当前原静态二阶密度记为 $q=\Phi_{m_0}(u,u)$。R73 的八坐标在 $\omega=0$ 时为
$$
\begin{gathered}
p_0=-\frac{ks_0}{2h},\quad p_1=k^2,\quad
p_2=-kh/2,\quad r_0=s_0^{\mathrm{coord}}=0,\\
r_1=-\frac{s_0^2}{8h^2},\quad
s_1=\frac{ks_0}{4h},\quad t_1=-s_0/8.
\end{gathered}
\tag{6}
$$
式(6)中的 $s_0^{\mathrm{coord}}$ 是原八矩坐标，特加上标与正标量区分。因此
$$
b=\frac{s_0R}{8h}+O(h^0),\qquad
q=-\frac{s_0^2R}{8h^2}+O(h^{-1}).
\tag{7}
$$
本稿所有 $O(h^j)$ 仅标记有限 Laurent 表中不低于该幂的项，并非取极限、忽略余项或作数值估计。

真实历史当前值可以在提取局部密度后置零，但其导数 $q$ 必须保留。原第二场及其协变导数为
$$
V_Z=(0,b,0),\qquad
\nabla_sV_Z=
\left(q'/2-kb,\ 0,\ -b+e q'/2-hq\right).
\tag{8}
$$
故其 $h^{-2}$ 部分准确是
$$
-\frac{s_0^2R'}{16h^2}(1,0,-k).
\tag{9}
$$
这已经说明纯 $ZZ$ 收缩的最高所需项会乘 $s_0^5$，但还不足以证明(1)：第三链、原势和有序尾必须继续保留。

## 3. 全外槽 N0：潜在 h 负四势项对每个 k 都消失

原 $N_0=P_h+F_*(k,\omega)$ 中，$P_h$ 是第三权一次密度沿水平 $h$ 方向的原函数。$F_*$ 及参考积分常数均不依赖 $h$。本节保独立 outer $f$、inner $g^2$，不从对角式反猜极化。

沿 $h_s=1,k_s=0,\omega=0$，取原权一次部分。局部第二场第一分子 $a_g=\eta_{Z,g}/h$ 的最低项为
$$
a_g=\frac{s_0R_g'}{16h^3}+O(h^{-2}).
\tag{10}
$$
它由 R56(6) 的全部四项得到；尤其 $P_s$ 保留。原 $b_g,q_g$ 仍用(5)–(7)。

记 $G_f=f-xf'/2$。原 R73 的 $\ell-\Psi$ 给完整权一次密度
$$
\begin{aligned}
n_\gamma(f;g^2)
={}&G_f\left\{\frac{\partial_h b_g}{2h}
-\frac{b_g}{2h^2}+\frac{xa_g}{2}\right\}\\
&+K_0\left(P_a+\frac{B_a}{x}\right)
-\Psi_\gamma(f,q_g),
\qquad K_0=kx^2-\frac{s_0x}{h},
\end{aligned}
\tag{11}
$$
其中
$$
P_a=\frac{(Qf''-he f')a_g+J(Qf'''a_g)}{4h},\qquad
B_a=\frac{(he f-Qf'/2)a_g}{2h},
\tag{12}
$$
$$
\Psi_\gamma(f,q_g)=
-\frac{k f'q_g}{4h^2}
-\frac{Qf'q_g'}{8h^3}
-\frac{xJ_e(f,q_g)}{8h^3},
$$
$$
J_e(f,w)=J(Qf''w''+2h^2f'w').
\tag{13}
$$
这里 $a_g$ 指权一次系数；高于该权的 $a_{g,s}$ 项不进入 $n_\gamma$，而不是在整个第三恢复中被删除。

由(10)–(13)，唯一可能的 $h^{-5}$ 项来自第二行和 $\Psi$。使用同一右零身份
$$
J((f''R_g')')=-f''R_g',
$$
它们分别为
$$
\begin{aligned}
[h^{-5}]K_0(P_a+B_a/x)
&=\frac{s_0^3}{64}
\{f'R_g'+xJ(f''R_g'')\},\\
[h^{-5}]\Psi_\gamma(f,q_g)
&=\frac{s_0^3}{64}
\{f'R_g'+xJ(f''R_g'')\}.
\end{aligned}
\tag{14}
$$
所以
$$
[h^{-5}]n_\gamma=0.
\tag{15}
$$
没有用左 collar 为零；此处需要的右零由原输入与原恢复保证。完整原式没有比 $h^{-5}$ 更低的幂。因此取真实 $h$ 原函数后，
$$
[N_0]_{h^{-4}}=0,\qquad N_0\text{ 的最低可能幂不低于 }h^{-3}.
\tag{16}
$$
可能的 $\log h$ 与 $h$ 无关常数不会改变(16)。

$m_0$ 的最低幂是 $h^{-2}$，固定线性 $\Gamma(m_0)$ 也不低于 $h^{-2}$。故原势响应和原参考项都没有所取的 $h^{-6}$，准确得到
$$
\boxed{V_6(k)=[h^{-6}]v_0(h,k,0).}
\tag{17}
$$
这是按原完整势的最低幂证明后的结论，不是整体删掉 $N_0$ 或 $\Gamma$。

## 4. 第三局部恢复与 YC 最高项

求完真实导数再置当前历史值零，第三局部场分子为 $(c,0,ec)$。原 $P_{C,s},B_{C,s}$ 中的 $-P_H(Y,Y_q),-B_H(Y,Y_q)$ 均保留。R56 直接给
$$
c=-\frac{Gb'}{4h}+\frac{Lb}{8h}
+\frac{Qr q'}{16h^2}
+\frac{(hv-er)q}{8h}
+\frac{J_e(u,q)}{16h^2}.
\tag{18}
$$
最低项因此为
$$
\begin{aligned}
[h^{-4}]c
&=-\frac{s_0^3}{128}\{rR'+J(rR'')\}\\
&=\frac{s_0^3}{128}J(tR').
\end{aligned}
\tag{19}
$$
第二行只用 $J((rR')')=-rR'$ 的同锚右端恒等。

静态 R56 密度为
$$
\mathcal R_H(A,B)=\frac{T_{s,AB}}{2h^2}
+K_0P_{AB}+\frac{K_0}{x}B_{AB}.
\tag{20}
$$
在 $YC$ 配对中，$T_s$ 部分没有 $h^{-6}$：$\nabla_sV_Y=(0,hG,0)$，所配的第二分量是 $hx\,c-b(u,q)$，而 $b(u,q)$ 的最低幂不低于 $h^{-3}$。真正的三阶 history 导数仍在原分子里；它不产生此处第二分量的更低幂。

$K_0P+K_0B/x$ 在所需项上则准确为
$$
\frac{s_0^2}{4h^2}
\{v c+xJ(r c')\}.
\tag{21}
$$
用 $J(r c')=-rc-J(tc)$ 与紧 $L$，
$$
\int t\{v c+xJ(r c')\}=2\int Lt\,c.
\tag{22}
$$
(22)不要求 $c$ 左紧。由(19)得到
$$
Y_6(k):=[h^{-6}]\int t\,\mathcal R_H(Y,C)
=\frac{s_0^5}{256}\int Lt\,J(tR').
\tag{23}
$$

## 5. ZZ 和所有有序尾使用同一个第五次因子

由(9)(20)，仅 $T_s/(2h^2)$ 能贡献 $ZZ$ 的 $h^{-6}$，所以
$$
Z_6(k):=[h^{-6}]\int t\,\mathcal R_H(Z,Z)
=\frac{s_0^5}{512}\int t(R')^2.
\tag{24}
$$
其余原 $P/B$ 项最早是 $h^{-4}$。

记
$$
\mu_0=\int r^2,\qquad M_3=\int r^3.
$$
真正左尾为 $R'(\ell)=\mu_0$，且
$$
R''=2Lt,\qquad
\int tR'=M_3/3,\qquad
\int Lrt=-M_3/6.
\tag{25}
$$
因此保留左边界的一次分部积分给
$$
512\{Y_6(k)-Z_6(k)\}=-s_0^5\mu_0M_3/3.
\tag{26}
$$

再取实际右包的三个矩 $n=(n_0,n_1,n_2)$。整个左域上有 $R_w=xn_0$。由(18)逐 outer 槽极化，
$$
[h^{-4}]c^\to=-s_0^3n_0r/128.
\tag{27}
$$
原双线性配对、(9)及(25)遂给
$$
\boxed{
Z_6^\to(k;n)=\frac{s_0^5n_0M_3}{1536},\qquad
Y_6^\to(k;n)=\frac{s_0^5n_0M_3}{1536}.}
\tag{28}
$$
没有假设右包的任一矩为零，也没有把有尾单包当紧输入。

原 local self 是 $-ZZ$，raw pure 是 $-ZZ-4YC$；正式 pure 为 raw 的 $1/16$，有序交叉 raw 为 $-2ZZ^\to-4YC^\to$。沿 R402/R415 的完整配方，
$$
\begin{aligned}
\Lambda_u(V_6(k))
&=\frac45\left\{Y_6(k)-Z_6(k)
+\frac13Z_6^\to(k;\mu)+\frac23Y_6^\to(k;\mu)\right\}\\
&=\frac45\left\{-\frac{s_0^5\mu_0M_3}{1536}
+\frac{s_0^5\mu_0M_3}{1536}\right\}=0.
\end{aligned}
\tag{29}
$$
这证明(1)。对任意不交辅助 profiles 作真实多项式极化，全部有序 $3+2$ 自然读出也为零；不是只证明某个特定母包的 self 为零。

## 6. 权负六的整个静态 action 消失

现在才使用正字符假设。R415 已得同一个乘子
$$
\mu=2a_1p_2^*,\qquad
\lambda F_0(h,k,\omega)=h^{-6}a(k)-a_1kh.
\tag{30}
$$
取 $\omega=0$ 的 $h^{-6}$ 系数，得
$$
a(k)=\lambda(V_6(k)).
\tag{31}
$$

(29)给 $V_6(k)$ 的所有新增共同自然查询为零。若先取真实权投影 $\Pi_{-6}$，则完整自然核的原仿射稳定性使这些零值仍保持。R323 已付
$$
E(U_{-6})=E(\mathcal R_{-6}).
$$
故可减一个同权真实响应，使其 whole $E$ 值也为零；响应自然值本就全零。由于 $\lambda$ 通过共同 $J$ 下降且杀 $\mathcal R$，准确有
$$
\lambda(V_6(k))=0.
$$
这一步明确用了(29)的全自然零，不是从旧 $E$ 等像直接推出增强等像。

于是 $a(k)\equiv0$，特别 $a_1=a(1)=0$。代入(30)即得(2)。同一个 cocycle 收缩亦为
$$
\lambda\mathfrak c=0,\qquad \lambda\mathfrak c_D=0.
\tag{32}
$$
没有由此声称原 $U$ 值 cocycle 全零。

## 7. 真正剩余的门

权 $-6$ 现在只余完整速度二次 action
$$
\lambda\widehat Q_2=
h^{-6}\left\{
b_2(k)(h_s/h)^2+b_1(k)(h_s/h)k_s+b_0(k)k_s^2
\right\},
$$
$$
\begin{pmatrix}
b_2(k)&b_1(k)/2\\
b_1(k)/2&b_0(k)
\end{pmatrix}\succeq0.
\tag{33}
$$
这些仍由同一个真实字符给出。本稿未证明(33)只能为零；仍须保原
$v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0$、R129 的完整水平分部积分和真实右锚尾。尤其先微分
$Y=\partial_k+(2h)^{-1}\partial_\omega$，再设 $\omega=0$。

权 $-4$ 仍保 R415 的 $a(0)=0$ 与 $\mu=2a(1)p_2^*$，其全 $k$ 静态项及完整二次 PSD 均未由本稿处理。

本稿没有把静态单个系数当成真实闭路径，没有重新执行原 pure/self 研究，也没有宣布共同 whole $E$、全部低自然查询和全部 period 的 actual 联合截面已经完成。
