# 工作检查点：共轭最小修补、头范围盲点及完整 S0 幂界

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI 辅助：GPT-6 Astra Pro。根核完整窗口变分、源头范围、全角正交及一致幂界。
状态：本稿保存已核恒等式和未闭接口；不是实际 Schur 能量估计，不登记为无权进展。

此前完整结果为
[R239 高出生块混合](../results/R239-appendix-true-high-birth-block-failure-to-preserve-outer-bridge-kernel.md)；
当前继续 [R271 低旗加权源](../results/R271-appendix-low-flag-full-head-commutators-and-weighted-source.md)
和 [头角消元](../results/R271-appendix-actual-middle-source-corner-elimination-and-positive-gram.md)。

## 0. 前置守卫：Haar 热像不能未经运输移到负整数边界

本稿 §§1--5 的 $M=\ker T_N$ 或 $\ker T_Y$ 位于实际负整数边界
$\mathcal H_-$。其基是物理 $e_n$；按 $n$ 的二进位支撑写成
$e_F$，原 R239 孔数准确为 $\mathcal N_{\rm phys}e_F=|F|e_F$。
具体表示见
[R239 首位图 §1](../results/R239-appendix-first-bit-small-graph-and-strong-cross-coupling.md)
所用的 $Be_n=\alpha_{v_2(n)}e_{n-1}$。

新 [R150 热值域](../results/R150-appendix-exact-weighted-occupation-ranges-of-positive-semigroups.md)
及 [不变旗热像](../results/R150-appendix-exact-heat-ranges-on-invariant-flags-and-closed-graphs.md)
则位于 Haar $H=L^2(\mathbb Z_2)$ 的 Walsh 表示，权由 $\chi_F$ 定义。
这些热定理在它们自己的未知闭 $A$ 不变空间内给准确稠密核心；
本稿没有给出将该空间、算子、不变旗及加权域同时运输到上述
$\mathcal H_-$ 边界的有界识别。

因此，仅凭两边都用有限子集 $F$ 标号，不能把 Haar 热核心稠密直接用于
R239 的边界 $M$，也不能把 Walsh 次数称为原物理孔数。
下文 §6 是直接在物理 $e_F$ 上构造的环境反例；
它不是已定义的 Haar 实际热像，更没有声称该向量属于边界 $M$ 或 $M\ominus N$。

“若同一表示的 $M$ 内有稠密核心 $\mathscr E$，且 $\mathscr E\subset N$，
则 $M=N$”当然成立，但这里的“同一表示”与核心包含均须独立支付。

## 1. 固定完整窗口上的共轭变分

设 $X$ 是固定有限孔窗口，$L=A_m+D_m$，$r$ 是一个可行边界源，
$c$ 是 $Lc=r$ 的最小范数解。写
$$
Z=\ker(L|_X),\quad P=P_Z,\quad Q=I-P,\quad Pc=0.
$$
此处约束为完整 $L$ 输出；不把内部输出核和零源核混同。

令 $W=W_2$ 在各层上作用，$0\le W\le S_mI$。因为它保孔窗口，
$$
L(t)=e^{-tW}Le^{tW},\qquad r(t)=e^{-tW}r
$$
的全部可行解为 $e^{-tW}(c+Z)$，零源空间为 $Z(t)=e^{-tW}Z$。
若 $P(t)$ 为其正交投影，则
$$
P'(0)=-QWP-PWQ.
$$
这是有界可逆像的标准局部图计算：$Z(t)$ 在 $Z\oplus Z^\perp$ 中的图算子一阶为 $-tQWP$。

相应最小解
$$
c(t)=(I-P(t))e^{-tW}c
$$
严格满足
$$
c'(0)=(2P-I)Wc,\qquad \|c'(0)\|\le S_m\|c\|.
$$
故
$$
\left.\frac d{dt}\|c(t)\|^2\right|_0=-2\langle Wc,c\rangle,
$$
$$
\left.\frac {d^2}{dt^2}\|c(t)\|^2\right|_0
=4\|QWc\|^2-4\|PWc\|^2.
$$
第二式也可对 $e^{-2tW}$ 的精确 Schur 补求导得到。

由于 $[L,W]=C=D_3$，
$$
Lc'(0)=-Wr-Cc,\qquad
L(Wc)=Wr+Cc.
$$
因此对这个已经表示为已知像的组合，
$$
R_{\min}^{\,L}(Wr+Cc)=QWc,\qquad
\|R_{\min}^{\,L}(Wr+Cc)\|\le S_m\|c\|.
$$
这里的 Moore--Penrose 逆只在所示实际像上使用，不声称全窗口输出满射。

这些式子必须在完整窗口使用。若冻结原联合旗，
$WE_h\subset E_{h+1}$ 会移动其尾旗，不能把上述最小原像自动当作原同旗的原像。

更一般，保窗口的有界生成元 $B$ 给已知源
$$
L(Bc)=Br+[L,B]c,\qquad
R_{\min}^{\,L}(Br+[L,B]c)=Q Bc.
$$
例如 $B=A_m^*$ 引入 $[A_m,A_m^*]c$。
没有证明这个新组合等于实际两出生桥有效源。

## 2. W-only 变分确实看不到原头通量

原宽 $d$ 的最优链每段满足
$$
c_t\in\bigoplus_{i\le d-t}e_iE_{d-i,q+t}.
$$
真正低核头通量的伴随源满足
$$
h_t\in\bigoplus_{i\ge d-t+1}e_iE_{d-i,q+t}.
$$
$W_2$ 只作用纯尾，保持每个头坐标。因此对所有整数 $k\ge0$，
$$
\langle h_t,W_2^k c_t\rangle=0.
$$
上述共轭只改变尾算子，有限头仍是 $A_m$。
同样的末端三角性使每个 $c(t)$ 仍有头范围 $i\le d-t$；
其所有存在的 $t$ 导数也保持这个范围。
所以不能直接把 $c'(0)$、能量二阶变分或其 W-only 高阶推广认作
$h(z)$ 或 $\widetilde C_{\rm tot}(h(z))$ 的已付预算。

这仅排除这种直接识别，不否定变分与另一个完整头恒等式结合的可能性。

## 3. 把单个头角扩大成全部 ker S0，并未支付实际中间源

用 R271 中出生层恰为1的链空间 $\mathscr X_1$ 和输出空间
$\mathscr Y_1$，令
$$
T_0=S^{(0)*}|_{\mathscr Y_1},\qquad
K_1=\ker(S^{(0)}|_{\mathscr X_1})=(\operatorname{Ran}T_0)^\perp.
$$
固定层上 $\operatorname{Ran}T_0$ 闭可由有限头三角右逆得到；
以下正交补恒等式本身不需要先用其闭性。

完整最优链 $c=b-S^*z$ 的出生1部分为
$$
c_1=-T_0z_1-S^{(1)*}z_2.
$$
故
$$
P_{K_1}S^{(1)*}z_2=-P_{K_1}c_1,\qquad
\|P_{K_1}S^{(1)*}z_2\|\le\lambda.
$$
这确实是一个无额外逆成本的全角投影恒等式。

但真正有效源为
$$
\sigma=S^{(1)}u_1,\qquad
u_1=T_0x,\qquad x=Q_1^{-1}\zeta.
$$
所以 $u_1\perp K_1$。上述由 $\lambda$ 支付的恰是另一正交部分；
不能据此给实际 $\sigma$ 的 $\mathcal H_2^{-1}$ 能量上界。
原具体角中的 $c_\Delta$ 约束仍然有用，其余长头跳跃不能因改成这个更大投影而删去。

## 4. 完整 S0 的一致拟幂零性

这一节只给后续求和工具，不给零参数逆。

两个实际 $T_N,T_Y$ 已知为范数拟幂零。
将 $A_m$ 张量尾恒等后，
$$
\|A_m-T\|\longrightarrow0,
$$
由实际尾范数 $O(1/m)$ 与已付 carry 误差可得。
每个 $A_m$ 又为有限幂零头。因此，对任意固定 $\rho>0$，
存在只依赖 $\rho$ 和原模型、与 $m,n$ 无关的 $C_\rho$，使
$$
\|A_m^n\|\le C_\rho\rho^n.
$$
证明：先取 $N$ 使 $\|T^N\|<\rho^N/2$，范数收敛控制所有足够大的 $m$；
按 $n=kN+r$ 使用次乘性。剩余有限多个 $m$ 各自幂零，
只需把有限多个非零幂并入常数。

在实际低旗以及完整链上，
$$
\mathbf S_0=A_m+D^{(0)}\text{（降一段）}.
$$
两项交换，第二项范数至多 $\|D_m\|\le1/m$。
大 $m$ 用上式的 $\rho/2$ 界及二项式展开；
有限多个小 $m$ 则用每次作用严格降低 $i+t$，得到与 $q$ 无关的有限幂零阶。
因此
$$
\boxed{
\forall\rho>0\ \exists C'_\rho<\infty:
\quad
\sup_{m,q}\|\mathbf S_0(m,q)^n\|
\le C'_\rho\rho^n.
}
$$
特别，对每个固定非负整数 $r$，
$$
\sup_{m,q}\sum_{n\ge0}(n+1)^r\|\mathbf S_0(m,q)^n\|<\infty.
$$
所有保留的旗都由各次作用保持；这里没有在出旗后又任意投回。

它可以给固定非零谱参数处的完整头预解及换序级数一个统一上界。
但是谱参数 $0$ 仍不能除：即使矩阵族一致拟幂零，其非零链权也可趋于零。
这一步没有把 $Q_1^{-1}$、$\mathcal H_2^{-1}$、$x$ 或 $z_2$ 的成本删去。

## 5. 当前未闭接口

仍需在准确合同度量中支付
$$
\Phi\sigma=S_{0,2}^*\mathbf J^*x-\mathcal B_2x,\qquad
x=Q_1^{-1}\zeta,\qquad
\widetilde{\mathcal H}_2=\Phi\mathcal H_2\Phi.
$$
第一项是伴随像，不能换成正确右像上的既有收缩；
第二项虽只在第2段 primitive 列，也仍带真实 $x$。
以上三种已核工具均未给出
$\mathcal E_2/\lambda^2$ 或原 $\widetilde C_{\rm tot}$ 的无权上界。


## 6. 物理全 ℓ² 占据权仍不控制原孔数：一条共同向量

这一节固定实际物理基 $e_F$，不使用 Haar 热算子。
对任意非负 $a\in\ell^2(\mathbb N)$，定义物理占据算子
$$
\mathcal N_a^{\rm phys}e_F=\Bigl(\sum_{j\in F}a_j\Bigr)e_F.
$$
下面构造同一个 $f\in\mathcal H_-$，同时属于每个这样的 $a$、
每个 $\sigma>0$ 的
$\operatorname{Dom}e^{\sigma\mathcal N_a^{\rm phys}}$，
但不属于任何正系数的原 R239 $\log^{4/3}$ 孔权域。

取两两不交的有限物理位块 $I_n$，$|I_n|=n^2$，例如按物理次序连续分块。
置
$$
u_n=\binom{n^2}{n}^{-1/2}
\sum_{\substack{F\subset I_n\\ |F|=n}}e_F,
\qquad
f=\sum_{n\ge1}\frac1n\,u_n.
\tag{6.1}
$$
$u_n$ 是正交单位向量，原物理孔数恰为 $n$。
故 $f$ 为非零 Hilbert 向量。

固定任意 $a\ge0$、$a\in\ell^2$ 和任意 $\sigma>0$。
写 $A=\|a\|_2$、$t=2\sigma$、
$C_{t,A}=\tfrac12t^2e^{tA}$。因 $0\le a_j\le A$，
$$
e^{t a_j}\le1+t a_j+C_{t,A}a_j^2.
$$
对任意正数 $v_1,\ldots,v_N$，有限对称平均满足
$$
\binom Nq^{-1}\sum_{|F|=q}\prod_{j\in F}v_j
\le\left(\frac1N\sum_jv_j\right)^q.
\tag{6.2}
$$
可直接证明：固定总和，把任意两数替成它们的平均，
$q$ 次初等对称多项式的改变为非负的
$q-2$ 次剩余对称多项式乘以这两个数乘积的增加量。
在固定总和的紧单纯形上取最大值，得到等值点的上界；
$q=1$ 是恒等式。故这里不需要随机独立性。

在 $N=n^2,q=n$ 上用 (6.2) 与 Cauchy--Schwarz，
$$
\begin{aligned}
\|e^{\sigma\mathcal N_a^{\rm phys}}u_n\|^2
&=\binom{n^2}{n}^{-1}
\sum_{\substack{F\subset I_n\\|F|=n}}
e^{t\sum_{j\in F}a_j}\\
&\le
\left(1+\frac{tA}{n}
+\frac{C_{t,A}A^2}{n^2}\right)^n\\
&\le \exp(tA+C_{t,A}A^2).
\end{aligned}
\tag{6.3}
$$
最后一个常数与 $n$ 无关，允许依赖这个任意给定的 $a,\sigma$。
权算子对角，不同 $u_n$ 的支撑仍正交。因此
$$
\boxed{
\|e^{\sigma\mathcal N_a^{\rm phys}}f\|^2
\le e^{tA+C_{t,A}A^2}\sum_{n\ge1}n^{-2}<\infty.
}
\tag{6.4}
$$
构造 $f$ 没有依赖 $a$ 或 $\sigma$；
所以 (6.4) 确实同时覆盖所有非负 $\ell^2$ 行及其所有正倍数，
不只是一个预先选定的可数族。

另一方面，对每个 $c>0$，
$$
\left\|
e^{c\log^{4/3}(2+\mathcal N_{\rm phys})}f
\right\|^2
=\sum_{n\ge1}\frac{\exp(2c\log^{4/3}(n+2))}{n^2}
=\infty.
\tag{6.5}
$$
因为其通项的对数
$2c\log^{4/3}(n+2)-2\log n$ 趋于正无穷。
这是原物理孔数的准确失败，不是把另一基中的次数代入。

更一般，把 (6.1) 的 $1/n$ 换成任意 $\ell^2$ 系数 $\varepsilon_n$，
(6.3) 仍保证所有物理占据权；
而原孔层质量准确为 $|\varepsilon_n|^2$。
所以这种共同占据域允许任意给定的可和孔层质量分布，
没有一个可从域的集合关系单独推出的普通孔尾速率。

同一个有限集合构造可在 Haar Walsh 正交基上独立重复，
得到对应的 Walsh 次数结论；那是另一个明确指定表示的命题。
它不构成两种实际模型之间的运输。

本节没有将 $f$ 放进真实边界核或真缺陷空间。
若要借占据权继续边界问题，仍须直接使用原 $D_m$ 权与真实源结构，
证明这类弥散高孔部分的修补成本，或另行支付两种表示之间的完整接口。

## 7. 残量的最低头分量在完整最小修补范数中精确分离

本节沿用
[实际末块返回源笔记](2026-11-13-actual-last-block-return-source-and-complete-low-chain-projection-1cf.md)
的同一原宽 $d$ 窗口、联合旗和最小范数；不扩大窗口。
固定 $m,q$，记纯尾 $q$ 孔层为 $\mathcal H_q$，
$E_{h,p}=\ker D^h\cap\mathcal H_p$，$E_{0,p}=0$。
允许残量为
$$
\mathscr R_q=\bigoplus_{i=0}^{d-2}e_iE_{d-i-1,q}.
$$
链空间的第 $t$ 段为
$$
\mathscr C_t=\bigoplus_{i=0}^{d-t}e_iE_{d-i,q+t}.
$$
完整约束是 $D c_1=r$、$A c_t+D c_{t+1}=0$；
把内部约束写成 $Sc=0$，边界约束写成 $Fc=r$。
其唯一最小范数解记 $c_{\min}(r)$，范数为 $\lambda_q(r)$。

固定层 $D:\mathcal H_{q+1}\to\mathcal H_q$ 有有界右逆，故满射且有
Moore--Penrose 逆 $D^\dagger$。这里仅使用固定 $q$ 的存在性，
不声称 $\|D^\dagger\|$ 对 $q$ 一致。
对任意
$$
r_0=e_0h,\qquad h\in E_{d-1,q},
$$
令
$$
c^0_1=e_0D^\dagger h,\qquad c^0_t=0\quad(t\ge2).
\tag{7.1}
$$
由 $DD^\dagger h=h$，
$$
D^dD^\dagger h=D^{d-1}h=0.
$$
所以 (7.1) 确在原联合旗内；$Ae_0=0$ 又给 $Sc^0=0$、$Fc^0=r_0$。

若 $r_+\in\mathscr R_q$ 的 $e_0$ 分量为零，任意满足完整约束
$Fc^+=r_+$、$Sc^+=0$ 的链都满足
$$
D(c^+_1)_0=0.
$$
而 $D^\dagger h\perp\ker D$，所以 $\langle c^0,c^+\rangle=0$。
特别，把任意源 $r=r_0+r_+$ 的可行链减去 $c^0$，
恰得到源 $r_+$ 的可行链，并有准确平方范数相加。
因此
$$
\boxed{
c_{\min}(r)=c^0+c_{\min}(r_+),\qquad
\lambda_q(r)^2=\|D^\dagger h\|^2+\lambda_q(r_+)^2.
}
\tag{7.2}
$$
这也证明 (7.1) 本身是 $r_0$ 的完整最小解。
按极化，$\mathcal G_{\rm flag}^{-1}$ 对
$e_0E_{d-1,q}\oplus(e_0E_{d-1,q})^\perp$ 精确分块。
这不声称 $r_+$ 的最小链没有 $e_0$ 坐标；
它的第1段 $e_0$ 坐标可以在 $\ker D$ 内。

进一步，$D^\dagger h\perp E_{1,q+1}$，
故 (7.1) 只有出生层 $\le q$ 的成分。
用返回源笔记的
$$
Z=\ker S_L,\qquad B=P_{\mathscr Y_H}S|_Z,\qquad
K=B^*(S_HS_H^*)^{-1}B,
$$
它的低链满足 $Bc^0=0$，从而 $Kc^0=0$。
所以真实末块能量 $\mathcal E_2$ 及返回源
$$
r_{\rm ret}=FK(c_{\min}(r))_L
$$
只依赖 $r_+$，纯 $r_0$ 时二者均为零。

返回源的输出也没有 $e_0$ 分量。准确理由是返回源笔记 (3.4) 给
$$
FB^*z
=F R_0B_0^{-1}V_1^*Q_1^{-1}V_2^*z,\qquad
F R_0y=D\,P_{\mathscr C_1}A^*y_1.
\tag{7.3}
$$
原 $A^*$ 严格升头，$P_{\mathscr C_1}$ 按头坐标分块，$D$ 仅作用尾。
故 (7.3) 对任意 $z\in\mathscr Y_H$ 的 $e_0$ 输出均为零；
取真实 $z=z_2$ 即得所述结论。
这里保留了全部 $B_0^{-1}$、$Q_1^{-1}$ 和联合旗投影，
没有将原范数半收缩升级成最小修补收缩。

下一头分量 $e_1h$ 满足 $Ae_1=a_1e_0\ne0$；
(7.1) 已不满足内部方程。
因此不能不付耦合便把 (7.2) 逐头重复。

## 8. 下一头 e1 的正交剥离已经失败：一个原 D3 像源

这一节回答 §7 的递归问题，仍在同一原窗口和联合旗内。
固定原 $m\ge5$、$d=2^m$ 与任意允许的 $q$；下面证明只需 $d\ge4$。
构造的源是一个环境合法源，甚至可来自合法低输出向量，
但没有把它识别为真实 $w\in M\ominus N$ 的投影残量。

### 8.1 两个原有限头的前三列

直接从 $N_0=E_0+\eta_0E_0^*N_1$ 及 $Y_j=N_j/(1+N_j)$，
在 $e_0,e_1,e_2$ 上有
$$
Ae_0=0,\qquad Ae_1=e_0,\qquad
Ae_2=\eta_0e_1+\beta e_0,
\tag{8.1}
$$
其中
$$
\beta=\frac14\quad(T_N),\qquad
\beta=\frac14-\eta_0\quad(T_Y).
$$
具体地，$N_0e_2=\eta_0e_1$、$N_0^2e_2=\eta_0e_0$、
$N_1e_2=e_0$，其余相关高幂为零。
原 $0<\eta_0<1/4$，故两型均有 $\beta\ne0$。
这里使用原头，未换成 Jordan 相似头。

### 8.2 一个正 Schur 补给出的非零混合

以下 $D$ 在相邻孔层间的限制按位置理解。令
$$
\mathcal K=\ker(D:\mathcal H_{q+1}\to\mathcal H_q),\qquad
\mathfrak F=DD^*|_{\mathcal H_{q+1}}.
$$
固定层 $D:\mathcal H_{q+2}\to\mathcal H_{q+1}$ 满射，
所以 $\mathfrak F$ 正且有有界逆；常数允许依赖 $m,q$。
对 $k\in\mathcal K$，用
$[D,D^*]=S_mI-2W_2$ 和 $[D,W_2]=D_3$ 得
$$
D\mathfrak Fk=-2D_3k,\qquad
D^2\mathfrak Fk=0.
\tag{8.2}
$$
因而在 $\mathcal K\oplus\mathcal K^\perp$ 上写
$$
\mathfrak F=
\begin{pmatrix}
F_{00}&\mathfrak B^*\\
\mathfrak B&F_{11}
\end{pmatrix},
\qquad
\mathfrak B=P_{\mathcal K^\perp}\mathfrak F|_{\mathcal K},
$$
有
$\operatorname{Ran}\mathfrak B\subset
U_{2,q+1}=E_{2,q+1}\ominus E_{1,q+1}$。
令
$$
\mathfrak S=F_{00}-\mathfrak B^*F_{11}^{-1}\mathfrak B.
$$
正可逆性给 $\mathfrak S>0$ 且有有界逆。
对任意满足 $\mathfrak Bk\ne0$ 的 $k\in\mathcal K$，
$$
P_{\mathcal K}\mathfrak F^{-1}\mathfrak Bk
=-\mathfrak S^{-1}\mathfrak B^*F_{11}^{-1}\mathfrak Bk
\ne0.
\tag{8.3}
$$
最后的不等式因为
$$
\langle\mathfrak B^*F_{11}^{-1}\mathfrak Bk,k\rangle
=\|F_{11}^{-1/2}\mathfrak Bk\|^2>0.
$$

这样的 $k$ 可直接在原权下有限支撑构造。
取 $q+1$ 对两两不交的尾位 $(i_\nu,j_\nu)$，置
$$
k=\bigotimes_{\nu=1}^{q+1}
\bigl(a_{j_\nu}e_{\{i_\nu\}}-a_{i_\nu}e_{\{j_\nu\}}\bigr),
\qquad a_j=(j+1)^{-2},
\tag{8.4}
$$
其余尾位取真空。每对被 $D$ 杀死，故 $Dk=0$。
$D_3$ 作用在第 $\nu$ 对产生非零系数
$a_{i_\nu}a_{j_\nu}(a_{i_\nu}^2-a_{j_\nu}^2)$；
各项在“哪一对是真空”的正交支撑上，所以 $D_3k\ne0$。
由 (8.2)，此时 $\mathfrak Bk\ne0$。

固定这样的 $k$，定义
$$
h=-2D_3k,\qquad x=\mathfrak Bk.
\tag{8.5}
$$
则 $h\ne0$、$Dh=0$、$Dx=h$、$x\perp\ker D$，所以
$$
x=D^\dagger h,\qquad
P_{\mathcal K}\mathfrak F^{-1}x\ne0.
\tag{8.6}
$$
因此 $r=e_1h$ 在原残量旗内，并且确属原 $D_3$ 的已知像。

### 8.3 限制在头 0、1 的最小链不能是完整最小链

若只允许头 $e_0,e_1$，由 (8.1)，链约束按
$(c_t^{\,1},c_{t+1}^{\,0})$ 分成互不相交的坐标对。
除了第1对以外，各对都是零源；另有独立的 $c_1^{\,0}\in\ker D$。
最小范数使这些零源坐标全为零。
所以受限最小链必有形状
$$
c_1=e_1x',\qquad c_2=e_0y,\qquad c_t=0\ (t\ge3),
\qquad
Dx'=h,\quad Dy=-x'.
\tag{8.7}
$$
由 $Dh=0$ 自动有 $x'\in E_{2,q+1}$、$y\in E_{3,q+2}$，
故它在原联合旗内；没有扩大允许的旗。

假设 (8.7) 也是完整链空间的最小解。
对仅在第2段、头 $e_0$ 取任意 $\ker D\cap\mathcal H_{q+2}$
的零源链正交，得到 $y\perp\ker D$。
因固定层 $D$ 满射，存在唯一 $\ell\in\mathcal H_{q+1}$ 使
$$
y=D^*\ell,\qquad \mathfrak F\ell=-x'.
\tag{8.8}
$$

对任意 $k_0\in\mathcal K$，取固定层 Moore--Penrose 原像
$$
R_1k_0=D_{q+2}^\dagger k_0,\qquad
R_2k_0=D_{q+3}^\dagger R_1k_0.
$$
于是 $DR_1k_0=k_0$、$DR_2k_0=R_1k_0$，
且 $R_1k_0\in E_{2,q+2}$、$R_2k_0\in E_{3,q+3}$。
下面两条链都是完整零源链：
$$
z^{[1]}=(e_1k_0,\,-Ae_1R_1k_0,\,0,\ldots),
$$
$$
z^{[2]}=(e_2k_0,\,-Ae_2R_1k_0,\,A^2e_2R_2k_0,\,0,\ldots).
\tag{8.9}
$$
边界源为零，内部相邻两项准确抵消，末端用 $A^3e_2=0$。
各段的头上界为 $2,1,0$，尾核阶至多为 $1,2,3$，
所以 $d\ge4$ 时全部属于原 $\mathscr C_t$。

将 (8.7) 分别与 (8.9) 配对，再用 (8.8)，得到
$$
\langle x'-\ell,k_0\rangle=0,\qquad
-\beta\langle\ell,k_0\rangle=0
\quad(k_0\in\mathcal K).
\tag{8.10}
$$
第二式因 $\beta\ne0$ 迫 $\ell\perp\mathcal K$，
第一式遂迫 $x'\perp\mathcal K$。
故由 $Dx'=h$ 与 (8.6)，
$$
x'=x,\qquad \ell=-\mathfrak F^{-1}x.
$$
这与 (8.6) 矛盾。

所以，源 (8.5) 的全局最小链必须使用头 $e_j$、$j\ge2$；
允许这些头后，最小平方范数严格小于只允许头 $0,1$ 的最小值。
严格性也由闭仿射约束集的唯一正交投影立即得出。
这证明 §7 的最低头精确分块不能从 $e_1$ 开始原样递归。

### 8.4 准确范围

该源不仅满足残量旗。令低输出向量只在第 $q$ 层非零，取
$$
v_q=\eta_0^{-1}(e_2-\beta e_1)h.
$$
则 $Dv_q=0$ 且由 (8.1) 有 $Av_q=e_1h=r$，
所以它属于同一个原低输出空间
$$
V_{m,q}
=\mathcal H_{\le q}^{(m)}
\cap\ker(P_{\le q-1}L_m).
$$
这个定义见[全整数窗口原稿 §4](2026-11-13-direct-linear-large-windows-and-all-q-minimal-energy-boundary-next.md)
式 (4.3) 前的 $\mathcal W^{\rm lin}_{m,q}$：
$v$ 仅位于尾 $q$ 层，$L_mv=e_1h$ 也仅位于尾 $q$ 层，
所以 $P_{\le q-1}L_mv=0$。
头至多为2且 $h\in\ker D$，也保留上述全部联合旗。
可按需整体归一化。

这个例子同时有便宜的已知源修补，不能被读成大能量下界。
由 $D^2D^*k=-2D_3k=h$，直接取
$$
\widehat c_1=e_1DD^*k,\qquad
\widehat c_2=-e_0D^*k,\qquad
\widehat c_t=0\quad(t\ge3).
$$
它满足 $D\widehat c_1=e_1h$、$S\widehat c=0$；
尾核阶分别至多为2、3，仍保原联合旗，并有
$$
\lambda_q(e_1h)^2
\le\|\widehat c\|^2
\le(\|D\|^4+\|D\|^2)\|k\|^2
\le(m^{-4}+m^{-2})\|k\|^2.
$$
此上界对 $q$ 一致。§8.3 证明的是继续允许高头会严格改善最小值，
没有否定这个已经支付的两头试探上界。

这并没有证明上述 $v$ 是某个真实 $w\in M\ominus N$ 的正交投影，
也没有给真实 $\mathcal E_2$ 的坏增长或某个下界。
它只准确排除“源属联合旗、甚至属已知 $D_3$ 像，
就可把 §7 的正交剥离逐头重复”这一捷径。
真实返回源的同窗最小修补预算仍须使用额外的 $M$ 结构。
