# R265：包内伴随方向与一条有序 Gaussian 面积的准确联合支付

日期：2026-11-15。**完整纸面建设性证明；未执行任何新积分、扫描、消元或几何计算。**

本稿接 [R256 准确六能量分支](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md)及 [R262 有序负号](R262-ordered-primitive-obstruction-for-the-multiwidth-energy-branch.md)，新增一个真实方向控制：不改变各点的 diagonal 二次密度，却将 imaginary quadratic primitive 的长平台压到每个外包内部。它给 [R257 剩余量](R257-cumulative-primitive-energy-in-the-complete-positive-negative-Gaussian-area.md) $\mathscr Q$ 的严格正号分支；与 R262 的负号完整 block 作正四次幅度组合，能够准确支付这一原 pure 面积必要等式，且保留已经支付的三矩、全部第三、六能量、整个 $A_{-2,-3}$ 面积和 [R259 全部 odd 面积条件](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)。

这只增加一条真实标量支付。它不支付 $A_{1,-3}$ 的全部整圆三外矩，不宣称剩余 even 方程独立或全部可解，更不声称完整第四 ruling/period 或有限等距族成立。

## 1. 一个带精确三交叉零矩的伴随母包

固定非零 even 实
$\psi\in C_c^\infty(-1/40,1/40)$，取

$$
t_j=(j-7/2)/5,\qquad
\epsilon_j=(-1)^{\operatorname{popcount}(j)},\quad0\le j\le7,
$$

$$
v(y)=\sum_{j=0}^7\psi(y-t_j),\qquad
w(y)=\sum_{j=0}^7\epsilon_j\psi(y-t_j).
\tag{1}
$$

支撑严格不交且都在 $(-1,1)$。$v$ 为 even，$w$ 为 odd。由于每点最多有一个子包活动，且子包之间有零 collar，对任意非负整数 $p,q$，逐点有

$$
v^{(p)}v^{(q)}=w^{(p)}w^{(q)}.
\tag{2}
$$

特别，所有原八矩二次算子都满足
$\Phi_X(v,v)=\Phi_X(w,w)$，不仅是二阶导数平方相同。

Thue–Morse 长度8的零至二次符号矩为零。每个平移子包的三个原矩是其同一普通矩向量的三角变换，故

$$
\boxed{\mathbf I(v,w)=0,\qquad
\mathbf I(v,v)=\mathbf I(w,w).}
\tag{3}
$$

这是真实三矩，不只 $I_0$。辅助变量 $y$ 可以正负；本节只用普通导数和多项式矩，不把物理 $1/x$ 算子放在 $y=0$ 评价。

用这个 $v$ 作 R256 的基本母包，并同时定义其伴随：

$$
u_{s,h}(y)=(sh)^{3/2}v(y/(sh))
+h^{3/2}v((y-L)/h)+h^{3/2}v((y+L)/h),
$$

$$
\widehat u_{s,h}(y)=(sh)^{3/2}w(y/(sh))
+h^{3/2}w((y-L)/h)+h^{3/2}w((y+L)/h),
\quad L=1/2.
\tag{4}
$$

仍先限 $s$ 在1的小邻域，取足够小正 $h$，使三个母子包不交。每个 affine copy 都保持 (2)、(3)，从而

$$
u^{(p)}u^{(q)}=\widehat u^{(p)}\widehat u^{(q)},\qquad
\mathbf I(u,\widehat u)=0.
\tag{5}
$$

以后每个外包都使用这一同参数伴随，而不只替换中央母子包。

## 2. 改变方向而保留原 even 能量和真正矩条件

沿用 R256 的两坡、两宽度及高低中心，将外包分别写为
$\eta_i=w_i^{3/2}u((x-\zeta_i)/w_i)$ 和
$\widehat\eta_i=w_i^{3/2}\widehat u((x-\zeta_i)/w_i)$。
定义

$$
f_+=\sum_i a_i\eta_i,\qquad
g_+=\sum_i b_i\widehat\eta_i.
\tag{6}
$$

与原 $g_-=\sum_i b_i\eta_i$ 相比，$f$ 完全相同，所有 diagonal 二次输出也完全相同：

$$
\Phi_X(f_+,f_+)=\Phi_X(f_-,f_-),\qquad
\Phi_X(g_+,g_+)=\Phi_X(g_-,g_-).
\tag{7}
$$

因此原 $L_c,M_c$ 作为完整函数，对所有参数逐点相同。三母包的 $A_0,\nu,K_2$、第一层简单形状根以及第二层能量隐函数定理均使用同一个实际 $u$，没有换成未经证明的独立积分常数。

三矩 circle 的 real 条件由 (7) 和 R256 保留；imaginary 交叉条件更强地在每个外包就为零：

$$
\mathbf I(f_+,g_+)=\sum_i a_ib_i\mathbf I(\eta_i,\widehat\eta_i)=0.
\tag{8}
$$

每个最小 $\psi$ 子包仍沿固定实方向，所以全第三 hook 零张量成立。R183 的八个完整副本因此仍能支付四个第三 ruling 槽。不能仅由 (7) 跳过这一步。

R250 的单面积 even 四次张量及其加权中心矩不变，因为在每个最小子包上，改变的只是 $b_i$ 的符号。其两个 odd 角系数，以及 $L_s,M_s$，由原十二完整副本支付：它们都是 profile 四次齐次、对 $g\mapsto-g$ 为奇，真实平移次数分别受 R259 的10次界与 R238 的10/9次界控制。全部36个 Gaussian odd 条件同样为零。于是完整包装后仍有原全角 $A_{-2,-3}$，并非只保其 pure 部分。

对这个更细的微包分解，R256 的一般身份 $N_c=6M_c,N_s=6M_s$ 继续成立。因此六能量全部支付。

## 3. 间距是一个先声明的新参数

为得到明确正号，允许 R256 的低组间距改为

$$
A=\Lambda+\sqrt{\nu(s)},\qquad \Lambda\ge10
\tag{9}
$$

的一次固定新参数；高组 $B$ 仍由原准确三矩方差式决定。并没有在一个已解出的固定 $\delta$ profile 上无偿改变间距。

先固定小正 $h$ 及形状根 $s_h$，再选有限大的 $\Lambda$，然后一次选定统一不交的八/十二复制间距，最后应用原双参数隐函数定理取正 $\delta$。其证明只要求 $A^2>\nu$ 和统一严格间隙。$F(\alpha,s,0)$ 与原 leading 根 $\alpha_0$ 不依赖 $A$；在该根处，$G(\alpha_0,s,0)$ 的中心项仍只通过
$V_L-V_H=\nu(1-q_0^2)$，所以原三角非退化 Jacobian 保留。

因此任意这样先固定的有限 $\Lambda$ 都给一个实际正宽的六能量根分支。参数可以很大、支持云可以很大；充分小正 $\delta$ 最后将这个有限云放入选定的正物理子区间。这里不声称数值规模适用或高阶范数一致有界。

## 4. 虚 primitive 在每个外包内真正紧

为避免把两层支撑混淆，写

$$
\rho_R=f_+''^2-g_+''^2,\qquad
\rho_I=2f_+''g_+''.
$$

由 (5)，$\rho_R$ 与原族完全相同。在第 $i$ 个外包上，$\rho_I=2a_ib_i\eta_i''\widehat\eta_i''$；其全积分为零，所以原右 primitive 在该外包两端都为零。没有跨外包的 imaginary 平台。

令

$$
K(u,\widehat u)=\int[J(u''\widehat u'')]^2\ge0.
\tag{10}
$$

这个母包 primitive 因真实交叉 $I_0=0$ 紧。I0 归一宽度变换给每个外包的平方积分等于 $w_iK$，所以

$$
\int(J\rho_I)^2=4K\sum_i a_i^2b_i^2w_i.
\tag{11}
$$

而

$$
\operatorname{Re}\int[J((f_++ig_+)''^2)]^2
=\int(J\rho_R)^2-\int(J\rho_I)^2.
\tag{12}
$$

这是一个真实有序 history 的改变；它不能被描述为仅在旧有限矩表中重新命名系数。

## 5. 原单位下的完整正号公式

在 R262 的 shape 坐标中，令

$$
a=q_0(1-\alpha),\qquad
U_\alpha=\alpha^2-6\alpha+1,\qquad
n=2^{11},\quad q_0=\frac1{16(1-\alpha)^2}.
$$

$\rho_R$ 的低包质量系数为 $-a$，高包为 $64a$。每个64低加1高的 cell 总 real 质量为零，故不同 cell 的 real primitive 交叉和为零。R262 的同 cell 计算只保 real 质量时准确给

$$
\sum_{i<j}R_iR_j(t_j-t_i)=-21856nAa^2.
$$

单包的真实自项仍保留。因此

$$
\int(J\rho_R)^2
=21856nm^2a^2 A
-\frac{\Delta}{2}na^2(64q_0+4096).
\tag{13}
$$

这里 $m=\int(u'')^2$、$\Delta$ 均由同一个母包定义，不含新自由常数。

另外，

$$
\sum_i a_i^2b_i^2w_i=n(64\alpha q_0^3+\beta).
\tag{14}
$$

在每个最小子包上，$g$ 的符号改变不影响任何 local 四次密度的实部。因此 R257 的其余完整 local 项与原族相同，准确为

$$
64nq_0U_\alpha(1-q_0^2)(C\nu-\mathcal L).
\tag{15}
$$

结合 (11)—(15)，

$$
\boxed{
\begin{aligned}
\operatorname{Re}\mathscr Q_+
={}&10928nm^2a^2 A
-\frac{na^2\Delta}{4}(64q_0+4096)\\
&-2nK(64\alpha q_0^3+\beta)
+64nq_0U_\alpha(1-q_0^2)(C\nu-\mathcal L).
\end{aligned}
}
\tag{16}
$$

所有后三项在固定 $\alpha,s,h$ 时与 $A$ 无关；第一项系数严格为正。这里没有把 R262 的负号公式直接换一个符号，因为新 imaginary 自项是原紧 primitive 的 $K$，必须按 (10) 保留。

在 $\delta=0$ 的已定根 $(\alpha_0,s_h)$，先取一个有限大的 $\Lambda$，使 (16) 严格为正并留正余量。随后按 §3 取得实际 $\alpha(\delta),s(\delta)$，其连续性使 (16) 对充分小正 $\delta$ 继续为正。

平移所需的完整复矩也可直接核：母包 TM3 符号对每个 $\psi$ 的0、1次中心矩给 $\int u''^3\widehat u''=\int x u''^3\widehat u''=0$，而每个 even $\psi$ 满足 $\int\psi'\psi''^3=0$。所以新复 profile 的 $M_4,M_1,N_1$ 本身全为零，非仅实部零。它们消掉 $\mathscr Q$ 的共同平移附加项，实际主宽度仍使 $\mathscr Q$ 同乘正 $\delta$。

八复制同乘正四次权。十二复制使最终 $\mathscr Q$ 为实数，其实部仍是正四次权和乘上述正值。因此有真正的、已付同一组条件的完整正号 block $\mathscr Q_+>0$。

R262 对相同 even 母包仍给负号 block $\mathscr Q_-<0$。两个号不是来自负幅度或把平方能量任意指定为负，而是来自不同的实际包内方向与完整累计历史。

## 6. 正四次混合准确支付新增必要等式

在两个有严格间隙的正物理子区间分别完成上述正号、负号构造。每个 block 都在其**最后位置**独立完成能量隐函数方程与八/十二包装。不能先解同一位置后任意搬移一个能量零点。

记它们为 $(f_-,g_-)$、$(f_+,g_+)$，其真实 $\mathscr Q$ 分别为负、正实数。取

$$
c_-=\mathscr Q_+^{1/4}>0,\qquad
c_+=(-\mathscr Q_-)^{1/4}>0,
$$

$$
f=c_-f_-+c_+f_+,\qquad
g=c_-g_-+c_+g_+.
\tag{17}
$$

每个完整 block 本身是三矩 circle，所以三矩准确相加。其二阶差与交叉 canonical 解真紧，完整第三槽仍准确相加；全 hook 在更细微包分解中也为零。

六能量的加法保真实边界：另一槽是紧的差或交叉像，背景左尾 $ax^2+bx$ 的完整配对按 R238/R241 消去；局部 bulk 交叉为零。对全部 Gaussian areas，R259 跨核对右侧 inner block 三矩线性，故两个完整合法 block 的交叉项准确为零。于是已为零的全角 $A_{-2,-3}$ 和全部 odd 条件保持。

对本稿新增的 $\mathscr Q$，更直接地，各完整 $J(q_\pm''^2)$ 都真紧，primitive 平方和 local 项按四次幅度相加：

$$
\boxed{
\mathscr Q(f+ig)
=c_-^4\mathscr Q_-+c_+^4\mathscr Q_+=0.
}
\tag{18}
$$

最后可共同实归一化三矩圆，所有齐次零条件继续保持。种子及其目标是这个新选择的 $(f,g)$，不能冒称原固定 seed/目标下的一次允许变形。

## 7. 准确新增内容与剩余方程

本稿保留 R256 的全部已付条件，并增加 R257/R252 对应的一个原 pure 面积标量。这个标量是 R259 剩余 even 方程中的真实线性组合；不凭计数声称剩余独立方程恰为29，也不声称同一个 Gaussian pair 的另外外矩或 mixed even 系数随它消失。

全 slot 的有序 self/cross 接口仍须继续使用。后续如果要同时支付更多 even 条件，需要研究已构造合法完整 blocks 的向量值，而非把每个 self 常数独立选择，或只用一个 scalar 符号反解所有面积。

正向结论是：R262 的具体负号来自可以改变的包内方向历史，不能升级成所有已付六能量圆的普遍障碍。对真实正宽 profile，存在严格正、严格负两种已付条件的完整 block；它们用正幅度就能准确支付新增的非局部面积标量。这里没有提出或运行新的数值研究，也没有授完整第四 range、嵌入、reach 或主课题成功。

