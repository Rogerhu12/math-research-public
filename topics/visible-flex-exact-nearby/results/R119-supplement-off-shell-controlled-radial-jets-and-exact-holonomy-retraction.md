# R119 续篇：非解背景的无额外层损径向 jets 与准确 holonomy 重建

2026-11-15，visible-exact / tail_connector。

**状态：已证明（声明域内）。** 本篇为有限 Sobolev 迭代确定一个
更窄、但含已知实际成员的背景域。仅有前篇 B 的任意径向 $C^4$ 球，
不能把其 $\ell_j^{-4}$ 费用灌入旧 middle 比较：
那会耗掉深层真正的 $75/256$ 余量。这里增加的是实际 residual
本身的前三阶 scaled 径向 norm。准确原单位转换给它额外的
$\delta_j^{16}$；使用 $K_t=F+\mathfrak r$ 而非假设 $\mathfrak r=0$ 后，根和 strict
所需有限 jets 因而不增加旧非径向量的负层幂。

第二部分给 holonomy-one 图中的准确 residual 投影和二阶状态重建。
完整 ordinary mean 没有被删去；它由真正加权平均决定。
本文不把这些局部/非线性恒等式单独称为新的全网络 inverse。
后继仍须支付变化背景的完整 high/middle/deep 与帽接口。

## 1. 对象、单位及新增 residual 域

沿用
[有限径向首相位](R119-supplement-finite-radial-Sobolev-first-phase-and-fixed-second-parameter-gap.md)
B.1--B.4 与
[非解背景准确散度差](R119-supplement-exact-off-shell-divergence-Jacobi-and-narrow-residual-defect.md)
O.1--O.17。记
$$
 J_j=j+5,\qquad
 \ell_j=2^{-64}J_j^{-2}\delta_j^4,\qquad
 c_j(t)=\frac{\mu_jp_*(t)^2}{12r(t)^{10}},
 \qquad
 C_j=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2}.
 \tag{C.1}
$$
$c_j$ 是 physical ordinary residual 的转换系数，
不是状态 $K$ 的 mean，也不是 Fourier 频率。
仍有 $t=\log a_{\rm ph}$、$a_{\rm ph}=\rho r$、
$w=\mu_jp_*/r^7$、$1\le r\le2$、$p_*\ge\delta_j/2$。
所有这些式子使用同一个当前 metric；参数对 $t$ 固定。

对真实四态
$Z=(P,K,U,V)$，$U=P_\theta,V=K_\theta$，取
$$
 P_t=V-(A+1)P,\qquad
 \mathfrak r=K_t-F(P,K,U,V),\qquad N=c_j\mathfrak r,\qquad A=-Q .
 \tag{C.2}
$$
第一式是由真实高度给出的运动学恒等式。
第二式定义非解背景的实际 residual，不把它设为零。
全文用 $\mathfrak r$ 表示 residual；无花体 $r$ 始终是原物理半径。

用 $C_j^\#$ 表示原六个实际邻胞的 $C$ 和，缺失胞不添项。
对本篇出现的有限整数 $s$，定义
$$
 \mathscr B_s=\sup_j(C_j^\#)^{-1}\sup_{I_j}\|Z\|_{H^s},\qquad
 \mathscr N_s^{[3]}
 =\sup_j\frac1{\zeta_j\delta_j^{16}}
       \max_{0\le a\le3}\ell_j^a
                    \sup_{I_j}\|\partial_t^aN\|_{H^s}.
 \tag{C.3}
$$
径向导数按原有限分片取单侧值；根 collar 内使用同一个真实 germ。
在普通接缝处仍要求 B 的四态和一阶 traces 相等。
本篇所有下述 jet、strict 和重建结论均限定在
$$
 R_s:=\mathscr B_{s+4}+\mathscr N_{s+4}^{[3]}
       \le R_*:=2^{-2097152},\qquad 0\le s\le4416,
$$
并满足 B 的其余真实背景、小根和接缝条件。
这里的角阶至多4420，严格在 B 的8196阶输入内；
只写出某个低阶结论并不取消它所引用的高阶输入条件。

可以另给有限 connector 同样的 norm：
以 $\ell_o=2^{-1024}$，直接按其真实原方程 residual
$\max_{a\le3}\ell_o^a\|\partial_t^a\mathfrak r_o\|_{H^s}$ 收费。
有限 connector 的 $c_o^{-1}$ 必须按其原物理源合同另付；
(C.1) 的内部 $\mu_j,p_*$ 公式不移用到该有限元件。

## 2. 准确 scalar 转换，不损失 $\delta^{16}$

从 $w=\mu_jp_*/r^7$ 和 $r_t=r$ 得
$$
 (\log p_*)_t=A+7,\qquad
 \boxed{\quad(\log c_j)_t=2A+4.\quad}
 \tag{C.4}
$$
这保留当前两个 metric bump 和整个 shape，未对 $c_j$ 作冻结。

B.4 的真实 profile 表给
$$
 \ell_j|(\log c_j)_t|<2^{-50},\quad
 \ell_j^2|(\log c_j)_{tt}|<2^{-109},\quad
 \ell_j^3|(\log c_j)_{ttt}|<2^{-165}.
 \tag{C.5}
$$
例如第一式用
$2^{14}J_j\delta_j^{-3/2}\ell_j
 =2^{-50}J_j^{-1}\delta_j^{5/2}$；
后两式分别用 $2|A_t|$ 和 $2|A_{tt}|$。
因而对 $a\le3$，$(c_j^{-1})^{(a)}$ 的普通 Bell 展开，
连同 Leibniz 的完整二项式和，只增加小于4的因子。
另一方面，
$$
 c_j^{-1}\zeta_j\delta_j^{16}
 =\frac{12r^{10}}{p_*^2}\frac{\zeta_j}{\mu_j}\delta_j^{16}
 <2^{-184}h_j^5 C_j\delta_j^{16}.
 \tag{C.6}
$$
这里 $12r^{10}/p_*^2<2^{16}\delta_j^{-2}$，
而 $\zeta_j/\mu_j=2^{-200}h_j^5 C_j\delta_j^2$。
故安全地有
$$
 \boxed{\quad
 \max_{a\le3}\ell_j^a
       \|\partial_t^a\mathfrak r\|_{H^s}
 \le2^{-170}h_j^5 C_j\delta_j^{16}\mathscr N_s^{[3]} .
 \quad}                                                   \tag{C.7}
$$
这个上界是完整原方程 residual 的球，不只是非mean分量。

## 3. 真根上的 source jets

取原根 $x=\varsigma b_e(t-t_e)$。
旧根和新增 simple 根的准确 polynomial $B_0=Q/x$、
四阶导数及与接缝分离的量词，正是 B.4 后补充的独立输入。
本节不从一般 $C^4$ profile 推出 $B_0^{(4)}$。

对于内部根，$b_e\ge\delta_j^{-9/4}$。
所以每个 $0\le a\le3$，
$$
 b_e^{-a-1}\ell_j^{-a}
 \le2^{64a}J_j^{2a}\delta_j^{\,9/4-7a/4}.
$$
将 (C.7) 代入，最大项在 $a=3$，得到
$$
 \boxed{\quad
 \max_{a\le3}\left\|
       \partial_x^a\frac{\mathfrak r}{b_e}\right\|_{H^s}
 \le2^{22}h_j^5J_j^6 C_j\delta_j^{13}\,
                                   \mathscr N_s^{[3]} .
 \quad}                                                   \tag{C.8}
$$
实际 $j\ge129$ 时，$h_j<1$ 且
$2^{22}J_j^6\delta_j^{13}<1$。
因而这三阶源不会把一个 $\ell_j^{-4}$ 因子带进根的非径向量。

更一般地，固定 $s\le4416$，继续使用第1节已声明的
$R_s=\mathscr B_{s+4}+\mathscr N_{s+4}^{[3]}\le2^{-2097152}$
及 B 的其余完整背景条件，则
$$
 \max_{a\le4}\sup_{\rm root}
       \|\partial_x^a Z\|_{H^s}
          \le2^{131072}C_j^\#R_s .
 \tag{C.9}
$$
证明不需要复角或复径向求值。把
$$
 \mathcal F_1=V-(1-Q)P,\qquad
 \mathcal F_2=F,\qquad
 (P,K)_x=\frac{\varsigma}{b_e}
                         [(\mathcal F_1,\mathcal F_2)+(0,\mathfrak r)]
 \tag{C.10}
$$
连续微分至三次，再在 $U,V$ 行准确多取一次 $\theta$ 导。
右边实际 source 只到 $\mathfrak r$ 的第三 $x$ 导和第四角导，
已由 (C.8) 及 $\mathscr N_{s+4}^{[3]}$ 给出。
$Q=xB_0$ 的前四导固定有界，
$q=w^2$ 满足 $q_x=-2\varsigma Qq/b_e$。
商的唯一非trivial分母仍是 $J=1+K+(1+q)U$，
完整小球给 $|J^{-1}|<2$。

为明确高角阶的完整 Nemytskii 费用，置 $\sigma=s+4\le4420$。
全 signed Fourier 和、包括 mean，给
$\|fg\|_{H^\sigma}\le2^{\sigma+2}
 \|f\|_{H^\sigma}\|g\|_{H^\sigma}$：
用 $\langle m+n\rangle^\sigma\le
2^{\sigma-1}(\langle m\rangle^\sigma+\langle n\rangle^\sigma)$
及 $H^1\hookrightarrow\mathcal A_0$ 的常数2即可。
故 $2^{\sigma+2}\|\cdot\|_{H^\sigma}$ 是一个归一化 Banach
algebra norm。

这里 $\mathcal A_0$ 只是完整无角宽 Fourier $\ell^1$ norm。
原 $\sum_j(K_j^{\rm ref})^2C_j<2^{160016}$ 及 $K_j^{\rm ref}>1$
使每个至多六项的真实 $C_j^\#<2^{160020}$；
即使规范重编号重复一个邻胞，这个宽界也保留全部计数。
因此本篇 $R_s\le2^{-2097152}$ 的输入给
$$
 2^{\sigma+2}\|J-1\|_{H^\sigma}
       \le2^{\sigma+4+160020-2097152}<2^{-1932700}<1/4 .
 \tag{C.9a}
$$
对 $D-1$、$1-qP^2-1$ 也用完整代数乘法得到同一更宽的
$1/4$ 门。于是 $J^{-1}$ 的**完整无限几何级数**在该代数收敛，
$\|J^{-1}-1\|_{H^\sigma}\le2\|J-1\|_{H^\sigma}$。
所需有限个整数/半整数幂使用同一绝对收敛二项式级数；
幂数绝对值不超过16，相关系数可统一放宽为 $2^{64}$。
这同时支付了任意高角阶，而不是只支付四次径向 chain rule。

随后四次径向求导按准确公式展开；
每项至多八个状态/方向 jet，已经求和的完整逆幂作为一个
bounded coefficient 保留。
二项式、四次链式法则、两行、补充角导及上述 $2^{64}$
可统一付 $2^{8(s+4)+4096}<2^{40000}$。
参考 $q,Q$ 的有限系数、原两 mean 和相邻根计数
放宽至 (C.9) 的131072 bits还有充分余量。
这里没有要求第五径向导数。

## 4. formal 径向导数与实际 residual 的准确差

为了避免把“使用原方程”误写成假设背景已经是解，
定义局部 jet 代数上的导数 $\mathfrak D$：
$$
 \mathfrak D Q^{(a)}=Q^{(a+1)},\quad
 \mathfrak D q=-2Qq,\quad
 \mathfrak D\partial_\theta^\ell(P,K)
       =\partial_\theta^\ell(\mathcal F_1,\mathcal F_2).
 \tag{C.11}
$$
对任意实际局部函数 $H$，准确有
$$
 \partial_t H=\mathfrak D H+
    \sum_{\ell\ge0}(\partial_\theta^\ell \mathfrak r)
                         \partial_{K_\ell}H ,
 \qquad K_\ell=\partial_\theta^\ell K .
 \tag{C.12}
$$
和式只遍历 $H$ 实际依赖的有限 jets。
这是一条 chain rule，不要求 $\mathfrak r=0$。

例如
$$
 (P,K)_{tt}
 =\mathfrak D(\mathcal F_1,\mathcal F_2)
   +D_{(P,K)}(\mathcal F_1,\mathcal F_2)[0,\mathfrak r]+(0,\mathfrak r_t).
 \tag{C.13}
$$
继续两次得到四阶差：每个新增项至少含
$\mathfrak r,\mathfrak r_t,\mathfrak r_{tt},\mathfrak r_{ttt}$ 中的一项或它的真实角导数。
所有零 residual 部分仍是原完整局部公式，
包括 $K$ mean 与全部 multiplication/primitive mean 行。
(C.12)--(C.13) 给出了可逐项核验的递推，不以
“沿解相同”跳过非解背景的差项。

特别，B/O 的 $D=1-q(2K+K^2+(1+q)P^2)$ 满足
$$
 \boxed{\quad
 D_t-dD_\theta
       =-2Qq\,UD/J-2q(1+K)\mathfrak r.
 \quad}                                                   \tag{C.14}
$$
因此旧 fixed-$t$ K.10 的正确非解版本为
$$
 \bar d\,\chi_\phi/\chi-\chi_t/\chi
       =-2Q(qU/J)\circ\Phi
          -2(q(1+K)\mathfrak r/D)\circ\Phi .
 \tag{C.15}
$$
完整通量 primitive 的第一行只多这一真实 diagonal 项；
$\eta_t,\phi_t,\bar d$ 则使用实际 $v_t$，
其中新增的准确相对项为
$$
 (\partial_t v)_{\rm residual}
          =-v\left(\frac1J+\frac{q(1+K)}D\right)\mathfrak r .
 \tag{C.16}
$$
原 $c$ 与 $u$ 的两条 mean 方程保留同一结构，
其中所有 $\chi,\eta,\bar d$ 均取当前真实值；不冻结这些系数。
这保留 same-$t$ ordinary/weak 源的 Piola 恒等式，
没有把未知源拉到 mixed 曲线后免费读取其 trace。

## 5. strict 密度中的 residual 收费

在原 fixed root cut 外，$Q>2^{-9}$。
仍用原准确
$$
 T=G/\Lambda,\quad l=\log\Lambda,\qquad
 \kappa=-\tfrac12\operatorname{div}(T\nabla l)
                 -\tfrac14\nabla l\cdot T\nabla l .
 \tag{C.17}
$$
把其中每个径向态导数用 (C.12) 展开。
这里可直接代入同一原角、原径向变量中的完整矩阵
$$
 \Lambda=\frac{w}{a_{\rm ph}}\frac{\sqrt Q}{D},\qquad
 l=\log\frac{w}{a_{\rm ph}}+\tfrac12\log Q-\log D,\qquad
 T=\frac{J}{\sqrt{QD}}
   \begin{pmatrix}1&-d\\-d&d^2-QD/J^2\end{pmatrix}.
$$
它没有 $q^{-1}$ 因子，两个 mean 仍在 $J,D,d$ 的真实表达式中。
记 $\kappa_{\rm on}(Z,Q,q)$ 为只保 $\mathfrak D$ 部分的表达式，
$\kappa_{\rm res}=\kappa-\kappa_{\rm on}$。
它是一个准确的 algebraic 分解，不另引入一个虚构解背景。

$\kappa_{\rm res}$ 中最高径向源导为 $\mathfrak r_t$。
最高角源导可以保守收在 $H^{s+2}$；
二次项至多含 $\mathfrak r^2$。逐 (C.17) 的两个二阶项和两个平方项，
原 profile 表与 $Q>2^{-9}$ 给
$$
 \begin{split}
 \|\kappa_{\rm res}\|_{H^s}
 \le 2^{131072}J_j^4\delta_j^{-6}
 \big(&\|\mathfrak r_t\|_{H^{s+1}}+\|\mathfrak r\|_{H^{s+2}}\\
                         &+\|\mathfrak r\|_{H^{s+2}}^2\big).
 \end{split}                                             \tag{C.18}
$$
这里最大的 profile 单项只用 $Q_t^2$ 或 $Q_{tt}$；
它们分别由 $2^{36}J_j^2\delta_j^{-6}$、
$2^{26}J_j\delta_j^{-9/2}$ 支付。
所有 $Q^{-1/2}$ 的幂因固定 strict cut 而有固定界。
在 (C.12) 展开后，含 $\mathfrak r$ 的系数不含一个未支付的 $K_t$。

尤其由 (C.7)，
$$
 \|\mathfrak r_t\|_{H^s}
 \le2^{-106}h_j^5J_j^2 C_j\delta_j^{12}
                               \mathscr N_s^{[3]} .
 \tag{C.19}
$$
再乘真实 strict 长度 $<4\delta_j$，
(C.18) 的新增完整积分上界小于
$2^{130970}h_j^5J_j^6 C_j\delta_j^7
 \mathscr N_{s+2}^{[3]}$，放宽即可纳入
$$
 \int\|\kappa-\kappa_{\rm rad}\|_{H^s}\,dt
 \le2^{131076}J_j^3\delta_j^{-5}C_j^\#
        (\mathscr B_{s+4}+\mathscr N_{s+4}^{[3]}).
 \tag{C.20}
$$
零 residual 部分逐项使用原 strict 密度公式，
其 profile 幂仍是原 $J_j^2\delta_j^{-5}$；
这里只把角解析乘法费换为前述有限 Sobolev 的实际费用。
$\mathfrak r_t$ 新项带 $\delta^{12}$，所以不增加 (C.20) 的负层幂。

若还取一次真实径向变差，新增项至多含 $\mathfrak r_{tt}$、
$\mathfrak r_{t\theta}$、$\mathfrak r_{\theta\theta\theta}$ 及已列项的积。
用 $Q,Q_t,Q_{tt},Q_{ttt}$，
可以统一放宽系数为 $2^{131072}J_j^6\delta_j^{-9}$。
而 (C.7) 给
$\|\mathfrak r_{tt}\|<2^{-42}h_j^5J_j^4C_j\delta_j^8
\mathscr N_s^{[3]}$。
乘真实长度，新增 integral variation 至多
$2^{131032}h_j^5J_j^{10}C_j\mathscr N_{s+3}^{[3]}$。
原有限 seam 的两侧 traces 按同式加入；每胞不超过32个，
均保留，故
$$
 \operatorname{TV}_t\kappa_{\rm res}
       \le2^{131080}C_j\delta_j^{-1}
                              \mathscr N_{s+3}^{[3]} .
 \tag{C.21}
$$
最后用了实际所有 $j\ge129$ 上 $J_j^{10}\delta_j<1$。
原固定 $Q$ 的 seam 跳仍属于 $\kappa_{\rm on}$；
不因这次分解而删除。

(C.9)、(C.15)--(C.16)、(C.20)--(C.21) 是后续 real root、
strict 和有序两窗比较所需的非解输入。
它们不声明旧完整余核已经具有一个统一 analytic-lag 图。

## 6. 保完整 mean 的相容投影与 smoothing

现在只考虑实际存在性所需的 holonomy-one 背景子图：
用 M 的同一个准确小根
$$
 \Phi_q(P,K_\perp+\kappa)=0
$$
重建 $K$ 的 mean，并以原全径向积分保留独立高度 gauge。
这不是设 $K_0=0$。对任何这个图中的非解背景，
M.16 的准确恒等式给
$$
               \langle A_0N\rangle=0,\qquad
                   A_0=JD^{-3/2}.
 \tag{C.22}
$$
$N$ 的普通 Fourier mean 一般非零；(C.22) 是完整加权条件。

定义实际投影
$$
 \Pi_{A_0}g=g-\frac{\langle A_0g\rangle}{\langle A_0\rangle}.
 \tag{C.23}
$$
它映到 (C.22) 的核，并且 $\Pi_{A_0}^2=\Pi_{A_0}$。
本篇小球给 $3/4<\langle A_0\rangle<5/4$、
$\|A_0\|_{L^2}<5/4$，故在每个 $H^s$，$s\ge0$，
$\|\Pi_{A_0}\|<4$。
区别于普通非mean投影的是一个完整 constant 输出列，
输入 functional 依赖真实 $A_0$。

令 $S_M$ 为同一物理角上任何标准 Fourier smoothing，
并令 $\mathcal T_M=\Pi_{A_0}S_M$。
若 $\Pi_{A_0}g=g$，则准确有
$$
 \mathcal T_Mg-g=\Pi_{A_0}(S_M-I)g,\qquad
                    \langle A_0\mathcal T_Mg\rangle=0 .
 \tag{C.24}
$$
因此标准有限 Sobolev smoothing/tail 门只增加显示的4。
取 scaled 径向 jets 时必须 Leibniz 微分
$\Pi_{A_0}$；这些 finite-rank 行由 (C.9)、(C.12) 及同一
真实 scalar 分母支付，不能写成 $[\partial_t,\Pi_{A_0}]=0$。
本篇不在此处预先指定全部迭代的 smoothing 频率。

## 7. 几何 proxy 的准确切向性

保持 metric 固定，给相容 ordinary 源 $g$，
即 $\langle A_0g\rangle=0$。
设同一个真实源域中的完整解满足
$$
 c_j\mathcal J_Wh=-g ,
$$
并保平端 total-flux mean 为0、所有原连接的 total flux 匹配。
这里只消费已经存在的解；其 inverse 仍须由完整网络证明提供。

O 的准确 Green 身份给
$$
 \partial_t D\chi_W[h]
      =12\mu_jr^{-4}\langle A_0c_j\mathcal J_Wh\rangle=0.
 \tag{C.25}
$$
所以 $D\chi_W[h]=0$，即该完整校正恰在 holonomy-one 图的切空间。
真实高度常数由原 gauge 决定，不由这个式子固定。
若有 metric、weak 端原子或外 mean 荷，(C.25) 右边必须
加入原对应项；本篇没有把它们归入相容 ordinary 源后丢掉。

特别取 $g=N$。对字面上的高度线段，O.21--O.22 已给
$$
 N(W+Dh)=
       -\mathcal E_N[h]-c_j e_2,\qquad
 \mathcal E_N[h]=\alpha Nk-\beta N_\theta p-\gamma Np .
 \tag{C.26}
$$
这里 $Dh$ 指高度产生的四态增量；
$e_2$ 是完整非线性分子的二阶商，
$\alpha,\beta,\gamma$ 是 O 的 residual 系数而非首相位。
(C.26) 没有用 $\mathcal L_W=\mathcal J_W$。

## 8. 真 mean 小根重建不会引入一个未付 mean 径向导数

为保持下一个背景仍在 (C.22)，用
$P+ p,K_\perp+k_\perp$ 的同一个 M 小根重新定义 mean。
因为 (C.25) 是准确切向式，新的 mean 与旧 mean 加校正 mean
之差是一个真正二阶 scalar $\Delta\kappa_2(t)$。
完整 implicit 小根的二阶差和 B 的小球给
$$
 |\Delta\kappa_2|
     \le2^{4096}(C_j^\#)^2\|h\|_{\mathscr Y_2}^2 ,
 \tag{C.27}
$$
其中 $\mathscr Y_s$ 表示 R 的实际四态增量 norm，
此处只在它已有限时使用。
真实高度再积分 $a_{\rm ph}w\,\Delta\kappa_2$，
保同一平端 gauge 与有限外端高度变化。

关键是先读非mean残差。$P,U,V$ 不因这个纯 mean 重建而变，
而
$$
 P_\perp \mathfrak r_{\rm retr}
 =P_\perp \mathfrak r_{\rm line}
  -P_\perp\{F(P+p,K+k+\Delta\kappa_2,U+p_\theta,V+k_\theta)
              -F(P+p,K+k,U+p_\theta,V+k_\theta)\}.
 \tag{C.28}
$$
$\partial_t\Delta\kappa_2$ 是真实 scalar，恰被这里的
$P_\perp$ 消去。它没有从完整 residual 中删除：
重建后的全 residual 准确是
$N_{\rm retr}=\Pi_{A_{0,\rm retr}}(P_\perp N_{\rm retr})$，
由 (C.22)--(C.23) 恢复其普通 mean。

在径向零态，$F_K=2Q$ 是角常数；
故 (C.28) 的非mean增量还至少含一个真实 nonmean 状态因子。
完整商法则给
$$
 \|P_\perp\Delta F\|_{H^s}
 \le2^{8192}(1+|Q|)C_j^\#
       (\mathscr B_{64}+\|h\|_{\mathscr Y_{64}})
                      |\Delta\kappa_2|,
 \qquad 0\le s\le64,
 \tag{C.29}
$$
在 tame 版本中将最高 $s$ 阶 norm 分配给实际高阶方向，
不以低阶 norm 控制任意高频。
(C.27)--(C.29) 与 O 的原 $c_j(1+Q)C_j^2$ 三段预算，
证明这个准确 mean 重建属于同一个窄 quadratic source 类型。
前三阶 scaled 径向版本逐式微分 (C.28)；
只需四态到三阶的 jets 和 mean 小根的前三阶差，
没有对已消去的 scalar 再取一次未付导数。

若后续还重选 $\Gamma_1^*(u)$，必须另外消费 P 的实际参数列和
O.17 的 $\psi N-\mathcal E_N[\widetilde h]$；
(C.26)--(C.29) 本身只是一条固定 metric 结论。
它不把第二 metric 参数的外部方向设为零，
也不代替最终 $\nu$、帽及强标签兼容。

本篇付清了两件此前未能由任意有限 $C^4$ 球推出的事实：
真实窄 residual 的 scaled 径向 jets 不增加根/strict 比较的负层幂；
相容普通校正和真 mean 重建可以精确保留 holonomy-one，
并继续给同一个实际 quadratic source 类型。
完整变化背景 inverse、最终 tame smoothing 序列及其收敛仍须续接。
