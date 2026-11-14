# R221 — 全深除幂源、极坐标尾成本与原逆图的锋利分母

日期：2026-11-13。**状态：全深 Frobenius／除幂整性、原极坐标矩形的等距嵌入、真实交集见证及两项代价抵消、原逆图的首坏系数与完整 Newton 边、原 $l=1$ 候选的单位行障碍均已证明。没有得到由双完整中央零导致的新增深交集或主阶收益；主课题未完成。**

本文始终保留同一个原多项式源 $E_D=O[A,C]_{\le D}$ 和原完整连续前缀。全深分母来自 [R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)，交集是在 [R218](R218-all-degree-original-image-intersection-recursion.md) 的真实有限目标中计算。第 8—10 节说明：把原曲线写成图并截断，并不能免费提供 [R223](R223-large-prime-deep-smith-and-original-product-input.md) 所需的 primitive 深关系。

## 1. 全深权、强首项与已付对角源

取
$$
 p=4r-1\ge19,\qquad O=\mathbf Z_p,\qquad v_0=-22,
 \qquad A(w)=w+\cdots,\quad C(w)=v_0w^2+\cdots.
 \tag{1}
$$
令
$$
 q_n=\lfloor n/r\rfloor,\qquad
 e_n=
 \begin{cases}
 0,&q_n=0,\\
 q_n+\lfloor(q_n-1)/(p-1)\rfloor,&q_n\ge1.
 \end{cases}
 \tag{2}
$$
R173/R215 已证明 $e$ 单调、超可加，并且
$$
 \frac A w,\qquad\frac C{v_0w^2}\in\mathscr B_e,\qquad
 \mathscr B_e=
 \left\{\sum a_nw^n:\ v_p(a_n)+e_n\ge0\ \forall n\right\},
 \tag{3}
$$
两个单位的常数项均为一。记
$$
 \nu_e(f)=\inf_n\{v_p([w^n]f)+e_n\}.
 \tag{4}
$$
超可加性给 $\nu_e(fg)\ge\nu_e(f)+\nu_e(g)$。这个加权 Gauss 滤过完备。对常数项为一的 $\mathscr B_e$ 元素，形式逆仍在 $\mathscr B_e$：逐阶逆运算只用整加乘，各项偏移之和由超可加性支付。下文第 2 节还证明其零常数项在此拓扑下拓扑幂零。

对原单项式 $A^aC^c$，令
$$
                         \ell=a+2c .
$$
由 (3)，
$$
                p^{-e_\ell}A^aC^c\in\mathscr B_e.
 \tag{5}
$$
因此全深对角整源
$$
 \mathcal D_D=\bigoplus_{a+c\le D}O\,p^{-e_{a+2c}}A^aC^c
 \tag{6}
$$
确实映入同一个整目标。这不是免费的原源变换：
$$
 \operatorname{length}_O(\mathcal D_D/E_D)
       =\sum_{a+c\le D}e_{a+2c}
       \le\frac{2p}{p^2-1}D(D+1)(D+2)
       =O(D^3/p).
 \tag{7}
$$
这里用了 $e_n\le4pn/(p^2-1)$ 和
$\sum_{a+c\le D}(a+2c)=D(D+1)(D+2)/2$。以后比较新增源方向时，必须先扣除 (6) 中已经付过的对角整化。

## 2. 全深 Frobenius 与除幂源

**引理 1。** 对每个 $n\ge1$，
$$
                         e_{pn}\ge p e_n+1.                 \tag{8}
$$

**证明。** 若 $q=\lfloor n/r\rfloor=0$，则 $e_n=0$，而
$\lfloor pn/r\rfloor\ge3$，所以结论成立。若 $q\ge1$，写
$q=(p-1)t+a$，其中 $1\le a\le p-1$。置
$g(q)=q+\lfloor(q-1)/(p-1)\rfloor$，则
$$
                         g(pq)-p g(q)=a\ge1.
$$
又 $\lfloor pn/r\rfloor\ge pq$，由单调性得 (8)。$\square$

**引理 2。** 若 $X\in\mathscr B_e$ 且 $X(0)=0$，则
$$
 X^p\in p\mathscr B_e,\qquad
             X^j\in p^{v_p(j!)}\mathscr B_e\quad(j\ge0).
 \tag{9}
$$

**证明。** 展开 $X^p$。单一系数的纯 $p$ 次项由 (8) 至少获得一层 $p$；混合项的多项式系数均被 $p$ 整除，其余分母由超可加性支付。对任意固定输出行只有有限项，故同一证明适用于无限形式级数。于是
$X^p/p$ 仍是零常数项的 $\mathscr B_e$ 元素。反复施加第一式，得
$$
 X^{p^t}\in
       p^{(p^t-1)/(p-1)}\mathscr B_e.
$$
将 $j$ 写成 $p$ 进展开并相乘，指数之和恰为
$(j-s_p(j))/(p-1)=v_p(j!)$。$\square$

定义原极坐标
$$
              F=\frac{v_0A^2}{C},\qquad X=F-1,\qquad z=\frac CA.
 \tag{10}
$$
式 (3) 给
$$
 F\in\mathscr B_e,\quad F(0)=1,\qquad
 X\in\mathscr B_e,\quad X(0)=0,\qquad
                    z/w\in\mathscr B_e,\quad(z/w)(0)=v_0.
 \tag{11}
$$
这里没有声称 $X/w\in\mathscr B_e$；第 8 节的首坏系数恰好排除这种错误加强。由引理 2，
$$
                     F^p-1\in p\mathscr B_e.
$$
又 $e_{2p}=7$。故以下是同一原源中的全深整函数：
$$
 G_p=\frac{(v_0A^2)^p-C^p}{p^8}
       =\frac{C^p}{p^7}\,\frac{F^p-1}{p}
                         \in\mathscr B_e.                  \tag{12}
$$
它的两条原单项式均有角阶 $2p$。由于原系数确有八层分母，(12) 在次数 $2p$ 时不属于只允许七层分母的对角源 (6)。

模去 (6)，也可以用
$$
                         \frac{(v_0A^2-C)^p}{p^8}
 \tag{13}
$$
表示同一新增方向：两者的差只有中间二项式项，其系数至少带一层 $p$，而每项角阶仍为 $2p$。

### 第一项代价抵消：乘法后不能每列都多算一层

将 (12) 乘一个角阶 $\ell$ 的已整化单项式，所得源分母指数是
$8+e_\ell$，但新列的已付对角指数是 $e_{\ell+2p}$。实际新增量至多为
$$
                  (8+e_\ell-e_{\ell+2p})_+.                 \tag{14}
$$
写 $\ell=qr+s$，$0\le s<r$。因为 $2p=8r-2$，若 $s\ge2$，新增量为零；若 $s=0,1$，只有 (2) 的第二项没有出现额外进位时新增量为一，否则仍为零。$q=0$ 的边界也直接满足同一陈述。

所以这个全深 Frobenius 源给出一个真实、但无条件的源扩张。它没有使用完整中央零；其原分母成本与角阶增长不能重复计算为新的中央收益。

## 3. 极坐标确是原几何坐标，矩形确是原源

原 theta–sigma 平面满足
$$
 a=\vartheta^4,\quad b=\sigma^4,\quad s=b/a,\qquad
 A=a^{17}P(s),\quad C=a^{17}Q_C(s),
 \tag{15}
$$
其中 $P(s)=s+\cdots$、$Q_C(s)=v_0s^2+\cdots$ 是固定整有理多项式；固定分母在 $p\ge19$ 处都是单位。于是
$$
              F=\frac{v_0a^{17}P(s)^2}{Q_C(s)},\qquad
              z=\frac{Q_C(s)}{P(s)}.
 \tag{16}
$$
在 $(a,b)=(1,0)$ 处，$(X,z)$ 对 $(a-1,b)$ 的 Jacobian 行列式是
$17v_0$，为单位。因此 (10) 是原二维形式平面上的整局部坐标。这个二维事实不声称原一维曲线在 $X$ 上的图整；两者由第 8—9 节明确区分。

取 $h\ge0,l\ge1$，记
$$
 H_{h,l}(X,z)=\sum_{0\le i\le h,\ 0\le j\le l}h_{ij}X^iz^j
       \in O[X,z],\qquad L=2h+l.
$$
定义
$$
 \mathcal I_{h,l}(H)
       =A^lC^h H(F-1,z)\in E_L.                             \tag{17}
$$
其展开为
$$
 \sum_{i,j}\sum_{k=0}^i
  h_{ij}\binom ik(-1)^{i-k}v_0^k
        A^{\,l+2k-j}C^{\,h-k+j}.                            \tag{18}
$$
全部指数非负；原总次数 $h+l+k\le2h+l=L$。

**矩形等距命题。** 映射 (17) 对原系数 Gauss 范数是等距嵌入；同时在对角源 (6) 中，其准确最小加权系数赋值是
$$
                   \min_{i,j}\{v_p(h_{ij})+e_{L+j}\}.
 \tag{19}
$$

**证明。** 对固定 $j$，从 $X^i=(F-1)^i$ 到 $F^k$ 是一个整单位二项式矩阵。乘上的 $v_0^k$ 也是单位。不同 $(k,j)$ 在 (18) 中给不同原单项式，因为其角阶为
$$
             (l+2k-j)+2(h-k+j)=L+j,
$$
先决定 $j$，再由一个指数决定 $k$。这证明普通等距性。同一个 $j$ 块的角权恒为 $e_{L+j}$，所以同一单位变换也保留 (19)。$\square$

## 4. 真正的全深矩形尾预算

任意 $H=\sum_{i,j\ge0}h_{ij}X^iz^j\in O[[X,z]]$ 在原曲线上有加权 Gauss 收敛的求值。事实上
$$
                 \nu_e(X^iz^j)\ge v_p(i!)+e_j,              \tag{20}
$$
右侧随 $i+j\to\infty$ 趋于无穷。令 $H_{h,l}$ 为矩形截断，则
$$
 \nu_e\bigl(H(X,z)-H_{h,l}(X,z)\bigr)
              \ge\min\{v_p((h+1)!),e_{l+1}\}.
 \tag{21}
$$
而
$$
                      \nu_e(A^lC^h)\ge e_L.                 \tag{22}
$$

因而，若实际原几何另给
$$
 \nu_e(H(X(w),z(w)))\ge N,\qquad
                 v_p((h+1)!)\ge N,\quad e_{l+1}\ge N,
 \tag{23}
$$
那么原多项式 $P=\mathcal I_{h,l}(H_{h,l})$ 满足
$$
                 \nu_e(P)\ge M,\qquad M=e_L+N.
 \tag{24}
$$
(23) 的第一个条件必须来自固定的原曲线。这里没有把可自由选取未来轴系数的形式曲线当作这个算术输入。

## 5. 从一个实际原多项式得到真实交集

取 $D\ge L$、完整前缀 $k>2D$。沿用 R218，在同一个归一目标
$T_{k,M}=(O/p^M)^k$ 中置
$$
 K_D=\langle C^b:0\le b\le D\rangle_O+
           \langle AC^b:0\le b\le D-1\rangle_O,
$$
$$
 K=\operatorname{im}(J_{<k}|_{K_D}),\qquad
 Y=\operatorname{im}(J_{<k}|_{A^2E_{D-2}}),\qquad
                   \iota_{D,k,M}=\operatorname{length}(K\cap Y).
 \tag{25}
$$
这个定义保留 R216 的全部低 torsion，不要求 $r>2D$。

令
$$
 d_j=\sum_{i=0}^h(-1)^i h_{ij},\qquad S=h+l.
 \tag{26}
$$
它正是 $H_{h,l}(F-1,z)$ 的 $F^0z^j$ 系数。式 (18) 中 $A$ 次数为零或一只可能在 $k=0,j=l$ 或 $k=0,j=l-1$ 出现。因此 $P$ 的原直和分解
$E_D=K_D\oplus A^2E_{D-2}$ 的低部分准确等于
$$
                       P_K=d_l C^S+d_{l-1}AC^{S-1}.
 \tag{27}
$$

R214/R215 的全深双分量目标单位变换把原函数唯一写成
$U(C)+A V(C)$。将 $v_0$ 的幂再作单位缩放后，归一行可取为
$$
 p^{e_{2n}}[C^n]U,\qquad p^{e_{2n+1}}[C^n]V.
$$
因此 (27) 只有两条非零行，分别为
$p^{e_{2S}}d_l$ 和 $p^{e_{2S-1}}d_{l-1}$。

若 (24) 成立，则 $JP_K=-J(P-P_K)$ 在 $T_{k,M}$ 中成立，故
$JP_K\in K\cap Y$。其生成的循环子模的长度准确为
$$
 \boxed{\quad
 \left(M-\min\{e_{2S}+v_p(d_l),\
                        e_{2S-1}+v_p(d_{l-1})\}\right)_+.
 \quad}                                                     \tag{28}
$$
约定 $v_p(0)=+\infty$。这是实际交集中的兼容深层见证，不是从环境目标的长度猜出的下界。

若 $d_l$ 为单位，还可以得到一个彼此独立的明确族。对
$1\le b\le D-L$，取 $PC^b$ 与 $PA C^{b-1}$。它们仍满足 (24)，其低部分在行对
$2(S+b),2(S+b)-1$ 上的未归一系数矩阵为
$$
                       \begin{pmatrix}d_l&0\\d_{l-1}&d_l\end{pmatrix}
                       \in GL_2(O).
$$
各 $b$ 的行对不交。因此除 (28) 外还可加上
$$
 \sum_{b=1}^{D-L}
       \left((M-e_{2(S+b)})_++(M-e_{2(S+b)-1})_+\right).
 \tag{29}
$$
对别的 $H$ 所产生的族不能未经独立性检查再相加。

## 6. 第二项代价抵消：一般角向尾只留下至多两层

式 (28) 是准确正向准则，但使用一般尾条件 $e_{l+1}\ge N$ 时，不会自动给随 $N$ 增长的深循环。

由 (2)，长度为二的下标区间内 $e$ 最多增加二：$r\ge5$，其中至多跨过一个 $r$ 的倍数，而该处跳跃为一或二。故
$$
                         e_{l+1}-e_{l-1}\le2.
$$
又 $2S-1=L+l-1$，超可加性给
$$
 e_{2S-1}\ge e_L+e_{l-1}
           \ge e_L+N-2=M-2.                                \tag{30}
$$
(28) 中 $d_j$ 整，所以其循环长度至多二。(29) 的每个单行循环也至多二。

这是针对 (21)—(23) 这一一般矩形构造的准确抵消，不是对整个 $\iota$ 的上界。若要保持很小的 $l$ 而获得深交集，就必须证明原几何的特殊角向尾优于 $e_{l+1}$，或使用另一份实际原关系。下面检验最自然的 $l=1$ 原逆图。

## 7. 原 $X,z$ 的线性项与首共振

由固定原多项式及原椭圆对数的低阶展开，在参数 $s=b/a$ 上有
$$
 [s^2]A(s)=\frac{394}{15},\qquad
             [s^2]z(s)=770,\qquad [s]A=1,\quad[s]z=v_0.
 \tag{31}
$$
因此
$$
 \lambda=[w]X=[s]X
     =\frac{394}{15}-\frac{770}{-22}
     =\frac{919}{15}.                                      \tag{32}
$$
这里 (31) 中的二阶系数明确是 $s$ 系数；只使用 $w=s+O(s^2)$ 保证线性项不变。不能把 $s$ 与 $w$ 的二阶系数混写。

先取 $p\ne919$，故 $\lambda\in O^\times$。原第一带公式 R199 给
$$
 A(w)=e^{\beta w^r}f(w),\qquad
 C(w)=e^{\beta w^r}c(w)
$$
在本节所需有限阶上成立，其中
$$
 f=w+\cdots,\quad c=v_0w^2+\cdots,\qquad
 \mathfrak a=p\beta=17\tau_p\in O^\times.
$$
轴截面的相关系数整。因此
$$
 F=e^{\beta w^r}\frac{v_0f^2}{c},\qquad z=\frac cf,
$$
并给出
$$
 X_j\in O\ (j<r),\qquad
            pX_r\equiv\mathfrak a\pmod p,\qquad
 z_j\in O\ (j\le r).                                       \tag{33}
$$
所有这些是固定原曲线的系数陈述。即使两个完整中央条件同时为零，共同径向指数仍保留常数项一产生的 (33)。R203 的中央整正规式不消去这个普遍首共振。

## 8. 原逆图首个坏系数，及 $p=919$ 的例外

由于 $X(w)=\lambda w+\cdots$，存在唯一形式逆 $w=w(X)$；置
$$
                       \phi(X)=z(w(X)).
$$
从 (33) 的逐阶反演，
$$
 \phi_j\in O\quad(1\le j<r),\qquad
 \phi_1=\frac{v_0}{\lambda},\qquad
 p\phi_r\equiv-\frac{v_0\mathfrak a}{\lambda^{r+1}}\pmod p.
 \tag{34}
$$
特别 $v_p(\phi_r)=-1$。

**证明。** 到次数 $r-1$ 为止，严格逆只涉及整系数和单位 $\lambda$。次数 $r$ 唯一非整输入是 $X_r$，它在逆级数中的贡献为
$-X_r/\lambda^{r+1}$。复合 $z$ 时，线性项 $v_0w$ 保留这个贡献；$z$ 的其他项在该次数只读取逆的较低整系数。由 (33) 得 (34)。$\square$

在异常素数 $p=919$ 上，已由
$\phi_1=v_0/\lambda$ 得 $v_p(\phi_1)=-1$。所以这里同样没有整图；但下面依赖 $\lambda$ 为单位的完整 Newton 结论不直接用于这个例外。

因此，无论这些素数处完整中央条件是否为零，都不能把
$H(X,z)=z-\phi(X)$ 当作 $O[[X,z]]$ 中的实际关系，直接代入第 4 节的一般尾引理。

## 9. 全深 Newton 边、准确分母列与加权不收敛

本节仍假设 $p\ne919$。对每个整数 $d>0$，由 (2) 有
$$
 e_{d+1}\le\frac d{r-1},
 \quad\text{实数等号当且仅当 }d=r-1,
 \qquad
                         e_d<\frac d{r-1}.                 \tag{35}
$$
这里是实数直线上的等号陈述；不能改说取整后的权只在一个位置相等，因为低区间许多权都等于零。

**证明。** 若 $q=\lfloor(d+1)/r\rfloor=0$，第一式严格。若 $q=1$，$e_{d+1}=1$，仅最小的 $d=r-1$ 取等。若 $q>1$，
$$
 e_{d+1}
 \le q+\frac{q-1}{p-1}
 <q+\frac{q-1}{r-1}
 \le\frac d{r-1}.
$$
对 $e_d$ 同样计算；即使 $d=qr$，右端也严格较大。$\square$

设 $\epsilon_d=\lfloor d/(r-1)\rfloor$。由 (11)、(35)，
$X/(\lambda w)\in\mathscr B_\epsilon$，常数项为一。严格逆的无除法逐阶递推保留同一超可加权，且
$z/w\in\mathscr B_e\subset\mathscr B_\epsilon$。所以
$$
                    v_p(\phi_n)\ge
                     -\left\lfloor\frac{n-1}{r-1}\right\rfloor
                     \quad(n\ge1).                         \tag{36}
$$

这个界在一列完整深度上准确取到。令
$$
                   m=p^t,\qquad n_t=1+(r-1)p^t,\qquad t\ge0.
$$
则
$$
                         \boxed{\ v_p(\phi_{n_t})=-p^t.\ }  \tag{37}
$$

**证明。** Lagrange 公式给
$$
 \phi_n=\frac1n[w^{n-1}]
       z'(w)\left(\frac{X(w)}w\right)^{-n}.                  \tag{38}
$$
写 $X/(\lambda w)=1+U(w)$。由 (35)，每个 $U_d$ 的 Newton 点都在直线
$v=-d/(r-1)$ 上方，唯一在边上的非常数项是
$d=r-1$，且 $U_{r-1}=X_r/\lambda$ 的赋值为 $-1$。
而 $z'$ 的每个非常数项严格在这条边上方，因为
$$
 v_p([w^d]z')\ge-e_d>-\frac d{r-1}\quad(d>0).
$$
在总偏移 $m(r-1)$ 处，唯一可能达到赋值 $-m$ 的项，必须取 $z'$ 的常数项 $v_0$，以及恰好 $m$ 个 $U_{r-1}$。其贡献是
$$
 \frac{v_0}{n}(-1)^m
             \binom{n+m-1}{m}X_r^m\lambda^{-n-m}
 =
 \frac{v_0}{n}(-1)^m
             \binom{rm}{m}X_r^m\lambda^{-n-m}.
 \tag{39}
$$
当 $m=p^t$ 时，$n=1+(r-1)p^t$ 是 $p$ 单位：$t=0$ 时等于 $r$，$t\ge1$ 时模 $p$ 等于一。由二项式的模 $p$ 数码公式，
$\binom{rp^t}{p^t}\equiv r\pmod p$，也是单位。故 (39) 赋值准确为 $-m$，其余项至少为 $-m+1$，不能相消。得 (37)。$\square$

式 (36)—(37) 还给出原图的准确 $p$ 进收敛半径
$$
                              p^{-1/(r-1)}.                 \tag{40}
$$
这个首 Newton 边由原共同径向项控制，完整中央零不改变它。

还须检验把这张图重新代入原 $X(w)$ 时的拓扑。对所有 $n\ge1$，
$$
                   v_p([w^{rn}]X(w)^n)=-n.                 \tag{41}
$$
事实上，对每个 $j\ge1$，
$v_p(X_j)+(j-1)/(r-1)\ge0$；只有 $j=1,r$ 在边上。
$n$ 个因子的下标和为 $rn$ 时，边上组合只能是全部下标 $r$；其贡献 $X_r^n$ 赋值 $-n$，其余项严格较高。因此 (41) 不受更深 CM carry 影响。

在 $n=n_t$ 时，单项 $\phi_n X(w)^n$ 的第 $rn$ 行归一赋值准确为
$$
 -p^t-n+e_{rn}
       =-p^t+\left\lfloor\frac{(r-1)p^t}{p-1}\right\rfloor
                         \longrightarrow-\infty.           \tag{42}
$$
所以各项甚至不在加权 Gauss 范数下趋于零，级数
$\sum_n\phi_nX(w)^n$ 不在这个拓扑下收敛。

必须保留这个结论的精确范围：作为普通 $w$-adic 形式级数，复合仍然逐系数有意义，并且准确等于 $z(w)$。式 (42) 排除的是用第 4 节的整系数加权收敛和尾预算去截断它；它不声称形式复合不存在。

## 10. 原 $l=1$ 清分母候选必有一个单位行

本节仍取 $p\ne919$。这一结论把逆图障碍直接接到 R223 的原 primitive 深关系入口。

取 $h\ge1$，令
$$
                         d=2h+1<r,
$$
并取任意
$$
 \psi(X)\in O[X],\qquad \deg\psi\le h,\quad
             \psi(0)=0,\quad \psi_1=v_0/\lambda .
$$
特别可以取原逆图的截断 $\psi=\sum_{j=1}^h\phi_jX^j$，因为 $h<r$ 时这些系数由 (34) 整。将有理极坐标的分母清掉，得到原多项式
$$
                    R=A C^h\bigl(z-\psi(X)\bigr)\in E_d.
 \tag{43}
$$
它在原源中 primitive：$AC^h z=C^{h+1}$ 的系数是一；$\psi(X)$ 部分展开后全部是奇数正次幂的 $A$，不会消掉该列。

然而
$$
 \boxed{\quad
     p[w^{r+d}]R
        \equiv-\frac{v_0^{h+1}\mathfrak a}{\lambda}\pmod p
        \in\mathbf F_p^\times.
 \quad}                                                     \tag{44}
$$

**证明。** 由 (33)，$[w^r]z$ 整。对 $j\ge2$，
$[w^r]X^j$ 只读取下标至多 $r-j+1<r$ 的 $X$ 系数，因而也整。因此 $z-\psi(X)$ 的第 $r$ 项唯一非整贡献为
$-\psi_1X_r$，即
$$
 p[w^r](z-\psi(X))
       \equiv-\frac{v_0\mathfrak a}{\lambda}\pmod p.
$$
另一方面，$AC^h$ 的首角阶为 $d$，首系数 $v_0^h$；由 (3)，相对偏移小于 $r$ 的系数整。其可能的首坏相对项位于 $r$，但 $z-\psi(X)$ 的常数项为零，所以这一项不参与总阶 $r+d$。剩下的低偏移乘积全整，唯一非整项正是上述第 $r$ 项乘 $v_0^h w^d$。得 (44)。$\square$

由于 $d<r$，$e_{r+d}=1$。所以 (44) 表明原真实归一行
$J_{r+d}R$ 为单位。只要完整前缀 $k>r+d$，便有
$$
                  R\notin\mathcal Q_{T,p}(d,k)
                      \qquad\text{对每个 }T\ge1.
 \tag{45}
$$
这里 $\mathcal Q_{T,p}$ 是 R223 的同一个原深核；没有改换 Hasse 源或丢掉这一行。

因此，低次数 $l=1$ 图形候选可以取消若干原低行，却不能作为 R223 的 primitive 深关系。这个障碍来自首共同径向共振，并不由完整中央零解除。本文尚未排除其他原多项式组合：下一步需要让原中央条件作用于首 Newton 边之外的实际系数，并在同一个完整目标中证明相应深交集。

## 11. 已证范围与未完成输入

本文给出了两个可直接使用的正向输入：全深除幂源 (12)，以及从实际原关系到兼容交集的准确公式 (28)—(29)。同时支付了它们的原源成本和一般角向尾成本，不能将这些成本抵消前的长度算作深收益。

原逆图的整性、加权径向截断及其低次数 $l=1$ 特例均已被固定原系数排除。结论不排除其他更高角度的实际关系，也没有给整个 $\iota$ 的一般上界。由双完整中央条件推出足够多的深 Smith 方向或严格有符号范数收益，仍是主课题的未完成输入。

依赖：[R167](R167-closed-theta-sigma-plane-and-integral-dynamics.md)、
[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R199](R199-exact-first-band-exponential-and-complete-divided-image.md)、
[R203](R203-finite-central-companion-and-rational-row-lattices.md)、
[R206](R206-fourth-layer-interior-schur-and-true-deleted-column-quotient.md)、
[R214](R214-quadratic-pair-tail-recursion-and-deleted-c-image.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R216](R216-all-degree-nonunit-low-kernel-and-true-finite-quotient.md)、
[R218](R218-all-degree-original-image-intersection-recursion.md)、
[R223](R223-large-prime-deep-smith-and-original-product-input.md)。
