# R402：原静态低层的一个完整自然通量及势项、Green 尾的准确抵消

日期：2026-11-15。**完整纸面原式证明；没有执行新的 profile 评价、积分、符号程序、原根恢复、秩、人工检查或科学运行。**

本稿从原 $F_0=v_0-\mathcal B_{m_0}N_0-\Gamma(m_0)$ 出发，在真实静态状态线 $k=\omega=0$ 上完整取得
$$
\boxed{
V_*=[h^{-4}]F_0(h,0,0)\in U,\qquad
\Lambda_u(V_*)=\frac3{32}\int(u'-xu'')^4u'''.
}
\tag{1}
$$
原 $N_0$ 的完整外槽、原八矩归一化 $\Gamma$、正式 pure 的 $1/8$、有序 $2+2$ 及全部真实左尾均保留。式(1)不是只从局部最高导数猜出的值；全部非局部项在最后合成时准确消去。

这给出一个此前未求值的**静态低层系数**的非零自然通量。它属于原实际成本的线性空间 $U$；没有把单个 Laurent 系数直接称为一条实际 $M=T=0$ 闭路径。特别，本稿不以其符号宣告实际闭路径成本取得该符号，不把它当作 [R400](R400-weight-zero-natural-flux-kernel-and-three-static-function-criterion.md) 的三个零权函数 $n_2,n_4,n_6$ 已经求值。

来源为 [R56 原完整恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 原逐点八矩及第三链式项](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109 原端点势局部化](R109-local-density-of-the-complete-fourth-quotient.md)、[R130 十四族与真实 U](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R344 原响应 Green 与有序 pure](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md)、[R352 全 U 的三矩尾](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)及 [R393 完整 Q4 像](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)。

## 1. 原读出、静态线与全部右锚

固定合法正窗口 $0<\ell<r_*$，原右 collar 不变，
$$
JF(x)=\int_x^{r_*}F(y)\,dy,\qquad
u\in C_c^\infty((\ell,r_*);\mathbb R).
$$
几何状态为
$$
h>0,\qquad k=\omega=0,\qquad e=hx,\qquad Q=1+h^2x^2.
\tag{2}
$$
所以 $z=x>0$；本次状态系数分离不越过原坐标极点。

自然读出始终是
$$
\begin{aligned}
\Lambda_u(V)
={}&\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),\\
\mu(u)={}&(\mu_0,\mu_1,\mu_2)
=\left(\int(u'')^2,\int x(u'')^2,
\int\{x^2(u'')^2+2(u')^2\}\right).
\end{aligned}
\tag{3}
$$
$\mathscr G_{V,u}(n)$ 是原正式 pure 的有序 $2+2$ 对右包真实矩的线性尾映射。先取实际位于整个 $u$ 右侧的三个包，以原三矩基作线性组合，才可代入 $n=\mu(u)$。没有要求存在一个位于右方、却与 $u$ 有相同重心的单个包。

对本稿暂分开的 ambient 项，$\widehat\Lambda$ 表示同一配方，且每项均在下文证明有序三矩因子化。最终(1)的 $V_*$ 属于原 $U$，因此其合成值就是(3)，不再是一个未经证明的扩展选择。

置
$$
v=u',\quad r=u'',\quad t=u''',\quad
L=v-xr,\quad G=u-\frac x2v,
$$
$$
P=J(r^2),\qquad C=J(x^2r^2+2v^2),\qquad
R=v^2+xP,\qquad T=x^2v^2+xC.
\tag{4}
$$
这里 $R=\Phi_{r_1}(u,u)$、$T=\Phi_{t_1}(u,u)$ 是原二次输出；下文用 $\mathbf R=\Phi_{r_1}$ 表示算子，以免与响应空间 $\mathcal R$ 混淆。再记
$$
D=xv^2+C=J(L^2),\qquad
F=x^2P-C=xR-D.
\tag{5}
$$
本稿的辅助 profile $F$ 不表示目标张量或静态成本 $F_0$。

逐项真微分给
$$
\begin{gathered}
P'=-r^2,\quad C'=-x^2r^2-2v^2,\quad
R'=2vr+P-xr^2,\quad R''=2Lt,\\
F'=2R,\quad D'=-L^2,\quad
T'=x^2R'-F,\quad L'=-xt,\quad G'=L/2.
\end{gathered}
\tag{6}
$$
在左 collar，
$$
P=\mu_0,\quad C=\mu_2,\quad
R=x\mu_0,\quad T=x\mu_2,\quad
F=x^2\mu_0-\mu_2.
\tag{7}
$$
这些尾从未设为零。式(6)只用同一个右锚；例如
$D=J(L^2)$ 的积分常数由右零准确决定。

## 2. 原 N0 的必要系数：完整外槽，而非对角猜测

原 R109 的静态势为
$$
N_0=P_h+F_*(k,\omega).
$$
$P_h$ 是原第三权一次密度的真实 $h$ 原函数；$F_*$ 与参考 $h_*$ 所产生的积分常数不依赖 $h$。本节直接沿水平 $h$ 方向、在 $k=\omega=0$ 取 $h_s=1$，求这个原密度。不是在静态第四项中任意增加一个第三算子。

对独立 outer $f$ 和 inner $g^2$，把(4)–(6)加下标 $g$。原第二局部 normal 分子与第一分子是
$$
b_g=\frac{R_g}{8h}+h\left(\frac{G_g^2}{2}+\frac{T_g}{8}\right),
\qquad
a_g=\frac{R_g'}{16h^3}+\frac{T_g'-2D_g}{16h}.
\tag{8}
$$
原二阶密度在此静态线上为
$$
m_0(g,g)=q_g=-\frac{R_g}{8h^2}-\frac{T_g}{8}.
\tag{9}
$$

为显示所有来源，原 R73 的 $\ell-\Psi$ 在这一权一次槽为
$$
\begin{aligned}
n_\gamma(f;g^2)
={}&G_f\left(\frac{\partial_h b_g}{2h}
-\frac{b_g}{2h^2}+\frac{xa_g}{2}\right)
-\frac{x}{h}\left(P_a+\frac{B_a}{x}\right)
-\Psi_\gamma(f,q_g),\\
P_a={}&\frac{(Qf''-h^2xf')a_g+J(Qf'''a_g)}{4h},\\
B_a={}&\frac{(h^2xf-Qf'/2)a_g}{2h},\\
\Psi_\gamma(f,q_g)
={}&-\frac{Qf'q_g'}{8h^3}
-\frac{xJ_e(f,q_g)}{8h^3},\\
J_e(f,w)={}&J(Qf''w''+2h^2f'w').
\end{aligned}
\tag{10}
$$
第一行的 $-b_g/(2h^2)$ 来自完整协变导数的 $B$ 分量；它不能改号或删掉。

看似最低的 $h^{-5}$ 项准确为
$$
-\frac{x}{64}
\left\{f''R_g'+J\big((f''R_g')'\big)\right\}=0.
\tag{11}
$$
这里使用 $J(H')=-H$ 的原右零边界，不使用左紧性。下一项为
$$
[h^{-3}]n_\gamma
=-\frac{G_fR_g}{8}-\frac{L_fD_g}{32}
-\frac{x}{32}J(L_fR_g'-f'''D_g).
\tag{12}
$$
因此对 $h$ 取原真实原函数，
$$
[N_0]_{h^{-4}}=0,\qquad
[N_0]_{h^{-2}}=\tau,
$$
$$
64\tau(f;g^2)
=4G_fR_g+L_fD_g+xJ(L_fR_g'-f'''D_g).
\tag{13}
$$
用 $F_g=xR_g-D_g$、$F_g'=2R_g$ 和一次同锚分部积分，(13)准确化成
$$
\boxed{
64\tau(f;g^2)
=2fF_g'-f'F_g+xJ(f'F_g'').
}
\tag{14}
$$
内两槽按原对称双线性作极化；outer 始终独立。式(14)对原右零、左可有二次尾的 $f$ 仍成立。后文的 $\tau(R;u^2)$ 和 $\tau(u;u,R)$ 因而没有通过错误的紧输入变分获得。

(11)已排掉唯一可能的 $h^{-4}$ 势项。剩余 $h$ 原函数中的常数或 $\log h$ 不会给下一节的 $h^{-4}(\log h)^0$；$F_*(k,\omega)$ 也不能在此系数中出现。

## 3. 原 Γ 与完整 F0 系数

原 R130 的定义为
$$
F_0=v_0-\mathcal B_{m_0}N_0-\Gamma(m_0),
\qquad
\Gamma(M)=\sum_{\alpha=1}^{8}a_\alpha(M)F_\alpha.
\tag{15}
$$
$F_\alpha$ 是固定八个参考状态的原完整静态值，不能任意改成零。

但在本静态线上，(9)给
$$
m_0=-\frac{\mathbf R}{8h^2}-\frac{\mathbf T}{8}.
$$
故 $\Gamma(m_0)$ 只有 $h^{-2}$、$h^0$ 两幂，准确没有 $h^{-4}$。结合(13)，
$$
\boxed{
V_*=[h^{-4}]F_0
=[h^{-4}]v_0+\frac18\mathcal B_{\mathbf R}(\tau).
}
\tag{16}
$$
$[h^{-4}]$ 在有限 Laurent/log 表达中表示该幂的无 $\log h$ 系数。本式不是忽略八矩归一化，而是先保留(15)，再按其真实 $h$ 幂排除。

原 R130 的完整值跨度与有限 Laurent/log 系数跨度相同，因而 $V_*\in U$。这是一条实际**线性空间**结论；它不赋予该系数独立的正时间实现。单独的两项在下文可作为 ambient 原式收缩，只有(16)的完整合成被此处认作 $U$ 成员。

## 4. 静态原场：求完真实导数后才将历史值置零

原移动框架是
$$
T_s=kN,\quad N_s=-kT-B,\quad B_s=N.
$$
在本状态线上，第二场当前分子及其完整协变导数为
$$
V_Z=(0,b,0),\qquad
\nabla_sV_Z=
\left(\frac{q'}2,\ 0,\ -b+\frac{hxq'}2-hq\right),
\tag{17}
$$
其中 $b$ 为(8)、$q$ 为(9)。第三分量中的 $-b$ 来自 $N_s=-B$。累计 scalar 值最后置零，其导数 $q$ 不能同时置零。

第三场当前分子为
$$
V_C=(c,0,hxc).
$$
原 $P_{C,s},B_{C,s}$ 仍含
$-P_H(Y,Y_q),-B_H(Y,Y_q)$。把它们和 R56 的完整 $\eta_C$ 一起保留，得到
$$
\boxed{
c=-\frac{Gb'}{4h}+\frac{Lb}{8h}
+\frac{Qr q'}{16h^2}+\frac{Lq}{8}
+\frac{J_e(u,q)}{16h^2}.
}
\tag{18}
$$
特别
$$
128[h^{-4}]c=J(tR'),
$$
$$
128[h^{-2}]c
=-4GR'-2J(LR')+J\{t(T'+x^2R')\}.
\tag{19}
$$
这些式子保留(17)的真实历史导数及(18)最后的 primitive；不能只使用当前分子值。

记 $\mathcal R_H(A,B)$ 为原 R56 对称 forcing 配对的 characteristic 密度。直接代(17)(18)，紧 outer 的一次分部积分给
$$
\int t\,\mathcal R_H(Y,C)
=\frac1{2h^2}\int QLt\,c
-\frac1{2h}\int tG\,b(u,q).
\tag{20}
$$
例如未分部前第一部分为
$QLc/(4h^2)-xJ(Qt c)/(4h^2)$，使用
$\int xtJ(Qt c)=-\int QLt c$ 才得到(20)。
$b(u,q)$ 是(8)的原对称极化，而不是将有尾 $q$ 作为紧参数使用。

## 5. 收缩表所需的真实积分

下列记号只为列出完整恒等式：
$$
\begin{array}{ll}
B_0=\int v^3r^2,&B_1=\int xv^2r^3,\\
B_2=\int x^2vr^4,&B_3=\int x^3r^5,\\
A_1=\int xPvr^2,&A_2=\int P^2v,\\
A_3=\int x^2Pr^3,&A_4=\int Cr^3.
\end{array}
\tag{21}
$$
再记
$$
M_3=\int r^3,\qquad H_0=\int rR
=-\int ur^2+\int xvr^2,
$$
$$
H=2\int ur^2-4\int xvr^2+\int x^2r^3.
\tag{22}
$$
这里 $H,H_0$ 是本表的 cubic 积分，不是正常层 $H_1,H_2$。

后文表格由(6)及以下真实分部积分逐项得到：
$$
\begin{gathered}
\int Pv^2r=B_0/3,\qquad
\int xP^2r=-A_2+2A_1,\\
\int tR'=M_3/3,\qquad
\int x^2tR'=\int xtR=H,\qquad
\int tF=-2H_0,\qquad \int LR'=H.
\end{gathered}
\tag{23}
$$
若被积式没有紧 outer，原左边界另列，不以(23)省略。所有 $P,C,R,T,F$ 仍具有(7)的尾。

## 6. 原 v0：self、pure、两份有序尾

置
$$
Z_4=[h^{-4}]\int t\,\mathcal R_H(Z,Z),\qquad
Y_4=[h^{-4}]\int t\,\mathcal R_H(Y,C).
$$
由(17)–(20)，
$$
512Z_4=\int t(2R'T'+x^2R'^2-4xJ(R'^2)-4R^2)
$$
$$
=\int t(3x^2R'^2-2FR'-4R^2)+4\int LR'^2,
\tag{24}
$$
以及
$$
\begin{aligned}
512Y_4={}&-\int LR'^2-2\int xtRR'
+3\int x^2tR'^2+4\int Gt\,B\\
&-2\mu_0H_0+\mu_2M_3/3,\qquad
B=\mathbf R(u,R).
\end{aligned}
\tag{25}
$$
这里的 $B$ 可完整写为
$$
B=2v^2r+vP-2xvr^2+\frac23x^2r^3-\frac x3J(r^3).
\tag{26}
$$
用(23)，两项的差准确为
$$
\begin{aligned}
512(Y_4-Z_4)
={}&-\frac{152}{3}B_0+56B_1-30B_2+6B_3\\
&+16A_1-4A_2-4A_3-2\mu_0H_0-\mu_2M_3/3.
\end{aligned}
\tag{27}
$$

现在取实际右包矩 $n=(n_0,n_1,n_2)$。其第二场在整个左域准确为
$$
R_w=xn_0,\quad T_w=xn_2,\quad
b_w=x\left(\frac{n_0}{8h}+\frac{hn_2}{8}\right),
\quad q_w=-b_w/h.
$$
第三交叉场 $C(u;w^2)$ 的必要两项是
$$
128c_4^\to=-n_0r,\qquad
128c_2^\to=-2n_0u+2n_0xv-(n_0x^2+n_2)r.
\tag{28}
$$
它们来自同一个(18)，包括右包的真实 $s$ history。定义 $Z_4^\to,Y_4^\to$ 为相应双线性配对的收缩，则
$$
\boxed{
\begin{aligned}
512Z_4^\to(n)&=2n_0H+2n_0H_0+n_2M_3/3,\\
512Y_4^\to(n)&=2n_0H_0+n_2M_3/3.
\end{aligned}}
\tag{29}
$$
右包只在这里通过三个真矩进入；不是假设各单包恢复场紧。

原 local self 为 $-ZZ$，raw pure 为 $-ZZ-4YC$。
正式 pure 是 raw 的 $1/16$；有序交叉 raw 系数为
$-2ZZ^\to-4YC^\to$。所以(3)准确给
$$
\boxed{
\widehat\Lambda_u([h^{-4}]v_0)
=\frac45\left\{
Y_4-Z_4+\frac13Z_4^\to(\mu)+\frac23Y_4^\to(\mu)
\right\}.
}
\tag{30}
$$
代(27)(29)：
$$
\boxed{
\begin{aligned}
960\,\widehat\Lambda_u([h^{-4}]v_0)
={}&-76B_0+84B_1-45B_2+9B_3\\
&+24A_1-6A_2-6A_3+\mu_0H.
\end{aligned}}
\tag{31}
$$
$\mu_2M_3$ 和 $\mu_0H_0$ 在这个完整组合中消去，$\mu_0H$ 尚未消去。若只看 local self 或丢任一有序尾，不会得到(31)。

## 7. 原势响应的 self 与 pure：三份完整积分

令
$$
\mathsf T=\tau(u;u^2),\qquad
I=\int t\,\tau(R;u^2),\quad
J_*=\int t\,\tau(u;u,R),\quad
K=\int t\,\mathbf R(u,\mathsf T).
\tag{32}
$$
从(14)直接得
$$
64\mathsf T=4uR-vF+2xJ(vR'),
$$
$$
64\mathsf T'=4GR'-rF-2J(rR).
\tag{33}
$$
对混合 inner 所需的 $F_{u,R}$，全式为
$$
\begin{aligned}
F_{u,R}={}&-\frac{x^2}{3}J(r^3)-J(x^2r^3)
+4J(xvr^2)+\frac43v^3\\
&+2uP-2J(ur^2).
\end{aligned}
\tag{34}
$$
它由 $F_{u,R}=x^2J(rR'')-J(x^2rR''+2vR')$ 作原右端分部积分得到；未删除常尾。

将(14)(26)(33)(34)逐项代入(32)，用(23)给下面的完整表。列出数值的是对应积分前的系数；最后一列是真实额外尾。

| 左式 | $B_0$ | $B_1$ | $B_2$ | $B_3$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | 额外项 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| $64I$ | $-80/3$ | $70/3$ | $-10$ | $2$ | $-10$ | $2$ | $3$ | $1/3$ | $0$ |
| $64J_*$ | $8$ | $-26/3$ | $5$ | $-1$ | $-2$ | $0$ | $1$ | $1/3$ | $-\mu_2M_3/3-\mu_0H$ |
| $64K$ | $-8$ | $26/3$ | $-5$ | $1$ | $2$ | $0$ | $-1$ | $-1/3$ | $2\mu_0H_0$ |

表(35)。

此处(32)的 $J_*$ 是一个积分名称，不能与原 primitive $J$ 混淆。表中两个有尾方向分别来自真正的 mixed inner 和真正的 $\mathbf R$ 外作用；不能沿一个只对紧参数成立的对角公式无条件变分。

原完整响应公式对任意内对称 $\tau$ 都有
$$
\mathcal B_{\mathbf R}(\tau)(u^2,0)=2\tau(R;u^2),
$$
$$
8\pi\mathcal B_{\mathbf R}(\tau)(u)
=\tau(R;u^2)+2\tau(u;u,R)-2\mathbf R(u,\mathsf T).
\tag{36}
$$
所以本表的 self 收缩是 $2I$，正式 pure 收缩是
$(I+2J_*-2K)/8$。没有额外假定 $\tau\in W$。

## 8. 势响应有序 2+2 的原外槽与真尾

对实际右包 $w$ 记 $n=\mu(w)$。原尾(7)和完整(14)给
$$
\tau(u;w^2)=X_nu,\qquad
X_n=\frac{n_2D_--n_0D_+}{64},
$$
$$
D_-=\partial_x,\qquad D_+=x^2\partial_x-2x.
\tag{37}
$$
并且 $p_{\mathbf R}(n)=xn_0$。直接代入全部外、内槽，
$$
64\{\tau(p_{\mathbf R}(n);u^2)
+2\tau(u;u,p_{\mathbf R}(n))\}
=n_0(x^2P+C+4uv).
\tag{38}
$$
逐槽可更具体地核对为
$
64\tau(p_{\mathbf R}(n);u^2)=n_0(xF'-F),\qquad
128\tau(u;u,p_{\mathbf R}(n))=n_0(4uv-2xv^2).
$
二式相加正是(38)。式(38)保留 $P,C$ 原尾；不能把它们仅以局部项替换。

把(37)(38)放入原(36)的有序 $2+2$ 展开，准确得到
$$
\boxed{
8\Gamma^\to_{\pi\mathcal B_{\mathbf R}\tau}(u;n)
=q_{X_n\cdot\mathbf R}(u)
+\frac{n_0}{64}(x^2P+C+4uv).
}
\tag{39}
$$
这里 $q_{X\cdot\mathbf R}=X\mathbf R(u,u)-Dq_{\mathbf R}(u)[Xu]$；矩 $n$ 在该导子作用中固定，不先代成 $\mu(u)$ 后一起变分。

原 E8 三阶伴随及紧 outer 给
$$
\int t\,q_{X\cdot\mathbf R}(u)
=-3\int(Xu)'''R,
$$
$$
\int(D_-u)'''R=-M_3/3,\qquad
\int(D_+u)'''R=H.
\tag{40}
$$
于是(39)的完整收缩为
$$
\boxed{
512\int t\,\Gamma^\to_{\pi\mathcal B_{\mathbf R}\tau}(u;n)
=n_2M_3+n_0(5H+6H_0).
}
\tag{41}
$$
例如(39)第二项自身贡献
$n_0\int t(x^2P+C+4uv)$；其中每个原尾仍在。
对实际右包三矩作原有限线性读出后，才以 $n=\mu(u)$ 使用(41)。

由(36)(41)，同一个自然配方是
$$
\widehat\Lambda_u(\mathcal B_{\mathbf R}\tau)
=\frac85I-\frac45J_*+\frac45K
-\frac{32}{15}\int t\,\Gamma^\to(u;\mu(u)).
\tag{42}
$$
将表(35)逐列代入，得到
$$
\boxed{
\begin{aligned}
40\,\widehat\Lambda_u(\mathcal B_{\mathbf R}\tau)
={}&-\frac{104}{3}B_0+32B_1-15B_2+3B_3\\
&-8A_1+2A_2+2A_3-\frac{\mu_0H}{3}.
\end{aligned}}
\tag{43}
$$
这里 $A_4,\mu_2M_3,\mu_0H_0$ 均经完整表和真尾消去，而不是事先设为零。

## 9. 全 F0 合成：全部非局部项准确消失

为直接复核(16)，把两项统一乘以 $960$：

| 项 | $B_0$ | $B_1$ | $B_2$ | $B_3$ | $A_1$ | $A_2$ | $A_3$ | $\mu_0H$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $\widehat\Lambda([h^{-4}]v_0)$ | $-76$ | $84$ | $-45$ | $9$ | $24$ | $-6$ | $-6$ | $1$ |
| $\widehat\Lambda(\mathcal B_{\mathbf R}\tau/8)$ | $-104$ | $96$ | $-45$ | $9$ | $-24$ | $6$ | $6$ | $-1$ |
| 合计 | $-180$ | $180$ | $-90$ | $18$ | $0$ | $0$ | $0$ | $0$ |

因此
$$
\Lambda_u(V_*)
=-\frac3{16}B_0+\frac3{16}B_1-\frac3{32}B_2+\frac3{160}B_3.
\tag{44}
$$
最后只对紧 $L,r,v$ 作一次普通分部积分，
$$
\int L^4t=-2B_0+2B_1-B_2+\frac15B_3.
\tag{45}
$$
(44)(45)即为(1)。没有剩余未定的 primitive、Green 常数或 $C^2$ 余项。

## 10. 非零、真权与 Q4 字符头的准确范围

式(45)将结果写为连续 $C^2$ 五次泛函。它不恒为零：对其局部密度
$$
g(x,v,r)=-2v^3r^2+2xv^2r^3-x^2vr^4+x^3r^5/5,
$$
Euler 导数的最高 $u^{(4)}$ 系数为
$$
g_{rr}=-4v^3+12xv^2r-12x^2vr^2+4x^3r^3,
\tag{46}
$$
这不是自由 jet 的零多项式。紧局部扰动的变分基本引理因此证明存在真实 $C_c^\infty$ 输入使(1)非零。没有运行或指定一个有限阶平端多项式作为假 $C^\infty$ 见证。

按原自然读出的完整仿射协变，
$$
\Lambda_u(\mathsf P_{a,0}V)=a^2\Lambda_{u(\,\cdot\,/a)}(V),
$$
(1)的函数具有真实权 $-4$。在 R393 的九维 Q4 像记号中，它恰为
$$
\boxed{\mathcal N(V_*)=\frac3{32}F,\qquad F=D_{0,0}.}
\tag{47}
$$
这里不增加那九维函数像的维数；新信息是**原低层实际系数**已经读到这个非零方向。

R393 的权 $-4$ 候选头在 Q4 子空间上满足
$\ell(F)=c,\ell(G)=c/6$，其四次速度 action 为
$$
-\frac{c}{32h^8}\gamma^2\{\gamma^2+(d\gamma-h\delta)^2\}.
$$
而对本稿(47)的线性系数，准确有
$$
\ell(\mathcal N(V_*))=\frac{3c}{32}.
\tag{48}
$$
所以在 $c<0$ 时，该**静态 Laurent 系数**的读出与前述非负 Q4 型具有相反符号。

(48)没有证明 $\ell$ 已延拓到全部自然像，也没有证明一条实际闭路径取得负值。实际路径还要保原 $M=0$、frame/scalar 端点、$\Gamma$ 乘子、$N_0$ 端势及其它 $h$ 系数。线性系数属于 $U$ 不等于它有独立正时间实现。本稿不据(48)宣布增强正字符已经被排除。

## 11. 仍须真正求值的低层

本稿完成的对象仅为(1)这一个完整原静态系数。R130 的完整十四族中，原三个 $\widehat Q_2$ 仍未全部读取，$F_0$ 的其余状态系数也未被消去。

特别，R400 的三个零权函数
$$
n_i(u)=\Lambda_u(C_i),\qquad i=2,4,6
$$
仍未由(1)求值；它们不是沿本 $k=\omega=0$ 状态线提取的同一个系数。原 $H_*=C_2+\mathcal R$ 也不能因为正常 H 层的通量零就得到新结论。

下一可直接使用的事实是：完整低层并不自然消失；求值必须同时保
$v_0,\mathcal B_{m_0}N_0,\Gamma m_0$ 和有序 pure 尾。本稿的两张最终表给出一个全部相消均可核对的非零实例。它不支付 whole $E$ 与全部自然通量的实际联合截面，也不支付同一固定几何、同一二阶 gauge 的完整 period 或主课题。
