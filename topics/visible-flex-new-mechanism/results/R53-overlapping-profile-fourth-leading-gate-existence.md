# R53：真正重叠profile的四阶常段最高次门与准确隐函数构造

日期：2026-11-14。literature推导，repo_sources独立全文核，root全文复核。独立正向存在证明。未执行真实 profile 积分、几何优化或 ODE 数值研究；有限相位代数与 Jacobian 可准确核对。

**结论范围。** 在已有单 P 全零算子、四块倒行周期浸入带上，存在真正重叠的实 profile 圆，完整满足三矩、两个二阶与四个第三阶 range，并且在 $(k,h,\omega)=(0,1,0)$ 常段上，其第四 ruling 的全部相位 sigma² 系数准确为零。这里支付的是一个曾严格阻断不交平面的必要门，尚未支付该常段的一次/常数项、其他常状态、完整第四周期函数或有限等距族。

来源为 [R45 单P与倒行闭合](R45-reversal-four-block-third-period-cancellation.md)、[R46 完整第三阶恢复](R46-eight-packet-complete-third-order-circle.md)、[R49 常段最高项](R49-fourth-ruling-leading-coefficient-and-narrow-packets.md)、[R50 准确局部四次式](R50-disjoint-profile-circle-fourth-order-positive-obstruction.md)及 [R52 重叠交叉通道](R52-overlapping-profile-plane-complete-third-order-circle.md)。本稿采用新的四相位packet，不声称R52指定谱构造自动通过四阶。有限代数复核见 [准确脚本](../scripts/literature_overlap_fourth_gate_certificate.py)和 [开发证书](../notes/literature-overlap-fourth-gate-certificate-20261114.json)；后者不评价任何真实profile积分。

## 1. 复记号与完整常段相位系数

取复 profile $q=f+ig$，实双线性 E、R0 复线性延拓。三矩圆等价于

$$\int q''^2=0,\quad\int xq''^2=0,\quad
\int x^2q''^2+2\int q'^2=0.\tag{1}$$

记

$$V=\mathcal R_0(q,q),\quad D=\operatorname{Re}V,$$

$$\mathcal C(r)=E(q,\mathcal R_0(q,r)),$$

$$\mathcal B(r)=E(q,\mathcal R_0(\bar q,r))
+E(\bar q,\mathcal R_0(q,r)).$$

固定目标仍为 $g_X+\varepsilon^2(dY_f)^2$，不是任意改变的平均目标。令 $\zeta=e^{-2i\theta}$。在常段，二阶 secular profile 为

$$R_\theta=\frac D2-\frac{\zeta V+\bar\zeta\bar V}{4},$$

即二阶场最高项 $-\sigma Y_{R_\theta}$；三阶场最高项为
$-\sigma^2Y_{\mathcal R_0(\phi_\theta,R_\theta)}$，其中
$\phi_\theta=\cos\theta f+\sin\theta g$。

所以第四 ruling 的 sigma² 系数是

$$K(\theta)=-E(R_\theta,R_\theta)
+2E\{\phi_\theta,\mathcal R_0(\phi_\theta,R_\theta)\}.$$

直接展开得到

$$K(\theta)=K_0+\operatorname{Re}\{\zeta K_2+\zeta^2K_4\},$$

$$\boxed{K_4=-\frac18\mathcal F(q),\qquad
\mathcal F(q)=E(V,V)+2\mathcal C(V),}\tag{2}$$

$$\boxed{K_2=\frac12\{E(D,V)+\mathcal C(D)\}
-\frac14\mathcal B(V).}\tag{3}$$

因为 theta=0 时 $R_\theta=0$，常项满足
$K_0=-\operatorname{Re}(K_2+K_4)$。故全部相位的最高次门恰为两个复等式

$$\mathcal F(q)=K_2(q)=0.\tag{4}$$

全部同 collar 二、三阶齐次 gauge 在此常段只改变较低 sigma 次数，不改变 (2)–(3)。

## 2. 普通复四次多项式与合法的局部表达

R50 的尾消去及多项式总导数身份可作普通复代数延拓。因此在 (1) 下，

$$\mathcal F(q)=\frac1{128}\int
\mathcal Q(x,q,q',q''),\tag{5}$$

其中

$$\begin{aligned}
\mathcal Q(x,f,p,r)={}&2(1+x^2)r^2
\left[\left(f-xp+\frac{x^2-1}{6}r\right)^2
+\left(p-\frac x3r\right)^2\right]\\
&+\frac{(1+x^2)^3r^4}{36}
+4p^2\left(f-\frac x3p\right)^2
+\frac{2(x^2+3)}9p^4.
\end{aligned}$$

所有平方都是普通复平方，**不是模平方**，因此没有实正性结论。

为处理 (3)，写 $Q=1+x^2$、$a_q=xq''-q'$、$F_q=Qq''-2q$，并定义

$$B_q=F_q^2/2-2Qa_q^2-Q^2a_qq''',$$

$$B(q,\bar q)=F_qF_{\bar q}/2-2Qa_qa_{\bar q}
-\frac{Q^2}{2}(a_q\bar q'''+a_{\bar q}q''').$$

准确分部积分和极化给

$$\mathcal C(r)=\frac1{32}\int B_qr'',\qquad
\mathcal B(r)=\frac1{16}\int B(q,\bar q)r''.\tag{6}$$

这些公式对 r 的尾部没有额外零条件，因为 q 紧支撑。

## 3. 四组相位、幅度与位置的准确定义

先固定一个实偶、非零的 C-infinity bump eta。以下两种尺度严格分开：raw bump 宽度 delta 在开始时固定，之后不取极限；共同物理缩放 lambda 才趋于零。

四组个数、幅平方与平方相位取

$$N=(4,48,3,3),\qquad b=(3,1/2,4,4),$$

$$z=( -1,1,e^{2\pi i/3},e^{-2\pi i/3}),\qquad
\alpha_j=\sqrt{b_j}e^{i\vartheta_j/2},\quad z_j=e^{i\vartheta_j}.
\tag{7}$$

所有数准确给

$$\boxed{\sum_jN_jb_jz_j=0,\quad
\sum_jN_jb_j^2z_j^2=0,\quad
\sum_jN_jb_j^2(z_j+1)^2=0.}\tag{8}$$

各组 raw 中心取

$$t_{j,r}=\sqrt2\cos\left(\pi\sqrt{p_j}+\frac{2\pi r}{N_j}\right),
\quad r=0,\ldots,N_j-1,\quad(p_1,p_2,p_3,p_4)=(2,3,5,7).$$

每组严格有

$$\sum_rt_{j,r}=0,\qquad \sum_rt_{j,r}^2=N_j.\tag{9}$$

它们全部互异：任何余弦相等都迫同组的 $2\sqrt{p_j}$ 或异组的 $\sqrt{p_j}\pm\sqrt{p_k}$ 为有理数，与所选不同素数矛盾（相同方向的同组等式只给同一索引）。

令 Delta 为这个有限节点集的最小正间距，固定
$0<\delta<\min(\Delta/10,1/10)$。以 $\eta_\delta(x)=\eta(x/\delta)$ 为各个相同 raw bump，必要时先把 eta 支撑定为 [-1,1]。于是所有 58 个 bump 的支撑互不相交。

对邻近 (7) 的控制 $(b_j,\vartheta_j)$，定义基本复 packet

$$q_\beta^{\rm base}(y)=\sum_{j=1}^4\alpha_j
\sum_{r=0}^{N_j-1}\eta_\delta(y-t_{j,r}).$$

由 (9)，三个复总矩均是同一个复数

$$C_0(\beta)=\sum_jN_jb_jz_j$$

乘固定实系数。因此只要 $C_0=0$，三个复矩准确同时为零；这里没有用“所有中心近似相同”替代位置矩条件。

## 4. 八个外 packet 仍完整支付第三阶

取外平移 $T_\ell=10\ell$、$\ell=0,\ldots,7$ 及

$$a_\ell=(-1)^\ell\binom7\ell^{1/3}.$$

这些基本 packet 的包络互不相交。定义

$$q_\beta^{\rm raw}(y)=\sum_{\ell=0}^7a_\ell
q_\beta^{\rm base}(y-T_\ell).$$

若 $C_0=0$，每个基本 packet 已三复矩为零，所以整个 raw profile 也满足 (1)。两个二阶解按 $a_\ell^2$ 局部相加，四条第三 ruling 按 $a_\ell^3$ 相加；完整平移次数至多六及第七差分同时使四条 ruling 恒零。四块倒行则支付全部第三周期函数。因此真正重叠三阶稿中的两个二阶、四个第三阶完整 range 均成立。

这里不会因组内 bump 很多而遗漏交叉 forcing：不同个体 bump 不交，但复相位使 f、g 在若干个体 bump 内同时非零。正确二阶式始终是 $\sin^2\theta Z_d-\cos\theta\sin\theta Z_c$。

设

$$A_4=\sum_{\ell=0}^7a_\ell^4>0,\quad
I_4=\int\eta_\delta''^4>0,\quad
I_{23}=\int\eta_\delta''^2\eta_\delta'''^2>0.$$

这些是固定的有限常数，本稿不需要对它们作数值求值。

## 5. 共同窄化下的两个准确主项

在共同正物理区间内固定 c>0，令

$$q_{\lambda,\beta}(x)=q_\beta^{\rm raw}((x-c)/\lambda),\qquad\lambda>0.$$

全部内外中心均为 $c+\lambda(T_\ell+t_{j,r})$，bump 半宽为 $\lambda\delta$。固定 raw 支撑后取 lambda 足够小，就有整个构造处于共同物理区间且两外 collar 非空。**所有中心共同趋于 c；本稿没有把固定分离的物理中心各自的 Q 值强行设为相同。**

令 $Q_c=1+c^2$。从 (5) 的最高导数四次项逐项缩放得到

$$\boxed{\mathcal F(q_{\lambda,\beta})
=\frac{Q_c^3I_4A_4}{1536\lambda^7}
\sum_jN_jb_j^2z_j^2+O(\lambda^{-6}).}\tag{10}$$

这是在 $C_0=0$ 上的真实公式；§6 给出适合隐函数定理的光滑扩展。

为核 (3)，在一个 raw bump 上记其复幅为 alpha。忽略低阶项时

$$V''=\frac{cQ_c}{4\lambda^5}\alpha^2
\eta_\delta''\eta_\delta'''+O(\lambda^{-4}).$$

令 $E_* = c^2Q_c^3 I_{23}/(64\lambda^9)$。该 bump 对最高次各项的贡献为

$$E(V,V):\ \alpha^4E_*,\quad
E(V,\bar V):\ |\alpha|^4E_*,$$

$$\mathcal C(V):\ -\alpha^4E_*/2,\quad
\mathcal C(\bar V):\ -|\alpha|^4E_*/2,$$

$$\mathcal B(V):\ -\alpha^2|\alpha|^2E_*.$$

将 $D=(V+\bar V)/2$ 代入 (3)，其贡献因此为
$E_*\,b^2(z+1)^2/8$。不同 bump 的最高导数支撑不交，真正尾项只进入较低阶；外幅按 $a_\ell^4$ 加权。故

$$\boxed{K_2(q_{\lambda,\beta})
=\frac{c^2Q_c^3 I_{23}A_4}{512\lambda^9}
\sum_jN_jb_j^2(z_j+1)^2+O(\lambda^{-8}).}\tag{11}$$

两式使用同一个冻结 raw profile，不是分别改形或分别选择参数的两个极限。

## 6. 不在约束外误用尾条件的光滑延拓

隐函数定理需要把映射定义到 $C_0\ne0$ 的附近。对第一项，直接用 (5) 右边的普通复多项式积分作为 $\mathcal F_{\rm loc}$：当 $C_0=0$ 时它等于真实 $\mathcal F$，而 $\lambda^7\mathcal F_{\rm loc}$ 在 lambda=0 有光滑延拓。

对 K2，固定 raw collar $[A,B]$，严格包含全部 raw 支撑；在移动区间 $I_\lambda=[c+\lambda A,c+\lambda B]$ 上按右端锚定义 J、V，并用 (3)、(6) 作所有积分。当 $C_0=0$ 时 V 在两 collar 为零，故移动区间与原固定活动区间的真实积分相同。

换元 $x=c+\lambda y$ 后，所有 profile 与积分界都固定。V、V'、V'' 的最坏幂次分别为 $\lambda^{-3},\lambda^{-4},\lambda^{-5}$，$B_q$ 的最坏幂次为 $\lambda^{-5}$。Q、x 及尾积分系数都是 lambda 多项式，所以 $\lambda^9K_2$ 是有限非负幂多项式，其系数光滑依赖 beta。第一项同样由最多四个二阶导数给 $\lambda^7\mathcal F_{\rm loc}$ 的有限非负幂展开。

因此这里没有对未知 $O(\lambda)$ 余项求导，也没有在约束外暗设左尾为零。

## 7. 六维准确 Jacobian 与小正 lambda 的真实解

归一化三个复方程为

$$C_0(\beta)=0,$$

$$\frac{1536\lambda^7}{Q_c^3I_4A_4}
\mathcal F_{\rm loc}(q_{\lambda,\beta})=0,$$

$$\frac{512\lambda^9}{c^2Q_c^3I_{23}A_4}
K_2(q_{\lambda,\beta})=0.\tag{12}$$

在 lambda=0，其值由 (8) 给零，映射恰变成

$$\left(\sum Nbz,\ \sum Nb^2z^2,\ \sum Nb^2(z+1)^2\right).$$

固定 $b_4=4,\vartheta_4=-2\pi/3$，以
$(b_1,b_2,b_3,\vartheta_1,\vartheta_2,\vartheta_3)$ 为六个实未知数，按三个复式的实部/虚部排列 Jacobian。于 (7) 的准确矩阵为

$$\begin{pmatrix}
-4&48&-3/2&0&0&-6\sqrt3\\
0&0&3\sqrt3/2&-12&24&-6\\
24&48&-12&0&0&48\sqrt3\\
0&0&-12\sqrt3&72&24&-48\\
0&192&-12&0&0&0\\
0&0&12\sqrt3&0&48&-96
\end{pmatrix},$$

其行列式准确为

$$\boxed{-716636160\ne0.}\tag{13}$$

有限维隐函数定理因而给充分小的正 lambda 和光滑参数 $\beta(\lambda)$，使 (12) 全部准确为零，且各 b_j 仍严格正。

第一式使三复总矩及完整二、三阶 range 成立；在这一约束上局部延拓就是实际函数，所以另两式正是 $\mathcal F=K_2=0$。由 §1，这准确支付常 $(0,1,0)$ 段的整个四阶 sigma² 相位函数。

## 8. 真正重叠、固定参数与未支付项

种子含四个不同实投影方向：0、pi/2、pi/3、-pi/3。附近参数仍至少含三个互不相同的投影方向，不能由同一个实 O(2) 变换同时变成两根坐标轴。因此最终 f、g 不是旧不交平面的旋转。

选择一个充分小的固定正 lambda 以及相应 $\beta(\lambda)$ 后，所有节点、宽度、幅度、相位均是同一设计的固定参数。lambda 是设计尺度，不是等距变形相位 theta；本稿也没有把 lambda=0 的退化 profile 当作曲面。

这证明新平面确实能通过旧不交类永远无法通过的一条完整必要门。它不支付常段的较低 sigma 系数、其他常 k/h/omega 状态、光滑连接部分、第四 characteristic 周期函数、四阶以后、级数收敛、闭曲面嵌入或宏观 reach/位移比例。
