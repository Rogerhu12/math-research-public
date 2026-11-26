# R567：完整次阶 S1 组合与同一规范的八个第二矩联合零

日期：2026-11-26。原式纸证；root 已逐段读取并对照原有序方程、
实际慢时钟、长快区间费用和参数端图。没有执行科学数值或符号计算。

本稿继续 R563 的三个真实低尾和 R564 的同一母库跨带。
新增部分是：在原完整有序第三 history 中保留此前被首阶精度遮住的
`r1` 列，给出整个参数盒上的细尺度消项恒等，再把两个不同高度的
真实长快回路放进同一个八矩端图。

这里所称“八矩零”只指原第二矩阵完全为零。
它尚不支付反射所需的全部 scalar germs、frame/位置、第四 period、
同十三规范或课题 README 的有限等距族。

## 1. 固定母、原规范和两个新的系数

所有数据属于 R521/R552/R563 的同一有限正交母库、同一物理区间、
真右锚和固定 profiles。保
$$
y=x+\Omega,\quad \eta=\omega-\Omega,\quad d=h\eta-k,
\quad u=d/h,
$$
$$
\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\qquad
R=L_h/\sqrt\lambda,\quad M=(1+\log R)^6,\quad
\delta=\lambda^2\zeta.
\tag{1}
$$
第二规范仍为零。原高度 $H_+=H$ 和 $H_0>\sqrt3H$
先固定；随后在这些固定数据和固定 profiles 上一次取大 $\Omega$。
R564 的负耦合高度是 $H_-=q_-/\Omega$，其中固定 $0<q_-<0.9$。
只在起点选择中同时加入本节末尾所需的严格号；路径内部不换
$\Omega$、$\chi$、$c=C_k(H_+,0)$ 或任一 profile。

用不同字体区分原算子和终点常数：
$$
Y=\Phi_{p_2}^{y},\quad Z_o=\Phi_{t_1}^{y},\quad
R_o=\Phi_{r_1}^{y},\quad V_o=\Phi_{p_1}^{y},\qquad Z=Z_*>0.
$$
原完整双线性配对为 R552(5)
$$
\mathcal B_j(E,F)
=I_{j,y}(F\Delta,E\Delta)
-2I_{j,y}\{g,E(g,F\Delta)\}.
\tag{2}
$$
它通常不对称。记
$$
Q_j=-\mathcal B_j(Y,Y),\quad
A_Y=-Q_2/(8c)>0,\quad g_j=-Q_jZ^2/2\quad(j=0,2),
$$
$$
D_Z=2\mathcal B_2(Z_o,Y)-\mathcal B_2(Y,Z_o)<0,
$$
$$
D_R=2\mathcal B_2(R_o,Y)-\mathcal B_2(Y,R_o),\qquad
\rho_*:=D_R/D_Z.
\tag{3}
$$
$D_Z$ 正是 R552 的 $D_*$；$D_R$ 是本稿必须保的新次阶系数。
不能在这一阶把 $R_o$ 当作零，也不能把两个复合次序合并。

以下所有渐近先固定上述母数据，再取大有限 $R$，最后在固定正参数盒上
统一取小正 $\delta$。符号 $o_\delta^1$ 表示对于每个固定有限
$R$，值与一阶控制参数导数都可由最后一次选择 $\delta$ 压低。
任意随 $R$ 的有限桥常数都只在这一步支付。

## 2. 实际 core 与准确的 S1 密度身份

core 采用 R563 的三低尾真实词，包括 R544 真零 history 准备、
原早期长段、R550 的饱和等待、三个低尾、三个高尾及全部有限过渡。
三低尾节点固定为
$$
r_1=1,\qquad r_2=1/2,\qquad r_3=1/4,
\quad z_i=Zr_i,
$$
第一节点是 $Z+o^1(1)$ 的真实饱和入口，后两个是原累计的准确事件。
参数为
$$
\theta=(\ell_1,\ell_2,\ell_3,\xi),\quad
H_{\rm low}^2=M\xi,\quad
T_i=M\ell_i/(\delta R^{3/2}),\qquad
\mu_j=\sum_i\ell_i r_i^j.
\tag{4}
$$
所有参数在严格正紧盒中变化。每个高目标由当次真实 incoming 和
原水平式决定，绝不复制第一段的 Gram。先把最后高尾停在准确 $z=0$；
后面增加回路时再保小停止参数 $v$ 并准确付总 $P_2$。

R562(5)(6)给
$$
p_1=2up_2,\qquad p_0=(u^2+h^{-2})p_2,
$$
$$
8t_1=\mathcal A-(h_s/h)^2,\qquad
4s_1=u\mathcal A-(h_s/h)(d_s/h).
$$
由 $d_s/h=u_s+u h_s/h$，得到准确身份
$$
\boxed{s_1=2u\,t_1-\tfrac14(h_s/h)u_s.}
\tag{5}
$$
这一步不冻结历史、不抹去速度项。

core 中(5)的最后一项在 $\delta R^{5/2}$ 尺度趋零。
最早快准备的全部速度平方是原 $O(\lambda^2/\delta)$，归一后为
$O(R^{-3/2})$。有限桥的实际速度费用是 $C_R$，最后乘
$\delta R^{5/2}$ 支付。其余原恒参考慢尾有
$h_s,k_s=O(C_R\delta)$，在各自已经证明的真实长时钟上积分，
归一量也由最后 $\delta$ 支付。这些是一阶参数一致的原估计，
不把首次 $1/\delta$ 快成本藏进 $C_R$。

## 3. 完整 history 的精度升级：保留三条横列

令
$$
a=\sqrt R\,\delta A,\qquad b=R\delta^2\widetilde T,
\qquad z=a_{p_2}=\sqrt R\,\delta\,\mathsf m_{p_2}.
\tag{6}
$$
其中 $\widetilde T$ 是 R537(14) 的原速度势变换，不是
$-A\circ A/2$。定义全程准确的两个累计读数
$$
w=\frac{\delta R^{3/2}}{M}\,\mathsf m_{t_1},\qquad
r=\delta R^{3/2}\,\mathsf m_{r_1},
\quad a_{t_1}=\frac MRw,\quad a_{r_1}=\frac1Rr.
\tag{7}
$$
特别，$w$ 包含原饱和等待的全部 $O(\log R/M)$ 成本；
这里从不把它替成只有三个竖段和高尾斜段的极限折线。

### 3.1 本稿实际使用的已发表输入

下面的升级不来自把 R552 的 $o(M)$ 宣称为 $o(1)$。
所用的是已付的原方程与几何/变分盒：

- R550(8)(11)(16)：首高尾原八列表、完整有序慢方程以及
  $\int|k|\,d\tau\le C+C\log R/R$；
- R552(16)(18)(26)(41)、R563(15)(20)(24)：实际低/高尾方程、
  开放恒参考速度界、严格停止导数及真实水平分部积分；
- R562(5)(6)(23)–(31)：原全八密度与各段实际高度、时间、速度成本；
- R544(28)(48)(49)和 R537(15)：首次快准备的
  $\bar A,\bar T=O(\lambda^2)$，以及原第三方程的完整无
  $k_{ss}$ 余项。

R563 §4.1 已给这些状态盒的一阶参数变分控制；下面只对已存在的原解
逐列重新积分，不重新假设长期存在或新的自由静态轨道。

分段路径的 $BV,C^1$ 范数指：在各原有限慢时钟、首次固定快时钟、
有限桥时钟上取值、总变差及它们的一阶参数导数，再求有限段和。
事件的参数导数由 R563(20) 支付。首次公共前缀与 $\theta$ 无关。

### 3.2 原全八列的有界变差账

真实总变差满足
$$
\|z\|_{BV,C^1}\le C,
\qquad \|w\|_{BV,C^1}+\|r\|_{BV,C^1}\le C+o_\delta^1(1).
\tag{8}
$$
解释每个可能长时间来源：首高尾由上述 $\int|k|$ 付 $z$；
三个高尾的 $z$ 严格下降且都在固定区间；低尾总 $|\Delta z|$
为 $O(M/R^2)$。$w$ 在三个低尾和三个高尾的总变差为 $O(1)$，
等待为 $O((1+\log R)/M)$。$r$ 的主变差在三个低尾，
高尾与等待合计只有 $O((M+1+\log R)/R^2)$。

除这三列外，原表直接给下表；速度及有限桥的 $o_\delta^1$
与首次快准备单列保留：

| 原缩放累计列 | 全 core 的 $BV,C^1$ 上界 |
|---|---:|
| $a_{p_0}$ | $C/R^2$ |
| $a_{r_0}$ | $C/R^2$ |
| $a_{s_1}$ | $CM/R^2$ |
| $a_{s_0}$ | $CM/R^3+C R^{-7/2}$ |

例如低尾的 $p_0$ 由
$(u^2+h^{-2})|dz|=O(M^{-1})O(M/R^2)$ 给 $O(R^{-2})$；
低尾静态 $r_0=O((MR)^{-1})$ 乘实际
$\delta\sqrt R\,T_i=M\ell_i/R$，同样给 $O(R^{-2})$。
高尾有
$$
h\asymp\sqrt M R,\quad u=O(R^{-1}),\quad
\eta=O(M/R),\quad
\mathcal A=O(M^3),\quad \mathcal B=O(M^3/R),
$$
和 $\delta\sqrt R\,T_{\rm high}=O((M^2R)^{-1})$，
故 $a_{s_1}=O(M/R^2),a_{s_0}=O(M/R^3)$。
首高尾的 $p_0$ 更直接由
$da_{p_0}=(u^2+h^{-2})dz$、$u=O(R^{-1})$、$h\asymp R$
及 R550(16) 的 $\operatorname{TV}(z)\le C+C\log R/R$
得到 $C/R^2$，没有对数损失；其 $r_0$ 甚至为
$O((1+\log R)/R^4)$。首高尾的 $s_1,s_0$ 两列至多为
$C(1+\log R)/R^2$、$C(1+\log R)/R^3$，被表中 $M$ 控制。
低尾的 $s_1,s_0$ 分别是 $O(R^{-1}),O(R^{-2})$ 密度，
得到同一表。首次快段给所有速度列至多
$C\sqrt R\lambda^2=C R^{-7/2}$。

最后单独处理 $p_1$ 列，不能只使用 $O(R^{-1})$。
原稳定支、R552(51)和各真实状态盒给
$$
u=-A_Yz^2/R+O(M/R^2)-\frac{\Gamma_0}{4ch^2}
+o_\delta^1(R^{-1})
\tag{9}
$$
于各慢段；(9)在低尾的逆高度项不应并入 $O(M/R^2)$。
但其 $|dz|$ 积分为 $O(R^{-3})$：低尾是
$O((MR)^{-1})O(M/R^2)$，首高尾为 $O(R^{-3})$，
后高尾更小。首次原准备和早期长段另由 R544 的实际时钟给更低阶。
由准确 $da_{p_1}=2u\,dz$，令
$$
v(z)=-2A_Yz^3/3,
$$
便有
$$
\left\|a_{p_1}-\frac1R v(z)\right\|_{BV,C^1}
\le CM/R^2+o_\delta^1(R^{-2}).
\tag{10}
$$
同一逐列计算施于原参数变分，因乘积的各因子已有相应 $C^1$ 盒，
给出的正是表和(8)(10)的参数一致总变差，不只是端值估计。

合并得到所需的新精度
$$
\boxed{
a=zY+\frac MRwZ_o+\frac1RrR_o+\frac1Rv(z)V_o+E_a,
\quad
\|E_a\|_{BV,C^1}\le CM/R^2+o_\delta^1(R^{-2}).
}
\tag{11}
$$

### 3.3 原第三项及有序余项

由 R537(15)，在任何真实段准确写成
$$
db=-da\circ a+dE_C.
\tag{12}
$$
$dE_C$ 保原权一项、$2\mathcal A h_{ss}k_s$、
全部速度面积及三次速度项。
首次快准备在快时钟上直接积分：
$h_\tau,k_\tau,h_{\tau\tau}=O(\lambda)$，
面积项缩放 $\Delta\bar T=O(\lambda^2)$，故
$\|E_C\|_{BV}=O(R\lambda^2)=O(R^{-3})$，
不是错误的 $O(\lambda^3)$。
其余有限桥的所有原导数在固定 $R$ 后有有限界。
各恒参考长尾满足 $h_s,k_s=O(C_R\delta)$、
$h_{ss},k_{ss}=O(C_R)$；原 $\mathcal C_{\rm slow}$
因此为 $O(C_R\delta)$。在实际 $O(C_R/\delta)$ 长度上积分后，
乘 $R\delta^2$ 仍为 $o_\delta^1$。
所以
$$
\|E_C\|_{BV,C^1}\le CR^{-3}+o_\delta^1(R^{-3}).
\tag{13}
$$
以上使用实际被证明的加速度界，没有在第三方程里遗留一个未控制的
$k_{ss}$。

把(11)代入(12)，保三个横列的一次项，得到
$$
\begin{aligned}
b={}&-\frac{z^2}{2}Y\circ Y\\
&-\frac MR\int\{wY\circ Z_o\,dz+zZ_o\circ Y\,dw\}\\
&-\frac1R\int\{rY\circ R_o\,dz+zR_o\circ Y\,dr\}\\
&-\frac1R\int\{vY\circ V_o\,dz+zV_o\circ Y\,dv\}+E_b,
\end{aligned}
\tag{14}
$$
$$
\boxed{\|E_b\|_{BV,C^1}\le CM^2/R^2+o_\delta^1(R^{-2}).}
\tag{15}
$$
所有积分都从真正零 history 的原起点开始。
(15)有明确来源：横列相互复合的总变差至多
$C(M/R)^2$，含 $E_a$ 的项至多 $CM/R^2$，
原 $E_C$ 为(13)。不使用任何 $b=-a\circ a/2$ 替代。

## 4. 整个参数盒上的完整 P1 次阶

实际有效 Gram 是
$$
\Gamma_j=\bar\nu_j+\Xi_j(a,b)/R,\quad
\Xi_j=\tfrac12I_{j,y}(a\Delta,a\Delta)
+2I_{j,y}\{g,b(g;\Delta)\}.
\tag{16}
$$
在纯 $Y$ 路径记 $\xi_j(z)=-Q_jz^2/2$。
由(11)–(15)及原 $d\Xi_j=\mathcal B_j(da,a)$
（保(13)原余项），每个横列 $\epsilon qU$ 的一次贡献为
$$
\epsilon\int\{\mathcal B_j(Y,U)q\,dz
+\mathcal B_j(U,Y)z\,dq\},
\tag{17}
$$
其余 $\Xi_j$ 项的 $BV,C^1$ 范数不超过
$CM^2/R^2+o_\delta^1(R^{-2})$。
在准确闭 $z$ 路径上，一次分部积分给
$$
\int \Xi_2\,dz
=\frac MRD_Z\int zw\,dz+rac1RD_R\int zr\,dz
+O^1(M^2/R^2)+o_\delta^1(R^{-2}).
\tag{18}
$$
$V_o$ 项不留下常数，因为其系数 $v(z)$ 是单值函数，
$\int zv(z)\,dz=0$。纯 $\xi_2(z)$ 同样准确消失。
上式没有要求 $w$、$r$ 或第三 history 自身闭合。

要从(18)读真实 $P_1$，还必须处理 $\Gamma_1$ 和规范常项，
不能沿用 R552(52)的旧粗余项。
令 $U_R(z)$ 为仅使用
$\bar\nu_j+\xi_j(z)/R$ 且去掉 $h^{-2}$ 后的原小根：
$$
(2c+\xi_1/R)U_R
+(\lambda+\xi_2/R)/2
+(-H_0^2\lambda+\xi_0/R)U_R^2/2=0.
\tag{19}
$$
它是单值光滑函数，且 $U_R=-A_Yz^2/R+O^1(R^{-2})$。
稳定小根的隐式导数统一有界，由(11)–(17)与稳定支的原准确约束
$$
\Gamma_1u+\Gamma_2/2+\Gamma_0(u^2+h^{-2})/2=0
$$
得到积分型估计
$$
\int\left|u-U_R(z)
+\frac{\Xi_2-\xi_2(z)}{4cR}\right|\,|dz|
\le CM^2/R^3+o_\delta^1(R^{-3}).
\tag{20}
$$
其中高度项的 $|dz|$ 费用是 §3.2 已明确给出的 $O(R^{-3})$；
$\Gamma_1$ 分母的路径依赖部分是 $O(M/R^2)$，
乘 $u=O(R^{-1})$ 后是 $O(M/R^3)$；其纯 $z$ 部分全在
$U_R$ 中。$\Gamma_0u^2$ 的其它项更小。
真正反馈误差及有限桥由最后 $\delta$ 支付。
同样估计对参数一阶导数成立。

准确 $p_1=2up_2$ 与 $dz=\sqrt R\delta p_2ds$ 给
$\delta R^{5/2}P_1=2R^2\int u\,dz$。
用 $\int U_R(z)dz=0$、(18)(20)，得到
$$
\boxed{
\delta R^{5/2}P_{1,\mathrm{core}}
=-\frac1{2c}\left\{
D_ZM\int zw\,dz+D_R\int zr\,dz\right\}
+O^1(M^2/R)+o_\delta^1(1).
}
\tag{21}
$$
这里 $M^2/R\to0$。原 $O(\log R)$ 等待没有被称为低阶；
它仍准确留在 $M\int zw\,dz$ 中。

## 5. S1 的次阶与等待统一相消

从(5)(7)及 §2 的真实速度账，
$$
\delta R^{5/2}S_{1,\mathrm{core}}
=2RM\int u\,dw+o^1(1).
\tag{22}
$$
原小根在 $|dw|$ 积分意义满足
$$
\int\left|u+\frac{A_Yz^2}{R}
+\frac{\Gamma_0}{4ch^2}\right|\,|dw|
\le CM/R^2+o_\delta^1(R^{-2}).
\tag{23}
$$
此处纯 $z$ 分母及规范 $\lambda$ 项均为 $O(R^{-2})$，
横向 history 为 $O(M/R^2)$，乘 $RM$ 后是 $O(M^2/R)$。
原快段另外按 §2 付出；不把非稳定快段代入稳定小根。

准确闭 $z$ 给
$\int z^2dw=-2\int zw\,dz$，即使 $w$ 的末值不为零也无边项。
逆高度项在低尾的真实首值为
$$
\Gamma_0=g_0r_i^2/R+O^1(M/R^2),\quad
h^2=M\xi+o_\delta^1(1),\quad
dw=-d\theta_i/8+o^1(1).
$$
首高尾、后高尾对 $RM\int(\Gamma_0/h^2)dw$ 分别为
$O((1+\log R)/R^2)$、$O(R^{-2})$；
首次准备和全部有限桥按上文支付。
于是
$$
\boxed{
\delta R^{5/2}S_{1,\mathrm{core}}
=4A_YM\int zw\,dz+\frac{g_0\mu_2}{16c\xi}
+o^1(1).
}
\tag{24}
$$

同样由原低尾表，$r$ 在第 $i$ 个低尾改变
$-\ell_i/(8\xi)+o^1(1)$，高尾的变化趋零。
由于 $z$ 全程有界变差且起末为零，
$$
\int zr\,dz=-\frac12\int z^2dr
=\frac{Z^2\mu_2}{16\xi}+o^1(1).
\tag{25}
$$
这一行使用真实 $r$，不是从形式 Gram 分配出来的自由变量。

R562(37)和已实现第三低尾的 R563 同时给
$$
\delta R^{5/2}R_{0,\mathrm{core}}
=C_0(\theta)+o^1(1),\qquad
C_0(\theta)=\frac{A_YZ^2\mu_2}{8\xi},
\tag{26}
$$
$$
\delta R^{5/2}P_{0,\mathrm{core}}
=Z-\frac{g_0\mu_2}{6c\xi}+o^1(1).
\tag{27}
$$
(26)(27)本来就是本稿所需细尺度；只对(21)(24)新增精度。
其中 $R_0$ 低尾的 $2p_0$ 余项可给 $O(M^{-1})$，仍趋零。

把(21)(24)–(27)合并，在整个原正参数盒得到
$$
\boxed{
\delta R^{5/2}\left[
S_{1,\mathrm{core}}+
\frac{8cA_Y}{D_Z}P_{1,\mathrm{core}}+
\frac38P_{0,\mathrm{core}}+
2\rho_*R_{0,\mathrm{core}}
\right]=\frac{3Z}{8}+o^1(1).
}
\tag{28}
$$
新 history 截断对这一行的误差有明确界 $CM^2/R$；
再加(26)(27)已付的 $o^1(1)$ 和最后 $o_\delta^1(1)$。
原等待以及任何后来为支付 $T_1$ 而产生的 $O(M^{-1})$ 参数移动，
全在同一个 $M\int zw\,dz$ 中准确消去。
这正是不能先取旧根的 $S_1$ 常数、再单独相加回路成本的原因。

在原 $P_0=P_1=0$ 极限分支上，
$$
C_0=\frac{3cA_YZ^3}{4g_0}=\frac{3Zg_2}{16g_0}>0,
\qquad C_S=\frac{3Z}{8}-2\rho_*C_0.
\tag{29}
$$
本稿不需要也不宣称 $C_S>0$。

## 6. 同一个大中心给正确的双回路锥条件

在同一冻结 profiles 上，令 $P(f,f)=J((f'')^2)$。
R552(4)(8)及原 $R_o$ 算子给
$$
R_o=\Omega P+O_{\rm op}(1),\quad
Z_o=\Omega^3P+O_{\rm op}(\Omega^2),\quad
Y=-\Omega^4P/4+O_{\rm op}(\Omega^3),
$$
$$
I_{2,x+\Omega}=\Omega^2I_0+O(\Omega),\qquad
\mathcal Q_0(P)=-I_0(P\Delta,P\Delta)/2<0.
$$
因此两个复合次序各自展开为
$$
D_R=\frac{\Omega^7}{4}\mathcal Q_0(P)+O(\Omega^6),
\quad
D_Z=\frac{\Omega^9}{4}\mathcal Q_0(P)+O(\Omega^8),
$$
$$
\rho_*=\Omega^{-2}(1+O(\Omega^{-1})),\qquad
\frac{g_2}{g_0}=\frac{Q_2(Y)}{Q_0(Y)}
=\Omega^2(1+O(\Omega^{-1})).
\tag{30}
$$
于是，使用 R564 的 $H_-=q_-/\Omega$，
$$
\boxed{
C_S+2H_-^2C_0
=\frac{3Z}{8}
\left[1+(H_-^2-\rho_*)\frac{g_2}{g_0}\right]
=\frac{3Z}{8}\{q_-^2+o_{\Omega}(1)\}>0.
}
\tag{31}
$$
先固定 $H_+$、$H_0$、profiles，再一次选充分大有限 $\Omega$，
可同时保 R550/R552 和 R564 的所有旧严格号及(31)。
这不是在一条已经冻结 $\chi$ 的词中改中心。
选完 $\Omega$ 后，后面全部常数固定，即使它们随这个已选大中心很大或很小，
也只在随后取 $R$ 时支付。

## 7. 两个真实长快回路及完整费用

采用 R564 已支付的顺序：core 后真实下降到 $H_+$，做正侧回路，
用原完整加速度系统跨过 $B=0$ 到 $H_-$，做负侧回路。
保每次真实 incoming 的 $A,T$、$j$、全部桥和四个末端内控。

这次各自取独立长度
$$
L_+=\ell_+\sqrt R,\qquad L_-=\ell_-\sqrt R,
\qquad \varepsilon=R^{-3/4}.
\tag{32}
$$
两个 $\ell_\pm$ 在固定严格正盒内；不再使用 R564 的共同
$M^{-1/4}$ 长度因子。
令
$$
c_j=C_k(H_j,0),\quad \omega_j^2=c/c_j>0,
\quad \beta_j=B(H_j,0)/(2c_j),\qquad \beta_+>0>\beta_-.
$$
仍使用固定紧支撑 $\psi$，$I_m=\int(\psi^{(m)})^2>0$，
$$
\psi_L=\sqrt L\,\psi(\tau/L),\quad
D=\psi_L'',\quad f_j=-(\psi_L''+\omega_j^2\psi_L)/\beta_j.
\tag{33}
$$
因此 $D''+\omega_j^2D=-\beta_j f_j''$ 准确成立。

R559 §4–5 的原完整 history 能量证明和 R564 的两侧版本仍适用：
$$
\sigma=\varepsilon\sqrt L=O(R^{-1/2}),\quad
a_R=M/R^{3/2},\quad g_R=M/R^2,
$$
$$
\sigma+a_RL+g_RL^2+L^{-2}
=O(R^{-1/2}+M/R)\longrightarrow0,
$$
$$
L(a_R\sigma+\sigma/L+\sigma^2)\longrightarrow0.
\tag{34}
$$
它们正是原长区间能量和真实因果核使用的小量。
频率 $\omega_j^2$ 固定正，$\beta_j$ 固定非零，符号不影响能量证明；
四末控的真实 Jacobian 由 R564 原方程导数支付。
原 $-M_2\circ A_{\rm in}$、速度面积、原势及三次速度全留在演化内。

记
$$
C_{1j}=\frac{\omega_j^4I_1}{8H_j^4\beta_j^2}>0,
\quad C_{2j}=\frac{\omega_j^2I_2}{8H_j^4\beta_j},
\quad C_{3j}=\frac{I_3}{4H_j^2}>0,
$$
$$
\mathfrak q_j=C_{2j}/C_{1j},\quad r_j^{\rm loop}=C_{3j}/C_{1j},
\qquad \mathfrak q_+>0>\mathfrak q_-.
\tag{35}
$$
此处 $\mathfrak q_-$ 与高度比例 $q_-$ 是不同常数。
选择两个正幅值
$$
a_+^2=X/(2C_{1+}),\qquad a_-^2=X/(2C_{1-}),\quad X>0.
\tag{36}
$$
每条回路原完整成本于共同参数盒上满足
$$
\begin{aligned}
\delta R^{3/2}\Delta R_1&=X/2+o^1(1),\\
\frac{\delta R^{3/2}}M\Delta T_1&=-H_j^2X/(2M)+o^1(M^{-1}),\\
\delta R^{5/2}\Delta R_0&=b_j+o^1(1),\qquad
b_j=\frac{X\mathfrak q_j}{2\ell_j^2},\\
\delta R^{5/2}\Delta S_1&=-2H_j^2b_j+o^1(1),\\
\frac{\delta R^{7/2}}M\Delta S_0&=
-\frac{Xr_j^{\rm loop}}{2M\ell_j^4}+o^1(M^{-1}).
\end{aligned}
\tag{37}
$$
新增 $p$ 费用是原静态 $O(C_R\delta L)$；三条 $p$ 没有
速度二次项。有限下降和开放段为真实 $O(C_R)$，统一最后支付。

跨 $B=0$ 的带宽仍取 R564 的 $\epsilon_R=R^{-15/8}$、
快带长度 $\sqrt R$。其八矩速度费用是
$O(\epsilon_R^2/\delta)$，在最细 $S_0$ 归一后为
$O(R^{-1/4}/M)$，在本稿 $S_1,R_0$ 归一后为
$O(R^{-5/4})$。两侧长桥的实际费用 $C_R$ 继续由最后 $\delta$ 支付，
不是把未知 $C_R$ 并进这些纯 $R$ 小量。

## 8. 同一原端图中的八个准确零

首先保原最后高尾事件参数 $v$。把全部后继的真实 $P_2$
一并带入 R559(43)/R564 的停止图，得到唯一小光滑函数
$$
v=v(\theta,X,\ell_+,\ell_-)
$$
使总 $P_2=0$。其在固定 $R$ 后的大小和全部一阶导数可由最后
$\delta$ 压到本稿每个归一尺度以下。因此先在 $z=0$ 写的
(21)–(28)代入实际小 $v$ 后仍成立。

定义原总累计的准确线性组合
$$
\widehat S_1=S_1+\frac{8cA_Y}{D_Z}P_1+\frac38P_0+2\rho_*R_0.
\tag{38}
$$
在 $P_1=P_0=R_0=0$ 处，$\widehat S_1=0$ 就是原 $S_1=0$。
不是添加新的松弛条件。

七个剩余实际参数为
$(\ell_1,\ell_2,\ell_3,\xi,X,\ell_+,\ell_-)$。
读取同一全词的七维端图
$$
\mathcal F=\left(
\frac{\delta R^{5/2}}M P_1,
\delta R^{5/2}P_0,
\frac{\delta R^{3/2}}M T_1,
\frac{\delta R^{7/2}}M S_0,
\delta R^{3/2}R_1,
\delta R^{5/2}R_0,
\delta R^{5/2}\widehat S_1
\right).
\tag{39}
$$
R563(23)、新(28)及完整(37)给整个共同参数盒上的 $C^1$ 极限
$$
\mathcal F^\infty=
\left(
F_1,F_0,F_t,F_s,
-\frac{\mu_0}{8\xi}+X,
C_0(\theta)+b_++b_-,
\frac{3Z}{8}-2(H_+^2-\rho_*)b_+-2(H_-^2-\rho_*)b_-
\right),
\tag{40}
$$
其中
$$
\begin{aligned}
F_1&=-\frac{D_Z}{2c}
\left(\frac{Z^2\mu_2}{16}-\frac{\mathfrak bZ^3}{24}\right),\\
F_0&=Z-\frac{g_0\mu_2}{6c\xi},\\
F_t&=\frac{\mathfrak bZ}{4}-\frac{\mu_0}{8},\\
F_s&=\frac{A_Y^2Z^4}{4}\left(\frac{2\mathfrak bZ}{5}-\mu_4\right).
\end{aligned}
\tag{41}
$$
原等待与回路 $\Delta T_1$ 造成的参数位移在实际(39)始终存在。
特别，不能把 $O(M^{-1})$ 的 $T_1$ 归一费用直接忽略后，
再读取未作(38)消项的原 $\delta R^{5/2}S_1$。
(28)使(40)对整盒成立，才解决这个问题。

前四行的正根满足
$$
\mu_0=2\mathfrak bZ,\qquad
\mu_2=2\mathfrak bZ/3,\qquad
\mu_4=2\mathfrak bZ/5,\qquad
\xi_*=g_0\mathfrak b/(9c).
\tag{42}
$$
节点 $(1,1/2,1/4)$ 的正权比例为
$(107,440,128)/675$，乘总质量 $2\mathfrak bZ$。
三个矩的 Vandermonde 可逆，$\partial_\xi F_0>0$，
所以这个四维根简单。

再取
$$
X_*=\mu_{0,*}/(8\xi_*)>0.
$$
令 $C_0,C_S$ 取(29)的根上值。后两行要求
$$
b_+^*=\frac{C_S+2H_-^2C_0}{2(H_+^2-H_-^2)}>0,
\qquad b_-^*=-C_0-b_+^*<0.
\tag{43}
$$
正号正是(31)，而 $H_+>H_->0$ 已由初选支付。
因此
$$
\ell_{+,*}^2=\frac{X_*\mathfrak q_+}{2b_+^*}>0,
\qquad
\ell_{-,*}^2=\frac{X_*\mathfrak q_-}{2b_-^*}>0
\tag{44}
$$
都有限且严格正。

(40)的 Jacobian 具有 $4+1+2$ 下三角块。
第一块已述可逆，第五行对 $X$ 导数为1。
末块由
$\partial_{\ell_j}b_j=-2b_j/\ell_j\ne0$ 及
$$
\det\begin{pmatrix}
1&1\\
-2(H_+^2-\rho_*)&-2(H_-^2-\rho_*)
\end{pmatrix}=2(H_+^2-H_-^2)>0
\tag{45}
$$
可逆。所有解都取于同一个原端图，不分别选七条不同路径。

先固定以(42)(44)为内点的正参数盒，再取大有限 $R$，
最后一次取统一小 $\delta$，准确付全部有限桥、规范依赖和停止余项。
稳定简单零/有限维 IFT 遂给实际参数点，使(39)全部为零。
连同先付的 $P_2=0$，得到
$$
\boxed{P_0=P_1=P_2=T_1=R_1^y=S_1^y=S_0^y=R_0^y=0.}
\tag{46}
$$
原 trace 关系同时使 $T_0=0$，所以整原第二矩阵
$\mathsf m=0$，$A=\Phi_{\mathsf m}=0$。
全矩阵为零与平移 profile 坐标无关。

## 9. 所得范围与继续接口

在上述证明范围内，(46)由同一 R521 母、一个固定 $\chi$、
从原零 history 出发的一条有限光滑受约束实际词取得。
全相位第四 ruling 沿词恒为零；完整第三 incoming、第三面积、势和
有序交叉始终实际演化。

第三总值通常不为零。当前末段沿 R564 的真实反馈 germ 接入，
不能因四个端值为零就断言 scalar 的全部奇 jets 为零。
因此本稿到这里也没有自动调用 R526 的反射完成规则。
后继要在同一八矩端图中付出真正 even germs，才可把 R526 的
$PP^R$ 接成同 $\chi$ 的真实第二/第三返回词。
R526 已说明即使该步骤成功，pose 与完整第四 characteristic period
仍是另外的实际条件；课题最终目标尚未完成。

### 直接来源

- R73：原全八矩、真实水平式、第三有序演化；
- R521：同母库、原全相位 ruling、$C_k$ 非退化；
- R537、R544：完整第三速度势变换、真零 history 快准备、真实反馈；
- R550、R552：饱和前缀、两个复合次序、原全部慢时钟与总变差；
- R559：增长快区间的完整 history 能量、法向速度精度和真实末控；
- R562：准确 S1/R0 表及 core R0 细尺度；
- R563：第三真实低尾与四个 core 原端图；
- R564：同一规范穿过耦合零的真桥、负耦合侧真实回路及费用。
