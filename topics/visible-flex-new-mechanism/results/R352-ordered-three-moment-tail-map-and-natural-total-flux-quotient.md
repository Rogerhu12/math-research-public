# R352：完整原成本的有序三矩尾映射与自然总通量商类

日期：2026-11-15。**完整纸面证明。没有执行新的 profile、原根、积分、秩或参数族计算。**

[R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md) 已证明，全部真实响应的总通量由正式 pure 及其有序 $2+2$ 交叉值准确恢复。该稿在一般原成本空间 $U$ 上定义了相应响应 annihilator，但尚未证明它与三个辅助右包的选择无关。

本稿付清这一具体缺口：**对于整个原 $U$，有序 pure 交叉项对右包的依赖恰通过其三个真实二阶矩因子化，且是完整输出函数的身份。** 所以 R344 的修正给出一个不依赖辅助包、线性作用于真实商 $U/\mathcal R$ 的自然五次 profile 泛函。

这不证明该泛函在 $U$ 上恒零或非零。尤其不把 [R350 的三个加速度平方生成族](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md) 已付结论扩大为 $H_1,H_2$ 或其余 normal 族。这里补的是原完整成本的结构桥，不是另一组数值零观察。

来源：[R56 原变系数恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 原二阶与三阶历史](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R105 原完整成本空间](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109 完整局部商公式](R109-local-density-of-the-complete-fourth-quotient.md)、[R248 原纯四次 forcing](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)及 R344。

## 1. 同一原锚、完整路径与原纯成本

固定一条实际有限路径 $B$，保持
$$
h>0,\qquad \omega_s=\frac{k_s}{2h},\qquad
z=x+\omega,\qquad e=hz-k.
$$
采用原共同右 collar $r_*$、共同 characteristic 起点 $s_0$，以及零 scalar 传入初值。几何应用仍须在实际共同物理区间上有 $z>0$ 的统一间隙。下文的 universal 函数身份采用 R105 已证明的无移动 $x$ 极点延拓；没有据此放宽实际几何门。

对称 forcing 规范固定为 $H(A,A)=(dA)^2$。用
$$
\mathcal K_B(A,B)=\int_B\mathcal R_{H(A,B)}(s,x)\,ds
\tag{1}
$$
表示完整 characteristic 配对。右端是整个 $x$ 函数；所有真实 $s$ 导数、局部项和累计值原样保留。参数路径与配对第二槽同用字母 $B$ 时，以 $\mathcal K_B$ 的下标区分。

记原 canonical 场
$$
Z(a,b)=\operatorname{Range}H(Y_a,Y_b),\qquad
C(a;b,c)=\operatorname{Range}H(Y_a,Z(b,c)).
\tag{2}
$$
Range 始终指 R56 的同锚原恢复式。对尚未付左 collar 或 period 的单项，它仍是实际右锚代数，不把该单项称为合法双 collar 周期场。

令 $F=f^2$、$D=F-\phi^2$。第二场是 $Z_D$，第三场是 $-2C(\phi;D)$，故原完整第四成本为
$$
V_B(F,\phi)
=-\mathcal K_B(Z_D,Z_D)
+4\mathcal K_B(Y_\phi,C(\phi;D)).
\tag{3}
$$
因此其原 raw pure 对角为
$$
\boxed{
P_B(q):=16\pi V_B(q)
=-\mathcal K_B(Z_q,Z_q)
-4\mathcal K_B(Y_q,C(q;q,q)),
}
\quad Z_q=Z(q,q).
\tag{4}
$$
式 (4) 是把 R248 的同一完整 forcing 送入 characteristic 配对，而非 ruling 配对；没有将二者的外积分互换。

原 $U$ 是实际同端口、零总二阶矩路径的完整成本的真实实线性跨度；R105 也可取 $M=T=0$ 的生成路径。下文先逐实际路径证明，再在这个原函数跨度中线性延拓。

## 2. 任意紧输入的完整第二左尾只依赖三个矩

对实紧 $w$ 定义原真实矩
$$
\mu(w)=
\left(
\int(w'')^2,\;
\int x(w'')^2,\;
\int\{x^2(w'')^2+2(w')^2\}
\right).
\tag{5}
$$
它们不在本稿中被设成零。写 $n=(n_0,n_1,n_2)$ 和 $d=h\omega-k$。

第一场分子为
$$
V_{Y_w}=(-w'/2,0,hw-ew'/2),
$$
所以
$$
(V_{Y_w})_x=(-w''/2,0,(hw'-ew'')/2).
$$
原 R56 右锚公式在整个 $w$ 支撑左方给 $B_Z=0$，且
$$
\begin{aligned}
P_Z
&=\frac1{8h}\int
\{(1+e^2)(w'')^2-2he\,w'w''+h^2(w')^2\}\\
&=\frac1{8h}\int
\{(1+e^2)(w'')^2+2h^2(w')^2\}.
\end{aligned}
$$
第二步只使用紧 $w$ 的普通分部积分。展开 $e=hx+d$，得到
$$
\boxed{
p_n(s)=
\frac{(1+d^2)n_0+2hd\,n_1+h^2n_2}{8h},
\qquad P_Z=p_{\mu(w)}.
}
\tag{6}
$$

令原几何系数
$$
K_0=kz^2-\frac{k^2+1}{h}z,\qquad
\lambda=\frac{h_sz-k_s/2}{h^2}.
$$
在这个真实左外域，R56 给
$$
\eta_Z=-\frac12(p_n)_s,\qquad
(W_n)_s=K_0p_n-\lambda(p_n)_s,\qquad
W_n(s_0,x)=0.
$$
因此定义
$$
\boxed{
W_n(s,x)=
\int_{s_0}^s
\{K_0(t,x)p_n(t)-\lambda(t,x)(p_n)_t(t)\}\,dt.
}
\tag{7}
$$
它对 $x$ 至多二次，对 $n$ 线性。三个多项式系数都是实际路径上的累计量，不另选初值，不将途中历史重新置零。

置
$$
A_n=\frac12(W_n)_x-\frac{(p_n)_s}{2h},
$$
并定义完整尾分子
$$
\boxed{
V_{\mathscr T_n}=(A_n,\;zp_n,\;eA_n-hW_n).
}
\tag{8}
$$
第三分量的二次项准确抵消，所以每个分量对 $x$ 至多仿射。这一降次不等于尾为零。

由原唯一右锚恢复，真实结论是
$$
\boxed{
Z_w(s,x)=\mathscr T_{\mu(w)}(s,x)
\quad\text{在整个 $w$ 支撑左方，}
}
\tag{9}
$$
这里等号包含全部 $s$、$x$ 导数。所有 $w$ 的形状依赖在该域已严格压到 (5)，不是近似展开或原尾的拟合。

## 3. 有序 $2+2$ 系数的完整场公式

取两个真实紧输入，满足
$$
\sup\operatorname{supp}u<\inf\operatorname{supp}w.
\tag{10}
$$
它们仍用同一个 $r_*$ 和 $s_0$。

不同支撑的第一 forcing 逐点交叉为零。因此
$$
Z_{\alpha u+\beta w}=\alpha^2Z_u+\beta^2Z_w.
\tag{11}
$$
另外，$Z_u$ 在整个 $u$ 支撑右方准确为零，包括全部真实导数。这来自同一右锚及原零 characteristic 初值，不需要支付 $Z_u$ 的左 collar。

于是 $H(Y_w,Z_u)\equiv0$，从而
$$
C(w;u,u)=0.
\tag{12}
$$
同理，$C(u;u,u)$ 与 $C(u;w,w)$ 均在 $u$ 支撑右方为零。原三线性展开是
$$
C(\alpha u+\beta w;\alpha u+\beta w,\alpha u+\beta w)
=\alpha^3C(u;u,u)+\alpha\beta^2C(u;w,w)+\beta^3C(w;w,w).
\tag{13}
$$
对 (4) 提取普通多项式系数，准确得到
$$
\boxed{
[\alpha^2\beta^2]P_B(\alpha u+\beta w)
=-2\mathcal K_B(Z_u,Z_w)
-4\mathcal K_B(Y_u,C(u;w,w)).
}
\tag{14}
$$

这里不套用 R248 的“完整 ruling 只有平方幅度”结论来删除整个 period 的其它混合项。特别 $\mathcal K_B(Y_u,C(w;w,w))$ 可能产生 $\alpha\beta^3$ 项；它不进入 (14)，但本稿没有将它设成零。

式 (14) 中两个 surviving 项都依赖右包第二场的真实左尾。第一项可以包含两个第二左尾的实际配对，第二项包含完整第三恢复及其 $s$ 积分。没有把任一微包的第二或第三场假设为紧。

## 4. 将右包换成真实三矩尾，不改变完整输出

把 (8) 当作整个 $x$ 轴上的多项式分子延拓，仍记为 $\mathscr T_n$。单独这个延拓一般不右零，也不声称它是新合法场。

但在
$$
H(Z_u,\mathscr T_n),\qquad H(Y_u,\mathscr T_n)
$$
中，另一个因子及其全部导数在 $u$ 支撑右方为零。因此两个 forcing 的四个原分子配对在共同右 collar 都为零，原 R56 锚定公式仍适用。

在 $u$ 的右方，原配对和替换配对都零；在其余域，(9) 给完整相等。所以
$$
\mathcal K_B(Z_u,Z_w)
=\mathcal K_B(Z_u,\mathscr T_{\mu(w)}),
$$
$$
C(u;w,w)
=\operatorname{Range}H(Y_u,\mathscr T_{\mu(w)}).
\tag{15}
$$
这些是完整函数身份。特别所有 $x$ primitive 仍由 $r_*$ 积分，所有 $s$ primitive 仍由 $s_0$ 积分。

对任意外部实三向量 $n$，定义
$$
\boxed{
\begin{aligned}
\mathscr G_{B,u}(n)
={}&-\frac18\mathcal K_B(Z_u,\mathscr T_n)\\
&-\frac14\mathcal K_B
\left(Y_u,\operatorname{Range}H(Y_u,\mathscr T_n)\right).
\end{aligned}}
\tag{16}
$$
它对 $n$ 线性，对 $u$ 为二次齐次，取值为原完整输出函数。由 (4)、(14)、(15)，
$$
\boxed{
\Gamma^\to_{\pi V_B}(u,w)
:=[\alpha^2\beta^2]\pi V_B(\alpha u+\beta w)
=\mathscr G_{B,u}(\mu(w)).
}
\tag{17}
$$
因子 $1/8,1/4$ 分别来自 (14) 的 $-2,-4$ 除以原 pure 规范 $16$。

(16) 可以用任意 $n$ 定义一个线性读出，并不意味着任意 $n$ 可由单个实紧 profile 实现。后文只通过三个实际包的矩基恢复所需外部向量。

## 5. 在原 U 上不依赖路径线性表示

若 $V=\sum_\nu a_\nu V_{B_\nu}\in U$，先按某一真实路径表示定义
$$
\mathscr G_{V,u}(n)=\sum_\nu a_\nu\mathscr G_{B_\nu,u}(n).
\tag{18}
$$
现在证明它只依赖原完整函数 $V$。

在 $u$ 与右 collar 之间取三个同形同宽实偶 bump 平移 $w_1,w_2,w_3$。其中心互异，真实矩向量为
$$
\mu(w_j)=(m,\;mc_j,\;mc_j^2+\sigma),\qquad m>0.
$$
对应行列式是
$$
m^3(c_2-c_1)(c_3-c_1)(c_3-c_2)\ne0.
\tag{19}
$$
这正是 R344 已付的三实际矩基，不作新的 rank 计算。

如果两种路径表示给同一个 $V$，它们的差的正式 pure 是整个 universal 函数零。由 (17)，两种 (18) 在三个基向量 $\mu(w_j)$ 上相同；再由 $n$ 线性，它们在所有 $n$ 上相同。

故得到一个真正的原函数映射
$$
\boxed{
(V,u,n)\longmapsto\mathscr G_{V,u}(n),
\qquad
V\in U,\quad
\Gamma^\to_{\pi V}(u,w)=\mathscr G_{V,u}(\mu(w)).
}
\tag{20}
$$
它还只依赖 $\pi V$：若 $\pi V=0$，同一矩基论证给 $\mathscr G_{V,u}=0$。这不需要事先知道 $\pi U=\pi\mathcal R$，也不使用任何未付奇权坐标表。

## 6. 任意辅助右包方案给同一个修正

可取三个或更多实际右包 $w_j$ 及实系数 $a_j$，只要求
$$
\sum_j a_j\mu(w_j)=\mu(u).
\tag{21}
$$
这些系数是线性读出权，允许有符号；不代表实现负成本或负平方幅度。

由 (20)，
$$
\boxed{
\sum_j a_j\Gamma^\to_{\pi V}(u,w_j)
=\mathscr G_{V,u}(\mu(u))
\quad(V\in U).
}
\tag{22}
$$
所以 R344 的辅助包位置、形状、宽度、数量及矩基选择全部从最终结果中消失。所有包仍须满足真实有序支撑条件；不能把同一式无条件移用于重叠辅助输入。

特别这不是仅在总通量收缩后发生的巧合：(22) 是整个输出函数的等式。在不同原实际几何路径上，(7) 的真实历史可以不同；(20) 只说它们在表示同一 $V$ 时产生同一个函数映射。

## 7. 自然的 U/R 总通量类

保持原 self 总通量
$$
\Omega_u(V)=\int u'''(x)V(u^2,0)(x)\,dx.
$$
定义
$$
\boxed{
\begin{aligned}
\Lambda_u(V)
={}&\Omega_u(V)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\end{aligned}}
\tag{23}
$$
式 (22) 证明这与 R344 的任意合法辅助方案完全相同。因此由该稿的全响应原 Green 定理，
$$
\boxed{\Lambda_u(\mathcal R)=0.}
\tag{24}
$$
没有重新假定无尾 $16/5$ 身份；第三项正是不能删除的有序尾修正。

对固定 $u$，(23) 在原 $U$ 上线性，遂给一个自然商读出
$$
\boxed{
U/\mathcal R\longrightarrow\mathbb R,\qquad
[V]\longmapsto\Lambda_u(V).
}
\tag{25}
$$
对固定 $V$，它是关于紧输入 $u$ 的齐次五次泛函：第一、第二项为三导外因子乘四次输出；第三项中 $\mathscr G$ 对 $u$ 二次、对 $\mu(u)$ 二次，再乘外因子。有限原 profile 模板保证这一陈述是原函数多项式身份，不是离散拟合。

若 $\pi V=0$，则 (20) 给
$$
\boxed{\Lambda_u(V)=\Omega_u(V).}
\tag{26}
$$
所以原 pure-zero 成本的总通量仍是最直接的新值目标。本稿没有把选择辅助包作为可能制造非零类的额外自由度。

在已付权 $-6$ 上，(23) 与 R338 的原三尾坐标公式相同；这只是 R344(39) 与 (22) 的合并，不产生新的 $U_{-6}$ 值判定。R342 的固定族零结果仍只限其声明族。

## 8. 平移导子的准确相容性

记原平移导子
$$
NV=\partial_xV-D_fV[f']-D_gV[g'].
$$
对纯和 self 取相应原槽导子。R105 的真实仿射不变性使 $N$ 作用于原 $U$；这里不假定整个响应空间对另一非仿射导子闭合。

先固定一个共同小平移参数，使 $u_t(x)=u(x+t)$ 及全部辅助包 $w_{j,t}(x)=w_j(x+t)$ 仍处于原 collar 内且保持次序。三个矩按同一个可逆三角矩阵变换，因此 (21) 的原权 $a_j$ 不变。

对 self，紧外因子给
$$
\Omega_u(NV)=-D_u\Omega_u(V)[u'].
$$
对 pure 项及 (22) 的整个有序读出，同样对原所有输入一起微分，输出 $\partial_x$ 项再与紧 $u'''$ 分部积分。故
$$
\boxed{\Lambda_u(NV)=-D_u\Lambda_u(V)[u'].}
\tag{27}
$$
辅助独立性保证右端是 (23) 本身的变分，不是某个随输入任意重选矩基的导数。

这里所有 $x$ 边项均由紧 $u$ 的 jets 消掉；没有使用中间输出左紧性。式 (27) 也没有将有序右尾的原常数设为零。

## 9. 对后继 normal 层的实际用途与范围

R109 的真实局部商公式为
$$
V_B=
\int_B(v-\mathcal B_mN_{\rm loc})\,ds
-\int_B\mathcal B_mH\,ds
-\frac16\int_B\mathcal B_A[A,m]\,ds.
$$
末两项属于原 $\mathcal R$。式 (23) 给一个不依赖辅助方案的读出，使后继可以逐原 normal 生成族研究同一个明确问题：
$$
\Lambda_u(v-\mathcal B_mN_{\rm loc})
\quad\text{作为完整紧 profile 泛函是否为零。}
$$
个别局部模板若尚未证明属于 $U$，应先在原有限环境空间按同一公式计算，待实际路径组合回到 $U$ 后再解释 (25)；不能把任意形式系数先宣称为实际可调成本。

R350 已付三个完整加速度平方族，其余 $H_1,H_2$、低权 normal 项及整个 $U$ 的值仍未由本稿支付。这里既没有新非零 witness，也没有 universal 零定理。

本稿也不将 total flux 代替逐包平台、退化点、全部 period 或同一个二阶 gauge 的联合范围。已有 whole pure/self 实际控制与内部点通量控制不能由 (25) 自动叠加；那些门仍须在真实共同核中处理。
