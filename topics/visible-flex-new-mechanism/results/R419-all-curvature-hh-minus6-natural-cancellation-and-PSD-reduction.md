# R419：权负六 hh 速度系数的全曲率自然零式与 PSD 的单方向缩减

日期：2026-11-16。**完整原式纸面证明；没有执行新的积分、符号程序、profile 评价、秩、人工检查或研究计算。**

令原 R130 完整正规二速度式为
$$
\widehat Q_2=\widehat Q_{hh}h_s^2+\widehat Q_{hk}h_sk_s+\widehat Q_{kk}k_s^2.
$$
对每个实际静态曲率 $k\in\mathbb R$，取
$$
V_{hh,-6}(k)=[h^{-8}(\log h)^0]\widehat Q_{hh}(h,k,0)\in U.
$$
本稿证明
$$
\boxed{\Lambda_u(V_{hh,-6}(k))=0
\quad\text{对所有真实紧光滑 }u\text{ 和所有 }k.}
\tag{1}
$$
完整原 $-\mathcal B_{m_0}N_2$、真正 second-history 导数、第三场对 second history 的导数、水平加速度正规化和有序两尾都进入(1)。单独的 $ZZ$ 或未经正规化的主项并不为零。

结合 R416 的全静态消去，R413/R414 共同查询上剩余权负六正字符的完整 action 只能为
$$
\boxed{\lambda\widehat Q_2=h^{-6}b_0(k)k_s^2,\qquad
b_0(k)\ge0,\qquad b_0(0)=0.}
\tag{2}
$$
最后一条用 R418。本稿没有把 $b_0(k)$ 对一般 $k$ 设零；全曲率 $kk$ 仍须继续。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)、[R415](R415-two-anchor-negative-character-multiplier-and-complete-static-tail-cancellation.md)、[R416](R416-all-static-curvatures-have-zero-weight-minus6-natural-flux.md)、[R418](R418-complete-kk-minus-six-natural-coefficient-and-common-query-cancellation.md)。R367 只用其独立成立的完整原势与 Green 公式，不使用已撤回的旧 H 非零结论。

## 1. 同锚记号与真正需要的最低幂

固定同一正窗口和右 collar，
$$
JF(x)=\int_x^{r_*}F(y)\,dy,\qquad u\in C_c^\infty((\ell,r_*)).
$$
写
$$
p=u',\quad r=u'',\quad t=u''',\quad
L=p-xr,\quad P=J(r^2),\quad R=p^2+xP,\quad j=J(tR'),
$$
$$
S=1+k^2,\quad \gamma=h_s,\quad \alpha=h_{ss}.
\tag{3}
$$
只在真实切片 $k_s=k_{ss}=0,\omega=0$ 上提取 $hh$ 系数。沿此切片 $k,\omega$ 均保持常数，因此 R129 对本项准确使用 $X=\partial_h$。没有在涉及 $kk$ 的地方擅自把水平 $Y$ 删除。

对任意右零输入定义原对称双线性算子
$$
\mathbf R(f,g)=f'g'+xJ(f''g'').
\tag{4}
$$
于是 $\mathbf R(u,u)=R$。它就是 R73 原坐标 $\Phi_{r_1}$，不是新增可调方向。

用三个实际积分缩写
$$
I=\int Lt\,j,\qquad Z=\int t(R')^2,\qquad K=\int L^3t^2.
\tag{5}
$$
同时记 $\mu_0=\int r^2,M_3=\int r^3$。真正左尾和原导数为
$$
R'(\ell)=\mu_0,\quad R''=2Lt,\quad
\int tR'=M_3/3,\quad \int Lrt=-M_3/6.
\tag{6}
$$
R415/R416 的完整左边界计算给
$$
\boxed{2I-Z=-\mu_0M_3/3.}
\tag{7}
$$
本稿不把这个非零右端当成零。

所有下文的“最低幂”指原有限 Laurent 表的严格系数，不是取小 $h$ 极限。在本方向上，R416 已付 $N_0$ 最低幂不低于 $h^{-3}$，而 $m_2$ 最低为 $\gamma^2h^{-4}$，故
$$
[h^{-8}\gamma^2]\mathcal B_{m_2}N_0=0.
$$
$\Gamma(m_2)$ 的最低幂也仅为 $h^{-4}$，不贡献本次 $h^{-8}$。二者只在此系数被排除，没有被一般删除。

## 2. 原第二场及两份不可遗漏的 history 配对

R56/R73 的第二局部分子为 $(a,b,ea)$，$e=hx-k$。所需完整最低项是
$$
a=\frac{S\gamma R'}{16h^3}+\text{较高 }h\text{ 幂},
\qquad b=\frac{SR}{8h}+\text{较高 }h\text{ 幂},
$$
$$
q_0=-\frac{S^2R}{8h^2}+\text{较高 }h\text{ 幂},
\qquad q_2=\frac{S\gamma^2R}{8h^4}+\text{较高 }h\text{ 幂}.
\tag{8}
$$
累计 second 值最后置零，但其导数仍为 $q=q_0+q_2$。真实协变导数中第一分量的三个必要项因此是
$$
-\frac{S^2R'}{16h^2}
+\frac{S\alpha R'}{16h^3}
-\frac{S\gamma^2R'}{8h^4};
\tag{9}
$$
相应第三分量的最低部分为其 $-k$ 倍。这使最高所需平方收缩有一个额外的 $1+k^2=S$，不能只平方第一分量。

原 $P_{ZZ,s},B_{ZZ,s}$ 还必须保
$$
-2P(K_Z,Y_q),\qquad -2B(K_Z,Y_q).
\tag{10}
$$
在 R56 的 $-\lambda P_s-\gamma B_s/h^2$ 中，(10)给出的
$h^{-8}\gamma^2$ 收缩准确为
$$
\frac{S^4}{256}\int t\{(R')^2+xJ((R'')^2)\}.
\tag{11}
$$
它不是零，也不是可重复计入另一份 $q$ 的项。

由(8)–(11)及原 $K_0P+(K_0/x)B$，得到 $ZZ$ 的未正规化系数
$$
[h^{-8}\gamma^2]\Omega(ZZ)
=\frac{S^4}{512}\int t\{5(R')^2+xJ((R'')^2)\},
$$
$$
[h^{-7}\alpha]\Omega(ZZ)=-\frac{S^4Z}{256}.
\tag{12}
$$
R129 从前式扣掉后一系数的真实 $h$ 导数，故
$$
\boxed{
Z_{hh}=\frac{S^4}{512}\int t\{-9(R')^2+xJ((R'')^2)\}
=\frac{S^4}{512}(-9Z-4K).
}
\tag{13}
$$
最后等号用紧 outer 的同锚 Fubini：
$\int xtJ((R'')^2)=-\int L(R'')^2=-4K$。不要求 $R$ 左紧。

## 3. 原第三局部值的完整最低表

为保留真实 outer 槽，先令外输入为 $f$、内输入为 $g^2$，并记
$$
L_f=f'-xf'',\quad R_g=\mathbf R(g,g),\quad
j_{fg}=J(f'''R_g').
$$
从 R56 原 $\eta_0/h$ 逐项取幂，在先求完真正 history 导数后得到
$$
\boxed{
\begin{aligned}
[h^{-4}]c_0(f;g^2)&=S^3j_{fg}/128,\\
[h^{-6}\gamma^2]c(f;g^2)
&=S^2\{3j_{fg}-L_fR_g''\}/128,\\
[h^{-5}\alpha]c(f;g^2)&=-S^2j_{fg}/128.
\end{aligned}}
\tag{14}
$$
例如 $\gamma^2$ 行在未合并之前来自
$$
-\frac{S^2}{8}\{3f''(R_g'/16)+L_f(R_g''/16)
+3J(f''R_g''/16)\}.
$$
利用
$f''R_g'+J(f''R_g'')=-j_{fg}$，即为(14)。
$\alpha$ 行由同一个原 $P_s$ 与 $T_{s\xi}$ 身份得到；不能先将 $\alpha$ 设零。

完整 $YC$ 的最低 $h$ 阶在本次取幂中只来自原 $P/B$ 项和它们的真实 $s$ 导数；$T_s$ 的其余项在此二速度权上没有 $h^{-8}$。原 $-Y_n$ 也不贡献：R416 的独立 outer 证明给 $n_\gamma$ 没有 $h^{-5}$，而原 $\Psi_\gamma$ 最低系数为 $h^{-3}$，所以本次所需幂为空。

对紧 outer，原 $P/B$ 收缩使用
$$
\int t\{p c+xJ(r c')\}=2\int Lt c.
\tag{15}
$$
先把局部状态导数作真实 $s$ 分部积分，再按 R129 扣加速度系数；尚未加入第三场对 second history 的 $C_Aq_0$ 项时，(14)(15)给
$$
\boxed{
Y_{hh}^{\,0}=\frac{S^4}{256}(-9I-2K).
}
\tag{16}
$$
为固定系数，第一次分部积分后的两行分别为
$$
[h^{-8}\gamma^2]Y^{\,0}=\frac{S^4}{256}(5I-2K),
\qquad
[h^{-7}\alpha]Y^{\,0}=-\frac{S^4 I}{128}.
$$
后者的 $h$ 导数贡献 $7S^4I/128$，所以得到(16)。

## 4. C_Aq0 与原 N2 的真正消去，含两端尾

这一步必须在完整自然配方中作，不能只删一个 local self 项。

原第三场对累计 second 的导数在本次系数给
$$
-4\int a'a(u,q_0)
=\frac{S^4\gamma^2}{256h^8}
\int Lt\,\mathbf R(u,R)'.
\tag{17}
$$
令 $X=\mathbf R(u,R)$。同右锚准确有
$$
X=pR'+xJ(rR''),\qquad X'=-j+2L^2t,
$$
所以
$$
I_X:=\int LtX'=-I+2K.
\tag{18}
$$
式(17)一般非零。

另一方面，R367 的完整 outer 势公式直接给
$$
[h^{-6}\gamma^2]N_2(f;g^2)
=\frac{S^2}{128}\{L_fR_g'-xJ(f'''R_g')\}
=\frac{S^2}{128}\mathbf R(f,R_g).
\tag{19}
$$
于是本次
$$
[h^{-8}\gamma^2]\mathcal B_{m_0}N_2
=-\frac{S^4}{1024}\mathcal B_{\mathbf R}(\mathbf R\circ\mathbf R).
\tag{20}
$$
这是原势的完整 outer 身份，不把 $\mathbf R\circ\mathbf R$ 假定为可调第三方向。

在(20)的响应中，self 与 raw pure 都是 $2\mathbf R(R,R)$；正式 pure 按原 $1/16$ 归一。右包矩为 $n$ 时，其有序 raw 系数为
$4n_0R'$。因此原自然三项逐一给
$$
\boxed{
[h^{-8}\gamma^2]\widehat\Lambda(\mathcal B_{m_0}N_2)
=-\frac{S^4}{640}(Z-4K)
+\frac{S^4}{5760}\mu_0M_3.
}
\tag{21}
$$
这里 $\widehat\Lambda$ 仅表示在这些已逐项验证尾因子化的 ambient 项上使用原配方；没有主张单独的(20)属于 $U$。

(17)的 self 自然贡献为 $S^4I_X/320$。其真正 $YC^\to$ 补偿贡献为
$-S^4\mu_0M_3/2880$：右包 $R_w=xn_0$，所以
$\mathbf R(u,R_w)'=n_0r$，用(6)即可得到这一原有序值。

由(7)(18)，这两项的和恰为
$$
\frac{S^4I_X}{320}-\frac{S^4\mu_0M_3}{2880}
=-\frac{S^4}{640}(Z-4K)+\frac{S^4\mu_0M_3}{5760}.
\tag{22}
$$
它与(21)相同。因此 $C_Aq_0$ 加原两尾与
$-\mathcal B_{m_0}N_2$ 在完整自然读出中准确抵消。

这也直接核对了 R367 独立 Green 公式的本次系数。右边的矩乘积没有在消去前被设为零；若漏掉(10)或(22)的尾，后面的最终零式就会失败。

## 5. 剩余 self 差与有序两尾

完成第4节的原势消项后，只需合并(13)(16)：
$$
Y_{hh}^{\,0}-Z_{hh}
=\frac{9S^4}{512}(Z-2I)
=\frac{9S^4\mu_0M_3}{1536}.
\tag{23}
$$
三阶平方项 $K$ 在完整差中准确消去，但剩余左矩仍非零。

现在取真实右辅助包，矩为 $n$。在整个左域
$R_w=xn_0,R_w'=n_0,R_w''=0$，故(13)的原 $ZZ$ 双线性极化给
$$
Z_{hh}^{\,\to}=-\frac{9S^4 n_0M_3}{1536}.
$$
用(14)(15)的独立 outer 版本，在第4节消项后的 $YC$ 中同样得到
$$
Y_{hh}^{\,0,\to}=-\frac{9S^4 n_0M_3}{1536}.
\tag{24}
$$
这两式没有要求右包的 $n_1,n_2$ 为零；本次最低幂只读到 $n_0$。完整三矩尾映射先由实际右包矩基定义，再代 $n=\mu(u)$。

由原自然配方
$$
\frac54\Lambda
=(Y-Z)+\frac13 Z^\to+\frac23Y^\to,
$$
(23)(24)给
$$
\frac54\Lambda_u(V_{hh,-6}(k))
=\frac{9S^4\mu_0M_3}{1536}
-\frac{9S^4\mu_0M_3}{1536}=0.
$$
证明(1)。$S^4$ 是从全部原最低幂获得的共同因子，不是把 $k=0$ 的答案猜测外推。

对任意真实不交辅助输入作五次多项式极化，原有序 $3+2$ 查询也为零。因此(1)在 R414 的同一个最小共同自然查询上成立，无需给辅助包额外 parity 或矩条件。

## 6. 正字符的 PSD 只剩全曲率 kk

取 R413/R414 允许的权负六正字符 $\lambda$。
R416 已付
$$
\mu=0,\qquad \lambda F_0=0.
$$
其完整二速度 action 为
$$
\lambda\widehat Q_2
=h^{-6}\{b_2(k)(h_s/h)^2+b_1(k)(h_s/h)k_s+b_0(k)k_s^2\}.
\tag{25}
$$
由(1)、同权 $E(U_{-6})=E(\mathcal R_{-6})$ 和 $\lambda$ 通过共同查询下降，准确得到
$$
b_2(k)=0\quad\forall k.
$$
这里先以同权真实响应消掉 whole $E$，自然值本就全零；不从旧 $E$ 等像单独推增强等像。

逐 $k$ 的原完整矩阵
$$
\begin{pmatrix}0&b_1(k)/2\\b_1(k)/2&b_0(k)\end{pmatrix}\succeq0
$$
迫 $b_1(k)=0$、$b_0(k)\ge0$。例如若 $b_1(k)\ne0$，固定非零 $k_s$ 再改变 $h_s/h$ 的符号和大小即可使二次式为负，与 PSD 矛盾。

R418 只在 $k=0$ 付共同查询 $V_{kk,-6}(0)$ 为零，故再得 $b_0(0)=0$，但非负函数可以在一个点为零而不恒零。下一仍须给出整个 $k$ 函数或进一步的完整关系。

本稿没有把二速度交叉项作为原 $U$ 值算子删掉；它只在满足全部前提的正字符下由 PSD 被迫为零。权负四的静态唯一 $W_4$、其二速度 PSD、全部实际 joint、period 与同一规范仍继续原 open 门。
