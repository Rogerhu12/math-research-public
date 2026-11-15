# R715 — 同一 cd 权的五维 Z 一阶来源与五十条整中性返回

日期：2026-11-15。**状态：已证明。**

本文在 R702/R713 的同一个六支中性 carry 家族内，再使用五条已经属于
该家族的十二次 C 测试。完整五十阶子式给出新的实际测试
$q_N^{(715)}$：两冻结来源、cd-Y 来源均为原 S，未缩放 cd-W 来源为
$6\delta T$，第二态整个 $2Y$ 来源为
$\omega^2S(2z)/2+S_{\rm new}(z)$，且 $\mathfrak j_2=1$；此外，
同一 cd 权的**整个第一 Z 条件来源**为零。

同一个整逆还给纯中性差 $\zeta_N^{(715)}$：所有既有正规来源为零，
$\mathfrak j_2=1$，第一 Z 条件来源也为零。
它仍保 R655 的原负一深支非零。因此新增的一阶混合来源确实可调，
不能把它当成原正规行必然遗漏的一条刚性非零约束。
本文只消去这一完整一阶来源，全部高阶混合行和实际外部补域仍保留。

## 1. 固定原来源与端点权

保 [R702](R702-forty-five-neutral-tests-and-complete-three-state-arithmetic-gate.md)
的全部原普通射线、周期、准周期、半特征、三态和实际参数：
$$
b=17,\quad \omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
$\Omega$ 为原单位周期。取
$$
Y=A+c+2d,\qquad W=A+3\delta c+4d,\qquad
b_Y=\frac{20+3\omega}{17},\qquad Z=W-b_YY.
\tag{2}
$$
$Z\perp Y$。原 $e_0=\mu_0$ 包含 $-1/84$，
$Y_*\mu_0=\nu_S$、$W_*\mu_0=6\delta\nu_T$；
$e_1,e_2$ 仍为 R702(4) 的完整 canonical W 四挠三态。

对原 carry 多项式 P，令 $\rho_{cd,N}(P)$ 是 R702(8)–(10) 的
完整 cd 端点来源。特别它包含以下两个 C 分支：
$$
\begin{aligned}
\Phi_P={}&P(H,E_\perp+uK,G_\perp+guK)\\
&-\eta\lambda P(H,\kappa E_\perp+uK,
 G_{00}+\kappa(G_\perp-G_{00})+guK),\\
g={}&3-2\omega,\qquad
H=D_*-\frac{E_{YW}}{29},\qquad K=H-\frac{406}{143}D_*,
\qquad \eta\in\{1,-1\}.
\end{aligned}
\tag{3}
$$
所有隐藏方向共同垂直于 Y、W。按每个齐次块保原 $b,\Omega$
归一，不能把 (3) 第二项删除。后文 $\rho_{cd,N}$ 总是这条完整来源；
它不是原未返回的 $1_{CD_N}q\mu_0$，也不是已将 Z 缩放的 T 观察。

沿 R713 的记号，原六个正规目标为
$$
(\mathscr U_0,\mathscr U_1,\mathscr B,\mathscr W,\mathscr Q,\mathfrak j_2).
$$
其中 $\mathscr B=Y_*\rho_{cd,N}$、$\mathscr W=W_*\rho_{cd,N}$，
$\mathscr Q$ 是相同完整权在 $e_1$ 上的整个第一 $2Y$ 来源。

## 2. 真正五维的一阶条件来源

定义
$$
\boxed{
\mathscr Z_1(P)(z)=\Omega^{-1}\int Z e^{Yz/\Omega}\,
                                     d\rho_{cd,N}(P).
}
\tag{4}
$$
这保任意后续完整 Y 测试。因为 $Z\perp Y$，在原正交 theta
张量格中对 Z 的一次导数不改变第一轴线丛。原总角型为零，
所以 (4) 属于整个 $\mathcal S_{34}$ 的角型5子空间。
完整基为
$$
\boxed{
\Psi_j(z)=-\sigma_b(z)^{34}x_b(z)^{13-3j}y_b(z),
\qquad j=0,1,2,3,4.
}
\tag{5}
$$
其首阶分别为 $5,11,17,23,29$，首系数均一。
一般 b 下使用 $b^j\Psi_j$ 作为归一坐标。
因此这五个阶次的 Taylor 系数经一个固定单位三角矩阵，
准确决定整个来源；其质量自动为零，质量本身不能替代五行。

一个不含协变导数歧义的实际生成法是
$$
\mathcal F_P(z,\epsilon)
=\int\exp((Y+\epsilon Z)z/\Omega)\,d\rho_{cd,N}(P),
\qquad\epsilon^2=0.
$$
则
$$
[\epsilon]\mathcal F_P(z,\epsilon)=z\mathscr Z_1(P)(z).
\tag{6}
$$
故只需读取 $\epsilon z^{6},\epsilon z^{12},\ldots,\epsilon z^{30}$。
逐个原 sigma 输入同时替换其 Y 系数为 Y 系数加
$\epsilon$ 倍 Z 系数；完整 C 因子、所有隐藏多项式和 (3) 两项原样保留。
这不是把 Y 的普通导数误认成 Z 条件矩。
例如未加权原来源的首项准确为
$$
[z^5]\mathscr Z_1(1)=6+3\delta-6b_Y=\frac{33+84\omega}{17},
\tag{7}
$$
与直接微分原六个 sigma 的六次首项相同。

## 3. 五十条实际中性列与完整兼容空间

沿 R702(13)–(15)，每条 C 列必须先把
$C^iF^jG^{d-i-j}$ 改成 $D,E_c,G$，再对整个多项式应用
$$
\widehat P=\sum_{a+e+g=d}
 \frac{[D^aE_c^eG^g]P}{1+\lambda\kappa^e}D^aE_c^eG^g,
\qquad C=(E_c-D)/14,\quad F=(E_c+13D)/14.
\tag{8}
$$
实际六支权中仍有 $C$-unit、$D_\zeta\in p^N$、
$E_{c,\zeta}$-unit 及 $D_\zeta/\kappa^N$。
完整 C 平均的 $m_{B_C}(i)=0$ 对 $1\le i\le5$，
准确给每条所选列的 $\pi_4$ 中性，其中
$\pi_4=(Y,W,W',G)$。这个来源级证明与 R702 相同，不以辅助矩阵核代替。

保 R702 的二十九条 G 列，原索引
$$
0,1,\ldots,22,\quad25,26,\quad36,37,\quad47,48.
\tag{9}
$$
十二次 C 列改用以下二十一条：
$$
\boxed{
\begin{array}{c|c}
i&j\quad(C^iF^jG^{12-i-j})\\ \hline
1&5,6,\ldots,11\\
2&5,6,\ldots,10\\
3&5,6,\ldots,9\\
4&5,6,7
\end{array}}
\tag{10}
$$
相对 R702 只增加 $(i,j)=(3,8),(3,9),(4,5),(4,6),(4,7)$。
最高原权仍为30；没有增加 B 方向、覆盖或新的核心假设。

R702 已证明，原53条正规坐标的完整特征零兼容空间维数为45：
半周期关系和整个四挠除子准确支付其八条缺行。
附上 (4) 的五坐标后，整个像维数至多50。
其中旧53行的全部几何约束仍适用，因 (10) 每一列仍共同隐藏于 Y、W。
新五行没有被先假定独立。

取旧53行中的 $0,\ldots,44$，再取 (6) 的五行作为新行
$53,\ldots,57$，共50行。完整程序的149列顺序仍是
55条 G、44条未选 B/G、50条 C12；本篇实际选列为
$$
\boxed{
\begin{gathered}
0,1,\ldots,22,\ 25,26,\ 36,37,\ 47,48,\\
104,105,106,107,108,109,110,\
116,117,118,119,120,121,\\
127,128,129,130,131,\quad137,138,139 .
\end{gathered}}
\tag{11}
$$
这些均为真实中性测试，不含额外目标列。

令 $\mathbb M_{715}(\lambda,\kappa,u,\eta)$ 为 (11) 的50列在上述50行的
完整实际矩阵。公开执行在 $\mathbf F_{1009}$、
$\omega=374,b=\Omega=1,\kappa=u=0,\lambda=(1-\tau)/\tau$ 给
$$
\boxed{
\begin{array}{c|rr}
 &\eta=1&\eta=-1\\ \hline
\tau=2&631&828\\
\tau=3&813&809
\end{array}}
\tag{12}
$$
为同一个子式的行列式。四个情形的完整58行均秩50；
仅有 R702 那八条旧关系，且它们的新五坐标为零。
对称正规目标以及纯中性 $\mathfrak j_2=1$ 目标加 $\mathscr Z_1=0$
都通过全部58行。

这里 (12) 只用来证明固定子式不恒零；缺八行的特征零兼容证明
是 R702 的完整几何。结合维数上界50，非零子式才证明：
**任意旧兼容目标与任意完整五维 $\mathscr Z_1$ 目标可同时实现。**

## 4. 实际参数曲线上的整逆与全部 N

(3)、(6)、(8) 和 R702 的45行生成法定义固定的
$K(\lambda,\kappa,u)$ 矩阵，$K=\mathbf Q(\omega)$。
清掉固定分母后的子式分子记 $d_\eta(L,K,U)$。
由 (12)，两个 $\eta$ 都满足
$$
d_\eta(L,0,0)\ne0.
\tag{13}
$$
所有分母为 R702 的旧固定有限组以及新固定子式。
新增五行最高只读第30阶，原整个计算仍只需最高总矩162；
保原 $p>163$ 门及固定有限坏素数即可。

将 $L=-1/T$ 代入，清固定幂和固定有限系数域的分母，
应用已付的
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。
在旧普通射线的相对密度一子族上，两个 (13) 及所有分母都为单位；
所删无限坏集计数仍是 $O(\sqrt X\log X)$，旧射线仍有无穷 p。
不添加新的模25、模81或改写任何旧射线。

对其中每个 p 和**所有** $N\in4\mathbf Z_{>0}$，
$\kappa,u=\kappa^N\in p\mathcal O$，故
$$
\boxed{
\mathbb M_{715}(\lambda,\kappa,\kappa^N,\eta)
       \in\operatorname{GL}_{50}(\mathcal O).
}
\tag{14}
$$
新系数是完整实际逆乘目标，不是辅助模1009解：
$$
a_{N,p}=\mathbb M_{715}(\lambda,\kappa,\kappa^N,\eta)^{-1}
          (\text{目标}-\text{基准权实际来源}).
\tag{15}
$$
子式赋值为零，没有额外深度损失。
所有新权仍整有界，固定 p、N 后不依观察深度 n。
N 改变时系数可能改变，因此不能免费套用固定权的 N 递推。

## 5. 两个新测试及全部已付算术返回

令 $q_N^{(715)}$ 为 (15) 的目标
$$
\boxed{
\begin{aligned}
&\mathscr U_0=\mathscr U_1=\mathscr B=S,\qquad
\mathscr W=6\delta T,\\
&\mathscr Q=\frac{\omega^2}{2}S(2z)+S_{\rm new}(z),\qquad
\mathfrak j_2=1,\qquad \mathscr Z_1=0.
\end{aligned}}
\tag{16}
$$
它是新的权，不将 R713 已固定的 $q_N^{\rm sym}$ 静默改名。
原 $\pi_4$ 全返回准确保持
$$
(\pi_4)_*(q_N^{(715)}e_i)=\beta^N(\pi_4)_*e_i,\qquad i=0,1,2.
\tag{17}
$$
令 $\mathcal E_N=\{E_{YW}\in p^N\}$。
R702 的完整三态 E 深来源表不变：
$$
\begin{aligned}
Y_*(1_{\mathcal E_N}q_N^{(715)}(e_0,e_1,e_2))
 &=\lambda^{2N}
  (\nu_S,\tfrac{\omega^2}{2}\nu_S+[1/2]_*\nu_{\rm new},
              \tfrac{\omega^2}{2}\nu_S-[1/2]_*\nu_{\rm new}),\\
W_*(1_{\mathcal E_N}q_N^{(715)}(e_0,e_1,e_2))
 &=\lambda^{2N}6\delta(\nu_T,\nu_T,-\nu_T).
\end{aligned}
\tag{18}
$$
双冻结现在均为 S，故 R713 的 $I/O/X$ 配对、同一个 $P_{30}$
以及两个实际域的差全部继续成立。
E 浅第二态的 $\Xi$、参考质量、A34 移动 E 门和所有 T 外部仍保。

另不减基准权，直接以50条纯列的目标取
$$
\boxed{
\zeta_N^{(715)}=\mathcal R_{715}(0,0,0,0,0,1;\mathscr Z_1=0).
}
\tag{19}
$$
这给所有旧正规来源零、全 $\pi_4$ 返回零，
E 深及 E 浅三态 Y/W 来源零，而 $\mathfrak j_2=1$。
同门归一词行无条件为零；不是给一个未知来源附加算术零。

## 6. 实际 T/S 混合行消去到二阶

对 (16) 的同一完整 cd 来源，置
$$
A_T(t;w)=\int 1_{b_YY+tZ\ {\rm unit}}
                  \langle b_YY+tZ\rangle^{d_pw}\,d\rho_{cd,N},
\qquad d_p=p-1 .
$$
只在 $t\in p\mathcal O$ 使用以下准确 unit 等价：
$b_YY+tZ$ unit 当且仅当 Y unit。于是
$$
\begin{aligned}
&\left.\partial_w\right|_0
 \{A_T(t;w)-\langle b_Y\rangle^{d_pw}J_S(w)\}\\
&\quad=d_p\sum_{k\ge1}
 \frac{(-1)^{k+1}t^k}{k b_Y^k}
 \int_{Y\ {\rm unit}}Z^kY^{-k}\,d\rho_{cd,N}.
\end{aligned}
\tag{20}
$$
两 Mellin 行的质量逐点相等；尺度 log 的处理没有假设局部质量零。
由整个 $\mathscr Z_1=0$，
$$
\int Zf(Y)\,d\rho_{cd,N}=0
\quad\text{对任意有界完整 }f,
$$
所以 (20) 的 k=1 项严格消失。特别
$$
\boxed{
(20)=
d_p\sum_{k\ge2}\frac{(-1)^{k+1}t^k}{k b_Y^k}
       \int_{Y\ {\rm unit}}Z^kY^{-k}\,d\rho_{cd,N}
\in p^{2N}\mathcal O\qquad(t=\kappa^N).
}
\tag{21}
$$
保 $1/k$ 的真实赋值后仍有 $kN-v_p(k)\ge2N$，故尾界完整。
同式用于 (19) 时把 $J_S$ 换成零。

(21) 只关于这里的完整 cd 来源。
若再附 R713(12) 的双 Y 域差、其他移动伙伴门或某个角域，
其 k=1 条件行不自动为零。不能用忘掉那些条件后的来源零删补域。

另一方面，(16)、(19) 都准确保
$$
J_2=\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N},
\qquad\ell_0=-3\omega/5.
$$
其余可能项 $J_8,J_{14},J_{20},J_{26}$ 完整保留；
新十二次列不继承旧六次网格的零质量。
同 R702/R713 的原 Q-unit/L-deep 级数与 R655 真实负一非零给
$$
\boxed{
v_p(\Delta_{N,n})=3n-2N+v_p(I_{\Sigma_5,-1}),
\qquad n>N,\quad 2n>v_p(I_{\Sigma_5,-1}).
}
\tag{22}
$$
因此即使追加整个 (4) 为零，仍不能仅从这些正规行推出该 native
深支为零。剩余信息在高阶混合来源及各自的完整补偿内。

## 7. 公开执行与可复算范围

唯一新增执行：

- script：`scripts/check-r715-native-z-first-moment.js`；
- args：`--max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12`；
- source commit：`25fdaddb02cdaf2a247264c87c7f8ad5add44eb6`；
- public run：`43691642194`；job：`132743359410`；
- script SHA256：`1f62063eb999b984be4c702fc598ef8e621f1e9af63af19c22a6da26e7d53325`；
- stdout：32286 bytes；SHA256：
  `a366b3a2ae25d76c6783cd4402bad4a569fd4d4e2520f80e07949bc6df5c6bb6`。

脚本从 R594 的算法及全部原 sigma 递推重建，不以数值输出表为输入。
完整 C 的0至30阶、原四挠相位、两个 C 分支、整个 E 单位逆、
旧53行和新五行均在同次执行内保存并验证。
按根规则不提交可重算输出。

本篇新增的是50条实际整返回、(16)/(19) 的同源全一阶消去和
(21) 的真实混合尾界。下一有限计算可同时读取
$Z^1,\ldots,Z^5$ 的全部条件来源；这只是有限混合矩壳，
不能据其角型维数把 $Z^6,Z^7,\ldots$ 或完整 joint 来源认作已知。
主目标尚未完成。
