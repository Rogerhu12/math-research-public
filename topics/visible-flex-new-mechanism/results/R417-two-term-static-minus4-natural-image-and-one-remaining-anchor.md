# R417：权负四静态自然像的完整两项曲率结构与唯一剩余锚值

日期：2026-11-16。**完整纸面原式证明；没有执行新的 profile 评价、积分程序、原根恢复、符号消元、秩、人工检查或研究计算。**

沿 [R415](R415-two-anchor-negative-character-multiplier-and-complete-static-tail-cancellation.md) 与 [R416](R416-all-static-curvatures-have-zero-weight-minus6-natural-flux.md) 的同一原式，置
$$
V_4(k)=[h^{-4}(\log h)^0]F_0(h,k,0),\qquad
W_4=[h^{-4}k^8(\log h)^0]F_0(h,k,0).
$$
它们都是原 $U$ 的真实有限系数。本稿证明完整自然函数身份
$$
\boxed{\mathcal N(V_4(k))=(1+k^2)^3
\{\mathcal N(V_4(0))+k^2\mathcal N(W_4)\},}
\tag{1}
$$
其中 $\mathcal N(V)$ 表示 $u\mapsto\Lambda_u(V)$；原 self、正式 pure、有序 $2+2$ 和右锚势响应全部包含在内。有序 $3+2$ 查询也继承(1)，不是仅对某个母包的 self 等式。

因此 R413/R415 所余共同增强查询的权 $-4$ 正字符，其完整静态函数准确为
$$
\boxed{a(k)=\frac{a_1}{8}k^2(1+k^2)^3,\qquad
a_1=a(1)\ge0,\qquad\mu=2a_1p_2^*.}
\tag{2}
$$
本稿不把 $a_1$ 设为零。$\mathcal N(W_4)$ 的完整值仍需单独求出；旧 pure 坐标不能代替它。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)、[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)、[R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md)、R415、R416。所有下述比较发生在完整原式中，不依赖 R207/R210 的 pure 列关系反推 full 成本。

## 1. 原锚与记号

固定 $0<\ell<r_*$、同一右 collar 和
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
几何状态为 $h>0,k\in\mathbb R,\omega=0$，记
$$
S=1+k^2,\quad e=hx-k,\quad Q=1+e^2,\quad
K_0=kx^2-Sx/h.
$$
对真实紧 $u$，置
$$
v=u',\quad r=u'',\quad t=u''',\quad
L=v-xr,\quad G=u-xv/2,\quad M=x^2r-2xv+2u,
$$
$$
P=J(r^2),\quad J_1=J(xr^2),\quad C=J(x^2r^2+2v^2),
$$
$$
R=v^2+xP,\quad T=x^2v^2+xC,\quad F=x^2P-C.
\tag{3}
$$
这里 $F$ 是辅助二次输出，区别于 $F_0$。它们均取真实右零值；其左常数、仿射或二次尾保留。

为避免原八算子与同名 scalar 混淆，定义两个具体二次输出
$$
E=-\frac12\Phi_{p_0}(u,u)+\frac14\Phi_{s_1}(u,u)
=-\frac{uv}{2}+\frac{xv^2}{2}+\frac{x^2P}{8}+\frac{xJ_1}{4},
$$
$$
V=\Phi_{p_1}(u,u)
=-\frac{u^2}{2}+xuv-\frac{x^2v^2}{2}-\frac{x^2J_1}{4}.
\tag{4}
$$
这里的 $E$ 不是 whole 读出 $E=(\pi,Q)$。相应原双线性算子记为 $\mathbf E,\mathbf V$，$\mathbf R=\Phi_{r_1}$、$\mathbf T=\Phi_{t_1}$。

R73 的完整静态矩阵输出准确为
$$
q=\Phi_{m_0}(u,u)
=-\frac{S^2R}{8h^2}+\frac{kS E}{h}
+k^2V-\frac{S T}{8}-\frac{kh}{2}\Phi_{p_2}(u,u).
\tag{5}
$$
原第二局部 normal 分子是
$$
b=\frac{SR}{8h}
+k\left(\frac{uv}{2}-\frac{3xv^2}{8}-\frac{xJ_1}{4}\right)
+h\left(\frac{G^2}{2}+\frac T8\right).
\tag{6}
$$

## 2. 原 N0 的两个必要系数：全部 outer 槽的显式公式

本节 outer 为独立的右零函数 $f$，inner 为 $g^2$。把(3)(4)的所有二次输出加下标 $g$；没有要求 $f$ 或它们的左尾为零。下面三个函数由原二阶局部第一分子准确给出：
$$
A=\frac{R_g'}{16},\qquad
B=\frac{R_g-xR_g'}8,\qquad
C_a=\frac{x^2R_g'-2xR_g+F_g}{16},
$$
$$
a_g=\frac{SA}{h^3}+\frac{kB}{h^2}+\frac{C_a}{h}.
\tag{7}
$$
例如 $a_g'=QL_g g'''/(8h^3)$、同右端 $a_g(r_*)=0$，直接积分即得(7)。

为完整列出系数，定义以下只依赖 $f$ 的线性 Volterra 映射：
$$
\begin{aligned}
\mathsf A_f(H)&=(f''-f'/x)H+J(f'''H),\\
\mathsf B_f(H)&=(xf''-3f'/2+f/x)H+J(xf'''H),\\
\mathsf C_f(H)&=(x^2f''-2xf'+2f)H+J(x^2f'''H),\\
\mathsf D_f(H)&=f'H'+xJ(f''H''),\\
\mathsf E_f(H)&=xf'H'+xJ(xf''H'')-f'H,\\
\mathsf F_f(H)&=x^2f'H'+xJ(x^2f''H''+2f'H').
\end{aligned}
\tag{8}
$$
固定正窗口使这些写法中的 $1/x$ 合法；最终出现时也都带相应 $x$ 因子。本节这些符号是完整映射，不是只保最高 jet。

R416(11)的原权一次式可准确重写为
$$
\begin{aligned}
n_\gamma={}&G_f\left(\frac{\partial_h b_g}{2h}
-\frac{b_g}{2h^2}+\frac{xa_g}{2}\right)\\
&-\frac{S^2x}{4h^2}\mathsf A_f(a_g)
+\frac{kS}{4h}\{x^2\mathsf A_f(a_g)+2x\mathsf B_f(a_g)\}\\
&-\frac{Sx}{4}\mathsf C_f(a_g)
-\frac{k^2x^2}{2}\mathsf B_f(a_g)
+\frac{khx^2}{4}\mathsf C_f(a_g)\\
&+\frac{S}{8h^3}\mathsf D_f(q_g)
-\frac{k}{4h^2}\mathsf E_f(q_g)
+\frac1{8h}\mathsf F_f(q_g).
\end{aligned}
\tag{9}
$$
最后一行就是原 $-\Psi_\gamma$，包括其 $-k f'q_g/(4h^2)$ 来源。式(9)已经保原 $P/B$ 与全部 history 导数，不能再另加或删除一份链项。

R416 已证明 $[h^{-5}]n_\gamma=0$。由(5)(7)(9)，下一系数是
$$
[h^{-4}]n_\gamma=kS^2\,\mathcal T_3(f;g^2),
$$
$$
\begin{aligned}
\mathcal T_3={}&
\frac14\{-x\mathsf A_f(B)+x^2\mathsf A_f(A)
+2x\mathsf B_f(A)\}\\
&+\frac18\mathsf D_f(E_g)+\frac1{32}\mathsf E_f(R_g).
\end{aligned}
\tag{10}
$$

为列出另一个系数，置
$$
\mathcal K_0=
-\frac x4\{\mathsf A_f(C_a)+\mathsf C_f(A)\}
-\frac{\mathsf D_f(T_g)+\mathsf F_f(R_g)}{64},
$$
$$
\begin{aligned}
\mathcal K_1={}&
\frac14\{x^2\mathsf A_f(B)+2x\mathsf B_f(B)
-2x^2\mathsf B_f(A)\}\\
&+\frac18\mathsf D_f(V_g)-\frac14\mathsf E_f(E_g).
\end{aligned}
\tag{11}
$$
则完整式为
$$
[h^{-3}]n_\gamma
=S\left[
G_f\left(-\frac{R_g}{8}+\frac{xA}{2}\right)
+\mathcal K_0
+k^2(\mathcal K_0+\mathcal K_1)\right].
\tag{12}
$$
这里用到的是 $S^2=S+k^2S$，没有把 $S,k$ 当独立可调参数。

因此原 $h$ 势的两个必要系数准确为
$$
\boxed{
[N_0]_{h^{-3}}=kS^2\tau_3,\qquad
[N_0]_{h^{-2}}=S(\tau_0+k^2\tau_1),
}
\tag{13}
$$
其中
$$
\begin{aligned}
\tau_3&=-\mathcal T_3/3,\\
\tau_0&=-\frac12\left[
G_f\left(-\frac{R_g}{8}+\frac{xA}{2}\right)+\mathcal K_0\right],\\
\tau_1&=-(\mathcal K_0+\mathcal K_1)/2.
\end{aligned}
\tag{14}
$$
这是完整 outer/inner 算子公式。其 $\tau_0$ 在 $k=0$ 准确回到 R402(13)(14)。$F_*(k,\omega)$ 与原 $h$ 参考常数没有上述负幂；本节没有替换它们的定义。

## 3. N0 响应的两项结构及 Gamma 的范围

原正规静态值始终为
$$
F_0=v_0-\mathcal B_{m_0}N_0-\Gamma(m_0).
\tag{15}
$$
$m_0$ 最低为 $h^{-2}$，而 $[N_0]_{h^{-4}}=0$。于是 $\Gamma(m_0)$ 没有 $h^{-4}$，且本次势响应只有两对乘积：
$$
\boxed{
[h^{-4}]\mathcal B_{m_0}N_0
=S^3\left\{-\frac18\mathcal B_{\mathbf R}\tau_0
+k^2\left(-\frac18\mathcal B_{\mathbf R}\tau_1
+\mathcal B_{\mathbf E}\tau_3\right)\right\}.
}
\tag{16}
$$
原 $\mathcal B$ 对两个因子线性，(13)的全 outer 槽使(16)同时适用于其 self、pure 和有序尾。无需假任何势属于旧可调第三空间，也没有把其左尾删掉。

## 4. 完整静态 YC 收缩

原第三局部分子 $(c,0,ec)$ 仍由 R416(18)给出：
$$
c=-\frac{Gb'}{4h}+\frac{Lb}{8h}
+\frac{Qr q'}{16h^2}+\frac{(hv-er)q}{8h}
+\frac{J_e(u,q)}{16h^2}.
\tag{17}
$$
定义以下固定函数：
$$
C_4=\frac{J(tR')}{128},\qquad
C_3=\frac{J\{t(R-xR'-4E')\}}{64},
$$
$$
A_2=\frac{J\{t(T'+x^2R')-2LR'\}}{128}-\frac{LR}{64},
$$
$$
B_2=\frac{J\{t(2xE'-2E-V')\}}{16},
$$
$$
C_{20}=-\frac{GR'}{32}+\frac{LR}{64}+A_2,\qquad
C_{21}=A_2+B_2.
\tag{18}
$$
这些不是三阶 field 的独立数据；由(5)(6)(17)原样展开、同锚分部积分，准确有
$$
\boxed{
[h^{-4}]c=S^3C_4,\quad
[h^{-3}]c=kS^2C_3,\quad
[h^{-2}]c=S(C_{20}+k^2C_{21}).
}
\tag{19}
$$
例如 $rE'+J(rE'')=-J(tE')$，
$x rE'+J(xrE'')=rE+J(tE)-J(xtE')$；
这两条直接核对(18)的 $C_3,B_2$ 号。所有右零常数由同一 collar 支付。

对原 R56 完整密度，先保真实 history 导数，得到准确收缩
$$
\boxed{
\int t\,\mathcal R_H(Y,C)
=\frac1{2h^2}\int Qt(SL+khM)c
-\frac1{2h}\int tG\,b(u,q).
}
\tag{20}
$$
这里 $b(u,q)$ 是(6)的原双线性极化，$q$ 可以有左尾。为检查整个 $k$ 因子，未积分的 $P/B$ 项含 $K_0J(Qt c)/(4h)$。紧 outer 的原 Fubini 身份是
$$
\int tK_0J(Qt c)
=\int Qt c\,(K_0r-K_0'v+K_0''u),
$$
$$
K_0r-K_0'v+K_0''u=kM+(S/h)L.
$$
再用 $x+e(kx-S/h)=kQ/h$，与 $T_s/(2h^2)$ 的真实第二分量合成(20)。没有重设第三 history 的初值。

代(19)后，完整 $h^{-4}$ 收缩为
$$
Y_4(k)=S^3(Y_0+k^2Y_1),
\tag{21}
$$
其中可直接取
$$
Y_0=\frac12\int t(LC_{20}+x^2LC_4)
+\frac1{128}\int tG\,\mathbf R(u,R),
$$
$$
Y_1=\frac12\int t\{
LC_{21}+(M-2xL)C_3+(x^2L-2xM)C_4\}.
\tag{22}
$$
最后的 $\mathbf R(u,R)$ 保留真实有尾输入；它来自(20)的 $b(u,q)$ 链，不能省略。

## 5. 完整静态 ZZ 收缩

用 R416(8)的真实协变导数，原密度可先准确写为
$$
\begin{aligned}
\mathcal R_H(Z,Z)={}&
\frac{Q(q')^2}{8h^2}
-\frac{xbq'}{2h}-\frac{eqq'}{2h}
+\frac{bq}{h}+\frac{q^2}{2}\\
&+\frac{kxb^2}{2h}+\frac{K_0}{2h}J((b')^2).
\end{aligned}
\tag{23}
$$
其中 $S b^2/(2h^2)$ 与 $K_0B/x$ 的一项准确抵消；不是丢掉 normal 平方。

因此
$$
Z_4(k)=S^3(Z_0+k^2Z_1),
\tag{24}
$$
并有完整未降阶表
$$
512Z_0=\int t\{2R'T'+x^2(R')^2-4R^2-4xJ((R')^2)\},
$$
$$
\begin{aligned}
512Z_1=\int t\{&
64(E')^2-16R'V'+2R'T'+32xR'E'+x^2(R')^2\\
&-4xRR'-32(RE'+ER')+4R^2\}.
\end{aligned}
\tag{25}
$$
(23)逐幂代入(5)(6)即可核(25)。$Z_0,Y_0$ 回到 R402 的完整 $k=0$ 原表，包括其非局部项和真实左尾。

## 6. 为什么有序尾也保同一两项结构

式(21)(24)对任意真实紧 $u$ 成立，包括任意不交 $a u+b w$；没有预设某个 profile 的三个矩为零。原 raw pure 为 $-ZZ-4YC$，故从这一完整对角多项式抽取 $a^2b^2$，每个有序 $2+2$ 系数仍恰有 $S^3(A+k^2B)$ 的形式。

把一个真实右包对左域的依赖改写为其三个矩，是 R352 的原线性尾映射。这一步对 $h,k$ 不引入新系数，也不改变原右锚。由实际三个右包的矩基构造该映射后，再代 $\mu(u)$，因此自然读出中的两份 Green 补偿仍保相同的两项结构。不能跳过这一步，只从 local self 猜(1)。

原 $N_0$ 响应在(16)已经是完整多线性算子等式；其正式 pure 按响应公式提出公共因子 $2$ 后的 $1/8$ 归一化以及各有序槽也自动保同一结构。于是(15)的完整自然函数准确为
$$
\mathcal N(V_4(k))=S^3(\mathcal A+k^2\mathcal B)
\tag{26}
$$
对两个固定自然函数 $\mathcal A,\mathcal B$。在 $k=0$ 得 $\mathcal A=\mathcal N(V_4(0))$；而 $S^3k^2$ 的最高项是 $k^8$，$S^3$ 最高仅 $k^6$，故 $\mathcal B=\mathcal N(W_4)$，证明(1)。

等价地，可用原 $U$ 成员
$$
W_4'=\frac18V_4(1)-V_4(0)
\tag{27}
$$
代表同一个自然函数。这里仅主张 $\mathcal N(W_4')=\mathcal N(W_4)$，不把自然函数相等冒作整个 $U$ 中相等。

## 7. 正字符只剩一个静态锚值

取 R413/R415 的同一个权 $-4$ 正字符。已付
$$
\lambda F_0(h,k,\omega)=h^{-4}a(k)-a_1kh,\qquad
a(0)=0,\quad a_1=a(1).
\tag{28}
$$
所以 $a(k)=\lambda V_4(k)$。

式(1)是完整自然函数关系。取真实权 $-4$ 投影后，自然核由原仿射协变保持；再用
$$
E(U_{-4})=E(\mathcal R_{-4}),
$$
可减同权真实响应而不改变自然读出。因此任何通过共同增强查询下降、且杀 $\mathcal R$ 的 $\lambda$ 都满足同一关系
$$
a(k)=S^3\{a(0)+k^2\lambda(W_4)\}.
\tag{29}
$$
没有把旧 $E$ 等像单独用来杀新增自然方向。

因为 $a(0)=0$、$S(1)^3=8$，
$$
\lambda(W_4)=a_1/8,
$$
代入(29)即得(2)。$a(k)\ge0$ 在这个精确族上仅等价于 $a_1\ge0$，本稿没有额外推出其必须为零。

三个完整速度二次系数仍由同一个 $\lambda$ 给出，并须满足原 PSD。其 $\mu m_2=0$，但原 $N_0,N_2$、R129 水平微分及原右尾均未因此被删掉。

## 8. 下一最小对象与付费边界

现在静态权 $-4$ 的未知部分准确只需一个完整自然函数 $\mathcal N(W_4)$。它可以从旧完整静态 $M_{-2}$ 的单个状态
$$
(h,k,\omega,\log h)=(-4,8,0,0)
$$
读取，再取真实权 $-4$。这里的四元组是原指数标签，不是一个几何状态值。

R210 已付该原 pure 系数的响应坐标；若以后由公开 Actions 读取新自然值，可先减原同权响应以使 universal pure 为零，再仅新增同锚 $\Omega=-4\int u'''M_{-2}(u,u)$。所有原 $N_0$ 已在旧静态原根中；$\Gamma$ 无本幂由前文证明。不能重复旧 pure/rank，不能只用其非零支撑漏掉完整 mixed 项，也不能由同 pure SHA 合并未求值的自然函数。

本稿未执行该新读出。若出现多字或非局部余项，必须完整保留；有限 profile 评价不替代 universal 恒等。当前结论是(1)(2)及原全槽表(13)(16)(19)–(25)，不是负权增强字符已全部排除或实际联合截面已经完成。
