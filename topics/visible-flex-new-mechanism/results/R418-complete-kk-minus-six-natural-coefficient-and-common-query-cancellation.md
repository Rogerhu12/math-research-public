# R418：原 kk 二速度最低系数的完整自然通量与共同查询零值

日期：2026-11-16。**完整原式纸面证明；没有执行新的 profile、求积、符号程序、秩、人工测试或科学运行。**

本稿计算原 R130 正规二速度密度在 $k=\omega=0$ 的一个完整系数：
$$
V_{kk,-6}=[h^{-6}]\widehat Q_{kk}(h,0,0).
$$
这里 $\widehat Q_{kk}$ 是 $k_s^2$ 的系数，先完成全部真实水平微分、历史项和加速度分部积分，再限制状态。主结论为
$$
\boxed{
\Lambda_u(V_{kk,-6})
=\frac1{640}\int
\{5u'(u'')^4-3x(u'')^5\}.
}
\tag{1}
$$
原 $C_A m_0$、$-\mathcal B_{m_0}N_2$、两份 $ZZ$ history 配对、$-Y_n$、加速度势和有序 $2+2$ 尾均进入此式。没有剩余 primitive 或矩乘积。

式(1)是整个 $U$ 中该系数的自然函数身份，不是 principal 计算。它只处理这个状态线上的 $kk,h^{-6}$ 槽；不宣告另外两速度槽、全 $k$ 状态或整个负六权 PSD 条件为零。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)、[R386](R386-complete-quartic-velocity-natural-flux-and-a-new-mixed-direction.md)、[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)、[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)、[R412](R412-complete-weight-zero-natural-null-mothers-and-nineteen-common-targets.md)、[R414](R414-common-high-natural-quotient-and-actual-finite-C1-sections.md)。

## 1. 同一右锚、正规系数及实际空间

固定 $u\in C_c^\infty(I)$，右积分始终是
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
由 $u$ 生成的二、三次输出只要求原右零；它们的左尾不设为零。

记 $w=k_s$、$\beta=k_{ss}$。先在真实 $h_s=h_{ss}=0$ 切片上展开，保持
$$
\omega_s=\frac{w}{2h},\qquad
Y=\partial_k+\frac1{2h}\partial_\omega
=\partial_k-\frac12\partial_d,\qquad d=h\omega-k.
\tag{2}
$$
后一个写法固定 $h$，把状态坐标换成 $(h,k,d)$。即使最终取 $k=\omega=0$，$Y$ 也不能先置零。

原完整密度为
$$
L_2=v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0-\Gamma(m_2).
\tag{3}
$$
若其本切片为 $\beta\,\mathscr A+w^2\mathscr R$，R129 给
$$
\widehat Q_{kk}=\mathscr R-Y\mathscr A.
\tag{4}
$$
常值端 germs 使原边界势 $w\mathscr A$ 的两端值准确为零；没有删除 $N_0$ 的原常势。

R130 的完整正规值及有限 Laurent 系数均在原真实线性成本空间 $U$ 中。因此 $V_{kk,-6}\in U$。这不把一个 Laurent 系数当作独立正时间路径。

采用同一个完整自然读出
$$
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{5}
$$
$\mathscr G$ 是原 pure 有序 $2+2$ 三矩尾映射。在整个证明中，对右辅助包矩 $n$ 求状态导数时固定 $n$，最后才代 $n=\mu(u)$。

## 2. 原二次局部场及不能漏掉的水平导数

以下写
$$
p=u',\quad r=u'',\quad t=u''',\quad
P=J(r^2),\quad M=J(xr^2),\quad
C=J(x^2r^2+2p^2),
$$
$$
R=p^2+xP,\quad T=x^2p^2+xC,\quad
L=p-xr,\quad G=u-xp/2.
\tag{6}
$$
$C$ 在本节是原 primitive，不是第四成本。常用原式为
$$
P'=-r^2,\quad M'=-xr^2,\quad
R'=2pr+P-xr^2,\quad R''=2Lt,
$$
$$
T'=x^2R'-(x^2P-C),\qquad
T''=2x^2Lt-2L^2.
\tag{7}
$$

在一般状态令
$$
z=x+\omega,\quad e=hx+d,\quad Q=1+e^2,\quad
K_0=kz^2-\frac{k^2+1}{h}z.
$$
原第二局部分子为 $(a,b,ea)$，在本切片 $a=wA$，且
$$
A=\frac{Qr^2+2hJ(er^2)}{32h^3},\qquad
A'=\frac{Qrt}{16h^3}.
\tag{8}
$$
静态中分量准确为
$$
b=\frac{(e+k)J_e(u,u)}{8h^2}
+\frac{1+2e^2+ke}{8h}p^2-\frac e2up+\frac h2u^2.
\tag{9}
$$

现在只在已完成的表达式中取 $k=\omega=0$。此时 $e=hx,Q=1+h^2x^2$，
$$
b=\frac R{8h}+h\left(\frac{G^2}{2}+\frac T8\right),
\quad
q_0=m_0(u,u)=-\frac R{8h^2}-\frac T8,
\quad
q_2=m_{2,kk}(u,u)=-\frac M{16h^2}.
\tag{10}
$$
从原 R73 八矩先求 $Y$，得到完整算子身份
$$
\boxed{
Ym_0\big|_0=-\frac{\mathbf P}{16h^3}
-\frac{\mathbf L}{2h}+\frac{\mathbf U}{8h}
-\frac h2\mathbf Y.
}
\tag{11}
$$
这里 $\mathbf P=r_0,\mathbf L=p_0,\mathbf U=s_1,\mathbf Y=p_2$。其余四坐标为零。一般
$$
m_{2,kk}=-\frac{d\mathbf P}{16h^3}
-\frac{\mathbf S}{16h^2},\qquad
Ym_{2,kk}\big|_0=\frac{\mathbf P}{32h^3}.
$$
特别不能把(10)视为沿 $Y$ 不变。

所需其余真实导数为
$$
YA\big|_0=-\frac{xr^2+P}{32h^2},\qquad
Yb\big|_0=\frac P{16h^2}+\frac C{16}
-\frac{xM}{8}-\frac{xp^2}{8}+\frac{up}{4}.
\tag{12}
$$
令 $G_z=u-zp/2,L_z=p-zr$，则
$$
YG_z=-\frac p{4h},\qquad YL_z=-\frac r{2h}.
\tag{13}
$$
这两个分母不同；它们均保留在下面的加速度势求导中。

## 3. 原第三场与完整 YC 收缩

先在 $h$ 常、$k,d$ 任意的状态上写原式。记
$$
j_A=J(QtA),\qquad
A_u=K_0r-K_0'p+2ku,\qquad A_u'=K_0t.
$$
对一个原右零 $q$，定义
$$
c_q(q)=\frac{Qr q'}{16h^2}
+\frac{(hp-er)q}{8h}
+\frac{J_e(u,q)}{16h^2}.
$$
原第三局部第一分量是
$$
c=c_0+\beta C_b+w^2C_v,
$$
$$
c_0=-\frac{G_zb'}{4h}+\frac{L_zb}{8h}+c_q(q_0),
\qquad C_b=-\frac{j_A}{8h^2},
$$
$$
\boxed{
C_v=-\frac{QrA'}{16h^3}
-\frac{Yj_A}{8h^2}+c_q(q_2).
}
\tag{14}
$$
这是 R56 的全部 $T_{sx},P_x,P_s$ 收集结果；其中
$P_{C,s}$ 的 $-P(Y,Y_q)$ 已进入 $c_q(q)$。没有把累计 scalar 的真导数 $q$ 设零。

对完整第四 $YC$ 配对先作真实 $s$ 分部积分，得到
$$
\begin{aligned}
\Omega(YC)=\int\bigg\{&
\frac{QA_u\,t c}{2h}
+\frac{\theta_s Qrt c}{2h^3}
-\frac{tG_z}{2h}b(u,q)\bigg\}\\
&-4\int a'a(u,q)-\int t\Psi(u,n),
\qquad \theta=-w/2.
\end{aligned}
\tag{15}
$$
这里 $q=q_0+w^2q_2$，$n$ 是原第三 characteristic 密度，
$b(u,q)$ 与 $a(u,q)$ 是原对称极化，$q$ 可有二次左尾。
式(15)中的 $-Y_n$ 是完整 $\Psi$，不只是 $T_s$ 项。

核对(15)的两个关键位置如下。第三中分量的真实导数为
$(b_3)_s^{\rm loc}-b(u,q)$；其局部 $s$ 导数经分部积分与 $T_s$ 中另一份
$\theta p b_3$ 准确抵消。第一分量相应的 $-a(u,q)$ 与原 $P_s$ 的同一交叉项合为 $-4\int a'a(u,q)$。这些式子只用紧 outer，未假设 $q$ 左紧。

R367 的完整 Green 恒等适用于任意 $E\in E_8$。取 $q=q_0$ 后，
(15)中的 $-4\int a'a(u,q_0)$ 加其原有序尾，恰为
$(5/4)\widehat\Lambda(\mathcal B_{m_0}N_2)$。故与(3)中的
$-\mathcal B_{m_0}N_2$ 整项消去。**静态 $b(u,q_0)$ 链不在这个消项中。**

R402 的原外槽恒等给 $[h^{-4}]N_0|_{k=\omega=0}=0$。
由(10)，$\mathcal B_{m_2}N_0$ 因此不贡献本稿的 $h^{-6}$ 槽。
$\Gamma(m_2)=-\Gamma(\mathbf S)/(16h^2)$ 只有 $h^{-2}$，同样不贡献。
这两个结论是按原真实幂排除，不是将两项一般删除。

## 4. 保真提取两个 scalar 密度与加速度系数

以下 $Y$、$Z$ 两个下标分别指 $YC$、$ZZ$ 收缩，避免与状态导子 $Y$ 混淆。
先完成上述 $C_A m_0/N_2$ 消项。

在(15)中，$\beta$ 的系数与 $w^2$ 的系数分别是
$$
\mathscr A_Y=\int\left\{
\frac{QA_u t C_b}{2h}-4A'c_0\right\},
$$
$$
\mathscr R_Y=
\int\frac{QA_u t C_v}{2h}
-\int\frac{tG_z}{2h}b(u,q_2)+\mathscr D(n_1),
\tag{16}
$$
$n_1=[w]n$。在最终状态，
$$
\mathscr D(f)=-\int t\Psi_{w=1}(u,f)
=\int\frac{r^2f}{8h}
-\int\frac{Qr^2f''}{16h^3}.
\tag{17}
$$
(17)对带真实左尾的 $f$ 也成立：$p,r$ 的双 collar 零支付全部边项。

原 $ZZ$ 给
$$
\mathscr A_Z=
\int\left\{\frac{tA}{h^2}
\left(\frac Q2q_0'-(k+e)b-ehq_0\right)
-\frac{r(b')^2}{4h^3}\right\}.
\tag{18}
$$
写
$$
D_0=q_0'/2-kb,\quad E_0=eq_0'/2-b-hq_0,
$$
$$
D_2=YA+q_2'/2,\quad E_2=eD_2-A/2-hq_2,\quad
M_1=Yb+(k+e)A.
$$
则完整 $w^2$ 系数为
$$
\begin{aligned}
\mathscr R_Z=\int\bigg\{&
\frac t{h^2}(D_0D_2+E_0E_2+M_1^2/2)\\
&+\frac{A_u}{2h}\{Q(A')^2+2heAA'+h^2A^2\}
+\frac{(ke-1)tQA^2}{2h^2}
-\frac{t}{h^2}P_{A,q_0}\bigg\},
\end{aligned}
\tag{19}
$$
$$
P_{A,q_0}
=\frac{(Qq_0''-heq_0')A+J(Qq_0'''A)}{4h}.
\tag{20}
$$
最后一项来自原 $P_{ZZ,s}$ 的 $-2P(K,Y_q)$；因为
$2\theta/w=-1$，其符号为(19)所示。漏掉它会制造一个不存在的三阶平方余项。
在有序 $ZZ$ 中必须保这项的两个交叉，而不是只代一个尾。

式(16)–(20)明确给出 R129 所需的两个 $\mathscr R-Y\mathscr A$，没有把“先取状态值后的普通导数”替代 $Y$。

## 5. 一张可逐项复核的完整 self 表

为缩短表格，只在本节记
$$
\mathsf A=\int P r^3,\quad
\mathsf B=\int p r^4,\quad
\mathsf C=\int x r^5,\quad
\mathsf T=\mu_0\int r^3,\quad
\mathsf K=\int x^2Lr^2t^2.
\tag{21}
$$
这些是实际积分名称，不假定独立。按(7)(10)–(20)收集同一个 $h^{-6}$ 系数，得到

| 左式（均已乘 3072） | $\mathsf K$ | $\mathsf A$ | $\mathsf B$ | $\mathsf C$ | $\mathsf T$ |
|---|---:|---:|---:|---:|---:|
| $[h^{-6}]\mathscr R_Y$ | $-18$ | $6$ | $7$ | $-3$ | $-3$ |
| $[h^{-6}]\mathscr R_Z$ | $-18$ | $18$ | $7$ | $-2$ | $0$ |
| $[h^{-6}]Y\mathscr A_Y$ | $0$ | $4$ | $-1$ | $2$ | $-2$ |
| $[h^{-6}]Y\mathscr A_Z$ | $0$ | $16$ | $29$ | $-15$ | $0$ |

表(22)。

列出足够的中间原函数以固定这张表。原第三密度的两个低幂是
$$
[h^{-5}]n_1=-\frac{J(r^3)}{384},
$$
$$
[h^{-3}]n_1=
\frac1{64}\left\{
(u-xp)P+pM-\frac{p^3}{3}
+J((u-xp)r^2)-\frac x3J(xr^3)\right\}.
\tag{23}
$$
原静态 $c_0$ 满足 R402 的完整式
$$
128[h^{-4}]c_0=J(tR'),
$$
$$
128[h^{-2}]c_0
=-4GR'-2J(LR')+J(t(T'+x^2R')).
$$
用(11)–(13)在原式上求导，另得
$$
[h^{-5}]Yc_0=\frac{r^3}{768},
$$
$$
\begin{aligned}
[h^{-3}]Yc_0={}&
\frac{xpr^2}{64}+\frac{rM-LP}{128}
-\frac{x^2r^3}{192}\\
&-\frac{J(xr^3)}{96}+\frac{3J(pr^2)}{128}.
\end{aligned}
\tag{24}
$$
式(24)特别使用 $YL_z=-r/(2h)$。

还可以用下列真实积分分部直接复核表(22)：
$$
\int r^2J(r^3)=\mathsf T-\mathsf A,\qquad
\int pPrt=(\mathsf B-\mathsf A)/2,
$$
$$
\int xPr^2t=(-\mathsf A+\mathsf C)/3,\quad
\int Mr^2t=\mathsf C/3,\quad
\int P^2t=2\mathsf A,
$$
$$
\int p^2r^2t=-2\mathsf B/3,\quad
\int xpr^3t=-(\mathsf B+\mathsf C)/4,\quad
\int x^2r^4t=-2\mathsf C/5.
\tag{25}
$$
第一式保留了左侧 $\mu_0\int r^3$，不是对两条非紧 primitive 假施紧边界。

表中唯一三阶平方列 $\mathsf K$ 在 $\mathscr R_Y-\mathscr R_Z$ 中消去。
更低的 $h^{-8}$ 平方项也由同一个(20)抵消；本稿不靠它猜测(22)。
由表直接得
$$
\boxed{
3072[h^{-6}]
\{(\mathscr R_Y-Y\mathscr A_Y)
-(\mathscr R_Z-Y\mathscr A_Z)\}
=30\mathsf B-18\mathsf C-\mathsf T.
}
\tag{26}
$$
这里 $\mathsf A$ 已因真正的水平加速度校正消去；$\mathsf T$ 仍在。

## 6. 原有序尾与最后矩乘积的准确消去

取一个完全位于 $u$ 右方的实际辅助包，矩为
$n=(n_0,n_1,n_2)$。一般状态令
$$
C_n=(1+d^2)n_0+2hdn_1+h^2n_2.
$$
原第二分子和矩阵尾为
$$
A^\to=\frac{dn_0+hn_1}{16h^2},\qquad
b^\to=\frac{zC_n}{8h},\qquad
q_0^\to=\frac{K_0C_n}{8h}.
\tag{27}
$$
特别在最终状态，
$$
A^\to=\frac{n_1}{16h},\quad
b^\to=x\left(\frac{n_0}{8h}+\frac{hn_2}{8}\right),\quad
q_0^\to=-b^\to/h.
$$
这些尾的状态导数仍按(27)求，不能停在其瞬时值。

第三 tail 的两个加速度系数可直接由原(14)给出。
其中
$$
C_b^\to=\frac{A^\to F}{8h^2},\qquad
F=Qr-2hep+2h^2u,
$$
且
$$
[h^{-4}]c_0^\to=-n_0r/128,\qquad
[h^{-3}]Yc_0^\to=\frac{n_1r-n_0L}{128}.
\tag{28}
$$
为核(28)，可先保留(27)及原 $J_e(u,q_0^\to)$：
$$
J_e(u,q_0^\to)
=\frac{C_n}{8h}
\{-2kQp+2h(1-k^2)u\}.
$$
这同时保留 $k$ 微分与辅助矩固定的口径。

将(27)(28)代入(16)–(20)的真实交叉配对，得到

| 左式 | $3072[h^{-6}](\cdot)/(n_0M_3)$ |
|---|---:|
| $\mathscr R_Y^\to$ | $3$ |
| $\mathscr R_Z^\to$ | $9$ |
| $Y\mathscr A_Y^\to$ | $2$ |
| $Y\mathscr A_Z^\to$ | $8$ |

表(29)，其中 $M_3=\int r^3$。表格是多项式身份，$n_0M_3=0$ 时不作实际除法。

例如
$$
[h^{-6}]\mathscr R_Y^\to
=\frac{n_0M_3}{3072}+\frac{n_0M_3}{1536}.
$$
两项分别来自 $QA_utC_v^\to/(2h)$ 与完整
$\mathscr D(n_1^\to)$。对 $ZZ$，原 $T_s$ 给
$17n_0M_3/6144$，两个 history 交叉中剩
$n_0M_3/6144$，相加为表中 $9/3072$。不是将 $ZZ$ 的一份 primitive 假作紧输入。

原自然配方的精确比例是
$$
\frac54\Lambda=
(\Omega(YC)-\Omega(ZZ))
+\frac13\Omega(ZZ^\to)
+\frac23\Omega(YC^\to),
\tag{30}
$$
并对整个表达式作(4)。最后由实际矩读出取 $n=\mu(u)$，表(29)给
$$
3072[h^{-6}]
\left\{
\frac13(\mathscr R_Z^\to-Y\mathscr A_Z^\to)
+\frac23(\mathscr R_Y^\to-Y\mathscr A_Y^\to)
\right\}
=\mathsf T.
\tag{31}
$$
式(31)恰好消去(26)的最后一项。因此
$$
\frac54\Lambda_u(V_{kk,-6})
=\frac{30\mathsf B-18\mathsf C}{3072},
$$
乘 $4/5$ 即(1)。全部原右尾已在(27)–(31)中参与，不剩未指定的 Green 常数。

## 7. 与 Q4 旧完整像的准确关系

R393 的成本真权 $-6$ 一行是
$$
\mathfrak b_6(u)
=-\frac16\int p r^4+\frac1{10}\int x r^5.
$$
故本稿准确得到
$$
\boxed{\mathcal N(V_{kk,-6})=-\frac3{64}\mathfrak b_6.}
\tag{32}
$$
这是两个完整自然函数的等号，不只是它们的最高 jet 相同。它没有断言两个原成本本身相等或仅差已知响应。

该函数在全部紧 profile 上不恒零。例如其局部密度
$5pr^4-3xr^5$ 的 Euler 最高 $u^{(4)}$ 系数为
$60r^2(p-xr)$，不是自由 jet 零多项式；变分基本引理给真实紧 profile 的非零见证。这里只用纸面见证，不指定一个未经合法性证明的数值测试包。

## 8. 当前共同母库的真零查询与仍欠门

若 $U$ 为偶母且
$$
M_5(U)=\int (U'')^5=0,
$$
则
$$
\int U'(U'')^4=0,\qquad
\int y(U'')^5=0.
$$
对其任一实际幅度、中心、正宽
$$
u(x)=\rho U((x-\xi)/w),\quad w>0,
$$
第一项仍零，第二项为
$$
\int x(u'')^5
=\rho^5w^{-9}\xi M_5(U)
+\rho^5w^{-8}\int y(U'')^5=0.
\tag{33}
$$
所以 R412/R414 的全部不同最终母以及每条共同正仿射 self 查询，对
$V_{kk,-6}$ 都给零。这里保真实 $\rho,\xi,w$，没有假设所有实际包同宽或借用一个旧冻结母的数值。

由(1)的完整局部五次性，对任意不交 $u,v$ 都有
$$
[s^3t^2]\Lambda_{su+tv}(V_{kk,-6})=0.
\tag{34}
$$
因此实际右辅助矩基不必偶、不必 $M_5=0$，也不必与母库有相同 $D,E_5$。
R414 的**同一个最小共同自然映射** $\mathcal A$ 准确满足
$$
\mathcal A(V_{kk,-6})=0.
\tag{35}
$$

式(35)支付了一个原完整二速度锚系数的新增自然读出。它不把全部
$\widehat Q_{hh},\widehat Q_{hk},\widehat Q_{kk}$ 或 $k\ne0$ 的值删掉。
若后续使用 PSD 在一个锚上推出交叉项零，仍须对那个候选字符的完整矩阵逐项应用；不能将本稿单系数身份外推为全状态 PSD 已解。

共同低自然商、实际完整 totals、内部通量和同一 gauge 的全部 period 条件仍按原接口保留；本稿没有把线性系数(1)当作一个可独立执行且无基准的真实控制。
