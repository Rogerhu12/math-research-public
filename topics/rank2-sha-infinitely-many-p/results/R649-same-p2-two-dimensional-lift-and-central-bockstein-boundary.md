# R649 — 同一 P2 的两维真实提升差与原第二中央必要式的界限

日期：2026-11-15。**状态：已证明。**

本篇支付一个严格的提升分辨：即使保留 R647 的同一个模 $p$ 有理
$P_2$、CM 型、原点首项、三挠零点和二挠极帽，这些资料仍不决定
原 $a_{34}/p,a_{72}/p$。
在这些完整模 $p$ 条件内存在一个显示的两参数整有理提升族；
它对两个除商的变化矩阵处处可逆。

该族不是原 sigma 允许自由变化的族。
原 sigma 及其微分方程选定唯一的实际 jet；本篇只说明
还必须使用这个实际模 $p^2$ 提升的额外条件，
不能从 R647 的模 $p$ Cartier 行和极帽自行消去原高位。

## 1. 完整保留的原模 p 对象

取
$$
p=6s-1>71,\qquad b=17,\qquad V=x^3,\qquad w=z^6,
$$
并保持 R647 的原 $E_b$、$D=d/dz$ 和 Gaussian
$$
c=[w^s]\log(\sigma/z),\qquad
\Theta^\circ=x\sigma^2e^{-2cw^s}.
\tag{1}
$$
令 $P_2$ 为 R647 的唯一实际有理解
$$
P_2=-(D-2G)^{p-1}Z^{p+1},\qquad \Theta_p=xP_2.
\tag{2}
$$
其全部局部、全局和曲率身份仍按 R647。
特别
$$
\Theta_p\in k(V),\quad \Theta_p(O)=1,\quad
(\Theta_p)_\infty\le M_p\mathcal D_2,\qquad
M_p=p^3-p^2+2p.
\tag{3}
$$
$\mathcal D_2$ 为三个非零二挠点之和。

还需明确其三挠零点。
$P_2$ 在 $x=0$ 的两点正则；它的 $\mu_6$ 型为二，且关于 $z$ 偶。
所以 $P_2=x^2R(V)$，其中 $R$ 在 $V=0$ 正则。
因此 $\Theta_p=VR(V)$ 在 $V=0$ 至少有单零。
令 $N=M_p/2$，可统一写成
$$
\boxed{
\Theta_p=\frac{V B_p(V)}{(V+b)^N},\qquad
B_p\in k[V],\quad \deg B_p=N-1,\quad
[V^{N-1}]B_p=1.
}
\tag{4}
$$
若实际极次较小，在分子中补相应 $(V+b)$ 幂即可。
(4) 同时保原点值、CM 型和全部极点支持。

取 $B_p$ 的任意首一整提升，得到
$\widetilde\Theta_0\in\mathcal O(V)$。
其分母、首项和 $V=0$ 零点都与 (4) 相容。
后文可以先将它的低有限 jet 调成原 $\Theta^\circ$ 的实际 jet。

## 2. 在同一极帽内的显示整变化

对 $j\ge1$ 置
$$
H_j(V)=\frac{V}{(V+b)^{j+1}}.
\tag{5}
$$
它在 $V=0$ 为零，在 $O$ 消失，型为零，
只在原 $\mathcal D_2$ 有极。
对本篇用到的 $j=s-2,s-1$，其极帽远小于 (3)。

定义同一个二参数族
$$
\boxed{
\widetilde\Theta_{\lambda,\mu}
=\widetilde\Theta_0
+p\{\lambda H_{s-1}+\mu H_{s-2}\},
\qquad \lambda,\mu\in\mathcal O.
}
\tag{6}
$$
所有成员都保持：

- 完整模 $p$ 有理函数 $\Theta_p$，不只是几个 Taylor 系数；
- 原点值一、型零、$V=0$ 零点和 (3) 的同一极帽；
- $\widetilde P_{2,\lambda,\mu}=\widetilde\Theta_{\lambda,\mu}/x$
  的型二、原点首项 $z^2$、只在 $\mathcal D_2$ 的极点；
- (2) 的全部模 $p$ 微分、曲率及 Cartier 身份。

最后一条只在模 $p$ 陈述。
(6) 没有被宣称满足原 sigma 的模 $p^2$ 方程。

### 2.1 可以从原实际有限 jet 起步

这不是因为随意选了一个与原来源无关的初始 jet。
由
$$
z^2x=1-\frac b7w+O(w^2)
$$
直接得
$$
H_j=w^j\left(1-\frac{4j+7}{7}bw+O(w^2)\right).
\tag{7}
$$
所以 $H_1,\ldots,H_{s-1}$ 在 $w,\ldots,w^{s-1}$ 上的系数矩阵
为单位上三角。
R647 的实际模 $p$ 比较保证
$\widetilde\Theta_0-\Theta^\circ$ 在这一窗口内被 $p$ 整除。
以 $pH_j$ 的整线性组合逐阶修正，可使
$$
\widetilde\Theta_0\equiv\Theta^\circ
\pmod{(p^2,w^s)}.
\tag{8}
$$
这些修正仍保 (3)、(4) 的全部全局条件。
此后固定这个初始提升，只有 (6) 的两个显示方向在变化。

因此族中 $(\lambda,\mu)=(0,0)$ 的两个原第一对角确是实际
$a_{34},a_{72}$ 模 $p^2$。
其余成员只用于辨别模 $p$ 资料能决定什么，不被认作原 sigma 来源。

## 3. 两条原完整来源的精确一阶变化

使用 R647 的同一个完整 $P_S,P_T$，令
$$
R_S(V)=V^{-1}P_S(b/V),\qquad
R_T(V)=V^{-1}P_T(b/V).
$$
原实际去 Gaussian 来源分别为
$(\Theta^\circ)^{17}R_S$、$(\Theta^\circ)^{36}R_T$。
对 (6) 定义
$$
\widetilde A_{34,\lambda,\mu}
=\widetilde\Theta_{\lambda,\mu}^{17}R_S,\qquad
\widetilde A_{72,\lambda,\mu}
=\widetilde\Theta_{\lambda,\mu}^{36}R_T,
$$
$$
\widetilde a_{m,\lambda,\mu}
=[w^s]\widetilde A_{m,\lambda,\mu}.
\tag{9}
$$
表面上的 $V=0$ 分母仍准确消去，剩余 $x$ 幂分别是二、三。
所有这些系数在本窗口整。

完整原低展开给
$$
\Theta^\circ=1-\frac{2b}{15}w+O(w^2),\qquad
R_S=w-\frac{50b}{7}w^2+O(w^3),
$$
$$
R_T=w-\frac{554b}{7}w^2+O(w^3).
\tag{10}
$$
Gaussian 首项在 $w^s$，所以不改变这里显示的低阶。
因此
$$
\frac{A_{34}e^{-34cw^s}}{\Theta^\circ}
=w-\frac{974b}{105}w^2+O(w^3),
$$
$$
\frac{A_{72}e^{-72cw^s}}{\Theta^\circ}
=w-\frac{1760b}{21}w^2+O(w^3).
\tag{11}
$$

在模 $p$ 下 $s\equiv1/6$，(7) 对 $j=s-2$ 化为
$$
H_{s-2}=w^{s-2}\{1+(b/21)w+O(w^2)\}\pmod p.
\tag{12}
$$
而 $H_{s-1}$ 只须保其首系数一。
对 (9) 作真正的模 $p^2$ 二项式展开，
二次变化带 $p^2$，所以
$$
\boxed{
\begin{pmatrix}
(\widetilde a_{34,\lambda,\mu}-\widetilde a_{34,0,0})/p\\[1mm]
(\widetilde a_{72,\lambda,\mu}-\widetilde a_{72,0,0})/p
\end{pmatrix}
\equiv
\begin{pmatrix}
17&-\dfrac{17\cdot323b}{35}\\[2mm]
36&-\dfrac{36\cdot1759b}{21}
\end{pmatrix}
\begin{pmatrix}\lambda\\ \mu\end{pmatrix}
\pmod p.
}
\tag{13}
$$
例如第一行第二项是
$17(-974/105+1/21)b=-17\cdot323b/35$；
第二行同理。
这里使用原 $S/T$ 的完整低系数，不把两个提升方向分别配给两条来源。

显示矩阵的行列式准确为
$$
\boxed{
-\frac{228072b}{5}
=-\frac{2^3\cdot3\cdot13\cdot17\cdot43}{5}\,b
\in\mathcal O^\times.
}
\tag{14}
$$
当前 $b=17$、$p>71$，全部因子都是单位。
因此 (13) 对每个允许的 $p$ 都满秩，无需删额外素数集合。

## 4. 对原第二中央必要式的准确后果

R647 从原完整 $j_m=0$ 得到
$$
\overline{a_m}=0,\qquad
\mathcal T_{m,2}
=\bar\gamma_m\,\overline{a_m/p},\qquad
\gamma_m=pmc.
\tag{15}
$$
$\mathcal T_{m,2}$ 是同一模 $p$ $P_2$ 的实际 Cartier 行。
族 (6) 的全部模 $p$ 函数相同，所以这些 $\mathcal T_{m,2}$
以及前五个全部 Cartier 行保持不变。
原 Gaussian 常数也没有随族变化。

若原两首行均为零，则 (13)–(14) 表明：
在保上述完整模 $p$ 条件的整有理提升中，
两个数 $(a_{34}/p,a_{72}/p)\bmod p$ 可独立取任何指定值。
特别，对给定的两条 $\mathcal T_{m,2}$，
总有且仅有一组 $(\bar\lambda,\bar\mu)$ 使这两个构造提升满足 (15)。

这不是说原实际高位可以自由选择。
原 sigma 对应的是 (8) 所固定的实际 jet，
其是否恰好满足 (15) 仍是必须解决的算术问题。
(13) 只严格说明，单靠模 $p$ 全局 $P_2$、其 CM 型、极帽、
共同三挠零点和原 Cartier 值，不能排除 (15)。

若原某个首行已经非零，则原完整 Newton 尾直接给相应 $j_m\ne0$；
本篇不修改这个已付充分条件。
在首行失败的真实情形，下一步必须加入原 sigma 的模 $p^2$
方程、真实除法 cocycle 或等价的实际高位约束。
R624 的 $\mathfrak R_1,\mathfrak R_2$ 和 R647 的
$\mathscr B_{m,h}$ 不会因为 (14) 是单位而消失。

## 5. 范围

本篇新增的是一个完整、同源形式和同极帽下的两维提升差计算，
以及所有允许素数上的准确单位行列式。
没有把族 (6) 加入原全局来源格，没有给它们赋新算术中央零，
没有改变原 sigma 的规范，也没有声称原 $S/T$ 存在真正的自由形变。

它排除了用仅有模 $p$ 的共同有理替代自动决定两个原除商的步骤；
原完整中央矛盾仍须额外的、实际的模 $p^2$ 输入。

依赖：
[R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)；
[R636](R636-original-rational-cartier-return-for-two-critical-rows.md)；
[R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)；
[R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md)。
