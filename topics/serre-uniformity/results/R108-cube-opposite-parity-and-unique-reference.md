# R108：立方分母的两个异奇偶分支，排除偶数 $a$ 并确定唯一参考

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明，含精确有限计算。** 处理 R19 的族 I 与族 III 奇数 $X$、$Z=Y^3$。两个分支都必须有 $a$ 奇、$b$ 偶；分别得到 $Y\equiv1,-1\pmod8$，并将辅助模 $p$ 同余的参考扭曲唯一确定。没有排除这些剩余全局同余。

## 1. 两个实际分支及结论

沿用[完整原始参数化](../notes/2026-11-12-cube-denominator-primitive-quartics.md)。参数满足
$$
a,b>0,\quad(a,b)=1,\quad a,b\text{ 奇偶相反},\quad
3\nmid a,\quad |Y|>1,\quad(Y,6p)=1.
$$
族 I 还要求 $3\mid b$。定义
$$
F=a^4-18a^2b^2-27b^4,\qquad
G=27b^4-18a^2b^2-a^4.
$$
实际的两行分别为
$$
\begin{array}{c|c|c|c}
\text{族}&\text{方程}&X&W\\\hline
\mathrm I&F=Y^p&Y^p+36a^2b^2&\pm2ab(a^4+27b^4)\\
\mathrm{III},\ X\text{ 奇}&G=Y^p&Y^p+36a^2b^2&\pm2ab(a^4+27b^4).
\end{array}
\tag{108.1}
$$
原曲线分别是
$$
E_{\mathrm I}:y^2=x^3-Xx-2W,\qquad
E_{\mathrm{III}}:y^2=x^3-4Xx-16W.
\tag{108.2}
$$
[R19](R19-converse-fermat-fixed-cm.md) 给 $E[p]\simeq A[p]$，$A:y^2=x^3-x$；实际 $p>37$、$p\equiv3\pmod4$。

置 $K=\mathbb Q(r)$、$r^2=3$。用 $\sigma=1$ 表示族 I，$\sigma=-1$ 表示族 III 奇数 $X$，定义
$$
S=a^2+3\sigma b^2,\qquad h=S/2,\qquad
B_\sigma(a,b):y^2=x^3+4ax^2+(2a^2+rS)x.
\tag{108.3}
$$
这里 $S$ 奇，所以 $h$ 是**半整数**。但 $B_\sigma$ 的显示系数都是 $\mathcal O_K$ 整数，且它精确等于此前的
$B(a,h):y^2=x^3+4ax^2+2(a^2+rh)x$，没有通过丢弃 $2$ 因子假称原始。

令
$$B_0:y^2=x^3+4x^2+(2+r)x.$$

**定理 108.1。** 对 (108.1) 的每一个实际分支，
$$
\boxed{a\text{ 奇},\quad b\text{ 偶};\qquad
Y\equiv\begin{cases}1\pmod8,&\mathrm I,\\-1\pmod8,&\mathrm{III},\ X\text{ 奇}.\end{cases}}
\tag{108.4}
$$
并且存在唯一可能的 $d\in\{1,-1,2,-2\}$：
$$
\boxed{B_\sigma(a,b)[p]\simeq B_0^{(d)}[p],\qquad
d=\left(\frac a3\right)(-2)^e,\quad
e\equiv b/2\pmod2,\quad e\in\{0,1\}.}
\tag{108.5}
$$
同构在 $G_K$ 的 $\mathbb F_p$ 表示上成立。唯一性是指四个固定参考中的唯一必要选择，不是把局部条件当作全局同构的充分条件。

## 2. 半整数 $h$ 的准确导子，仍是层 $768$

令
$$u=1+r,\quad\pi=r-1,\quad\varepsilon=2+r=u/\pi,\quad C=B_\sigma^{(u)}.$$
R99 的显式 $\mu:C\to\overline C$、$\overline\mu\mu=[-2]$ 和系数下降因子 $\sqrt{-2}$ 对任意 $a,h$ 都成立，所以仍有
$$
\det\widetilde\rho=\chi_{12}\chi_{\rm cyc},\qquad
\widetilde\rho^{\,\sqrt{-2}\mapsto-\sqrt{-2}}
=\widetilde\rho\otimes\chi_{12}.
\tag{108.6}
$$

置 $D_\pm=2a^2\pm rS$。它们在 $\mathfrak p_2=(\pi)$ 为单位，且
$$
D_+D_-=4a^4-3S^2
=\begin{cases}Y^p,&\sigma=1,\\-Y^p,&\sigma=-1.\end{cases}
$$
准确判别式为
$$
\Delta(B_\sigma)=64D_+^2D_-,\qquad
v_{\mathfrak p_2}(\Delta(C))=18.
\tag{108.7}
$$

### 2.1 对全部异奇偶参数的最小 $\mathrm I_2^*$ 模型

在 $C$ 上作
$$x=x'+\pi,\qquad y=y'+\pi^2.$$
所得系数满足
$$
a'_1=0,\quad a'_2=4au+3\pi,\quad a'_3=2\pi^2,
$$
$$
a'_4=\pi^2(\varepsilon^2D_++8a\varepsilon+3),
$$
$$
a'_6=\pi^3(\varepsilon^2D_++4a\varepsilon+1-\pi).
\tag{108.8}
$$
这里 $v_{\mathfrak p_2}(2)=2$。因为 $S$ 奇，
$$D_+\equiv r\pmod{2\mathcal O_K},\qquad
\varepsilon^2\equiv1\pmod{2\mathcal O_K}.$$
所以 $a'_4/\pi^2\equiv1+r\pmod{2\mathcal O_K}$，恰有赋值一；而 $a'_6/\pi^3$ 被 $2$ 整除。因而
$$
(v(a'_1),v(a'_2),v(a'_3),v(a'_4),v(a'_6))
=(\infty,1,4,3,\ge5).
\tag{108.9}
$$

具体地，Tate 算法的 $\mathrm I_0^*$ 三次多项式模 $\pi$ 为
$$
T^3+\overline{a'_2/\pi}\,T^2
+\overline{a'_4/\pi^2}\,T+\overline{a'_6/\pi^3}
=T^2\bigl(T+\overline{a'_2/\pi}\bigr),
$$
原点恰为二重根。进入 $\mathrm I_n^*$ 循环后，$n=1$ 所用二次式为
$$
T^2+\overline{a'_3/\pi^2}\,T-\overline{a'_6/\pi^4}=T^2,
$$
仍为二重根。$n=2$ 所用二次式则为
$$
\overline{a'_2/\pi}\,T^2+
\overline{a'_4/\pi^3}\,T+\overline{a'_6/\pi^5}.
$$
其线性系数为单位，在特征二中可分，所以准确停止在 $\mathrm I_2^*$。横线均指模 $\pi$ 约化；$n=1$ 中的负号来自把 $a'_6$ 移到 $y$ 方程左边，在本剩余特征下不影响根。这也证明显示模型最小。由七个分量及 (108.7)，
$$
v_{\mathfrak p_2}\mathfrak N_C=18+1-7=12.
\tag{108.10}
$$
此推导同时涵盖 $a$ 奇及 $a$ 偶，不预先使用待证结论 (108.4)。

在 $\mathfrak p_3$ 处仍好约化，迹为 $-2(a/3)$。每个 $q\mid Y$ 在 $K$ 分裂，两处乘法最小判别式赋值为 $p\,v_q(Y)$ 和 $2p\,v_q(Y)$。$C$ 在 $p$ 上方好约化。因此
$$
\mathfrak N_C=\mathfrak p_2^{12}\operatorname{rad}(|Y|)\mathcal O_K,
\qquad N(\widetilde\rho)=768\operatorname{rad}(|Y|).
$$
R99 的基本单位、$\mathfrak p_3$ 结果式和复共轭证明仍给全部实际 $p>37$ 的绝对不可约性；唯一形式例外 $97$ 与 $p\equiv3\pmod4$ 冲突。模 $p$ 在 $q\mid Y$ 不分歧，在 $2,3$ 精确保持导子指数 $8,1$，在 $p$ 为权二。故
$$
\overline{\widetilde\rho}\simeq\overline\rho_{f,\mathfrak P},
\qquad f\in S_2^{\rm new}(768,\chi_{12}),\quad\mathfrak P\mid p.
\tag{108.11}
$$
全部模性与不可约原始来源及假设核验见 R99 §§2–4、10；半整数的分母只有 $2$，不影响所用奇素数和 $p$ 处条件。

## 3. 原曲线模型的精确比较，及两个完整筛

本节说明为何可直接使用两个已完整枚举的迹集合，不混用 Frey 模型。

对 $F$ 分支，(108.2) 的原曲线就是
$$
y^2=x^3-(a^4+18a^2b^2-27b^4)x
\mp4ab(a^4+27b^4).
\tag{108.12}
$$
它与 R99 的 III 偶分支在相同形式参数 $(a,b)$ 上的显示曲线**逐系数相等**：R99 的 $X$ 缩为这里的 $1/4$、$W$ 缩为这里的 $1/8$，其模型又使用 $-4X,-16W$。

对 $G$ 分支，令 $X_0=27b^4+18a^2b^2-a^4$。这里的原曲线为
$$y^2=x^3-4X_0x\mp32ab(a^4+27b^4).$$
换元 $x=4x',y=8y'$ 后得到
$$y'^2=x'^3-\frac{X_0}{4}x'\mp\frac{ab(a^4+27b^4)}2,$$
恰为 R106 的族 II 原模型。辅助曲线也精确相同，因为都使用 $h=(a^2-3b^2)/2$。

因此 $F$ 的局部辅助迹平方集合就是 R99 的 $S_q$，$G$ 的就是 R106 的 $S_q$。相同的分母素数下界 $q\mid Y\Rightarrow q\ge4p-1$ 与 Hasse 界，使 $q\ne p$ 时原迹必须等于 $a_q(A)$。仍定义
$$
D_q(f)=q\prod_{t\in S_q}N_{\mathbb Q(f)/\mathbb Q}(a_q(f)^2-t),
\quad
G_f=\gcd_{q\in\{11,13,23,37,47,59,61,71,73,83,97\}}D_q(f).
\tag{108.13}
$$
前置 $q$ 处理 $q=p$，故所有实际 $p>37$ 都须整除 $G_f$。

对层 $768$ 的全部十个轨道，**两个**筛恰好给出同一 gcd 列：
$$
(2^{12},0,0,2^{12},0,0,2^{24},2^{24},2^{24},2^{28}).
\tag{108.14}
$$
本证书重新运行完整新形式空间及两个范数计算，未将较大层 $1536$ 的轨道误用于这里。新空间维数 $28$、轨道次数为 $2,2,2,2,2,2,4,4,4,4$，全部覆盖。

故仅剩 R99 已精确识别的四条 $B_0^{(d)}$，$d=\pm1,\pm2$。不同系数共轭只引入 $\chi_{12}$，限制到 $G_K$ 不变；共同去掉角色 $\chi$，得到
$$B_\sigma(a,b)[p]\simeq B_0^{(d)}[p].\tag{108.15}$$
以下二进比较不再扩大同一种奇素数窗口。

## 4. 使用 R103 的两个带嵌入好约化域

沿用 R103 的两个三挠点域 $\mathscr L_\delta$，$\delta=1,2$。它们在 $\mathbb Q_2$ 上有 $e=8,f=2$，在 $K_{\mathfrak p_2}$ 上有 $e=4,f=2$，且 $B_0^{(\delta)}$ 好约化。其方程和嵌入为
$$
z^4+16z^3+18(2+r)z^2-27(2+r)^2=0,\quad x_0=z/3,
$$
$$
w_\delta^2=81\delta\bigl(x_0^3+4x_0^2+(2+r)x_0\bigr).
\tag{108.16}
$$
绝对点域的最大整环判别式为 $2^{48}3^{20}$。本证书按 (108.16) 重新构造，核验唯一二进素理想与参考好约化。

因为 $\mathscr L_\delta$ 包含 $\sqrt3$ 和剩余次数二的未分歧二次域 $\mathbb Q_2(\sqrt5)$，任意有理奇单位在两个域中都是平方。因此奇单位归一化不会改变实际同构类，负号扭曲也平凡。

- 若 $a$ 奇、$b$ 偶，令 $t=b/a\in2\mathbb Z_2$，则在这些域中可用
  $$B_\sigma(1,t):y^2=x^3+4x^2+\bigl(2+r(1+3\sigma t^2)\bigr)x.$$
- 若 $a$ 偶、$b$ 奇，令 $t=a/b\in2\mathbb Z_2$，则可用
  $$B_\sigma(t,1):y^2=x^3+4tx^2+\bigl((2+r)t^2+3\sigma r\bigr)x.$$

两个图完整覆盖全部原始异奇偶参数。

## 5. 十六个基准模型及全部参数的稳定性

在每个域、每个 $\sigma=\pm1$，分别取
$$(a,b)=(1,0),(1,2),(0,1),(2,1).$$
下面表格对两个 $\sigma$ 同时有效；完整十六个模型的全部系数赋值存于证书。所有 $v$ 都是 $\mathscr L_\delta$ 的整数归一化，$v(2)=8$。换元为
$$x=U^2x'+R,\qquad y=U^3y'+SU^2x'+T.$$

| 参数图 | $t\bmod4$ | $\delta$ | 型 | 导子指数 | $v(\Delta_{\min})$ | $(v(U),v(R),v(S),v(T))$ |
|---|---:|---:|---|---:|---:|---|
| $a$ 奇、$b$ 偶 | 0 | 1 | 好 | 0 | 0 | $(4,0,0,4)$ |
| $a$ 奇、$b$ 偶 | 2 | 1 | II$^*$ | 4 | 12 | $(3,0,0,4)$ |
| $a$ 奇、$b$ 偶 | 0 | 2 | II$^*$ | 4 | 12 | $(3,0,0,4)$ |
| $a$ 奇、$b$ 偶 | 2 | 2 | 好 | 0 | 0 | $(4,0,0,4)$ |
| $a$ 偶、$b$ 奇 | 0 或 2 | 1 或 2 | $\mathrm I_0^*$ | 8 | 12 | $(3,0,0,4)$ |

### 5.1 奇数 $a$ 的两条剩余类

固定 $t_*=0$ 或 $2$，令 $t=t_*+4z$、$z\in\mathbb Z_2$。原模型只改变
$$a_4,\qquad \eta=3\sigma r(t^2-t_*^2),\qquad v(\eta)\ge32.$$
在同一个换元中，
$$\delta a'_4=\eta/U^4,\qquad
\delta a'_6=R\eta/U^6.
\tag{108.17}
$$
好约化行的两个增量赋值至少为 $16,8$，故仍整。原判别式的赋值恒为 $48$，$v(U)=4$ 除去全部赋值，故仍好约化。

II$^*$ 行的两个增量赋值至少为 $20,14$。原最小模型满足
$$v(a'_1)\ge1,\ v(a'_2)\ge2,\ v(a'_3)\ge3,\ v(a'_4)\ge4,\ v(a'_6)=5.$$
这些条件及 Tate 算法的 II$^*$ 终止步骤完整保持；原判别式减去 $12v(U)$ 后仍为 $12$，始终坏约化。

### 5.2 偶数 $a$ 的两条剩余类

仍令 $t=t_*+4z$，此时原模型同时改变 $a_2,a_4$，分别记为 $\eta_2,\eta_4$：
$$
\eta_2=4(t-t_*),\qquad
\eta_4=(2+r)(t^2-t_*^2),\qquad
v(\eta_2),v(\eta_4)\ge32.
$$
在同一个换元下，
$$
\delta a'_2=\eta_2/U^2,\qquad
\delta a'_4=(\eta_4+2R\eta_2)/U^4,
$$
$$
\delta a'_6=(R\eta_4+R^2\eta_2)/U^6.
\tag{108.18}
$$
其赋值分别至少为 $26,20,14$。基准模型有
$$
v(a'_1)\ge1,\quad v(a'_2)\ge2,\quad v(a'_3)\ge3,\quad
v(a'_4)=2,\quad v(a'_6)=3.
$$
Tate 算法的 $\mathrm I_0^*$ 三次多项式化为
$$T^3+\alpha T+\beta,\qquad \alpha\ne0,\quad\beta\ne0$$
于特征二的剩余域。它可分：若其导数为零，则 $T^2=\alpha$，代回多项式得到 $\beta\ne0$。所以准确型为 $\mathrm I_0^*$；(108.18) 保持全部所用剩余系数，原判别式赋值仍给 $12$，导子仍为 $12+1-5=8$。这证明**每个偶数 $a$、奇数 $b$ 参数在两个域中都坏约化**。

以上稳定性证明覆盖无界 $z$，没有把有限十六个模型当作经验分类。

## 6. 偶数 $a$ 全排，奇数 $a$ 时唯一确定 $d$

若 (108.15) 中 $d=\pm\delta$，则参考在 $\mathscr L_\delta$ 好约化。实际 $B_\sigma[p]$ 也必须在那里不分歧。潜在好约化的有限惯性像的阶只含 $2,3$，而 $p>37$，所以模 $p$ 约化忠实；由 Néron–Ogg–Shafarevich，实际曲线也必须好约化。

第 5.2 节与此矛盾，故 $a$ 偶不可能。于是 $a$ 奇、$b$ 偶。第 5.1 节进一步给
$$
4\mid b\Rightarrow d\in\{\pm1\},\qquad
b\equiv2\pmod4\Rightarrow d\in\{\pm2\}.
\tag{108.19}
$$
因为 $a$ 是奇单位，$t=b/a\bmod4$ 与 $b$ 有相同的“零或二”类别。

在 $\mathfrak p_3=(r)$，实际与参考迹分别为 $-2(a/3)$、$-2(d/3)$。它们的模 $p$ 相等性在 $p>37$ 时就是整数相等，故
$$d\equiv a\pmod3.$$
结合 (108.19) 便得到唯一值 (108.5)。

这里只使用参考好约化迫使实际好约化的必要方向；从共同好约化不推出全局或局部模 $p$ 同构的充分性。

## 7. 对原 $Y$ 的新约束

对奇偶相反的 $a,b$，直接模 $8$ 算得
$$
\begin{array}{c|cc}
&F\bmod8&G\bmod8\\\hline
a\text{ 奇},b\text{ 偶}&1&-1\\
a\text{ 偶},b\text{ 奇}&5&3.
\end{array}
$$
$p$ 奇，且 $(\mathbb Z/8\mathbb Z)^\times$ 的指数为二，所以 $Y^p\equiv Y\pmod8$。结合第 6 节，得到 (108.4)。

因此族 I 的 $Y\equiv5\pmod8$ 与族 III 奇数 $X$ 的 $Y\equiv3\pmod8$ 均被全部排除。剩余类仍有无穷多个整数参数；这不是变动 $Y,p$ 的统一无解结论。

## 8. 复验及与先前结果的关系

- [标准库 Python + 内嵌 GP 验证程序](../notes/verify_r108_cube_opposite.py)。
- [两个完整范数筛及十六个局部模型证书](../notes/r108_cube_opposite_parity_certificate.json)。

~~~sh
python3 -B topics/serre-uniformity/notes/verify_r108_cube_opposite.py \
  --gp /tmp/pari-2.19.0/gp --check
~~~

程序调用已入库的 R99、R106 有限域生成函数，从零重做两个必要迹集合；再重新计算层 $768$ 的十个轨道和全部范数。数域与局部换元也按 (108.16) 重做，不使用预存局部模型。--write 可重新生成证书。所有计算是无条件精确运算，无 GRH 或浮点识别。

固定参考 $B_0$ 的非 CM、准确模性及系数轨道识别均已在 R99 完整证明。R103 给出的带嵌入三挠点域也在这里重新构造。局部标准输入为 Tate 算法、Ogg 公式、Néron–Ogg–Shafarevich；半整数 $h$ 的准确模型与全参数稳定性已在本文自含展开。

四条立方分母分支现在均有实际固定参考归约：R99–R103 处理 III 偶，R106 处理 II，本文处理 I 与 III 奇。这些限制仍未控制剩余全局同余的最大指数，也未处理非立方 $Z$ 的全部原始方程。

