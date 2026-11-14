# 固定椭圆伸缩差分解：代数化定理的精确输入

日期：2026-11-12。状态：**下述算子、共振与局部反例均已证明；
由额外 Selmer 余秩推出全局代数化的路线尚未闭合。**

本文只研究固定 $a=69$ 的差分方程，不重复 R14 的直接椭圆指数叶。
新增的代数函数障碍另已完整登记为 R28。

## 1. 形式解与真正需要的结论

令 $z=\log_E(t)$、$q(z)=\log\Phi(\exp_E z)=\sum_{k\ge2}b_kz^k$。
R19 给出 $q(0)=q'(0)=0$。对 $m\ge1$，设
$$
H_{m,c}(z)=cz+\sum_{k\ge2}\frac{b_kz^k}{(a^k-a)^m},
\qquad F_{m,c}(t)=\exp H_{m,c}(\log_E t).
\tag{1}
$$
则 $\mathcal D_a^mF_{m,c}=\Phi$，其中
$\mathcal D_aF=(F\circ[a])/F^a$。
R28 已证明每个这样的 $F_{m,c}$ 都在 $\overline K(E)$ 上超越。
因此路线的正向任务确实可以仅为“证明某个 $F_{m,c}$ 代数”，
无须再把代数解加强为 $E$ 上的有理解。

反设目标初级部分对几乎所有分裂 $p$ 均无限，已知控制与奇偶性给
目标字符上的 $\operatorname{ord}_{T=p}H_p\ge4$。
以下检查这一假设距离 (1) 的全局代数化还有什么。

## 2. 可以准确引用的代数化工具

已直接核对 J.-B. Bost、A. Chambert-Loir，
*Analytic curves in algebraic varieties over number fields*，
[arXiv:math/0702593v3，2008](https://arxiv.org/abs/math/0702593v3)：

- Definition 3.7（印刷页 13）：A-analytic 要求各处解析，且形式曲线
  在有限处的大小满足 $\sum_v-\log S_v<\infty$。
- Theorem 6.1（页 38）：A-analytic 加上典范切线度数严格为正，推出代数性。
- Theorem 7.9（页 48–49）：在任意光滑射影曲线上，形式函数若在适配
  adelic tube 上亚纯延拓、图像 A-analytic 且容量切线度数严格为正，
  则函数有理。图像在 $\mathcal O_K[1/N]$ 上整地延伸是其充分条件。

原文页 14 特别区分大小与收敛半径：$\log(1+t)$ 在每个 $p$ 处的
收敛半径都是一，但图像大小为 $p^{-1/(p-1)}$，并非 A-analytic。
所以逐 $p$ 正半径、甚至全部局部半径等于一，都不能替代大小的可求和性。

R28 允许直接使用 Theorem 6.1；若只构造大复圆盘上的参数化，
不必先证明它在 $E(\mathbb C)$ 的像上成为单值函数。
但 Theorem 6.1 的 A-analytic 和正度数两个假设仍须各自证明。

也核对 Bost、F. Charles，
*Quasi-projective and formal-analytic arithmetic surfaces*，
[arXiv:2206.14242v2，2022](https://arxiv.org/abs/2206.14242v2)，
§§0.2.1、0.3.1、Corollary 0.3.2。
该处的形式部分为整形式算术曲面；例如向 $\mathbb A^1_{\mathbb Z}$
的映射要求整级数，伪凹条件再给代数化。
它没有将这里所缺的全部有限处整性替换为一个 tame 字符的整性。

## 3. 固定 $a$ 的小除数与额外 tame 共振

设 $p\nmid a$ 为奇素数，置
$$
d_p=\operatorname{ord}_{\mathbb F_p^\times}(a),\qquad
c_p(a)=v_p(a^{d_p}-1)=v_p(a^{p-1}-1).
$$
对 $k\ge2$，提升指数引理给出精确公式
$$
v_p(a^k-a)=
\begin{cases}
0,&d_p\nmid k-1,\\
c_p(a)+v_p((k-1)/d_p),&d_p\mid k-1.
\end{cases}
\tag{2}
$$
第二式中的 $d_p$ 素于 $p$。特别地，对每个固定 $p$，这些赋值是
$O_p(\log k)$；这并不控制常数 $c_p(a)$ 随 $p$ 的变化。

在普通素数处写
$$
a=\omega(a)\langle a\rangle,
\qquad r_p=\frac{\log\langle a\rangle}{\log(1+p)}\in\mathbb Z_p.
$$
在 tame 字符 $\omega^j$ 的分量，$\sigma_a-a$ 对应
$$
s_{a,j}(T)=\omega(a)^j(1+T)^{r_p}-a.
\tag{3}
$$
若 $\omega(a)^{j-1}\ne1$，它是 $\Lambda=\mathbb Z_p[[T]]$ 的单位。
若 $\omega(a)^{j-1}=1$，则它在 $T=p$ 为零。
后者等价于 $d_p\mid j-1$，可能包含多个 $j$。
本题的秩和 Selmer 假设只控制 $j=1$，不控制其他共振块的中心零阶。
因此不能把“目标 $\chi$ 块可除”替换成整个固定 $F_{m,c}$ 的整性。

这里的困难不只是权重写法：式 (2) 在所有 $k\equiv1\pmod{d_p}$
产生小除数，而本题输入只落在 $k\equiv1\pmod{p-1}$。
两类在 $d_p<p-1$ 时通常不同。

## 4. Wieferich 商是额外的特征因子，不能当作常数处理

仍在共振块 $\omega(a)^{j-1}=1$ 中，令
$$
s=c_p(a)-1\ge0,
\qquad r_p=p^s u,\quad u\in\mathbb Z_p^\times,
\qquad Y=\frac{T-p}{1+p}.
$$
变换 $T\leftrightarrow Y$ 为 $\mathbb Z_p$ 完备局部代数同构。
由于
$$
s_{a,j}(T)=a\bigl((1+Y)^{p^su}-1\bigr),
$$
并且 $((1+Z)^u-1)/Z$ 的常数项 $u$ 为单位，可得
$$
s_{a,j}(T)\sim (1+Y)^{p^s}-1
=Y\prod_{h=1}^{s}\Phi_{p^h}(1+Y),
\tag{4}
$$
其中 $\sim$ 表示相差 $\Lambda$ 单位，$\Phi_n$ 是第 $n$ 个圆分多项式。
因此
$$
\frac{s_{a,j}(T)}{T-p}\in\Lambda^\times
\quad\Longleftrightarrow\quad c_p(a)=1.
\tag{5}
$$
当 $c_p(a)>1$ 时，中心之外还出现有限阶野分歧字符的零点。
除去 $T-p$ 后的商的 $\lambda$ 为 $p^{c_p(a)-1}-1$，$\mu=0$。
虽然其中心值的赋值是 $c_p(a)-1$，**该商不是一个可统一约去的
常数 $p^{c_p(a)-1}$**。
只知道 $H_p$ 在中心有四重零，不保证它被这些额外因子整除。

式 (4) 的证明完全是上述形式幂级数恒等式；没有假设某个
非 Wieferich 素数集合有限或无限。

## 5. 四次除法的线性共振：一个具体局部反例

即使暂时只看目标字符，并额外假设 $c_p(a)=1$，还不能无条件把
四次局部商与式 (1) 中 $c=0$ 的形式函数认同。
算子 $\sigma_a-a$ 消灭 $z=\log_E(t)$，所以形式解的线性系数自由。
局部 Coleman 商则选择了一个特定的 $\operatorname{CW}_1$ 值。

以下例子准确展示这一点。固定一个本题的非异常普通素数。
取 R24 的目标字符 Coleman 单位基 $u(t)\in1+t\mathbb Z_p[[t]]$，
其
$$
c=\delta\log u(O)\in\mathbb Z_p^\times.
$$
它可由 R24 的 $\beta-X(t)$ 取非平凡 $\chi$ 投影得到；
投影消掉常数项，并保留单位的第一 Coates–Wiles 值。
令 $R_p(t)=\mathcal D_a^4u(t)$。若 $c_p(a)=1$，
这个局部范数系统的 $\chi$ 特征系数恰含四个中心因子，商为单位。
例如 $a=69,p=13$ 满足此附加条件，因为
$69^6\equiv53\pmod{169}$。

具有零线性对数系数的形式解是
$$
F_0(t)=u(t)\exp(-c\log_E(t)),
\qquad \mathcal D_a^4F_0=R_p.
\tag{6}
$$
但 $F_0\notin\mathbb Z_p[[t]]$。

**证明。** 令 $A\in\mathbb F_p^\times$ 为 R24 的 Hasse 标量，
使 $\delta^p=A\delta$ 在约化形式群上成立；非异常性给 $A\ne1$。
若 $v\in\mathbb Z_p[[t]]^\times$，置 $\ell=\delta v/v$。
Bell 多项式的模 $p$ 恒等式给
$$
\delta^{p-1}\ell=A\ell-\ell^p,
$$
所以在原点有
$$
\delta^p\log v(O)\equiv(A-1)\delta\log v(O)\pmod p.
\tag{7}
$$
式 (6) 给 $\delta\log F_0(O)=0$，但 $p\ge2$ 时
$\delta^p\log_E(t)=0$，因而
$$
\delta^p\log F_0(O)=\delta^p\log u(O)
\equiv(A-1)c\not\equiv0\pmod p.
$$
这与假设 $F_0$ 整后可用的 (7) 矛盾。$\square$

此例只否定“局部四重中心因子自动给零线性系数解整性”的逻辑；
$R_p$ 是为此构造的局部 Coleman 输入，没有被冒充为本题固定的有理函数 $\Phi$。

若改为除三次，则有一个实质改善：在目标块中，
$H_p\in(T-p)^4\Lambda$ 和 (5) 给出整局部商
$H_p/s_{a,1}^3\in(T-p)\Lambda$，其 $\operatorname{CW}_1$ 为零。
因此它的形式对数与零线性系数解相容。
R28 对三次算子同样排除代数解，所以没有必要为使用 R28 坚持四次除法。
不过其他 tame 共振块、式 (4) 的额外因子以及非目标素数处仍未处理。

## 6. 可证明的收敛信息没有补齐全局假设

在每个固定有限处，$q(z)$ 有正收敛半径。
对 $p\nmid a$，式 (2) 的对数级增长说明除以 $(a^k-a)^m$
不改变这个 $z$ 坐标半径。对 $p\mid a$，当 $k\ge2$ 时
$v_p(a^k-a)=v_p(a)$，亦不改变半径。
形式 $\log_E$、$\exp_E$ 与通常指数在充分小圆盘内解析，
故每个 $F_{m,c}$ 在每个固定有限处都有某个正半径。

在复数处，如果 $q$ 的收敛半径为 $R>0$，则
$\lim_{k\to\infty}|a^k-a|^{1/k}=a$，所以 $H_{m,0}$ 的半径为 $a^mR$。
这给出复圆盘上的解析参数化
$z\mapsto(\exp_E z,\exp H_{m,0}(z))$。
但它没有计算典范度数的所有有限处贡献；圆盘很大时也不能默认
第二坐标在第一坐标的像上单值。

尤其，以上论证没有把 $t$ 坐标的图像大小提高为一，
没有给出 $\sum_v-\log S_v<\infty$，也没有控制惰性素数处。
因此本节的局部收敛论证本身不能给 Bost–Chambert-Loir 6.1
的完整输入。后续 [全平面参数化笔记](2026-11-12-difference-entire-uniformization.md)
已构造全 $\mathbb C$ 上的亚纯乘积，使无穷处的典范半范数为零；
一旦 A-analytic 成立，度数便为 $+\infty$。目前真正仍缺的是
全部有限处大小损失的可求和性。

## 7. 常见的 $q$-差分代数化定理为何不能直接替换

核对 L. Di Vizio、C. Hardouin，
*On the Grothendieck conjecture on p-curvatures for q-difference equations*，
[arXiv:1205.1692，2012](https://arxiv.org/abs/1205.1692)，
导言 Theorems 2–6 与 §1.2。
其对象是 $K(x)$ 上、底环自同构 $x\mapsto qx$ 的有限维线性差分模；
曲率判据涉及几乎所有相应有限处的整矩阵关系。

本题在 $K(E)$ 上的 $[a]^*$ 是像指数 $a^2$ 的非满嵌入，
不是该定理中的底域自同构。
改用 $z$ 虽使伸缩成为 $z\mapsto az$，却把右端改成
$\log\Phi(\exp_Ez)$，没有成为该定理所要求的有理函数系数差分模。
此外，即使 $a^{d_p}\equiv1\pmod p$，椭圆曲线上的
$[a]^{d_p}=[a^{d_p}]$ 仍不是恒等态射；其度数大于一。
不能把作用在切空间上的同余偷换成整个椭圆函数域上的有限阶作用。

本次核查留下了明确而较小的正向目标：可以尝试三次差分解，
但必须先对这个**固定、完整**形式图像证明可求和的有限处大小界；
后续全平面参数化已经解决复解析部分，仅补充单个 $\chi$ 块的
中心零阶仍不足以满足剩余输入。
