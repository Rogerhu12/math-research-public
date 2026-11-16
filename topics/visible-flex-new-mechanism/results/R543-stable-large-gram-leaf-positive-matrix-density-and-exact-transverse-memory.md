# R543：大 Gram 稳定水平叶的严格正矩与同一规范下的准确离叶入口

日期：2026-11-16。**完整原式与条件推论的纸面证明；没有执行数值、符号、profile、秩或开发计算。**

本文研究 R521 同一正交母库中，从原起点一次选择
$$
\nu_1^\delta=\frac{2c}{\delta^2},\qquad
\nu_2^\delta=\frac{\lambda}{\delta^2},\qquad
\nu_0^\delta=-\frac{H^2\lambda}{\delta^2}+2HF_c
\tag{1}
$$
所产生的主导稳定几何支，其中 $H,c,\lambda>0$。全部 profiles、窗口、右锚、第二规范及这一条第三规范始终固定。本文的精确叶结论不依赖实际奇异 ODE 跟踪。第 5 节先给明确写出假设的一般实际路径推论，再用于 R541 已给出的本次真实有限路径；不将该有限跟踪扩成任意控制或无界时长的延续。

严格结论是：从 $k=0,\omega=\omega_c$ 出发，在这条稳定支上的任意水平路径，即使高度反复往返，原 $p_1^{\omega_c}$ 密度仍非负，非恒路径的总积分严格正。高高度可以使原 $t_1^{\omega_c}$ 为正，但不会改变这一剩余矩障碍。

任意真实离叶路径另有准确的水平记忆公式。它量化了进入另一条水平叶所需的实际积分，不能由换时钟、重设入值或引用另一条 $\chi$ 的负路径免费取得。本文没有据此宣称该积分已经可达或全部八矩已经配平。

## 1. 原坐标、原矩与同一个固定 Gram

固定原常态
$$
S_c=(H,0,\omega_c),\qquad
\eta=\omega-\omega_c,\qquad d=h\eta-k,\qquad h>0.
\tag{2}
$$
这里 $d$ 是在固定坐标 $y=x+\omega_c$ 中的真实变量，不能与未平移坐标中的 $h\omega-k$ 混淆。

R521 的实际水平关系及 R529/R537 的原矩坐标为
$$
\eta_s=\frac{k_s}{2h},\qquad p_1^{\omega_c}=-kd,
\tag{3}
$$
$$
8t_1^{\omega_c}
=2kh\eta-k^2-1-(h_s/h)^2
=k^2+2kd-1-(h_s/h)^2.
\tag{4}
$$
因此在任意真实路径上均有
$$
8t_1^{\omega_c}=k^2-2p_1^{\omega_c}-1-(h_s/h)^2.
\tag{5}
$$
这些是原 $M_{\rm raw}$ 中的固定坐标，保留端势，没有改成只含局部 forcing 的呈示。

记
$$
c=C_k(S_c)>0,\qquad F_c=\mathcal F(S_c,0,0,0,0).
$$
R521 的完整固定 Gram 项是
$$
2\mathbf w_y(S)\cdot\nu
=\frac{\nu_0(1+d^2)}{2h}+\nu_1d+\frac{h\nu_2}{2}.
$$
代入(1)，准确得到
$$
2\mathbf w_y(S)\cdot\nu^\delta
=\delta^{-2}\Psi(h,d)+\frac{HF_c(1+d^2)}h,
\tag{6}
$$
$$
\boxed{\Psi(h,d)
=-\frac{H^2\lambda(1+d^2)}{2h}+2cd+\frac{\lambda h}{2}.}
\tag{7}
$$
式(7)只是在完整 ruling 中分离主导势；完整 $\mathcal F$、真实第二与第三历史及有限补偿项均未被删除。

## 2. 稳定实支及 $q/h$ 的严格单调性

置
$$
a=\frac{2c}{H^2\lambda},\qquad
b=\sqrt{a^2+H^{-2}},\qquad h_*=\frac1b.
\tag{8}
$$
由于 $c,\lambda>0$，有 $0<h_*<H$。在整个开区间 $\mathcal I=(h_*,\infty)$ 上，方程 $\Psi(h,q)=0$ 中通过 $q(H)=0$ 的稳定实支唯一写成
$$
\boxed{
u(h):=\frac{q(h)}h=a-\sqrt{b^2-h^{-2}},\qquad q(h)=hu(h).
}
\tag{9}
$$
证明是把(7)除以 $\lambda h/2$，得到
$$
H^2u^2-\frac{4c}{\lambda}u-1+\frac{H^2}{h^2}=0.
$$
在 $h=H$，平方根等于 $a>0$；故满足 $q(H)=0$ 的恰为(9)中的负号支。

沿该支，
$$
\boxed{
\Psi_d(h,q(h))
=2c-H^2\lambda u(h)
=H^2\lambda\sqrt{b^2-h^{-2}}>0.
}
\tag{10}
$$
其真正退化端是 $h=h_*$，不在本文的稳定开支内。在任何预选紧区间 $K\Subset\mathcal I$，(10)一致远离零。

直接微分(9)给
$$
\boxed{u'(h)=-\frac1{h^3\sqrt{b^2-h^{-2}}}<0.}
\tag{11}
$$
于是
$$
q(h)>0\ (h<H),\qquad q(H)=0,\qquad q(h)<0\ (h>H).
\tag{12}
$$
这些结论只需要稳定支实且严格，未假设实际高度单调。原几何还须满足 R521 的合法窗口条件；若这些条件只允许 $\mathcal I$ 的一部分，以下结论在该允许部分原样成立，不能用(9)替代合法性检查。

## 3. 从原起点决定的完整水平叶

定义真实水平变量
$$
j=\frac{\eta}{h}+\frac d{h^2}.
\tag{13}
$$
由(2)(3)逐项微分，得到 R537 的准确身份
$$
\boxed{
j_s=-\frac{2d h_s}{h^3},\qquad
\eta=hj-\frac dh,\qquad k=h^2j-2d.
}
\tag{14}
$$

现在取任意 $C^1$ 高度路径 $h:[0,L]\to\mathcal I$，使 $h(0)=H$，并要求整条路径在几何支 $d=q(h)$ 上，实际入口为 $k(0)=\eta(0)=0$。定义
$$
J(h)=-2\int_H^h\frac{q(r)}{r^3}\,dr.
\tag{15}
$$
链式法则直接给
$$
\frac{d}{ds}J(h(s))=-\frac{2q(h(s))h_s(s)}{h(s)^3}=j_s(s).
$$
又因 $J(H)=j(0)=0$，故
$$
\boxed{
j(s)=J(h(s)),\quad k(s)=k_0(h(s)),\quad
k_0(h)=h^2J(h)-2q(h).
}
\tag{16}
$$
这里没有除以 $h_s$，所以允许 $h_s=0$、改变符号、开放常高度段及任意有限次往返。同一高度再次出现时，(16)给同一个 scalar 点；第二、第三历史不因此返回。

令
$$
W(h)=\frac{k_0(h)}{h^2}=J(h)-\frac{2u(h)}h.
\tag{17}
$$
由 $J'=-2u/h^2$ 准确算得
$$
\boxed{
W'(h)=-\frac{2u'(h)}h
=\frac2{h^4\sqrt{b^2-h^{-2}}}>0,\qquad W(H)=0.
}
\tag{18}
$$
特别，$k_0(h)$ 与 $h-H$ 同号，而(12)中的 $q(h)$ 与 $h-H$ 反号。

## 4. 完整非单调叶上的严格正矩

由(3)(12)(16)(18)，
$$
\boxed{
p_{1,0}^{\omega_c}(h)=-k_0(h)q(h)\ge0,\qquad
p_{1,0}^{\omega_c}(h)=0\Longleftrightarrow h=H.
}
\tag{19}
$$
因此对任意上述非恒 $C^1$ 路径，
$$
\boxed{P_0[h]:=\int_0^L p_{1,0}^{\omega_c}(h(s))\,ds>0.}
\tag{20}
$$
严格号来自连续性：只要 $h$ 不是恒等于 $H$，便有一个正长度开放时间区间使 $h\ne H$，而(19)在其上严格为正。反向行进只改变 $h_s$，不会改变作为当前 scalar 函数的(19)。

若 $h\equiv H$，则(16)给 $k=\eta=d=0$；原(4)成为 $t_1^{\omega_c}=-1/8$。故任意正长度的这一恒态段也不是全 $M=0$。

由此得到完整分离：

> 从原常态出发并始终留在(9)稳定几何支上的任意正长度水平路径，都不能使全部原八矩积分为零。非恒路径由原 $p_1^{\omega_c}$ 严格分离；恒态路径由原 $t_1^{\omega_c}$ 严格分离。

这也可视为 R529 非零二次零叶障碍在(7)上的一个直接坐标证明。本文额外明确了稳定支、任意非单调高度及后面所需的准确横向记忆。

### 4.1 高高度正 $t_1$ 与该障碍同时存在

固定 $\lambda>0$，由(9)(18)，
$$
u(h)\longrightarrow u_\infty=a-b<0,
$$
$$
W(h)\longrightarrow
W_\infty:=2\int_H^\infty
\frac{dr}{r^4\sqrt{b^2-r^{-2}}}>0.
\tag{21}
$$
积分在 $H$ 处光滑，且在无穷处被常数倍 $r^{-4}$ 控制，故有限且严格正。于是
$$
q(h)=u_\infty h+O(h^{-1}),\qquad
k_0(h)=W_\infty h^2+O(h^{-1}).
\tag{22}
$$
在常高度的 scalar 段，(4)给
$$
p_{1,0}^{\omega_c}=-u_\infty W_\infty h^3+O(h)>0,
$$
$$
t_{1,0}^{\omega_c}=\frac{W_\infty^2}{8}h^4+O(h^3)>0
\tag{23}
$$
于充分大且合法的有限 $h$，并且
$$
\frac{p_{1,0}^{\omega_c}}{t_{1,0}^{\omega_c}}\longrightarrow0.
\tag{24}
$$
所以稳定叶的正 $t_1$ 入口并没有代数矛盾；它仍携带严格正的 $p_1$。式(23)是精确叶上的 scalar 密度结论，不单独保证完整 ruling 可沿该常高度段保持任意时长。

## 5. 固定有限路径的小 $\delta$ 真实总符号：条件接口

本节先证明一个只需水平身份的条件接口，随后使用 R541 对其本次完整实际路径已付的跟踪。一般非单调路径若要从精确叶结论转到实际解，仍须逐条满足下列前提。

先固定 $L<\infty$、一个非恒路径 $h:[0,L]\to K\Subset\mathcal I$，其中 $h(0)=H$。设一族**同一实际原恢复**产生的路径满足原水平关系，且
$$
h_\delta(0)=H,\quad j_\delta(0)=0,\quad
\|h_\delta-h\|_\infty\longrightarrow0,
$$
$$
\sup_\delta\operatorname{TV}(h_\delta)<\infty,\qquad
\|d_\delta-q(h_\delta)\|_\infty\longrightarrow0,
\tag{25}
$$
各 $h_\delta$ 均在同一个稳定紧区间中。全部原 $A,T$、固定规范、frame 和端势仍按各自真实方程演化；(25)不授权重设其中任何值。

置
$$
e_\delta=d_\delta-q(h_\delta),\qquad
\rho_\delta=j_\delta-J(h_\delta).
$$
由(14)(15)准确得到
$$
\rho_\delta(s)=-2\int_0^s
\frac{e_\delta(t)h_\delta'(t)}{h_\delta(t)^3}\,dt.
\tag{26}
$$
若 $h_->0$ 是共同高度下界，则
$$
\boxed{
\|\rho_\delta\|_\infty
\le 2h_-^{-3}\|e_\delta\|_\infty
\operatorname{TV}(h_\delta)=o(1).
}
\tag{27}
$$
进而
$$
k_\delta=k_0(h_\delta)+h_\delta^2\rho_\delta-2e_\delta
\longrightarrow k_0(h)\quad\text{一致},
$$
所以
$$
\boxed{
\int_0^L p_{1,\delta}^{\omega_c}\,ds
=P_0[h]+o(1)>0
}
\tag{28}
$$
于充分小的每个正 $\delta$。若(25)中的高度及离叶误差均为 $O(\delta^2)$，且共同总变差有界，则(28)中的误差可写成 $O(\delta^2)$。

**应用于 R541 的实际路径。** 该稿先固定同一母、$\lambda$、有限上升高度与有限常高尾长，再选小 $\delta$；真实起点为(2)及 $A=T=0$。其(40)(41)在包括全部入段的整个固定区间上给 $d^\delta=q(h)+O(\delta^2)$，且高度本身就是预给的固定路径，所以(25)全部成立。该路径非恒，故其真实总 $p_1^{\omega_c}$ 由(28)严格为正。它与 R541 已证的真实总 $t_1^{\omega_c}>0$ 是同一条实际路径的两个输出，并未清除原矩阵返回障碍。

这里的“总”是同一从原入口开始的整个已指定区间。若另有额外前缀，必须加上其真实原积分；只有该前缀积分已经证明为 $o(1)$ 时，才可将它直接吸收入(28)。不能拿另一条规范下的负前缀代替。

(28)并未证明实际密度逐点非负：在 $h$ 接近 $H$ 的地方，精确叶密度本来就接近零，小误差可能改变局部号。它证明的是固定非恒路径的严格正总积分。

### 5.1 没有排除的 $\delta$ 相关情形

若路径、时长、高度范围或总变差随 $\delta$ 改变，(28)不自动成立。具体可能包括：

- $P_0[h_\delta]\to0$，其正余量不足以压过真实离叶项；
- 总变差增长，使(27)右端不再趋零；
- 高度接近稳定退化端 $h_*$，或高度上界、时长、导数界发散，使共同常数失效；
- 实际轨迹保有未被(25)控制的快振子能量或较大的完整历史。

这些都是当前定理未排除的范围，不是已经构造成功的逃离路径。

## 6. 任意真实离叶路径的准确入口量

对任意真实水平路径，只要 $h(s)\in\mathcal I$，定义
$$
e(s)=d(s)-q(h(s)),\qquad \rho(s)=j(s)-J(h(s)).
$$
不作小量假设，(14)直接给
$$
\boxed{
\rho_s=-\frac{2e h_s}{h^3},\qquad
\rho(s_1)-\rho(s_0)=-2\int_{s_0}^{s_1}\frac{e\,dh}{h^3}.
}
\tag{29}
$$
同时保留完整点态式
$$
\boxed{
k=k_0(h)+h^2\rho-2e,\qquad
p_1^{\omega_c}
=-\{k_0(h)+h^2\rho-2e\}\{q(h)+e\}.
}
\tag{30}
$$
因此真正离叶时还可直接通过 $e$ 改变密度；不能只研究 $\rho$ 而删掉这一项。

若某一后段准确重新落到 $e=0$ 的同一个几何支，则 $\rho$ 在该后段为常数 $\rho_*$，而
$$
k=h^2\{W(h)+\rho_*\},\qquad
p_1^{\omega_c}=-h^2q(h)\{W(h)+\rho_*\}.
\tag{31}
$$
它是同一几何支上的另一条水平叶。严格负号的准确门为
$$
\boxed{
\begin{array}{ll}
h>H:& p_1^{\omega_c}<0\Longleftrightarrow \rho_*<-W(h),\\[2mm]
h<H:& p_1^{\omega_c}<0\Longleftrightarrow \rho_*>-W(h).
\end{array}}
\tag{32}
$$
在 $h=H$，$q=0$，所以该重新落叶点的 $p_1$ 恒为零，不论 $\rho_*$ 的值。

从原入口 $\rho=0$ 出发，(32)中任何非零入口值都必须由(29)的真实离叶积分产生。只在精确稳定支上往返时 $e=0$，积分字面为零；改变行进方向不创造它。式(29)也没有把 $e$ 与 $h$ 授为两个独立可控函数；它们仍受同一完整 ruling 和真实历史约束。

### 6.1 原合法窗口内，负 $p_1$ 与正 $t_1$ 的代数兼容点

设同一预选母窗口满足
$$
y_{\min}:=\min_I(x+\omega_c)>-u_\infty.
\tag{33}
$$
因为 $-u_\infty=b-a\to0$ 当 $\lambda\downarrow0$，从起点足够小地选择 $\lambda$ 可满足此条件；这里不在路径中途改变窗口或 $\lambda$。

固定任意 $\kappa>1$。对充分大的有限 $h>H$，在同一稳定几何支上取
$$
d=q(h)<0,\qquad k=-\kappa,\qquad
\eta=\frac{q(h)-\kappa}{h},
$$
$$
\boxed{\rho_*=-W(h)-\frac{\kappa}{h^2}.}
\tag{34}
$$
它满足(31)(32)。原合法性可以直接核：
$$
x+\omega=y+u(h)-\frac{\kappa}{h}
\longrightarrow y+u_\infty>0,
$$
$$
h(x+\omega)-k=hy+q(h)=h\{y+u(h)\}>0.
$$
若还要求 R537 的较强区域 $hy>\sqrt{1+d^2}$，则由(33)同样在充分大有限 $h$ 成立。

在 $h_s=0$ 的该 scalar 点，
$$
\boxed{
p_1^{\omega_c}=\kappa q(h)<0,\qquad
8t_1^{\omega_c}=\kappa^2-2\kappa q(h)-1>0.
}
\tag{35}
$$
这给同一 Gram 主导稳定几何支、同一合法窗口中的真实几何兼容点；没有必要以令某个负 $\rho_*$ 固定后无限升高的办法来论证。后者会使 $\eta$ 最终很负，不能忽略固定窗口的 $x+\omega>0$ 门。

但是(34)目前仍是**待实际到达的入口值**。要把(35)变成完整 ruling 路径，须在同一条 $\chi^\delta$ 下支付(29)的入口、重新落叶或有明确误差的准备、有限保持以及原二三阶 history，再计算全部进入段的真实成本。本文不把 $\rho_*$ 设为新的自由初值，也不拼接 R539 的另一条固定 Gram 路径。

## 7. 本稿已付与后继问题

已证明的是：

1. 稳定实支上的准确 $u'(h)<0$ 和 $W'(h)=-2u'(h)/h>0$；
2. 从原常态出发、允许任意高度往返的精确叶严格正总 $p_1$；
3. 在明确有限跟踪假设下，固定非恒实际路径的小 $\delta$ 正总符号；
4. 任意真实离叶路径的准确记忆(29)、重新落叶后的严格负号门(32)，以及同一合法窗口内的代数兼容点(34)(35)。

下一实际问题是同一规范下实现足够的离叶积分或直接利用(30)的有限离叶段，并完整支付进入成本、原 $A,T$ 和有限保持。局部可选加速度、非退化 $C_k$ 或快高度时钟本身都不证明这一有限入口可达。

本文不改变主课题要求：原八矩共同返回、scalar 端 germ、frame、位置、第三及第四 period，以及闭曲面的全时全域等距、嵌入、reach 与至少 $0.3D$ 的握持位移均仍未付。

## 原式来源

- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：唯一正交母库、实际水平关系、完整第四 ruling、固定 Gram 及完整第三历史；
- [R529](R529-fixed-nonzero-quadratic-leaves-and-the-real-positive-matrix-increment.md)：原 $p_1^{\omega_c},t_1^{\omega_c}$ 坐标与非零二次零叶的水平障碍；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)：准确 $j_s=-2dh_s/h^3$、完整慢第三重写及有限路径结论的参数次序；
- [R539](R539-one-fixed-gram-and-a-real-negative-total-matrix-entry-in-the-orthogonal-library.md)：固定坐标中的完整 Gram 项；其负路径使用另一组起点参数，本文没有将其拼入(1)。
- [R541](R541-finite-curvature-and-positive-total-matrix-entry-on-one-stable-gram-branch.md)：本次同一 Gram 的真实有限区间、完整 $A,T$ 能量与 $O(\delta^2)$ 跟踪；仅在第 5 节明确应用其已付路径。

