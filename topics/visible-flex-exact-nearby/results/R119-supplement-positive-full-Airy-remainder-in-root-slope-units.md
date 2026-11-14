# R119 续篇：完整正片 Airy 余项的根斜率单位

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在第51束同一个实际双端正片、同一个 joint $\Gamma^*(\mathbf a,\Omega)$ 和完整 Airy 波单位中，令两个真实根斜率为 $b_-,b_+>1$，$b_*:=\max(b_-,b_+)$。则真正完整双端 reflection 满足

$$
\boxed{\quad
\|R_++I:H^s(\mathbb T_{\pi/2})^2
                 \longrightarrow H^{s+4/3}(\mathbb T_{\pi/2})^2\|
 <2^{5700}b_*^{4/3},\qquad |s|\le1.
\quad}
\tag{P.1}
$$

两个 mean、两端之间的 transmission、相反 Fourier 锥以及全部 angular lag 都在这个算子中。这里 $R_+$ 的真实 low block 未被替换为 $-I$。证明中只将低频**试解**设为零；由完整 graph 恒等式保留了其所有真输出。

本篇改进的是第51束 (H.19) 的收费单位。它不改任何实际 profile 参数，也不提前授予一个新的全网络 cutoff。根的完整一次积分、负段及 graph 还须与这个因子接合。

## 1. 当前正片与原完整 form

使用 [实际正片 DN/Cayley/source 定理](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md) 的真实闭 form、两个 mean、两端法向以及完整 regularized root frame。沿当前实际负窗控制，两个 root germ 不变；非径向背景及 joint 两列并未冻结。

[实际完整余项](R119-supplement-actual-nonradial-full-remainder-and-high-network.md) §5 已在本对象上重新支付：每端的 canonical 正 collar 为 $0\le y\le H=1/64$，

$$
P_{+,e}=-\partial_y^2-{y\over b_e^2}\partial_\phi^2-V_e(-y,\phi),
\quad |V_e|<17,\quad
|\nabla\log\alpha_e^{-1/2}|_{\operatorname{diag}(1,y/b_e^2)}<5.
\tag{P.2}
$$

两个 collar 相离，整个正片依然共同求解；没有在 $y=H$ 添加边界条件。原完整 Poisson 常数 $P_*<128$ 在各 collar 的实际频率

$$
\lambda_{e,m}=|m|/b_e,\qquad m\in4\mathbb Z,
\tag{P.3}
$$

单位中成立。以 $H^r_{\lambda_e}$ 表示权 $(1+\lambda_{e,m}^2)^{r/2}$，完整 contact 是同一 Poisson 算子的负 adjoint。因此 canonical ordinary collar 源给

$$
\|K_c f\|_{(H^{1/3}_{\lambda_-}\oplus H^{1/3}_{\lambda_+})^*}
 <2^{12}\|f\|_{\bigoplus_e L^2_yH^{-2/3}_{\lambda_e}}.
\tag{P.4}
$$

这里原128已经是两 collar 联合 norm；标准权与原 $\sigma_{e,m}$ 的比较至多2倍，再乘原复 form Neumann 的16倍余量，合计 $128\cdot2\cdot16=2^{12}$。它同时适用于 $|\operatorname{Im}z|<1/256$ 的真实角平移族。其证明与原 (C.19)、(C.28)–(C.32) 是同一个完整 form/resolvent 证明；未从实参数 positivity 猜测复参数 unitarity。

在实参数上，完整 $R_+$ 为 onto unitary。在上述较窄复条带，原第51束的全 graph 比较给 $\|R_+(z)\|_{L^2}<2$；实参数的 $H^r$ norm 也小于2，$|r|\le4$。该事实已经包含实际 root density、normal shear 和原 mean frame，不把参考 Cayley $\mathcal C_a$ 与 Airy $R_+$ 混同。

## 2. contact 到原 Airy 波的准确频率因子

令 $c=c_A^{-1/2}$，$c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0)$，仍取原两列

$$
D_\pm(\xi,m)=c\lambda_{e,m}^{-1/3}
[\operatorname{Bi}(-\xi\lambda_{e,m}^{2/3})
 \pm i\operatorname{Ai}(-\xi\lambda_{e,m}^{2/3})],\quad m\ne0,
\tag{P.5}
$$

以及 mean 的 $c(1\pm i\xi/\pi)$。其 determinant 对每模都是 $-2ic^2/\pi$，完整 Green 因子相同。

零 Dirichlet 的 contact correction 到任一 Airy 波，在 $m\ne0$ 上的准确模为

$$
{\pi\operatorname{Ai}(0)\over c}\lambda_{e,m}^{-1/3}.
\tag{P.6}
$$

因而相对于 (P.4) 的 contact norm，其算子因子为

$$
N_{e,m}={\pi\operatorname{Ai}(0)\over c}
      \lambda_{e,m}^{-1/3}(1+\lambda_{e,m}^2)^{1/6}.
\tag{P.7}
$$

原 Airy 常数给两个充分门

$$
N_{e,m}<4\quad(\lambda_{e,m}\ge1),\qquad
N_{e,m}<4b_*^{1/3}\quad(m\ne0),
\tag{P.8}
$$

mean 的独立因子 $\pi/(2c)<2$。真实 physical shear 在定义 canonical contact 时已按原式减去；零 Dirichlet correction 没有额外的 height-shear 项。没有把 (P.8) 的第二个因子直接当作高输出的费用。

## 3. 一个完整的高频试解，低列保留为误差

置

$$
L=2^{4200}b_*,\qquad P_H=\mathbf1_{\{|m|\ge L\}},\qquad
P_L=I-P_H,\qquad \mathcal D=\langle D_\phi\rangle.
\tag{P.9}
$$

对每端的高输入，使用与原 incoming 一、outgoing 负一**准确相同**的 Ai trial：

$$
U_{{\rm tr},e}(y,m)=2ic\lambda_{e,m}^{-1/3}
       \operatorname{Ai}(y\lambda_{e,m}^{2/3})\chi(y).
\tag{P.10}
$$

$\chi=1$ 于 $[0,H/2]$、$\chi=0$ 于 $[H,\infty)$，中间使用五次 cutoff。其前二导数满足

$$
\|\chi'\|_\infty\le15/(4H)<2^8,\qquad
\|\chi''\|_\infty\le24/H^2<2^{17}.
\tag{P.11}
$$

在**全部** $P_L$ 输入列取零 trial，包括两个 mean。后面这些列给 $E_A=-I,E_B=I$；它们不表示真实 reflection 已被指定。

每个高输入 trial 的完整 ordinary residual 为

$$
f_{{\rm tr},e}=-\chi V_e U_{0,e}
       -2\chi'\partial_yU_{0,e}-\chi''U_{0,e},\qquad
U_{0,e}=2ic\lambda_{e,m}^{-1/3}\operatorname{Ai}(y\lambda_{e,m}^{2/3}).
\tag{P.12}
$$

trial 在 collar 外零延拓的两 jets 匹配，所以没有接缝 delta source。两端 trial 同时保留其各自的真 $b_e$。

## 4. 原物理频率中的完整 residual 预算

本节在 $|\operatorname{Im}z|<1/256$ 的同一个复族上作估计。由剩余角宽，$|\partial_\phi V_e|<2^{13}$。乘法、插值和对偶给

$$
\|M_{V_e}:H^{-2/3}_{\lambda_e}\to H^{-2/3}_{\lambda_e}\|<2^{16}.
\tag{P.13}
$$

因为 $b_e>1$，角 Fourier lag 的权比不超过 $(1+|m-n|)^{2/3}$；该界不依赖于 $b_e$。两个 collar 的源范数取直和，不将每个输入单列的界冒作全矩阵界。

准确积分 $\int_0^\infty\operatorname{Ai}(q)^2dq=\operatorname{Ai}'(0)^2$，连同变量 $q=y\lambda^{2/3}$ 和 Parseval，给 potential residual 右乘 $\lambda^{4/3}$ 后的 norm 小于 $2^{20}$。这里所有输入 $\lambda\ge2^{4200}$，因此 $(1+\lambda^{-2})^{1/3}<2$；没有使用可能趋于0的全局最小 $\lambda$。

两个 cutoff 项使用原已证正轴 Airy 衰减。可统一取 tail 常数 $M_*<2$、

$$
\kappa_H=(H/2)^{3/2}/3>2^{-13},\qquad
\sup_{\lambda>0}\lambda^{2/3}e^{-\kappa_H\lambda}<2^9.
\tag{P.14}
$$

故它们右乘 $\lambda^{4/3}$ 后分别小于 $2^{23}$ 和 $2^{22}$。这些是原完整 (P.12) 三项，不只估计一个 formal potential 项。

改回 $\mathcal D^{4/3}$ 时，$\langle m\rangle^{4/3}<2b_e^{4/3}\lambda_{e,m}^{4/3}$。合并两端、三项和标准权，得到

$$
\boxed{\quad
\|f_{\rm tr}P_H\mathcal D^{4/3}:
 L^2(\partial I)^2\to\bigoplus_eL^2_yH^{-2/3}_{\lambda_e}\|
 <2^{30}b_*^{4/3}.
\quad}
\tag{P.15}
$$

这条界包含 $V_e$ 的全部 Fourier lag、跨锥及 mean 输出。

## 5. 真正隔带消掉 contact 的低频因子

用整个正片的真实零 Dirichlet inverse 修正 trial。它在两端的 incoming/outgoing 分别记为

$$
A_{\rm in}=I+E_A,\qquad A_{\rm out}=-I+E_B.
\tag{P.16}
$$

对高输入，(P.4)、(P.8)、(P.15) 首先给全输出复族的安全界

$$
\|E_A(z)P_H\mathcal D^{4/3}\|,
\ \|E_B(z)P_H\mathcal D^{4/3}\|
 <2^{46}b_*^{5/3}.
\tag{P.17}
$$

但若输出限制在 $|m|\ge L/2$，则其 $\lambda_{e,m}\ge2^{4199}$，可以使用 (P.8) 的**第一**界；于是 (P.17) 改为 $2^{46}b_*^{4/3}$。

剩下的输出满足 $|m|<L/2$。由于正型 form、Poisson/contact 和 trial 系数在同一真实角平移条带组成有界全纯族，(P.17) 对该族的额外平移仍成立。先取 $|\operatorname{Im}z|<1/1024$，再沿输入正负 Fourier 锥分别取相反的额外平移 $\pm i/512$。总平移小于 $1/256$。

例如正输入 $n\ge L$ 和输出 $|m|<L/2$，写

$$
E(z)=e^{\sigma D_\phi}E(z+i\sigma)e^{-\sigma D_\phi},
\qquad \sigma=1/512,
\tag{P.18}
$$

必要时统一反转 $z$ 的平移号数。输入、输出 spectral projections 与这些指数可交换，给真正的**算子 norm**因子
$e^{\sigma L/2}e^{-\sigma L}=e^{-L/1024}$。它不是对单个 kernel entry 作估计后漏掉无限行和。负输入使用相反号；两锥只增加因子2。

因为 $b_*>1$、$L=2^{4200}b_*$，初等 $e^x>x$ 已给

$$
b_*^{1/3}e^{-L/1024}<1.
\tag{P.19}
$$

因此低输出/高输入部分也小于 $2^{47}b_*^{4/3}$。连同高输出，得到在 $|\operatorname{Im}z|<1/1024$ 上统一的

$$
\|E_A(z)P_H\mathcal D^{4/3}\|,
\ \|E_B(z)P_H\mathcal D^{4/3}\|<2^{48}b_*^{4/3}.
\tag{P.20}
$$

真实低输入没有消失：零 trial 准确给 $E_AP_L=-P_L,E_BP_L=P_L$，故

$$
\|E_AP_L\mathcal D^{4/3}\|,
\ \|E_BP_L\mathcal D^{4/3}\|
 <2L^{4/3}=2^{5601}b_*^{4/3}.
\tag{P.21}
$$

于是全输入的两个误差右乘 $\mathcal D^{4/3}$ 均小于 $2^{5602}b_*^{4/3}$。两端的 mean 以及每个低频输入产生的无限输出，都将在下一节通过真正的 $R_+$ 保留。

## 6. 完整 graph、两侧强增益与 Sobolev 窗

每个修正 trial 都属于实际完整 homogeneous 正片 graph，所以

$$
R_+A_{\rm in}=A_{\rm out},\qquad
\boxed{\ R_++I=E_B-R_+E_A.\ }
\tag{P.22}
$$

不需要反解 $A_{\rm in}$。在复条带内用 $\|R_+(z)\|<2$，得到

$$
\|(R_+(z)+I)\mathcal D^{4/3}\|<2^{5604}b_*^{4/3}.
\tag{P.23}
$$

令 $S=R_++I$。对实角平移，(P.23) 正是 $S\mathcal D^{4/3}$ 的共轭族；Cauchy 到四阶给 $k!1024^k$，$k\le4$。完整 Leibniz、adjoint、对偶和插值将这些有限 commutator 界变为

$$
\|S\mathcal D^{4/3}:H^r\to H^r\|
 <2^{5660}b_*^{4/3},\qquad |r|\le3.
\tag{P.24}
$$

例如 $4!1024^4<2^{45}$，四阶 Leibniz 的16项及 norm 等价仍在56 bits余量内。负阶使用同一个实际 adjoint 的 commutator，不能只从正阶插值跳过 dual domain。

实参数的完整 unitarity 准确给

$$
S=S^*R_+.
\tag{P.25}
$$

因此 (P.24) 的 adjoint 以及 $\|R_+:H^r\to H^r\|<2$ 给

$$
\|\mathcal D^{4/3}S:H^r\to H^r\|
 <2^{5661}b_*^{4/3},\qquad |r|\le1.
\tag{P.26}
$$

先在有限 Fourier 数据上应用，再使用已界定 adjoint 和闭 Fourier 权，得到整个所述空间上的结论。这证明 (P.1)。没有借助全网络解、近核集中于低锥或某个尚未实现的参数选择。

## 7. 实际 source 和剩余拼接

本篇仅换 trial 的证明 cutoff，不改真实正片。ordinary/weak affine 列仍是原 (C.29)–(C.33) 的完整列，包括

$$
\langle(q_{\mathcal F})_-+(q_{\mathcal F})_+\rangle
=\int_I\langle\widehat s\rangle\,dt,
\tag{P.27}
$$

以及两个 mean、实际材料 Jacobian、normal shear 和 total/bare 端点荷。若将参数响应或两条 $D\Gamma^*$ 放到源端，也必须照此换算；(P.1) 不使这些列为零。

完整负 Cauchy 的 low 条件数不再通过这个正型因子重付。消费本篇时可直接使用真正 unitary 的 $R_+$：例如 $(R_++I)S_-$ 的 $L^2$ 右输入费用只需 $\|S_-\|=1$。若还需要更大的有权窗口或 physical trace 恢复，必须使用对应原单位的实际合同。

新的界覆盖完整实际正片，不是半线 Ai impedance，也不是有限频率试算。全负段、一次 root 首符号、graph 和混频 Schur 的接合继续进行；课题完成标准仍未达到。

## 8. 证据范围

本篇复用第51束在**本对象**上已付的 canonical collar、全 form 与 Poisson 常数。通用 trial/contact/Green 代数与 [完整 Airy contact 方法](R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md) §4–9 相同；没有移用该另一有限帽的数值常数或其旧频率因子。

本篇新的预算均为显示的初等不等式。[源码](../scripts/fourfold_positive_root_slope_remainder_20261114.py) 与独立输入清单由本公开仓库 Actions 实际执行；未执行前不声称任何新增 native 已通过。

```bash
python3 topics/visible-flex-exact-nearby/scripts/fourfold_positive_root_slope_remainder_20261114.py --manifest topics/visible-flex-exact-nearby/notes/2026-11-14-R119-positive-root-slope-remainder-inputs.json --out topics/visible-flex-exact-nearby/notes/2026-11-14-R119-positive-root-slope-remainder-budget.json
```
