# R150 附录：实剪切碰撞的一支排除及剩余核上的真实有界归一化

日期：2026-11-13（UTC）。kernel_resume_1cf / Astra-ISP-1cf8c51d；根逐项复核完整 Bell 配方、实际平方根与差商、两向核等式和所有有限头的域。
状态：已证明的部分定理；给首位二维头之后的准确核归约，未排除剩余核，不作为完整循环性结论。
只处理普通一次符号 $F$；不将 $F^r$ 的 Bell 实现替换成下文算子的自然幂。

使用已核的 [R186 共同域和最大图](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)、[首位二维头记录](../notes/2026-11-13-real-beta4-exact-head-determinant-and-persistent-zero-root-kernel.md)及[低权剪切证明](R150-appendix-nonlinear-scalar-shears-degenerate-newton-edges-and-point-powers.md)。以下单独写出新增的有界根和实际域推导。

## 1. 范围、记号与已闭部分的扣除

令
$$
u=\sum_{j\ge0}a_j\chi_j,\qquad
v=\sum_{j\ge0}c_j\chi_j,\qquad a,c\in\ell^2,
\quad a_0=\alpha\ne0.
$$
允许常数并入 $X,Y$。假设原 $X_u$ 空谱，故任意复 $\ell^2$ 指数权
$w=b_*+\sum b_j\chi_j$ 下真实倾斜 $X=X_{u,b}$ 仍空谱。
置 $Y=X_{v,b}$、$L=X^{-1}\in A'$；$L$ 有界拟幂零。
实正非可和主行及实交替辅助行是这里主要实例；
以下代数计算本身只需上述空谱和真实首位条件。

记 $B_{ij}$ 为完整联合 Bell 系数：
$$
P_F(X,Y)=\sum_{i,j}\frac{B_{ij}}{i!j!}
\,\partial_x^i\partial_y^jF(X,Y),\qquad B_{00}=I,\quad B_{10}=B_{01}=0.
$$
始终保留 $B_{11},B_{21}$ 等交叉项；令 $B=B_{20}$。
规范最大闭实现和所有深域均取 R186 的实际闭图。

考察
$$
F(x,y)=(y-x^2)^2-4\alpha^2x^2-\lambda,\qquad \lambda\in\mathbb C.
\tag{1.1}
$$
已发表 R150 剪切附录关闭系数 $\beta\ne4\alpha^2$。
本稿仅固定碰撞值，并延续首位二维头笔记；
新 R236 的一条非可和主行、有限可和辅助行简单纤维结论也没有把这里
两个独立无界模式的核排除。

## 2. 普通四次符号的全部实际 Bell 项

逐项求导准确得到
$$
\begin{aligned}
P={}&(Y-X^2)^2-4\alpha^2X^2
+B(6X^2-2Y-4\alpha^2)\\
&+4(B_{30}-B_{11})X
+B_{02}+B_{40}-2B_{21}-\lambda I.
\end{aligned}
\tag{2.1}
$$
$P$ 的闭算子记作 $\mathsf P$。
式(2.1)先在覆盖全部中间词的共同自然域上成立，之后用规范闭包。
特别 $B_{40}$ 是完整 Bell 系数而不是单独四阶 cumulant。

令
$$
\mathsf T=\overline{\,Y-X^2-B\,}_{\rm can},\qquad
W=\mathsf T L,\qquad
\operatorname{Dom}W=\{f:Lf\in\operatorname{Dom}\mathsf T\}.
\tag{2.2}
$$
这是实际有界预复合，不是把 $YL$ 假定为全域有界。
$\mathsf T$ 闭且 $L$ 有界，所以 $W$ 闭。
R201 已说明在当前交替实例中，连 $YL^N$ 对任何固定 $N$ 都不全域有界。

取 R186 共同正则器 $R(s)$。任意固定足够深幂 $D_s=R(s)^N$
把 $H$ 送入这里全部自然词域，
$$
WD_s=(\mathsf T D_s)L\in A',\qquad D_s\to I\quad\hbox{强}.
\tag{2.3}
$$
$D_s$ 保持 $\operatorname{Dom}W$ 且域交换，故这些深域给 $W$ 的图核心。
下面只使用 $W$ 的闭性、实际预复合域和这些深域。
非临界支的跨核配对将转到 R186 已核的多项式最大图，
不需要预先声称 $W$ 的完整 $C$ 自伴，也不对未知限制沿用 $C$。

在全部共同深域上配方：
$$
\boxed{P L^2=W^2-\mathcal K,}
\tag{2.5}
$$
其中
$$
\begin{aligned}
\mathcal K={}&4\alpha^2I-4B
-4(B_{30}-B_{11})L\\
&-\bigl(B_{02}+B_{40}-B^2-2B_{21}
-4\alpha^2B-\lambda I\bigr)L^2.
\end{aligned}
\tag{2.6}
$$
这没有断言自然平方 $W^2$ 在原全域上闭；
后文只在真实深域使用 (2.5)。

## 3. 实际有界平方根，而非无界形式根

令
$$
\mathfrak B=\overline{\operatorname{alg}}(I,\mathcal A,L)
\subset A'.
$$
$\mathfrak B$ 是交换 Banach 代数。每个字符在 $\mathcal A$ 上等于其唯一字符，
又因 $r(L)=0$ 必须取 $L\mapsto0$。
因此 $\mathfrak B$ 也只有一个字符，记 $\phi$，满足
$$
\phi(B_{ij})=0\quad(i+j>0),\qquad \phi(L)=0.
$$
于是
$$
\phi(\mathcal K)=4\alpha^2\ne0.
$$
在 $\mathfrak B$ 中作通常有界全纯演算，唯一选定
$$
\boxed{E^2=\mathcal K,\qquad E\in\mathfrak B,\quad \phi(E)=2\alpha.}
\tag{3.1}
$$
可在单点谱 $4\alpha^2$ 的小邻域取该平方根分支。
所有有界因子、其单位逆及 $E$ 都保持任意闭 $A$ 不变空间和相关自然域。

定义闭算子
$$
J_+=W-E,\qquad J_-=W+E
\tag{3.2}
$$
在同一 $\operatorname{Dom}W$ 上；这里只使用有界扰动后的闭性。
在深域上 (2.5) 正是自然乘积
$$
P L^2=J_+J_-.
\tag{3.3}
$$

## 4. 非临界支 $J_+$ 的真实首商是单位

令 $\Gamma_\zeta(T)=U_\zeta T U_\zeta^*$，
$\zeta\ne1$ 为任意 dyadic 参数。
写
$$
D=\Gamma_\zeta(X)-X,\quad H=\Gamma_\zeta(Y)-Y,\quad
\Delta B=\Gamma_\zeta(B)-B,\quad
\tau=e^{-2b_0},\quad \kappa=\tau(\zeta-1).
$$
$N_0=A/d_0$ 是真实首位步长。
R124/R139 的实际余数计算（包括 $h=1$）给
$$
D=N_0d,\quad H=N_0h,\quad
\Delta B=N_0e,\qquad
d,h,e\in\mathcal A_{\zeta},
$$
且
$$
\phi(d)=-2\alpha\kappa,\qquad
\phi(e)=4\alpha^2\kappa.
\tag{4.1}
$$
$\Gamma_\zeta(L)=L(I+DL)^{-1}$，所以
$$
\Gamma_\zeta(L)-L=-N_0\,\Gamma_\zeta(L)dL
\tag{4.2}
$$
是真实有界除法，商字符为0。

设
$$
a=I+DL,\qquad
b=-2D+(H-D^2-\Delta B)L.
$$
$a$ 在 $\mathfrak B$ 中为单位。
由 (2.2) 在共同深域直接计算，
$$
a\,\Gamma_\zeta(W)=W+b
\tag{4.3}
$$
在此真实域上成立；下面不依赖将该式预先延拓成全局 $C$ 自伴关系。

式(2.6)、(4.1)—(4.2)逐项给
$$
\Gamma_\zeta(\mathcal K)-\mathcal K=N_0k,\qquad k\in\mathfrak B,
\quad \phi(k)=-16\alpha^2\kappa.
\tag{4.4}
$$
所有带 $L$ 的项对该字符为0。
又 $\Gamma_\zeta(E)+E$ 的字符为 $4\alpha\ne0$，是实际单位，所以
$$
\Gamma_\zeta(E)-E
=N_0 k\bigl(\Gamma_\zeta(E)+E\bigr)^{-1},
\quad
\phi\!\left(\frac{\Gamma_\zeta(E)-E}{N_0}\right)
=-4\alpha\kappa.
\tag{4.5}
$$
没有把一般零字符元素直接除以 $N_0$。

### 4.1 转到有完整 C 自伴保证的真实多项式最大图

定义 R186 的规范最大实现
$$
\mathsf P_E=\overline{\,Y-X^2-B-EX\,}_{\rm can}.
$$
这是有界 $A'$ 系数的真实有限混合多项式，完整 $C$ 自伴和核内深域均由 R186 给出。
在共同深域上
$$
P_E L=W-E.
$$
直接展开 gauge 差，得
$$
\begin{aligned}
(\Gamma_\zeta(P_E)-P_E)L
&=-(2D+\Gamma_\zeta(E)-E)\\
&\quad+[H-D^2-\Delta B-\Gamma_\zeta(E)D]L\\
&=N_0V_\zeta.
\end{aligned}
\tag{4.6}
$$
这里 $V_\zeta\in\mathfrak B$ 是实际有界商，
$$
\boxed{\phi(V_\zeta)=8\alpha\kappa\ne0.}
\tag{4.7}
$$
故 $V_\zeta$ 在原 $H$ 上有真正的有界交换逆。
改用 $Y-X^2-B+EX$ 则首商字符为0，不能同样排除。

令 $M_E=\ker\mathsf P_E$，取足够深
$f\in R(s)^NM_E$、$g\in U_\zeta R(s)^NM_E$。
$L$ 保全部中间自然词域，(4.6) 和原 $H$ 上的 $B$ 对称给
$$
\begin{aligned}
B(N_0V_\zeta f,g)
&=B(\Gamma_\zeta(P_E)Lf,g)-B(LP_Ef,g)\\
&=B(Lf,\Gamma_\zeta(P_E)g)=0.
\end{aligned}
$$
先以核内深域稠密性取极限，再用
$V_\zeta M_E=M_E$ 和 R23 的 $\overline{N_0M_E}=M_E$，得
$$
B(M_E,U_\zeta M_E)=0\qquad(\zeta\ne1).
\tag{4.8}
$$
R122/R125 的有限 Fourier 支撑论证给 $\dim M_E\le1$：
反射乘积只有零频；非零不变空间总本质支撑全测，
比较两个向量即可得到限制秩1。
单射拟幂零 $A$ 不容许非零有限维不变空间，故
$\ker\mathsf P_E=0$。

现在取 $f\in\ker(W-E)$。
$z=Lf$ 按定义属于 $\operatorname{Dom}\mathsf T$，
又 $z\in\operatorname{Dom}X$、$Xz=f$，所以
$$
\mathsf Tz-EXz=0.
$$
用 $z_s=R(s)^Nz$，真实域交换给
$z_s\to z$、$\mathsf Tz_s\to\mathsf Tz$、$Xz_s\to Xz$。
故 $P_Ez_s\to0$，由规范最大闭图的闭性，
$z\in\ker\mathsf P_E$。
$L$ 单射，于是
$$
\boxed{\ker(W-E)=0.}
\tag{4.9}
$$
这个步骤只把已知实际域上的 $L$ 像送进 $\mathsf P_E$ 的最大核，
没有假定 $YL$ 有界或混合自然和自动闭。

## 5. 原核准确等于剩余有界分支核

设 $M=\ker\mathsf P$。
R186 给任意固定足够深的 $R(s)^NM$ 在 $M$ 中稠密。
对该深域的 $f$，$Pf=0$ 且 $L$ 保持全部词域，
于是 (3.3) 给
$$
J_+J_-f=PL^2f=L^2Pf=0.
$$
由 (4.9)，$J_-f=0$。$J_-$ 闭，取深域逼近得到
$$
M\subseteq\ker J_-.
\tag{5.1}
$$

反向，取 $g\in\ker J_-$ 并用同一共同正则器取
$g_s=R(s)^Ng\to g$。
它保持 $\ker J_-$，在真正深域上
$$
L^2Pg_s=PL^2g_s=J_+J_-g_s=0.
$$
$L^2$ 单射，所以 $Pg_s=0$。
$\mathsf P$ 闭，令 $s\downarrow0$ 得 $g\in\ker\mathsf P$。
故
$$
\boxed{
\ker\mathsf P=\ker(W+E).
}
\tag{5.2}
$$
特别整个原核确实包含于 $\operatorname{Dom}W$，而且
$$
\boxed{W|_M=-E|_M\in B(M).}
\tag{5.3}
$$
$E$ 保持 $M$，因此 $M$ 还包含于全部 $W$ 的自然幂域。
若 $M\ne0$，$E-2\alpha I$ 在原空间拟幂零，限制仍拟幂零，所以
$$
\boxed{\sigma(W|_M)=\{-2\alpha\}.}
\tag{5.4}
$$
这是真实有界限制；没有从任意闭算子的形式二次关系直接推断有界性。
关键额外步骤是先独立证明 (4.9)，然后在核内深域消掉该因子并用闭性。

## 6. 与有限头兼容性的精确连接

剥离前 $n$ 个物理位，令
$$
U_n=\sum_{j<n}a_jR_j,\quad
V_n=\sum_{j<n}c_jR_j,\quad
s_n=\sum_{j<n}a_j,
$$
$X_t=X-U_n$、$Y_t=Y-V_n$，
$B_t=B-\sum_{j<n}a_j^2(I-R_j^2)$。
有限有界扰动保持空谱，故 $L_t=X_t^{-1}\in A'$。
定义真实尾归一化
$$
W_t=\overline{Y_t-X_t^2-B_t}_{\rm can}\,L_t.
$$
直接展开
$$
Y-X^2-B
=(Y_t-X_t^2-B_t)-2U_nX_t+C_n,
$$
其中
$$
C_n=V_n-U_n^2-\sum_{j<n}a_j^2(I-R_j^2)\in A'.
$$
因此在共同深域、随后以相同图核心闭包，
$$
\boxed{
W_t=W(I+U_nL_t)+2U_n-C_nL_t.
}
\tag{6.1}
$$
所有右侧有界因子保持 $M$。由 (5.3) 得整个 $M\subseteq\operatorname{Dom}W_t$，
并且 $W_t|_M$ 有界；若 $M\ne0$，其单点谱为
$$
\boxed{\sigma(W_t|_M)=\{-2\alpha+2s_n\}.}
\tag{6.2}
$$
$n=1$ 正好给0，吻合首位二维头行列式保留的共同零根；
$n=2$ 给 $2a_1$，吻合两个物理位的头范数计算。

如果主行正且不可和，$s_n\to\infty$，这些必要谱点发散。
但尚没有证明 $W_t|_M$ 具有统一谱界：
$Y_tL_t$ 一般无界，尾 $\ell^2$ 小不能直接给这一界。
所以 (6.2) 目前是实际兼容性约束，不是矛盾。

## 7. 剩余的准确问题

原实碰撞核已归约为闭算子 $W+E$ 的单核；
其所有核向量对 $W$ 真正正则、限制有界且谱固定，
并满足所有有限头的 (6.1)—(6.2)。

仍须排除这个单核，或建立能与 (6.2) 冲突的真实尾限制估计。
不把全空间单射稠密传给未知限制；不假定正主系数支配辅助系数便有相对域包含；
不把自然平方当成点态幂。
