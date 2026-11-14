# R263：实际二除法域的奇偶迹检测与双同域三次曲线正规形

日期：2026-11-13。

**状态：已证明。** 在 R258 的 $K=\mathbb Q(\sqrt{-3})$、$\sigma=1$、整 $j$ 设置中，本文继续 R261 留下的实际三除法商域相同分支。先证明实际判别式的平方类只能为 $\pm3$；若取 $+3$，得到有效下界 $c\gg_\delta p^{5/3-\delta}$。若平方类取 $-3$ 但实际二挠点域与真实 CM 参考不同，则得到 $c\gg_\delta p^{1/3-\delta}$。

结合 R261，除去这个后一量级的导子增长分支后，实际二挠点域和实际三除法 $S_3$ 商域必须同时与 CM 参考相同。该双同域条件等价于一个准确的有理模型，加上下列两条三次曲线之一：

$$\boxed{
\begin{gathered}
E_{a,b}: y^2=x^3+3abd\,x+d(a^3-db^3),\\
a^3+db^3=z^3
\quad\text{或}\quad
a^3+db^3=4dz^3,\qquad z\ne0.
\end{gathered}}
\tag{263.1}
$$

这里 $d=d_0>0$ 是 R258 的同一个真实 CM 参数，不能另选来适配这两条方程。它含 $p$，其余素数支撑由实际 $c$ 控制。这些三次曲线随 $d$ 变化；本文没有断言它们只有平凡点，也没有从导子下界偷换出绝对的 $p$ 上界。

## 1. 对象与定理

保留 R258 的实际假设

$$
p>37,\quad \rho_{E,p}(G_{\mathbb Q})=N_{\rm ns}(p),\quad
\rho_{E,p}(I_p)=C^3,\quad
H=K=\mathbb Q(\sqrt{-3}),\quad
\sigma=(\lambda/\psi)^6=1,\quad j(E)\in\mathbb Z.
\tag{263.2}
$$

按 R258 的同一个全局二次扭曲取

$$
E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3+d,\qquad
d>0\text{ 立方自由}.
\tag{263.3}
$$

于是

$$
\begin{gathered}
N(E_0)=N(A_d)=\kappa p^2c^2,\qquad
\kappa\in\{3,9,12,36,192,576\},\\
d=2^u3^v p^m\prod_{\substack{q\mid c\\q\ge5}}q^{e_q},
\quad u,v\in\{0,1,2\},\ e_q\in\{1,2\},\\
m=2\ (p\equiv2\pmod9),\qquad
m=1\ (p\equiv5\pmod9).
\end{gathered}
\tag{263.4}
$$

令 $\Delta_E$ 为 $E_0$ 的任意有理模型判别式，置

$$F=\mathbb Q(\sqrt{\Delta_E}),\qquad
\mathcal L_2(E_0)=\mathbb Q(E_0[2]).$$

判别式平方类和二挠点域均不受前述二次扭曲影响。仍以 $\mathcal L_3$ 表示 R261 的实际 $\operatorname{GL}_2(\mathbb F_3)/Q_8\simeq S_3$ 商域。

**定理 263.1。** 在 (263.2) 下：

1. $F=\mathbb Q(\sqrt{-3})$ 或 $\mathbb Q(\sqrt3)$，而 $p$ 在 $F$ 中惰性。特别当 $p\equiv11\pmod{12}$ 时必有 $F=H$。整性还给
   $$j(E)=1728-3n^2\quad\text{或}\quad1728+3n^2,\qquad n\in\mathbb Z,$$
   符号与 $\Delta_E$ 的平方类一致。
2. 若 $F=\mathbb Q(\sqrt3)$，则对任意 $\delta>0$，
   $$c\gg_\delta p^{5/3-\delta}.$$
3. 若 $F=H$ 但 $\mathcal L_2(E_0)\ne\mathcal L_2(A_d)$，则对任意 $\delta>0$，
   $$c\gg_\delta p^{1/3-\delta}.$$
4. 因此，对任意 $\delta>0$，以下至少一个成立：
   $$\boxed{c\gg_\delta p^{1/3-\delta};}
   \tag{263.5}$$
   或者
   $$\boxed{
   \mathcal L_2(E_0)=\mathcal L_2(A_d),\qquad
   \mathcal L_3(E_0)=\mathcal L_3(A_d).
   }
   \tag{263.6}$$
   在后一情形，$E_0$ 有 (263.1) 的有理短模型；反之，该模型中的任一非奇异有理解确实给两个域同时相同。

所有 $\gg_\delta$ 常数都绝对且有效。最后的反向只断言两个实际除法域相同，不断言任意该模型自动满足 (263.2) 的模 $p$ 同余、完整像或整 $j$。

## 2. 判别式平方类与 $p$ 的惰性

### 2.1 三以外的赋值为偶数

对 $q\ne3,p$，扩张 $H/\mathbb Q$ 在 $q$ 不分歧，因此 $I_q\subset G_H$。R258 §3 的实际角色计算给

$$\lambda(I_q)\subset\mu_6.$$

由于 $j(E_0)$ 整，惯性作用有限；其阶只含二、三素因子。模 $p$ 约化忠实，因为 $p>37$。因此最小好约化分歧指数 $e_q$ 整除六。

取使曲线好约化、分歧指数为 $e_q$ 的局部扩张；有限惯性商的 Frobenius 截面构造可按 R251 引理 251.4 选取这样的全分歧扩张。好约化判别式的赋值为零，模型缩放只改变十二的倍数，所以

$$12\mid e_qv_q(\Delta_E).$$

这里可先取局部极小模型；不同有理模型的差仍为十二的倍数。因为 $e_q\mid6$，得到

$$2\mid v_q(\Delta_E)\qquad(q\ne3,p). \tag{263.7}$$

此论证包括 $q=2$，但并不声称二挠点表示在二处不分歧。

在 $p$ 处，实际小惯性 $\rho_{E,p}(I_p)=C^3$ 的局部分类给好约化分歧指数为三或六；这是 R258 §6 所使用的同一个结论。因此同一判别式缩放论证给

$$2\mid v_p(\Delta_E). \tag{263.8}$$

### 2.2 三处平方类确实分歧

$H/\mathbb Q$ 在三分歧，故存在 $\tau\in I_3$ 的模 $p$ 像位于 $N_{\rm ns}(p)\setminus C$。因 $p\ne3$，行列式在 $I_3$ 平凡。非分裂 Cartan 正规化子的外陪集元素迹为零，所以

$$\rho_{E,p}(\tau)^2=-I.$$

在好约化特殊纤维的有限自同构群上，模 $p$ 作用忠实；故该惯性自同构本身的平方是 $[-1]$。在 $T_2(E_0)$ 上也就有

$$U^2=-I.$$

若 $U$ 模二为恒等，则 $U=I+2B$ 给 $U^2\equiv I\pmod4$，与 $-I\not\equiv I\pmod4$ 矛盾。故 $U\bmod2$ 是 $\operatorname{GL}_2(\mathbb F_2)\simeq S_3$ 中的非平凡二阶元，即换位。

三次二分多项式判别式的平方类等于椭圆曲线判别式的平方类，因此模二置换的符号角色正是 $\chi_{\Delta_E}$。上述换位说明 $F/\mathbb Q$ 在三分歧。因三是奇素数，

$$v_3(\Delta_E)\text{ 为奇数}. \tag{263.9}$$

合并 (263.7)–(263.9)，准确得到

$$\boxed{\Delta_E\in3\mathbb Q^{\times2}\ \cup\
-3\mathbb Q^{\times2},\qquad
F\in\{\mathbb Q(\sqrt3),H\}.} \tag{263.10}$$

由 $j-1728=c_6^2/\Delta_E$，有 $j-1728=\pm3r^2$，$r\in\mathbb Q$。若 $j$ 整，将 $r=a/b$ 约分后有 $b^2\mid3$，故 $b=1$，得到定理中的整数 $n$。

### 2.3 $p$ 在 $F$ 中惰性

在 $p>37$ 处，潜在好约化惯性阶为三或六；其模二像为三阶循环群。确切地，三部分不能落在 $\operatorname{GL}_2(\mathbb Z_2)\to\operatorname{GL}_2(\mathbb F_2)$ 的 pro-$2$ 核中；六阶时其中心 $[-1]$ 在模二被杀掉。

因此实际二挠点惯性包含一个三循环 $t$。这里惯性温和，算术 Frobenius 满足

$$\phi t\phi^{-1}=t^p=t^{-1},$$

因为 $p\equiv2\pmod3$。在 $S_3$ 中，反转三循环的元素恰为换位，所以模二 Frobenius 的符号为 $-1$。惯性本身符号为一，故 $F$ 在 $p$ 不分歧且

$$\boxed{\left(\frac{D_F}{p}\right)=-1.} \tag{263.11}$$

若 $p\equiv11\pmod{12}$，则 $(3/p)=1$，排除了 $F=\mathbb Q(\sqrt3)$。这证明第 1 项。

## 3. 实二次预解式的奇偶迹障碍

假定 $F=\mathbb Q(\sqrt3)$。在固定域 $H$ 上令

$$\mu=\chi_F\circ N_{H/\mathbb Q},\qquad
\beta_2\text{ 为 }H(\sqrt[3]{d})/H\text{ 的非平凡三次角色}.$$

由于 $F\ne H$，$\mu$ 确为非平凡二次角色。实际 CM 二挠点域是

$$\mathcal L_2(A_d)=H(\sqrt[3]{d}), \tag{263.12}$$

因为二挠点的 $x$ 坐标满足 $x^3+d=0$，而 $-1$ 已是有理立方。由 $v_p(d)\in\{1,2\}$，$\beta_2$ 非平凡。

记 $C_\chi=3N\mathfrak f_\chi$。二次角色的拉回导子整除 $12\mathcal O_H$，故 $C_\mu\le432$。对 $\beta_2$，二处至多温和指数一，导子范数因子至多四；三处任意三次角色杀掉 $U_4=(U_2)^3$，范数因子至多 $3^4$。在所有 $q\ge5$，分歧支撑恰为 $q\mid pc$，且温和指数为一。因此

$$C_{\beta_2}\le 2^2\,3^5(pc)^2,\qquad
C_\mu C_{\beta_2}\le2^6\,3^8(pc)^2. \tag{263.13}$$

取

$$Q=2^6\,3^8(pc)^2$$

并删去 $6pc$ 上方的全部素理想；其范数乘积至多 $(6pc)^2\le Q$。R251 定理 251.3 的联合 Euler 检测给一个剩余素理想 $\mathfrak q$，满足

$$\mu(\mathfrak q)=-1,\qquad\beta_2(\mathfrak q)\ne1,\qquad
N\mathfrak q\ll_\epsilon(pc)^{3/4+\epsilon}. \tag{263.14}$$

若底下的有理素数在 $H$ 惰性，其范数是平方且 $\mu(\mathfrak q)=1$；所以 (263.14) 强迫

$$N\mathfrak q=q,\qquad q\equiv1\pmod3,\qquad
\chi_F(q)=-1,\qquad q\nmid6pc.$$

两曲线均在 $q$ 好约化。在 $E_0[2]$ 上，Frobenius 的符号为负，故为换位，矩阵迹为零；在 $A_d[2]$ 上，它位于非平凡三阶子群，矩阵迹为一。因此整数迹满足

$$a_q(E_0)\equiv0\pmod2,\qquad a_q(A_d)\equiv1\pmod2. \tag{263.15}$$

另一方面，(263.3) 给两个整数迹模 $p$ 相同。若 $q<p^2/16$，Hasse 界给

$$|a_q(E_0)-a_q(A_d)|\le4\sqrt q<p,$$

所以两者完全相等，与 (263.15) 矛盾。故

$$p^2/16\le q\ll_\epsilon(pc)^{3/4+\epsilon}.$$

对任意 $\delta>0$ 适当缩小 $\epsilon$，得到

$$\boxed{c\gg_\delta p^{5/3-\delta}.} \tag{263.16}$$

这里二次角色处于固定域且自身也固定，所有变化导子只在实际三次角色及删去的坏集合中。R251 的有效常数和坏 Euler 乘子估计原样适用。

## 4. 同一虚二次预解式下的二挠点域检测

现在假定 $F=H$。由 §2.3，模二全局像含三循环；又因其符号角色 $\chi_H$ 非平凡，模二像准确为 $S_3$。因此

$$\alpha_2\text{ 为 }\mathcal L_2(E_0)/H\text{ 的非平凡三次角色}$$

定义良好。如果 $\mathcal L_2(E_0)\ne\mathcal L_2(A_d)$，则 $\alpha_2,\beta_2$ 线性独立。

对所有 $q\ge5,q\ne p$，实际 $p$ 挠点同构忠实识别两曲线的有限惯性像。由 (263.4)，当 $q\nmid c$ 时两曲线好约化；当 $q\mid c$ 时其惯性阶为三或六。模二保留其三部分而杀掉标量负一，所以 $\alpha_2,\beta_2$ 在这些地方同为温和分歧、指数一。$p$ 处也同为温和三次分歧。

因此，除二、三外，它们有同一个分歧支撑

$$q\mid p\,c^{(6)},\qquad
c^{(6)}=c/(2^{v_2(c)}3^{v_3(c)}).$$

在任一这样的素理想处，三条角色

$$\beta_2,\qquad\beta_2\alpha_2,\qquad
\beta_2\alpha_2^2$$

中恰有一条不分歧、另两条导子指数为一。这就是 R261 §3 的同一个局部导子抵消，给出准确的二、三以外导子范数乘积

$$\prod_{j=0}^2N\mathfrak f_{\beta_2\alpha_2^j}^{(6)}
=(pc^{(6)})^4. \tag{263.17}$$

二处不必假定 $\alpha_2,\beta_2$ 有相同分歧。$H_2/\mathbb Q_2$ 不分歧，而每条角色阶三，所以它们及所有乘积至多温和、导子指数一；三因子合计范数至多 $4^3=2^6$。三处每条的导子指数至多四，合计至多 $3^{12}$。包括判别式因子后，

$$C_{\alpha_2}^2\le2^4\,3^{10}(pc)^4,\qquad
\prod_{j=0}^2C_{\beta_2\alpha_2^j}
\le2^6\,3^{15}(pc)^4. \tag{263.18}$$

取 $Q=2^6\,3^{15}(pc)^4$，仍删去 $6pc$ 上方全部素理想。R261 引理 261.1 给

$$\alpha_2(\mathfrak q)=1,\qquad
\beta_2(\mathfrak q)\ne1,\qquad
N\mathfrak q\ll_\epsilon(pc)^{3/2+\epsilon}. \tag{263.19}$$

$H$ 中惰性的有理素数在实际 CM 的 $S_3$ 群中为换位；其平方在 $H$ 上恒为一。因此 $\beta_2(\mathfrak q)\ne1$ 强迫 $N\mathfrak q=q$、$q\equiv1\pmod3$。此时 $\alpha_2(\mathfrak q)=1$ 表示 $E_0[2]$ 的 Frobenius 是恒等矩阵，其迹为零；$\beta_2(\mathfrak q)\ne1$ 表示 $A_d[2]$ 的 Frobenius 为三循环，其迹为一。再用同一个 Hasse 比较，

$$p^2/16\le q\ll_\epsilon(pc)^{3/2+\epsilon}$$

便得

$$\boxed{c\gg_\delta p^{1/3-\delta}.} \tag{263.20}$$

合并 (263.16)、(263.20) 和 R261 的三除法异域二择一，证明 (263.5)–(263.6)。

## 5. 双同域条件的准确有理正规形

### 5.1 实际二挠点域相同给出的全部模型

令 $\theta^3=-d$。因为 $d$ 在 $p$ 的赋值为一或二，$x^3+d$ 不可约，其分裂域的 Galois 群为 $S_3$。

如果 $\mathcal L_2(E_0)=\mathcal L_2(A_d)$，两个三点上的传递 $S_3$ 作用相同至共轭；所有阶二子群共轭。因此可以选择 $E_0$ 的一个非零二挠点，使其 $x$ 坐标所在的三次子域就是 $\mathbb Q(\theta)$。

取 $E_0$ 的有理短模型 $y^2=x^3+Ax+B$。其选定二分根 $r$ 的迹为零；$\operatorname{Tr}(\theta)=\operatorname{Tr}(\theta^2)=0$，所以存在 $a,b\in\mathbb Q$ 使

$$r=a\theta+b\theta^2.$$

三个共轭根的平方和为 $-6abd$，乘积为 $-d(a^3-db^3)$。由根与系数关系，得到准确模型

$$\boxed{E_{a,b}:y^2=x^3+3abd\,x+d(a^3-db^3).} \tag{263.21}$$

直接计算其判别式及 $j$ 得

$$\boxed{
\Delta(E_{a,b})=-432d^2(a^3+db^3)^2,\qquad
j(E_{a,b})=\frac{6912d\,a^3b^3}{(a^3+db^3)^2}.
} \tag{263.22}$$

非奇异条件恰为 $a^3+db^3\ne0$。反之，任取满足该条件的有理 $a,b$，$r=a\theta+b\theta^2$ 非有理，否则 $1,\theta,\theta^2$ 的线性独立性给 $a=b=0$；其三次最小多项式就是 (263.21) 的二分多项式，故分裂域确为 $\mathcal L_2(A_d)$。

所以 (263.21) 是实际同一二挠点域的完整有理模型族，不是仅凭判别式平方类相同得到的必要条件。

### 5.2 再加入实际三除法商域相同

令

$$s=a^3+db^3\ne0,\qquad \Delta_A=-432d^2.$$

(263.22) 给 $\Delta_E/\Delta_A=s^2$。R261 的实际 Kummer 描述及有理立方类的单射性给

$$\mathcal L_3(E_{a,b})=\mathcal L_3(A_d)
\iff
\Delta_E\in\Delta_A\mathbb Q^{\times3}
\ \cup\ \Delta_A^2\mathbb Q^{\times3}. \tag{263.23}$$

第一种情形等价于 $s^2\in\mathbb Q^{\times3}$，也即 $s\in\mathbb Q^{\times3}$。第二种等价于 $s^2/\Delta_A\in\mathbb Q^{\times3}$；在指数三的立方类群中取平方逆，得

$$s\in\Delta_A^2\mathbb Q^{\times3}
=4d\,\mathbb Q^{\times3}.$$

于是准确得到 (263.1) 的两条三次曲线。反向每一步均可逆；而 $\Delta_A$ 的立方类非平凡，故这确实是同一个非平凡 $S_3$ 商域，不会因选到立方判别式而退化。

两条三次曲线给出的 $j$ 公式分别为

$$
\begin{array}{c|c}
\text{三次曲线}& j\\ \hline
a^3+db^3=z^3&
4d\left(\dfrac{12ab}{z^2}\right)^3\\[4pt]
a^3+db^3=4dz^3&
2d^2\left(\dfrac{6ab}{dz^2}\right)^3 .
\end{array}
\tag{263.24}
$$

这逐式恢复 R261 的两个立方形，并额外把同一二挠点域的实现条件完全写出。$a,b,z$ 同时乘以 $t\in\mathbb Q^\times$，会把 $E_{a,b}$ 换成其二次扭曲 $E_{a,b}^{(t)}$；它保持 $j$ 和这里的两个小除法域，只有 $t$ 为平方时才自动给有理同构。故在保留实际模 $p$ 同余时必须保留实际的仿射缩放代表，不能任意把二次扭曲遗漏。

第一条三次曲线总有 $(a:b:z)=(1:0:1)$，对应 CM 曲线 $A_d$；当 $d$ 含 $p$ 时，它没有 $a=0$ 的非奇异有理点。第二条没有 $ab=0$ 的非奇异有理点，因为那将强迫 $4$ 或 $4d$ 为有理立方。这些事实不能排除其余有理点。

## 6. 使用范围与继续所需的输入

本结果把两个独立的真实小除法域同时接到同一个 CM 参考上，所有导子均是 R258 的实际 $c$；未引入一个可以自由调整的辅助三次域。

若能证明一族实际输入中的 $c$ 有绝对上界，则 (263.5) 只留下有限个 $p$；其余必须落在 (263.1)。然而一般情形没有这样的 $c$ 上界。即使 $c$ 固定，(263.1) 的参数 $d$ 仍含 $p$，两条三次曲线也仍随 $p$ 变化。排除这些曲线的所有非 CM 有理点，或者把实际模 $p$ 同余、局部指数、整 $j$ 进一步用于这些方程，才会消去当前同域分支。

## 来源与依赖

- **R258**：真实六次 CM 下降、同一个全局二次扭曲、准确 $p$ 指数、有限惯性识别、全部导子及支撑。
- **R261**：实际三除法 $S_3$ 商的 Kummer 描述、固定 $H$ 三角色 Euler 检测引理、温和三因子导子抵消。
- **R251**：固定 $H$ 二次–三次联合 Euler 检测、所有删去的 Euler 因子、有效非实 $L(1)$ 下界及 Frobenius 截面好约化扩张。
- **Yang**, *Relative trace formula and twisted $L$-functions: the Burgess bound*, Compositio Math. **162** (2026), 2591–2641, Corollary 1.2；DOI [10.1017/S0010437X26103327](https://doi.org/10.1017/S0010437X26103327)。只经 R251/R261 已证明的固定域检测引理使用，未要求变化判别式的一致常数。
- **Thorner–Zaman**, *A unified and improved Chebotarev density theorem*, Algebra Number Theory **13** (2019), 1039–1068, Theorem 3.1；[原文 PDF](https://msp.org/ant/2019/13-5/ant-v13-n5-p02-p.pdf)。只用于同上检测引理中的非实角色有效 $L(1)$ 下界。

本文的新增局部群论、奇偶迹矛盾、全部导子因子和有理模型恒等式均已在正文证明。没有额外数值数据或验证脚本。
