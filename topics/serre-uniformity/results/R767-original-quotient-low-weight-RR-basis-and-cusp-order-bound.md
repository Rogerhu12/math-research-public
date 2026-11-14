# R767：原商曲线的权二生成、权十二 Riemann–Roch 基与真实尖点阶界

日期：2026-11-14。状态：**本篇证明原商的一个显式有限低权生成定理，并把实际 R759 的 $d=1206$ 映射恢复落实到 1514 个权十二模形式的基。** 具体的 Eisenstein 种子、基的有限秩证书及恢复出的 $y$ 函数仍须公开计算；本篇不将它们预称为已返回结果。

原 R759 run [43625474728](https://github.com/Rogerhu12/math-research-public/actions/runs/43625474728)、source
$\,\mathtt{4728e6868e2509556e5c60e138fd97c9b4120d8e}\,$ 已实际成功。其小证书 SHA-256 为
$\,\mathtt{7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0}\,$。
本篇使用它的原第 4 号整数格基映射（从 0 编号），其次数是 1206；没有声称它在整个格里全局最短。

## 1. 固定原模型与将得到的有限数据

保持 R762 的
$$
X=X_1,\quad Y=X/\mu_3,\quad t=a^3,\quad
K=\mathbf Q(\zeta),\quad s=1+2\zeta,\quad \alpha=\sqrt[3]4,
\quad j=6912t(1-t).
\tag{767.1}
$$
原 $c_0$ 和 $c_1=4424$、原参考 cusp、原 $g_*$ 运输、R735 的正目标
$C/L:y^2=x^3+b$ 均不改变。写 $M=K(U)=L(\xi)$，
$\xi=e^{2\pi i/41}$，沿用 R751 的原正根和原 $U$ 分支。

令 $\mathcal D$ 是 $Y$ 上 20 个 cusp 的约化和。令 $P_0,P_1$ 是 $Y$ 上的两个阶 3 椭圆点：前者在 $t=0$，是原 $c_0$ 的像；后者在 $t=1$，是原 $c_1$ 的三点 deck 轨道在 $Y$ 的像。置
$$
E=P_0+P_1,\qquad \mathcal L=K_Y+\mathcal D.
\tag{767.2}
$$
这里 $K_Y$ 表示典范除子类，后续 $H^0(r\mathcal L)$ 与线丛记号等价。

本篇的主要等式是
$$
\boxed{\begin{aligned}
M_{12}(\Gamma_Y)
={}&H^0(6\mathcal L)
+E_4\,H^0(4\mathcal L)
+E_6\,H^0(3\mathcal L)\\
&+E_4E_6\,H^0(\mathcal L)
+\langle E_6^2,\ E_6\eta_{\rm Ded}^{12}\rangle.
\end{aligned}}
\tag{767.3}
$$
其中 $H^0(r\mathcal L)$ 由 $r$ 个真实权二模形式的乘积张成。
等号是向量空间的和，不是将相交部分错误计作直和。
记 $\eta_{\rm Ded}$ 为 Dedekind eta；它与 R762 的亚纯微分 $h/a$ 不同。

权二空间维数为 146，$H^0(6\mathcal L)$ 维数为 1506，(767.3) 的总空间维数为 1514。故高权部分只须补八个椭圆点主部方向；不需要枚举全部十二次 Eisenstein 乘积。

## 2. 原 $\Gamma_Y$ 与两个椭圆点

在 $\mathbf C$ 上，原 level-six graph 的几何群是
$\{(\theta(g_3),g_3):g_3\in\operatorname{SL}_2(\mathbf F_3)\}$，
其中 $\theta$ 的核是 $Q_8$、像为模 2 的阶 3 群。加入原 deck $\delta=T^{82}$ 后，得到模 2 的 $C_3$ 与模 3 的整个 $\operatorname{SL}_2(\mathbf F_3)$ 的直积。于是商的几何同余群准确为
$$
\Gamma_Y=
\{\gamma\in\operatorname{SL}_2(\mathbf Z):
 \gamma\bmod2\in\langle C\rangle,\quad
 \gamma\bmod41\in N_{\mathsf T_\zeta}\cap\operatorname{SL}_2(\mathbf F_{41})\},
\quad C=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\tag{767.4}
$$
本篇在 $M\supset K$ 中使用原参数识别，所以没有将原有理三次扭曲或原 $t$ 替换成未标记的标准模型。

该群的 level 为 82。其在 $\operatorname{SL}_2(\mathbf Z/82\mathbf Z)$ 中的像记为 $H_{82}$：
$$
|H_{82}|=3\cdot84=252,\qquad
[\operatorname{SL}_2(\mathbf Z):\Gamma_Y]=1640.
\tag{767.5}
$$
$-I\in H_{82}$；有效的 $\operatorname{PSL}_2$ 平均群阶为 126。
这里是原 $\mathsf T_\zeta$ 的正规化子，不能任意换一条未同步运输的环面。

R762 已从原固定点与 cusp 轨道证明
$$
g(Y)=127,\qquad |\mathcal D|=20,\qquad
(t)_\infty=41\mathcal D.
\tag{767.6}
$$
原 cusp 参数是
$$
q_Y=e^{2\pi i\tau/82}=Q^3,\qquad Q=e^{2\pi i\tau/246}.
\tag{767.7}
$$
模 2 的 $C_3$ 不含阶 2 椭圆元，因此没有阶 2 椭圆点。R762 的原非分裂正规化子计数在 $Z=X_{\rm ns}^+(41)$ 上给出唯一 $j=0$ 非分歧点；经 $j=6912t(1-t)$ 的两个分支，它在 $Y$ 上给出恰好 $P_0,P_1$ 两个阶 3 椭圆点。其余 $j=0$ 点局部 $j$ 次数为 3，是普通点。也可由
$$
127=1+\frac{1640}{12}-\frac{2}{3}-\frac{20}{2}
$$
核对计数，但不以这条亏格公式代替原 $t=0/1$ 的标记证明。

## 3. 模形式与粗曲线线丛的准确对应

对任意整数 $r\ge1$，把权 $2r$ 模形式视为 $r$ 次微分，可得
$$
\boxed{
M_{2r}(\Gamma_Y)
=H^0\!\left(r\mathcal L+
           \left\lfloor\frac{2r}{3}\right\rfloor E\right).
}
\tag{767.8}
$$
说明局部阶数如下。在一个阶 3 椭圆点附近取上半平面坐标 $z$，稳定子作用 $z\mapsto\zeta z$，粗参数 $w=z^3$。一个不变 $r$ 次微分的首项写成 $z^u(dz)^r$，满足 $u+r\equiv0\pmod3$。取最小非负 $u$，换成 $dw$ 后恰允许
$\lfloor2r/3\rfloor$ 阶极点。反之，这个范围的粗曲线亚纯微分拉回后全纯。在 cusp，$d\tau$ 是 $dq_Y/q_Y$ 的非零常数倍，因而允许至多 $r$ 阶极点；其他点不允许极点。这证明 (767.8)。

特别是
$$
M_2=H^0(\mathcal L),\qquad
\deg\mathcal L=2\cdot127-2+20=272,\qquad
\dim M_2=272+1-127=146.
\tag{767.9}
$$
$H^1(r\mathcal L)=0$ 对全部 $r\ge1$ 成立，所以
$$
\dim H^0(r\mathcal L)=272r-126.
\tag{767.10}
$$
而权十二对应
$$
\mathcal W=6\mathcal L+4E,\qquad
\deg\mathcal W=1640,\qquad
\dim M_{12}=1640+1-127=1514.
\tag{767.11}
$$

$\deg\mathcal L=272\ge2g(Y)+2$。高次数线丛的正常生成定理因而给出
$$
\operatorname{Sym}^rH^0(\mathcal L)\twoheadrightarrow H^0(r\mathcal L)
\quad(r\ge1).
\tag{767.12}
$$
本篇只对这个没有额外椭圆点极点的子空间应用正常生成；不把
$M_{2r}$ 全部误作 $H^0(r\mathcal L)$。
可用的 primary 依据是 Khuri-Makdisi 原文 Theorem 5.1 证明中所用的高次数乘法满射，以及同文 Definition 5.2 后的次数至少 $2g+2$ 的曲线表示；该文明确将标准乘法结论指向其 earlier Lemma 2.2。

对后续实现，所需六个维数依次是
$$
146,\ 418,\ 690,\ 962,\ 1234,\ 1506.
\tag{767.13}
$$
它们是理论目标维数，尚不是本篇中新运行的秩数据。

## 4. $E_4,E_6,\eta_{\rm Ded}^{12}$ 的真实局部主部

设
$$
\mathcal E=\eta_{\rm Ded}^{12},\qquad \Delta=\mathcal E^2.
\tag{767.14}
$$
这里 $\mathcal E$ 权为 6。Dedekind eta 的 $S,T$ 变换给
$$
\mathcal E|_6S=-\mathcal E,\qquad
\mathcal E|_6T=-\mathcal E.
\tag{767.15}
$$
这个二阶角色正是 $\operatorname{SL}_2(\mathbf F_2)\simeq S_3$ 的符号角色，因此在 (767.4) 的模 2 $C_3$ 上平凡。故
$$
\mathcal E\in M_6(\Gamma_Y)
$$
是该曲线的真实模形式，并非偷偷加入另一个角色的形式。
其原 cusp 展开是
$$
\mathcal E=q_Y^{41}\prod_{m\ge1}(1-q_Y^{82m})^{12}.
\tag{767.16}
$$
它在上半平面无零点，在每个原 cusp 的零阶为 41。

在 $P_0,P_1$ 的上半平面坐标中，$E_4$ 恰有一个简单零，$E_6$ 和 $\mathcal E$ 都非零。结合 (767.8)，作为相应的粗曲线次数微分：

- $E_4$ 在两点都恰有一阶主部；
- $E_6$ 在两点都恰有二阶主部；
- $\mathcal E$ 在两点都恰有二阶主部。

没有声称它们在 $\mathcal L$ 的相应次幂中全纯；正是这些主部补齐高权空间。

由 R745 的原展开，使用 $\alpha^3=4$，得到准确全局恒等式
$$
t=\frac12-\frac{sE_6}{144\mathcal E},
\qquad
\boxed{\frac{E_6}{\mathcal E}=24s(2t-1)}.
\tag{767.17}
$$
因此
$$
(E_6/\mathcal E)(P_0)=-24s,\qquad
(E_6/\mathcal E)(P_1)=+24s.
\tag{767.18}
$$
这保留了原 $t=0$ 的 $c_0$ 与 $t=1$ 的原 $c_1$ 轨道，不交换两个点来隐藏相位。

## 5. 权十二空间只须补八个方向

记
$$
A_r=H^0(6\mathcal L+rE),\qquad 0\le r\le4.
$$
因这些线丛的次数都大于 $2g-2$，每一步 $A_r/A_{r-1}$ 都是两维，由 $P_0,P_1$ 处恰 $r$ 阶的最高主部组成。

对任意 $k\ge1$，
$$
H^1(k\mathcal L-E)=0
$$
因为其次数至少 $272-2=270>252$。故 $H^0(k\mathcal L)$ 在这两个点的纤维评价满射。利用 §4 的非零最高主部：

- $E_4H^0(4\mathcal L)$ 向 $A_1/A_0$ 满射；
- $E_6H^0(3\mathcal L)$ 向 $A_2/A_1$ 满射；
- $E_4E_6H^0(\mathcal L)$ 向 $A_3/A_2$ 满射。

余下 $A_4/A_3$ 的两个方向由 $E_6^2$ 和 $E_6\mathcal E$ 给出。
在每个点同时以最高主部系数表示它们。行列式等于一个非零公共局部因子，乘以
$$
(E_6/\mathcal E)(P_0)-(E_6/\mathcal E)(P_1)=-48s\ne0.
\tag{767.19}
$$
故最后两方向也独立。逐层合并即证明 (767.3)。

于是可以先从权二的乘积选出 1506 个 $H^0(6\mathcal L)$ 基元素，再从上面四个明确小族中各补两个方向；基的具体选取可由单个原 cusp 的有限系数秩认证。不必先算两椭圆点的高阶代数参数。

## 6. 原 $D=2(t)_0$ 的实际 Riemann–Roch 基

作为 $\mathcal W$ 的 section，$\Delta$ 在椭圆点没有额外零：它在上半平面非零，允许的四阶粗极点已恰由 $\mathcal W$ 吸收。它的零除子准确是
$$
\operatorname{div}_{\mathcal W}(\Delta)=82\mathcal D.
\tag{767.20}
$$
用原 $(t)_\infty=41\mathcal D$，得到
$$
\boxed{
\operatorname{div}_{\mathcal W}(t^2\Delta)=2(t)_0.
}
\tag{767.21}
$$
因此，若 $F_1,\ldots,F_{1514}$ 是任一由 (767.3) 得到的真实权十二基，则
$$
\boxed{
\left\{\frac{F_i}{t^2\Delta}:1\le i\le1514\right\}
\text{ 是 }L\bigl(2(t)_0\bigr)\text{ 的一个基。}
}
\tag{767.22}
$$
该结论包括椭圆点的全部极点补偿，不能只由 cusp 的阶数猜测。

而分母本身有非常小的原公式：
$$
\boxed{
t^2\Delta=
\left(\frac{\mathcal E}{2}-\frac{sE_6}{144}\right)^2.
}
\tag{767.23}
$$
在原参考 cusp，其常数项是
$$
-\frac1{6912}\ne0.
\tag{767.24}
$$
所以同一 cusp 上不发生额外分母零或参数平移。实际恢复 $y$ 时，共同分母完全消掉：
$$
y_P=\frac{\sum_i A_iF_i}{\sum_i B_iF_i}.
\tag{767.25}
$$
这些是真实模函数的表达；没有先假定一个未知的 genus-127 平面模型。

实际选中映射的 $d=1206$ 给
$$
\deg 2(t)_0=1640,\quad
1640-d=434>2g(Y)-2,\quad
M_Y=1640+d=2846.
\tag{767.26}
$$
故 R762 的 $m=2$ 除子正是本节的除子。分母乘子空间维数准确为
$$
h^0\bigl(2(t)_0-(y_P)_\infty\bigr)
=434+1-127=308.
\tag{767.27}
$$
因而 (767.25) 的完整有限线性系统在特征零中的核维数是 308，秩为
$2\cdot1514-308=2720$。这也是有真实次数和完整前缀后可用的成功条件，尚未冒称该线性系统已经执行。

## 7. 原权二基的完全明确有限 Eisenstein 输入

令 $N=82$，取
$$
\xi_N=e^{2\pi i/82}=-\xi^{21}.
\tag{767.28}
$$
这明确固定解析正向，不用任意原始根替换原 $\xi$。
对 $(a,b)\in(\mathbf Z/N\mathbf Z)^2$，取 Hecke 正则化的权一 Eisenstein series $E_{a,b}^{(1)}$，采用 Zywina Lemma 4.7 的规范：
$$
E_{a,b}^{(1)}
=c_0(a,b)+
\sum_{\substack{m,n\ge1\\m\equiv a\ (N)}}\xi_N^{bn}q_Y^{mn}
-\sum_{\substack{m,n\ge1\\m\equiv-a\ (N)}}\xi_N^{-bn}q_Y^{mn},
\tag{767.29}
$$
其中 $0\le a<N$，且
$$
c_0(a,b)=
\begin{cases}
0,&a=b=0,\\
\frac12\frac{1+\xi_N^b}{1-\xi_N^b},&a=0,\ b\ne0,\\
\frac12-\frac aN,&a\ne0.
\end{cases}
\tag{767.30}
$$
行向量作用满足
$$
E_\lambda^{(1)}|_1g=E_{\lambda g}^{(1)}.
\tag{767.31}
$$

对两个非零标签 $\lambda,\mu$，定义精确有限形式
$$
F_{\lambda,\mu}
=\frac12\sum_{g\in H_{82}}
E_{\lambda g}^{(1)}E_{\mu g}^{(1)}.
\tag{767.32}
$$
由于 $E_{-\lambda}^{(1)}=-E_\lambda^{(1)}$，可用 $H_{82}/\{\pm I\}$ 的 126 个代表计算此和；代表改变不影响乘积。它定义于 $\mathbf Q(\xi_N)$，扩到 $M$ 后是原 $Y$ 的权二模形式。

**完整性在权二也没有例外。** Khuri-Makdisi, *Moduli interpretation of Eisenstein series*, Theorem 5.1（arXiv:0903.1439v6）对 $\Gamma(N)$ 给出权一 Eisenstein series 生成的代数包含全部权数 $\ge2$ 的模形式。Zywina, *Explicit open images for elliptic curves over Q*, Theorem 4.9 和 Corollary 4.10(i)，明确给出同一命题的 $\mathbf Q(\xi_N)$ 线性版本：权二空间由两个权一 Eisenstein series 的乘积张成。取 (767.32) 的有限群迹，因 characteristic 0 的平均满射到不变子空间，得到
$$
\boxed{\operatorname{span}_{M}\{F_{\lambda,\mu}\}=M_2(\Gamma_Y,M)}.
\tag{767.33}
$$
没有附加“中心 $L$ 值非零”的权二 cuspform 条件。不能用仅对 $\Gamma_1(N)$ 的某个 toric 子空间结论替代这里的 full-level 定理。也没有直接使用原始权二 Eisenstein series $E_\lambda^{(2)}$，故不存在把其非全纯公共项误当模形式的问题；使用的是两个真正全纯的权一形式的乘积。

这给出一套有限、具体且任意 Fourier 前缀可直接计算的候选函数。Khuri-Makdisi 同文 §3 的 torsion-slope 模解释也保证这些形式是代数的，不仅是数值分析对象。

## 8. 有限秩证书如何成为实际基

下列是后续公开计算可以直接使用的流程，不是预填成功结果：

1. 按原 (767.4) 构造 $H_{82}$；不重算 R738 的陪集、树或周期。枚举 (767.32) 的有限种子，精确记录两个原标签和群代表规范。
2. 用 (767.29) 计算原 $q_Y$ 系数，从候选中选出秩 146。单个 cusp 的系数到 $q_Y^{273}$ 是一个安全的有限分离界；事实上 $H^0(\mathcal L)$ 的 section 次数为 272。
3. 用 (767.12) 逐次乘法得到 (767.13) 的六个基，并记录每个元素在较低次基中的乘积 recipe。
4. 用 (767.3) 的四个补充族，选取全部 1514 个元素；其 $q_Y^0,\ldots,q_Y^{1640}$ 系数足以认证独立。理由是非零 $\mathcal W$ section 的零次数至多 1640。
5. 将选出的符号 recipe 保留成精确 characteristic-zero 模形式，再按 (767.23) 给出整个 $L(2(t)_0)$ 基。后来扩展前缀只执行缺失的系数，不重做已经得到的有限秩选择。

可用一个分裂辅助素数的非零 minor 来认证特征零独立。例如 R745 已固定的 $\ell=739$、$\xi\mapsto538$ 给 $\xi_N=-538^{21}$。必须现场验证其阶为 82，并保每个种子的实际秩证书；本篇不预言这个素数上的运行一定完成。式 (767.30) 的全部分母在该嵌入处为单位，因为 $\ell\nmid2N$ 且非平凡 $\xi_N^b$ 不变成 1。于是一个真实非零的 146 或 1514 阶 minor 模 $\ell$ 足以证明相应精确函数在 characteristic zero 线性独立，再由已证维数得到完整基。若所选素数未达秩，不得补填；应继续有限种子或更换一个完整记录的合法素数。

一个可选的乘法加速也有完整证据：若 $u,v\in H^0(\mathcal L)$ 满足
$$
uH^0(2\mathcal L)+vH^0(2\mathcal L)=H^0(3\mathcal L),
\tag{767.34}
$$
则 $u,v$ 无共同零点，否则右侧所有 section 都在该点为零，违背 $3\mathcal L$ 的全局生成。由 base-point-free pencil 的正合列及
$H^1((r-2)\mathcal L)=0$，对全部 $r\ge3$ 有
$$
H^0(r\mathcal L)
=uH^0((r-1)\mathcal L)+vH^0((r-1)\mathcal L).
\tag{767.35}
$$
因此一次实际秩 690 的检查即可认证以后只乘两个固定形式的加速。不把未经检查的两个随机形式当作无基点 pencil。

## 9. 原 cusp 的 $e\le19$ 与明显更短的实际前缀

本节使用的是 R745 真实 Fourier 小证书，而非有限 40 坐标向量的秩，也不是 CM 点的 jet。
该证书来自 run 43616027318，
SHA-256
$\,\mathtt{7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be}\,$。
其字段准确记录原同一参考 $Q$ 的六个指数
$$
(1,4,7,13,16,19),
$$
对应 R745 (745.18) 的六列 $\omega_j$；去掉每行非零公共因子后，实际 minor 在
$\ell=739,\xi\mapsto538,s\mapsto98$ 下的行列式为 $407\ne0$。

R745 的原微分式是
$$
\omega_j=\frac{\alpha}{7}
\left(\sum_{n\ {\rm odd}}sP_{j,n}(\xi)Q^n+
      \sum_{4\mid n}3P_{j,n}(\xi)Q^n\right)\frac{dQ}{Q}.
\tag{767.36}
$$
因此被移去的因子是 $\alpha s/7$ 或 $3\alpha/7$，均非零。
这正是同一参考 cusp 的系数矩阵；不是另一个点或未乘原相位的平移矩阵。

该 $6\times6$ 矩阵在其数域中满秩，扩到 $L(\alpha,\xi)$ 后仍满秩。
故任意非零
$h=\sum v_j\omega_j$，$v_j\in L$，不可能同时令上述六个实际 Fourier 系数全零。
其以参考 cusp 为零的 primitive $I$ 逐项除以非零整数 $n$，不改变首个非零指数。所以
$$
\boxed{e=\operatorname{ord}_QI\le19}.
\tag{767.37}
$$
目标平移不改变不变微分，而在目标原点它是单位，因此该 $e$ 正是 $f_P$ 在参考 cusp 的局部次数。没有把该 cusp 认作 $c_0$，也没有先假设 $f_0(P)=O$。

对实际 $d=1206$ 与 $M_Y=2846$，R762 的完整恒等式证明因而可直接使用
$$
\boxed{
F_i\text{ 的原 }q_Y\text{ 系数至 }2846,\qquad
h/dQ\text{ 的原 }Q\text{ 系数至 }8557.
}
\tag{767.38}
$$
这里还利用参考 cusp 的 $e$ 阶极点从全局极点次数中准确扣除；完整证明在下一节。统一 Hodge 界是 $3\cdot2846+19=8557$。若实际首先算出的 $e$ 更小，还可据真实 $e$ 缩短；本篇保留统一界 19。
在同一参数中用精确
$y_b(\alpha J)=\frac14y_{16b}(J)$，保 R762 的 $1/4$ 与原 $b$ 不变。

## 10. 从基到一个真实函数的有限完成条件

假设公开计算已给出 (767.22) 的真实基，并按 (767.38) 得到原 $y_P$ 的 Laurent 前缀。
解
$$
[q_Y^n]\left(\sum_i A_iF_i-y_P\sum_i B_iF_i\right)=0,
\qquad -e\le n\le2846-e.
\tag{767.39}
$$
令参考 cusp 仍记为 $P$，并写
$$
(y_P)_\infty=eP+E',\qquad \deg E'=1206-e.
\tag{767.40}
$$
$t^2\Delta$ 在 $P$ 是单位，故可以等价地将 (767.39) 除以这个固定 section，写成
$A-y_PB$，其中 $A,B\in L(D)$、$D=2(t)_0$ 且 $P\notin\operatorname{supp}D$。
在 $P$ 外，它的极点次数至多
$$
\deg(D+E')=1640+1206-e=2846-e.
$$
(767.39) 先消掉 $P$ 的全部负次项，再令其在 $P$ 至少有 $2847-e$ 阶零，故必恒为零。
等价地，原权十二表达此时是 $\mathcal W+E'$ 的 section；其次数同样只有 $2846-e$。
这给出 (767.25) 的完整代数恒等式，且非零解必有 $\sum B_iF_i\ne0$。

这个扣除也给出更短且准确的前缀。为计算到 $n=2846-e$，权十二基只需到
$(2846-e)+e=2846$；$y_P$ 只需到 $q_Y^{2846-e}$。原 $y_b(I)$ 的首项是 $-I^{-3}$，
若 $\operatorname{ord}_Q I=e$，要算到 $Q^{3(2846-e)}$，只需 $I$ 到
$$
Q^{\,3(2846-e)+4e}=Q^{\,3\cdot2846+e}.
\tag{767.41}
$$
故 $h/dQ$ 到相同指数已经充分（比求导所需的紧界还多保留一项）。由 $e\le19$ 得 (767.38)。
线性方程的指数范围 $-e,\ldots,2846-e$ 总共恰有 2847 行，与 $e$ 无关；
不能将 $e$ 扣除两次，也不能先删去仍可能存在的负次项。

随后只用 R762 原
$$
x_P=a\,\frac{3(y_P^2-b)(h/a)}{dy_P}
$$
恢复第二坐标，按 R764 的准确三个平移把基点译回 $c_0$，最后在原 $c_1$ 分支求 $\beta$。
本篇没有提前提供这三个输出，也没有把 cusp 基或 Abel 不回零结论当作真实高度排根。

## Primary 依据及已完成原证书

- K. Khuri-Makdisi, *Moduli interpretation of Eisenstein series*, arXiv:0903.1439v6, Theorem 5.1、其证明中的高次数乘法、Definition 5.2 及 §3：[原文](https://arxiv.org/pdf/0903.1439)。
- D. Zywina, *Explicit open images for elliptic curves over Q*, Lemma 4.7、Theorem 4.9、Corollary 4.10 和 §4.8：[作者稿](https://pi.math.cornell.edu/~zywina/papers/ExplicitOpenImage.pdf)。
- [R738](R738-certified-original-p41-period-input.md)、[R745](R745-certified-original-p41-Hodge-and-adelic-input.md)：原群、参考 cusp、标记和实际 Fourier minor。
- [R762](R762-original-mu3-quotient-and-single-function-map-recovery.md)：原商、21 个固定点、精确 $y$ 恢复及平移。
- [R759 原实际证书](../computations/R759-original-integral-period-lattice-and-map-degrees/43625474728-1/p41-original-integral-period-lattice-and-degree-certificate.json)：真实第 4 个映射及 $d=1206$，完整 Hom 格与原交配验证。
