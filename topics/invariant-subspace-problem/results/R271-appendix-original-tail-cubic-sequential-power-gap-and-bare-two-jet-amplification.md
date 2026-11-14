# R271 附录：原尾顺次／真幂二步费用的三次增长与同源裸二阶 jet 放大

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_continue。

状态：**已证明。** 本文在原无限正规尾上构造一个明确单位 primitive 源，使顺次两步 MP 与真正二次幂 MP 的能量比至少为 $3q^3/(m+1)^4$。这把原先有限三权的范围反例推进到原连续尾，并直接给出[真实 jet 费用稿](R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md)的 $C_{2,3,q+2}$ 及同源裸 $\mathfrak N_2$ 的增长下界。全部位置、完整层最小逆和斜投影成本都保留。没有证明这些测试源来自真实 $M$ 图或实际最优 Schur 来源。

## 1. 同一个原 primitive 源

固定 $m\ge5$ 和整数 $q\ge16(m+1)^2$。令
$$
D=D_m=\sum_{j\ge m}(j+1)^{-2}E_j,
\quad a=(m+1)^{-2},
\quad J=m+1+2q,
$$
$$
S=S_J=\sum_{j\ge J}(j+1)^{-4},\qquad b=\sqrt S.
\tag{1.1}
$$
保留第 $m$ 位作为一个真实强位；将 $[m+1,J)$ 分成 $q$ 个相邻二位块，余下是原无限尾 $[J,\infty)$。

在每个中间块，权记为 $\alpha,\beta$，定义单位暗向量
$$
h=\frac{\beta|10\rangle-\alpha|01\rangle}{\sqrt{\alpha^2+\beta^2}}.
$$
全部暗向量的张量积记为 $h_{\rm gap}$。取
$$
\boxed{f=|0\rangle_m\otimes h_{\rm gap}\otimes\Omega_J.}
\tag{1.2}
$$
每个暗对有一个孔，强位和远尾均为真空，所以
$$
f\in K_q^{(m)},\qquad Df=0,\qquad\|f\|=1.
$$
此处使用的是原纯尾，不是两个实际边界算子的有限孔核。

记完整层单步 MP 为 $R_p=D_p^\dagger$，并定义
$$
u_1=R_{q+1}f,\qquad
u_2=R_{q+2}R_{q+1}f,
\qquad
g=(D_{q+1}D_{q+2})^\dagger f.
\tag{1.3}
$$
它们都是原全孔层最小逆；$u_2$ 是顺次两步，$g$ 才是真幂两步。原固定层满射保证这些算子存在有界。显式定义同源比
$$
\mathcal C(f)=\frac{\|u_2\|^2}{\|g\|^2}.
$$

**定理。** 有
$$
\boxed{
\mathcal C(f)\ge\frac{a^2}{2R^2S}
\ge\frac{3q^3}{(m+1)^4},
\qquad R=e^{2/(m+2)}<2.
}
\tag{1.4}
$$
因而原真实短核常数满足
$$
\boxed{C_{2,3,q+2}\ge\frac{3q^3}{(m+1)^4}.}
\tag{1.5}
$$
下面还给出一个同一 $h\in E_{2,q+1}$ 的裸费用放大身份。

## 2. 有界且精确交织的原空间测试

对一个暗对，再置
$$
g_{\rm pair}=\frac{\alpha|10\rangle-\beta|01\rangle}
{\sqrt{\alpha^2+\beta^2}},\qquad
\rho=\frac{2\alpha\beta}{\alpha^2+\beta^2},
\qquad P=|h\rangle\langle g_{\rm pair}|/\rho.
$$
它在其余孔层上为零。直接计算给
$$
P^2=P,\qquad D_{\rm pair}P=PD_{\rm pair}=0,
\qquad\|P\|=\rho^{-1}.
$$
全部中间块的张量积投影 $P_{\rm gap}$ 与完整 $D$ 交换，并且
$$
\|P_{\rm gap}\|\le e^{2/(m+2)}=R.
\tag{2.1}
$$
这是[完整首个三维块稿 §5](R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)对从 $m+1$ 开始的原相邻权的同一估计。该投影是斜投影，成本 $R$ 不省略。

在远尾第 $r$ 层，定义真空创建行
$$
T_r u=
\left(\sum_{|I|=r}\sqrt{r!}\,S^{-r/2}
\Bigl(\prod_{i\in I}a_i\Bigr)u_I\right)e_r.
\tag{2.2}
$$
$e_r$ 是单玻色模的第 $r$ 个单位向量。创建系数计数给
$$
\|T_r\|^2=\frac{r!e_r((a_j^2)_{j\ge J})}{S^r}\le1,
\qquad
T_{r-1}D_J=\sqrt{rS}\,T_r.
\tag{2.3}
$$
这就是对所有实际远尾向量均成立的收缩行，不要求输入在创建像内。

先施加 $P_{\rm gap}$、识别单位暗张量因子、再在远尾施加 $T_r$，得到原第 $q+t$ 层到测试模型第 $t$ 层的算子 $\mathcal A_t$。各头占据分量正交，故
$$
\|\mathcal A_t\|\le R,
\qquad \mathcal A_0f=\Omega.
$$
测试模型是一个真实强位加一个单玻色模，下降为
$$
\mathcal L=aE+bb_{\rm osc},\qquad
b_{\rm osc}e_r=\sqrt r\,e_{r-1}.
$$
由 (2.3)，准确交织为
$$
\boxed{\mathcal A_{t-1}D=\mathcal L\mathcal A_t.}
\tag{2.4}
$$
它保留全部原未选位的费用；没有把一个 $D$ 不变小空间内的最小逆当成完整原空间最小逆。

## 3. 真实第一步便宜，迫出顺次第二步的高费

将强位置为一孔、其余保持 (1.2)，得到原向量
$$
v_1=a^{-1}|1\rangle_m\otimes h_{\rm gap}\otimes\Omega_J,
\qquad Dv_1=f,
\qquad\|v_1\|=a^{-1}.
$$
所以真正第一步最小者满足
$$
\|u_1\|\le a^{-1}.
\tag{3.1}
$$
写其测试像为
$$
\mathcal A_1u_1=x\,|1,0\rangle+y\,|0,1\rangle.
$$
由 (2.4) 和 (3.1)，
$$
\boxed{ax+by=1,\qquad |y|\le R/a.}
\tag{3.2}
$$
这里没有假定 $\mathcal A_1u_1$ 是测试模型的单步最小原像；只使用真实原最小者的已付范数。

测试模型第2层的完整正交基为 $|1,1\rangle,|0,2\rangle$。若
$$
\mathcal A_2u_2=z\,|1,1\rangle+w\,|0,2\rangle,
$$
则 $Du_2=u_1$ 及 (2.4) 迫
$$
bz=x,\qquad az+\sqrt2\,bw=y.
$$
这个二乘二三角矩阵可逆，所以
$$
\boxed{w=\frac{by-ax}{\sqrt2\,b^2}
=\frac{2by-1}{\sqrt2\,b^2}.}
\tag{3.3}
$$
由 $S\le1/(3J^3)$、$J\ge q\ge16(m+1)^2$、$R<2$，有
$$
\frac{2Rb}{a}
\le\frac{4(m+1)^2}{\sqrt3 J^{3/2}}<\frac12.
$$
因此 (3.2)--(3.3) 给
$$
|w|\ge\frac{1-2Rb/a}{\sqrt2 b^2}
\ge\frac1{2\sqrt2 S}.
$$
再用 $\|\mathcal A_2u_2\|\le R\|u_2\|$，得到
$$
\boxed{\|u_2\|\ge\frac1{2\sqrt2 R S}.}
\tag{3.4}
$$
事实上，这个下界对任何先取范数至多 $a^{-1}$ 的第一步原像、再取其任意第二步原像都成立；因此它尤其适用于顺次两个真实 MP。

## 4. 真二次幂有一个便宜得多的原候选

原远尾单位一孔向量
$$
v_J=D_J^*\Omega_J/b
$$
满足 $D_Jv_J=b\Omega_J$、$D_J^2v_J=0$。所以
$$
v_2=\frac1{2ab}|1\rangle_m\otimes h_{\rm gap}\otimes v_J
$$
准确满足
$$
D^2v_2=f,
\qquad\|v_2\|=\frac1{2ab}.
$$
两次删除中的系数 $2$ 来自不同头尾位的两个次序，全部保留。因此
$$
\boxed{\|g\|\le\frac1{2a\sqrt S}.}
\tag{4.1}
$$
将 (3.4) 和 (4.1) 合并，
$$
\mathcal C(f)\ge
\frac{1/(8R^2S^2)}{1/(4a^2S)}
=\frac{a^2}{2R^2S}.
$$
又 $R<2$、$S\le1/(3J^3)$、$J\ge2q$，得到 (1.4)。

$f\in K_q$ 正是 $C_{2,3,q+2}$ 的合法整个 primitive 源空间中的一个单位向量；该常数是同源能量比的上确界，故得到 (1.5)。没有把顺次／真幂比较误认作相邻高度 Gram 比较。

## 5. 同一个首头源的裸二阶 jet 费用准确放大

取
$$
h=Dg\in E_{2,q+1}.
\tag{5.1}
$$
因为 $D^2g=f$ 且 $Df=0$，所以 $D^2h=0$；又 $g\perp\ker D^2$，特别 $g\perp\ker D$，因此
$$
R_{q+2}h=g.
\tag{5.2}
$$
真实二阶 jet 次数算子是
$$
\mathfrak N_{2,q+1}=I+R_{q+1}D
\quad\text{在 }E_{2,q+1}\text{ 上}.
$$
从 $Dh=f$，得到
$$
R_{q+2}\mathfrak N_{2,q+1}h=g+u_2.
\tag{5.3}
$$
同时 $D^2u_2=D^2g=f$，所以 $u_2-g\in\ker D^2$；真正二步最小性使它与 $g$ 正交。于是
$$
\boxed{\|g+u_2\|^2=3\|g\|^2+\|u_2\|^2.}
\tag{5.4}
$$

对原有限头的第一坐标 $e_0$，已有准确同源身份
$\alpha_{q+1}(e_0z)=\lambda_{q+1}(e_0z)=\|R_{q+2}z\|$。
因此在参数还位于原合法窗口时，(5.2)--(5.4) 给
$$
\boxed{
\frac{\alpha_{q+1}(e_0\mathfrak N_{2,q+1}h)^2}
{\alpha_{q+1}(e_0h)^2}
=3+\mathcal C(f)
\ge3+\frac{3q^3}{(m+1)^4}.
}
\tag{5.5}
$$
两个首头源的完整右费用 $\lambda$ 也满足同一身份。这里使用同一个明确 $h$，不是通过两次独立上确界替换源。

普通物理范数中 $\|\mathfrak N_2\|=2$ 仍然成立；(5.5) 是在真实裸源度量中的放大，并不矛盾。它给出旧精确二步 Schur 常数在原连续尾高孔层实际增长的下界。

## 6. 尚未外推的范围

这些是原 $D_m$、原 Hilbert 范数和完整 MP 中的结论，不是有限三权的直接删位移植。它们排除原全部短核源上与孔数无关或仅为次幂的顺次／真幂比较，以及全部 $E_2$ 首头源上与孔数无关或仅为次幂的裸 $\mathfrak N_2$ 算子范数预算；不排除更大的明确多项式预算。

但本文没有证明 (5.1) 的 $h$ 来自真实 $M$ 图、原实际残量族或原最优 Schur 来源；也没有把 (5.5) 外推给 $\lambda_{\rm flat}$。同源两费用图中的额外约束仍须保留。

本稿亦不反驳真实相邻 primitive Gram 常数一：顺次 MP 链与真幂 MP 的差，正是前述完整二步 Schur 所投掉的自由方向，不能由一个相邻高度常数免费支付。原无权 $N=M$ 与普通 ISP 均未由本稿解决。
