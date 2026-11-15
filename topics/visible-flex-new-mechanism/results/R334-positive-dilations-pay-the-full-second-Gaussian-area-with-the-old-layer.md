# R334：正伸缩与四个真实面积方向同时支付完整第二面积及旧一层

日期：2026-11-15。**完整纸面建设性证明。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R331](R331-interior-constant-and-wide-moment-repair-pay-the-new-area-and-old-layer.md) 已支付带内部常项的真实弱圆上的新面积第零外矩；[R332](R332-true-translation-and-reflection-pay-the-next-Gaussian-area-moment.md) 又证明同一构造的第1外矩也准确为零。本稿支付余下的第2外矩，并保持旧面积的全部三矩、三条 directed 行与指定完整一层。

关键是两个不同的准确齐次次数。真实 $I_2$ 面积按正伸缩 $\Lambda^{-5}$ 变化，而原兼容量 $\Psi$ 按 $\Lambda^{-7}$ 变化。因此，可以用四个真实强模块支付任意两维 $I_2$ 目标，同时把新增的正 $\Psi$ 压到一个已经严格为负的弱宏块所能承担的范围内。全部宽度、幅度与频率最后都取有限值。

本稿使用 [R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md) §§3–5 的实际两斜率族及母包形状局部图。没有使用其 §6 将 $\alpha$ 锁在六能量根上的最终分支，也不将那条分支的六能量零附加到本稿的新四个模块上。所付的是本文逐式列出的联合目标。

其他来源：[R259 原 self／cross 接口](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R280 真实完整强模块](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R293 初选有限观察与有限频率根](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、[R325 完整 directed 行与块加法](R325-inward-weak-hook-circles-pay-three-directed-rows-and-the-one-history-compatibility.md)，以及 R331、R332。

## 1. 同一实际几何、两个完整面积与目标

固定 R331 已经实际安装的有限闭 hook 几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
$$
及其共振端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\qquad
\varepsilon=\kappa^2/4,\quad 0<t:=\kappa^2<1/100.
\tag{1}
$$
$\kappa,h_e$ 始终固定。最后选择一个新的、足够大的有限共同正物理区间；不声称在任意先前冻结的窄 $I$ 内完成下述伸缩。

记
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},
$$
$$
W_*=aR+bS,\qquad Z_*=d_*L+e_*U,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\qquad
b=-\frac{17t^2+4t}{32h_e^2},
$$
$$
d_*=\frac{6\kappa^3}{h_e},\qquad
e_*=-\frac{\kappa(15t+1)}{4h_e}.
\tag{2}
$$
Gaussian $B_{-3}=c_PP$ 的 $c_P$ 非零。因此下面去掉这个公共因子不改变零条件。

对同一个最终实圆
$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u,
$$
使用原右锚 $J F(x)=\int_x^{r_*}F$，定义
$$
\mathfrak a_j(\theta)=2I_j\{u,[Z_*,P](u;D)\},\qquad j=0,1,2.
\tag{3}
$$
这里只是 R332 的 $A_j$ 的两倍，便于直接使用 R267 的 self 表。

本稿得到同一圆上、全部 $\theta$ 的
$$
I_j\{u,[W_*,P](u;D)\}=0,\qquad
\mathfrak a_j(\theta)=0,\qquad j=0,1,2,
\tag{4}
$$
$$
F_0=H_2^P=0,\quad F_1=aH_1^R+bH_1^S=0,\quad
F_2=d_*H_0^L+e_*H_0^U=0,\qquad \Psi_\theta=0,
\tag{5}
$$
其中
$$
H_j^X=-I_j(XD,PD)+2I_j\{u,X(u,PD)\}.
$$
兼容量采用 R325/R331 的完整规范：
$$
\Psi_\theta=\frac{N(t)}{24P_0(t)}D_4(\theta)
+J_\theta+\frac7{12}C_\theta,
\tag{6}
$$
$$
D_4=\int\{(f'')^2-(u'')^2\}^2,\quad
C_\theta=\int(u'')^2\{(f'')^2-(u'')^2\},
$$
$$
J_\theta=\int(u'f''-f'u'')u''f''',
$$
$$
N(t)=16+184t-1713t^2-2475t^3-4590t^4,
$$
$$
P_0(t)=8+114t-169t^2+231t^3-612t^4.
$$
$N,P_0>0$ 在本稿参数区间成立。由 R325 的原完整 local／chain／history 恒等，(5)使
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\theta}=0
\quad\text{对全部 }\theta.
\tag{7}
$$

## 2. 保留真实宽过渡成本的负基块

取 R331 §7 的阶段性宏块 $\mathcal B_-$，即尚未加入最后正 $\Psi$ 控制宏块以前的真实对象。它已经包含：

- 带内部常数 $c(L)=O(L)$ 的真实幂曲段；
- 宽度 $R=\eta L$ 的实际 cutoff 与三个宽 rank-one 矩补包；
- 旧面积的全部强补偿、八完整副本、镜像与十二副本。

R331 的全部面积方程先被准确求解，其后才以
$$
R^{-1}+c(L)^2R^{-4}+c(L)^4R^{-7}=O(L^{-1})
$$
证明成本界。取一个足够大但有限的 $L$ 后，这个实际块固定，且
$$
\Psi_\theta(\mathcal B_-)=-\Delta\sin^2\theta,\qquad \Delta>0.
\tag{8}
$$
原三矩、完整三阶及旧面积三矩全部成立。R332 §§4–5 的真实反射与算子平移证明，还给
$$
\mathfrak a_0(\mathcal B_-)=\mathfrak a_1(\mathcal B_-)=0.
\tag{9}
$$
这一步适用于该阶段性宏块，并不需要先加最后强控制器。

$\mathfrak a_2$ 是真实有限积分，包含内部常项、所有宽过渡和补包。其全部 odd 相位已经由十二完整副本消去。原表达对 $u$ 为二次与四次的和，乘 $\cos^2\theta+\sin^2\theta=1$ 可写成四次齐次式；在 $\theta=0$，$D=0$。因此存在两个实际实数 $r_{22},r_{04}$，使
$$
\mathfrak a_2(\mathcal B_-)
=r_{22}\cos^2\theta\sin^2\theta+r_{04}\sin^4\theta.
\tag{10}
$$
没有把 $r_{22},r_{04}$ 当作可独立指定的形状积分。本稿将对这个实际两向量建立真实正幅右逆，所以不需要另假设它的符号、秩或近似值。

## 3. R267 原 self 与真正可用的两斜率族

置
$$
\lambda=-\frac56(d_*+7e_*)
=\frac{5\kappa(81t+7)}{24h_e}\ne0.
\tag{11}
$$
对实紧偶母包 $v$，记
$$
\mathsf C(v)=\int(v'')^4>0,\qquad
\nu(v)=
\frac{\int x^2(v'')^2+2\int(v')^2}{\int(v'')^2},
$$
$$
\begin{aligned}
\mathcal K_\kappa(v)={}&
\int x^2(v'')^4
-\frac{8(141t+11)}{5(81t+7)}\int xv'(v'')^3\\
&+\frac{48(15t+1)}{5(81t+7)}\int(v')^2(v'')^2
+\frac{16(15t+1)}{5(81t+7)}\int v(v'')^3,
\end{aligned}
$$
$$
\mathcal F_\kappa(v)=\mathcal K_\kappa(v)/\mathsf C(v)-\nu(v).
\tag{12}
$$
R267 从原算子与真实 Green 项给
$$
2I_2\{v,[Z_*,P](v;v^2)\}
=-\lambda\mathcal K_\kappa(v),
\tag{13}
$$
并给此 pair 的全部跨微包核为零：
$\Gamma_{P,L}=\Gamma_{P,U}=0$。该结论保留非紧单包二次输出的左尾，不能以“单包三矩为零”替代。

现在固定任意
$$
\frac13<\alpha<\frac12,\qquad
\beta=\frac{5-\alpha}{1-\alpha},\qquad
q=\frac1{16(1-\alpha)^2}.
\tag{14}
$$
取 $n=2^{11}$，低组 $64n$ 个实际母包宽 $q\delta$，高组 $n$ 个包宽 $\delta$，使用
$$
\eta_{w,\xi}(x)=w^{3/2}v((x-\xi)/w),
$$
以及低、高两组系数
$$
(a_i,b_i)=(\epsilon_i\sqrt{\alpha q},\sqrt q),\qquad
(a_i,b_i)=(\epsilon_i\sqrt\beta,1).
\tag{15}
$$
$\epsilon_i$ 为各组原 TM 符号。

两组真实中心具有相同均值。用未乘 $\delta$ 的中心方差记号，准确要求
$$
V_L-V_H=\nu(v)(1-q^2).
\tag{16}
$$
例如低组采用间距 $A$，高组采用间距 $B$，则取
$$
B^2=\frac{A^2((64n)^2-1)-12\nu(v)(1-q^2)}{n^2-1}.
\tag{17}
$$
选择 R256/R267 允许的充分大有限 $A$，再取充分小正 $\delta$，所有实际包严格不交。式(17)用同一个母包的真实 $\nu(v)$，不是独立调整二次矩。

等式
$$
64q(1-\alpha)=\beta-1
$$
与(16)支付两实对角的全部三矩；TM 的0、1、2阶消去支付三交叉矩。旧完整 $A_{-2,-3}$ 的四次张量是
$$
A_4=5C_{22},\qquad E_4=C_{22},\qquad B_4=D_4^{\rm tens}=0.
\tag{18}
$$
偶母包与实际中心矩使其另两位置条件也准确成立，正是 R267 §4 所使用的 R250 全角结论。此时并未令 $\mathcal F_\kappa=0$，也未求解 R267 的能量方程。

每个微包上 $f,g$ 成固定实比例，故整个强 hook 平面为零。随后采用原八完整复制支付第三 ruling，再采用十二完整复制清全部 odd 项。复制同时保留其真实四次权与位置；并未只在未包装基本包上计算目标。

## 4. 第零、第1矩恒零，第2矩是一条准确实直线

R267 原三 self 矩、(15)、(16)给
$$
\mathfrak a_0=\mathfrak a_1=0
\quad\text{对全部 }\theta.
\tag{19}
$$
对第2矩，写
$$
\mathfrak a_2=E_{22}\cos^2\theta\sin^2\theta+E_{04}\sin^4\theta.
$$
若 $\mathcal W>0$ 为全部八、十二实际副本的四次权和，则
$$
\boxed{
E_{04}=-\lambda\mathcal W n(\beta-1)\delta(1-q^2)
\mathsf C(v)\mathcal F_\kappa(v),\qquad
E_{22}=\alpha\beta E_{04}.
}
\tag{20}
$$
本稿(3)用两倍外矩并去掉 $c_P$，所以(20)正是 R267(18)去掉其公共 $c_P$ 后的规范，没有遗漏 $1/2$。

可直接核实第二个身份：在两种实际斜率上分别有
$$
\frac{\alpha(\alpha-5)}{\alpha-1}
=\frac{\beta(\beta-5)}{\beta-1}=\alpha\beta.
$$
因该 pair 的原 cross 核为零，两个 even self 系数具有这个准确比例。第一个身份来自
$$
\mathcal K_\kappa(\eta_{w,\xi})
=\xi^2\mathsf C(v)/w+w\mathcal K_\kappa(v),
$$
与(16)，保留了真实二次中心矩。

每次完整平移都会搬动原 $L,U$。R332 已证明，弱 hook 与旧三面积为零后
$$
(\mathfrak a_0,\mathfrak a_1,\mathfrak a_2)
\longmapsto
(\mathfrak a_0,\mathfrak a_1+s\mathfrak a_0,
\mathfrak a_2+2s\mathfrak a_1+s^2\mathfrak a_0).
\tag{21}
$$
由(19)，完整复制与最终搬移均不改变(20)，只乘各副本的正四次权。这是使用原算子平移式后的结论。

这些模块也准确满足
$$
J_\theta=0,\quad C_\theta=0,\quad
D_4(\theta)=4C_{22}\sin^2\theta.
$$
因此
$$
\boxed{\Psi_\theta=\psi\sin^2\theta,\qquad
\psi=\frac{N(t)}{6P_0(t)}C_{22}>0.}
\tag{22}
$$
(22)是完整量；没有使用三导 principal 或六能量零。

## 5. 用真实母包参数取得两个符号

这里不能只把 $\mathcal F_\kappa(v)$ 当作任意实坐标。使用 R267 §5 的真实三子包母形：
$$
v_{\gamma,s,h}(y)=
\gamma(sh)^{3/2}v_*(y/(sh))
+h^{3/2}v_*((y-\ell)/h)
+h^{3/2}v_*((y+\ell)/h),
\qquad \ell=\frac12,
\tag{23}
$$
其中 $v_*$ 是一个固定非零实偶紧母包，$\gamma,s>0$，$h>0$ 小，使三个子包严格不交。

R267 的原积分换元表明，仅归一标量 $\mathcal F_\kappa$ 在 $h=0$ 解析延拓，其值为
$$
\mathcal F_0=
2\ell^2\left\{
\frac1{\gamma^4s^{-1}+2}
-\frac1{\gamma^2+2}
\right\},
$$
且
$$
\left.\partial_\gamma\mathcal F_0\right|_{\gamma=s=1}
=-\frac{4\ell^2}{9}\ne0.
\tag{24}
$$
原两参数母图给充分小正 $h$ 的真实点
$(\gamma_h,s_h)=(1,1)+O(h^2)$，其 $\mathcal F_\kappa=0$，并且真实 $\partial_\gamma\mathcal F_\kappa$ 非零。

固定这样的一个正 $h$ 和 $s=s_h$，再在实际根两边取足够近的两个正 $\gamma$。得到两个实际实偶紧母包 $v^+,v^-$，使
$$
\mathcal F_\kappa(v^+)>0,\qquad
\mathcal F_\kappa(v^-)<0.
\tag{25}
$$
所有支撑仍具有正间隙。每次更换母包后，以其真实 $\nu(v^\pm)$ 重新使用(17)，所以三矩没有被破坏。

本稿在此只使用(24)的一维横截及原母图的真实正宽点。没有要求改变 $\gamma$ 后仍保原 $\mathcal H=0$ 或原六能量；那些条件不属于本稿四个面积模块的输入。

## 6. 四个实际正幅方向覆盖完整两维目标

选两个不同的固定
$\alpha_1,\alpha_2\in(1/3,1/2)$。
函数
$$
r(\alpha)=\alpha\beta
=\frac{5\alpha-\alpha^2}{1-\alpha}
$$
严格递增，因为
$$
r'(\alpha)=\frac{5-2\alpha+\alpha^2}{(1-\alpha)^2}>0.
$$
于是
$$
v_1=(r(\alpha_1),1),\qquad
v_2=(r(\alpha_2),1)
\tag{26}
$$
线性无关。

对每个 $\alpha_i$，用(25)的两个母包按 §§3–4 完成两个真实模块。按实际 $E_{04}$ 的正负重新命名，四个模块的 $I_2$ 向量为
$$
s_i^+v_i,\qquad -s_i^-v_i,\qquad s_i^\pm>0,\quad i=1,2.
\tag{27}
$$
所有低阶面积、旧三面积和完整三阶逐模块为零；所有 $\Psi$ 系数 $\psi_i^\pm$ 严格正。

给定(10)的实际目标
$$
z=-(r_{22},r_{04})=r_1v_1+r_2v_2,
$$
选有限 $K_i>\max(0,-r_i)$，令
$$
w_i^+=\frac{r_i+K_i}{s_i^+}>0,\qquad
w_i^-=\frac{K_i}{s_i^-}>0.
\tag{28}
$$
则四个实际正四次权准确满足
$$
\sum_{i=1}^2(w_i^+s_i^+-w_i^-s_i^-)v_i=z.
\tag{29}
$$
每个权由真实幅度 $(w_i^\pm)^{1/4}$ 实现。(28)提供严格正 balance，没有使用负的实际四次权。

记这些未伸缩权带来的完整正兼容量为
$$
S_\Psi=\sum_{i,\pm}w_i^\pm\psi_i^\pm>0.
\tag{30}
$$
它是有限真实数。下一节控制这笔成本。

## 7. 完整原算子的两个齐次次数

令
$$
(\mathcal D_\Lambda v)(x)=v(x/\Lambda),\qquad \Lambda>0.
$$
右锚始终在全部输入支撑右方。原二次算子的所有输出在右 collar 为零，所以改变到另一个这样的右锚不产生新常数。将原 $J$ 与显式 $x$ 同时换元，得到准确权：

| 原二次算子 | $\Phi_X(\mathcal D_\Lambda u,\mathcal D_\Lambda v)$ |
|---|---|
| $P$ | $\Lambda^{-3}\mathcal D_\Lambda\Phi_P(u,v)$ |
| $R,S$ | $\Lambda^{-2}\mathcal D_\Lambda\Phi_X(u,v)$ |
| $L,U$ | $\Lambda^{-1}\mathcal D_\Lambda\Phi_X(u,v)$ |

例如
$$
L(u,u)=uu'-\frac{x(u')^2}{2}
-\frac{x^2J((u'')^2)}4
+\frac{J(x^2(u'')^2+2(u')^2)}4.
$$
四项各自都有 $\Lambda^{-1}$，包括两个真实左尾项。$U$ 的三个原项也各有该权。这是完整原算子身份，不是只对最高导数成立。

由双线性与上述权，
$$
[Z_*,P](\mathcal D_\Lambda u;\mathcal D_\Lambda D)
=\Lambda^{-4}\mathcal D_\Lambda[Z_*,P](u;D),
$$
其中 $\mathcal D_\Lambda D$ 表示两个输入槽同时伸缩。因此保原 $I_2$ 的 $2u'v'$ 后，
$$
\boxed{
\mathfrak a_j(\mathcal D_\Lambda f,\mathcal D_\Lambda g)
=\Lambda^{j-7}\mathfrak a_j(f,g),\qquad j=0,1,2.
}
\tag{31}
$$
具体第2矩的两项都为 $\Lambda^{-5}$。

另一方面，(6)中 $D_4,C$ 各为四个二阶导数的积分；$J_\theta$ 的两个乘积总导数阶同为8。因此
$$
\boxed{
\Psi_\theta(\mathcal D_\Lambda f,\mathcal D_\Lambda g)
=\Lambda^{-7}\Psi_\theta(f,g).
}
\tag{32}
$$
它们均为 local 完整式，所以同时平移不改变(32)。

原三矩在伸缩后的真实平移 $s$ 下为
$$
\begin{aligned}
I_0&\mapsto\Lambda^{-3}I_0,\\
I_1&\mapsto\Lambda^{-2}I_1+s\Lambda^{-3}I_0,\\
I_2&\mapsto\Lambda^{-1}I_2+2s\Lambda^{-2}I_1+s^2\Lambda^{-3}I_0.
\end{aligned}
\tag{33}
$$
故三矩圆零式保持。强 hook 平面零也保持；对一般弱 hook，原 $\mathfrak H$ 在共同伸缩下权为 $-5$，平移式的额外 $[P,P]$ 为零，所以其零式同样保持。

完整第三 ruling 的保持不靠假设固定几何在伸缩下协变：每个模块保留原八个副本，伸缩同时伸缩它们的间距。原完整第三表达的平移次数仍至多6，原七次差分仍准确为零。真实第三 period 则由同一 $M=0,T=\kappa_H\mathfrak H$ 与已零 hook 支付。后续十二完整复制和正幅不改变这些零式。

## 8. 支付 $I_2$，同时保留一半负储备

对 §6 的四个模块共同作正伸缩 $\Lambda$，然后把其四次权改为
$$
\widetilde w_i^\pm=\Lambda^5 w_i^\pm.
\tag{34}
$$
由(31)，它们的总 $I_2$ 向量仍准确为(29)。第零、第1矩仍为零。各模块可放在任意最终不交位置；因为旧三面积和自身 $\mathfrak a_0,\mathfrak a_1$ 已零，(21)证明最终搬移不再改变 $I_2$。

由(32)、(34)，四模块的总正 $\Psi$ 恰为
$$
\Lambda^{-2}S_\Psi\sin^2\theta.
\tag{35}
$$
选一个足够大的有限 $\Lambda$，使
$$
\Lambda^{-2}S_\Psi<\Delta/2.
\tag{36}
$$
不取任何无限宽 profile；(36)只用于选定一个有限值。

把四个已经放在最终不交包络内的真实模块加入 $\mathcal B_-$，得到 $\mathcal B_0$。它准确满足
$$
\mathfrak a_0=\mathfrak a_1=\mathfrak a_2=0,
\quad
I_j\{u,[W_*,P](u;D)\}=0\quad(j=0,1,2),
\tag{37}
$$
全部相位，并且
$$
\Psi_\theta(\mathcal B_0)
=-\Delta_0\sin^2\theta,\qquad
\Delta_0=\Delta-\Lambda^{-2}S_\Psi>\Delta/2>0.
\tag{38}
$$
原真实宽过渡、矩补包及其 costs 已全部包含在 $\Delta$ 与(10)的实际目标中；没有在伸缩阶段重新忽略它们。

## 9. 为什么加入完整块确实是原式加法

所有模块单独满足
$\mathbf I(f,f)=\mathbf I(g,g)$、$\mathbf I(f,g)=0$。
因此每一完整块的 $D_\theta$ 三矩均为零，$PD_\theta$ 与 $XD_\theta$ 对所用 $X$ 都是真紧函数。

对不交完整块，$X(D_i)$ 与 $P(D_j)$ 的同点导数乘积在 $i\ne j$ 时为零。outer profile 与另一个块的紧 inner 也不交。剩余同块 nested 输出可以有真实二次左尾，但对另一个紧 outer $v$，
$$
I_j(v,p_2)=0,\qquad j=0,1,2,
\tag{39}
$$
其中 $p_2$ 是任意二次多项式；第2式包括原 $2v'p_2'$，两项分部积分准确抵消。

分别对面积的两个 directed 方向应用以上事实，得到(37)所用的完整面积加法。同理，三条 $F_i$ 也是真加法。$\Psi$ 本来就是 local 四次积分，所以也准确相加。这里使用的是完整三矩块，未把任何单个非三矩闭的微包二次输出假称紧。

原第三恢复同样保留完整相位 forcing、共同初值与右锚。只在各基本三矩圆上实施原八复制，再组合这些完整对象，符合 R308/R325 已付的全 range 范围。

## 10. 最后一个强控制器支付 $\Psi$ 和三条完整 directed 行

从构造起点按 R325/R293 选择强控制器用的有限观察
$$
\mathcal F_\star=(\mathcal F,\mathsf C),\qquad
\mathsf C(v)=\int(v'')^4,
\tag{40}
$$
其中 $\mathcal F$ 包括原三矩及全部72 Gaussian 面积 self 的实际平移系数与其有序接口。选择其真正最大秩母包、一个真非零 minor和固定光滑纠正方向；不能把 §5 四个面积模块的任意母包自动当作该 regular 点。

取 R280/R293 的一个完整强控制宏块 $\mathcal C$，保其实际五个最后 block、所有副本位置与正权。它自己的全部72面积均为零，因此包括(37)的两个完整面积；同时
$$
\Psi_\theta(\mathcal C)=\psi_{\mathcal C}\sin^2\theta,\qquad
\psi_{\mathcal C}>0.
$$
给它真实正四次权 $\Delta_0/\psi_{\mathcal C}$。由(38)、(39)，总圆此时准确满足两个完整面积及 $\Psi=0$。

四个新面积模块和整个弱宏块此后全部固定。只在 $\mathcal C$ 的真实 rank-one 微包内作 R325 两种 even 形状的有限频率变化，并共享每个微包的全部同名实际副本。其原三行最高平方在
$$
\left(\int x^2(v'')^2(v''')^2,\ 
\int xv'v''(v''')^2,\ 
\int vv''(v''')^2\right)
$$
上的矩阵是
$$
\begin{pmatrix}
4&0&0\\
4(a+b)&-4a&0\\
6e_*&2d_*-4e_*&-2d_*
\end{pmatrix},
\qquad \det=32ad_*\ne0.
\tag{41}
$$
R325 已以两个真实 even 振荡形状、全部 copy 权和十二个实际交替位置证明三维正锥为 $\mathbb R^3$。控制器当前额外的正四次幅度只乘这些真实列的正数，不改变此正锥或正核。

在一个固定有限正幅盒上，原同 $\mathcal F_\star$ 纠正给
$$
\mathbf F_{\mathsf N}(\mathbf z)
=\mathbf F_{\rm base}+\sum_i z_i^2v_i+o_{C^1}(1),
\qquad \mathsf N\to\infty.
\tag{42}
$$
$\mathbf F_{\rm base}$ 包含本稿弱块、四个伸缩面积块、强控制器、所有最终位置、真实原尾与低阶项的实际值。它只是一个有限 $\mathbb R^3$ 目标，不要求它落入旧32观察的 principal 子空间。

取严格正 balance 表示 $-\mathbf F_{\rm base}$，选三个独立列，固定其余幅度。极限映射的三个实际幅度导数可逆。故一致 $C^1$ 收敛给一个充分大但有限的整数 $\mathsf N$ 及附近正幅精确根
$$
F_0=F_1=F_2=0.
\tag{43}
$$
没有把 principal 零当作全式零，也没有对离散 $\mathsf N^{-1}$ 使用未经证明的光滑参数定理。

每个被改微包的整个 $\mathcal F_\star$ 准确保持，故控制器的全部72面积和 quartic 值保持。特别它对新 $\mathfrak a_2$ 始终贡献零，而非仅固定第零、第1矩。四个非零 $I_2$ 支付模块不参加这次纠正。于是(37)、$\Psi=0$ 对这个有限 $\mathsf N$ 全部保持。

R325 的完整相位归约与原十二副本使三行的交叉相位为零，故(43)对全部 $\theta$ 成立。代入其完整一层恒等即得(7)。

## 11. 有限选择次序、同一个 profile 与实际合法区间

各选择按以下次序一次完成：

1. 固定真实几何及非零 $\kappa$，从起点选择控制器的 $\mathcal F_\star$、最大秩母包、纠正方向和两个真实振荡形状。
2. 按 R331 选内部常项、有限大 $L$、$R=\eta L$、全部矩补包、原强面积修正与十二副本，固定实际 $\mathcal B_-$。由 R332 得(9)，读取其真实目标(10)和严格负量(8)。
3. 固定两个 $\alpha$、正母宽 $h$、四个真实 $\gamma$ 及各自准确中心方差，完成四个面积模块的八／十二包装。按(28)选严格正权，再按(36)选一个有限正伸缩 $\Lambda$。
4. 固定所有模块和强控制器的最终不交包络、所有位置与正四次权。由(21)、(31)–(33)，这一步不改变已经支付的面积或 $\Psi$。三条 directed 的目标则始终在这些最终坐标中重新定义为(42)的完整基线。
5. 对这整个有限集合选择共同有限正 $I$ 和同一右锚。按 R105/R325 的合法包络规则，固定有限几何上的 $h>0$、$\omega$ 有界；可将有限包络放在足够右的正半轴，使 $x+\omega(s)>0$ 留有正间隙。这是从起点选择新共同区间的实际构造，不是把旧冻结 $I$ 无声扩大。
6. 在此固定位置、固定 $I$、固定复制与幅度上取有限 $\mathsf N$，完成(43)。此后不再移动或伸缩任何 profile。
7. 最后作一次共同正幅归一化 $I_0(f,f)=1$，并固定新 seed 的目标 metric。所有已列齐次零式保持。

弱核心始终含真正 $W\ne0$ 的开区间，整个过程中未修改它。新四模块与控制器均位于不交的强区，保持弱条件 $\mathfrak H(g;ff)=0$，没有另加一般不必要的第二 hook。原三矩、第二／第三周期、第三 ruling、两 collar 与种子初值按上述完整构造保持。

所有正幅、支撑宽度、复制数和频率均有限。不同母包的积分由其实际定义决定；本稿没有把有限矩表中的各分量当作独立自由变量。

## 12. 新增结论与剩余问题

存在同一个真实带内部常项的弱单 hook、导数 rank-two 圆，同时准确满足：

- 原三矩圆和完整三阶；
- $A_{-2,-3}$ 的三个完整外矩、全部相位；
- $A_{-1,-3}$ 的三个完整外矩、全部相位；
- 三条完整 directed 行 $F_0,F_1,F_2$；
- 原兼容量 $\Psi$ 和由完整原式确定的一层(7)。

R328 对无内部常项幂曲段的否定仍成立。新结论使用 R331 已经支付的真实常项与宽恢复，并以完整 $I_2$／$\Psi$ 的不同齐次次数完成下一门。

其余 Gaussian 面积、对称乘积、零／一层完整函数、canonical 平台与退化通量、完整第四 period、同一 gauge 的 joint range 仍未由本文支付。强控制器自己的72条件没有被扩成整个弱强圆的72条件。本文改变初选 profile 圆及 seed，始终使用同一已固定几何；不声称保持旧 seed 的目标度量。
