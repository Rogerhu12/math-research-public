# R377：原整个 theta 的模 p² 有理代表与同一整 Serre 矩阵

日期：2026-11-14。**状态：已证明。** R363 的真实二阶连接可以积分成整个原径向 theta 的模 $p^2$ 有理代表。其原点常数、移动测试点的首提升、坐标第一商和完整 Gaussian 同时支付。任意原 canonical 来源的三块矩阵、模 $p^2$ 左右核及正确 $C_2$ 都保持不变；相应有理 Serre 代表只保留原测试极和固定二／三挠点。这里尚未把固定边界或其总和的约束加强为逐测试极为零。

## 1. 原整对象及精度

固定原惰性好位
$$
p=6s-1>83,\qquad b=17,\qquad
\mathcal O,\quad k=\mathcal O/p\mathcal O .
$$
所有原 canonical 整格的固定坏素数仍排除。
在
$$
E_b:y^2=x^3+b,\qquad Dx=2y,\quad Dy=3x^2,\quad w=z^6
$$
上工作。目标仍为实际三块
$$
\Gamma_T=\bigoplus_{0\le r<T}\mathcal O\,{w^r\over p^{\lfloor r/s\rfloor}},
\qquad T\le3s,\qquad w^s=p\epsilon,\quad\epsilon^3=0 .
\tag{1}
$$
$T$ 可以是原 $L+13$ 及所有已经支付的较大目标；
两条十三行带没有删除。

沿 R342/R356 取同一个特征零有理函数
$$
\widetilde Z=\mathscr R_p(x)/y^p,\qquad
D\widetilde Z=1-3p\widetilde Z a,\qquad a=x^2/y ,
\tag{2}
$$
并记其约化为 $Z$。
它在原点的准确首系数是
$$
\lambda=[z]\widetilde Z=(1-3p)^{-1}.
\tag{3}
$$
对有理函数定义
$$
\widetilde I(f)=
\sum_{i=0}^{p-2}{(-1)^i\widetilde Z^{\,i+1}D^if\over(i+1)!}.
\tag{4}
$$
所有这些阶乘均为单位；$D$ 在 (4) 中是原不变导子，
未将 $D\widetilde Z$ 擅自改成一。

令
$$
\widetilde G_\kappa=\widetilde I(-x)-\delta_\kappa\widetilde Z^p,
\qquad
\widetilde H_\kappa=\widetilde I(\widetilde G_\kappa).
\tag{5}
$$
它们约化为 R356/R369 的原 $G_\kappa,H_\kappa$。
允许使用 R373 的合法降极 Gaussian 规范；
下述论证仍保留它在特征零产生的全部 $p$ 倍极部。

## 2. 两个原点常数恰在模 p² 相消

记
$$
c_{\rm lin}=\sum_{j=1}^{p-1}\lambda^j .
$$
R356 已证明 $\widetilde G_\kappa$ 的原点极部为
$-c_{\rm lin}/z$。因此 (4)、(5) 给准确常数
$$
\boxed{
C_H=\widetilde H_\kappa(O)
=-c_{\rm lin}\sum_{j=1}^{p-1}{\lambda^j\over j}.
}
\tag{6}
$$
$\delta_\kappa\widetilde Z^p$ 不产生这一常数。
其余项在原点正规；所有系数在所需短窗内整。

**命题1。**
$$
\boxed{
C_H\equiv-3p\pmod{p^2},\qquad
\log\lambda\equiv3p\pmod{p^2}.
}
\tag{7}
$$
所以
$$
\boxed{
c_*=\lambda^{34}E_{p-1}(34C_H)\in1+p^2\mathcal O,
\qquad E_{p-1}(X)=\sum_{j=0}^{p-1}X^j/j!.
}
\tag{8}
$$

**证明。** $\lambda^j\equiv1+3pj\bmod p^2$，故
$c_{\rm lin}\equiv p-1\bmod p^2$。
另一方面，配对 $j,p-j$ 给
$$
\sum_{j=1}^{p-1}j^{-1}
\equiv-\frac p2\sum_{j=1}^{p-1}j^{-2}
\equiv0\pmod{p^2}.
$$
最后的和模 $p$ 为零，因为 $p>3$。
于是
$\sum\lambda^j/j\equiv3p(p-1)\equiv-3p\bmod p^2$；
代入 (6) 即得第一式。第二式由
$\log\lambda=-\log(1-3p)$ 得出。再展开 (8) 即可。
$\square$

这是实际的常数取消，不能只因为两者模 $p$ 为一就省去。
最终可以准确除以已明确的 $c_*$，同时它不改变任何模 $p^2$ 原目标。

## 3. 保 x=0 的二阶连接提升

沿 R363，记
$$
R_{\kappa,p}^{(2)}
=\widetilde r_\kappa+p\widetilde r^{(1)}_p,\qquad
G^{(2)}={y\over x}R_{\kappa,p}^{(2)}.
\tag{9}
$$
在同一原目标中
$$
R_{\kappa,p}^{(2)}\equiv{x\over y}\zeta_\kappa\pmod{p^2\Gamma_T},
\qquad R_{\kappa,p}^{(2)}(O)=-1.
\tag{10}
$$
在所有真正 lifted 测试点 $\widetilde Z=0,\ x,y\ne0$，
$G^{(2)}$ 准确为零。

本篇在 R363 允许的提升中，另保 $x=0$ 的真实零。
这不增加任何假设。该文的
$r_p^{(1)}=(x/y)I_Z(\mathfrak F_p)$
在 $x=0$ 为零，因为 $\mathfrak F_p$ 在那里正规而 $Z=0$。
其型为零，故在局部 $x$ 中实际消失至少三阶。
于是 R363 的多项式可加强为
$$
\deg\bigl((1-t)^{p^2}r_p^{(1)}\bigr)\le p^2-1 .
\tag{11}
$$
先除以 $B_p(-t)^2$，再按这个次数上界逐系数提升，
同时仍取原常数 $-\eta_{\rm lin}$，即可得到
$\widetilde r_p^{(1)}$ 在 $x=0$ 精确有至少三阶零。
因此
$$
G^{(2)}\in\mathcal A
:=\mathcal O[x,y,1/y]/(y^2-x^3-b),
\tag{12}
$$
在整个仿射部分只可能于原三个非零二挠点有极。
它在 $x=0$ 消失至少二阶。
(11) 只约束本来为零的最高系数，不改变 R363 的任何原目标比较。

## 4. 一个全局真正可除以 p 的 forcing

定义完整的特征零 lift
$$
\widetilde\chi={(1+\widetilde Za)^p\over\widetilde Z},
$$
以及
$$
\boxed{
F_1={1\over p}
\left(G^{(2)}-{D\widetilde Z\over\widetilde Z}
      -D\widetilde H_\kappa+\widetilde\chi\right).
}
\tag{13}
$$

**定理1。** (13) 属于共同整环 $\mathcal A$。
其约化 $\bar F_1$ 在 $O$ 及 $x=0$ 正规，只可能在原三个非零二挠点有极；
其 $\mu_6$ 型为负一。在每个真正测试点
$$
\boxed{\bar F_1(P)=4a(P)=4x(P)^2/y(P)\in k^\times.}
\tag{14}
$$

**证明。** 先消去显示的 $\widetilde Z$ 分母，使用 (2) 得
$$
\boxed{
\widetilde\chi-{D\widetilde Z\over\widetilde Z}
=4pa+\sum_{j=2}^{p-1}\binom pj\widetilde Z^{j-1}a^j
+\widetilde Z^{p-1}a^p .
}
\tag{15}
$$
它确在 $\mathcal A$，没有新移动极。
其余两项由 (4)、(5)、(12) 也在 $\mathcal A$。

模 $p$ 后，
$$
\overline{G^{(2)}}=G_\kappa,\qquad
DH_\kappa=G_\kappa+Z^{p-1}a^p .
$$
因此 (13) 分子在 $\mathcal A/p\mathcal A$ 中准确为零。
该环是同一光滑仿射曲线的局部化，且 $\mathcal A$ 对 $\mathcal O$ 平坦；
约化核恰为 $p\mathcal A$。所以全局可以除以 $p$，
并非只在原点逐个系数宣称可除。

在 $O$，$G^{(2)}$ 的极部准确为 $1/z$，
$D\widetilde Z/\widetilde Z$ 的极部也是 $1/z$，
而 $D\widetilde H_\kappa$ 正规。
(13) 唯一可能剩余极系数为
$$
{(1-\lambda)^p\over p\lambda}
=(-3)^pp^{p-1}\lambda^{p-1},
$$
其约化为零。因此 $\bar F_1$ 在 $O$ 正规。
其负一型进一步使首个可能项从 $z^5$ 起。

在 $x=0$，(12) 的 $G^{(2)}$、$D\widetilde H_\kappa$ 和 (15)
都有至少二阶零；可在同一整局部环先提取 $x^2$ 再约化。
所以这里亦无新极。

最后，在任一 $\widetilde Z=0$、$x,y$ 为单位的实际整测试点，
$G^{(2)}=D\widetilde H_\kappa=0$。
(15) 余下的值恰为 $4pa$；除以 $p$ 得 (14)。
$\square$

这是原 first-lift 的新 forcing；它与 R363 中具有双零的
$r_p^{(1)}$ 不同，不能把两者的阶数互换。

## 5. 原 theta 对数的第一提升

定义同一剩余函数域中的有限 primitive
$$
\boxed{
H_1=I_Z(\bar F_1)
=\sum_{i=0}^{p-2}{(-1)^iZ^{i+1}D^i\bar F_1\over(i+1)!}.
}
\tag{16}
$$
它在 $O$ 的常数为零；在 $x=0$ 也为零。
在所有真正非原点测试点，
$$
\boxed{
H_1(P)=0,\qquad DH_1(P)=4a(P).
}
\tag{17}
$$
故这里是准确的简单零，显示一阶系数为单位。

这些断言由同一个有限恒等式
$$
DH_1=\bar F_1+Z^{p-1}D^{p-1}\bar F_1
\tag{18}
$$
直接得到。原点没有隐藏积分常数：
$\bar F_1$ 正规、型负一，(16) 至少从 $Z^6$ 起。
其 $D^{p-1}$ 在原点只可能从 $Z^{5p}$ 起，
故 (18) 的附加项至少从 $Z^{6p-1}$ 起。
所需窗口远低于第一次同型共振。

还可以保全一个明确的全局极界。
$G^{(2)}$ 与 $D\widetilde H_\kappa$ 的二挠极阶至多 $2p^2-1$；
(15) 的极阶不超过此界。
所以 $\bar F_1$ 的极阶至多 $2p^2-1$。
(16) 每次导数增至多一阶、每个 $Z$ 增 $p$ 阶，给
$$
\operatorname{pole}_T H_1\le3p^2-3 .
$$
置 $M_1=3(p^2-1)/2$，于是
$$
\boxed{
H_1={N_1(t)\over(1-t)^{M_1}},\quad
N_1(0)=0,\quad \deg N_1\le M_1-1,\quad B_p(-t)\mid N_1(t).
}
\tag{19}
$$
每个 $B_p(-t)$ 根的重数准确为一，因 (17) 及 $Dt\ne0$。

将 $N_1/B_p(-t)$ 按这些次数、零常数约束整提升，
并乘回真正的整 $\mathscr B_p(-t)$，得到
$\widetilde H_1$。它在原点、$x=0$ 和所有真正 lifted 测试点
都精确为零，只有原二挠极。
不同这种 lift 只改变 $p\widetilde H_1$ 的模 $p^2$ 项。

## 6. 整个原径向 theta 在三块中的比较

先定义准确归一的有理函数
$$
\boxed{
\Theta_{\kappa}^{[2]}
=c_*^{-1}(\widetilde Z^2x)^{17}
 E_{p-1}\!\left(34(\widetilde H_\kappa+p\widetilde H_1)\right).
}
\tag{20}
$$
它的原点值准确为一。相应径向变量是
$$
g_\kappa^{[2]}=\Theta_\kappa^{[2]}(1+8t).
$$

**定理2。** 对每个原三块长度 $T\le3s$，
$$
\boxed{
g_\kappa^{[2]}\equiv
g_\kappa=e^{-\kappa w^s}\Theta^{17}(1+8t)
\pmod{p^2\Gamma_T}.
}
\tag{21}
$$

**证明。** 普通整系数的误差属于 $p^2\Gamma_T$，
准确等价于
$$
p^2\mathcal O[[w]]+p\,w^s\mathcal O[[w]]
+w^{2s}\mathcal O[[w]]
\quad\text{在该长度中}.
\tag{22}
$$
所以只需低块模 $p^2$、中块模 $p$；高普通块不再索取未付精度。

对低块，置
$$
\ell_\kappa=\log(\sigma/z)-\kappa w^s/34,\qquad
\mathfrak L=\log(z/\widetilde Z)+\ell_\kappa-\widetilde H_\kappa .
$$
由 (7)，$\mathfrak L(0)=-\log\lambda-C_H\in p^2\mathcal O$。
由 (10)、(13)，在所需低窗内
$$
D\mathfrak L=pF_1-\widetilde\chi+O(p^2).
\tag{23}
$$
这里 $(y/x)R_{\kappa,p}^{(2)}$ 对 $\zeta_\kappa$ 的误差在低块为 $p^2$，
乘 $y/x$ 的单极没有跨过原允许的窗口。

还须支付 $\widetilde\chi$ 的低系数。
$1+\widetilde Za$ 的常数 $1-\lambda$ 被 $p$ 整除，
其正次从 $w$ 起且在原窗口整。
故其 $p$ 次幂中，$w^j$、$j<s$ 的系数至少被 $p^{p-j}$ 整除。
再除以 $\widetilde Z=z$ 乘整单位，
所有低块导数系数仍被 $p^2$ 整除。
因此在 (23) 低块中可以准确略去 $\widetilde\chi\bmod p^2$，
没有将其全局微分删除。

(18) 及其原点阶给
$D(\mathfrak L-p\widetilde H_1)=0\bmod p^2$
至该窗口。积分的系数 $6j$、$1\le j<s$ 全为单位，
再用已付常数，得到
$$
\mathfrak L\equiv p\widetilde H_1\pmod{p^2,w^s}.
\tag{24}
$$
这正是 (20) 所需的低块对数比较。

有限指数尾也完整可控。
$\widetilde H_\kappa+p\widetilde H_1$ 的常数为 $C_H\in p\mathcal O$，
正次从 $w$ 起。对第 $r\ge p$ 个遗漏指数项，
其 $w^j$ 系数的赋值至少为 $r-j-v_p(r!)$。
当 $j<s$ 时此值至少二；当 $j<2s$ 时至少一。
所以 $E_{p-1}$ 与所需完整局部指数在 (22) 的全部精度相同。
$c_*\in1+p^2\mathcal O$ 亦已付。

对中块，模 $p$ 后 (20) 就是 R369 原 finite theta 代表；
$p\widetilde H_1$ 消失，而该文比较至 $w^{5s-1}$，
覆盖本篇所有中块。
各函数在该短窗的整性来自 R342 原 $z(u)$ 的首次坏项在 $u^{5p}$，
以及 (4) 中小于 $p$ 的阶乘；没有借更远 Taylor 系数的整性。
结合 (22) 即得 (21)。$\square$

(21) 在同一整目标代数中成立，故任意有限原次数的幂、多项式和
原已付角乘法都保持这个比较。它不是新增一条来源。

## 7. 原坐标第一商及 Gaussian 的有理代表

还不能把物理 $\epsilon=w^s/p$ 直接换成 $\widetilde Z^{p+1}/p$。
为支付这个差，定义
$$
\widetilde e=3\widetilde Za,\qquad
\widetilde Z_1=\widetilde I(\widetilde e),\qquad
\boxed{\widetilde Z_2=\widetilde Z+p\widetilde Z_1.}
\tag{25}
$$
由 (2)，真实 $z_1=(z-\widetilde Z)/p$ 满足 $Dz_1=\widetilde e$。
模 $p$ 的有限 primitive $I_Z(\bar e)$ 与 $z_1$ 的差，
在首次型一共振 $z^{5p}$ 之前为零：
其导数误差从 $Z^{5p-1}$ 起，常数和首同型项均固定。
因此
$$
\boxed{
z-\widetilde Z_2
\in p^2\mathcal O[[z]]+p z^{5p}\mathcal O[[z]]
\quad\text{于原有限整窗口}.
}
\tag{26}
$$
这里的完整首系数还可直接检查：
$$
[z]\widetilde Z_1=-3\lambda^2,\qquad
[z]\widetilde Z_2=\lambda-3p\lambda^2
=1-9p^2\lambda^2 .
\tag{27}
$$
在所有真正测试点，$\widetilde Z_1$ 有至少二阶零，
所以 $\widetilde Z_2$ 仍精确为零，且
$D\widetilde Z_2=1$。在 $x=0$ 它有更高的同型零。
这些函数只有原二挠极。

令
$$
\boxed{\epsilon^{[2]}={\widetilde Z_2^{\,p+1}\over p}.}
\tag{28}
$$
虽然它是带显示 $p$ 分母的有理函数，它在原点属于同一个除幂目标，
并且 (26) 准确给
$$
\boxed{\epsilon^{[2]}\equiv\epsilon\pmod{p^2\Gamma_T}.}
\tag{29}
$$
因为 $\widetilde Z_2/z=1+p^2$ 乘一个整级数，
其 $p+1$ 次幂除以 $p$ 的差是 $p^2\epsilon$ 乘整级数；
(26) 中更高的项落在原截断外。

因此对每个真实 charge $N$，完整物理 Gaussian 为
$$
\boxed{
(g_\kappa^{[2]})^N e_2(Na_\kappa\epsilon^{[2]})
\equiv g_\kappa^N e_2(Na_\kappa\epsilon)
\pmod{p^2\Gamma_T}.
}
\tag{30}
$$
没有只比较 regularized 函数后遗忘中心补偿。
每个全局齐次代表使用显示的二次指数，不把其高于三块的幂
额外带进全局残数。

## 8. 同一 P、同一左核及完整有理 Serre 代表

乘回整个原 $G_0$ 后，原 canonical 列是
$$
\Theta^{17N}F_{a,j}(t),\qquad N=a+40 ,
$$
其中 $F_{a,j}$ 是 R361/R372 的完整多项式，含全部 $P_{134}$。
选择其全局有理代表
$$
\boxed{
\mathcal S_{a,j}^{[2]}
=(\Theta_\kappa^{[2]})^N F_{a,j}(t)
 e_2(Na_\kappa\epsilon^{[2]}).
}
\tag{31}
$$
(21)、(29) 证明这些正是同一原矩阵的模 $p^2$ 列。
原十三行仍由这些列在 $O$ 的实际零阶给出。
若用 $M=m_{13}J$ 规范，则继续使用原本的整目标单位 $U_0$；
不在非原点把 $U_0=G_0/w^{13}$ 或 $Z^{-78}$ 重新称为单位。
整目标同构保留 (31)，无须免费反向删除十三行。

设原整个目标的整行是 $\lambda=(\lambda_r)$，先按真实 $U_0$
同构转到 (31) 的物理规范。其物理对偶为
$\sum\lambda_rp^{\lfloor r/s\rfloor}w^{-r-1}dw$。
在原 $E_b$ 上按 $w=z^6$ 的分歧指数除以六，取如下全局有理代表：
$$
\boxed{\begin{aligned}
\Lambda_\lambda^{[2]}
=\sum_{r=0}^{T-1}\lambda_rp^{\lfloor r/s\rfloor}
\widetilde Z^{-6r-1}\bigg[
D\widetilde Z+pD\widetilde Z_1
-p(6r+1){\widetilde Z_1\over\widetilde Z}D\widetilde Z
\bigg]dz .
\end{aligned}}
\tag{32}
$$
$\widetilde Z_1/\widetilde Z$ 在所有测试零处正规。
(32) 是 $\widetilde Z_2$ 坐标对偶拉回后除以六的完整一次 $p$ 展开，
其全部原 $p^{\lfloor r/s\rfloor}$ 权均在式内。
不用倒置 $1+p\widetilde Z_1/\widetilde Z$，从而不加入它的新零点。

**定理3。** 对任意一个原来源向量 $P$，
$$
\boxed{
\langle\lambda,M^{\rm orig}P\rangle
\equiv\operatorname{Res}_{O}
 \left(\mathcal S_P^{[2]}\Lambda_\lambda^{[2]}\right)
\pmod{p^2},
}
\tag{33}
$$
其中 $\mathcal S_P^{[2]}$ 使用同一个 $P$ 的原系数逐列组合 (31)。

**证明。** 原 $w$ 残数在 $z$ 支上的拉回恰增六倍；(32) 的除六使其值恢复为原矩阵系数。(26) 将原 $z$ 对偶换成 $\widetilde Z_2$ 时，
每一行的相对误差是 $p^2$ 乘原点整级数。
再展开 $(1+p\widetilde Z_1/\widetilde Z)^{-6r-1}$，
遗漏项也都是 $p^2$ 乘原点整级数，得到 (32)。

这里必须核除幂精度：一个原整列的第 $j$ 个物理系数
赋值至少为 $-\lfloor j/s\rfloor$。
某个原点整误差乘回后，读第 $r$ 行只会使用 $j\le r$。
故遗漏项乘真实对偶权后的赋值至少为
$$
2+\lfloor r/s\rfloor-\lfloor j/s\rfloor\ge2 .
$$
因此即使全局来源 (31) 有显示的 $p^{-1},p^{-2}$ Gaussian 项，
它们也不会破坏 (33)。结合 (30)、(31) 即得结论。
$\square$

于是原左右模 $p^2$ 核、$\beta_1$ 和正确的
$C_2=\operatorname{coker}\bar M/\beta_1(\ker\bar M)$
都由同一矩阵给出。
特别对于一个真正可提升的整左核 $\lambda_2$，
(33) 对全部原列和同一原 $P_2$ 给出实际的零模 $p^2$ 约束。
这没有要求 Euler 保持 $K_2$，也没有将混合次数 $P$ 分开取核。

## 9. 真实固定边界及下一配对

(31)、(32) 的全局极只可能在：
原 $O$、原全部 $\widetilde Z=0$ 测试点、两个 $x=0$ 点，
以及三个非零二挠点。全部 $P_{134}$ 和角零仍在来源分子内。
式 (32) 没有添加另一个移动测试集合。

在每个原 $B_p$ 测试点，(31) 的 Gaussian 第 $j$ 项
至少含 $\widetilde Z^{j(p+1)}/p^j$；
若它能贡献第 $r$ 行的留数，必有 $r\ge js$。
所以原对偶权 $p^{\lfloor r/s\rfloor}$ 至少取消这 $p^j$ 分母。
其余所有局部系数整。
$x=0$ 处原全纯角界给相同结论。
原点已由 (33) 保证整；三个二挠点由 $\mu_6$ 相位相同，
其总和再由全局残数定理保证同一整性。
因此 (33) 的全局残数关系确实可在原整测试格中模 $p^2$ 使用。

原可提升左核现在严格给
$$
\boxed{
\sum_{\text{原非原点测试点}}
 \operatorname{Res}\bigl(\mathcal S_P^{[2]}\Lambda_{\lambda_2}^{[2]}\bigr)
+\sum_{E[2]\setminus O}
 \operatorname{Res}\bigl(\mathcal S_P^{[2]}\Lambda_{\lambda_2}^{[2]}\bigr)
+\sum_{x=0}
 \operatorname{Res}\bigl(\mathcal S_P^{[2]}\Lambda_{\lambda_2}^{[2]}\bigr)
\equiv0\pmod{p^2}.
}
\tag{34}
$$
每组测试点只计一次；第一个和不重复后两组。
这是整个真实原矩阵的固定边界关系，不是随意选取的模 $p$ 局部权。

R363 的二阶有理连接现在可以与 (31)、(32) 同时放入同一配对；
R372 给出的 double-Euler 交换差和固定二／三挠边界也继续保留。
本篇已支付 whole-theta 的第一提升，
但 (34) 是完整的和式，不是各个非原点残数分别为零。
同样，模 $p^2$ 相同还没有识别需要模 $p^3$ 的整个 $d_2$；
其下一位与原完整中央失败的
$a_\kappa c_1-pc_2=0\bmod p^2$ 聚合均按原定义继续使用。

本篇为全参数证明，没有目标素数扫描，
也没有把全局有理代表的巨大极度计作免费来源。

## 依赖

- R335、R338、R342：原整个来源、除幂目标、Gaussian 与真正二阶余核。
- [R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)、
  [R363](R363-original-first-frobenius-quotient-and-second-rational-connection.md)：
  准确线性常数、真实 first-lift 及二阶连接。
- R365、R366：全部公共因子、整来源算子和同一提升核运输。
- [R369](R369-original-finite-theta-frame-and-shifted-joint-residue-primitivity.md)、
  [R371](R371-original-frame-defect-cartier-logarithm-and-weighted-exact-term.md)、
  [R373](R373-original-theta-log-cartier-chain-and-gaussian-pole-reduction.md)：
  原有限 theta、完整 frame 差和合法降极。
- [R372](R372-original-fixed-torsion-boundaries-and-true-double-euler-pullback.md)：
  固定端点边界、真实 double-Euler 拉回及所有末行。

通过已授权的 GitHub API 保存；核心登记与同步由根代理维护。
