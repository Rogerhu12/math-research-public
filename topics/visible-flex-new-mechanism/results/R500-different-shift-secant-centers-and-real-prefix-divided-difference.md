# R500：异平移正割中心的共同规范差商与真实三中心前缀障碍

日期：2026-11-16。**完整原式纸证；没有执行新的 profile、积分、符号、rank、几何或优化计算。**

[R494](R494-complete-secant-pairing-and-real-two-center-source-incompatibility.md) 的双中心不变量要求两条真实正割段使用相同的 $\omega$。若允许不同 $\omega$，两个中心之间仍残留一个对共同第二规范的线性项。本稿把这个项准确消掉：三个真实中心的二阶差商同时杀掉任意共同规范的两个系数。它对任意紧 profiles 成立，不使用偶母；非零 $P$ 前缀见证只另用原三矩合法性、严格不交 rank-one 表示和已付全 $W$ 外矩。

原 R70 的正长度有限矩阵桥可以实现相应中心矩阵。因而这里给出的不是任意形式 source，而是一类真实路径不能同时通过三个局部完整 ruling 的必要障碍。它不排除全部路径，也不把各段之间的真实桥当成已满足 ruling。后文只保留一个有限多中心推论，供实际路径设计识别应准确配平的前缀量。

## 1. 原场、同一个规范与各中心的完整奇行

固定同一个物理区间 $I$、原右锚和真实圆
$$
 \phi_\theta=f\cos\theta+g\sin\theta,\qquad
 D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
 \tag{1}
$$
所有外层紧输入在同一双 collar 平零。假设原三矩圆合法，所以每个 $E\in\mathcal E_8$ 的 $ED_\theta$ 都是同 collar 真紧；不能把单个微包的二次输出当成左紧。

同一实际路径包含 $N$ 个标记正割小段，每段实际包含其中心 $s_j^*$。在第 $j$ 段，
$$
 k=0,\quad \omega=\omega_j,\quad
 h=H_j\sqrt{1+v_j^2},\quad (v_j)_s=1+v_j^2,\quad
 v_j(s_j^*)=0,\quad H_j>0 .
 \tag{2}
$$
$\omega_j$ 可以不同。全词仍沿同一个原方程
$\omega_s=k_s/(2h)$ 演化；不在各段重置 $\omega$。

记实际中心二阶历史为
$$
 A_j=\Phi_{\mathsf m(s_j^*)},\qquad
 A_j-A_i=\Phi_{\int_{s_i^*}^{s_j^*}M_{\rm raw}(s)\,ds}.
 \tag{3}
$$
固定任意一个全局允许的第二规范 $w_\theta$ 及第三规范
$\chi_\theta$。真实 second characteristic 为
$$
 q_{j,\theta}^*=w_\theta+A_jD_\theta .
 \tag{4}
$$
所有特解、seed、incoming 和端口条件均指这个同一个全局选择。

[R488](R488-real-secant-height-patches-and-complete-same-gauge-ruling.md)
的完整 affine-field 证明及 R494(18)–(24) 给出该段的完整 ruling
$$
 K_{j,\theta}(s)=
 \frac{a_{j,\theta}+b_{j,\theta}v_j+c_{j,\theta}v_j^2}{h(s)},
 \qquad
 b_{j,\theta}=\beta_\theta^{\omega_j}(q_{j,\theta}^*).
 \tag{5}
$$
其中任意真实第三 incoming、第三齐次规范及完整 second 平方对
$v_j$ 都为 even，所以没有被漏到 $b_{j,\theta}$ 之外的自由 odd 项。

原完整 pairing 是
$$
 \beta_\theta^\omega(\eta)
 =\frac12\int_I\eta\left[
 ((x+\omega)\phi_\theta'-\phi_\theta)\phi_\theta''''
 +2(x+\omega)\phi_\theta''\phi_\theta'''
 -(f'-(x+\omega)f'')f'''
 \right]dx .
 \tag{6}
$$
它对任意真紧 $\eta$ 成立，不要求 $\eta\in\ker L_f$，不借原十三行，也不要求 profiles 偶对称。特别，
$$
 \beta_\theta^\omega=B_{0,\theta}+\omega B_{1,\theta},
 \tag{7}
$$
这里 $B_{0,\theta},B_{1,\theta}$ 是同一个紧输入空间上的真实线性泛函，均不依赖各段高度 $H_j$。本稿不把它们在整个输入空间上等同于原十三行中的任何组合。

## 2. 异 $\omega$ 的精确共同规范商

**定理 1。** 对任意实权 $\lambda_1,\ldots,\lambda_N$，若
$$
 \sum_j\lambda_j=0,\qquad
 \sum_j\lambda_j\omega_j=0,
 \tag{8}
$$
则对全部相位和任意同一个允许的全局规范，
$$
 \boxed{\displaystyle
 \sum_j\lambda_j b_{j,\theta}
 =\sum_j\lambda_j\beta_\theta^{\omega_j}(A_jD_\theta).
 }
 \tag{9}
$$

证明：把(4)代入(5)。$w_\theta$ 的总贡献由(7)恰为
$$
 \left(\sum_j\lambda_j\right)B_{0,\theta}(w_\theta)
 +\left(\sum_j\lambda_j\omega_j\right)B_{1,\theta}(w_\theta)=0.
$$
没有分部积分、没有假定某个 source 已有紧逆，也没有丢弃任何 primitive 常数。其余项就是(9)。证毕。

若同一个实际最终成本先改变了 period source，重新选出的共同
$w_\theta$ 仍按上式全部消去。因此(9)也消掉该 source 在所有这些中心共同产生的贡献。若原 period 无解，则全路径当然尚未解决；本定理并不为了书写(9)而假定已经得到特解。

当 $\omega_1<\omega_2<\omega_3$ 时，取
$$
 (\lambda_1,\lambda_2,\lambda_3)
 =(\omega_3-\omega_2,-(\omega_3-\omega_1),\omega_2-\omega_1).
 \tag{10}
$$
条件(8)成立，故三个完整 ruling 同时为零必须满足
$$
 \boxed{\begin{aligned}
 0={}&(\omega_3-\omega_2)\beta_\theta^{\omega_1}(A_1D_\theta)\\
 &-(\omega_3-\omega_1)\beta_\theta^{\omega_2}(A_2D_\theta)
 +(\omega_2-\omega_1)\beta_\theta^{\omega_3}(A_3D_\theta)
 \quad\text{对全部 }\theta .
 \end{aligned}}
 \tag{11}
$$
这是异平移中心之间的一个完整二阶差商。它没有把各
$\omega_j$ 当成同一个值，也没有逐段选取不同的 $w_\theta$。

若 $A_j=A_*$ 对所有中心相同，则(11)准确为零。这个事实只支付相对 odd 门；共同的 odd source 和每段两个 even 门仍在。

## 3. 原 $P$ 前缀的严格值不需要偶母

令
$$
 P(u,u)=J((u'')^2).
$$
采用原严格不交 rank-one 圆
$$
 f=\sum_i a_i u_i,\quad
 \phi_\theta=\sum_i c_i(\theta)u_i,\quad
 d_i=a_i^2-c_i^2,\quad
 c_i=a_i\cos\theta+b_i\sin\theta .
 \tag{12}
$$
原三矩中的零阶合法式给
$\sum_i d_i\int(u_i'')^2=0$，所以完整 $PD_\theta$ 真紧。

R494(29)–(34) 已保留每个 $P_i$ 的左常数和完整有序 suffix。全部常尾项最后准确合成
$$
 \frac18\left(\sum_i d_i\int(u_i'')^2\right)^2=0.
$$
在此之后，完整结果为
$$
 \beta_\theta^\omega(PD_\theta)
 =\sum_i\left[
 -\frac{a_i^2d_i}{2}\int u_i'(u_i'')^3
 +\frac{d_i(3a_i^2+c_i^2)}{12}
      \int(x+\omega)(u_i'')^4
 \right].
 \tag{13}
$$
本稿不重新计算这个已付原式，也不把它简化为仅 principal。

已付全 $W$ 外矩在同一个库上给
$$
 \sum_i c_i^2d_i\int(u_i'')^4=0 .
 \tag{14}
$$
因此
$$
 \partial_\omega\beta_\theta^\omega(PD_\theta)
 =\frac14\sum_i d_i^2\int(u_i'')^4 .
 \tag{15}
$$
在 $\theta=\pi/2$，原同圆身份进一步给
$$
 G:=\partial_\omega\beta_{\pi/2}^\omega(PD_{\pi/2})
   =\int_I(g'')^4>0.
 \tag{16}
$$
严格号用的是非退化 $g$ 与双零 collars。式(13)–(16)都不需要
$\int u_i'(u_i'')^3=0$，故没有用母的偶性。

定义已有实际积分确定的唯一实数
$$
 \omega_{\rm blind}
 =-\frac{\beta_{\pi/2}^0(PD_{\pi/2})}{G}.
 \tag{17}
$$
于是
$$
 \beta_{\pi/2}^\omega(PD_{\pi/2})
   =(\omega-\omega_{\rm blind})G.
 \tag{18}
$$
这不是一个新的数值观测；它是(7)(16)的准确写法。

## 4. 真正三个中心的非零前缀不变量

指定中心历史
$$
 A_1=A_3=A_*,\qquad A_2=A_*+tP .
 \tag{19}
$$
由于(7)(8)，公共 $A_*$ 在(11)中准确消去。由(9)(10)得到
$$
 \sum_{j=1}^3\lambda_j b_{j,\theta}
 =-(\omega_3-\omega_1)t\,
        \beta_\theta^{\omega_2}(PD_\theta).
 \tag{20}
$$
在 $\omega_2\ne\omega_{\rm blind}$ 时，
$$
 \boxed{\displaystyle
 \sum_{j=1}^3\lambda_j b_{j,\pi/2}
 =-(\omega_3-\omega_1)t
   (\omega_2-\omega_{\rm blind})\int(g'')^4 .
 }
 \tag{21}
$$
故 $t\ne0$ 时，三个实际正割小段不可能同时满足完整
$K_\theta(s)=0$，无论采用哪个同一个全局允许规范。

这条结论覆盖不同的 $H_j$、不同的 $\omega_j$ 以及一般非偶的紧输入。它不宣称一个任意非偶 profile 已经满足其余原母条件：具体非零应用只要求实际输入满足本节逐项列出的三矩、rank-one 和全 $W$ 外矩前提。现有从起点库提供其一个已付实例。

### 4.1 原 R70 桥使(19)成为实际目标

[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)
§§1–2 允许任意指定两端 frame、正 $h$、常值
$(k,h,\omega)$ germs，以及任意有限无迹八矩目标。桥满足原
$\omega_s=k_s/(2h)$，以正长度真实圆和连接构成；目标在固定紧盒内时，可先固定一个有限圈数得到光滑截面。

按 [R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md) §10 实施(19)：先固定各短正割段及其向常值 collars 的真实短连接；把每个入口至中心、中心至出口的原 $M_{\rm raw}$ 积分全部保留，再从相邻桥的矩阵目标中扣除。因此所付的是实际中心的 $A_j$，而不是仅把三座连接桥的低导数积分写成形式目标。

$t<0$ 使用原真实桥的负矩阵目标，绝不表示负时间。有限参数盒内所有额外桥、圈数、时长、scalar/frame 端数据和原成本基准均固定或按该截面光滑依赖。对(19)的实际实现不需要给 profiles 单独求新的第四响应。

### 4.2 共同窗口与从起点选择的次序

R70 的共同物理窗口不能偷换成任意预冻结窄窗口。本稿的真实非零例采取其合法次序：

1. 固定有限个正割 germs、三条不同的 $\omega_j$、有限 $t$ 盒和上述 profile 无关的 $P$ 矩阵桥；
2. 在所有桥的同一个实际 $\omega(s)$ 包络确定后，选择共同紧区间，使 $x+\omega(s)>0$ 有统一余量；
3. 在该窗口内从起点选原合法 rank-one / 全 $W$ 外矩圆及其完整布局。

[R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md)
§§7–9 明确保留这些布局的合法共同平移，并要求全部路径、参数盒、桥与窗口先于有限 profile 根选择。若需要避开(17)的单值，可以在从起点布局中预留一个小的共同平移参数。对
$u_i^c(x)=u_i(x-c)$，原同锚式给
$$
 \beta_{\pi/2}^\omega(PD^c_{\pi/2})
   =\beta_{\pi/2}^{\omega+c}(PD_{\pi/2}),
 \qquad
 \omega_{\rm blind}(f^c,g^c)=\omega_{\rm blind}(f,g)-c .
 \tag{22}
$$
原合法矩和全 $W$ 外矩在此共同平移下保持，所以最多一个
$c$ 被排除。选择在同一个合法开区间完成，然后才冻结库。

这里没有移动一套旧已冻结库并声称它的其它数值或二十目标记录不变。若还需这些其它 profile 目标，应按 R480 的从起点同点构造把所选布局一起纳入；本定理的障碍本身只消费明确列出的三矩与全 $W$ 外矩。

### 4.3 后置成本不能更改标记前缀差

在所有标记中心之后，可接原 R70 矩阵复位桥，使总 $M=0$。若还需指定总第三 period，可使用原 R80 的零矩真实第三块。它们的完整第四 $V$、incoming、桥基准和真实圈数仍必须计入最终问题。

这些后置块不改变(3)(19)。即使它们改变最终 source 并迫使重新选择共同 particular，(9)仍杀掉这个共同 $w_\theta$。它们不能改变(21)。这不表示后置块的内部 ruling 自动成立，更不表示总 $M/T/V$、原十三行或闭嵌入要求都已解决。

## 5. 有限多中心的真实相对坐标

此节只给(9)的一个实际有限参数推论，不重新计算旧控制秩。

取 $N\ge3$ 个互异 $\omega_j$，并指定
$$
 A_1=A_N=A_*,\qquad A_j=A_*+t_jP\quad(2\le j\le N-1).
 \tag{23}
$$
定义原完整 odd 系数的端点仿射残差
$$
 \mathcal R_{j,\theta}
 =b_{j,\theta}
 -\frac{\omega_N-\omega_j}{\omega_N-\omega_1}b_{1,\theta}
 -\frac{\omega_j-\omega_1}{\omega_N-\omega_1}b_{N,\theta}.
 \tag{24}
$$
由(9)，
$$
 \boxed{\mathcal R_{j,\theta}
     =t_j\beta_\theta^{\omega_j}(PD_\theta).}
 \tag{25}
$$
若内部各 $\omega_j\ne\omega_{\rm blind}$，则在同一个相位
$\pi/2$，真实参数到这些相对残差的映射准确为
$$
 (t_2,\ldots,t_{N-1})
 \longmapsto
 \bigl(t_j(\omega_j-\omega_{\rm blind})G\bigr)_{j=2}^{N-1}.
 \tag{26}
$$
这是一个对角可逆的有限实线性映射。R70 按顺序实现所有目标，
给同一个实际有限桥族及同一个共同窗口；不是逐中心重新挑选规范或分别实现后拼成一个虚构解。

反过来，设计者可以准确取全部 $t_j=0$，从而消掉这一组相对门。故(26)同时说明这些门不是不可避免的拓扑障碍，而是实际 prefix 设计必须处理的独立相容量。共同 odd 值、每个 even 值、所有非正割连接段的完整 $K$ 及原 period/十三行仍不能由此消去。

## 6. 当前已付边界与后继正向问题

本稿的严格新增项是：

- 任意紧输入下，不同 $\omega$ 中心的共同规范只占
  $\operatorname{span}\{1,\omega\}$ 两个参数；
- 三中心二阶差商准确杀任意共同 $w_\theta$、其整个 source，以及全部第三 incoming 的可能影响；
- 原正长度有限矩阵桥可真实实现非零差商，值由(21)完整给出；
- 同一个实际多中心桥族具有(26)的准确相对坐标，而共同规范和其余完整成本仍保留。

它既没有求解一个非对称 whole-path，也没有排除所有这样的路径。后继正向构造应优先找实际非恒前缀落在这些差商的共同零集，并同时处理唯一规范下的完整 even 和非正割段方程；不能只继续增加障碍数目，也不能把每个 patch 的 Gram 解当成同一个全局 $\chi_\theta$。
