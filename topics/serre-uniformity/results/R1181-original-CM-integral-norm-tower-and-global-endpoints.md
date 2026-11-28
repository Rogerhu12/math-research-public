# R1181：原 CM primitive 塔的整范数与全部精度的全局端点

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面，所有 $p>37$、所有 $n\ge1$，分别在 Gaussian
$p\equiv3\pmod4$ 与 cubic $p\equiv2\pmod3$ 情形。**
本篇接 R1178–R1179，将同一原 primitive 点矩的 CM 比较升到
$R_n=\mathbb Z/p^n$。高层 norm 的 degree 含 $p$；
证明不反除该 degree，也不借一个只在第一层成立的 restriction 单射。

令 $N=p^n$，保持 R1147 (1147.23) 的 exact-order-$N$ 全点矩
$\mathsf M_{d,n}$，以及相同正 Kummer 的圆单位
$\gamma_{3,n},\gamma_{5,n}$。在 Gaussian CM 中 $J=[i]$，
在 cubic CM 中 $J=[\zeta_3]$，均取真实 CM endomorphism。
则
$$
\boxed{
\begin{array}{c|cc}
 & (q_J^2)_*\mathsf M_{4,n}&(q_J^4)_*\mathsf M_{8,n}\\ \hline
\text{Gaussian}&-\dfrac{1+p^2}{2}\gamma_{3,n}
 &\dfrac{5(1+p^4)}2\gamma_{5,n}\\[2mm]
\text{cubic}&-\dfrac{1+p^2}{3}\gamma_{3,n}
 &(1+p^4)\gamma_{5,n}
\end{array}}
\tag{1181.1}
$$
原十二次矩也满足
$$
\boxed{
(q_{[i]}^6)_*\mathsf M_{12,n}
 =-\frac{61}{2}(1+p^6)\gamma_{7,n},\qquad
(q_{[\zeta_3]}^6)_*\mathsf M_{12,n}
 =-7(1+p^6)\gamma_{7,n}.}
\tag{1181.1a}
$$
这条延伸的完整范围核验见 §5.1；在对应惰性同余类中，
两个系数对全部 $p>37$ 都是单位。

这里 $q_J(v)=e_N(v,Jv)$，全部 tensor 和 polarization 保原规范。
两个 Euler 因子为整塔的实际因子，模 $p$ 后才变成一。

对这两个实际 CM fibre，固定原 $\delta$ 的一个
$\widehat\delta\in\mathbb Z_p^\times$ 提升，并以真实 CM 构造
$I_\infty^2=\widehat\delta$。用原高层 bilinear 系数
$\lambda_\infty=21(1+p^4)/11$ 作正确 pushout，完整全局 fibre 为
$$
\boxed{
\mathscr P_{E,\infty}
 =[x_{E,\infty},y_{E,\infty}]_*\Theta_\infty,}
\tag{1181.2}
$$
其中
$$
\begin{array}{c|cc}
 &x_{E,\infty}&y_{E,\infty}\\ \hline
\text{Gaussian}&\dfrac{\widehat\delta(1+p^2)}4
 &\dfrac{87\widehat\delta^2(1+p^4)}{44}\\[2mm]
\text{cubic}&\dfrac{2\widehat\delta(1+p^2)}9
 &\dfrac{160\widehat\delta^2(1+p^4)}{99}
\end{array}
\tag{1181.3}
$$
$\Theta_\infty$ 是原兼容圆单位 pair 的唯一全局
$\mathbb Z_p(3),\mathbb Z_p(5),\mathbb Z_p(8)$ Heisenberg lift。
因此在原正向 Frobenius/Hodge frame 中，若其坐标为
$(r_\infty,s_\infty,z_\infty)$，同一 CM fibre 的全部精度坐标为
$$
(x_{E,\infty}r_\infty,\quad
 y_{E,\infty}s_\infty,\quad
 x_{E,\infty}y_{E,\infty}z_\infty).
\tag{1181.4}
$$
没有 Bernoulli 非零前提。本篇只在确有 CM endomorphism 的端点
提升 $I$，不提升任意非 CM 曲线上的有限 Cartan label。

## 1. 原 primitive source 与真正的高层 ray norm

统一记
$$
K=\mathbb Q(i)\ \text{或}\ \mathbb Q(\zeta_3),\qquad
f=4\ \text{或}\ 3,\qquad
w=|\mathcal O_K^\times|=4\ \text{或}\ 6,
$$
并令 $\epsilon=\chi_{-4}$ 或 $\chi_{-3}$。
$p$ 在 $K$ 中惰性，故 $\epsilon(p)=-1$。

选择原合法辅助素数 $c\equiv1\pmod{12}$，
且 $c\bmod p$ 为 primitive root。
R1147 已付 primitive 矩的辅助独立性和全部根规范。
$\theta_c$ 作为函数在 $\mu_w$ 下不变，
而不是只把其绝对值作商。置
$$
F_N=K(N),\quad L_N=K(\xi_N),\quad
G_N=\operatorname{Gal}(L_N/K)=(\mathbb Z/N)^\times .
$$
CM reciprocity、class number one 与原 theta 的 rationality 给
$$
\operatorname{Gal}(F_N/K)
 =(\mathcal O_K/N)^\times/\mu_w
 \xrightarrow{\ N\ } G_N.
\tag{1181.5}
$$
范数在 residue units 上满射，在 principal units 上由未分歧
二次扩张的整 trace 满射逐层提升，故此箭头满射。
其 kernel 阶为
$$
\frac{p+1}{w}p^{n-1}.
$$
当 $n>1$ 时这个阶不是 $p$ 单位。

在原格中取 $P_1=\Omega/N$，$P_v=vP_1$，并令
$\xi_N=q_J(P_1)$，选择相容的 $P_1$ 和 $\xi_N$。
由原 Weil pairing
$$
q_J(P_v)=N(v)\,\xi_N.
\tag{1181.6}
$$
用加法记号表示 units，置真正的 field norm
$$
U_{c,N}=N_{F_N/L_N}\theta_c(P_1).
$$
全 primitive 点按 $\mu_w$ 取商后给
$$
\sum_{v\in(\mathcal O_K/N)^\times}
 \chi(Nv)[\theta_c(P_v)]
 =
w\sum_{b\in G_N}\chi(b)\sigma_b[U_{c,N}].
\tag{1181.7}
$$
这里 $\sigma_b(\xi_N)=\xi_N^b$，方向沿 R1178–R1179 的真实格标签。
(1181.7) 是 norm 的完整和，未反除其 kernel 的阶。

由于 $p$ 惰性，$v\in(\mathcal O_K/N)^\times$ 正好表示
exact-order-$N$ 的点，所以本节 source 精确是原 primitive 塔，
不是 all-vector 塔，也不漏掉某种非自由 basis 情形。

## 2. 全部字符的有理单位比较与整群环元素

令 $\chi$ 是 $G_N$ 的偶字符，其 Teichmüller 部分非平凡。
其 conductor 可以是 $p^m$，$1\le m\le n$。
R1178 (1178.4) 的 shifted Epstein 公式，在同一个
$N$-格上逐 residue 求和给
$$
\sum_{v\in(\mathcal O_K/N)^\times}
 \chi(Nv)\log|\theta_c(P_v)|^2
 =
-w\bigl(c^2-\chi(c^2)^{-1}\bigr)
       L'_{\mathbb Q}(0,\chi)L_{\mathbb Q}(0,\chi\epsilon).
\tag{1181.8}
$$
若 $\chi$ 的 conductor 小于 $N$，这仍是原式：
Dirichlet series 中的项恰为与 $p$ 互素的 ideals，
而它的 character 已在 $p$ 处 ramified。
等价地，可用原 theta norm distribution 降到 conductor 层。
全圆单位也由实际 cyclotomic norm distribution 给
$$
\sum_{b\in G_N}\chi(b)\log|1-\xi_N^b|^2
 =-4L'_{\mathbb Q}(0,\chi).
\tag{1181.9}
$$
没有在高层多出 $p^{n-m}$ 平均。

对 $1\le b<N$、$(b,p)=1$，定义有理整数分母为 $f$ 的系数
$$
t_N(b)=-\frac1f\sum_{j=0}^{f-1}j\,\epsilon(b+jN),
\qquad
\Theta_N=\sum_{b\in G_N}t_N(b)\sigma_b^{-1}
          \in\mathbb Z_p[G_N].
\tag{1181.10}
$$
因为 $\sum_j\epsilon(b+jN)=0$，conductor $fN$ 的 Bernoulli 公式
先作整消去，准确给
$$
L(0,\chi\epsilon)=\sum_{b\in G_N}t_N(b)\chi(b).
\tag{1181.11}
$$
即使 $\chi$ imprimitive，这也是同一 L-function：
所有多加的 modulus 因子仍只有已 ramified 的 $p$。
特别本式没有未消去的 $1/p^n$。

令
$$
K_c=c^2-\sigma_{c^2}.
$$
在 $\chi^{-1}$ eigenspace，$K_c$ 的 eigenvalue 为
$c^2-\chi(c^2)^{-1}$，而 $\Theta_N$ 的 eigenvalue 是 (1181.11)。
结合 (1181.7)–(1181.9)，得到
$$
[U_{c,N}]=\frac14K_c\Theta_N[1-\xi_N]
\tag{1181.12}
$$
在所有上述字符的 rationalized unit component 中成立。
系数 $1/4$ 与 $w$ 无关：全点侧的 $w$ 已在
(1181.7) 与 (1181.8) 两处同时出现，圆单位侧仍为四。

这里的 regulator 推理检查全部嵌入：
对字符值域的每个共轭字符重作 (1181.8)–(1181.9)，
再用 $G_N$ 的实际 $\sigma_b$ 重指标。
所得为 $L_N$ 的全部复 places。
$\theta_c(P_1)$ 及其 norm 在 $p$ 外为单位；
$L_N$ 的 $p$ 素点唯一，所以非平凡 Teichmüller 分量的
valuation 为零，属于普通单位格。
Dirichlet regulator 的单射性遂给 (1181.12)，
并非只从一个复 embedding 的对数相等作结论。

## 3. 在高层整格中比较，不反除 wild character 群的阶

固定 $r=2$ 或 $4$。写
$$
G_N=\Delta\times P_N,\qquad |\Delta|=p-1,\quad |P_N|=p^{n-1},
$$
并取唯一的整 Teichmüller idempotent $e_{-r}$，
投影到 $\Delta$ 作用为 $\omega^{-r}$ 的分量。
其分母仅为 $p-1$，为单位。

对 $e_{-r}$ 分量，所有 extension characters 都是 §2 的
非平凡偶字符。因此 (1181.12) 在该分量 rationalization 后成立。
它的两边原本就在整 $\mathbb Z_p$-unit 格中：
$K_c$ 和 $\Theta_N$ 都是整群环元素，$4$ 为单位。
rationalization 的 kernel 是 $p$-primary roots of unity；
这些 roots 在 $\Delta$ 上的角色为 $\omega$，
与 $\omega^{-2},\omega^{-4}$ 不同。
所以该 kernel 在 $e_{-r}$ 中为零，得到
$$
\boxed{
e_{-r}[U_{c,N}]
 =\frac14K_c\Theta_Ne_{-r}[1-\xi_N]
\quad\text{在整 unit 格中。}}
\tag{1181.13}
$$
这里没有逐个除以 $p$-power character idempotent 的分母，
也没有使用圆单位在整个单位格中的 index 为单位。

现在在 $R_n[G_N]$ 中置
$$
P_r=\sum_{b\in G_N}b^r\sigma_b.
$$
它满足
$$
P_re_{-r}=P_r,\qquad
P_r\sigma_a=a^{-r}P_r,\qquad
P_rK_c=(c^2-c^{-2r})P_r,
$$
以及
$$
P_r\Theta_N=\vartheta_r(N)P_r,\qquad
\vartheta_r(N)=\sum_{b\in G_N}t_N(b)b^r\pmod N.
\tag{1181.14}
$$
这些都是模 $N$ 的真实重指标。
特别 $c^2-c^{-2r}=k_{2r}(c)$ 为原同一个平滑单位。

对 (1181.13) 作 Kummer，应用 $P_r$，再用 (1181.7)：
$$
\frac{1}{k_{2r}(c)}
 \sum_{v\in(\mathcal O_K/N)^\times}
 (Nv)^r\kappa_N(\theta_c(P_v))
 =
\frac w4\,\vartheta_r(N)
 \sum_{b\in G_N}b^r\kappa_N(1-\xi_N^b).
\tag{1181.15}
$$
两边再 tensor $\xi_N^{\otimes r}$，就是原 coefficient-map
moment 与原圆单位的比较。全程没有除 $(p+1)p^{n-1}/w$、
$p^{n-1}$ 或 $\varphi(N)$。

## 4. 高层 Euler 因子的有限整计算

本节证明
$$
\boxed{
\vartheta_r(N)\equiv
 (1-\epsilon(p)p^r)L(-r,\epsilon)
 =(1+p^r)L(-r,\epsilon)\pmod N,\qquad r=2,4.}
\tag{1181.16}
$$
所有固定阶 factorial、Bernoulli 多项式和分母均只用至多六，
在 $p>37$ 时是单位。

### 4.1 Gaussian

取唯一的奇数 $a_b\in[1,2N)$、$a_b\equiv b\pmod N$。
四个 lift 中两个非零项的差给
$t_N(b)=\epsilon(a_b)/2$，与 $N\bmod4$ 无关。
因此
$$
2\vartheta_r(N)\equiv
 \sum_{\substack{0\le j<N\\p\nmid2j+1}}
       (-1)^j(2j+1)^r\pmod N.
\tag{1181.17}
$$
先不排除 $p$ 倍。有限生成式
$$
\sum_{j=0}^{N-1}(-1)^j e^{(2j+1)T}
 =\frac{1+e^{2NT}}{2\cosh T}
$$
在 degree 至多四上模 $N$ 化为 $\operatorname{sech}T$。
故全和约化为 Euler 数 $E_r$，$E_2=-1,E_4=5$。

被排除的奇数是 $p(2j+1)$，$0\le j<N/p$；
其符号为 $\epsilon(p)(-1)^j$。
因此被排除和是 $\epsilon(p)p^r E_r$ 模 $N$：
较小层全和的误差为 $O(N/p)$，乘 $p^r$ 后已为 $O(N)$。
$n=1$ 时该乘积本来即被 $p$ 整除，亦成立。
所以
$$
\vartheta_r(N)\equiv
 (1-\epsilon(p)p^r)\frac{E_r}{2}\pmod N.
$$
$\frac{E_2}{2}=-1/2$、$\frac{E_4}{2}=5/2$，
分别是 $L(-2,\chi_{-4})$ 和 $L(-4,\chi_{-4})$，
故得 (1181.16)。

### 4.2 Cubic

先把 (1181.10) 的相同 $t_N(b)$ 定义到
$1\le b<N$ 的全部 residues，暂不排 $p$ 倍。
记全部 weighted 和为 $\vartheta_r^{\rm all}(N)$。

若 $N\equiv-1\pmod3$，三个 $j\epsilon(b+jN)$ 之和
按 $b\bmod3=0,1,2$ 是 $(1,-2,1)$；
若 $N\equiv1\pmod3$，则是 $(-1,-1,2)$。
所有 residues 的 $\sum b^r$ 模 $N$ 为零：
乘一个 $a$ 使 $a^r-1$ 为单位，即由重指标得到。
于是
$$
\vartheta_r^{\rm all}(N)\equiv
\begin{cases}
 \displaystyle\sum_{b\equiv1\ (3)}b^r,&N\equiv-1\pmod3,\\[1mm]
 \displaystyle-\sum_{b\equiv2\ (3)}b^r,&N\equiv1\pmod3 .
\end{cases}
\tag{1181.18}
$$
两行均只取 $1\le b<N$。
用固定 Faulhaber 多项式，在第一行令
$N=3m+2$、$b=1+3j$、$0\le j\le m$，
第二行令 $N=3m+1$、$b=2+3j$、$0\le j<m$，
得到同一个余数
$$
-\frac{2\cdot3^r}{r+1}B_{r+1}(1/3)
 =L(-r,\chi_{-3}).
\tag{1181.19}
$$
具体为 $r=2$ 的 $-2/9$ 与 $r=4$ 的 $2/3$。

对被排除的 $b=pb'$，原三 lift 逐项给
$$
t_N(pb')=\epsilon(p)t_{N/p}(b').
$$
因此其 weighted 和为
$\epsilon(p)p^r\vartheta_r^{\rm all}(N/p)$。
较小层的 (1181.19) 误差是 $O(N/p)$，
乘 $p^r$ 后是 $O(Np^{r-1})$，足以约模 $N$。
这证明 (1181.16)，也保留了 $n$ 奇偶改变 $N\bmod3$ 的情形。

## 5. 返回原全局 Kummer 类：高层 restriction 的单射自证

(1181.15) 乘 $\xi_N^{\otimes r}$ 后，
左侧正是 $(q_J^r)_*\mathsf M_{2r,n}$ 的原全点 trace；
右侧是 $\frac w4\vartheta_r(N)\gamma_{r+1,n}$。
这个 trace 可以先在 $L_N$ 上按各实际点轨道作 norm，
所以 (1181.15) 在 $L_N$ 的 Kummer 群中给出等式，
并非只在一个会杀掉 $p$-torsion 的更大 splitting field 中比较。

还须返回 $\mathbb Q$。因 $K$ 与 $\mathbb Q(\xi_N)$ 的 conductors 互素，
$$
\operatorname{Gal}(L_N/\mathbb Q)
 \simeq C_2\times\Delta\times P_N.
$$
$C_2$ 的阶是单位，$\Delta$ 也有单位阶。
$\Delta$ 在 $C_2\times P_N$ 上的共轭平凡，
在 coefficient $L_{r+1,n}$ 上则按非平凡的
$\omega^{r+1}$ 作用，$r+1=3,5<p-1$。
因此 Hochschild–Serre 给
$$
H^i\bigl(\operatorname{Gal}(L_N/\mathbb Q),L_{r+1,n}\bigr)=0,
\qquad i=1,2.
\tag{1181.20}
$$
确切地，先对 $C_2\times P_N$ 取上同调，再取 $\Delta$ invariants；
后者在每个次数仍按同一非平凡 scalar 作用，故全为零。
于是 inflation–restriction 的 kernel 为零，restriction 在所需 H¹ 单射。
没有以 $[L_N:\mathbb Q]$ 为 $p$ 单位作假设。

因为 $r$ 为偶数，复共轭把 $q_J$ 变号后
$q_J^r$ 不变；两个 coefficient maps 本来就在 $\mathbb Q$ 上。
故 (1181.15)–(1181.16) 返回原全局类，给
$$
(q_J^r)_*\mathsf M_{2r,n}
 =\frac w4(1+p^r)L(-r,\epsilon)\gamma_{r+1,n}.
\tag{1181.21}
$$
代入四个已计算的常数即 (1181.1)。

标准 Gaussian/cubic 模型之外的 rational twists
在 degree 至多四/六的扩域后同构；
这些 degree 对 $p>37$ 可逆。
原 moment、CM map 和 Weil tensor 都与该同构相容，
所以同样由 restriction/corestriction 返回所有所述 twists。
这一步只除四或六，不除高层 $p$-power ray degree。

### 5.1 原十二次矩及真实 $B_{p-7}$ 接口所需的范数

在同一个 R1147 primitive 塔中，$\mathsf M_{12,n}$ 已存在，
辅助数仍选上述 primitive $c$，故
$k_{12}(c)=c^2-c^{-12}$ 对全部 $p>37$ 为单位。
特别不使用可能在 $p=43,127$ 为零的 $k_{12}(2)$。

定义同一全轨道未平均类
$$
\gamma_{7,n}
 =\operatorname{Cor}_{\mathbb Q(\xi_N)/\mathbb Q}
   \bigl(\kappa_N(1-\xi_N)\otimes\xi_N^{\otimes6}\bigr).
$$
在 §§1–5 中取 $r=6$：
$\omega^{-6}$ 仍不是 roots of unity 的 $\omega$，
restriction 的 $\Delta$ 角色为非平凡 $\omega^7$，
所有平滑与半因子依旧为单位。
新的有限多项式只用到 degree 七、阶乘至多八，
所以 §4 的模 $N$ 计算与排除 $p$ 倍的误差界仍完整成立。

Gaussian 中 $E_6=-61$，故
$L(-6,\chi_{-4})=-61/2$。
cubic 中
$$
B_7(x)=x^7-\frac72x^6+\frac72x^5-\frac76x^3+\frac16x,
\qquad B_7(1/3)=\frac{49}{2187},
$$
所以
$$
L(-6,\chi_{-3})
 =-\frac{2\cdot3^6}{7}B_7(1/3)=-\frac{14}{3}.
$$
乘原 $w/4$ 后分别为 $-61/2$ 与 $-7$，
再保 (1181.16) 的 $1+p^6$，即 (1181.1a)。

Gaussian 的唯一可能新分子素数 $61$ 满足 $61\equiv1\pmod4$，
不在这里的惰性范围；cubic 的七也不在 $p>37$。
因此这两个真实原类的 Tate projection 在局部为零，
分别等价于同一个 $\gamma_{7,n}$ 的局部类为零。
这为原十二次矩的实际中槽提供同源输入，
不把一个别的 off-middle 槽改名为中槽，
也不新增原 actual-good mask 中没有出现的观测。

## 6. CM 端点上真正存在的整 Cartan map

选择原 $\delta$ 的整提升 $\widehat\delta$。
在 Gaussian 情形令
$$
I_\infty=u[i],\qquad u^2=-\widehat\delta;
$$
在 cubic 情形令
$$
I_\infty=u(2[\zeta_3]+1),\qquad
u^2=-\widehat\delta/3.
$$
惰性条件使相应右边为 $\mathbb Z_p$ 单位平方；
选定模 $p$ 的原两个号之一后，Hensel 引理给唯一相容的 $u$。
这里使用真实 CM endomorphism 作 $\mathbb Z_p$-线性组合，
故它实际作用于整个 $T_pE$。
$I_\infty^2=\widehat\delta$，复共轭将其变为 $-I_\infty$；
全部 $q_{I_\infty}^{2j}$ 真正定义在 $\mathbb Q$ 上。

原 43 维 primitive 塔的 bilinear map 是
$$
\mathfrak b_\infty(v,v')
 =
\bigl(\Pi_0(x,y'),\Pi_2(x,y'),
 \Pi_4(x,y')+\lambda_\infty x t'\bigr),\qquad
\lambda_\infty=\frac{21}{11}(1+p^4).
$$
沿同一个 $I_\infty$，准确的高层群同态为
$$
\begin{aligned}
a&=\frac12q_I^2x,\\
b&=\frac12q_I^4y+\frac{8\widehat\delta^2}{11}(1+p^4)t,\\
h&=\frac14q_I^6z_0-\frac{4\widehat\delta}{11}q_I^4z_2
                   +\frac{4\widehat\delta^2}{21}q_I^2z_4 .
\end{aligned}
\tag{1181.22}
$$
原完整 polar identity 是具有 $p$-单位分母的多项式恒等式，
所以同样在 $\mathbb Z_p$ 上成立：
前三项给 $(q_I^2x)(q_I^4y')/4$，
最后一项给
$$
\frac{4\widehat\delta^2}{21}\lambda_\infty q_I^2x\,t'
 =
\frac12q_I^2x\cdot
   \frac{8\widehat\delta^2}{11}(1+p^4)t'.
$$
因此 $h(\mathfrak b_\infty(v,v'))=a(v)b(v')$，
(1181.22) 保完整 ordered 群律。
若把第二槽的 $1+p^4$ 丢掉，这个群同态在高层将不成立。

应用 (1181.1)：
Gaussian 的 $q_I^2=u^2q_{[i]}^2$、$q_I^4=u^4q_{[i]}^4$，
cubic 的 $q_I=2u q_{[\zeta_3]}$。
连同 (1181.22) 的两个半因子和真实 Tate 修正，立即得到
$$
a=x_{E,\infty}\gamma_{3,\infty},\qquad
b=y_{E,\infty}\gamma_{5,\infty}
\tag{1181.23}
$$
及 (1181.3) 的四个系数。
它们是 $\mathbb Z_p$ 单位；$87=3\cdot29$、
$160=2^5\cdot5$ 的素因子均不在本范围。

这是在两个实际 CM 端点定义的 compatible pushout。
$\widehat\delta$ 及所选 CM map 在本节明确指定；
没有由原 mod-$p$ 标签凭空得到整个 level-$p$ 曲线上的
$T_pE$ Cartan，也没有在非 CM family 上声称存在同一 map。

## 7. 全 S₀ 上的唯一 Heisenberg 塔与坏约化位

令 $\mathcal H_n$ 为 $R_n(3),R_n(5),R_n(8)$ 的 ordered Heisenberg 群。
R1146 的
$H^1(S_0,L_{8,1})=H^2(S_0,L_{8,1})=0$
沿 coefficient 短正合列逐 $n$ 给
$$
H^1(S_0,L_{8,n})=H^2(S_0,L_{8,n})=0.
\tag{1181.24}
$$
同样 $H^0(S_0,L_{3,n}\oplus L_{5,n})=H^0(S_0,L_{8,n})=0$。
所以每个原兼容 pair $(\gamma_{3,n},\gamma_{5,n})$
有唯一到唯一同构的 global lift $\Theta_n$。
Kummer norm 的实际相容箭头见 R1147 §8；
对权二的 $\gamma_3$ 使用同一个 norm/projection formula。
唯一性使 $\Theta_n$ 的约化同构也相容，得到 $\Theta_\infty$。

将原 universal $\mathscr P_\infty$ 拉到 rational CM 曲线，
再用 (1181.22) pushout，先得到 $G_{\mathbb Q}$ 上的真实
$\mathbb Z_p$ Heisenberg cocycle。
还须证明它在所有 $\ell\ne p$ 无分歧：
不能仅因第一层 proper 就宣布高层同样 proper。

由 (1181.23)，它的两个 abelian classes 都是
$\mathbb Z_p$-圆单位类，故在这些 $\ell$ 无分歧。
由于 $p$-adic Tate coefficients 在 $I_\ell$ 上平凡，
inertial restriction 的 abelian cocycle 事实上为零，
从而整个 inertial image 位于中心 $\mathbb Z_p(8)$。
wild inertia 是 pro-$\ell$ 群，对这个 pro-$p$ 中心没有非零像。
tame inertia 的可能 map 为
$$
\mathbb Z_p(1)\longrightarrow\mathbb Z_p(8).
$$
arithmetic Frobenius 的 equivariance 给
$$
(\ell^8-\ell)\,c(\tau)=0.
$$
虽然 $\ell^7-1$ 可能被 $p$ 整除，它在 $\mathbb Z_p$ 中不是零，
而中心是无挠 $\mathbb Z_p$ 模，所以 $c(\tau)=0$。
内共轭不会改变中央元素，故没有额外 Heisenberg cross term。

因此整个 compatible CM pushout 在全部 $\ell\ne p$
无分歧，包括 $\ell=2,3$ 的坏 elliptic reduction 位，
并给 $S_0$ 上的真实 pro-finite étale torsor。
本段特意在完整无挠塔中证明；不能把该论证截成有限
$R_n$ 后再反除可能非单位的 $\ell^7-1$。

它的 abelian quotient 是 (1181.23)。
由 (1181.24) 的全局唯一性，逐层得
$$
\mathscr P_{E,n}
 =[x_{E,\infty}\bmod p^n,\,
   y_{E,\infty}\bmod p^n]_*\Theta_n.
\tag{1181.25}
$$
兼容后即 (1181.2)。没有使用全局 $H^1(S_0,L_3)$ 或
$H^1(S_0,L_5)$ 的秩一生成性，也没有 $C_{\rm cyc}$ 门。

## 8. 全精度端点、原最低中央槽与精确边界

在 $p$-good CM 模型上，原 43 维 fibre 的整 crystalline/FL
实现由 R1147、R1150–R1166 给出。
(1181.22) 来自真实 CM 自同态和原 Weil tensor，
因此是相同整 tensor category 中的群同态。
它沿唯一 Hodge 截面及正向 Frobenius 自然，
所以 (1181.25) 在每个精度给出 (1181.4)。

这也给 $\Theta_\infty$ 的 crystalline 实现：
(1181.3) 的两个系数是单位，可从 good CM fibre
作逆 scaling 取得，而非另假设一个未付的 integral lift。
本篇的 $r_\infty,s_\infty,z_\infty$ 指这个同一全局圆单位
Heisenberg 对象的实际整读数，不另选三组常数。
R1177 的 $S\mapsto-A_\Phi$ 字典若用于实际 syntomic 读取，仍须保留；
这里由 class-level map 直接得出的 scaling 没有另一次符号翻转。

对于原 primitive 的三个 ordered 中央槽，
(1181.22) 给全部精度的等式
$$
q_I^2 Z_4
 =
\frac{21}{4\widehat\delta^2}
 \left(x_{E,\infty}y_{E,\infty}z_\infty
       -\frac14q_I^6Z_0+\frac{4\widehat\delta}{11}q_I^4Z_2\right).
\tag{1181.26}
$$
cubic 的 $\mu_6$-不变 $\operatorname{Sym}^4$ 整空间仅为
$\omega^2\eta^2$ 一条直线，且其 polarization 系数六为单位；
因此 (1181.26) 在该端点确定整个 $Z_4$。
Gaussian 仍只确定 middle Tate 投影，不删两条外侧不变线。
若使用 BCH 坐标，先保原二次补项回到 ordered 坐标。

本篇没有数值执行 $z_\infty$ 的全部 $p$-adic 位。
它证明的是两个 CM 端点与同一个原全局圆单位 Heisenberg 塔
之间的精确整比例，并给每个 $p^n$ 的实际类等式。
若从 R1175–R1176 的有限算法取得参考 fibre，
或者独立读取该原圆单位塔，必须用这些比例和原群同态相互运输。

### 8.1 与已付 all-vector 比例的独立相容核验

R1147 (1147.60) 已证明
$\mathsf M_{d,n}=(1-p^d)\widetilde{\mathsf M}_{d,n}$。
所以 (1181.1) 的两个 primitive 因子分别化为
$$
\frac{1+p^2}{1-p^4}=\frac1{1-p^2},\qquad
\frac{1+p^4}{1-p^8}=\frac1{1-p^4}
$$
用于相同 all-vector moment。
同时原 all-vector Tate 输入是
$\widetilde\gamma_5=(1-p^4)^{-1}\gamma_5$，
其 bilinear 系数是 $21/11$。
故 all-vector 的 CM 两标签分别为
$x_{E,0}/(1-p^2)$、$y_{E,0}/(1-p^4)$，
其中 $x_{E,0},y_{E,0}$ 指 (1181.3) 去掉 Euler 因子的整常数。
这与 R1147 (1147.63) 的完整群尺度相同，
不是只比较其 associated graded。
若比较实际根代表，仍携带 R1147 (1147.64)–(1147.65) 的原 gauge；
本篇的 cohomology 比例不把该 gauge 设为零。

### 8.2 尚未改变的主目标量词

实际非 CM 曲线仍只有原模 $p$ Cartan label；
本篇没有将其任意提升成 $T_pE$ endomorphism。
因此不能从这些 CM 端点的全精度公式，
推出邻近整个深盘只剩 CM 点。
原 actual good-mask 联合分离、全局中央减法的非零、
有限标签以外的高阶排点和完整一般 $p$ 目标继续沿 open.md。

## 来源与准确依赖

- [R1178](R1178-original-cubic-CM-norm-and-global-CM-endpoints.md)、
  [R1179](R1179-original-Gaussian-CM-norm-and-middle-Tate-moments.md)：
  原 theta 规范、CM 标签方向、shifted Epstein 的符号、
  全圆单位对数因子四及第一层四个类。
  本篇新增高层整群环比较、非单位 ray degree 的处理与 Euler 因子。
- M. Flach, *Iwasawa Theory and Motivic L-functions*,
  **Pure and Applied Mathematics Quarterly 5 (2009), 255–294**，
  [正式 PDF](https://intlpress.com/site/pub/files/_fulltext/journals/pamq/2009/0005/0001/PAMQ-2009-0005-0001-a008.pdf)，
  [作者机构书目](https://resolver.caltech.edu/CaltechAUTHORS:FLApamq09)，
  [同作者全文镜像](https://studylib.net/doc/7931909/iwasawa-theory-and-motivic-l-functions---mathematics)。
  §2.2.2 Lemma 2.1 与 §2.2.3 Lemma 2.2(a)–(c)、
  后续 Remark：一般 conductor 下实际 theta 的 rationality、
  integrality、CM reciprocity 及格标签。
  所需全字符与整单位格推理在本篇 §§2–3 给出。
- [R1147](R1147-original-canonical-moment-Heisenberg-lift.md)
  §§8–11、17–18：同根 primitive 塔、圆单位兼容箭头、
  $\lambda_\infty$、唯一 universal lift、
  all-vector 比例及有序根 gauge。
- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md)
  §§4–5：原 $S_0$ 中心 H¹/H² 消失。
  高层 coefficient 归纳及坏位无分歧在本篇 §7 自证。
- [R1177](R1177-original-syntomic-to-Frobenius-sign-dictionary.md)：
  同一正 Kummer/左扭曲/正向 Frobenius 的坐标字典。

全篇纸面证明；没有数学程序执行，也没有以小素数拟合高层因子。
