# R673 — 原乘 p 分子的收缩方程与真实 sigma 模 p² 提升

日期：2026-11-15。**状态：已证明。**

本篇使用原乘 p 坐标的分子，而不是只用原 psi_p。
同一个 Θ=xσ² 的准确乘法身份给一个在原有限窗口内收缩四位
的方程。它唯一恢复原 canonical Θ 的全部模 p² 系数，
只需该分子的最高 p 个系数模 p⁴，以及显示的原形式对数。

这将 R649 的实际提升限制付成一个具体、无自由参数的条件：
保持模 p 的比较提升，若改变原高位，就不能继续满足同一乘法分子方程。
三条原 S/T/U 的真实第二中央类都由这同一个提升读取；
H^{-hp} 的全部第一 log 修正仍保留。

本篇没有证明这些第二类在无穷素数上至少一个非零。
新增的是实际高位的完整有限来源、整除性、唯一性和准确输入精度，
不是再给一组可以选择的提升参数。

## 1. 原规范、两个乘法多项式和完整有限窗口

保持
$$
p=6s-1>101,\quad d=p+1,\quad b=17,\quad
E_b:y^2=x^3+b,\quad D_zx=2y,\quad D_zy=3x^2,
$$
$$
u=x^{-1/2}=z+O(z^7),\qquad t=bu^6,\qquad
C(t)=(1+t)^{-1/2}=\sum C_nt^n,
$$
$$
H(t)=\sum_{n\ge0}\frac{C_n}{6n+1}t^n,\qquad z=uH(t).
\tag{1}
$$
u 的符号和原微分 dz=dx/(2y) 保持，特别
y=−u^{-3}(1+t)^{1/2}。

全篇先在准确有限环
$$
R=\mathcal O[t]/(t^p),\qquad I=tR,\qquad R_K=K[t]/(t^p)
\tag{2}
$$
中运算。I 不含常数项。原 R606 已付 H∈1+I；
若 6n+1 在 n<p 内被 p 整除，唯一指标 n=5s−1
的中央二项式恰有一个 p，抵消该分母。
全部有限 exp/log 的指标都小于 p，故所有所需阶乘和 log 除数为单位。

取标准原奇除法多项式 ψ_p，首项 p x^{(p²−1)/2}。
令
$$
\phi_p(x)=x\psi_p(x)^2-\psi_{p-1}(x)\psi_{p+1}(x),
\qquad
x([p]P)=\frac{\phi_p(x)}{\psi_p(x)^2}.
\tag{3}
$$
相邻偶除法多项式的两个 y 因子在 (3) 中相乘，
所以 φ_p 确是原整数 x 多项式，首项为 x^{p²}。

定义两个准确反转多项式
$$
\boxed{
Q_p(t)=u^{p^2-1}\psi_p(u^{-2}),\qquad
B_p(t)=u^{2p^2}\phi_p(u^{-2}),\qquad u^6=t/b.
}
\tag{4}
$$
原加权齐次性保证 (4) 是 t 的整多项式，系数中的 b 尺度已由 t 保留；
Q_p(0)=p，B_p(0)=1。
本篇只读取它们在 (2) 的实际截断，不改变原多项式。

为避免同旧 P2 有理替代混淆，B_p 始终专指 (4) 的乘法分子。
它不是 R647 的 Θ_p，也不是任意选择的 lift。

## 2. 真实乘 p 参数和四位收缩

记原形式乘法参数为 u_p=u(pz(u))，并令
$$
\varphi_p(t)=b\,u_p^6 .
$$
原 (3) 在 u=0 取首项 p u 的平方根，准确给
$$
\frac{u_p}{u}=\frac{Q_p(t)}{B_p(t)^{1/2}},\qquad
\boxed{\varphi_p(t)=t\,Q_p(t)^6B_p(t)^{-3}.}
\tag{5}
$$
平方根以常数项一规范；p≠2，故它在 R 中整且唯一。

在本截断里 u_p/u 被 p 整除。
例如原 supersingular height2 给 [p](u) mod p 从 u^{p²} 起，
而 6(p−1)+1<p²；本篇所用系数全在该端点之前。
也可从原 H 的整性和 u(z) 的整有限组合逆直接得到：
u(pz(u)) 的每个保留正次项都有 p 因子。
所以
$$
Q_p\in pR,\qquad
\boxed{\varphi_p\in p^6I,\qquad
       [t]\varphi_p=p^6.}
\tag{6}
$$
这里不把 Q_p 的全局最高端点称为被 p 整除；
(6) 只在显示的原 t^{<p} 窗口陈述。

定义 K 线性、一般不乘法的算子
$$
\mathcal F_p:I_K=tR_K\longrightarrow I_K,\qquad
\mathcal F_p(f)=p^{-2}f(\varphi_p(t)).
\tag{7}
$$
它是原乘 p 的实际组合拉回乘 p^{-2}，不是绝对 Frobenius，
也没有将系数另取 p 次幂。
由 (6)，对每个整数 a≥0，
$$
\boxed{
\mathcal F_p(p^aI)\subset p^{a+4}I.
}
\tag{8}
$$
证明只需逐项读 f=Σ_{n=1}^{p−1}f_n t^n：
第 n 项在组合后至少含 p^{6n}，除去 p² 后至少含 p⁴。
正是限制在 I 上，才有 (8)；常数项不能加入这个收缩断言。

因此 1−F_p 在 I 上整可逆，逆为
$$
\boxed{
(1-\mathcal F_p)^{-1}
=\sum_{a\ge0}\mathcal F_p^a,\qquad
\mathcal F_p^a(f)=p^{-2a}f(\varphi_p^{\circ a}(t)).
}
\tag{9}
$$
每项较前一次至少多四位，有限自由 O 模 I 的 p 进完备性
保证整系数一致收敛。

## 3. 原 Θ 的乘法身份和规范化完整分子

保持原 Weierstrass sigma，而非另选 Gaussian：
$$
D_z^2\log\sigma=-x,\qquad \sigma=z+O(z^7),\qquad
\Theta(t)=x(z(u))\sigma(z(u))^2.
$$
奇数 p 的同一原乘法式为
$$
\sigma(pz)=\psi_p(x(z))\,\sigma(z)^{p^2}.
$$
与 (3) 相乘，所有 psi_p 因子准确消去，得到
$$
\boxed{
\Theta(\varphi_p(t))=B_p(t)\,\Theta(t)^{p^2}.
}
\tag{10}
$$
这是特征零的原函数身份，随后才在 (2) 截断。
所有原挠点除子和标准首项都在 (3)、(10) 中，未另取一个 theta。

使用 R606 已付的 canonical 首 Gaussian
$$
c_b^\dagger=-\frac{b^sC_s}{p(p+1)},\qquad
\Theta^\dagger(t)=\Theta(t)
 \exp\{-2c_b^\dagger b^{-s}t^sH(t)^d\}.
\tag{11}
$$
它与原 c 的差是整数；对常数项为零的原 S/T/U，
完整 Newton 函数只乘一个解析单位，完整中央导数原样不变。
这里不把 c^dagger 认作原 σ 的 Taylor 系数。

R606 的同一整窗口给
$$
\Theta^\dagger\in1+I,\qquad
L_p:=\log\Theta^\dagger\in I.
\tag{12}
$$
确实 Θ^\dagger=(Λ^\dagger)^{1/3}，3 是单位，
且 exp/log 只在 t^{<p} 中进行。

原 z([p]P)=pz(P) 保证
$$
(t^sH^d)\circ\varphi_p=p^d t^sH^d .
$$
对 (10) 取有限 log，并保 (11) 的全部变化，得到
$$
p^2L_p-L_p(\varphi_p)
=-\log B_p
-2c_b^\dagger(p^2-p^d)b^{-s}t^sH^d .
\tag{13}
$$
因此定义完全由原乘法数据给出的
$$
\boxed{
\begin{aligned}
\mathcal N_p(t)
&=\log B_p(t)
-\frac{2pC_s}{p+1}(1-p^{p-1})t^sH(t)^{p+1},\\
G_p(t)&=-\,\mathcal N_p(t)/p^2 .
\end{aligned}
}
\tag{14}
$$
代入 (13) 恰给
$$
\boxed{(1-\mathcal F_p)L_p=G_p.}
\tag{15}
$$

**定理1。** (14) 的花括号是整体可除的：
$$
\boxed{\mathcal N_p\in p^2I,\qquad G_p\in I.}
\tag{16}
$$
且原真实规范化来源唯一地由
$$
\boxed{
L_p=\sum_{a\ge0}p^{-2a}G_p(\varphi_p^{\circ a}(t)),
\qquad \Theta^\dagger=\exp(L_p)
}
\tag{17}
$$
恢复。

证明：(12)、(8)、(15) 先证明 (16)，所以除 p² 合法。
随后 (9) 给 (17) 以及 I 内的唯一性。
这里用已经存在的原 σ 支付整除，再由同一数据和收缩证明唯一恢复；
没有先将两个可能只含一个 p 的项分别除 p² 后约化。证毕。

## 4. 四位分子给完整模 p²；准确的首个遗漏阶

由 (8)、(15)，
$$
\boxed{L_p-G_p\in p^4I.}
\tag{18}
$$
故对每个 1≤r≤4，
$$
\boxed{
\Theta^\dagger
\equiv\exp\left[
-\frac1{p^2}
\left\{\log B_p
-\frac{2pC_s}{p+1}t^sH^{p+1}\right\}
\right]\pmod{p^rR}.
}
\tag{19}
$$
(19) 省略的 p^{p−1} 项在除 p² 后有 p^{p−2}，
对当前 p>101 和 r≤4 确实不影响显示精度。
若要更高精度，使用 (14)、(17) 原完整式。

特别 r=2 的实际输入为：

| 原输入 | 所需精度及范围 |
|---|---|
| 乘法分子 B_p 的最高 p 个反转系数 | t^{<p}、模 p⁴ |
| 原 H(t) | t^{<p}、模 p³ |
| 原显式 C_s | 模 p³ |
| 原 p+1 的逆及常数规范 | 在同一环中准确取逆 |
| 合法除法 | 先用 (16) 证整体 p² 整除，再除 p² |

Q_p 不需要进入这个 r≤4 的恢复；它只在 (5)、(17)
更高精度的实际组合拉回中出现。
这与 R624 的四位 psi_p 接口有区别：
那里先除 psi_p 首项中的 p，再读取 log。
这里由 (10) 先准确消掉 psi_p，使用的是原坐标分子 B_p；
不是把同一数据的一个 p 分母漏算。

(18) 的四位界不能无条件提升。
从原低系数得到
$$
[t]L_p=-2/15,\qquad[t]\varphi_p=p^6 .
$$
因此
$$
\boxed{
[t](L_p-G_p)=-2p^4/15,\qquad
[t]B_p=\frac{2p^2}{15}(1-p^4).
}
\tag{20}
$$
对所有当前 p，第一式恰有赋值四。
这既核定 (13)–(19) 的符号，也指出第五位必须保真实拉回项。
(20) 的固定低系数单位不被当成原随 p 中央指标的非零证书。

## 5. 原三条来源全部前五块的真实两位值

保持 R647 的完整三个固定多项式 P_m(t)，
m=34,72,136，次数分别4、10、21，全部常数项一。
原精确身份是
$$
A_m e^{-mc_b^\dagger z^d}
=u^6(\Theta^\dagger)^{m/2}P_m(t).
\tag{21}
$$
记 (19) 在 r=2 恢复的实际类为
$$
E_p^{[2]}(t)=\Theta^\dagger(t)\bmod p^2R .
$$
这是同一个原提升；三个 m 不可分别选择它。

对 1≤h≤5 定义
$$
\boxed{
\mathfrak a_{m,h}^{[2]}
=b^{hs-1}[t^{hs-1}]
 (E_p^{[2]})^{m/2}P_m(t)\,
 C(t)H(t)^{-h-1}
 \bigl(1-hp\log H(t)\bigr)
\pmod{p^2}.
}
\tag{22}
$$
负幂用 H 的整逆，log 是原有限 log。
因为 hs−1<p，(22) 只用本篇已恢复的整个窗口。

**定理2。** (22) 准确给原 canonical 全块：
$$
\boxed{
\mathfrak a_{m,h}^{[2]}
\equiv [z^{h(p+1)}]\bigl(A_me^{-mc_b^\dagger z^{p+1}}\bigr)
\pmod{p^2},\qquad
m=34,72,136,\ 1\le h\le5.
}
\tag{23}
$$

证明：原留数换参给完整 Jacobian
$$
[z^{h(p+1)}]\bigl(A_me^{-mc_b^\dagger z^{p+1}}\bigr)
=b^{hs-1}[t^{hs-1}]
 (\Theta^\dagger)^{m/2}P_m\,C\,H^{-h(p+1)-1}.
\tag{24}
$$
在 (2) 中
$$
H^{-hp}\equiv1-hp\log H\pmod{p^2},
$$
其二次以上项都被 p² 整除，所有实际阶乘指数<p。
代入 (24) 和 E_p^[2] 就是 (22)。证毕。

因此 H^{-hp} 的修正不是从模型的模 p 式猜出的新高位；
它和 (19) 的真实高位来自同一个原 sigma/参数。
R624/R647 的全部低多项式卷积已在 P_m 中，不另删除残差。

## 6. 同一完整 j 的第二判据

令原首对角
$$
a_m=[z^{p+1}]A_m .
$$
因为 A_m(0)=0，Gaussian 不改变这个首对角，
故 a_m mod p² 正是 \(\mathfrak a_{m,1}^{[2]}\)。

置
$$
\gamma_m^\dagger=pmc_b^\dagger
=-\frac{m b^sC_s}{p+1}\in\mathcal O^\times .
$$
若 a_m∈pO，完整原 Newton 尾（R606/R614，U 用 R647）给
$$
\boxed{
\frac{j_m}{p^2}\equiv
(\bar\gamma_m^\dagger)^{-1}\overline{a_m/p}
-(\bar\gamma_m^\dagger)^{-2}
              \overline{\mathfrak a_{m,2}^{[2]}}
\pmod p .
}
\tag{25}
$$
这里 canonical j_m 与原物理中央导数准确相同；
三曲线的原 b 尺度及 U 的额外微分单位照 R303/R402/R469 保留。

所以可由 (19)、(22) 直接计算同一个实际第二类
$$
\boxed{
\Xi_{m,p}
=\overline{\mathfrak a_{m,2}^{[2]}}
-\bar\gamma_m^\dagger
 \left(\mathfrak a_{m,1}^{[2]}/p\bmod p\right).
}
\tag{26}
$$
在首行模 p 为零的前提下，最后的除 p 在 O/p² 中有唯一模 p 值。
若 Xi_m,p≠0，则原 j_m 赋值恰二；
由原完整通常 Selmer 桥得到对应固定曲线的初级有限。

若原三条中央全零，则三条首行模 p 与三条 (26) 必全零。
这不是将两条中央零免费传给第三条。
相反，三个实际值共享 (19) 的同一 B_p 和同一真实提升。

本篇虽然恢复前五个 g 块的模 p²，
却没有据此声称已恢复 j mod p⁶：
更深中央位还要求更早块的更高精度。
那些精度可用 (17) 和更深的同一原乘法数据继续读取，
不能从 (23) 的两位值自行补出。

## 7. R649 的比较提升为何不能保同一乘法方程

把实际模 p² 来源 E=Theta^dagger 改成
$$
\widetilde E=E(1+pV)\pmod{p^2},\qquad V\in I.
$$
其有限 log 的真实变化是 pV。
由 (8)，
$$
\boxed{
(1-\mathcal F_p)\log\widetilde E-G_p
\equiv pV\pmod{p^2R}.
}
\tag{27}
$$
因此一个非零模 p 的 V 不能仍满足原 (14)–(15) 的模 p² 方程。
这给出实际乘法数据所排除的明确高位，而不是只说提升唯一。

R649 的两个 H_{s−1},H_{s−2} 在原低窗口有不同的非零首阶，
除以模 p 的实际 Θ 仍线性独立。
在 t^{<s} 内原 c 与 c^dagger 两规范完全相同，
因为规范差从 z^{p+1} 才开始。
所以对该篇从实际低 jet 起步的两参数族，
任何非零参数对都会在 (27) 留下非零实际残差。
这并不否定该族保持全部模 p 有理条件；
它准确指出那些条件没有包含的原乘法分子高位。

(27) 使用真实 B_p 数据，因而也没有把 R649 的两个方向
加入原全局来源格，或给它们添加新的算术零。

## 8. 已完成与尚缺的接口

本篇完成了同一原来源的以下接口：

- 原乘 p 分子给准确 (10)，canonical Gaussian 给完整 (14)；
- 在原 t^{<p} 窗口，实际拉回是四位收缩，完整原提升由 (17) 唯一恢复；
- B_p mod p⁴ 给整个实际 Θ^dagger mod p²，
  全部除 p² 先有整除证明，首个遗漏阶恰在第五位；
- 三条原来源的前五块两位值和第二中央类
  由同一个提升、全部 H^{-hp} 修正及原完整 P_m 读取。

仍须证明：在无穷不同 p 上，至少一个原首行或实际 Xi_m,p 非零，
或者由更深的同源条目排除原三个 j 同时为零。
(14) 的整除、(17) 的唯一性和 (20) 的固定低系数本身都不支付该非零性。

本篇没有运行新的素数扫描；以上均为原乘法身份、有限整性与一般收缩证明。
也没有把原 p 依赖的乘法多项式加入一个免费的固定全局来源池。

主要依赖：
[R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md)；
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R624](R624-original-paired-forcing-determinant-and-four-digit-division-return.md)；
[R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)；
[R649](R649-same-p2-two-dimensional-lift-and-central-bockstein-boundary.md)。
标准乘法分子和 sigma 身份在本文 (3)、(10) 保全部原首项；
本篇不依赖新增的外部非消失定理。
