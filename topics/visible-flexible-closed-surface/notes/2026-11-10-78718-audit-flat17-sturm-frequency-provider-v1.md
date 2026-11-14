# 固定 flat17 的全周期 Sturm 传播：完整独立审查

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
可信度：**原稿全文数学审查通过；有限符号/严格有理检查由审者实际重跑。**
审者未参与本稿的变量变换、正则化或估计构造，也未参与 root/geometric 正在发展的后续中央普通源证明。本审不运行数值 PDE，不调主 M14 参数。

## 1. 冻结对象和准确结论

被审对象为 [geometry-flat17-sturm-frequency-provider-v1.md](2026-11-10-78718-geometry-flat17-sturm-frequency-provider-v1.md)，14,295 B，SHA256
`68962bac35e0a6969ce159b17e0b7754698cffc816248ddfb596c35a7a93f5db`。
原稿 §§1–7 全文由 `0d52c3/4a0a9d` 读完。下文独立覆盖完整线性化、实际全周期和符号分区、所有正变差估计、两个方向的传播、全模重构、均值、逐模散射、普通源和坐标换算。

配套 [78718-geometry-flat17-sturm-frequency-check.py](../scripts/78718-geometry-flat17-sturm-frequency-check.py)，5,338 B，SHA256
`83735a6881a9934b8a0611ddef302bdfa0e3ce6844fbb92a997bc6ac4ec215ee`，本人已 `5dbe21` 全文读完并真实执行。源码与原稿身份另由 `ecc2da` 实核。

**通过的命题**是固定解析 Target 的旋转背景线性化：精确无零阶势 Sturm 化；整个第一 outward 周期上全部 Fourier 模的真实基本解；物理变量的 $20\langle j\rangle^5e^{|j|\Omega}$ 界和 $\Omega(T,0)<459/1000$；两个实际外区的 $6\langle j\rangle^2$ 无指数角带损失界；精确通量及单位范数的两端口齐次散射；相应解析类普通源变常数公式和坐标范数换算。

这仍是线性背景模块。没有证明任意低正则端口数据的无角带损耗内部/普通源估计，没有支付原尾 Robin 反馈逆、当前非径向数值候选的线性化、非线性扰动、帽、H、幅度/reach或闭面。以下没有把未来中央证明的预期结论写成本稿已完成结果。

## 2. 从完整非线性系统独立线性化

已审多项式 Gauss–Codazzi 系统为

$$
b_s=\frac{bb_u-Qpp_u}{a}-\frac ca b(1+b^2-Qp^2),
\quad
p_s=\frac{bp_u-pb_u}{a}-\frac ca p(b^2-Qp^2),
$$

其中 $c=a',Q=aa''$。背景为 $b=0$、$\bar p=(1-c^2)^{-1/2}$。置 $b=\tau\beta$、$p=\bar p+\tau\pi+O(\tau^2)$，由于背景不依赖角，逐项的一阶部分为

$$
\begin{aligned}
\beta_s&=-\frac{\bar p}{a}Q\pi_u
-\frac ca(1-Q\bar p^2)\beta+f_1,\\
\pi_s&=-\frac{\bar p}{a}\beta_u
+\frac{3cQ}{a}\bar p^2\pi+f_2.
\end{aligned}
\tag{A1}
$$

不存在被省略的交叉零阶项。$f_1,f_2$ 是此坐标下实际加入的二分量源，并非未经转换的另一 Darboux column。

由 $\bar p'=ca''\bar p^3=(cQ/a)\bar p^3$ 和 $\alpha=\bar p/a$，确有

$$
\frac{\alpha'}\alpha=-\frac ca(1-Q\bar p^2),
\qquad 3\frac{\bar p'}{\bar p}=\frac{3cQ}{a}\bar p^2.
$$

故 $x=\beta/\alpha$、$y=\pi/\bar p^3$ 完全消去两个零阶项，得到

$$
x_s=-Q\bar p^3y_u+f_1/\alpha,
\qquad y_s=-\frac1{a^2\bar p}x_u+f_2/\bar p^3.
$$

令 $H=1/(a^2\bar p)>0$、$dr=Hds$，再除以 $H$ 即有

$$
x_r=-Vy_u+g_1,\qquad y_r=-x_u+g_2,
\quad V=a^2Q\bar p^4=\frac{a^3a''}{(1-c^2)^2},
\tag{A2}
$$

$$
g_1=a^3f_1,\qquad g_2=a^2\bar p^{-2}f_2.
\tag{A3}
$$

这是真正全周期递增坐标中的恒等变换，未使用高频近似。对连续 $V$，每个整数 $j$ 的一阶 ODE 基本解实际存在。

齐次时 $y_{rr}=Vy_{uu}$，即 $y_j''+j^2Vy_j=0$。有源时右端为 $-ijg_{1,j}+\partial_rg_{2,j}$，但仅在分布意义使用。对一般 $L^1_r$ 源应保留 (A2) 变常数；无需给 $g_2$ 多加径向导数。$j=0$ 的一阶系统仍保留两个均值：齐次时传递恰为 $I$，有源时分别积分两个源分量。

## 3. 真实符号区间和剖面结构

本稿使用同一解析 Target：五个主程序参数各按其实际 binary rational 解释，并由精确表达式 $T_v=\delta/[v(1-\varepsilon)]$ 算物理时长。没有用替换度量或浮点求值曲线作证明。原 `turn_ramp/ramp/FlatFlow.prefix_profile` 和 `Target.a_prefix_poly` 的具体公式已在本人的完整 ramp 审稿直接核过；本稿采用同一冻结公式。

第一上升阶段的 $a'=v_uw$：开始 ramp 有 $a''\ge0$，随后平段为0，末端减速 ramp 有 $a''\le0$。下降阶段的 $a'=-v_dw$：开始 ramp 有 $a''\le0$，随后平段为0，末端返零 ramp 有 $a''\ge0$。因此准确分界为

$$
s_-=(1-\varepsilon)T_u,
\qquad s_+=T_u+\varepsilon T_d.
$$

整个 $[0,s_-]$ 与 $[s_+,T]$ 的 $V\ge0$，中央 $[s_-,s_+]$ 的 $V\le0$。在 $s=T_u$ 两个负 ramp 相接于 $V=0$，不改变负号区；所有二次零点、加速度平台和开放 $V=0$ 段都保留，未换成简单根模型。

每个 ramp 上 $v=|a''|$ 为一个正固定倍数的加速度型 $d(t)$。两端分别是 $3z^2-2z^3$ 的上升和反射下降，中间是平台。因此 $v$ 从0单调升至峰值、平台、再单调回0；反向走也只有一次上升。有限分段多项式及端点匹配保证 $V$、$|V|$ 绝对连续；正的 $H$ 作坐标变换保留这一性质。

$a$ 在第一阶段从1升至 $1+\delta$、第二阶段降回1。$\bar p$ 依次为 $1\to P_u\to1\to P_d\to1$，故

$$
\operatorname{Var}_+(\log a)=\log(1+\delta),\qquad
\operatorname{Var}_+(\log\bar p)=\log P_u+\log P_d.
\tag{A4}
$$

相应总负变差相同，因为周期端值相同。这里正变差是导数正部的积分，不是函数正部的导数。

## 4. 所有统一常数的来源

置 $A=43/40,P=51/50$。原参数的严格 binary 包含给

$$
1\le a<A,\quad 1\le\bar p<P,\quad |a''|<3/4,
\quad T<3/2.
$$

$\bar p<P$ 来自 $P^2[1-(181/1000)^2]>1$。周期上界不靠浮点加法：用
$\delta<3/40$、$1-\varepsilon>599/1000$、$v_u>169/1000$、$v_d>179/1000$，得到严格有理上界小于 $3/2$。

实际有理比较为

$$
A^3P^4<27/20,\quad A^3<5/4,\quad P^4<11/10,
\quad A^2P<6/5,\quad AP^3<23/20.
$$

写 $\omega=a^3\bar p^4$，则 $|V|=\omega v<81/80=:V_*$。又 $5/6<H\le1$，所以 $R=r(T)<3/2$。

中央物理宽度为 $\varepsilon(T_u+T_d)$。以较小的 $\varepsilon,\delta$、较大的 $1-\varepsilon,v_u,v_d$ 外包，

$$
\varepsilon(T_u+T_d)>
\frac{399}{1000}\frac{9/125}{601/1000}\frac{2000}{181}>\frac12.
$$

乘 $H>5/6$ 后，$r_+-r_->5/12$，上界则由总长 $R<3/2$ 得到。这个真实中央宽度是可以交给未来中央估计的输入，但不单独构成该估计。

## 5. 正则化能量的 Hermitian 部分

对所有整数 $j$，取 $n_j=\sqrt{1+j^2}$、$m_j=1/n_j$、$q_j=\sqrt{|V|+m_j^2}$，$S_j=\operatorname{diag}(1,q_j)$。因 $q_j\ge m_j>0$，整个周期包括 $V=0$ 开段和二次零点都在同一能量中。$W_j=S_jZ_j$ 满足原稿 (18)。

主矩阵乘 $-i$ 后的 Hermitian 部分是由两个非对称非对角元之差产生的 Hermitian 矩阵，其最大特征值绝对值为

$$
\chi_j(V)=\frac{q_j-V/q_j}{2}
=\frac{|V|+m_j^2-V}{2\sqrt{|V|+m_j^2}}.
$$

真实频率系数再乘 $|j|$。若 $V\ge0$，$\chi=m_j^2/(2q_j)\le m_j/2$。若 $V=-z^2$，与 $z+m_j/2$ 比较、乘正分母后，两边非负；平方差正好为

$$
4m_jz^3+m_j^2z^2+4m_j^3z\ge0.
$$

故 $\chi\le\sqrt{V_-}+m_j/2$。对角修正 $\operatorname{diag}(0,q_j'/q_j)$ 的最大特征值是正部，而非必须取绝对值。因此齐次能量几乎处处满足

$$
\frac{d}{dr}|W_j|\le
\left[|j|\sqrt{V_-}+|j|m_j/2+(\log q_j)'_+\right]|W_j|.
\tag{A5}
$$

可从平方范数推该不等式；非零解不会在某点整体为零，零解则平凡。反向路径的主矩阵符号翻转但最大特征值相同，对角项改用负变差。整个论证是有限模实际能量估计，不是 WKB 主项。

## 6. 正变差控制完整覆盖四个 ramp

由于 $q_j^2=\omega v+m_j^2$，几乎处处有

$$
(\log q_j)'_+
\le\frac12(\log\omega)'_+
+\frac12\frac{(v')_+}{v+m_j^2/\omega_{\max}}.
\tag{A6}
$$

证明先用 $(\omega'v+\omega v')_+\le(\omega')_+v+\omega(v')_+$。第一项除分母后至多 $(\omega')_+/\omega$；在 $v=0$ 时原第一项为0，所以不需非法除以零。第二项中 $m_j^2/\omega\ge m_j^2/\omega_{\max}$。所有分母都严格正。

正时间变换使 $\int(h_r')_+dr=\int(h_s')_+ds$，所以用物理 ramp 的单调结构计算合法。每个 ramp 的上升积分恰至多

$$
\int\frac{(v')_+}{v+m_j^2/\omega_{\max}}
\le\log(1+V_*n_j^2).
$$

四个 ramp 给四次该对数。另一方面
$\operatorname{Var}_+(\log\omega)\le3\operatorname{Var}_+(\log a)+4\operatorname{Var}_+(\log\bar p)$。结合 (A4) 并取指数，得到

$$
\exp\int_0^R(\log q_j)'_+dr
\le(1+\delta)^{3/2}(P_uP_d)^2(1+V_*n_j^2)^2
<\frac{99}{80}(1+V_*n_j^2)^2.
\tag{A7}
$$

最后一步用 $A^{3/2}<9/8$ 和 $P^4<11/10$。反向可以直接以周期端点 $q_j(0)=q_j(R)=m_j$ 知总正、负变差相同；任何子区间正变差不超过相应全周期总量。故 (A7) 同时适用于任意两点和两个方向。没有使用会产生 $j^2\int|V'|$ 损耗的粗估计。

## 7. 全周期常数17、20与准确作用量

有 $\|S_j\|\le3/2$、$\|S_j^{-1}\|\le n_j$，因为 $q_j^2\le V_*+1=161/80<9/4$ 且 $q_j\ge1/n_j$。沿任意子区间 $|j|m_j\le1$、长度小于 $3/2$，所以补偿指数小于 $3/4$。

令

$$
\Omega(s,t)=\left|\int_t^s\frac{\bar p}{a}\sqrt{Q_-}\,d\tau\right|
=\left|\int_{r(t)}^{r(s)}\sqrt{V_-}\,dr\right|.
$$

坐标等式由 $H\sqrt{V_-}=\bar p\sqrt{Q_-}/a$ 直接核得。结合能量与 (A7)，

$$
\|T_j^Z\|
\le\frac32n_j e^{3/4}\frac{99}{80}(1+V_*n_j^2)^2e^{|j|\Omega}.
$$

因为 $n_j\ge1$，$1+V_*n_j^2\le(161/80)n_j^2$；又

$$
e^{3/4}<11/5,\qquad
\frac32\frac{99}{80}\left(\frac{161}{80}\right)^2\frac{11}{5}<17.
$$

故实际 $Z$ 传播小于 $17n_j^5e^{|j|\Omega}$。变回 $U$ 的矩阵为
$\mathcal R=\operatorname{diag}(a/\bar p,\bar p^{-3})$，$Z=\mathcal RU$，并有
$\|\mathcal R(s)^{-1}\|\|\mathcal R(t)\|\le AP^3<23/20$。所以

$$
\|T_j^U(s,t)\|\le20\langle j\rangle^5e^{|j|\Omega(s,t)}.
\tag{A8}
$$

$j=0$ 也包含；$Z$ 的均值传递恰为 $I$，而 $U$ 的中间点均值坐标因子没有被误写成 $I$。

负势只在中央两段 ramp。任一 ramp 的 $v=|a''|$ 满足
$v=(v_{\rm speed}/(\varepsilon T_v))d(t)$、$ds=\varepsilon T_vdt$、$\int_0^1d=1$。Cauchy–Schwarz 给

$$
\int_{\rm ramp}\sqrt v\,ds
\le\sqrt{v_{\rm speed}\varepsilon T_v}
=\sqrt{\frac{\delta\varepsilon}{1-\varepsilon}}.
$$

在两负 ramp 分别用 $\bar p\le P_u,P_d$ 和 $a\ge1$，得到

$$
\Omega(T,0)\le(P_u+P_d)\sqrt{\frac{\delta\varepsilon}{1-\varepsilon}}
<\frac{51}{25}\frac9{40}=\frac{459}{1000}.
$$

最后严格根号界来自 $(3/40)(401/599)<81/1600$，不以小数近似的作用量代付。

## 8. 全模解析重构和真实普通源

为明确原稿的共同 Fourier 权，可取

$$
\|U\|_{\sigma,k}^2=\sum_{j\in\mathbb Z}
 e^{2\sigma|j|}\langle j\rangle^{2k}|U_j|^2.
$$

同样逐模证明适用于其它以相同二维模范数定义的常用 Fourier 权范数。对 $0\le t\le s$，因作用量被积非负，
$\Omega(s,t)=\Omega(s,0)-\Omega(t,0)$。故若 $\sigma(s)=\sigma_0-\Omega(s,0)>0$，则
$\sigma(s)+\Omega(s,t)=\sigma(t)$。

对每模实际变常数公式乘权，再用 (A8) 与 Minkowski，得到原稿 (29)，损失完整五次角导数。每模的连续系数 ODE 先已存在；此估计证明 Fourier 和收敛，不是先假定一个完整角解后只给先验界。任何严格较窄的正解析带上，指数余量使全部角导数一致收敛。源可积于相应加权空间给 mild 解；源在相应严格子带拓扑连续时给经典解。

全程没有截断 Fourier 模，也没有删除均值。源进入的是物理 $f$ 的真实变常数式，(A3) 的变换不会凭齐次酉性消掉任何源分量。

## 9. 两个外区的精确两次导数损失

左外区 $a,\bar p$ 均不下降，$\omega=a^3\bar p^4$ 不下降；右外区两者均不增加。沿各外端走向中央时，$\omega$ 均不下降，且从不小于1的值到不大于 $\omega_{\max}$，故任意同外区有向路径的 $\log\omega$ 正变差至多 $\log\omega_{\max}$。反方向的这部分不更大。

每个实际外区只有一个完整的上升—平台—下降加速度 ramp，其余是 $v=0$ 开段。反向也只有一次上升，所以 (A6) 对任意同外区两点只用一次对数积分，得

$$
\exp\int(\log q_j)'_+dr
\le\sqrt{\omega_{\max}}\sqrt{1+V_*n_j^2}
<\frac65\frac32 n_j.
$$

此处 $\sqrt{\omega_{\max}}<\sqrt{27/20}<6/5$；另一个根号由 $161/80<9/4$ 控制。外区 $V\ge0$，所以作用量严格为0。结合两端坐标和补偿指数，

$$
\|T_j^Z(r_2,r_1)\|
<\frac32\frac65\frac32\frac{11}{5}n_j^2
=\frac{297}{50}n_j^2<6n_j^2.
\tag{A9}
$$

这同时覆盖两个方向、全部二次零点及开放平段，不假定严格正势。普通源的 (32) 随实际变常数公式成立；反向时积分理解为所经过区间上的正长度 $L^1$ 积分。原稿没有把 $Z$ 的常数6直接误用于物理 $U$ 而省略坐标因子。

## 10. 通量、SU(1,1)和准确散射消元

令 $B=\begin{pmatrix}0&V\\1&0\end{pmatrix}$、$\mathcal A_j=-ijB$、$J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$。因 $V$ 实，$B^TJ=JB$，故 $\mathcal A_j^*J+J\mathcal A_j=0$；且 trace为0。因此真正基本解满足 $T^*JT=J$、$\det T=1$。

用原稿实正交对称矩阵 $P_0$ 把 $J$ 化为 $J_0=\operatorname{diag}(1,-1)$。对
$\widetilde T=\begin{pmatrix}A&B\\C&D\end{pmatrix}$，由
$\widetilde T^{-1}=J_0\widetilde T^*J_0$ 和二维行列式一的逆式比较，得到

$$
D=\overline A,\qquad C=\overline B,\qquad |D|^2-|B|^2=1.
$$

所以 $|D|\ge1$ 对每模成立，不需另行排除这个特定端口的分母零。解第二行
$z_-(R)=Cz_+(0)+Dz_-(0)$，再代第一行，利用 $AD-BC=1$，得到

$$
\mathcal S_j=\begin{pmatrix}-C/D&1/D\\1/D&B/D\end{pmatrix}.
$$

两列的平方范数均为1，互内积为 $(B-\overline C)/|D|^2=0$，因此确为酉矩阵。$j=0$ 时 $T=I$、$\mathcal S_0$ 是交换矩阵；实系数给 $\mathcal S_{-j}=\overline{\mathcal S_j}$。

在任意给两个端口使用同一正 Fourier 权的加权 Hilbert 空间中，逐模酉性给范数恰一且由 $\mathcal S_j^*$ 给逆，所以是完整酉延拓。它不是仅一个衰减的数值矩阵估计。

但这个边界空间结论不等于任意低正则 incoming 都有同类内部解。足够宽的解析输入可用 (A8) 重构；无角带损耗的全内部估计仍需后续中央分析。本稿已经明确区分，审者不预支后续结果。

## 11. 两源分量的仿射散射和物理单位

有源时完整传递为 $z(R)=\widetilde Tz(0)+w$，其中
$w=P_0\int_0^R T^Z(R,r)g(r)dr$。第二行消元给左 outgoing 多一项 $-D^{-1}w_-$；代第一行给右 outgoing 多一项 $w_+-BD^{-1}w_-$。这与原稿 (37) 完全一致，未丢弃 $g_2$ 或用分布二阶式迫源求导。

每模 $L^1$ 源的该积分是真实有限维积分；全模原始积分可以在已给解析类内使用。其它权下的完整源估计和原尾 Robin 反馈尚未证明，不能由 $|D|\ge1$ 自动推出。

周期两端 $a=1,c=0,\bar p=1$，所以 $Z=U$，端口没有隐藏缩放。对 $L^2$，$g=\operatorname{diag}(a^3,a^2\bar p^{-2})f$、$dr=Hds$，用 $H\le1$、$a,\bar p\ge1$ 得

$$
\|g\|_{L^2_r}\le A^3\|f\|_{L^2_s}<\frac54\|f\|_{L^2_s}.
$$

反向 $U=\operatorname{diag}(\bar p/a,\bar p^3)Z$，矩阵范数至多 $P^3$，且 $ds/dr=a^2\bar p\le A^2P$，故

$$
\|U\|_{L^2_s}\le AP^{7/2}\|Z\|_{L^2_r}<\frac65\|Z\|_{L^2_r},
$$

最后由有理式 $A^2P^7<36/25$。这些是同一变量的真实单位转换，不改变度量、源或边界条件。

## 12. 有限 checker 的全部覆盖和实际重跑

15 个符号检查覆盖两个对数导数、两行线性化、两个源缩放、4个通量矩阵条目、trace、4个散射 Gram 条目。散射 Gram 的最后对角值为 $(1+BC)/(AD)$；等于1所需的 SU(1,1)关系和 det1由 §10 完整数学证明，不以符号程序替代。

23 个 Fraction 检查覆盖五个实际 binary 参数外包、加速度、$\bar p$、周期、全部乘积/根号/坐标常数、中央宽度、作用量、外区6与全周期17/20以及 $L^2$ 常数。程序对 $e^{3/4}$ 用0至18阶的精确有理 Taylor 和，余项从19阶起以相邻比率不超过 $(3/4)/20$ 的几何级数控制；其有理上界严格小于 $11/5$，没有用浮点指数比较。

本人真实执行：

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-geometry-flat17-sturm-frequency-check.py \
  --out notes/2026-11-10-78718-audit-flat17-sturm-frequency-check-01.json
```

真实工具 `2ce6a8` 自然 exit0，15符号、23有理全部通过。输出 [audit-flat17-sturm-frequency-check-01.json](2026-11-10-78718-audit-flat17-sturm-frequency-check-01.json)，1,710 B，SHA256
`e0fce82bc3130307c0a6ff3ea3879ff7583ed798cb22f5bc2019498573ea9fcd`。
0 PDE、0新候选运行。报告与作者确定性内容相同，但本人的真实执行回执为本次 `2ce6a8`，不借作者 `6596c9`。

## 13. 范围核对与最终意见

本稿给的是固定旋转背景下径向系数的精确逐模系统。当前非径向有限候选具有角依赖系数，不再逐模解耦，不能继承这里的 $T_j$ 或常数。support、chart、投影误差、真实源 column 换算、原尾反馈及闭合也不能由本模块自动支付。

两个外区的实际无指数界与中央非正势/宽度是后续内部普通源证明可使用的输入；本审没有参与构造该后续证明，也没有提前把其结果算作已审。主独立数值运行的源码、参数、回执和状态均与本数学审查分开。

**完整独审结论：原稿全部声明在准确范围内通过，无实质订正项。可登记为中间全周期线性传播与端口模块；仍不构成课题完成。**
