# R807 — 原二阶来源的完整投影连接、唯一 primitive 预像与两个单位余行

日期：2026-11-15。**状态：以下原同源连接、有限矩阵恒等式、两个实际单位障碍与全半周期公式已证明。指定负二矩及原三中央的非消失均未由本篇推出。**

本文固定 [R801](R801-original-nonzero-second-e-source-and-complete-negative-two-row.md) 的同一个 $q_N^*$、全部58行和真实 $Z^2$ 来源。所用有限矩阵由原 canonical 半周期公式重建；实际来源由同一个公开 producer 重建。没有重新选择使某个余行非零的测试，也没有将辅助素数当成目标素数。

## 1. 原来源、坐标与周期

置
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad \delta=1+2\omega,
\quad b=17,\quad y_b^2=x_b^3+b,
$$
$$
D=\frac d{dz},\qquad Dx_b=2y_b,\quad Dy_b=3x_b^2,\quad
\zeta_b=D\log\sigma_b .
\tag{1}
$$
保留原
$$
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad u=\kappa^N,\quad N\in4\mathbf Z_{>0},
\quad \eta(p)\in\{\pm1\},\quad \Omega=\Omega_p .
$$
所有 Amice 变换的规范仍是 $F(\Omega\log(1+T))$。

沿 R798/R801 定义
$$
F_{2,N}(z)=\Omega^{-2}\int Z^2e^{Yz/\Omega}\,d\rho_{cd,N}^{YZ},
\qquad G_{2,N}=P_4F_{2,N}.
\tag{2}
$$
这里 $\rho_{cd,N}^{YZ}$ 是同 $q_N^*$ 的完整 cd 返回来源。
$P_4$ 是原 $B_0=(e_0-\omega h_W)/(1-\omega^2)$ 在型四上的 canonical 投影。
原物理条件式为
$$
\boxed{
\Omega^{-2}Y_*(Z^2\,1_{E\in p^N}q_N^*B_0)
=\lambda^{2N}\nu_{G_{2,N}}.
}
\tag{3}
$$
原 generator 由 $Y+\varepsilon Z$ 的 $\varepsilon^2$ 系数乘 $2!$ 读取(2)；
全 $-1/84$、原 E 单位逆、C 高正矩、quarter 行和原两条核修正均未改变。

为使 b 的缩放完全显式，采用升幂基
$$
V_{4,j}=b^{5-j}\sigma_b^{34}x_b^{3j}\quad(0\le j\le5),
$$
$$
V_{5,j}=-b^{4-j}\sigma_b^{34}x_b^{1+3j}y_b
\quad(0\le j\le4).
\tag{4}
$$
它们分别张满原 degree34 的型四六维空间 $\mathcal V_4$ 和型五五维空间
$\mathcal V_5$。R801 的下降幂坐标在这里只按 $j\mapsto5-j$ 反序；
没有改变来源、周期或物理 Y。

若 $\theta^6=b$，则
$$
V_{4,j,b}(z)=\theta^{-4}V_{4,j,1}(\theta z),\qquad
V_{5,j,b}(z)=\theta^{-5}V_{5,j,1}(\theta z).
\tag{5}
$$
因此以下连接与半周期矩阵在(4)中不依赖 b。

## 2. 未投影连接的完整余行

令
$$
\nabla_{34}=D-34\zeta_b.
$$
对 $P=\sigma_b^{34}R(x_b,y_b)$，有
$\nabla_{34}P=\sigma_b^{34}DR$。
由(1)直接得到
$$
\boxed{
\nabla_{34}V_{5,j}=-(6j+2)V_{4,j}-(6j+5)V_{4,j+1}.
}
\tag{6}
$$
记此 $6\times5$ 双对角矩阵为 C。其秩为5。

定义坐标余行
$$
\Lambda_j=(-1)^j\frac{(1/3)_j}{(5/6)_j}\quad(0\le j\le5),
$$
即
$$
\Lambda=
\left(1,-\frac25,\frac{16}{55},-\frac{224}{935},
\frac{896}{4301},-\frac{23296}{124729}\right).
\tag{7}
$$
递推
$\Lambda_{j+1}=-(6j+2)\Lambda_j/(6j+5)$ 给 $\Lambda C=0$。
结合秩5，得到
$$
\boxed{\operatorname{im}C=\ker\Lambda\subset\mathcal V_4.}
\tag{8}
$$
这是原有限 theta 连接的余商。本文不将它另认成一个未付的普通二维 de Rham 商，
也不把 $\Lambda G=0$ 与某个指定负矩为零混同。

## 3. 原 canonical 投影后的两种像

令
$$
H_r=\mathcal H_Y|_{\mathcal V_r},\qquad
P_r=\frac{I-\omega H_r}{1-\omega^2}\quad(r=4,5),\qquad c_B=1-\omega^2.
\tag{9}
$$
[R798](R798-original-halfperiod-two-types-and-e-depth-second-source.md)
已用完整 E[2] lift 和原 S 锚支付
$$
H_r^2+H_r+I=0,\quad
\operatorname{rank}P_4=3,\quad\operatorname{rank}P_5=2.
$$
在型五中，$\operatorname{im}P_5$ 恰是原 $D_\omega,D_-$ 两条算术线；
$\ker P_5$ 是旧 primitive 三维块，H 特征为 $\omega^2$。
在型四中，$\operatorname{im}P_4$ 的原 CM13 多项式是 $X^3+\omega$。

取 $P_4$ 的原前三个 pivot 列为 Q 的三列，即在(4)中
$$
Q=\frac1{13122}
\begin{pmatrix}
6562&8&64\\
680&8464&2480\\
12376&5642&3394\\
24310&-2431&1045\\
6188&364&50\\
136&-19&-17
\end{pmatrix}.
\tag{10}
$$
它们是 R801 的三个完整 theta 基。直接的完整有限恒等式是
$$
\boxed{\Lambda Q=\frac1{36685}(14901,-3004,-496).}
\tag{11}
$$
所以 $\operatorname{im}P_4\cap\operatorname{im}C$ 恰为二维，
而非整个型四三维块。

对 $P_5$ 的原 pivot 基施 $P_4C$，其 Q 坐标矩阵为
$$
D_{\rm ar}=\frac1{27}
\begin{pmatrix}
-112&4\\
-1376&107\\
6188&-59
\end{pmatrix}.
\tag{12}
$$
该矩阵秩2，唯一余行可以取
$$
\ell_{\rm ar}=\left(\frac{1793}{20},-\frac{14}{5},1\right).
\tag{13}
$$
等价地，在型四的完整六坐标上取
$$
L_{\rm ar}=
\left(\frac{112509}{680},-\frac{26487}{2720},
\frac{2673}{340},0,0,0\right).
\tag{14}
$$
有 $L_{\rm ar}Q=\ell_{\rm ar}$，且
$$
\boxed{
L_{\rm ar}G=0
\iff
G\in P_4\nabla_{34}(\operatorname{im}P_5),
\quad G\in\operatorname{im}P_4.
}
\tag{15}
$$

相反，$P_4C$ 在 $\ker P_5$ 上是三维同构。其完整右逆，
以 Q 为输入坐标、以 $V_{5,j}$ 为输出坐标，恰是
$$
R_-=
\begin{pmatrix}
-43/1458&-2/4131&-32/12393\\
23/1458&-232/4131&-158/12393\\
-77/486&55/2754&-11/8262\\
-55/1458&-11/4131&-11/12393\\
-1/1458&1/8262&1/12393
\end{pmatrix}.
\tag{16}
$$
完整恒等式为
$$
\boxed{P_5R_-=0,\qquad P_4CR_-=Q.}
\tag{17}
$$
因此若 $G_{2,N}=Qd_N$，则
$$
P_{-,N}=\sum_{j=0}^4(R_-d_N)_jV_{5,j}
$$
是满足
$$
\boxed{P_5P_{-,N}=0,\qquad
G_{2,N}=P_4\nabla_{34}P_{-,N}}
\tag{18}
$$
的唯一原 primitive 型五截面。唯一性只在指定 $\ker P_5$ 内；
整个五维投影连接本身有二维核。

(10)–(17)是由原半周期公式重建后在 K 上得到的恒等式，
不是辅助域的秩猜测。公开 producer 同时核对
$\operatorname{rank}(P_4C)=3$、算术限制秩2和 primitive 限制秩3。
固定右逆的分母始终保留；未把 K 上循环性提升为某个全整格行列式为单位。

## 4. 同一个实际来源的两个单位障碍

对原实际 $G_{2,N}$，定义
$$
A_{\eta}(\lambda,\kappa,u)=\Lambda G_{2,N},\qquad
B_{\eta}(\lambda,\kappa,u)=L_{\rm ar}G_{2,N}.
\tag{19}
$$
坐标均指(4)。公开运行保同一原 q 和全部58行；
在
$$
\mathbf F_{1009},\quad \omega=374,\quad\tau=2,\quad
\lambda=(1-\tau)/\tau=504,\quad \kappa=u=0,\quad b=\Omega=1
$$
上，对 $\eta=+1,-1$ 两个实际分支分别得到
$$
\boxed{A_\eta=54,\qquad B_\eta=724.}
\tag{20}
$$
两次读取的原58行均验证通过，最终同一 q 的
$\mathfrak j_2$ 辅助值均为319。没有用这个辅助值替换实际
$\mathfrak j_2(\lambda,\kappa,u)$。

R801 已支付这些系数的真实整返回：
它们是保全部原50阶逆、联合修正、E 单位逆及固定分母的
$K(\lambda,\kappa,u)$ 有理函数，且在既有整域内
$$
A_\eta=A_\eta(\lambda,0,0)+\kappa A_{\eta,1}+uA_{\eta,2},
\quad
B_\eta=B_\eta(\lambda,0,0)+\kappa B_{\eta,1}+uB_{\eta,2},
\tag{21}
$$
余项整。由(20)，两符号下的四个边界分子均非零。
对这些实际分子、既有分母及(7)、(14)、(16)的固定分母，
应用 [固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)，
可从旧 ray 删去一个零密度坏集与固定有限坏集，使
$$
\boxed{
A_{\eta(p)}(\lambda,\kappa,\kappa^N),
\ B_{\eta(p)}(\lambda,\kappa,\kappa^N)\in\mathcal O^\times
\quad\text{对所有 }N\in4\mathbf Z_{>0}.
}
\tag{22}
$$
统一全部 N 的原因仍是 $\kappa\in p\mathcal O$、
$u=\kappa^N\in p^4\mathcal O$。不新增 mod1009 条件，
也不改变旧高13/19或 M3 射线。

从(8)、(15)、(22)得到两条针对原指定来源的严格结论：
$$
\boxed{
G_{2,N}\notin\nabla_{34}(\mathcal V_5),\qquad
G_{2,N}\notin P_4\nabla_{34}(\operatorname{im}P_5).
}
\tag{23}
$$
而(18)给出它的唯一 primitive 投影预像。
所以不能把原 G 直接写成两个算术点线的协变导数，
也不能去掉投影后将它写成任一型五截面的协变导数。

## 5. 完整半周期交换子与绝对号

现在在原同一 theta 来源上解释(18)，而非只给一个矩阵因子化。
对非零半周期 $t_e$，记 $e=x_b(t_e)$，于是 $e^3=-b$。
取 R798 已定绝对号的完整 Mumford lift $U_e$；包含其原 canonical 常数相位。
对 $P=\sigma_b^{34}R(x_b,y_b)$，它写为
$$
U_eP=(\delta e)^{-17}\sigma_b^{34}(x_b-e)^{17}
R\!\left(\frac{e(x_b+2e)}{x_b-e},
         \frac{-3e^2y_b}{(x_b-e)^2}\right).
\tag{24}
$$
在这个 U 规范中
$$
\mathcal H_Y=\frac{\sum_{e^3=-b}U_e-I}{2}.
\tag{25}
$$
这与用 $T_e=-U_e$ 写
$-\frac12(I+\sum T_e)$ 完全相同；不能漏掉这一共同负号。

置
$$
A_e(z)=\zeta_b(z+t_e)-\zeta_b(z)-\zeta_b(t_e)
      =\frac{y_b(z)}{x_b(z)-e}.
\tag{26}
$$
最后等号是原 Weierstrass 加法公式。canonical lift 的指数为
$\exp(-34\zeta_b(t_e)z)$ 乘一个与 z 无关的相位；
直接微分给
$$
\boxed{[\nabla_{34},U_e]=34A_eU_e.}
\tag{27}
$$
相位常数在微分中保留而不产生额外项。
由(25)得到
$$
[H,\nabla_{34}]=-17\sum_eA_eU_e.
\tag{28}
$$
在两个角型之间，矩阵写作 $H_4C-CH_5$；
公开完整矩阵的秩是4。因此该交换子不是一个可省略的 scalar 修正。

由(9)还有
$$
P_4C-CP_5=-\frac{\omega}{c_B}(H_4C-CH_5).
\tag{29}
$$
对 $P_{-,N}\in\ker P_5$，联立(18)、(28)、(29)得到
$$
\boxed{
G_{2,N}
=\frac{17\omega}{1-\omega^2}
  \sum_{e^3=-b}\frac{y_b}{x_b-e}\,U_eP_{-,N}.
}
\tag{30}
$$
这给出同一个原 G 的完整有限半周期表达，
不是把 primitive 与算术块按相同 CM 次数相认。

(30)中的每项实际上全纯。若
$$
P=-\sigma_b^{34}x_by_bQ(x_b^3),\qquad\deg Q\le4,
$$
则将(24)直接代入(26)，记 $X=x_b^3$，得到
$$
\boxed{
A_eU_eP
=-3b(\delta e)^{-17}\sigma_b^{34}
 (X+b)(x_b+2e)(x_b-e)^{13}
 Q\!\left(\frac{-b(x_b+2e)^3}{(x_b-e)^3}\right).
}
\tag{31}
$$
对 Q 的第 j 项，剩余 $(x_b-e)$ 次数为 $13-3j\ge1$。
因此没有隐藏的二挠点极；除 $\sigma_b^{34}$ 外的多项式次数至多17，
原点极也由其零阶34完全抵消。每项都有真实因子 $X+b=y_b^2$。
在型四和式中，这正给 R801 的
$$
\sigma_b(2z)^2\sigma_b(z)^{26}
=4y_b(z)^2\sigma_b(z)^{34}
\tag{32}
$$
共同因子。

一般 b 的(24)由 $x_b=\theta^2x_1$、
$e_b=\theta^2e_1$、$\sigma_b(z)=\theta^{-1}\sigma_1(\theta z)$
得到：$(\delta e_b)^{-17}$ 的 $\theta^{-34}$
与 $(x_b-e_b)^{17}$ 的 $\theta^{34}$ 抵消。
结合(5)，这里没有遗漏底曲线17的周期或相位变换。

## 6. 原负二行、ζ 伴随与完整单位域

本篇实际返回的指定负二值仍然是
$$
\boxed{
\mathcal I_{2,N}
=\int_{\substack{E\in p^N\\Y\in\mathbf Z_p^\times}}
  Z^2Y^{-2}q_N^*\,dB_0
=\lambda^{2N}\Omega^2
  \int_{\mathbf Z_p^\times}Y^{-2}\,
       d\nu_{P_4\nabla_{34}P_{-,N}} .
}
\tag{33}
$$
(30)可以代入右边，所有半周期 lift 和同一个 unit 测试必须同时保留。

尤其 $\nabla_{34}$ 不能当作普通导数。若 $P=\sigma_bH$，
则 $H=P/\sigma_b$ 是原 degree33 全纯截面，
$$
\nabla_{34}P=\sigma_bH'-33\sigma_b'H .
$$
在原两个输入 c、v 和同一 $\Omega$ 下，这给准确有界卷积来源
$$
\boxed{
\nu_{\nabla_{34}P}
=\Omega^{-1}(c+v)_*
 \left((v-33c)\,\nu_{\sigma_b}(c)\otimes\nu_H(v)\right).
}
\tag{34}
$$
故未投影的负二测试是
$$
\int_{\mathbf Z_p^\times}Y^{-2}\,d\nu_{\nabla_{34}P}
=\Omega^{-1}
 \int_{c+v\in\mathbf Z_p^\times}
 \frac{v-33c}{(c+v)^2}\,
 d\nu_{\sigma_b}(c)d\nu_H(v).
\tag{35}
$$
等价地，它是 R801(18)的
$\Omega^{-1}I_{P,-1}-34I_{\zeta_bP,-2}$。
两项共用和变量单位域，不能把第二项删掉。
对(33)还必须保完整 $P_4$ 的半周期转置；
(23)恰排除了将这个投影免费省略的做法。

因此即使 primitive 型五的完整负一值已有点公式，
它也不直接给(33)的非零。R806 对型四的完整 order18/Katz 负二身份
与本篇连接相容，但不删除(30)、(34)中的半周期和 ζ 伴随。

## 7. 与原中央的准确接口

R801 的原整条 W 关系不变。置
$$
\mathcal G_N(z,w)=\int_{E\in p^N}
 1_{b_YY+zZ\ {\rm unit}}\,
 \langle b_YY+zZ\rangle^{d_pw}q_N^*\,dB_0,
\qquad b_Y=\frac{20+3\omega}{17}.
$$
当 $z\in p\mathcal O$ 时，单位域就是 Y-unit；
原零次、一次来源均为零。因此
$$
\partial_w\mathcal G_N(z,0)
=-\frac{d_pz^2}{2b_Y^2}\mathcal I_{2,N}
+d_p\sum_{k\ge3}\frac{(-1)^{k+1}z^k}{kb_Y^k}
 \int_{\substack{E\in p^N\\Y\ {\rm unit}}}Z^kY^{-k}q_N^*\,dB_0 .
\tag{36}
$$
对原偶 j≥2，完整浅补域仍满足
$$
\mathscr X_{N,j}(w)+\lambda^j\mathcal G_N(\kappa^j,w)
=\lambda^{2N}6\delta J_T(w)/c_B.
\tag{37}
$$
本篇新证明的是(18)、(22)、(23)、(30)这些同源有限关系。
原 $J_T'=0$ 仍只使(37)两边的真实中央补偿成立；
没有把(33)、其三个 CM 分量、(36)高尾或 $\mathscr X_{N,j}'$
分别赋零。

## 8. 公开证明记录与可复现范围

本篇有限恒等式与实际余行由以下公开运行支付；写作时亲读整个小矩阵输出，
没有另作本地或 V8 数值复算。

- source commit：$08b5c59698e361935d3e57c7e3d46b354564f669$；
- producer：[check-r807-native-covariant-connection.py](../scripts/check-r807-native-covariant-connection.py)，顶层参数为空；
- run：[43742915855](https://github.com/Rogerhu12/math-research-public/actions/runs/43742915855)，job：132899794982；
- request：rank2-r807-native-covariant-connection-20261115；
- python-flint：0.9.0，实际退出码0；
- producer SHA256：$ed2804a12d7850d36d34b372ed947cf94d700f92ff1d8a102af338526250c8db$；
- stdout：4635 bytes，SHA256：$9f4a91a7102aaf9e5e796be5998c5ba8fffe3228632f178c0233acfe4139b23f$。

内部同源 reader 为 check-r798-native-second-z-source.js，
参数为
$--max-block=4,\ --taus=2,\ --with-b,\ --b-g-blocks=3,\ --neutral-degree=12$。
其 stdout 为1972 bytes，SHA256 为
$088fd208cf6715dfd274cbc22c140993ad6bf15b486738bd87cc29814430545c$。

三个实际输入的 SHA256 分别为：

| 原输入脚本 | SHA256 |
|---|---|
| check-r798-type-four-halfperiod-and-cm13.py | f6a1fe72d01b0c804059a06395c5a9c5d78e54d5742a6ca9af957febec9661b3 |
| check-r732-original-type-five-cm13.py | d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469 |
| check-r798-native-second-z-source.js | f051903f53667e86c5e782532e11a31745522a45a516bc6d0f44444fdfcef9fd |

producer 从原 E[2] 公式及 S 锚重建 H/P 矩阵，
再重建同 q 的完整来源；没有使用旧矩阵 JSON 或保存可重算数据文件。
(6)–(8)、(24)–(35)另有正文所给逐式推导；
其余小矩阵为该准确有限算法的公开输出。实际密度结论使用(20)证明
固定有理分子非零，并使用既有 CM 单位密度引理，
没有从少量目标素数样本猜普遍非零。
