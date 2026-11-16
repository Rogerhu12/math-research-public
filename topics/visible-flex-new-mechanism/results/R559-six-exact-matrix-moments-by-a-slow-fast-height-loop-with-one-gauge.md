# R559：同一规范的缓变快高度回路与六个矩的准确联合零

日期：2026-11-16。**完整原式纸证；没有执行数值、符号、profile、求积、秩或开发检查。**

本文在 R557 的实际端点族中释放快高度形状的长度参数。
同一 R556 完整 core 的 $S_0^y$ 在更细尺度上有严格正净首项；
最早快准备的负速度平方费用在该尺度上也真实计入。
一条拉长的快高度回路保留正 $R_1^y$ 收益，
同时把负 $S_0^y$ 成本降至与这个正余量同阶。
在同一个原端图上联调，得到
$$
\boxed{P_0=P_1=P_2=T_1=R_1^y=S_0^y=0.}
\tag{1}
$$

这里仍是同一 R521 母库、原右锚和一次选定的 $\chi$。
真实 $A/T$ 从原零 history 起点累计，完整 ruling 全相位为0。
本稿不保留 R557 固定长度形状的交叉零：
新的 $S_1^y/R_0^y$ 费用有明确非零首项，均留在实际全词。
剩余这两个独立矩、frame／位置与完整 periods 仍未闭合。

## 1. 同一原端点族与新的尺度

保持 R556/R557 的原记号
$$
y=x+\omega_c,\quad \eta=\omega-\omega_c,\quad
d=h\eta-k,\quad u=d/h,\quad j=\eta/h+d/h^2,
$$
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\quad
R=L_h/\sqrt\lambda,\quad M=(1+\log R)^6,\quad
\delta=\lambda^2\zeta.
\tag{2}
$$
原第二规范仍为0。新控制参数不进入 $\nu$。
先固定充分大的有限 $R$，最后在共同有限参数盒上一次选小正 $\zeta$；
在每条实际词内部没有换规范。

令 $\theta=(\ell_1,\ell_2,\xi)$ 为 R556 的原三参数，
$\mathfrak b>0$ 固定，$Z_*>0$ 为原饱和坐标。
记
$$
A_Y=-Q_2/(8c)>0.
$$
原三个端图和中心 $R_1^y$ 满足
$$
\begin{aligned}
F_1^\infty(\theta)
&=-\frac{D_*}{2c}
 \left\{\frac{Z_*^2}{16}(\ell_1+\ell_2/4)
                    -\frac{\mathfrak bZ_*^3}{24}\right\},\\
F_0^\infty(\theta)
&=Z_*-\frac{g_0(\ell_1+\ell_2/4)}{6c\xi},\\
F_t^\infty(\theta)
&=\frac{\mathfrak bZ_*}{4}-\frac{\ell_1+\ell_2}{8},\\
\delta R^{3/2}R_1^y\big|_{\rm core}
&=-\frac{\ell_1+\ell_2}{8\xi}+o^1(1).
\end{aligned}
\tag{3}
$$
前三项分别是原
$\delta R^{5/2}P_1/M$、$\delta R^{5/2}P_0$、
$\delta R^{3/2}T_1/M$ 的完整 $C^1$ 极限。
共同零为
$$
\theta_*=
\left(\frac{2\mathfrak bZ_*}{9},
      \frac{16\mathfrak bZ_*}{9},
      \frac{g_0\mathfrak b}{9c}\right),
\tag{4}
$$
三维 Jacobian 可逆。

“core”始终包括 R544 真零历史快入、R550 饱和、
两次低尾、两段高尾以及全部真实过渡。
它不是删去原准备成本后的几段静态密度之和。
暂留原最后高尾停止值
$z=\sqrt R\,\delta\,\mathsf m_{p_2}=v$，
以便最后准确支付新增段的 $P_2$。

## 2. 完整 core 的正 $S_0^y$ 首项

R555 的原点态恒等式为
$$
4s_0=-2\eta p_0-\eta^2-(d_s/h)^2.
\tag{5}
$$
以下先计算全部静态项，再单独计原负速度平方。

### 2.1 两个低尾

两个低尾的当前 $Y$ 坐标分别为
$z_1=Z_*$、$z_2=Z_*/2$，真高度为 $\sqrt{M\xi}$。
R556 的完整当前 Gram 与水平式给
$$
u=-A_Yz_i^2/R+o^1(R^{-1}),\qquad
\eta=u+O((MR)^{-1})+o^1(R^{-1}),
$$
$$
p_2=O(R^{-1}),\qquad
s_0^{[0]}=-\frac{A_Y^2z_i^4}{4R^2}
+o^1(R^{-2}).
\tag{6}
$$
特别，(6)使用第二低尾的真实 incoming，
不是把第一低尾复制到内部事件。
乘以原时长 $M\ell_i/(\delta R^{3/2})$，
得到两段的总贡献
$$
\frac{\delta R^{7/2}}M S_0^{[0]}\big|_{\rm low}
\longrightarrow
-\frac{A_Y^2Z_*^4}{4}
  (\ell_1+\ell_2/16).
\tag{7}
$$

### 2.2 两段高尾

在两段高尾上，R556 的实际目标均满足
$$
\mathfrak r:=hj=\mathfrak bM/R+o^1(M/R),\qquad
u=-A_Yz^2/R+o^1(R^{-1}),\qquad
\eta=\mathfrak r-u.
\tag{8}
$$
两个高度通常不同，但各自均为 $\asymp\sqrt M R$。
原 $p_2$ 坐标准确给
$$
p_2\,ds=\frac{dz}{\delta\sqrt R}.
\tag{9}
$$
(5)的主要静态部分是 $-\eta u^2p_2/2$。
贯穿两段，$z$ 从 $Z_*+o^1(1)$ 降至0，
所以
$$
\begin{aligned}
\frac{\delta R^{7/2}}M
 \int_{\rm high}-\frac{\eta u^2p_2}{2}\,ds
&=-\frac{R^3}{2M}\int_{Z_*+o^1(1)}^0\eta u^2\,dz\\
&\longrightarrow \frac{\mathfrak b A_Y^2Z_*^5}{10}.
\end{aligned}
\tag{10}
$$
$p_0$ 的另一项 $h^{-2}p_2$ 在此尺度上为 $O(M^{-1})$。
原 $-\eta^2/4$ 的真实时间成本也为 $O(M^{-1})$：
高尾时间为 $O((\delta M^2R^{3/2})^{-1})$，
而 $\eta^2=O(M^2/R^2)$。
两项都保留在原累计内，不当作点态零。

### 2.3 原最早快准备与所有速度成本

不能只凭(7)(10)宣布净正。R544 的原快准备及其开放反馈接入，
在原固定低高度盒内有
$$
|h-H|+|k|+|\eta|=O(\lambda),\qquad
|h_s|+|d_s|=O(\lambda/\delta),
$$
实际总快时长为 $O(\delta)$。
因此它的完整 $S_0$ 速度平方费用为
$$
O(\lambda^2/\delta).
$$
在本节更细尺度上，其绝对值至多
$$
C\frac{R^{7/2}\lambda^2}{M}
=O(R^{-1/2}/M)\longrightarrow0.
\tag{11}
$$
这里使用 $\lambda=L_h^2/R^2$。
这个原 $1/\delta$ 费用没有归入一个事后可压的有限慢桥常数。

共同饱和高前缀满足
$h\asymp R$、$k=O(1)$、$u,\eta=O(R^{-1})$，
其 $\delta R^{3/2}s$ 时长为 $O(1+\log R)$。
故其完整静态 $S_0$ 在本节尺度上为
$O((1+\log R)/M)=o(1)$。
更早的 R544 原恒参考长段按同一个
$O(\lambda^2/\delta)$ 时间界和原小 scalar 盒估计，贡献也为低阶。

其余有限高度桥的完整静态和速度平方费用是有限 $C_R$，
最后统一小 $\delta$ 后乘以 $\delta R^{7/2}/M$ 趋零。
两个低尾与两个高尾的真实反馈速度
$h_s,k_s=O(C_R\delta)$，
结合各自原长时钟，速度平方费也在最后同一个 $\delta$ 中趋零。
所有这些估计保原端图参数的一阶导数。

因此整个实际 core 有完整 $C^1$ 极限
$$
\boxed{
\frac{\delta R^{7/2}}M S_0^y\big|_{\rm core}
\longrightarrow
K(\theta):=
\frac{A_Y^2}{4}
\left\{\frac{2\mathfrak b Z_*^5}{5}
      -Z_*^4(\ell_1+\ell_2/16)\right\}.
}
\tag{12}
$$
在(4)处，
$$
\boxed{
K(\theta_*)=\frac{\mathfrak b A_Y^2Z_*^5}{60}>0.
}
\tag{13}
$$
这才是本稿负速度补偿可使用的真实正余量。
取足够小的共同参数盒后，$K$ 保持严格正。

## 3. 拉长原闭振子，而不假定交叉槽仍为零

固定 R557 使用的非零紧支撑光滑函数 $\psi$。
记
$$
I_1=\int(\psi')^2>0,\quad
I_2=\int(\psi'')^2>0,\quad
I_3=\int(\psi''')^2>0.
$$
可以保持其原归一 $I_3=I_2$，但下文不使用这个等式去删除伸缩后的交叉项。

令新的正长度参数为 $\ell$，最终限制在一个固定正紧盒。
置
$$
\varepsilon=R^{-3/4},\qquad
L=\ell\,R^{1/2}M^{-1/4},\qquad
\sigma=\varepsilon\sqrt L.
\tag{14}
$$
$\tau=(s-s_{\rm in})/\delta$ 仍是同一个原快时钟。
在长快区间定义
$$
\psi_L(\tau)=\sqrt L\,\psi(\tau/L),\quad
D_L=\psi_L'',\quad
f_L=-\frac{\psi_L''+\psi_L}{\beta},
\quad \beta=\frac{B(H,0)}{2c}>0.
\tag{15}
$$
原线性闭振子身份准确为
$$
D_L''+D_L=-\beta f_L'',\qquad
\int D_L'f_L''=0.
\tag{16}
$$
所有端 jets 仍为0。

但三个相关二次量准确变成
$$
\begin{aligned}
\int(f_L')^2
 &=\frac1{\beta^2}
  (I_1-2I_2/L^2+I_3/L^4),\\
\int(D_L')^2&=I_3/L^4,\\
\int f_L'D_L'
 &=\frac1\beta(I_2/L^2-I_3/L^4).
\end{aligned}
\tag{17}
$$
所以(16)的二阶第三面积为0，并不使(17)最后一行等于0。
这个区别在真实余矩中保留。

从 R556 最后高尾的真实状态沿原反馈有限下降到 $H$，
取开放恒参考段。其 incoming 仍为 R557 的原界
$$
\mathsf A_{\rm in}:=\delta A_{\rm in}
 =O(a_R),\qquad
\mathsf T_{\rm in}:=\delta^2T_{{\rm third},{\rm in}}
 =O(g_R)+O(C_R\delta^2),
$$
$$
a_R=M/R^{3/2},\qquad g_R=M/R^2,
\tag{18}
$$
并有 $k,\eta,d,j=O(g_R)+O(C_R\delta)$。
入口开放恒参考段还提供同一反馈的强准备：
$$
h-H=O(C_R\delta),\quad
h_\tau,k_\tau=O(C_R\delta^2),\quad
d-q_\Gamma(h)=O(C_R\delta^2).
\tag{18a}
$$
最后一式是 R544/R552 恒参考法向估计；
不能只用 $d=O(g_R)$ 代替它，否则可能留下足以污染
下文精细 $S_0$ 费用的自由振子能量。
这些界保端图参数的一阶导数。
所有初值都是真实 incoming，后面不重设为0。

长快段使用原唯一高度加速度输入，
其领先高度为
$$
h=H+\varepsilon a f_L(\tau)
=H-\frac{a\sigma}{\beta}
\{\psi(\tau/L)+L^{-2}\psi''(\tau/L)\}.
\tag{19}
$$
$a>0$ 是原 R557 的幅值参数，最终也取固定正紧盒。
实际入口接原反馈 germ；末端仍用四个原加速度内控接回真实开放反馈。
它们在第5节支付。


## 4. 长快区间的完整历史与统一振子估计

固定 $a,\ell,\theta$ 的共同紧盒。
本节常数除显式 $C_R\delta$ 余项外，不随 $R,L$ 增长。
高度变化的实际幅度是 $\sigma$，不是 $\varepsilon$；
所用区间在快时钟中的长度是 $O(L)$，不能沿用固定长度
R557 的一个未经估计的 $e^{CL}$ 常数。

有四个准确小参数：
$$
\sigma\longrightarrow0,\quad
a_RL=O(M^{3/4}/R),\quad
g_RL^2=O(\sqrt M/R),\quad
L^{-2}=O(\sqrt M/R).
\tag{20}
$$
置
$$
\kappa_R=\sigma+a_RL+g_RL^2+L^{-2}\longrightarrow0.
\tag{21}
$$
最后的 $\delta$ 误差可以在每个固定 $R$ 上同时小于
本节所有明确尺度，以下用 $o_\delta$ 保留它们。

### 4.1 原无 $k_{\tau\tau}$ 第三变量

令 $G=h_\tau$、$V=k_\tau$，使用原
$$
\mathsf A=\delta A,\qquad
\mathsf Z=\delta^2\widetilde T
=\delta^2T_{\rm third}-P_{\rm acc}(S;G,V)+\mathcal A(S)GV .
$$
这是变量变换，不是重新选择第三字段。
R537/R544 的完整快方程为
$$
\mathsf A_\tau=\delta^2\Phi_{M_0}+\Phi_{M_2(S;G,V)},
\tag{22}
$$
$$
\begin{aligned}
\mathsf Z_\tau={}&
-(\delta^2\Phi_{M_0}+\Phi_{M_2})\circ\mathsf A
+\delta^2\mathcal C^{[1]}\\
&+2\mathcal A(S)h_{\tau\tau}V
+\{\mathcal X\mathcal A\,G+\mathcal Y\mathcal A\,V\}GV
+\sum_j\mathcal B_j(S)G^{3-j}V^j .
\end{aligned}
\tag{23}
$$
原有序复合、速度面积和所有 $YC$ 项均在(23)内。
特别保留
$-\Phi_{M_2}\circ\mathsf A_{\rm in}$。
(23)中没有尚待估计的 $k_{\tau\tau}$。

有效 Gram $\Gamma=\Gamma(\mathsf A,\mathsf Z)$ 仍用 R544 原式。
在以下盒内有
$$
\Gamma_1=2c+O(g_R),\qquad
|\Gamma_0|+|\Gamma_2|=O(g_R).
\tag{24}
$$
原稳定支 $q_\Gamma(h)$ 和其系数光滑，
$q_\Gamma=O(g_R)$、$\partial_hq_\Gamma=O(g_R)$。

先在一个放大的最大区间上假设
$$
h=H+O(\sigma),\quad
|k|+|\eta|+|d|=O(g_R+\sigma/L^2),\quad
|G|=O(\sigma/L),\quad |V|=O(\sigma/L^3).
\tag{25}
$$
后面将严格改进这些界。

由(22)(23)逐项积分，原历史的增量满足
$$
\|\Delta\mathsf A\|
\le C\sigma^2/L+o_\delta
=C\varepsilon^2+o_\delta,
\tag{26}
$$
$$
\boxed{
\|\Delta\mathsf Z\|
\le C\{a_R\sigma^2/L+\sigma^2/L^4+\sigma^3/L^2\}
+o_\delta .
}
\tag{27}
$$
三项的原来源分别是有序 $M_2\circ\mathsf A$、
$h_{\tau\tau}V$、以及完整三次速度多项式。
系数变化的 $GV$ 项包含在后两项中。
$M_0$、$\mathcal C^{[1]}$ 的实际贡献至多为有限
$C_R\delta^2L$，没有从原方程删除。

(26)不超过 $O(a_R)$，(27)为 $o(g_R)$：
$$
a_R\sigma^2/L=M/R^3,\quad
\sigma^2/L^4=O(M^{3/4}/R^3),\quad
\sigma^3/L^2=O(M^{1/8}/R^{5/2}).
\tag{28}
$$
真实 $T_{\rm third}$ 在内部还包含原速度势。
其缩放大小至多 $C(G^2+V^2)=O(\sigma^2/L^2)=o(g_R)$，
所以整个长快区间上真实 $\delta^2T_{\rm third}$ 也有 $O(g_R)$ 界。

水平式 $j_\tau=-2dG/h^3$ 给
$$
|\Delta j|\le C(g_R\sigma+\sigma^2/L^2)+o_\delta
=O(g_R).
\tag{29}
$$
这些估计保全部 incoming，不依赖先证明末端历史为0。

### 4.2 完整快方程的正频率形式

以 $e=d-q_\Gamma(h)$ 为法向变量。
由 $V=2\eta G-2d_\tau$ 和
$C_h+2\eta C_k=-B$，
将原完整 ruling 改写为正频率二阶方程。
把 $\Gamma_\tau$ 中的原(22)(23)一并代入；
若微分 $q_\Gamma(h)$ 产生一个 $d_{\tau\tau}$ 项，
其质量修正为
$$
1+O(a_R|V|+|h_{\tau\tau}|+G^2),
$$
在(25)中严格正，因而可以准确除去。
这一步没有把含 $e_\tau$ 的原 $L_{\rm vel}$ 当作小常势。

把含 $e,e_\tau$ 的点态线性部分保在左边，并保累计状态产生的
因果项，得到
$$
e_{\tau\tau}-b(\tau)e_\tau+\omega(\tau)^2e
=-\beta h_{\tau\tau}+F_{\rm slow}+\mathcal K[e].
\tag{30}
$$
$\mathcal K$ 是真实历史误差的因果作用，以下单列其小量；
不能把它悄悄当成与解无关的缓变强迫。
这里
$$
\omega^2=1+O(\sigma+g_R),\quad \omega^2\ge\tfrac12,\qquad
|b|\le C(a_R+\sigma/L).
\tag{31}
$$
完整系数的一阶总变差与阻尼总量满足
$$
\int_0^{LT_f}\bigl(|(\omega^2)_\tau|+|b|\bigr)\,d\tau
\le C(\sigma+a_RL)+o_\delta.
\tag{32}
$$
因此即使 $b$ 的号不固定，正能量的增长因子也统一有界；
这里没有使用 $e^{CL}$。

在原慢时钟 $t=\tau/L$ 上，先将给定的法向比较函数代入
原(22)(23)与水平式，恢复它的完整累计状态。
其所需的 $d_\tau$ 隐式系数与上述质量一样接近1，
因而这是一个实际有限维初值系统。
在比较函数的缓变部分上，(30)右端除了
$-\beta h_{\tau\tau}$，各组完整强迫及其前两阶加权导数
由下表控制；与比较函数的差别保在 $\mathcal K$ 内：

| 原项 | 值、$L$ 倍一导、$L^2$ 倍二导的界 |
|---|---:|
| $C_k,B$ 与有效频率相对 $H$ 的变化 | $C(\sigma+g_R)\sigma/L^2$ |
| 原全部速度二次项 | $C\sigma^2/L^2$ |
| 原 $L_{\rm vel}(\mathsf A\Delta)$ | $Ca_R\sigma/L$ |
| $q_\Gamma(h)$ 的二阶导数与原历史导数 | $C\{g_R\sigma/L^2+a_R\sigma^2/L^3+\sigma^3/L^4+\sigma^2/L^6\}$ |
| 原 $\delta^2R_0,M_0,\mathcal C^{[1]}$ 及入口误差 | $o_\delta$ |

这些导数由给定光滑比较函数和原累计 ODE 取出。
它们不是预先假设真实法向余量也缓变。
(23)无 $k_{\tau\tau}$，所以这张表不循环依赖一个自由加速度。

具体地，两个具有同一真 incoming 的比较解之差记为 $z$。
原 $M_2$ 对 $V$ 的导数为 $O(G+V)$；
经有效 Gram 对 $\mathsf A$ 的真实导数 $O(a_R)$ 配对，
其 $z_\tau$ 系数为 $O(a_R\sigma/L)$。
原第三速度面积贡献的该系数为 $O(\sigma/L^2)$，
原三次速度项为 $O(\sigma^2/L^2)$。
故完整有效历史差中的 $z_\tau$ 项系数为
$$
O(a_R\sigma/L+\sigma/L^2+\sigma^2/L^2).
\tag{32a}
$$
将这些真实因果积分中的 $z_\tau$ 一次分部积分。
入端差为0，末端项收入(30)的点态频率／质量；
剩余核由
$$
C(a_R\sigma/L^2+\sigma/L^3+\sigma^2/L^2)
\tag{32b}
$$
控制。先对历史积分、再对振子强迫积分，
相应总算子范数至多
$C(a_R\sigma+\sigma/L+\sigma^2)$，趋于0。
$j$ 的差由 $j_\tau=-2dG/h^3$ 积分；
它只经速度二次项或 $\mathsf A$ 速度项回到(30)，有更小的同类界。
余下非线性项在(25)中也带一个
$O(\sigma/L^2)$ 法向小因子。

还由(14)(18)有
$$
L(a_R\sigma+\sigma/L+\sigma^2)\longrightarrow0.
\tag{32c}
$$
因此将一个 $O(\mu_R)$ 缓变修正重新送入真实历史所产生的能量误差
也是 $o(\mu_R/L)$，不会损失下面的一阶速度精度。

在原正能量范数内，
$\mathcal K$ 的差是一个范数趋于0的因果算子。
这一步显式保留了真实累计历史的反馈，而非把(30)当无历史的
外力振子。参数的一阶变分满足相同核界。

### 4.3 一次缓变修正与能量闭合

先代入原精确线性解
$$
e_0=\varepsilon aD_L.
$$
由(16)，它准确支付常系数部分
$e_0''+e_0=-\beta h_{\tau\tau}$。
把该比较函数的原累计状态一并恢复后，
剩余缓变强迫 $F$ 连同其前两阶加权导数有界于
$$
\mu_R
=C(\sigma+a_RL+g_R+L^{-2})\,\sigma/L^2+o_\delta.
\tag{33}
$$
取一次缓变修正 $F/\omega^2$。
其代回(30)后的残余为 $O(\mu_R/L^2)$；
$b(F/\omega^2)'$ 也在此界内，因为 $a_RL+\sigma=o(1)$。

对最后余量取原正振子能量。
由(32)，有限快长度 $O(L)$ 上的显式强迫积分至多
$C\mu_R/L$；(32a)(32b)的真实因果差在充分大 $R$ 后
范数小于 $1/2$，可吸收到能量左边。
等价地，可用相同真 incoming 的累计恢复与振子解构成一个
小范数因果迭代；其固定点就是原完整初值解。
因此
$$
\begin{aligned}
|e-e_0|&\le C\mu_R+o_\delta,\\
|e_\tau-e_{0,\tau}|&\le C\mu_R/L+o_\delta .
\end{aligned}
\tag{34}
$$
这就是为何不能把长区间直接套固定长度连续依赖估计。

另一方面，原(22)(23)和水平式给
$$
|(q_\Gamma(h))_\tau|
\le C\{g_R\sigma/L
+a_R\sigma^2/L^2+\sigma^2/L^5+\sigma^3/L^3\}
+o_\delta .
\tag{35}
$$
将(33)–(35)合并，得到需要的真实速度精度
$$
\boxed{
\left\|d_\tau-\varepsilon aL^{-5/2}\psi'''(\tau/L)
\right\|_{L^2(0,LT_f)}
\le C\kappa_R\,\varepsilon L^{-2}+o_\delta .
}
\tag{36}
$$
同时 $d-q_\Gamma(h)=\varepsilon aD_L+
O(\kappa_R\sigma/L^2)+o_\delta$。

为明确最大区间闭合，先以固定大常数放大(25)–(27)及上述法向界。
原余项中的二次法向误差具有
$O(\sigma/L^2)$ 小系数；其在长快区间的积分为 $O(\sigma/L)$。
它们连同(32)可吸收到同一个能量估计。
依次使用(26)(27)、(34)(35)、(29)：
先改进完整历史盒，再改进 $d_\tau,d$，
最后改进 $j,k,\eta$ 和原合法窗口。
这严格延长最大区间至全部 $LT_f$。
没有先假定长期存在再引用其历史界。

相同顺序应用于 $(\theta,a,\ell,v)$ 的一阶变分。
$\ell$ 变化只改变有限慢区间上的 $\partial_\ell L/L$，
其在固定正盒上有界。
因此(26)–(36)都是本稿端图所需的统一 $C^1$ 估计。
控制形状为固定 $C^\infty$ 函数；
所用加权二导表及其变分仅调用它的有限阶实际导数界。

## 5. 真实末 germ 和完整第三费用

在长形状的两端，$\psi$ 全 jets 为0。
(33)的一次缓变修正也在端部为0，除已保留的 $o_\delta$ 项。
因而未补偿的原末端法向残差满足
$$
|d-q_{\Gamma_{\rm out}}(H)|+|d_\tau|
\le C\mu_R/L+o_\delta .
\tag{37}
$$
高度与快高度速度的残差只有入口继承的 $o_\delta$。
在末端留一个固定长度的快区间，
用 R557(23)的四个原加速度内控和最终开放反馈段，
准确支付
$$
h=H,\quad h_\tau=0,\quad
d=q_{\Gamma_{\rm out}}(H),\quad d_\tau=0 .
\tag{38}
$$
其 Jacobian 在当前 small-state 盒内一致可逆。
实际控制修正的大小为 $O(\mu_R/L)+o_\delta$，
而非一个与长形状同幅的额外快撞击。

这些短控制的速度平方成本至多为
$O((\mu_R/L)^2)+o_\delta$。
与长回路 $S_0$ 的尺度
$\varepsilon^2/L^4=\sigma^2/L^5$ 比，
其比值趋零：
$$
\frac{(\mu_R/L)^2}{\sigma^2/L^5}
\le C\kappa_R^2/L+o_\delta\longrightarrow0.
\tag{39}
$$
所以末端付真 germ 没有破坏(36)所需的精度。
原 R544 反馈量在开放末段导数为0，
(38)使其值准确为0；
故这里仍是完整实际反馈 germ，而非只接四个端值。

真实第三增量仍逐项为 R557(26)：
原 $-\int M_2\circ\mathsf A_{\rm in}$、
内部有序交叉、$P_{\rm acc}$ 两端、
速度面积和三次速度项全保。
leading 面积由(16)准确消失；
原势在(38)的输出速度0处为0，输入的原小速度势仍保。
剩余完整估计即(27)，连同短端控的低阶费用。
真实 $T_{\rm third}$ 是相应缩放量除以 $\delta^2$，通常非零；
(27)绝不授予第三 period 返回。


## 6. 新回路的完整矩成本与两个非零交叉首项

令
$$
C_1=\frac{I_1}{8H^4\beta^2}>0,\qquad
C_3=\frac{I_3}{4H^2}>0.
\tag{40}
$$
原 R555 点态表、(19)(36)及真末控(39)给
$$
\begin{aligned}
\delta\,\Delta R_1^y
 &=\varepsilon^2a^2C_1\{1+o^1(1)\},\\
\delta\,\Delta T_1
 &=-\varepsilon^2a^2H^2C_1\{1+o^1(1)\},\\
\delta\,\Delta S_0^y
 &=-\frac{\varepsilon^2a^2C_3}{L^4}\{1+o^1(1)\}.
\end{aligned}
\tag{41}
$$
这些是同一个实际回路的三项费用。
$S_0$ 的相对精度来自(36)的 $L^2$ 估计，
不能只用一个不带 $L$ 权的 $O(\varepsilon^2)$ 误差来替代。

具体地，
$$
\delta\int s_0^{[2]}ds
=-\frac14\int(d_\tau/h)^2\,d\tau,
$$
其主值为(41)第三行；
静态部分在真实时间长度 $O(\delta L)$ 上有有限界，
乘以 $\delta$ 后由最后一次 $\delta$ 选择压低。
$R_1$ 的 $h^{-4}h_s^2/8$ 给第一行，
其余含 $u$ 或 $d_\tau$ 的原项由(25)(36)为相对低阶。
$T_1$ 的负高度速度平方给第二行。

同样必须保留
$$
\boxed{
\begin{aligned}
\delta\,\Delta S_1^y
 &=-\frac{\varepsilon^2a^2I_2}
          {4H^2\beta L^2}\{1+o^1(1)\},\\
\delta\,\Delta R_0^y
 &=+\frac{\varepsilon^2a^2I_2}
          {8H^4\beta L^2}\{1+o^1(1)\}.
\end{aligned}}
\tag{42}
$$
它们来自(17)的最后一行，新增回路上的领先号分别负、正。
(42)只是该回路增量，不预断全词这两个累计的号。
原 $T_0=P_0/4+S_1/2$ 始终保留。

三个 $p$ 没有速度二次项，新增长快回路的原静态增量至多
$C_R\delta L$。有限下降与开放段的完整增量则至多 $C_R$。
这些值以下在同一个原端图中准确校正。
原速度平方费用、第三有序成本与(42)都没有因
“快段很短”而被删掉。

## 7. 原停止坐标仍先准确支付 $P_2$

保持原最终高尾停止参数 $v$。
它之后的有限下降与整个长快回路都取同一个真实 incoming，
不重锚任何累计。
完整 $P_2$ 映射满足
$$
\sqrt R\,\delta\,P_2^{\rm total}
=v+O_{C^1}(C_R\sqrt R\,\delta)
 +O_{C^1}(C_R\sqrt R\,\delta^2L).
\tag{43}
$$
对每个已固定的有限 $R$，$L$ 在本稿正参数盒上也有限。
最后小 $\delta$ 使 $\partial_v$ 一致接近1。
所以有一个真正事件参数
$$
v=v(\theta,a,\ell)
$$
使总 $P_2=0$，并保全部一阶参数导数。
原高尾在0两侧的开放 $z_s<0$ 区间仍允许这两个符号的小修正。

(43)代回后的影响低于以下所有归一化尺度。
这里没有取一条已经准确停在0的旧路径后，
忽略新增快段的 $p_2$。

## 8. 五参数共同端图与准确第六零

在已经支付总 $P_2=0$ 的真实族上，以
$$
(\ell_1,\ell_2,\xi,a,\ell)
$$
为五个有限正参数。
四个末端内控和停止值均是这些参数的实际光滑函数。

读取完整端点映射
$$
\mathcal F=
\left(
\frac{\delta R^{5/2}}M P_1,\ 
\delta R^{5/2}P_0,\ 
\frac{\delta R^{3/2}}M T_1,\ 
\delta R^{3/2}R_1^y,\ 
\frac{\delta R^{7/2}}M S_0^y
\right).
\tag{44}
$$
前面各节给整个共同参数盒上的 $C^1$ 极限
$$
\boxed{
\mathcal F^\infty=
\left(
F_1^\infty(\theta),\
F_0^\infty(\theta),\
F_t^\infty(\theta),\
-\frac{\ell_1+\ell_2}{8\xi}+a^2C_1,\
K(\theta)-\frac{a^2C_3}{\ell^4}
\right).
}
\tag{45}
$$
最后一项使用
$L^4=\ell^4R^2/M$，因此(41)第三行准确落在
完整正余量(12)的尺度。

$T_1$ 的新负成本在第三坐标中为
$-a^2H^2C_1/M+o^1(M^{-1})$。
它只在极限(45)中消失，在实际 $\mathcal F$ 中从未删除；
原三个 core 参数会准确支付这个费用。
(42)则完全保在原 $S_1/R_0$ 累计内。

先取原 $\theta_*$。定义
$$
\boxed{
a_*^2=\frac{\ell_{1,*}+\ell_{2,*}}{8\xi_*C_1},\qquad
\ell_*^4=\frac{a_*^2C_3}{K(\theta_*)}.
}
\tag{46}
$$
两值严格正且有限。
(45)在 $(\theta_*,a_*,\ell_*)$ 的 Jacobian 分块下三角：
原三维块可逆，
第四行对 $a$ 的导数为 $2a_*C_1>0$，
第五行对 $\ell$ 的导数为
$$
4a_*^2C_3/\ell_*^5>0.
$$
所以五维 Jacobian 可逆。

先固定以(46)为内部点的一个正参数盒，
再取充分大的有限 $R$，最后同一次小正 $\delta$。
原有限维 IFT 给实际参数点
$$
(\theta_{R,\delta},a_{R,\delta},\ell_{R,\delta})
\longrightarrow(\theta_*,a_*,\ell_*),
\tag{47}
$$
使(44)的五个原累计准确为0。
结合(43)，得到(1)的六个准确零。
所有根都属于同一完整实际词的参数化，
没有分别选不同路径来清六个数。

## 9. 选择顺序、中心坐标和剩余真实义务

本稿不是拿 R557 已冻结的一个有限路径在中途重新选规范。
它使用同一 R556＋原加速度回路的实际控制族，
从起点将形状长度加入有限参数盒。
完整选择顺序为：

1. 固定 R521/R552 同一母库、原右锚、
   足够大的有限 $\omega_c$ 和全部已付严格号；
   保原 $H,H_0,c,L_h$、第二规范及 R544 反馈。
2. 固定 R556 的 $\mathfrak b>0$、内部事件 $z=Z_*/2$，
   以及 $\psi$、原四个末内控与开放反馈规则。
3. 由(4)(13)(40)(46)固定一个严格位于正象限的五参数盒。
4. 取充分大的有限 $R$，
   从而同时固定 $M,\lambda,\varepsilon$，
   并按各参数的 $\ell$ 定义有限长快时钟 $L$。
   (20)(21)(32c)及全部纯 $R$ 余量此时统一成立。
5. 在同一盒上固定各有限真实高度过渡；
   原高目标仍由各自完整 incoming 决定，
   最后下降到原 $H$。保所有有限费用及导数常数 $C_R$。
6. 最后一次取 $\zeta>0$，$\delta=\lambda^2\zeta$，
   从原起点固定唯一 $\chi$。
   同一个 $\delta$ 同时支付 core 的全部原成本、
   长快区间的 $\delta$ 余项、末 germ 和两个实际 IFT。
7. 在这份固定规范上先用(43)清 $P_2$，
   再用(47)选择五个几何参数。

没有把一条随 $R$ 增长的实际区间直接套入
固定区间 $C_R$ 连续依赖；长快区间的统一界由第4节单独支付。
物理高度扰动幅 $\sigma\to0$，
$k,\eta,d$ 在该段仍处原合法盒，
故原 $h>0$、$e>0$ 及 $C_k,B$ 正余量保持。
真实 frame、位置、第三和第四字段始终按原完整 ODE 恢复。

坐标转换仍是 R555 的原式。
三个 $P$ 和 $T_1$ 零后，
$$
R_1^y=R_1^x-\omega_cS_1^x,\qquad
S_0^y=S_0^x-2\omega_cS_1^x .
\tag{48}
$$
所以不能把(1)写成六个未经识别的原 $x$ 单槽都零。
在固定 $y$ 坐标中，剩余完整矩阵恰为
$$
\begin{pmatrix}
0&0&-4R_0^y\\
0&2S_1^y&0\\
0&0&-2S_1^y
\end{pmatrix}.
\tag{49}
$$
两个独立目标是 $S_1^y=0$、$R_0^y=0$。
(42)表明它们不能从本稿形状伸缩中免费删除。

**定理。** 在上述从起点一次选择中，
存在一条同 R521 母、同一右锚和同一个 $\chi$ 的有限光滑实际词，
从原零 $A,T$ 开始，完整全相位第四 ruling 恒为0，
并满足(1)。
末端是原反馈的真实开放 germ；
完整 incoming、所有速度平方、第三有序交叉、
原两端势以及全部实际时间成本均保留。

本稿不授两个余矩、frame／位置、第三／第四 periods、
同十三规范或最终主目标。
后继必须继续同一完整历史并联合保(44)的真实端点方程；
不能把两个新增交叉首项当成可任意选号的自由成本。

### 原来源

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：
  原八矩、完整 $M_2$、水平关系及有序第三累计；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：
  同一母库、全相位 ruling 和原 $C_k,B$；
- [R537](R537-prescribed-finite-height-paths-with-one-gauge-and-complete-history-energy-bounds.md)：
  无 $k_{ss}$ 的完整第三变量；
- [R544](R544-one-fixed-gram-and-a-real-path-with-negative-p1-and-positive-t1.md)：
  唯一规范、真零 history 快准备及完整反馈；
- [R550](R550-positive-horizontal-branch-and-exact-p2-zero-with-one-fixed-gauge.md)：
  原饱和等待与实际高尾停止接口；
- [R552](R552-three-exact-p-moments-with-one-gauge-and-a-positive-t1-remainder.md)：
  同词全成本、原有序历史与低高段精度；
- [R555](R555-five-remaining-moments-gram-energy-and-real-history-area-interfaces.md)：
  原静态／负速度表、trace 和中心坐标；
- [R556](R556-four-exact-matrix-moments-by-two-real-low-coasts-with-one-gauge.md)：
  原三参数端图、两个低尾的真实入值及负 $R_1^y$；
- [R557](R557-five-centered-matrix-moments-with-a-real-fast-height-loop-and-one-gauge.md)：
  当前 incoming 的完整快方程、四个实际末内控和开放反馈 germ。

本文新增的是完整 core 的正 $S_0^y$ 净首项、
增长快区间上的统一历史／振子估计，
以及同一个实际六方程共同零。没有新科学执行。
