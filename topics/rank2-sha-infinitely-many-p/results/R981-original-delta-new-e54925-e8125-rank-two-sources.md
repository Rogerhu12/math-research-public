# R981 — 原 δ-new 两条质量零线的 E54925、E8125 真秩二来源

日期：2026-11-26 UTC。**已证明：R976 原66维谱的 $(3,5)$、$(5,3)$ 两个质量零一维块，分别来自固定曲线 $E_{54925}:y^2=x^3+54925$ 与 $E_{8125}:y^2=x^3+8125$；两曲线均有无条件秩至少二。** 本篇从原 $W_2\otimes W_3\otimes W_5\otimes W_{13}$ 及全部坏位确定角色，给两条真实 Schwartz、同一 degree390 全权平方及普通/惰性通常全 Selmer 桥。两线已在原完整 $\delta$-new 交叉项中实际非零。无穷多个素数的中央首导数非零尚未由这些新来源自动取得。

## 1. 原完整三因子确定这两条线的算术类型

固定 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$、
$\zeta_6=-\omega$、$\zeta_{12}^2=\zeta_6$、
$\zeta_{12}^4=\omega^2$，保持 R959 的
$$
 \alpha=15/13,\qquad\kappa=45\sqrt3/13.
 \tag{1}
$$
原 degree390 的完整 Fourier 模型是
$W_2\otimes W_3\otimes W_5\otimes W_{13}$，维数
$2\cdot3\cdot5\cdot13=390$。其几何 $\mu_6$ 主型为
$$
 V_{390}=\sigma^{390}K[X]_{\le65},\qquad X=x^3,\qquad\dim_KV_{390}=66.
 \tag{2}
$$
第65次 $X$ 是质量列，完整保留。

二处采用 R959(21) 的实际矩阵。它的特征为 $1,\omega$；
以 $\epsilon=0,1$ 标记，算术单位角色为
$\operatorname{Teich}_{\mu_3}^{\,1+\epsilon}$。
五处以 $g_5=-\omega$ 标记 $\tau_a(g_5)=\zeta_6^a$，
$a\ne3$，各重数一；十三处以 $t=x+6y$、生成元2标记
$\tau_b(2)=\zeta_{12}^b$，只有 $b=6$ 重数二。这两张完整迹表
与 R973 相同，实际矩阵改用 R959 的 $\alpha=15/13$。

三处必须保全部三方向。R776 与 R959 的实际中心相位
$\psi_3(5/156)=\omega$ 给
$$
 W_3(\omega)=\operatorname{diag}(1,\omega,\omega),\qquad
 W_3(-1)(f_0,f_v,f_{-v})=(f_0,f_{-v},f_v).
$$
以 $(c,\eta)$ 标记三条特征：
$$
 (c,\eta)=(0,0),(1,0),(1,1),\qquad
 \tau_3(\omega)=\omega^c,\quad\tau_3(-1)=(-1)^\eta .
 \tag{3}
$$
它们对应 $\phi_0,\phi_{\rm e},\phi_{\rm o}$，不是三个可任选的相位。
完整 Hilbert90 转置为
$$
 \chi_{3,c,\eta}(\varepsilon\omega^j)=\varepsilon\omega^{cj},
 \qquad
 \chi_{3,c,\eta}(\delta)=-i(-1)^\eta.
 \tag{4}
$$
第一条导子为 $\delta$，另外两条准确为 $\delta^2$。

与其余实际有限矩阵组合，几何 $\mu_6$ 不变条件恰为
$$
 \boxed{a+b+\eta\equiv0\pmod2,\qquad
        a+b+\epsilon+c\equiv0\pmod3.}
 \tag{5}
$$
第一条也来自主 idèle $\delta$：其无穷、3、5及双13值的乘积为
$(-1)^{a+b+\eta}$；全局 $-1$ 的无穷与3处因子已相消。
第二条是全局主单位 $\omega$ 的相容条件。
坏单位的其余部分完整为
$$
 \chi_2(u)=\operatorname{Teich}_{\mu_3}(u)^{1+\epsilon},\quad
 \chi_5(u)=u^{4(a+3)},\quad
 \chi_\pi(u)=\lambda_{13}(u)^{6-b},\quad
 \chi_{\bar\pi}(u)=\lambda_{13}(u)^{b-6},
 \tag{6}
$$
其中 $\pi=4+\omega$、$\lambda_{13}(2)=\zeta_{12}$，方向与 R973 相同。
由类数一，(4)–(6) 及主 idèle 公式唯一规定整个角色；
uniformizer 不是在好位读取谱之后另猜。

在三处的有限商中，实际
$\gamma_7/\bar\gamma_7=\omega^2$、
$\gamma_{19}/\bar\gamma_{19}=\omega$。
将它们和 R973 的完整 theta-group 交织合并，得到
$$
 \boxed{
 \lambda_7=\zeta_{12}^{\,8-4\epsilon-6a+b+4c},\qquad
 \lambda_{19}=\zeta_{12}^{\,6+4a+3b+8c}.}
 \tag{7}
$$
原 theta-group 的共同绝对标量仍由 R959 的真实 $E_{65}$ 锚固定；
将这个标量与完整有限标签合并后，
其标签 $(\epsilon,a,b;c,\eta)=(0,4,4;1,0)$ 在 (7) 上准确为
$(\omega^2,-1)$。完整平移提升、Gaussian 与 trace 的除数一并保留。

$(c,\eta)=(0,0)$ 给原22维 $\delta$-old部分。
$(1,0)$ 给22维，含14维六次值与8维非六次值；
$(1,1)$ 给22维，含10维六次值与12维非六次值。
所以原 $\delta$-new44维准确为 $24+20$，与 R976 全66列的实际回执一致。
这个计数包含13处的 quadratic 重数二，不把44维当成两份同一22维来源。

令 $(i_7,i_{19})$ 指 R976 的
$(U-\zeta_6^{i_7},U-\zeta_6^{i_{19}})$ 因子。
将 (5) 的全部合法标签代入 (7)，两条目标唯一为
$$
 \begin{array}{c|c|c}
 (i_7,i_{19})&(\epsilon,a,b;c,\eta)&d\\ \hline
 (3,5)&(0,5,0;1,1)&5^2\,13^3=54925\\
 (5,3)&(0,1,4;1,1)&5^4\,13=8125.
 \end{array}
 \tag{8}
$$
其算术解释由 (6) 的全部单位角色给出：当 $b$ 偶数时，
$v_5(d)\equiv a+3\pmod6$、
$v_{13}(d)\equiv3-b/2\pmod6$、
$v_2(d)=2\epsilon$。这里两个 $a$ 都为奇数，故三处必须用
$\phi_{\rm o}$，uniformizer 为 $+i$。两数都为 $7\pmod9$，
与 (4) 的实际局部六次类一致。它们不是 R959 的 even 三方向。

## 2. 两条固定曲线的无条件秩至少二

本节给实际独立性证明，不用数据库的 rank 字段。
两条曲线上可显示
$$
 \begin{array}{c|c|c}
 E& P&Q\\ \hline
 E_{54925}&(39,338)&(-39/4,1859/8)\\
 E_{8125}&(-9,86)&(129/4,1633/8).
 \end{array}
 \tag{9}
$$
直接对这些点取 $y+\sqrt d$ 的三次下降时，某些像是立方，
不能据此判定不独立。改用真实对偶三同源上的两点。

对 $E_B:y^2=x^3+B$，三同源曲线是
$E'_B:y'^2=x'^3-27B$，对偶的实际公式为
$$
 \widehat\phi(x',y')
 =\left(\frac{x'^3-108B}{9x'^2},
        \frac{y'(x'^3+216B)}{27x'^3}\right).
 \tag{10}
$$
以下两对点准确映为 (9)：
$$
 \begin{array}{c|c|c|c}
 B& E'_B& P'&Q'\\ \hline
 54925&y'^2=x'^3-1482975&(390,7605)&(156,1521)\\
 8125&y'^2=x'^3-219375&(75,450)&(300,5175).
 \end{array}
 \tag{11}
$$
每点直接满足其显示方程。候选坐标可在 Cremona 的原 allgens 数据
456300c2、456300co2 中找到；下述独立性完全在本地证明。

令 $F=\mathbf Q(r)$、$r^2=-39$，
$w=(1+r)/2$。则
$$
 \mathcal O_F=\mathbf Z[w],\qquad w^2-w+10=0.
 \tag{12}
$$
两个对偶常数分别是 $-39\cdot195^2$ 和 $-39\cdot75^2$。
对 $n=195$ 或75，定义
$$
 \Delta_n:E'_B(\mathbf Q)\longrightarrow F^\times/F^{\times3},
 \qquad (x',y')\longmapsto[y'+nr],\quad O\longmapsto1.
 \tag{13}
$$
同一原弦恒等式
$\prod_i(y'_i+nr)=(b_{\rm line}+nr)^3$
及 $(y'+nr)(-y'+nr)=-x'^3$ 给群同态；
它杀掉 $3E'_B(\mathbf Q)$，包含切线重交与垂直线情况。

### 2.1 E54925 的对偶两像

两下降值为
$$
 A=195(39+r),\qquad B_1=39(39+5r).
 \tag{14}
$$
5在 $F$ 中分裂；记 $\mathfrak q_+=(5,r-1)$、
$\mathfrak q_-=(5,r+1)$。有
$N(39+r)=1560$，其5赋值为一，而 $39+r$ 只在
$\mathfrak q_+$ 为零。因此
$$
 (v_{\mathfrak q_+}(A),v_{\mathfrak q_-}(A))=(2,1),\qquad
 (v_{\mathfrak q_+}(B_1),v_{\mathfrak q_-}(B_1))=(0,0).
 \tag{15}
$$
2也分裂，记 $\mathfrak p_0=(2,w)$、
$\mathfrak p_1=(2,w-1)$。由于
$$
 39+5r=2(17+5w),\qquad N(17+5w)=624=2^4\cdot39,
$$
$17+5w$ 在 $\mathfrak p_0$ 为单位、在 $\mathfrak p_1$ 有赋值四，故
$$
 (v_{\mathfrak p_0}(B_1),v_{\mathfrak p_1}(B_1))=(1,5).
 \tag{16}
$$
若 $A^uB_1^v$ 为立方，(15) 在 $\mathfrak q_-$ 迫
$u=0\bmod3$，再由 (16) 迫 $v=0\bmod3$。两像独立。

### 2.2 E8125 的对偶两像

这次
$$
 C=75(6+r),\qquad D=75(69+r).
 \tag{17}
$$
$N(6+r)=75$，且只有 $\mathfrak q_-$ 上为零，所以
$$
 (v_{\mathfrak q_+}(C),v_{\mathfrak q_-}(C))=(2,4).
 \tag{18}
$$
另一方面，$C$ 的范数为 $75^3$，故两个2素理想上的赋值均零。
准确有
$$
 69+r=2(34+w),\qquad N(34+w)=1200=2^4\cdot75.
$$
$34+w$ 只在 $\mathfrak p_0$ 非单位，因而
$$
 (v_{\mathfrak p_0}(D),v_{\mathfrak p_1}(D))=(5,1).
 \tag{19}
$$
若 $C^uD^v$ 为立方，先在 $\mathfrak p_1$ 迫 $v=0\bmod3$，
再用 (18) 迫 $u=0\bmod3$。两像也独立。

两对偶曲线都没有有理三挠：除法式
$3x'(x'^3+4B')=0$ 中，$x'=0$ 需要负数 $B'$ 为有理平方，
另一项的5赋值分别为2、4，均不是有理立方的赋值。
所以其 $E'_B(\mathbf Q)/3E'_B(\mathbf Q)$ 的维数就是有理秩。
(15)–(19) 给两个真实点的独立像，不涉及 Sha 或 Selmer 上界。
三同源保持秩，遂得
$$
 \boxed{\operatorname{rank}E_{54925}(\mathbf Q)\ge2,\qquad
        \operatorname{rank}E_{8125}(\mathbf Q)\ge2.}
 \tag{20}
$$
证明不需要 $F$ 的类数或单位生成元；全部独立性由两个分裂素数的原赋值承担。

## 3. 两条曲线全部 Hecke 角色、根数和 Hermitian 类

记 $\chi_B=\psi_B N^{-1/2}$，
$\chi_{B,\infty}(z)=(z/|z|)^{-1}$。
在两个13剩余嵌入中 $\omega$ 分别为9、3。
从 (4)–(8)，也从 Silverman–Stange 的原六次剩余式直接核定：
$$
 \begin{array}{c|c|c}
 v&\chi_{54925,v}\text{ 在单位上}
     &\chi_{8125,v}\text{ 在单位上}\\ \hline
 2&\operatorname{Teich}_{\mu_3}(u)&\operatorname{Teich}_{\mu_3}(u)\\
 3&\varepsilon\omega^j\mapsto\varepsilon\omega^j
      &\varepsilon\omega^j\mapsto\varepsilon\omega^j\\
 5&u^8&u^{16}\\
 \pi&u^6&u^2\\
 \bar\pi&u^6&u^2 .
 \end{array}
 \tag{21}
$$
其绝对 uniformizer 是
$$
 \begin{array}{c|c|c}
 v&\chi_{54925,v}&\chi_{8125,v}\\ \hline
 2\text{ 的 }2&-1&-1\\
 3\text{ 的 }\delta&+i&+i\\
 5\text{ 的 }5&-1&-1\\
 \pi\text{ 的 }\pi&\omega^2\pi/\sqrt{13}&\pi/\sqrt{13}\\
 \bar\pi\text{ 的 }\bar\pi&\omega\bar\pi/\sqrt{13}&\bar\pi/\sqrt{13}.
 \end{array}
 \tag{22}
$$
例如全局 $\pi$ 在2、3处的单位值是 $\omega,-\omega^2$。
在5及另一13处，第一曲线给 $\omega,-1$，乘积总为 $\omega$；
第二曲线给 $\omega^2,-\omega$，总乘积为1。
主 idèle 公式正好给 (22)，并保留两支。
全局 $\delta$ 在5处的值为 $+1$，这与 R959 的 $-1$ 不同，
所以三处必须为 $+i$。

二处的奇单位部分为 $1\bmod4$，在 $K_2$ 中为六次幂。
三处 $B/(-11)\equiv1\bmod9$，为同一 $\mathbf Q_3$ 六次类；
故 (21)–(22) 的三导子为 $\delta^2$。
五、十三处的 tame 指数显示导子各一次。因此
$$
 \mathfrak f_B=(390),\qquad N(E_B)=456300,\qquad
 [K(\mathfrak f_B):K]=10368=2^7\,3^4.
 \tag{23}
$$

五处的完整 Gauss 和为 $+5$，因为单位角色在
$\mathbf F_5^\times$ 平凡且在 $\delta$ 上为1；
再乘 $\chi_5(5)=-1$，epsilon 为 $-1$。
三处单位六项和仍为 $-3$，而
$\chi_3(\delta)^3=-i$，所以 epsilon 为 $+i$。
两13 split epsilon 的乘积为1，二处为1，无穷处为 $i$。
总根数为 $+1$；dichotomy 在 $2,3,5,13,\infty$ 为
$(+,-,-,+,+)$。因此 (1) 确是同一个正确 Hermitian 类，
没有因新 odd 三向量漏掉一个全局符号。

## 4. 全部实际有限 Schwartz

### 4.1 二、三处

二处 $\alpha\equiv3\bmod8$，使用 R959 的原四陪集生成元积分：
$$
 v_2=(1,t,-1,t),\qquad t=(\sqrt3-1)/\sqrt2,\qquad n_2=3-\sqrt3.
 \tag{24}
$$
三处准确取
$$
 \phi_{3,\mathrm o}
   =\mathbf1_{\frac19+\frac13\mathbf Z_3}
      -\mathbf1_{-\frac19+\frac13\mathbf Z_3},\qquad n_3=6.
 \tag{25}
$$
它的 $-1$ 特征为负，$\omega$ 特征为 $\omega$。
(4) 支付了它在真实 Hecke splitting 中的全部不变性；
不能将减号改成 R959 的加号，范数也不能沿用旧球的3。

### 4.2 五处真正的奇有限线

原五维矩阵是
$$
 W_5(x+y\delta)_{uv}
  =\frac{(y/5)}{\sqrt5}
       \zeta_5^{\,4\{x(u^2+v^2)-2uv\}/y},\quad y\ne0,
 \qquad W_5(-1)e_u=e_{-u}.
 \tag{26}
$$
两条所需角色分别为 $a=5,1$，均为奇角色。
$e_0$ 在它们上的投影为零，因此不能抄旧 even 投影公式。
固定
$$
 \Pi_a=\frac16\sum_{g\in T_5}\tau_a(g)^{-1}W_5(g),\qquad
 f_a=6\sqrt5\,\Pi_a e_1.
 \tag{27}
$$
令 $q_+(u)=u^2+u+1,q_-(u)=u^2-u+1$。全部六项展开为
$$
 \boxed{\begin{aligned}
 f_a(u)={}&\sqrt5(\mathbf1_{u=1}-\mathbf1_{u=-1})\\
 &-\zeta_6^{-a}\zeta_5^{q_+(u)}
   -\zeta_6^{-2a}\zeta_5^{-q_-(u)}
   -\zeta_6^{2a}\zeta_5^{q_-(u)}
   -\zeta_6^{a}\zeta_5^{-q_+(u)},\qquad a=1,5 .
 \end{aligned}}
 \tag{28}
$$
原四个非中央元的 $(x,y)$ 依次为
$(-2,2),(2,2),(2,-2),(-2,-2)$；
$y$ 均为非平方，给 (28) 的四个负号。
成对共轭与 $a$ 奇给 $f_a(u)\in\mathbf R$、
$f_a(-u)=-f_a(u)$。

这些投影确实非零。每个 $\tau_a$ 重数一；若其线与 $e_1$ 正交，
奇性迫整条线只支撑于 $\{\pm2\}$，即为
$K(e_2-e_{-2})$。但在 $g=(2,2)$ 下，其第1坐标是非零的
$-(\zeta_5^2-\zeta_5^3)/\sqrt5$，不可能仍在该线，矛盾。
正交投影于是给准确、严格正的范数
$$
 \boxed{\phi_{5,a}=\sum_{u\bmod5}f_a(u)\mathbf1_{u/5+\mathbf Z_5},
 \qquad n_{5,a}=6\sqrt5\,f_a(1)>0.}
 \tag{29}
$$
$f_a(1)$ 已由 (28) 完整显示为一个固定代数数；这个范数包含所有相位和
原 $\operatorname{vol}\mathbf Z_5=1$，不是一个待定归一常数。

### 4.3 两个13向量及非紧作用

十三处使用 R959 的实际矩阵
$$
 W_{13}(x+y\delta)_{uv}
 =\frac{(y/13)}{\sqrt{13}}\,
       \zeta_{13}^{\,3\{x(u^2+v^2)-2uv\}/y}.
 \tag{30}
$$
split 参数仍为 $t=x+6y$，quadratic splitting 为 $t^6$。
对 $E_{54925}$，单位角色为 $t^6$，故有限角色 $b=0$；
对 $E_{8125}$，单位角色为 $t^2$，故有限角色 $b=4$。
完整投影各乘 $6\sqrt{13}$，分别为
$$
 \boxed{f_{13,0}(u)=\sqrt{13}\mathbf1_{u=0}+1
        -\zeta_{13}^{4u^2}-\zeta_{13}^{10u^2}
        -\zeta_{13}^{3u^2}-\zeta_{13}^{9u^2},}
 \tag{31}
$$
$$
 \boxed{\begin{aligned}
 f_{13,4}(u)=\sqrt{13}\mathbf1_{u=0}+1
 &-\omega(\zeta_{13}^{4u^2}+\zeta_{13}^{3u^2})\\
 &-\omega^2(\zeta_{13}^{10u^2}+\zeta_{13}^{9u^2}).
 \end{aligned}}
 \tag{32}
$$
它们均实偶，零坐标为 $\sqrt{13}-3,\sqrt{13}+3$，非零。
每个原陪集 $\mathbf1_{u+13\mathbf Z_{13}}$ 的范数平方是 $1/13$，故
$$
 n_{13,0}=6(13-3\sqrt{13})/13,\qquad
 n_{13,4}=6(13+3\sqrt{13})/13.
 \tag{33}
$$
isometry 是 R959(26)，$A=\delta_0^3\alpha$、$13A\equiv3\bmod13$。
自然极化中两实际单位环带分别为
$\vartheta^{-1}\mathbf1_{\mathbf Z_{13}^{\times}}$，
$\vartheta(u)=u^6$ 或 $u^2$。该 isometry 将它们送到 (31)–(32)
的同一非零一维线，付清两个 split 分支的方向。

非紧 uniformizer 仍移动到不交环带；其矩阵系数只有零赋值环带
非零。完整紧平均的范数平方为 $1/12$，因而 Yang split 因子
$13/144$ 乘十二为 $13/12$。本篇既保 (22) 两个非紧参数，
也保这个实际 Haar 费用。

## 5. 原 degree390、同一全权平方及实际交叉项

令 $v_3=(0,1,-1)$，两条系数系统分别为
$$
 \begin{aligned}
 a_n^{54925}
 &=v_2(n\bmod4)v_3(n\bmod3)\,
       f_5(2n\bmod5)f_{13,0}(-n\bmod13),\\
 a_n^{8125}
 &=v_2(n\bmod4)v_3(n\bmod3)\,
       f_1(2n\bmod5)f_{13,4}(-n\bmod13).
 \end{aligned}
 \tag{34}
$$
有理支撑仍准确为 $x=n/90$。三处与五处两个奇因子相乘，故
$a_{-n}=a_n=\overline{a_n}$；CRT 及所有非零有限向量给来源非零。
准确周期仍是
$a_{n+780}=a_n$、$(-1)^na_{n+390}=-a_n$。
因此
$$
 F_B(Z)=\sum_na_n^B
  e^{\pi i(\delta/3)n^2/780+2\pi inZ},\qquad
 S_B(Z)=e^{390\sqrt3\pi Z^2}F_B(Z)
 \tag{35}
$$
是标准 $\mathcal O(390O)$ 的真实非零截面，无额外 flat twist。
(5) 的主型条件给全部六次对称性。

用原 Hermite 规范定义
$$
 b_{B,m}=\sum_n a_n^B H_m(\sqrt\kappa n/90)
                     e^{-\pi\kappa n^2/90^2},\qquad
 h=\sqrt\kappa/(180\pi i).
$$
完整生成式为
$$
 \sum_m b_{B,m}T^m/m!=S_B(hT),\qquad
 390\sqrt3\pi h^2=-1/(8\pi).
 \tag{36}
$$
$b_{B,m}$ 实，且 $6\nmid m$ 时为零。
对 $6\mid m$，(21) 全部单位角色及三处 $+i$ 保持；
13非紧参数随权变化，但同一单位环带矩阵系数仍只在零赋值环带
非零，故不用逐权更换 Schwartz。

置 $c(0)=65/108$，取 (24)、(25)、(29)、(33) 的实际范数，
$$
 C_B=\frac2{6c(0)}\frac{\pi}{3\sqrt3}
            \frac{\sqrt{2\kappa}}{n_2n_3n_{5,B}n_{13,B}}>0.
$$
Yang 的完整 theta 积分、所有局部费用及类数一的体积比六给
$$
 \boxed{L(\psi_B^{2m+1},m+1)
       =C_B\frac{(4\pi)^m}{m!}\,b_{B,m}^2\qquad(6\mid m).}
 \tag{37}
$$
由 (20) 与已证 CM 解析秩零定理的逆否命题，
$L(E_B,1)=0$，故 $b_{B,0}=0$。真实来源均至少六阶。

标准 Fourier 坐标 $a_n^B\zeta_{1560}^{-n^2}$ 全代数；
原两个390挠平移的绝对不可约 Heisenberg 交织，先给固定代数来源线。
其全部坏角色已由 (21)–(22) 指定，故 (7) 给准确 CM 值
$$
 (\lambda_7,\lambda_{19})_{54925}=(-1,-\omega^2),\qquad
 (\lambda_7,\lambda_{19})_{8125}=(-\omega^2,-1).
 \tag{38}
$$
这一步没有用计算谱来猜新曲线。

R976 的公开 run45884058894、job140130269899、源
fbb1c31937b02426caa21e77d65bd22e080a32c9，已在全部66列返回：
这两个完整共同块各秩一、质量零、全系数有理且首阶六。
将首项归一为一，写
$$
 \Phi_{B,1}=\sigma_1^{390}\sum_{j=0}^{64}u_{B,j}X_1^j,\qquad
 u_{B,j}\in\mathbf Q,\quad u_{B,64}=1.
 \tag{39}
$$
两源摘要依次为
4485e52f18d5349f8158e0d2177d38b6ae5c5b5862089ea66ab6e4cf4546bcb0、
dd354f3138dff257035c02561acef381470829b66fdb712801cb08455442fbe1。
先验非零来源、(38) 与完整一维性将它们唯一认回 (34)，不任选核向量。

对原 $\delta$-new 来源
$R_{\rm new}=(1-Q_\delta)(SZ_{390})$，实际全部坐标回乘给
$$
 \boxed{
 \Pi_{(3,5)}R_{\rm new}=\frac7{270}\Phi_{54925,1},\qquad
 \Pi_{(5,3)}R_{\rm new}=\frac{167}{360}\Phi_{8125,1}.}
 \tag{40}
$$
两块在 $\delta$-old 中秩零，因此同式也适用于原 $SZ_{390}$ 的这两个
完整谱投影。其余原 $\delta$-new 块依旧全部保留。

## 6. 物理周期、普通与惰性的通常全 Selmer 桥

对每条来源固定一次清分母 $D_B$，使
$\widehat u_{B,j}=D_Bu_{B,j}$ 整。以下只排这个固定有限坏集，保持
新平方常数的实际赋值。真正齐次来源为
$$
 \Phi_{B,b}(z)=\sigma_b^{390}\sum_{j=0}^{64}
            u_{B,j}b^{64-j}x_b^{3j}
       =b^{-1}\Phi_{B,1}(\theta_bz),\qquad\theta_b^6=b.
 \tag{41}
$$
物理参数是 $b=B$，共同参数是17；(1) 不是这两者之一。
沿用原 $\varpi_B=s_0\Omega_B$，(36)–(37) 的同一周期计算给固定
非零代数 $\widehat\kappa_B$：
$$
 \mathscr E_{B,m}=\frac{\widehat\kappa_B}{s_0}
                 390^{-m}\widehat s_{B,m}^{\,2},\qquad
 \widehat\Phi_{B,B}(z)=\sum_m\widehat s_{B,m}z^m,\quad6\mid m.
 \tag{42}
$$
它在第一个非零系数的临界值处由 CM 代数性取得，
清分母使常数除以 $D_B^2$；不逐权选平方根。

### 6.1 普通完整单位测度

对好普通 $p>211$，(41) 每项阶 $390-6j\ge6$。
原 CM sigma 整性给有界整测度 $\widehat\nu_{B,p}$。
取原单位切域、同一相容单位周期，定义
$$
 \widehat G_{B,p}(T)=\int_{\mathbf Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}
                  \,d\widehat\nu_{B,p}(x).
 \tag{43}
$$
Katz 的真实两个 Euler 因子同为
$1-\pi_p^m/\bar\pi_p^{m+1}$，其中 $\pi_p=\psi_B(\mathfrak p)$。
对全部 $p-1\mid m$，(42) 及同一单位矩极限准确给
$$
 \mathcal K_{B,p}(T)=
 \frac{\widehat\kappa_B}{s_0}\Omega_{p,B}
 (1+T)^{-\log_p\langle390\rangle/\log_p(1+p)}
                  \widehat G_{B,p}(T)^2.
 \tag{44}
$$
$L(E_B,1)=0$ 在同一 Katz 分支迫 $\widehat G_{B,p}(0)=0$，
不从全质量零单独推单位质量零。

Agboola–Howard 的正根数通常单 CM Selmer 定理及基层控制适用：
两曲线均最大整环 CM，ray 次数10368与 $p$ 互素；可用好惰性11
辅助理想，原中心因子 $-132$ 为单位。原2、$\delta^2$、5、双13
primitive 参数保持。惯性像排塔上初级挠点，二次分解及三同源保持
通常全 Selmer 范围，与 R959 的通用证明相同。
于是对 $r_B=\operatorname{rank}E_B(\mathbf Q)$、
$r_{B,p}=\operatorname{corank}_{\mathbf Z_p}\Sha(E_B/\mathbf Q)[p^\infty]$，
$$
 \boxed{r_B+r_{B,p}\le2\operatorname{ord}_0\widehat G_{B,p},\qquad
 \widehat G'_{B,p}(0)\ne0\Longrightarrow
 r_B=2,\quad\Sha(E_B/\mathbf Q)[p^\infty]\text{ 有限}.}
 \tag{45}
$$
秩下界由 (20) 提供，不假定两曲线已经精确秩二。

### 6.2 惰性完整 Newton 与 signed 通常群比较

令 $p=6s-1>211,d=p+1$，在原 $E_1$ 上保持
$f=\log(\sigma/z),c_p=[z^d]f$，$v_p(c_p)=-1$。
定义
$$
 \widehat H_{B,p}=\widehat\Phi_{B,1}e^{-390c_pz^d},\qquad
 a_{B,h}=(390c_p)^{-h}[z^{dh}]\widehat H_{B,p},
 \qquad
 \widehat J_{B,p}(v)=\sum_{h\ge0}a_{B,h}(v)_h.
 \tag{46}
$$
完整余项是
$\sum_{j=0}^{64}\widehat u_{B,j}z^{390-6j}
 (z^2x)^{3j}\exp\{390(f-c_pz^d)\}$。
R301 的同一严格圆盘给
$$
 v_p(a_{B,h})\ge
 \left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\qquad
 \widehat J_{B,p}\in pv\mathcal O\langle v\rangle,
 \quad
 \widehat J_{B,p}(k)=k!(390c_p)^{-k}[z^{dk}]\widehat\Phi_{B,1}.
 \tag{47}
$$
没有更换 Gaussian 或截掉后续系数。

取单位 Hensel 根 $\theta^6=B$。
实际整模型同构 $F_\theta:E_1\to E_B$ 为
$(X,Y)\mapsto(\theta^2X,\theta^3Y)$，
$F_\theta^*\omega_B=\theta^{-1}\omega_1$。
同时运输 Gaussian 为 $\theta^dc_p$，Newton 系数中的
$\theta^{dh}$ 完全相消。物理半因子是
$B^{-1}\widehat J_{B,p}$，共同模型是 $17^{-1}\widehat J_{B,p}$。

R303/R943/R959 的同一个 primitive 椭圆单位类和完整 BKO signed
格给 $0\ne\mathcal A_{B,p}\in\mathcal O[[T]]$。新费用逐项为
导子390、ray10368、(22) 的三处 $+i$ 与5、双13相位、同一实际
微分和 CM/Tate 张量。三处 finite Gauss 与导子幂只是固定3单位；
两边 $m!$、Tate/Gamma 和 $p$ 处 $1+1/p$ 非单位因子只在比中消去。
参考5因子 $6/5$ 及双13因子
$$
 (1-\rho^{2m+1}/13^{m+1})(1-\bar\rho^{2m+1}/13^{m+1}),
 \quad\rho=-\omega^2\pi,\quad\rho+\bar\rho=2
 \tag{48}
$$
在 $d\mid m$ 上分别为单位，后者模 $p$ 为 $12/13$。
辅助好惰性 $\ell\equiv1\bmod p$ 的原因子模 $p$ 为2。
有限六次扭曲由 $d\mid m$ 消掉，使用同一反圆分支。

混合权比较采用 Kato 已证 (15.16.1) 与 Theorem12.5(1)：
从 §15.8 的同一 CM 张量，分别拉回 Lemma15.11 的 étale/de Rham
和 Betti 周期图，共同任意标量消去；不需要尚未证明的更强 motivic
图相容命题。完整核查见本轮 mixed-weight period audit note。
因此在 $x_m=q_{\rm ac}^m-1$、$v_p(q_{\rm ac}-1)=1$ 时，逐权准确有
$$
 \boxed{v_p\mathcal A_{B,p}(x_{dk})
       =v_p(\widehat\kappa_B)+2v_p\widehat J_{B,p}(k).}
 \tag{49}
$$
固定平方常数的赋值保留；被约掉的剩余单位不必随权解析。
沿 $k=p^n$ 比较 $n$ 的系数得
$\operatorname{ord}_0\mathcal A_{B,p}
 =2\operatorname{ord}_0\widehat J_{B,p}$，非零 $\mathcal A$ 排除
$J\equiv0$。平凡角色在正号格；BKO Theorem6.2 的通常全 Selmer
控制没有相反符号的一维加项。因此
$$
 \boxed{r_B+r_{B,p}\le2\operatorname{ord}_0\widehat J_{B,p},\qquad
 \widehat J'_{B,p}(0)\ne0\Longrightarrow
 r_B=2,\quad\Sha(E_B/\mathbf Q)[p^\infty]\text{ 有限}.}
 \tag{50}
$$

完整有限证书仍为
$$
 L_{B,H}=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_{B,h},\qquad
 M_H=\left\lceil\frac{(H+1)(p-1)+6}{2p}\right\rceil+v_p(H!),
$$
$$
 \widehat J'_{B,p}(0)\ne0
 \quad\Longleftrightarrow\quad
 \exists H:\ v_p(L_{B,H})<M_H.
 \tag{51}
$$
(47) 给完整尾项赋值至少 $M_H\to\infty$，故这不是首位模 $p$ 判据。

## 7. 原来源中的使用范围

本篇新增的是两条有真实独立点和完整通常群桥的固定曲线来源。
(40) 表明它们已经出现在原 $SZ_{390}$ 的完整 $\delta$-new部分，
而非为了扩大空间另挑两条任意特征线。

若要把它们接到原六 sigma 张量的完整 companion，仍应在同一次原66
矩阵上读取实际六 sigma 候选的两个投影，并保原整 Gram、全半特征、
双向逆及 mixed cut。不能将 (40) 的非零交叉投影直接当成一个新的
单位 companion，也不能给原 $\delta$-new 整个44维来源赋两条中央零。
主目标所需的无穷素数量词仍须对这些实际中央与已有来源联合消费。

## 依据与来源

- 候选点：John Cremona 原数据 allgens.450000-459999，
  456300c1/c2、456300co1/co2：
  <https://github.com/JohnCremona/ecdata/blob/master/allgens/allgens.450000-459999>。
  本篇 (10)–(20) 自行证明独立性，未引用其 rank 输出。
- R776：原三处完整三个方向、绝对 phase、Hilbert90 转置和精确
  $\delta^2$ 导子；R959：本篇同一 $\alpha=15/13$ 的实际2/5/13矩阵、
  split isometry、完整390周期及通常全 Selmer 通用桥。
- R973：原全部有限角色、theta-group 交织与绝对好位算子；
  R976：同次全66矩阵及 (40) 的实际完整回执。
- Silverman–Stange §6 原六次剩余方向：
  <https://arxiv.org/pdf/0912.1831>。
- Yang 的原 theta 积分及全部局部公式：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>、
  <https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>、
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- Agboola–Howard Theorem2.4.17(1)：
  <https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf>；
  BKO (2021) Theorems6.1–6.2：
  <https://annals.math.princeton.edu/2021/194-3/p08>；
  BKO (2024) §2.2.1、Corollary4.11(i)、Proposition4.12：
  <https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf>。
- Kato §15.8、Lemma15.11、(15.16.1)、Theorem12.5(1)：
  <https://www.numdam.org/article/AST_2004__295__117_0.pdf>。
