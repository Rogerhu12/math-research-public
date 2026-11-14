# R107：实际四次迹的奇偶约束与变化判别式的平方级增长

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的全局必要条件。** 本文在 R100/R104 的实际分支中，把同一条曲线的模 $p$ 迹、真实二除 Frobenius 与有限四次差特征同时使用。随后用两个普通 Dirichlet 特征的 Burgess 界，证明四阶惯性支撑乘积必须满足 $Q\gg_\epsilon p^{2-\epsilon}$。这里的常数有效，只依赖 $\epsilon$；没有 GRH、变化二次域的 Siegel 常数或未核准的 Hecke Burgess 输入。这个下界仍不限制 $Q$ 向上增长，因而不是 Serre 一致性的完成证明。

## 1. 设置及主要结论

保持 R100/R104 的实际条件：
$$
\begin{gathered}
E/\mathbb Q,\quad \rho_{E,p}(G_{\mathbb Q})=N_{\rm ns}(p),\quad
K=\mathbb Q(\sqrt{-3}),\quad p>37,\quad p\equiv11\pmod{12},\\
\rho_{E,p}(I_p)=C^3,\quad c(\eta)\in\{6,9\},\quad
j(E)\in\mathbb Z,\quad j(E)\ne0.
\end{gathered}                                                   \tag{107.1}
$$
令
$$
A:y^2=x^3+1,\qquad \beta=\lambda_E/\lambda_A.
$$
R100 给同一全局特征的两个等式
$$
\beta^{12}=1,\qquad \beta^6=\chi_\Delta|_{G_K}.             \tag{107.2}
$$
按 R104 记
$$
F=\mathbb Q(\sqrt\Delta),\quad
\mathcal S=\{q\ge5:q\ne p,\ e_q(E)=4\},\quad
Q=\prod_{q\in\mathcal S}q,
$$
以及
$$
d=\prod_{q\in\mathcal S}q^*,\quad
q^*=(-1)^{(q-1)/2}q,\quad D_F=-3d.
                                                               \tag{107.3}
$$
每个 $q\in\mathcal S$ 为 $1$ 或 $11$ 模 $12$，故 $d$ 是带符号的奇基本判别式，$|d|=Q$，且 $d\equiv1\pmod3$。

**定理 107.1（同一实际迹的必要条件）。** 设有理素数 $q\ge5$、$q\ne p$ 在 $K$ 分裂，在 $F$ 惰性。令
$$\pi_A=u+v\sqrt{-3},\quad u,v\in\mathbb Z,\quad
q=u^2+3v^2$$
为参考曲线 $A$ 的一个 Frobenius 根。固定一个 $s_p\in\mathbb F_p$，满足 $s_p^2=3$。则存在**同一个实际好约化二次扭曲的整数迹** $a$ 及一个整数
$$m\in\{\pm2v,\ \pm(u+v),\ \pm(u-v)\},$$
满足
$$
\boxed{
a\in2\mathbb Z,\quad |a|\le2\sqrt q,\quad
a\equiv s_pm\pmod p,\quad
0<|a^2-3m^2|<4q.
}                                                             \tag{107.4}
$$
其中 $p\mid a^2-3m^2$。所以必有
$$\boxed{q>p/4.}                                               \tag{107.5}$$
若实际所选的 $m$ 为偶数，则更有
$$\boxed{q>p.}                                                 \tag{107.6}$$
这里不允许把任意四次根、任意整数迹和不同 Frobenius 提升分别选择后拼合。第 2–4 节从同一个好约化扭曲推出所有条件，并说明如何用原三次角色保留相位。

**定理 107.2（全局支撑增长）。** 若 $\mathcal S\ne\varnothing$，则对任意 $\epsilon>0$，存在有效常数 $c_\epsilon>0$，只依赖 $\epsilon$，使
$$
\boxed{Q\ge c_\epsilon p^{\,2-\epsilon},
\qquad |D_F|\ge3c_\epsilon p^{\,2-\epsilon}.}              \tag{107.7}
$$
等价地，对任意 $\delta>0$，
$$\boxed{p\ll_\delta Q^{\,1/2+\delta}}                     \tag{107.8}$$
且隐含常数有效。R104 规范化后的同 $j$ 全局二次扭曲还满足
$$\boxed{N_{E'}\gg_\epsilon p^{\,6-\epsilon}}.             \tag{107.9}$$

R98 已证明剩余 $p=47,59,83$ 的非 CM 分支必有 $\mathcal S\ne\varnothing$；定理 107.2 对满足上述前提的其他层也成立，但不替这些其他层补上整 $j$ 或非空支集前提。

## 2. 从真实局部曲线得到一个偶数好约化迹

### 2.1 为什么测试素数确实能用好二次扭曲

设 $q$ 满足定理 107.1。因 $j\in\mathbb Z$，$E$ 在 $q$ 潜在好约化。R104 的实际惯性阶清单为
$$e_q\in\{1,2,4\}.$$
但 $q$ 在 $F$ 惰性，特别不分歧；阶四恰使 $F$ 分歧，故这里
$$e_q\in\{1,2\}.$$
阶二惯性为标量 $-I$。在奇局部域 $\mathbb Q_q$ 上，非平凡二次惯性角色可延为分歧二次字符；用它扭曲，或在阶一时不扭曲，得到 $\mathbb Q_q$ 上的好约化曲线 $E_q$。Néron–Ogg–Shafarevich 给好约化，且二次扭曲不改变 $E[2]$。

在 Cartan 特征中，此扭曲只把 $\beta$ 乘一个二次特征，所以 $\beta^4$、$\beta^6$ 与 $\beta^{12}$ 不变。下面始终取这个 $E_q$ 的同一个 Frobenius 根和同一个整数迹
$$a=a_q(E_q),\qquad |a|\le2\sqrt q.$$

这一步不适用于 $q\in\mathcal S$，因为那里是四阶惯性；定理已通过“$q$ 在 $F$ 惰性”排除了该支撑。$q=2,3,p$ 也不在定理使用范围。

### 2.2 二除 Frobenius 迫整数迹为偶数

$E_q$ 好约化且 $q$ 为奇数，故二除表示不分歧。其 Frobenius 在 $S_3$ 二次商中的符号为 $\chi_F(q)=-1$，所以在三个非零二挠点上是一个换位。

因此 $E_q(\mathbb F_q)$ 恰有一个非零有理二挠点；特别其阶为偶数。由
$$\#E_q(\mathbb F_q)=q+1-a$$
以及 $q+1$ 为偶数，得到
$$\boxed{a\in2\mathbb Z.}                                 \tag{107.10}$$
这里使用实际二除域，不能用模 $p$ 迹恰有某个偶数代表代替。

## 3. 十二次单位根与真正的 CM Frobenius 根

### 3.1 参考根的整数坐标

$q$ 在 $K$ 分裂，且 $q\ge5$，故 $A$ 在 $q$ 好普通约化；其 CM Frobenius 根在 $\mathcal O_K$，范数为 $q$。$A$ 的点 $(-1,0)$ 是有理二挠点，所以 $a_q(A)$ 为偶数。

若先写 $\pi_A=(a+b\sqrt{-3})/2$，$a,b$ 同奇偶，则 $a=a_q(A)$ 偶迫 $b$ 也偶。于是确有
$$\pi_A=u+v\sqrt{-3},\quad u,v\in\mathbb Z,\quad
u^2+3v^2=q.$$
选择共轭根只改变 $v$ 的符号。$u,v$ 均非零，且 $u\ne\pm v$：否则素数 $q\ge5$ 会是平方、三倍平方或四倍平方。

### 3.2 在同一个剩余嵌入下提升差特征

因 $p\equiv11\pmod{12}$，$p$ 在 $K$ 惰性，并在 $\mathbb Q(\sqrt3)$ 分裂。选择与 $\lambda_A$ 的取向一致的剩余嵌入
$$\mathcal O_{K(i)}\longrightarrow\mathbb F_{p^2}.$$
这个嵌入也固定了 $\sqrt3$ 的某一剩余根 $s_p\in\mathbb F_p$。$\mu_{12}$ 的约化是单射，且 $p$ 次幂作用等于复共轭。

$E_q$ 的实际 Frobenius 特征值等于
$$\beta_q(\operatorname{Frob}_q)\,\lambda_A(\operatorname{Frob}_q).$$
由 (107.2) 和 $F$ 惰性，第一因子是唯一某个 $\zeta\in\mu_{12}$ 的约化，满足
$$\zeta^6=-1.$$
因此，在同一个剩余嵌入下，实际整数迹满足
$$
a\equiv\zeta\pi_A+\zeta^{-1}\bar\pi_A\pmod p.             \tag{107.11}
$$
$\zeta$ 的六种可能值给
$$
\zeta\pi_A+\zeta^{-1}\bar\pi_A
\in\sqrt3\,\{\pm2v,\ \pm(u+v),\ \pm(u-v)\}.               \tag{107.12}
$$
例如 $\zeta=i$ 给 $-2v\sqrt3$，$\zeta=e^{\pi i/6}$ 给 $(u-v)\sqrt3$。余下值由共轭和取负得到。

局部二次扭曲只把 $\zeta$ 改为 $-\zeta$；它同时改变右侧符号，而二除表示和偶性不变。交换 $K$ 的取向或 $\sqrt3$ 的剩余根也只置换列出的同一集合。因此 (107.4) 不遗漏任何实际取向，且每次使用的是同一个实际 $a$。

### 3.3 不把三次相位擅自独立选择

若需更精确的必要集合，可以保留原三次角色。令
$$T=p^2-1,\quad U=T/3,\quad V=U^{-1}\pmod3,$$
并按 R97 选择
$$e\equiv4-UV\pmod T,\qquad e\in\{4,4+U,4+2U\}.$$
设测试素理想 $(\alpha)$ 与角色导子互素，且 $\pi_A$ 选为该取向的参考根，则 R97 给
$$
\beta^4(\operatorname{Frob}_{(\alpha)})
=\frac{\alpha^e\,\eta((\alpha))^V}{\pi_A^4}
\quad\text{在 }\mathbb F_{p^2}^\times\text{ 中}.           \tag{107.13}
$$
因此只应保留 (107.12) 中其对应 $\zeta$ 同时满足
$$\zeta^4=\beta^4(\operatorname{Frob}_{(\alpha)})$$
的项。$\eta$ 是一个固定的全局特征，不得在不同测试素数各自翻转。

定理 107.1 为了得到无须逐点求 $\eta$ 的全层结论，使用六项的更大必要集合。这是有意放宽，没有把六项分别可实现当成充分条件。

## 4. 两个严格窗口及一个实际共同实现反证

所有候选 $m$ 均非零。又 $\zeta\pi_A$ 的复绝对值为 $\sqrt q$，故
$$3m^2\le4q.$$
事实上等号要求范数为素数 $q\ge5$ 的 $\pi_A$ 落在固定实射线上，会迫 $q$ 为平方或三倍平方，故等号不成立；也可直接用
$$
4q-12v^2=4u^2>0,\quad
4q-3(u\pm v)^2=(u\mp3v)^2>0.
$$
最后一个平方不为零，因为 $u=\pm3v$ 会给 $q=12v^2$。

同样 $a^2\le4q$，且 $a^2=4q$ 不可能。于是
$$|a^2-3m^2|<4q.$$
若它等于零，整数平方比为三；这只能有 $a=m=0$，已被 $m\ne0$ 排除。因此它是一个非零的 $p$ 倍数。$q\le p/4$ 时会有
$$0<|a^2-3m^2|<4q\le p,$$
矛盾，证明 (107.5)。

若实际 $m$ 偶，则 $a$ 也偶，故差还被四整除。因 $p$ 奇，它是非零的 $4p$ 倍数。若 $q\le p$，又有
$$0<|a^2-3m^2|<4q\le4p,$$
矛盾，证明 (107.6)。

**例 107.3。** R104 §9 的抽象域
$$p=47,\qquad F=\mathbb Q(\sqrt{-111})$$
通过所列原始环类导子和 $D_4$ 范数条件，但不能来自本题实际曲线。

取 $q=13$。它在 $K$ 分裂，而
$$(-111/13)=(6/13)=-1,$$
所以在 $F$ 惰性。写
$$13=1^2+3\cdot2^2,\qquad m\in\{\pm4,\pm3,\pm1\}.$$
模 $47$ 可取 $\sqrt3=12$，相应迹剩余类为
$$\{\pm1,\pm11,\pm12\}.$$
Hasse 窗口为 $|a|\le2\sqrt{13}<8$，其中只有 $\pm1$，都是奇数。这与 (107.10) 矛盾。

这不否定 R104 的抽象例子；它准确展示“两个抽象域都存在”与“它们和模 $p$ 表示由同一条椭圆曲线实现”之间的额外限制。这里只排除此指定域，不能把一个例子的排除推广到全部变化域。

## 5. 固定 $K$ 上的二次特征及两个 Dirichlet 因子

以下给定理 107.2 的解析部分，完整保留 $Q$ 的依赖。假设 $Q>1$，所以 $F\ne K$。

令 $\psi$ 是二次扩张 $KF/K$ 的原始二次 Hecke 特征。它可写成有理二次 idèle 特征 $\chi_{D_F}$ 经范数的拉回，但在分歧取消处必须使用这个**原始** Hecke 特征，不能机械写成对所有理想的 $\chi_{D_F}(N\mathfrak a)$。

具体地：

- 对 $q\mid Q$，$KF/K$ 在其上方所有素理想处分歧，准确导子指数为一；
- 在三处，$F_3=K_3$，扩张已经分裂，故 $\psi$ 在三上方的素理想取一；
- 若 $q\nmid3Q$ 在 $K$ 惰性，则唯一素理想 $(q)$ 的范数为 $q^2$，其 $\psi$ 值为一；
- 若 $q\nmid3Q$ 在 $K$ 分裂，则每个范数为 $q$ 的素理想取值 $\chi_{D_F}(q)$。

二处也在惰性一行中，取值一。故
$$\mathfrak f(\psi)=Q\mathcal O_K,$$
并且任何 $\psi$ 值为负一的素理想，必在某个
$$q\ge5,\quad q\ne p,\quad
(q/K)=\mathrm{split},\quad(q/F)=\mathrm{inert}             \tag{107.14}
$$
之上，范数就是 $q$。这里自动排除了 $p$，因为 $p$ 在 $K$ 惰性。

双二次扩张的 Artin 表示分解或逐个 Euler 因子给
$$
\boxed{L_K(s,\psi)=L(s,\chi_{D_F})\,L(s,\chi_d).}          \tag{107.15}
$$
两个右侧特征均非主、原始；其导子分别为 $3Q$、$Q$，都是平方自由数。特别三处的右侧因子为 $(1-3^{-s})^{-1}$，与左侧原始特征取值一一致。

令
$$
S(X)=\sum_{N\mathfrak a\le X}\psi(\mathfrak a),
$$
并把与导子不互素的理想之值置零。由 (107.15)，
$$
S(X)=\sum_{ab\le X}\chi_{D_F}(a)\chi_d(b).                \tag{107.16}
$$

## 6. 双曲线公式与普通 Burgess 界

### 6.1 唯一外部解析输入

使用已发表的普通 Dirichlet Burgess 估计：对任意整数 $r\ge2$、$\varepsilon_B>0$，平方自由导子 $M$ 的原始非主特征满足
$$
\left|\sum_{n\le Y}\chi(n)\right|
\ll_{r,\varepsilon_B}
Y^{1-1/r}M^{(r+1)/(4r^2)+\varepsilon_B}.                 \tag{107.17}
$$
常数有效。其一般立方自由版本见 Burgess 原文及 Heath-Brown 已发表论文的式 (1)；本文只用平方自由的 $M=Q,3Q$。若 $Y>M$，用完整周期的和为零及剩余区间即可延伸同一上界。没有使用变化数域上的另一条 Burgess 定理。

### 6.2 严格的双曲线上界

置 $Y=\lfloor\sqrt X\rfloor$，$C_i(t)=\sum_{n\le t}\chi_i(n)$，其中
$\chi_1=\chi_{D_F}$、$\chi_2=\chi_d$。精确双曲线公式为
$$
S(X)=\sum_{a\le Y}\chi_1(a)C_2(X/a)
+\sum_{b\le Y}\chi_2(b)C_1(X/b)-C_1(Y)C_2(Y).
$$
第一项的绝对值至多
$$
\ll X^{1-1/r}Q^{(r+1)/(4r^2)+\varepsilon_B}
\sum_{a\le Y}a^{-1+1/r}
\ll_r X^{1-1/(2r)}Q^{(r+1)/(4r^2)+\varepsilon_B}.
$$
第二项同样。最后一项对一个因子用 (107.17)，另一个用平凡上界 $Y$，仍是同一量级。因此
$$
\boxed{
|S(X)|\ll_{r,\varepsilon_B}
X^{1-1/(2r)}Q^{(r+1)/(4r^2)+\varepsilon_B}.
}                                                            \tag{107.18}
$$

### 6.3 与导子互素的理想计数：主项不会丢失

记
$$A_Q(X)=\#\{\mathfrak a\subset\mathcal O_K:
N\mathfrak a\le X,\ (\mathfrak a,Q)=1\}.$$
固定域 $K=\mathbb Q(\sqrt{-3})$ 类数一，有六个单位；其整数环是平面六角格。数范数圆盘中的格点再除以六，直接得到
$$
A_1(X)=\kappa X+O(\sqrt X+1),\qquad
\kappa=\frac{\pi}{3\sqrt3}.                              \tag{107.19}
$$
令 $\mathfrak R$ 为 $Q\mathcal O_K$ 的平方自由根理想。对其约数作 Möbius 反演：
$$
A_Q(X)=\sum_{\mathfrak b\mid\mathfrak R}
\mu(\mathfrak b)A_1(X/N\mathfrak b).
$$
这给
$$
A_Q(X)=\kappa_Q X+
O\!\left(
\sqrt X\prod_{\mathfrak q\mid Q}(1+N\mathfrak q^{-1/2})
+2^{\omega(\mathfrak R)}
\right),                                                 \tag{107.20}
$$
其中
$$\kappa_Q=\kappa\prod_{\mathfrak q\mid Q}(1-N\mathfrak q^{-1}).$$
即使 $N\mathfrak b>X$，(107.19) 的 $+1$ 也控制这项，所以没有遗漏长约数。

对任意 $\eta>0$，有效的初等素因子估计给
$$
\kappa_Q\gg_\eta Q^{-\eta},\qquad
\prod_{\mathfrak q\mid Q}(1+N\mathfrak q^{-1/2})
+2^{\omega(\mathfrak R)}\ll_\eta Q^\eta.                  \tag{107.21}
$$
例如对足够大的有理素数 $q$，分别用
$(1-1/q)^2\ge q^{-\eta}$、
$(1+q^{-1/2})^2\le q^\eta$、$4\le q^\eta$；有限个较小素数贡献一个明确可计算常数。这里固定 $\eta$ 后阈值和常数均有效，不是 Siegel 下界。

于是
$$
\boxed{
A_Q(X)=\kappa_QX+O_\eta\bigl(Q^\eta(\sqrt X+1)\bigr),
\quad \kappa_Q\gg_\eta Q^{-\eta}.
}                                                            \tag{107.22}
$$

### 6.4 必有一个小的负特征素理想

先取 $0<\delta\le1/4$，置
$$
r=\lceil1/\delta\rceil,\quad
\eta=\varepsilon_B=\frac{\delta}{16r},\quad
X=CQ^{1/2+\delta},
$$
其中 $C\ge1$ 稍后有效选择。因为 $1/r\le\delta$，(107.18) 给
$$
\frac{|S(X)|}{X}
\le B_\delta C^{-1/(2r)}
Q^{-(1/2+\delta)/(2r)+(r+1)/(4r^2)+\eta}
\le B_\delta C^{-1/(2r)}Q^{-3\eta}.                       \tag{107.23}
$$
取 (107.22) 中的有效常数 $c_\delta,A_\delta>0$，使
$$\kappa_Q\ge c_\delta Q^{-\eta},\qquad
|A_Q(X)-\kappa_QX|\le A_\delta Q^\eta(\sqrt X+1).$$
由 $2\eta<1/4+\delta/2$ 及 $Q\ge1$，误差除以 $X$ 至多
$$
A_\delta(C^{-1/2}+C^{-1})Q^{-\eta}.
$$
故只要有效选择
$$
C\ge\max\left\{1,
(8A_\delta/c_\delta)^2,
(4B_\delta/c_\delta)^{2r}\right\},
$$
对所有 $Q>1$ 都同时有
$$A_Q(X)\ge\tfrac34c_\delta XQ^{-\eta},\qquad
|S(X)|\le\tfrac14c_\delta XQ^{-\eta}.$$

如果所有范数不超过 $X$、与导子互素的素理想均有 $\psi=1$，那么这些理想的所有乘积也取一，故
$$S(X)=A_Q(X).$$
这与上述两个界矛盾。因此对所有 $Q>1$，存在负特征素理想
$$N\mathfrak q\le CQ^{1/2+\delta}.$$
其下方有理素数满足 (107.14)，且 $q=N\mathfrak q$，即
$$
\boxed{
\text{存在满足 (107.14) 的 }q\ll_\delta Q^{1/2+\delta}.
}                                                            \tag{107.24}
$$
任意更大 $\delta$ 的结论随之成立。统一常数在上面直接选出，不需要用一个未定量的密度结论填补小 $Q$。这个证明也避免了“一个指定有理算术级数里的非剩余整数必有同级数的非剩余素因子”的错误：我们先得到 $K$ 的负特征素理想，而 $K$ 惰性素理想的特征恒为一，故它必是需要的次数一素理想。

## 7. 应用于同一实际曲线的全局结论

(107.24) 给一个在 $K$ 分裂、在 $F$ 惰性的真实好二次扭曲测试素数。定理 107.1 对它给 $p<4q$，所以
$$p\ll_\delta Q^{1/2+\delta},$$
即 (107.8)。

给定 $0<\epsilon<2$，取
$$\delta=\frac{\epsilon}{2(2-\epsilon)}$$
并整理指数：
$$\frac1{1/2+\delta}=2-\epsilon.$$
得到有效的 (107.7)；$\epsilon\ge2$ 时可直接减小 $\epsilon$ 后取弱化结论。

R104 给
$$N_{E'}=12p^2D_F^2\ (c=6),\qquad
N_{E'}=27p^2D_F^2\ (c=9).$$
对 (107.7) 使用 $\epsilon/2$，即得 (107.9)。

这些常数与 $E,p,F$、新四阶素数的个数以及 $c\in\{6,9\}$ 无关。证明只让固定的 $\epsilon$ 控制 Burgess 参数与有限小素数常数。它是变化域的统一**下界**，并不提供所需的统一上界。

## 8. 来源与未闭合接口

- [R100](R100-quartic-shadow-and-dyadic-inertia-exclusion.md)：全局 $\beta^{12}=1$、$\beta^6=\chi_\Delta|_{G_K}$；参考曲线及取向。
- [R104](R104-variable-discriminant-field-and-actual-cubic-conductor.md)：准确 $D_F$ 支集、实际二除域、$p$ 惰性、全局规范化导子。
- [R97](R97-level41-class-three-exclusion-by-certified-thue-equations.md) §2：保留原三次角色的 $\lambda_E^4$ 主理想公式；本文 (107.13) 没有删掉这个有限三次因子。
- D. A. Burgess，*On character sums and $L$-series, II*，Proceedings of the London Mathematical Society (3) **13** (1963), 524–536，[原刊 DOI](https://doi.org/10.1112/plms/s3-13.1.524)。
- D. R. Heath-Brown，*Burgess’s Bounds for Character Sums*，in *Number Theory and Related Fields*, Springer Proceedings in Mathematics & Statistics **43** (2013), 199–213，[正式篇章](https://doi.org/10.1007/978-1-4614-6642-0_10)，[作者 v2](https://arxiv.org/pdf/1203.5219v2)，§1 式 (1)（作者稿 p.1；正式 p.199）明确给原始特征、立方自由模数任意 $r\ge2$ 的量词；其后主定理的 $J=1$ 也恢复同一估计。本文仅用该已发表的 Dirichlet 结论。

本结果没有把模 $p$ 上可选的六个数提升为特征零有理 CM 迹，也没有把有界次数检测域改写成统一小素数界。实际变化域越大，(107.24) 允许的检测素数也越大；这正是仍然存在的全局缺口。继续推进需同时使用原始三次层的全局类、三次相位 (107.13)、整 $j$ 模型和同一条曲线的全部 Frobenius 数据。

