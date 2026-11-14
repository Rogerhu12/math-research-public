# R380：原低轴第三位的确定修正与完整第二 Bockstein 的同一有理模型

日期：2026-11-14。**状态：已证明。** R377 的整个 theta 代表与原矩阵模 $p^2$ 相同，但它本身不提供完整第二 Bockstein 所需的第三位。本篇用原 theta 的确切低轴对数支付唯一仍能作用的第三位。修正后，两个矩阵虽然不必逐项模 $p^3$ 相同，却在每一个原首核输入上模 $p^3$ 相同。因此它们的模 $p^3$ 右核、指定模 $p^2$ 核的第二障碍，以及原 $C_2$ 中的整个 $d_2$ 都准确一致。完整 charge、十三行、Gaussian、原整左核和固定残数边界均保留。

## 1. 原矩阵与 R377 的精确范围

仍取
$$
p=6s-1>83,\qquad b=17,\qquad
\Gamma_T=\bigoplus_{0\le r<T}\mathcal O e_r,\qquad
e_r={w^r\over p^{\lfloor r/s\rfloor}},\qquad
w^s=p\epsilon,\qquad T\le3s .
\tag{1}
$$
相对来源是 R335、R338 的整个已付 canonical 模
$\mathcal V_D$，相对径向 Euler 是 $\mathcal E=R\partial_R$。
实际列乘回公共来源后的 charge 为
$$
N=n+40 .
$$
用 $M^{\rm orig}$ 表示完整物理矩阵；它与 R338 的
$m_{13}J$ 通过已付目标单位 $U_0$ 等价。所有原点零阶和两条十三行带均在
$M^{\rm orig}$ 中，不将其删去以改变目标长度。

真实径向变量为
$$
\rho=\Theta^{17}(1+8t)
=g_\kappa e_2(a_\kappa\epsilon),\qquad
g_\kappa=e^{-\kappa w^s}\rho,\qquad a_\kappa=p\kappa .
\tag{2}
$$
这里及下文的等式在同一个有限三块代数中解释，$\epsilon^3=0$。
原角变量是 $t=-b/x^3$，且
$$
t(w)=-bw+O(w^2).
\tag{3}
$$

沿 R377，记已经明确构造的有理函数为
$$
\Theta_\kappa^{[2]},\qquad
g_\kappa^{[2]}=\Theta_\kappa^{[2]}(1+8t),\qquad
\epsilon^{[2]}={\widetilde Z_2^{\,p+1}\over p}.
$$
其原点值分别为 $1,1,0$，并已证明
$$
g_\kappa^{[2]}\equiv g_\kappa,\qquad
\epsilon^{[2]}\equiv\epsilon\pmod{p^2\Gamma_T}.
\tag{4}
$$
置
$$
\rho^{[2]}=g_\kappa^{[2]}e_2(a_\kappa\epsilon^{[2]}).
\tag{5}
$$
该元素属于原目标的单位群；不同 charge 的物理列准确使用
$e_2(Na_\kappa\epsilon^{[2]})$。
由于 $\epsilon^{[2]}$ 从物理 $w^s$ 起，在原长度中其三次幂为零，所以
(5) 的 $N$ 次幂与 R377 的逐 charge 二次指数一致。

(4) 只给
$$
\rho^{[2]}/\rho=1+p^2H\pmod{p^3\Gamma_T},
\qquad \bar H\in\Gamma_T/p\Gamma_T.
\tag{6}
$$
一般不能由此直接识别 $M(P_2)/p^2\bmod p$。
本篇先计算 $\bar H$ 中唯一可能作用于原核的部分。

## 2. 整个真实来源上的目标 Euler 身份

令 $\mathcal E_{\rm tot}=\mathcal E+40$。
在 $\Gamma_T/p$ 中，目标算子
$$
\mathsf E_\epsilon=\epsilon\partial_\epsilon
$$
保持全部截断关系。普通整级数 $g_\kappa(w)$、$t(w)$
及原角因子约化后只在第一普通 $w$ 块中，不另含 $\epsilon$。
每条原 charge $N$ 列的 $\epsilon$ 依赖恰为
$e_2(N\bar a_\kappa\epsilon)$。故对整个原来源都有
$$
\boxed{
\epsilon\,\overline{M^{\rm orig}}
       (\mathcal E_{\rm tot}P)
=\bar a_\kappa^{-1}\mathsf E_\epsilon
       \overline{M^{\rm orig}}(P).
}
\tag{7}
$$
此式也可由 R338 的相对 Euler 身份乘回原 charge40 Gaussian 直接得到。
十三行运输不破坏它：$\mathsf E_\epsilon$ 保持两条实际边界，
所有跨界被乘 $p$ 的行在约化后仍按原规则处理。

于是
$$
\boxed{
\bar P\in K_1(M^{\rm orig})
\ \Longrightarrow\
\epsilon\,\overline{M^{\rm orig}}
       (\mathcal E_{\rm tot}\bar P)=0.
}
\tag{8}
$$
这没有断言 $\mathcal E_{\rm tot}$ 或 $\mathcal E$ 保持原核。

对任意径向改变量
$\rho^\dagger/\rho=1+p^2H^\dagger\bmod p^3$，
按原各列的真实整数 charge 展开，准确有
$$
\boxed{
M^\dagger(P)-M^{\rm orig}(P)
\equiv p^2H^\dagger
 \overline{M^{\rm orig}}(\mathcal E_{\rm tot}P)
\pmod{p^3\Gamma_T}.
}
\tag{9}
$$
右边只使用 $P\bmod p$。
因此在原首核上，$\bar H^\dagger$ 的第二、第三 $\epsilon$ 块均由 (8) 消去。
真正需支付的只有它的第一块
$$
H^\dagger_0(w)\in k[w]/w^s .
\tag{10}
$$
由于 (5) 与原径向变量在 $O$ 都准确为一，(6) 中 $H_0(0)=0$。
特别，未付第三位的作用没有一个可自由选择的常数项。

## 3. 原低轴提供一个确切可计算的第三位修正

R334 已由原椭圆方程证明
$$
\log\Theta^{17}=\sum_{j\ge1}\ell_jt^j,\qquad
\ell_j={17\over3j}{(1/3)_j\over(5/6)_j}.
\tag{11}
$$
当 $1\le j<s$ 时，(11) 的全部分母均为 $p$ 单位：
$j<p$，而 $(5/6)_j$ 尚未包含首个因子 $p=6s-1$。
故定义
$$
\mathcal L_{<s}(t)
=\left[\log(1+8t)+\sum_{j=1}^{s-1}\ell_jt^j\right]_{<s}
\in t\mathcal O[t]/t^s .
\tag{12}
$$
这是原 $\log\rho$ 的确切低窗。
Gaussian 的首次物理次数是 $w^s$，经 (3) 换元后仍从 $t^s$ 起，
所以原 $\log g_\kappa$ 在此窗也正是 (12)。

R377 的 $g_\kappa^{[2]}$ 是原曲线上的 $\mu_6$ 不变有理函数，
因此是 $t$ 的有理函数，并在 $t=0$ 准确为一。
其低窗整性及 (4) 给
$$
\left[\mathcal L_{<s}(t)-\log g_\kappa^{[2]}(t)\right]_{<s}
\in p^2t\mathcal O[t]/t^s.
\tag{13}
$$
这里有限对数只用分母 $1,\ldots,s-1$，全部可逆。
(3) 是整形式参数的单位变换，所以在 $t$ 窗与 $w$ 窗之间
没有丢失精度，也没有引入额外行。

定义一个完全确定的整多项式
$$
\boxed{
A_0(t)={1\over p^2}
 \left[\mathcal L_{<s}(t)-\log g_\kappa^{[2]}(t)\right]_{<s}
\in t\mathcal O[t]_{<s}.
}
\tag{14}
$$
也可只取其约化后任一常数为零的整提升。
(14) 是已知有限有理系数的计算式：它不使用未知的原中央值，
也不把 $A_0$ 当作一个原来源或新中央观察。
只要改变 $A_0$ 一个 $p$ 倍，以下矩阵结论不变。

用这个目标修正置
$$
\boxed{
\rho^\star=\rho^{[2]}(1+p^2A_0(t)).
}
\tag{15}
$$

**命题1。** 同一三块代数内存在 $\bar H_1,\bar H_2$，使
$$
\boxed{
\rho^\star/\rho
=1+p^2\{\epsilon H_1+\epsilon^2H_2\}
\pmod{p^3\Gamma_T}.
}
\tag{16}
$$

**证明。** (4) 保证比值在 $1+p^2\Gamma_T$ 中。
其第一块的对数差，由 (12)–(14) 被 (15) 准确消至模 $p^3$。
有限对数或指数的二次误差带 $p^4$，因此不影响这一结论。
在 $\Gamma_T/p$ 中，第一块为零的元素恰属于理想 $(\epsilon)$。
这给 (16)，第三块仍按原长度截断。
$\square$

这一步只支付缺失的确定低轴，未声称整个矩阵逐项模 $p^3$ 已相同。

## 4. 原模 p³ 核与完整第二障碍逐向量相同

令 $M^\star$ 是以 (15) 为径向变量、原角因子完全不变的原物理矩阵。

**定理1。** 有
$$
M^\star\equiv M^{\rm orig}\pmod{p^2},
\tag{17}
$$
并且对任何整来源向量 $P$，只要
$\bar P\in K_1(M^{\rm orig})$，就有
$$
\boxed{
M^\star(P)\equiv M^{\rm orig}(P)\pmod{p^3\Gamma_T}.
}
\tag{18}
$$
因此：
$$
\boxed{K_r(M^\star)=K_r(M^{\rm orig})\qquad(r=1,2,3)}
\tag{19}
$$
作为同一原来源模 $p^r$ 中的子模成立。
此外，对每个指定 $P_2\in K_2$，
$$
\boxed{
\widetilde\beta_2^{M^\star}(P_2)
=\widetilde\beta_2^{M^{\rm orig}}(P_2)
\quad\text{于共同 }C_1,
}
\tag{20}
$$
并有
$$
\boxed{
d_2^{M^\star}=d_2^{M^{\rm orig}}
:\ker\beta_1\longrightarrow C_2 .
}
\tag{21}
$$

**证明。** (17) 来自 (4)、(15)。
将 (16) 代入 (9)，其变化含
$\epsilon\,\bar M^{\rm orig}(\mathcal E_{\rm tot}\bar P)$，
由 (8) 为零，所以得到 (18)。
任何模 $p^3$ 核必先落在共同首核中，故 (18) 双向给 (19) 的最后一式。
指定模 $p^2$ 核的任意整提升也在共同首核中；
(18) 除 $p^2$ 后给 (20)。
两个矩阵模 $p^2$ 相同，因此首 Bockstein 及其整个像相同，
再投到 R338 的正确商
$$
C_2=
{\Gamma_T/p\over
 \operatorname{im}\bar M+
 \operatorname{im}(\beta_1:K_1\to C_1)}
$$
即得 (21)。$\square$

这里的 $C_1$ 相同是指两边共同的 $\bar M$ 像。
(20) 没有换掉给定的第一次核提升；(21) 进一步保留了
更换第一次提升所产生的全部 $\beta_1(K_1)$。

若使用 R338 的 $m_{13}J$ 规范，可以用同一个原目标单位 $U_0$ 将
(17)–(21) 同时转回。若选择模型自己的公共单位，其与原单位模 $p^2$ 相同；
作用于一个 $p^2$ 输出后差为 $p^4$。
因此这也不改变指定第二障碍。
证明的关键始终是原 $\mathcal E+40$，不能先删 charge40 再比较两个不同规范。

## 5. 全局有理列及同一个 P₂

将 R377 的完整原列记为
$$
\mathcal S_{a,j}^{[2]}
=(\Theta_\kappa^{[2]})^N F_{a,j}(t)
 e_2(Na_\kappa\epsilon^{[2]}),\qquad N=a+40,
\tag{22}
$$
其中 $F_{a,j}$ 是整个已付角多项式，仍含全部 $P_{134}$。
本篇可准确取以下全局有理代表：
$$
\boxed{
\mathcal S_{a,j}^{\star}
=\mathcal S_{a,j}^{[2]}\{1+Np^2A_0(t)\}.
}
\tag{23}
$$
与 (15) 的真正 $N$ 次幂之差为 $p^4$ 乘原整目标列，
不影响 (17)–(21)。
对混合来源向量 $P$，$\mathcal S_P^\star$ 使用原来同一个 $P$
逐列组合 (23)，没有把各 grade 分别取核。

因 $A_0$ 是次数小于 $s$ 的多项式，它只可能增加原 $x=0$ 固定边界的极阶，
不加入新的移动测试极。
其 $p^2$ 因子也完整保留：
对于 (22) 的 Gaussian 第 $j$ 项、$j=0,1,2$，
新增项的显示系数为 $p^{2-j}$ 乘整系数。
因此新增的 $x=0$ 极部是整的，不能因为它不影响低窗就从全局残数中删除。

这给一个实际可操作的二阶计算：
先用已知的有理矩阵 $M^{[2]}$ 算指定 $P_2$ 的第二障碍，
再加
$$
\boxed{
\left[A_0(t)\,\bar M^{\rm orig}
                  (\mathcal E_{\rm tot}\bar P)\right].
}
\tag{24}
$$
在 $C_2$ 中也用同一个式子。
(24) 是确定的目标修正，而不是要求它本身属于原来源像。
定理1证明修正后的结果恰为真正原 $d_2$。

## 6. 原有的一次坐标对偶已足以读第二障碍

R377 付出的坐标关系是
$$
\widetilde Z_2/z=1+p^2u(w)
\tag{25}
$$
于本篇全部原短窗，$u(w)$ 为整级数；
更高的 $pz^{5p}$ 项在 $T\le3s$ 的范围之外。
$w\mapsto\widetilde Z_2^6$ 给 $\Gamma_T$ 的整行变换，
且该变换为 $I+p^2B_0$。
这是因为只向较高物理行移动，除幂权之差
$\lfloor r/s\rfloor-\lfloor j/s\rfloor$ 非负。

R377 为避免新增测试零，使用的有理对偶是
$$
\boxed{\begin{aligned}
\Lambda_\lambda^{[2]}
=\sum_{r=0}^{T-1}\lambda_rp^{\lfloor r/s\rfloor}
\widetilde Z^{-6r-1}\bigg[
D\widetilde Z+pD\widetilde Z_1
-p(6r+1){\widetilde Z_1\over\widetilde Z}D\widetilde Z
\bigg]dz .
\end{aligned}}
\tag{26}
$$
它是 $\widetilde Z_2$ 坐标对偶拉回后除以六的一次 $p$ 展开。
略去的项也给一个 $p^2$ 倍的整行变换；
所需整性直接由原系数权
$p^{\lfloor r/s\rfloor}$ 保证。
因此对一个任意整目标输入，它与原对偶只需模 $p^2$ 比较；
但对一个 $p^2\Gamma_T$ 输入，误差自动升到 $p^4$。

现在令
$$
\bar P\in\ker\beta_1,\qquad
P_2\in K_2(M^{\rm orig}),\qquad
\lambda_0\in C_2^\vee ,
$$
并取 R351 保证存在的真正整左核提升 $\lambda_2$，
满足 $\lambda_2M^{\rm orig}=0\bmod p^2$。
定理1与 (17) 保证 $\mathcal S_{P_2}^\star$ 的原目标输出在 $p^2\Gamma_T$。
故同一 $P_2,\lambda_2$ 有
$$
\boxed{
\left\langle\lambda_0,d_2^{M^{\rm orig}}(\bar P)\right\rangle
=
\overline{{1\over p^2}
 \operatorname{Res}_{O}
   \left(\mathcal S_{P_2}^\star\Lambda_{\lambda_2}^{[2]}\right)}.
}
\tag{27}
$$
原点残数被 $p^2$ 整除由真正核条件保证。
无需把 (26) 对每条来源的比较擅自升为模 $p^3$；
这里提升精度的原因是同一 $P_2$ 的输出已经含 $p^2$。

更换 $P_2$ 的首次提升，在 (27) 中产生的变化正是
$\lambda_0\beta_1(K_1)=0$；
更换其整提升 $p^2Q$ 则产生 $\lambda_0\bar M Q=0$。
整左核提升的自由度也由这个 $p^2$ 输出支付。
所以 (27) 是原真正 $C_2$ 配对，而非任意局部 Laurent 测试。

## 7. 全部真实边界的原二阶聚合

(23)、(26) 的极仍只位于：
原 $O$、真正的 $\widetilde Z=0$ 非原点测试点、
两个 $x=0$ 点和三个非零二挠点。
公共 $P_{134}$、完整 $U_0$ 及 $Z^{-78}$ 对应的十三行均未删除。
R377 的原 Gaussian 与整性证明仍适用；
新增项的整性另由第5节的 $p^{2-j}$ 支付。

全局残数定理把 (27) 准确改写为
$$
\boxed{\begin{aligned}
\left\langle\lambda_0,d_2^{M^{\rm orig}}(\bar P)\right\rangle
=-\overline{{1\over p^2}\bigg\{
 &\sum_{\text{真实非原点测试点}}\operatorname{Res}
       (\mathcal S_{P_2}^\star\Lambda_{\lambda_2}^{[2]})\\
+&\sum_{E[2]\setminus O}\operatorname{Res}
       (\mathcal S_{P_2}^\star\Lambda_{\lambda_2}^{[2]})\\
+&\sum_{x=0}\operatorname{Res}
       (\mathcal S_{P_2}^\star\Lambda_{\lambda_2}^{[2]})
\bigg\}} .
\end{aligned}}
\tag{28}
$$
各组只计一次。
**先将整个括号相加，再除以 $p^2$**；
这里没有断言各个固定边界或每个移动残数单独被 $p^2$ 整除。
整个括号的整除性由 (27) 的同一原核保证。

(28) 已把原完整第二 Bockstein 基准运输到确定的有理微分，
没有剩下一个未指定的低轴第三位。
它保留 R372 的真实 double-Euler 拉回及其交换差：
当对 $P$ 乘原来源乘子时，实际 forcing 仍为
$L^{-1}\operatorname{pp}(v\,Lq)$，不是直接改成 $vq$。
R366/R369 的两个联合局部单位模型也不能据此分别赋零。

原完整中央失败的输入仍只是
$$
a_\kappa c_1-pc_2\equiv0\pmod{p^2}
$$
及原已付的更高聚合；(27)、(28) 没有把它拆成逐权消失。
下一需要比较的是这个真实同 $P_2,\lambda_2$ 的全边界聚合与原中央条件，
而不是再次补一个任意第三位或把局部单射替成原深核。

## 依赖与同步

- R334：原 $\ell_j$ 的全参数公式与完整中央下一聚合。
- R335、R338：整个 canonical 来源、十三行与正确 $C_1/C_2$。
- R351、R365：原整左核、完整 total-charge 连接及公共目标规范。
- [R377](R377-whole-original-theta-first-lift-and-integral-serre-model.md)：
  整个 theta 模 $p^2$、精确原点常数、真实坐标第一商和有理 Serre 代表。
- [R372](R372-original-fixed-torsion-boundaries-and-true-double-euler-pullback.md)：
  固定边界与真正 double-Euler 拉回。

本篇为全参数整线性代数与原有理系数证明，没有目标素数扫描。
通过已授权 GitHub API 保存；核心登记与 HANDOFF 由根代理维护。
