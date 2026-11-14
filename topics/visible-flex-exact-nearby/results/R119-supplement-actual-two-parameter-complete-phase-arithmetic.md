# R119 续篇：真实两参数的完整相位算术与实际网络高块

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对每个完整内部负型分量，在已给出的实际两参数盒内，
可以一次选定径向参数，使真实 PDE 的主角和首系数同时满足

$$
 |e^{in\omega_i}-1|>\frac{\kappa_i}{4096|n|},\qquad
 |1+e^{i(n\omega_i+\beta_i/n)}|>\frac1{128N_i|n|}
                       \quad(n\ne0).
 \tag{Q.1}
$$

其中 $\kappa_i$ 是实际可调角窗，$N_i$ 是下面明确的有限整数，不是未付
的小除数常数。第45束已经将这里的 $\omega_i,\beta_i$ 识别为同一个
实际完整返回的首相位；本篇不把任意给定 $\beta$ 误称为自动满足算术。

还得到该新径向候选的一个实际全频网络高块逆：按 (Q.18) 保留真正高块，
所有其余频率、全部 mean、外部接口以及 ordinary/weak source 都作为
独立输入，完整高块的误差反馈 norm 小于 $2^{-30}$。这不是完整低块或
最终 nonlinear regular 逆；新候选的全标签图与第四停止/全模好集也
不由本算术选择自动转移。

## 1. 任意真实小角窗中的明确判别式5目标

固定一个分量，暂写 $\kappa=\kappa_i\in(0,1)$，
$\Omega_0=4\Theta_i(0)$，$\alpha_0=\Omega_0/(2\pi)$。
令 $Q_0=\lceil1024/\kappa\rceil$，取 $p_0$ 为 $Q_0\alpha_0$ 的最近
整数，平局取较小者。约去公因子后记 $p/q=p_0/Q_0$，则

$$
 1\le q<2048/\kappa,\qquad
 |p/q-\alpha_0|\le\kappa/2048.
 \tag{Q.2}
$$

取这个有理数的有限简单连续分数，相邻前一收敛分数记为 $p'/q'$，使
$0\le q'<q$、$pq'-p'q=\pm1$。整数情形取 $q'=0,p'=1$。
令

$$
 H=\max\{4,\lceil1024/(\kappa q^2)\rceil\},\quad
 \varphi=(1+\sqrt5)/2,\qquad
 \alpha=\frac{p(H+\varphi)+p'}{q(H+\varphi)+q'},
 \qquad\omega=2\pi\alpha.
 \tag{Q.3}
$$

相邻行列式准确给

$$
 |\alpha-p/q|<1/(Hq^2)\le\kappa/1024,
 \qquad |\omega-\Omega_0|<3\kappa/256<\kappa/64.
 \tag{Q.4}
$$

所有正部分商都小于 $2048/\kappa$：原有理前缀的部分商不超过 $q$，
新增部分商为 $H+1$，以后全是1；$H+1\le5+1024/\kappa<2048/\kappa$。
由相邻收敛分数的行列式和最佳逼近证明（见 R30 §3，同一初等证明），
若最大部分商为 $K$，则
$\|n\alpha\|_{\mathbb Z}>[(K+2)|n|]^{-1}$。因此
$2\sin(\pi x)\ge4x$ 于 $0\le x\le1/2$ 直接给 (Q.1) 第一式。
它比原 KAM 消费的二阶 Diophantine 形式更强；使用较弱的
$\kappa/(4096n^2)$ 时，旧小除数平方费只增加 $2^{12}$。

写 $u=p,v=Hp+p',r=q,s=Hq+q'$。矩阵
$(u,v;r,s)$ 的行列式是 $\pm1$，而 $\alpha=(u\varphi+v)/(r\varphi+s)$。
消元得到

$$
 A\alpha^2-B\alpha+C=0,
 \quad A=s^2+rs-r^2>0,
$$
$$
 B=2vs+vr+su-2ru,\qquad C=v^2+vu-u^2,
 \qquad B^2-4AC=5.
 \tag{Q.5}
$$

$A,B,C$ 都是奇整数：$r,s$ 与 $u,v$ 各互素，在模2的三个非zero
向量上分别检查 $s^2+rs-r^2$ 和 $v^2+vu-u^2$；$B$ 的奇性来自
$us-vr=\pm1$。共同因子的平方须整除5，所以多项式本原。
又 $s+r\le6q+1024/(\kappa q)<2^{14}/\kappa$，故

$$
                        1\le A<2^{28}\kappa^{-2}.
 \tag{Q.6}
$$

这给实际角窗中的完整二次目标，不需要猜一个近似无理数。

## 2. 在真实首系数的单位窗口中选择完整相位

先用实际第一参数实现 (Q.4)，再沿第43/45束的准确保持主角曲线调第二
参数。设第二步开始时的完整 PDE 系数为 $\beta_0$。取任意已经证明的
$B_*>|\beta_0|+1$，在本题可取

$$
 B_*=2^{62}(j+5)^2\delta_j^{-5},\qquad
 N=\left\lceil64(A+1)(B_*+1)\right\rceil\ge64,
 \quad d=1/64,\quad c=1/(64N).
 \tag{Q.7}
$$

在闭区间 $I=[\beta_0-1,\beta_0+1]$ 删除下面两类**开**坏集：

1. 距格点 $\pi(2\mathbb Z+1)/(2\sqrt5)$ 小于 $d$ 的点；
2. 对某个 $1\le n\le N$、奇整数 $p$，满足
   $|\beta+\pi n(2n\alpha-p)|<c$ 的点。

第一类格点间距为 $\pi/\sqrt5>1$，能与 $I$ 相交的 $d$ 邻域至多4个，
总长度至多 $8d=1/8$。第二类对每个 $n$ 的中心间距是 $2\pi n>6$，
故至多两个相交小区间，全部长度至多 $4cN=1/16$。
留下的闭好集测度至少 $29/16>0$。可一次固定其最小值为 $\beta$；
这只是原点的固定选择，不宣称随未知标签重选最小值会连续。

## 3. 高于有限截止的全部频率

令 $\alpha=(B+\sigma\sqrt5)/(2A)$，$\sigma\in\{\pm1\}$ 是 (Q.3) 的
实际根号。对任意 $n>N$ 和任意奇整数 $p$，置

$$
 q_n=2n,\qquad \varepsilon=q_n\alpha-p,\qquad
 Q=Ap^2-Bpq_n+Cq_n^2\in2\mathbb Z+1.
$$

准确整数范数恒等式为

$$
 Q=A\varepsilon^2-\sigma\sqrt5\,q_n\varepsilon.
 \tag{Q.8}
$$

写完整归一相位距离

$$
 F=n(2\pi\alpha n+\beta/n-\pi p)
    =\beta+\frac\pi2q_n\varepsilon
    =\beta-\frac{\sigma\pi Q}{2\sqrt5}
                       +\frac{\sigma\pi A\varepsilon^2}{2\sqrt5}.
 \tag{Q.9}
$$

若 $|F|<1/128$，由 $\pi>3$、$|\beta|<B_*$ 有
$|q_n\varepsilon|<B_*+1$。于是

$$
 \left|\frac{\pi A\varepsilon^2}{2\sqrt5}\right|
 <\frac{A(B_*+1)^2}{n^2}
 \le\frac{A}{4096(A+1)^2}<1/4096.
 \tag{Q.10}
$$

但 (Q.9) 的格点部分距离至少 $d=1/64$，矛盾。因此所有 $n>N$ 都有
$|F|\ge1/128$；所有 $n\le N$ 则由第二类坏集排除有 $|F|\ge c$。
统一得到

$$
 |2\pi\alpha n+\beta/n-\pi p|\ge c/n
        \quad(n\ge1,\ p\text{ 奇}).
 \tag{Q.11}
$$

再取最近的奇数倍 $\pi$，用 $2\sin(x/2)\ge2x/\pi$ 于 $0\le x\le\pi$，
便得到 (Q.1) 第二式。负 $n$ 由真实共轭得到同样界。这里没有只检查
最接近 $2n\alpha$ 的 $p$；低频的 $\beta/n$ 可改变最近奇格点，所有
可能的奇整数从一开始全部保留。

## 4. 实际参数确实实现这两个目标

原主角逆满足 $|G_i'|<512\sqrt{\Delta_i/\eta_j}$，
$\kappa_i=2^{-25}\sqrt{\eta_j/\Delta_i}$。
(Q.4) 对 $\Theta$ 的改动小于 $\kappa_i/256$，因此实现新主目标的
第一参数满足

$$
                       |\gamma_1^{\rm base}|<2^{-24}.
 \tag{Q.12}
$$

这是同一个实际 profile 的真实复逆，不是参数数量比较。
第45束已经识别完整 $\beta=-b/2$，并证明在保持该主角的曲线上
$|d\beta/d\gamma_2|>2^{-9}\sqrt B$。其双向范围均大于 $2^{55}$，
所以所选 $\beta\in I$ 准确可达，且

$$
 |\gamma_2|,quad|\gamma_1-\gamma_1^{\rm base}|<2^{-86}.
 \tag{Q.13}
$$

两者都严格处于第43束的真实参数盒。各分量的两支集相离，不同分量的
参数不相互改变其径向相位，故所有层可同时选择。
原有限前缀、正型分量和两个 root germ 均准确保持；参考 mean 高度的
积分变化按原式保留。

所构造的是一个**新公共径向度量候选**。后续若对非zero标签保持相同
$(\omega_i,\beta_i)$，必须解其真实联合参数行；本篇没有在一次固定
目标的 Newton 步里悄悄换度量，也没有从逐点好集选择推出标签连续性。

## 5. 真实全层算术常数

旧实际角窗平方下界
$\kappa_i^2>2^{-55}\delta_j^{3/2}/j$ 与 (Q.6)--(Q.7) 给

$$
 N_i<512A_iB_{*,i}
       <2^{160}(j+5)^3\delta_j^{-13/2}.
 \tag{Q.14}
$$

在物理 $M=4|n|$ 单位，定义
$D_{i,m}=1+e^{i(n\omega_i+\beta_i/n)}$，则

$$
 |D_{i,m}|>\frac1{32N_iM},\qquad
 |D_{i,m}^{-1}|<32N_iM
          <2^{165}(j+5)^3\delta_j^{-13/2}M.
 \tag{Q.15}
$$

所以这个已识别的真实首相位模型在同一物理 Fourier 圆上只损失一阶；
并非借一个固定的正角宽掩盖指数小分母。mean 不代入 $\beta/n$，而是
保留第45束的准确两状态系统。

## 6. 完整实际返回网络的高块，所有低历史仍在

第45束的实际返回行有全矩阵形式

$$
 (D_m+\mathcal E_m)z_m=g_m,
 \qquad
 \|\text{第 }i\text{ 行 }\mathcal E_m\|_{
                    \ell^\infty\to\mathbb C}
 <C_i M^{-4/3},\quad
 C_i=2^{5800}(j+5)^{16}\delta_j^{-36}.
 \tag{Q.16}
$$

输入指标包括相邻所有 incoming 端口，故其 row norm 已含有限度数、
真正正型 cross 和完整负区两行。$g_m$ 是实际 ordinary/weak particular、
端点 charge 和外部接口组合；其顺序与第41--45束相同。

用真实的指标/频率投影

$$
 \mathcal H_m=\{i:M\ge T_i\},\qquad
 T_i=2^{18000}(j+5)^{60}\delta_j^{-129},\qquad
 \mathcal L_m=\mathcal I\setminus\mathcal H_m.
 \tag{Q.17}
$$

对固定 $m$，$\mathcal H_m$ 是有限集合；当 $|m|\to\infty$ 时其所有
模式仍按同一个公式保留。它不是删去固定高频。mean 全部属于低输入。
由 (Q.15)--(Q.17)，每个实际高行有

$$
 \|D_{H,m}^{-1}(\mathcal E_m)_{HH}\|_{
                         \ell^\infty\to\ell^\infty}
 <2^{-35}(j+5)^{-1}\delta_j^{1/2}<2^{-30}.
 \tag{Q.18}
$$

所以真正高块解为

$$
 z_{H,m}=
 [I+D_{H,m}^{-1}(\mathcal E_m)_{HH}]^{-1}
 D_{H,m}^{-1}\,[g_{H,m}-(\mathcal E_m)_{HL}z_{L,m}].
 \tag{Q.19}
$$

Neumann norm 小于2。这是**同一实际径向网络**的高块逆；它消费完整
正型 DN，而不是一个理想的单端阻抗。给源范数

$$
 \|g_H\|_{\mathcal Y_{s,\sigma}}
 =\sum_{m\ne0}e^{\sigma M}\langle m\rangle^s
           \sup_{i\in\mathcal H_m}32N_iM|g_{i,m}|,
$$

以及 $z_H$ 的相同范数去掉 $32N_iM$，(Q.19) 直接给 norm 小于2。
这同一 Wiener 权没有固定宽差；完整低历史贡献是
$D_H^{-1}\mathcal E_{HL}z_L$，不是未说明的零边界条件。
实共轭、四重周期和给定 source 的线性性由准确唯一性保留。

正区 weak $F^z$ 的 bare 端迹仍须另外给出；其 total-contact 已在
$g$ 中，不能靠 (Q.19) 删除。物理 mean 高度 $\lambda$、mean flux、
cut128 两迹与所有尚未解的低行也都保持为独立接口。

## 7. 此后真正剩余的逆

这里已经支付真实 $(\omega,\beta)$ 的同时选择、完整模型全频间隙，
以及真实径向返回算子的高块。仍须解含全部 $\mathcal L_m$、mean 和
外接口的真实 Schur 系统，并将它与原标签/平端空间归一。该低集合
随频率变化，不能与旧 $b_m$ 的理想低窗直接等同。
非径向更新还需要两相位不变量的联合参数消去和同一空间的完整余项
估计。既不由 (Q.1) 单独宣布全逆，也不把给定低历史的 (Q.19) 当作
最终 $F(a,f_*)=0$ 已闭合。

[准确整数/有理恒等式与全层预算程序](../scripts/fourfold_actual_complete_phase_arithmetic_20261113.py)
及[完整报告](../notes/2026-11-13-R119-complete-phase-arithmetic-budget.json)
记录构造、坏集长度和实际高块常数。
