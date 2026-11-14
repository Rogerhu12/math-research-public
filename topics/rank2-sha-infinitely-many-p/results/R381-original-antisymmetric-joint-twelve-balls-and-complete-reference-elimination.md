# R381：原三输入的反对称加法、同层十二球与保持 R 的完整参考消去

日期：2026-11-14。**状态：已证明。** 本篇在 R379 同一三输入表示中，
证明一个完整的两来源联合分解。对任意 $N\ge49$，两个单位尺度中心
$t,2t$ 的原加法球矩阵在所有单位 $t$ 上均可整逆。
由此构造真正模 $p^N$ 局部常数的十二球权，逐点消去整个参考联合，
同时保持任意另一坐标 $R$ 的限制。
取 $t=Y$ 及 $R$ 的原点深球，所得整条原 Mellin 准确返回 $J_S$；
本篇没有把十二球缩成一个独立叶，也未删除 $Q\approx2\mu_6Y$ 的补域。

## 1. 同一原对象与固定素数族

保留 R379 的原 $E_{17}$、微分、周期和普通素数族：
$$
y^2=x^3+b,\quad b=17,\quad \delta^2=-3,\quad
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad\sigma=z+\cdots,
$$
$$
\Theta=x\sigma^2,\qquad
\pi=\psi_{17}(\mathfrak p),\quad
\kappa=p/\bar\pi^2,\quad\lambda=1/\bar\pi,\qquad
\int e^{zt/\Omega}\,d\nu_G(t)=G(z).
$$
当前固定无穷族为 R379 的
$\pi\equiv1\bmod5346432\mathcal O_K$。
原 $\Omega$ 是单位，所有来源、移权和测试都使用它。

记 $X=x^3$。原来源及三输入身份为
$$
A=\sigma(z)\sigma(2z)\sigma(\delta z)
  =-2\delta\sigma^8xy,
$$
$$
C=C_{18}=\sigma^{18}(X-8b)(X^2-4bX/7+16b^2/7),
\qquad S=-A^2C/12.
\tag{1}
$$
$A$ 的型为三、首项 $2\delta z^3$；$C$ 的型为零、质量一。
沿用原有界整测度
$$
d\eta_3=-\frac1{12}d\nu_A(a)d\nu_A(b_1)d\nu_C(c),\qquad
Y=a+b_1+c,\quad Q=a-b_1,\quad R=9(a+b_1)-8c.
\tag{2}
$$
$Y_*\eta_3=\nu_S$。R379 已付整个 $(Y,Q,R)$ 的三个 core；
特别 $Y,Q,R$ 每个单独的原点深度作用都保持另两坐标，标量为 $\lambda$。

本篇另用两个**明确的实际 degree 十六来源**
$$
\boxed{
D=\sigma^{16}x^2(X+b)=-A^2/12,\qquad
E=\sigma^{16}x^2(X^2-28b^2).
}
\tag{3}
$$
其中 $D=z^6+\cdots$、$E(0)=1$。
它们并不是新加入的秩二椭圆曲线。
真实整有界性也直接可见：
$$
D=\sigma^6\Theta^5+b\sigma^{12}\Theta^2,\qquad
E=\Theta^8-28b^2\sigma^{12}\Theta^2.
$$
R379 的整个 $\mathcal S_{16}$ 用同 degree 的 $\sigma(4z)$ 锚定，
所以两者都有完整原 core
$$
\boxed{\nu_D|_p=\lambda[\kappa]_*\nu_D,\qquad
       \nu_E|_p=\lambda[\kappa]_*\nu_E.}
\tag{4}
$$
没有用它们的质量来猜这个标量。

## 2. 完整反对称加法身份

令 $\mathsf P_u$ 表示只在 $u$ 上对 $\mu_6$ 平均，固定 $z$。
则准确有
$$
\boxed{
\mathsf P_u\{A(z+u)A(z-u)\}
 =12\{E(z)D(u)-D(z)E(u)\}.
}
\tag{5}
$$

**证明。** $A\in\mathcal S_8$，两个原自动因子的交叉项相消，
所以左边在 $z,u$ 各自属于真实 $\mathcal S_{16}$。
$A(\zeta z)=\zeta^3A(z)$，故同时旋转 $z,u$ 时总型零。
在 $u$ 上平均后，两个变量都为型零。
$\mathcal S_{16}$ 的型零空间准确是三维：
$$
F_0=\sigma^{16}x^2,\quad F_1=\sigma^{16}x^5,\quad
F_2=\sigma^{16}x^8.
\tag{6}
$$
其首阶为十二、六、零；没有额外 Gaussian 或平坦特征。

因为 $A$ 为奇函数，交换 $z,u$ 使左边变号；
同时型零又使在第一或第二变量平均相同。
所以它是 (6) 的完整反对称张量。
原 $z=0$ 边界为 $-A(u)^2=12D(u)$，其中
$D=F_1+bF_0$，这固定三个反对称参数中的两个。
第三个参数可用一个准确系数确定；这不是以有限样本外推整个身份。

为完整记录规范，原曲线方程给
$$
A=2\delta z^3
 \left(1+\frac{19b}{105}z^6
 -\frac{64676b^2}{1576575}z^{12}+\cdots\right),
$$
$$
D=z^6+\frac{38b}{105}z^{12}+\cdots,\quad
F_2=1-\frac{16b}{15}z^6+\frac{8656b^2}{17325}z^{12}+\cdots .
$$
若取 $E=F_2+\beta b^2F_0$，则 $z^6u^{12}$ 的准确比较是
$$
\begin{aligned}
\beta={}&
 \left(-\frac{16}{15}\right)\frac{38}{105}
 -\frac{8656}{17325}
 +728\left(-\frac{64676}{1576575}\right)
 +84\left(\frac{19}{105}\right)^2\\
={}&-28.
\end{aligned}
$$
其中 $728$ 来自 $(3,15)$、$(15,3)$ 两项，$84$ 来自 $(9,9)$；
完整正负号均保留。也可由
$\sigma=z+(b/210)z^7-(b^2/1801800)z^{13}+\cdots$
和原因子 $1,2,\delta$ 直接复核。
这确定整个三维反对称张量，证明 (5)。$\square$

## 3. 保持任意 R 的两来源联合

令 $u_0=a+b_1$。定义两个真实 $(Y,R)$ 联合：
$$
\eta_{DC}=(u_0+c,\,9u_0-8c)_*
                (\nu_D(u_0)\otimes\nu_C(c)),
$$
$$
\eta_{EC}=(u_0+c,\,9u_0-8c)_*
                (\nu_E(u_0)\otimes\nu_C(c)).
\tag{7}
$$
第一条的 $Y$ 边际为原 $\nu_S$；
第二条的边际为实际 $H=EC$，其质量一。
本篇不预设 $H$ 的完整中央导数已知。

若 $\mathcal J=(Y,R,Q)_*\eta_3$，则 (5) 给**整个**联合测度身份
$$
\boxed{
\mathsf P_Q\mathcal J
 =\eta_{DC}\otimes\nu_E-\eta_{EC}\otimes\nu_D.
}
\tag{8}
$$
其原符号可从 (2) 的 $-1/12$ 直接核对。
更明确，将 (5) 中 $z$ 替为 $z+9v$，再乘
$-C(z-8v)/12$，得到 (8) 的全部 $(Y,R,Q)$ 生成函数。
所以 (8) 保持任意原 $R$ 测试或限制，而不只在 $R=0$ 的变换上成立。
有界性和多变量矩唯一性给全部连续测试的测度式。

特别，忽略 $R$ 后
$$
\mathsf P_Q(Y,Q)_*\eta_3
 =\nu_S\otimes\nu_E-\nu_H\otimes\nu_D,\qquad H=EC.
\tag{9}
$$
下面消去的是 (8) 的整个 $\eta_{EC}$，因此其所有质量、tame、
中央斜率及与 $R$ 的相关项同时被消掉。

## 4. 同层加法球的真实单位行列式

对 $N\ge1$ 和 $t\in\mathbf Z_p^\times$ 写
$$
d_N(t)=\nu_D(t+p^N\mathbf Z_p),\qquad
e_N(t)=\nu_E(t+p^N\mathbf Z_p).
$$
这两个函数都只依赖 $t\bmod p^N$，且为 $\mu_6$ 不变。

$D=-A^2/12$ 的零除子全部在固定二、三挠点，包含原点六阶零。
R376 的原整小球公式与 (4) 因而给
$$
\boxed{d_N(t)\in\mathcal O^\times\quad(t\text{ unit},\,N\ge1).}
\tag{10}
$$
$E$ 是质量一的实际整 degree 十六截面；
同一证明也给 $e_N(t)$ 在 $N>16$ 时为单位。

更重要的是两者**同 degree、同 core、同原周期**。
R376 的 division 因子、完整 Fourier 的 $p^{-N}$ 及 $\lambda^N$
在球比中全都准确相消。
若 $q_t\in E[\bar\pi^N]$ 是 R376 的原标签，
$P_t=[\pi^N]q_t$，则
$$
\boxed{
\frac{e_N(t)}{d_N(t)}
 =\mathfrak r(P_t),\qquad
\mathfrak r(P)=\frac{X(P)^2-28b^2}{X(P)+b}.
}
\tag{11}
$$
$t\mapsto q_t$ 是同一个 degree 十六的加法标签，因此
$P_{2t}=2P_t$；这里使用的是整数二，不涉及另一个 CM 标签方向。

原有理差
$$\mathfrak r(P)-\mathfrak r(2P)$$
在每个 $p>17$ 的当前好约化上非零，极总阶准确为四十八。
详细地：

- 在 $O$ 的极阶为六，首差是 $(1-2^{-6})z^{-6}=63z^{-6}/64$；
- 另三个二挠点各有六阶极，来自 $\mathfrak r(2P)$；
- 其余十二个四挠点各有二阶极，来自二倍后的非零二挠极。

这些 prime-to-$p$ 点在好约化中仍互异，所列主项均为单位。
原 $\mathfrak r$ 在非零二挠点的分子是 $-27b^2$，所以没有隐藏的消极。
因此其约化仍为非零有理函数，零除子 degree 为四十八，
且定义在 $\mathbf F_p$ 上。

若单位 $t$ 对应的精确阶 $p^N$ 点 $\bar P_t$ 是一个零点，
它在某个 $\mathbf F_{p^e}$ 上有定义，$e\le48$；
于是 $p^N\mid\#E(\mathbf F_{p^e})<p^{e+1}$，迫 $N\le48$。
它又不可能落在上述 prime-to-$p$ 极点上。
所以
$$
\boxed{
N\ge49\quad\Longrightarrow\quad
\mathfrak r(P_t)-\mathfrak r(2P_t)\in\mathcal O^\times
\quad\text{对全部单位 }t.
}
\tag{12}
$$

定义同层行列式
$$
\boxed{
\Delta_N(t)=e_N(t)d_N(2t)-e_N(2t)d_N(t).
}
\tag{13}
$$
(10)–(12) 完整证明
$$
\boxed{\Delta_N(t)\in\mathcal O^\times
       \quad(N\ge49,\ t\text{ unit}).}
\tag{14}
$$
这没有用数值素数样本，亦没有只从有限矩阵可逆猜测整逆。

## 5. 真正十二球权与逐点参考消去

固定 $N\ge49$。对单位中心 $t$ 置
$$
\chi_N(Q;t)=\frac16\sum_{\zeta\in\mu_6}
                       1_{\{Q-\zeta t\in p^N\}} .
\tag{15}
$$
六个球两两不交。两个尺度 $t,2t$ 的六球族也互不相交：
否则 $2^6-1=63$ 将被 $p$ 整除，而本篇 $p>17$。
这个归一是六球平均；不能在后文忘掉 $1/6$。

现在定义实际权
$$
\boxed{
W_N(Q;t)=
\frac{d_N(2t)\chi_N(Q;t)-d_N(t)\chi_N(Q;2t)}
     {\Delta_N(t)} .
}
\tag{16}
$$
它的支撑准确是上述十二个单位球。
在各球上的非零值都是单位；它在 $(Q,t)$ 上模 $p^N$ 局部常数。
逆矩阵没有引入一个更细而未声明的局部常数层。
它对 $Q$ 的 $\mu_6$ 作用不变，所以可直接用于原 $\mathcal J$，
而不仅用于已经平均后的测度。

由完整球值，两个系数准确为
$$
\boxed{\int W_N(Q;t)\,d\nu_E(Q)=1,\qquad
       \int W_N(Q;t)\,d\nu_D(Q)=0.}
\tag{17}
$$

**保持部分输出的完整返回。** 设 $\mathcal B$ 是任意原 $(Y,R)$ 域，
$t(Y,R)$ 在其上是一个连续单位中心函数。
将 (8) 与 (17) 逐点应用，得到
$$
\boxed{
(\operatorname{pr}_{Y,R})_*
 \left(1_{\mathcal B}W_N(Q;t(Y,R))\,\mathcal J\right)
 =1_{\mathcal B}\eta_{DC}.
}
\tag{18}
$$
这里所有乘法和推前都在同一 $(Y,R,Q)$ 联合上。
函数依赖 $Y$ 并不是被免费移出一个中央积分：
(18) 来自两个实际系数在每个 $(Y,R)$ 上分别为一和零。
有限层局部常数测试先直接给该式，再由有界性给所有连续测试。
特别，未知参考 $\eta_{EC}$ 在取任何 Mellin 之前已经完全消失。

## 6. 原中央零真正能够传播的移动球域

取 $t(Y,R)=Y$ 并限制 $Y$ 为单位。
由 R379 的完整 $R$-core，
$$Y_*(1_{\{R\in p^m\}}\eta_{DC})=\lambda^m\nu_S.$$
故对任意 $m\ge0$，
$$
\boxed{
Y_*\left(
 1_{\{Y\ {\rm unit},\,R\in p^m\}}
 W_N(Q;Y)\mathcal J
\right)
=\lambda^m\nu_S^\times .
}
\tag{19}
$$
$R$ 的深度 $m$ 与球矩阵深度 $N$ 不必相同。
若 $R$ 改为精确环带 $v_p(R)=m$，右边另乘 $1-\lambda$。

因此，保留原全部 tame，
$$
\boxed{
\int_{\{Y\ {\rm unit},R\in p^m\}}
 W_N(Q;Y)\,
 \omega_p(Y)^\ell\langle Y\rangle^{(p-1)u}\,d\mathcal J
=\lambda^m J_{S,\ell}(u).
}
\tag{20}
$$
原输出没有被缩放，故这里没有遗漏的输出尺度对数。
(20) 是整条式；其中央质量和导数都直接读取。
principal 质量零，若原 $J'_S(0)=0$，
则 (20) 这一个明确的**有权十二球组合**的中央导数确为零。
这比仅在原点辅助球上返回 $S$ 更强，也没有借用未知参考的斜率。

然而 (19)–(20) 的支撑同时含
$$Q\approx\mu_6Y\quad\text{和}\quad Q\approx2\mu_6Y.$$
第二组的系数是 (16) 的真实非零单位，不能从 (20) 删除。
第一组内部六个相位也尚未变成一个单支。

## 7. 与原三输入叶的准确交域及完整余行

R379 的逆变换是
$$
a=\frac{8Y+R+17Q}{34},\quad
b_1=\frac{8Y+R-17Q}{34},\quad
c=\frac{9Y-R}{17}.
$$
所以单一叶仍是
$$
Y\text{ unit},\qquad Q-Y\in p^N,\qquad R-9Y\in p^N.
\tag{21}
$$
(20) 的 $R$ 球是原点球，(21) 的 $R$ 球则是单位中心。
前者的零不能被无说明地移到后者。

(18) 确实允许保留这个第二移动中心，但返回的是一个明确的新余行，
并非自动的 $\lambda^m\nu_S^\times$。
若取
$$\mathcal B_m=\{Y\text{ unit},\,R-9Y\in p^m\},\qquad m\ge1,$$
则 $c\in p^m$，且 $u_0=(8Y+R)/17$ 必为单位。
由 (7)，完整返回为
$$
\boxed{
Y_*\!\left(1_{\mathcal B_m}W_N(Q;Y)\mathcal J\right)
=\lambda^m(u_0+\kappa^mc)_*
           (\nu_D^\times(u_0)\otimes\nu_C(c)).
}
\tag{22}
$$
它保留了原 $C$ 输入的全部加法 carry。
其 principal 中央完整展开是
$$
\boxed{
\lambda^m\left[
 J_D'(0)-(p-1)\sum_{j\ge1}
 \frac{\kappa^{6mj}}{6j}M_{6j}(C)I_{-6j}(D)
\right],
}
\tag{23}
$$
其中
$$
M_k(C)=\int c^k\,d\nu_C(c),\qquad
I_{-k}(D)=\int_{\mathbf Z_p^\times}u^{-k}\,d\nu_D(u).
$$
$M_0(C)=1$，$D$ 的单位质量零；
所有保留的正权是六的倍数，故 log 符号为负。
第 $j$ 项赋值至少 $6mj-v_p(6j)$，整个尾收敛。
不能把 (23) 中尚未控制的 $J_D'$ 或负矩删掉。

全 tame 也没有额外假设：对应整条返回为
$$
\lambda^m\sum_{j\ge0}
 \binom{(p-1)u}{6j}\kappa^{6mj}M_{6j}(C)
 \int_{\mathbf Z_p^\times}
 \omega_p(t)^\ell\langle t\rangle^{(p-1)u}t^{-6j}\,d\nu_D(t).
\tag{24}
$$
$j=0$ 是完整 $J_{D,\ell}(u)$；它的质量在非 principal tame 上仍保留。

### 7.1 权的尺度与各支输入

若 $m\ge N$，则在 $\mathcal B_m$ 上
$u_0\equiv Y\bmod p^N$。
第一组六球的 $Q\equiv Y$ 支正是
$a$ unit、$b_1\in p^N$、$c\in p^m$；
$Q\equiv-Y$ 支交换 $a,b_1$。
其余四支的两个 $A$ 输入都是单位。
第二组 $Q\equiv2\zeta Y$ 的六支也都有两个 $A$ 输入为单位；
$1\pm2\zeta$ 的范数只会在二、三、七处出现例外，本篇均已排除。

因此 (22) 仍包含两个单一单位叶和十个实际双单位补域。
在前述单一叶上，(16) 的系数确实可因模 $p^N$ 局部常数而写成
原单位输入 $a$ 的函数；但所得是**带这个真实函数的负矩**，
不是将该函数删掉后的 $I_{-k}(A)$。
任何只读 $Y\bmod p^N$ 的测试在这一单叶上，都被深 $A$ 的零质量消掉。
原 log 的非零高位必须通过完整 Taylor 尾读取。
这与 (22)–(24) 完全一致，也说明为什么不能由整逆预付一个
未计算的 $\kappa^{3N}$ 首项。

## 8. 本篇新增的实际用途

(5) 是同一原 $A$ 的全 theta 加法式；
(8) 保持任意 $R$，使原参考的完整导数不再是一个未消的项。
(11)–(14) 用原 theta 群标签和固定 degree 四十八的有理差
证明同层球矩阵的统一单位逆。
(18)–(20) 于是将一类真正随原输出移动的十二球域
完整返回原 $J_S$，所有权、尺度和相位都可直接使用。

剩下的控制问题精确落在 (21) 的第二单位中心及 (22)–(24) 的原余行。
本篇不把两个尺度的有权组合拆成各支零，也不把有限矩阵的单位性
当作独立叶格非零或固定曲线无穷素数的最终证明。

## 依赖与同步

- [R379](R379-original-third-joint-core-unit-collisions-and-three-input-return.md)：原三输入、整个 theta core、正交坐标与全尾规范。
- [R376](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)：原加法标签、整 division 因子、深层单位与 residue-degree 界。
- [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：原 sigma、Theta 与实际有界周期。

本证明通过根规则允许的小文本 GitHub 接口提交；没有把 API 同步
称为 git pull，亦未声称失联的终端执行过检查。核心登记和 HANDOFF
由根代理负责。
