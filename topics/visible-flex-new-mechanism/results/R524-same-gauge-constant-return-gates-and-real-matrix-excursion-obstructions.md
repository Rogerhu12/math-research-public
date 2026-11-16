# R524：同一 R520 规范的常态返回门、八矩局部刚性与真实有限幅度障碍

日期：2026-11-16。**完整纸面推导；没有执行数值、符号、秩、profile 或开发计算，也没有重跑任何已付观察。**

本文继续 [R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md) 已经实际构造的同一个变形母库、同一个 $w_\theta=0$ 和同一个第三规范 $\chi_\theta$。不改变母形，不把真实累计 $m,T$ 重新归零，不用 R518 的无 ruling 限制成本桥替代内部约束路径。

先给两个准确返回结论。第一，回到原常 scalar 状态不等于能接上一段同规范的常态 germ；还须满足同一个八矩输入上的两个完整二次型条件。第二，在一个明确的小高度速度盒内，任何真正非恒的路径都不能与同长度常态段具有相同的完整八矩传递。后一条甚至不需要 ruling 假设，因此对 R520 的实际反馈族严格成立。

进一步，任意完整 raw $M=0$ 的正长度真实路径，都必须有曲率换号、$\max|k|>1$，以及一个明确严格的 $\omega$ 振幅下界。这说明 R520 的局部隐函数邻域不能被当成已付的零矩返回桥；要得到该种返回，必须进入真实有限幅度的状态区间。

本文不证明仅 scalar 返回不可能，也不证明剩余的两条二次型返回门已经可控。全闭路径、固定同一十三行、完整第三和第四目标仍保其原欠项。

## 1. 固定的是已经实现的常态前缀

沿 R520 固定
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0,\qquad x+\omega_c>0,
$$
$$
M_c=M_{\rm raw}(S_c,0,0),\qquad A_c=\Phi_{M_c}.
\tag{1}
$$
同一个实际圆已经满足
$$
\mathscr Q_c(A_c)=0,\qquad
\mathscr G_c(\pi/2)=1,
\tag{2}
$$
并保 R520 的完整 $\mathcal F_{\rm path}$、全部 $W$ outer 矩和原二十目标。

从真实零历史出发，常态路径有
$$
m(s)=sM_c,\qquad
T(s)=-s^2A_c^2/2.
\tag{3}
$$
原固定 $\chi_\theta$ 已支付整段全相位 ruling。取它内部一个 $t_0>0$；后继非恒段的入口是
$$
S(0)=S_c,\qquad m(0)=t_0M_c,
\tag{4}
$$
第三入值仍是(3)在 $t_0$ 的真实值。后继参数另记 $s\in[0,L]$，不把原全局时钟重置为零 history。

R520 在(4)给真实分支
$$
k_s=G(h,k,\omega,m,\gamma),\qquad \gamma=h_s,
$$
$$
\omega_s=\frac{k_s}{2h},\qquad
m_s=M_{\rm raw}(h,k,\omega,\gamma,k_s).
\tag{5}
$$
本文的局部结论只要求控制和状态留在该已付分支内。任意几何路径的八矩结论则只使用 R73 的原 $M_{\rm raw}$，不会借用另一母库的反馈或端口秩。

## 2. 同一个原常态 germ 的准确两条返回门

在固定 $S_c$ 上，对任意真实 E8 算子 $A$ 定义整个相位二次型
$$
\mathscr Q_c(A;\theta)
=-\mathcal E_c(AD_\theta,AD_\theta)
+2\mathcal E_c\{\phi_\theta,A(\phi_\theta,AD_\theta)\}.
\tag{6}
$$
这是原 physical 配对，保全部左尾；$D_\theta$ 的三矩为零，使整个 $AD_\theta$ 真紧。它不是单包 principal。

R520 的完整 pure self 纤维和有序核给全部实际输入上的角向身份
$$
\mathscr Q_c(A;\theta)=\sin^2\theta\,q_c(A),\qquad
q_c(A):=\mathscr Q_c(A;\pi/2).
\tag{7}
$$
令
$$
b_c(A,B)=\frac{q_c(A+B)-q_c(A)-q_c(B)}2.
\tag{8}
$$
这是同一个完整实二次型的对称极化。$q_c(A_c)=0$ 不表示
$b_c(A_c,B)$ 对所有 $B$ 都为零。

假设某条真实路径终于回到
$$
h=h_c,\quad k=0,\quad \omega=\omega_c,\quad
h_s=k_s=0,
\tag{9}
$$
其实际累计为 $A_e=\Phi_{m_e}$。R482 的第三商势必须从原真正初端读取：
$$
P^{\rm end}
=\Pi(j^1S_e)-\Pi(j^1S_{\rm initial})=0.
$$
所以此处完整第三类为
$$
T_e=-A_e^2/2+\tau_e,\qquad \tau_e\in W.
\tag{10}
$$
这里 $\tau_e$ 一般非零。能够删除的只是同一原母库已付的三个 outer 配对，不是第三传递本身。

若从(9)继续走一段真实常态区间，按该段长度 $\sigma$ 有
$$
A(\sigma)=A_e+\sigma A_c.
$$
常态 $C_s=0$、固定初端势及全部 $W$ outer 零，使 R520 原完整 source 准确为
$$
\begin{aligned}
\mathscr K(\sigma,\theta)
&=\sin^2\theta\,q_c(A_e+\sigma A_c)\\
&=\sin^2\theta\{q_c(A_e)+2\sigma b_c(A_e,A_c)\}.
\end{aligned}
\tag{11}
$$
R520 已选择的同一个 $\chi$ 仅消掉原常态 $\mathscr R_c$；未在此重新选择。二次 $\sigma^2q_c(A_c)$ 项由(2)消掉。

因此，存在正长度的同规范常态继续，当且仅当
$$
\boxed{q_c(A_e)=0,\qquad b_c(A_e,A_c)=0.}
\tag{12}
$$
二、三阶端场仍按(10)真实传递；(12)只支付完整 ruling 的常态继续，不额外支付它们的周期。

令相对同长度原常态轨道的真实矩阵差为
$$
\delta m=m_e-(t_0+L)M_c,\qquad
\delta A=\Phi_{\delta m}.
$$
由 $q_c(A_c)=0$，(12)等价于
$$
\boxed{b_c(\delta A,A_c)=0,\qquad q_c(\delta A)=0.}
\tag{13}
$$
这是两个同一图上的完整条件。不能从末 scalar 值相等或某一个瞬时 $F=0$ 推出第二个条件，更不能把 $\delta m$ 默认为零。

若实际控制已在末 collar 为零，则(12)给一个精确的常态 ODE 继续；同一局部唯一性使它与原反馈分支一致。反过来，若实际解具有常态末 germ，则(12)由那一整段的时间多项式严格必要。

## 3. 原 raw 八矩的三个坐标：只换固定记号，不换几何

为了检查真实 $m$，固定任意实数 $c$，仅把 profile 坐标写成
$$
y=x+c,\qquad \eta=\omega-c.
\tag{14}
$$
原物理量仍是 $z=x+\omega=y+\eta$。这只是同一个 E8 的固定可逆坐标变换，不是将路径的 $\omega$ 平移，不改变活动窗口或右锚。

用 R73(9)(10)的原约定，在此坐标中
$$
\boxed{
\begin{aligned}
p_2^{\,c}&=-kh/2,\\
p_1^{\,c}&=k^2-kh\eta,\\
t_1^{\,c}
&=\{2kh\eta-k^2-1-(\gamma/h)^2\}/8.
\end{aligned}}
\tag{15}
$$
例如 R73 的
$$
B_2=\frac{hK_0-\gamma\lambda}{8},\qquad
K_0=k(y+\eta)^2-\frac{k^2+1}{h}(y+\eta),
$$
$$
\lambda=\frac{\gamma(y+\eta)-k_s/2}{h^2}
$$
的 $y$ 系数正是(15)第三行。没有去掉速度平方或假设 $\gamma=0$。

原坐标与新坐标之间具体有
$$
p_2^{\,c}=p_2,\qquad
p_1^{\,c}=p_1-2cp_2,\qquad
t_1^{\,c}=t_1+\frac c2p_2.
\tag{16}
$$
故整个 raw $M$ 的积分为零，必使(15)的三个积分都为零。以下所有 $M$ 都是原 R73 点态密度的真实积分；若改用完成分部积分的另一个呈示，必须先补回其真实端势，不能直接替换。

两条尤其有用的准确恒等是
$$
\boxed{
8t_1^{\,c}+2p_1^{\,c}=k^2-1-(\gamma/h)^2,
}
\tag{17}
$$
$$
\boxed{
8t_1^{\,c}
=h^2\eta^2-(k-h\eta)^2-1-(\gamma/h)^2.
}
\tag{18}
$$
它们对任意真实水平路径逐点成立，与 profile、第三规范及 ruling 是否为零均无关。

## 4. 小高度速度盒内，相同常态八矩传递严格刚性

令一条光滑真实路径从 $S_c$ 出发，长度为 $L>0$，且
$$
0<h_{\min}\le h(s)\le h_{\max}.
$$
在本节取 $c=\omega_c$，所以入口 $k=\eta=0$。原水平关系给
$$
\left(\frac{k}{2h}\right)_s
=\eta_s-\frac{k\gamma}{2h^2}.
$$
保入口常数后，准确有
$$
\boxed{
\eta(s)=\frac{k(s)}{2h(s)}
+\frac12\int_0^s\frac{k(t)\gamma(t)}{h(t)^2}\,dt.
}
\tag{19}
$$
这是 R509 使用的原几何身份；本节不消费其另一母库的端口 IFT。

把(19)代入(15)，令
$$
\varepsilon_h=
\frac{h_{\max}\sqrt L}{h_{\min}^2}\|\gamma\|_{L^2(0,L)}.
$$
Cauchy–Schwarz 给
$$
\sup_s\left|\int_0^s\frac{k\gamma}{h^2}\right|
\le h_{\min}^{-2}\|k\|_2\|\gamma\|_2,
\qquad
\int_0^Lh|k|\le h_{\max}\sqrt L\,\|k\|_2.
$$
因此保完整有序积分后，
$$
\boxed{
\int_0^L p_1^{\,\omega_c}\,ds
\ge\frac12(1-\varepsilon_h)\int_0^L k^2\,ds.
}
\tag{20}
$$
不需要 $k$ 或 $k_s$ 预先为零，也没有把右端有序项丢掉。

现在假设
$$
\varepsilon_h<1,\qquad
\int_0^L M_{\rm raw}\,ds=LM_c.
\tag{21}
$$
原常态的 $p_1^{\,\omega_c}=0$。由(20)，(21)迫 $k\equiv0$。
水平关系和入口值随即迫 $\eta\equiv0$。此时(15)给
$$
\int_0^L t_1^{\,\omega_c}\,ds
=-\frac L8-\frac18\int_0^L(\gamma/h)^2\,ds.
\tag{22}
$$
而同长度常态值为 $-L/8$，所以(21)再迫 $\gamma\equiv0$，
进而 $h\equiv h_c$。

得到完整刚性命题：
$$
\boxed{
\varepsilon_h<1,\quad
\int_0^L M_{\rm raw}=LM_c
\quad\Longrightarrow\quad
(h,k,\omega)\equiv(h_c,0,\omega_c).
}
\tag{23}
$$
此命题甚至没有额外要求右 scalar 先返回；相同完整八矩本身已强迫整段常态。

对 R520 的固定短时间、足够小 $h_s$ 控制盒，$\varepsilon_h<1$ 自动由固定统一界保证。所以每一条已经构造的真正非恒局部离开，都有
$$
m(L)\ne(t_0+L)M_c.
\tag{24}
$$
它不能原样替换同长度常态段并保持完整二阶传递。这个结论不把其差冒称某个纯四阶 response，不删除差对后继 $T,V$ 的作用。

(23)也不等于“无法回常 scalar”。非零 $\delta m$ 仍可能满足(13)；
这需要在同一个实际 endpoint 映射上另证，而不能用(23)排除。

## 5. 完整零矩返回必须有真实有限幅度

现在不要求路径从 $S_c$ 出发，也不假设它留在任何局部反馈盒。
只设正长度 $L>0$、$h>0$、真实水平关系成立，且
$$
\int_0^L M_{\rm raw}\,ds=0.
\tag{25}
$$
由(15)(17)，对任意固定 $c$，
$$
\boxed{
\begin{aligned}
\int_0^L kh\,ds&=0,\\
\int_0^L kh(\omega-c)\,ds&=\int_0^L k^2\,ds,\\
\int_0^L k^2\,ds&=L+\int_0^L(h_s/h)^2\,ds.
\end{aligned}}
\tag{26}
$$
最后一行的常数 $L$ 是真实正时间，不是可随意扣除的基准。

因为右端严格正，$k$ 不恒零；第一行和 $h>0$ 迫 $k$ 同时取正值、负值。并且
$$
\boxed{\max_{[0,L]}|k|>1.}
\tag{27}
$$
若最大值至多1，则(26)迫 $h_s=0$ 且 $k^2\equiv1$。连续性使 $k$ 恒取一个符号，这与第一行矛盾。这里没有以负时间作抵消。

高度速度本身也有一个真实必要下界。取
$$
c=\omega(0)-\frac{k(0)}{2h(0)},
$$
则 $\eta(0)=k(0)/(2h(0))$，所以(19)的完整有序公式仍成立，即使入口 $k(0)\ne0$。应用同一个(20)并用(25)(26)，得到
$$
\boxed{
\frac{h_{\max}\sqrt L}{h_{\min}^2}\|h_s\|_2\ge1.
}
\tag{27a}
$$
这里仅取已经证明的非严格必要界，不以未审的等号分类再加强它。它说明常高度整段不可能具有完整 raw 零矩；原辅助桥中的真实高度变化不能免费省略。

再取真实 $h^2$ 加权均值
$$
c_*=\frac{\int_0^Lh^2\omega\,ds}{\int_0^Lh^2\,ds},
\quad
D=L+\int_0^L(h_s/h)^2\,ds,\quad
H_2=\int_0^Lh^2\,ds.
$$
(26)第二行与 Cauchy–Schwarz 给
$$
D=\int kh(\omega-c_*)\le
\sqrt D\left(\int h^2(\omega-c_*)^2\right)^{1/2},
$$
故
$$
\int h^2(\omega-c_*)^2\ge D.
\tag{28}
$$
令 $a=\min\omega,b=\max\omega$。对正概率权
$h^2ds/H_2$，由 $(\omega-a)(b-\omega)\ge0$ 得原区间方差界
$$
\frac1{H_2}\int h^2(\omega-c_*)^2
\le(b-c_*)(c_*-a)\le(b-a)^2/4.
\tag{29}
$$
$\omega$ 不能恒定，否则(26)前两行会迫 $\int k^2=0$。
由于真实 $\omega$ 连续、$h^2$ 严格正，其从最小值到最大值经过一段具有中间值的开区间；(29)第一步因此严格。因此
$$
\boxed{
\operatorname{osc}\omega
>2\sqrt{\frac{L+\int_0^L(h_s/h)^2\,ds}
                {\int_0^Lh^2\,ds}}
\ge\frac{2}{h_{\max}}.
}
\tag{30}
$$
每一步使用同一真实路径，原 $h_s$ 正平方全部保留。

等价的完整余量亦可直接由(18)积分保留：
$$
\int h^2(\omega-c)^2
=L+\int(h_s/h)^2+\int\{k-h(\omega-c)\}^2.
\tag{31}
$$
它不是仅对某个未付极限成立的近似式。

(27)(30)适用于任何真实 raw 零矩段，因而也适用于任何未来满足 ruling 的零矩段。它们不涉及母形，也不能被改变 $\chi$ 或删除第三 history 绕开。原 R70 的辅助桥本来使用正负曲率 bulk 和有限范围连接，并不声称留在 $k=0$ 的小盒；本文没有反驳那个无 ruling 限制的桥定理。

## 6. 对 R520 后继控制问题的准确结论

对同一个 R520 圆与固定规范，当前真正的返回问题有三层，不能合并：

1. **返回 scalar 与常态 germ。** 除(9)外，必须付完整实际矩阵差的(13)。它们是两个由同一个原 physical 配对定义的实条件；目前不能由局部 IFT 或 scalar 末值自动得到。
2. **保持原常态段的完整传递。** 在原小高度速度盒内，(23)排除了任何非恒替换。若只匹配少数成本投影而遗漏 $p_1,t_1$，就会丢失这个真实二阶基准。
3. **得到完整 raw $M=0$ 返回。** 必须经过(27)(30)要求的有限幅度区域。R520 的局部 $k_s$ 右逆只在其原非零导数邻域有保证，不能沿该较大区域无证延长，更不能在导数退化时重置 $m,T$。

这些结果给出了确定的局部障碍及真实尺度。它们没有把非恒小路径误作闭控制词，也没有由一个局部障碍推出全机制无解。下一真正的正向任务是：在同一个母与固定规范上，支付超出局部盒的受约束几何连接，并保持全部原 $M,T$ 与端 germ；或从起点构造另一个能在该区域持续保持正则的完整 ruling 入口。不同母库的正则性、R518 的成本截面和 R523 的带规范反射，均不能直接替代这一步。

### 来源与审查范围

- R73(6)(9)(10)：本稿全部原 raw 坐标及固定换元；
- R482(12)–(25)：初端势、第三 $W$ 类与完整 history 平方；
- R520：同一个原母、固定第三 Gram、全角归约和真实局部反馈；
- R509：只引用其从真实水平关系导出的(19)，不引用其不同母的端口控制结论；
- R70：仅用于解释本文真实有限幅度要求与旧无 ruling 桥的范围区别。

全部不等式和端口等价在文中直接推导，没有任何新求值、样点、科学执行或复跑。

