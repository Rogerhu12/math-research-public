# R908 — 原惰性双新类的整特殊化与完整点影子向量

日期：2026-11-16。**状态：下述整局部同构、原双新类的单位读取、全部上方素点与 ordinary 特殊化相容性已证明。尚未计算出其中的非零值。**

本篇继续 [R901 附录 B](R901-original-inert-endpoint-test-matrix-and-local-period.md) 的同一个原类 $\mathcal N_{12}^{\mathrm{aug}}$。新的具体公式是在原新增惰性位 $q_1$，将这枚类的 tame-inertia 坐标准确送到原 $\mathcal N_{12}$ 的**全部局部 Frobenius 坐标**：
$$
\boxed{\quad
\operatorname{loc}_{q_1}(\mathcal N_{12})
=u_1(\sigma_2-1)a_{12},\qquad
u_1=\frac{q_1+1}{p^{v_p(q_1+1)}}\in\mathbf Z_p^\times.
\quad}
\tag{1}
$$
右边属于完整素点向量，而不是任选一个角色的平均。经原 R859 的整 Frobenius 收缩，它也是同一类的点影子坐标；原固定 CM 对应的尺度仍须保留。这里没有除 $q_1+1$、没有以局部测试积分替代 Galois 类，也没有从这个读取同构宣布原类非零。

## 1. 同一个原来源、四角色和格

固定原普通 $p>211$、原系数整数环 $\mathcal O$，以及 R897/R900 中任意一个允许的旧 split 层与有限 wild 层。取不同良好惰性有理素数
$$
q_1,q_2\nmid30\cdot34p,\qquad
h_i=p^{v_p(q_i+1)}>1,\qquad u_i=(q_i+1)/h_i.
\tag{2}
$$
$K=\mathbf Q(\omega)$，$G_i=\langle\sigma_i\rangle\simeq C_{h_i}$。记
$$
R_i=\mathcal O[G_i],\quad
N_i=\sum_{r=0}^{h_i-1}\sigma_i^r,\quad
A_i=R_i/(N_i),\quad I_i=(\sigma_i-1)R_i.
\tag{3}
$$
R901(B3) 的原整同构是
$$
j_i:A_i\xrightarrow{\sim}I_i,\qquad j_i(\bar a)=(\sigma_i-1)a.
\tag{4}
$$

以下的 $T$ 是原指定最高角色的格，或者已为全部原 finite/wild 类一次固定扩大的格 $\mathcal T=p^{-C}T$。两者的公式完全相同，但不能在最后点读取时忘记 $p^{-C}$。所有旧对应、$q/q^4$ 端点、$X_1/X_0$ 倍率及 $C_5=-216$ 沿 R897 固定；本篇不重新将它们归一为一。

为核准确 twist，R886 的原四条算术 Galois 角色为
$$
\begin{aligned}
\rho_0&=\eta^{3-2a_j-2a_k}\psi_0^3\mathbf N^{-1},\\
\rho_1&=\eta^{3+2a_j+2a_k}\bar\psi_0,\\
\rho_2&=\eta^{3-2a_j+2a_k}\psi_0,\\
\rho_3&=\eta^{3+2a_j-2a_k}\psi_0,
\end{aligned}
\qquad
(a_4,a_{10},a_{16})=(13,1,7).
\tag{5}
$$
$(j,k)$ 是原 $(10,16),(16,4),(4,10)$。对应有限指数分别为
$(5,1,15,9)$、$(17,7,15,9)$、$(11,13,9,15)$。

在一个新增惰性 $q$ 处，原有限角色在有理主理想 $(q)$ 上取一，
$E_0:y^2=x^3+1$ 的 CM 角色满足
$$
\eta(\operatorname{Fr}_{(q)})=1,\qquad
\psi_0(\operatorname{Fr}_{(q)})
=\bar\psi_0(\operatorname{Fr}_{(q)})=-q,\qquad
\mathbf N(\operatorname{Fr}_{(q)})=q^2.
$$
所以在**四个原格上**，
$$
\boxed{\rho_\nu(\operatorname{Fr}_{(q)})=-q
\quad(\nu=0,1,2,3).}
\tag{6}
$$
特别最高项的 Tate twist $\mathbf N^{-1}$ 已包括在内：
$(-q)^3/q^2=-q$。如果用几何 Frobenius，则同一格上的值是 $-q^{-1}$；下面一直用算术 Frobenius，不能只倒换其中一个因子。

(6)是整 Galois 作用，不涉及以复 period 或 $p$-adic period 除过的分析积分。更换某条原格的固定基时，下面的 tame 坐标、Frobenius 坐标和点比较同时乘同一个标量，公式不变。R901 的 Hermitian 局部积分 $(q+1)/q^3$ 及其 Euler 正规化不在下面的 cocycle 公式中充当乘子。

## 2. 真正的局部域与所有上方素点

设 $v=(q)$ 是 $K$ 的唯一 $q$ 位。它在任何与 $q$ 互素的原 ring-class 层完全分裂：其 Artin 类由有理生成元 $q$ 表示，正是 ring-class 商中被除掉的类。此说法在原每个 wild 层同样成立；这是 R900(A10)–(A11) 的准确主理想陈述。

另一方面，
$$
G_q\simeq
\bigl(\mathbf F_{q^2}^{\times}/\mathbf F_q^\times\mu_6\bigr)_{(p)}
\simeq C_h,\qquad h=p^{v_p(q+1)}.
\tag{7}
$$
该商完全来自 $q$ 的惯性。因此 $K[q]_w/K_v$ 是 totally ramified、tame 的循环 $h$ 次扩张，剩余域保持
$$
k_v=k_w=\mathbf F_{q^2}.
\tag{8}
$$
这里“tame”指剩余特征 $q$，不表示 $h$ 是系数素数 $p$ 的单位。

于是，在固定旧层的每一个 $q_1$ 位上，$K[q_2]$ 给 $h_2$ 个不同素点；每个这样的素点再经 $K[q_1]$ 作(8)的全分歧扩张。不能将这 $h_2$ 个不同素点的 trace 写成单一局部 Frobenius 的长和。

下面使用原 Shapiro/Mackey 的完整分解。可以令 $G_2$ 的 coset lifts 在原固定格 $T$、$H_{34}$ 和旧层上都作用为一：$K[q_2]$ 只在 $q_2$ 分歧，其余这些域在 $q_2$ 不分歧；交域因(7)全惯性而为 $K$。有限层上先选这样的 lifts，涉及无限 Tate 域时由相容有限商和紧性选取。这样 $R_2$ 的标准坐标正是带原固定 $T$-frame 的全部 $q_1$ 上方素点。

若改用别的 coset lifts，必须同时作其真实 Galois 作用所给的 CM-frame 运输。下面的等式是 Shapiro 自然等式，因而在这种同步运输下仍成立；没有将系数域的共轭混入 point-factor 作用。

## 3. 单个新增位的准确 cochain 计算

先固定一个 $q$，省去下标。置
$$
Q=q^2,\qquad h=p^{v_p(q+1)},\qquad u=(q+1)/h.
$$
令 $\tau$ 是 tame pro-$p$ 惯性生成元，取向使其在原 induced/permutation 格 $R\otimes T$ 上准确作用为 $\sigma$。取算术 Frobenius lift $F$，使它在 $G_q$ 上的像为一。于是
$$
F\tau F^{-1}=\tau^Q,\qquad
F|_T=-q,\qquad \tau|_T=1.
\tag{9}
$$
选这样的 $F$ 是允许的：从任意 Frobenius lift 乘一个惯性 lift，就可消其 $G_q$ 分量。$F$ 在全分歧扩张的剩余域上仍是同一个算术 Frobenius。

可先除去作用平凡的 wild pro-$q$ 及 tame prime-to-$p$ 惯性；它们对这些 $p$-adic 格的正阶 cohomology为零。所需 tame relation 仍是(9)。所有 cocycle 使用
$$
z(gh)=z(g)+g z(h),\qquad
(\delta m)(g)=(g-1)m
\tag{10}
$$
的约定。

定义实际有限群环导数
$$
\mathfrak d=\sum_{i=1}^{h-1}i\sigma^i\in R.
$$
准确恒等式为
$$
(\sigma-1)\mathfrak d=h-N.
\tag{11}
$$
$h\mid Q-1$，故在 $R$ 中
$$
N_Q:=\sum_{i=0}^{Q-1}\sigma^i
=1+\frac{Q-1}{h}N,
\qquad N_Q=1\text{ 在 }A.
\tag{12}
$$

令 $z$ 为 $A\otimes T$-值 cocycle，写
$$
a=z(\tau),\qquad b=z(F)
$$
并在原 $T$ 基下读其系数。由 $F\tau=\tau^QF$、(10)得到
$$
(\sigma-1)b=(-q-N_Q)a=-(q+1)a.
\tag{13}
$$
乘 $\sigma-1$ 在 $A$ 上单射：在特征零各非平凡角色上可逆，而 $A$ 是 $\mathcal O$-torsion-free。因此(11)–(13)准确给
$$
\boxed{b=-u\,\mathfrak d\,a.}
\tag{14}
$$

反过来，每个 $a\in A$ 都给连续 cocycle，并非只形式地满足一个关系。取 $\widetilde a\in R$，令 $z_0$ 是 $R\otimes T$ 中的 unramified cocycle，
$$
z_0(\tau)=0,\qquad z_0(F)=uN\widetilde a.
$$
$N\widetilde a$ 被惯性固定，$F$ 在该线上为 $-q\in1+p\mathbf Z_p$，所以该 cocycle 从 unramified procyclic quotient 连续定义。然后
$$
z_R=\delta\widetilde a+z_0
$$
的 augmentation 在 $\tau,F$ 上均为零，因而它取值于 $I\otimes T$。以(4)的逆取回 $A\otimes T$，其两值恰为 $a,-u\mathfrak d a$。这也支付(14)的连续性及存在性。

Coboundary $\delta m$ 对 $a$ 的改变为 $(\sigma-1)m$；其 $F$ 值的改变按(11)与(14)准确相容。因此
$$
\boxed{
H^1(K_v,A\otimes T)
\xrightarrow[\ z\mapsto z(\tau)\ ]{\sim}
A/(\sigma-1)A\otimes T
=\bigl(\mathcal O/(h)\bigr)\otimes T.
}
\tag{15}
$$
最后等号采用同一个原 $T$ 基，不将 $T$ 换成新的分析规范。

## 4. 减 coboundary 的正号与 Shapiro 的单位

将(14)经 $j:A\to I\subset R$ 送入原 induced 格。由(11)，其两值为
$$
jz(\tau)=(\sigma-1)\widetilde a,\qquad
jz(F)=-u(h-N)\widetilde a.
$$
现在按(10)**减去** $\delta\widetilde a$，得到
$$
\boxed{
(jz-\delta\widetilde a)(\tau)=0,\qquad
(jz-\delta\widetilde a)(F)=+uN\widetilde a.
}
\tag{16}
$$
正号由
$-u(h-N)\widetilde a-(-q-1)\widetilde a
=uN\widetilde a$ 给出。不能改成 $-u$，也没有除 $h$。

原 Shapiro 映射在 identity coset 上 evaluation；$N\widetilde a=\epsilon(\widetilde a)N$。所以(16)在 $K[q]_w$ 上的准确 unramified Frobenius 坐标是
$$
\boxed{
u\,\epsilon(\widetilde a)\pmod{q+1}.
}
\tag{17}
$$
若换一个提升 $\widetilde a$，augmentation改变 $h$ 的倍数；乘 $u$ 后改变 $q+1$ 的倍数，所以(17)良定。

也可直接核目标群：在 $K[q]_w$ 上，$T$ 未分歧且 $F=-q$。惯性项
$\operatorname{Hom}(\mathbf Z_p(1),T)^F$
被非零标量 $-q-q^2$ 杀；$T$ torsion-free，故该项为零。于是
$$
H^1(K[q]_w,T)=H^1_{\rm unr}(K[q]_w,T)
=T/(q+1)T.
\tag{18}
$$
(15)到(18)的映射就是单位 $u$：
$$
\boxed{
H^1(K_v,A\otimes T)
\xrightarrow{\,H^1(j)\ {\rm and\ Shapiro}\,}
H^1(K[q]_w,T),\qquad
\bar a\longmapsto u\bar a.
}
\tag{19}
$$
两边都保留整 torsion 群；先张量特征零会使这个信息全部消失。

若原 reciprocity 整体取反，必须同步采用
$\sigma^{-1}-1=-\sigma^{-1}(\sigma-1)$ 及对应的 tame 生成元。这样是(19)的同一自然映射，不能只将一个显示因子取逆而保持其余坐标不变。

## 5. 原双新类：完整素点向量的单位读取

令 $\mathcal N_{12}$ 是 R900(A5) 的实际最高双新项。R901(B18)–(B19)已付唯一、整且饱和的提升
$$
\mathcal N_{12}^{\mathrm{aug}}
\in H^1(A_1\otimes A_2\otimes T),\qquad
\mathcal N_{12}=(\sigma_1-1)(\sigma_2-1)
               \mathcal N_{12}^{\mathrm{aug}}.
\tag{20}
$$
这里可以取一个原 finite wild 层；所有旧辅助群和旧层素点保留。

在一个固定旧层的 $q_1$ 位，$A_2$ 是常系数。将§3逐项张量 $A_2$，有
$$
H^1(K_{v_1},A_1\otimes A_2\otimes T)
\simeq (A_2/h_1A_2)\otimes T.
\tag{21}
$$
令 $a_{12}$ 表示**这枚原类**在(21)中的值，即其 tame cochain值再模 $\sigma_1-1$；不是一个自由选择的参数。

先在第一个因子用(19)，再在第二因子施 $j_2$，得到
$$
\boxed{
\operatorname{Mack}_{v_1}
 \bigl(\operatorname{loc}\mathcal N_{12}\bigr)
=u_1(\sigma_2-1)a_{12}
\in \bigl(R_2/(q_1+1)R_2\bigr)\otimes T.
}
\tag{22}
$$
$\operatorname{Mack}_{v_1}$ 是§2的完整局部 Shapiro 分解：右端有 $h_2$ 个标准坐标，分别对应 $K[q_1q_2]$ 在该旧层位上方的全部素点。对旧层的其它素点也分别使用(22)，不能只保留其中一份。

交换两个素数，准确得到
$$
\operatorname{Mack}_{v_2}
 \bigl(\operatorname{loc}\mathcal N_{12}\bigr)
=u_2(\sigma_1-1)a_{21}.
\tag{23}
$$
这里 $a_{12}$ 与 $a_{21}$ 来自同一全局类；本篇没有额外断言两者可互相任意指定。

$I_2\subset R_2$ 是 $\mathcal O$-饱和的，商为 $\mathcal O$。故
$$
A_2/h_1A_2\xrightarrow{\ \sigma_2-1\ }
R_2/h_1R_2
$$
仍单射，像为 $I_2/h_1I_2$。于是(22)不仅保非零，也保**整个局部元素的精确 $p$-幂阶**：
$$
\boxed{
a_{12}=0
\Longleftrightarrow
\operatorname{loc}_{v_1\ {\rm all\ places}}\mathcal N_{12}=0.
}
\tag{24}
$$
同理适用于(23)。这不是全局 localization 单射；它只准确比较(21)和原全局类在这些指定地方的像。

## 6. 单素原返回与 finite/wild Euler 全部相容

R900 的原单惰性最高类已经准确为
$$
D_q=c_q\operatorname{res}D_1,\qquad
c_q=-\frac{(q+1)^2}{qh}=-\frac{hu^2}{q}.
\tag{25}
$$
由(18)，其在新增 $q$ 的整局部值严格为零，因为 $c_q$ 是 $q+1$ 的整倍数：
$$
c_q=-(u/q)(q+1).
$$
因此(22)读取的双新局部余量不是误留了(25)的旧部分。

在 finite/wild 比较中也不丢普通 Euler。令 $\xi_n$ 为 R900(19) 的实际 $\sigma_{\bar{\mathfrak p},n}^{-1}$。原单位为
$$
\mathcal E_{p,n}=
\frac{(1+\bar\pi^{-1}\xi_n)
      (1+\bar\pi^{-1}\xi_n^{-1})^2
      (1+\pi\bar\pi^{-2}\xi_n^{-1})}
     {(1-\pi\bar\pi^{-1}\xi_n^{-2})
      (1-\pi/\bar\pi)^2}.
\tag{26}
$$
原 finite 和有界 wild 来源满足
$$
\operatorname{sp}_0\mathcal N_{12}^{\rm wild}
=\mathcal E_{p,n}\mathcal N_{12}^{\rm fin}.
\tag{27}
$$
这跟随 R897 的真实比较及 R900 的 Möbius式：在 restriction 项上，
$\mathcal E_{p,n}$ 按真实群环投影作用，正好等于较低层的同一单位，所以可以逐项比较。

(4)与 $\mathcal E_{p,n}$ 交换，(20)的提升唯一，故(27)在 $A_1\otimes A_2$ 的原提升上仍成立。再通过(21)，第一群因子取 $\sigma_1=1$，所以
$$
\boxed{
a_{12}^{\rm wild,sp}
=\left.\mathcal E_{p,n}\right|_{\sigma_1=1}
 a_{12}^{\rm fin}\quad\text{于 }A_2/h_1A_2.
}
\tag{28}
$$
显示乘数仍为单位，但没有被改写成一。其它旧群变量也仍在其中。

在所有有限 wild 层作上述计算时，$q_i$ 完全分裂。wild corestriction是全部上方素点之间的实际求和；(16)、(22)都与该求和相容。故这些公式适用于原有界系统的全部有限层及其真实逆极限。没有把完全分裂层的全局 trace 当成一个局部扩张上的乘度数。

## 7. 同一原格到 R859 点影子的准确含义

在 $H=H_{34}$ 的选定位上，$q$ 的剩余域仍是 $k=\mathbf F_{q^2}$。原 $E_0/k$ 满足
$$
\varphi_q^2=[-q],\qquad
E_0(k)=E_0[q+1].
\tag{29}
$$
R859 的实际 cross divisor 是
$$
D_{\varphi_q}
=\Gamma_{\varphi_q}-(E_0\times O)-q(O\times E_0).
\tag{30}
$$
与它相交并推第三轴，给原最高两条 CM 线
$$
c_q^{\rm geom}:
\Pi H^3_{\rm et}(E_0^3,\mathcal O)(2)
\xrightarrow{\sim}H^1_{\rm et}(E_0,\mathcal O)(1).
\tag{31}
$$
在固定 cup 规范下，矩阵为 $\operatorname{diag}(a,-b)$，其中 $ab=-q$，故行列式为 $q\in\mathcal O^\times$。这支付真正的整同构；不只比较 Frobenius 特征值。原 CM 符号投影及 $\eta_j^{\pm1}$ 的 point-factor 投影按 R859 同步保留。

R859 使用几何 Frobenius 时，两边的值为 $-q^{-1}$。改为本篇算术 Frobenius后准确为 $-q$，与(6)、(18)一致。有限域 Kummer 因而给
$$
H^1(k,H^1(E_0)(1))
\simeq E_0(k)\otimes_{\mathbf Z}\mathcal O,
\tag{32}
$$
其中只有 $p$-primary 部分留下。

将原固定 $T$ 经同一个 CM 比较送入(31)，再用(32)，便可把(22)的每个 Frobenius 坐标读成同一原类的点影子坐标。这里有两种尺度须明确：

- (15)–(28)以原 $T$ 或原 $\mathcal T$ 的格为准，完全是整等式。
- 若固定 CM/Chow 比较使用 R859 的清分母整数 $D$，则实际椭圆点读取的是 $D\mathcal N_{12}$，或等价地在原 scaled point lattice 中读 $\mathcal N_{12}$。该固定 $D$ 必须显示；不能因(31)整就删掉进入(31)之前的原对应尺度。没有随新增 $q_i$ 增长的 $q_i+1$ 成本由(31)产生。

对于已经给出的同源 Chow 代表，光滑良好约化目标上的 cycle specialization、AJ、交积及 Kummer 的相容性，准确把上述 cohomological读取认作
$$
(\operatorname{pr}_3)_*
 \left(\operatorname{sp}(D\mathcal N_{12})\cdot
       \operatorname{pr}_{12}^*D_{\varphi_q}\right).
\tag{33}
$$
源曲线在新增 $q$ 可以有坏约化；(33)须使用完整 specialized cycle和全部分支、重数，不能只取其平滑 open 或一条 generic 图形。R859 的原有限闭点 trace 规则亦全部保持。

本篇没有另行列出各新增层的 Jacobian Hom 坐标，也不以原首层的已定义坐标替代新层对应。(22)已经在 ACR 的原整 CM/Shapiro 格中成立；若用几何交点计算它，仍须提交同一层的实际代表和尺度。这是公式的实施输入，不是(22)的额外非零假设。

## 8. Mixed 槽为何不能随最高槽一起删除

(6)说明本篇局部 cochain计算对原四槽都适用，但 R900 的最高奇数新块消失不是整个对角来源消失。

原最高角色的中心根数为 $-1$；R832 的三个 mixed 因子在原基域具有非零中心值，根数为 $+1$。在一个实际非平凡、奇数阶惰性 ring-class 角色处，四个 unitary 未分歧根都是 $-1$。与 R900 相同的有限 Gauss 计算给新的局部根数比 $-1$；角色在其它旧坏位只给被有理 idèle/主 $\delta$ 条件消去的未分歧因子。因此单个实际新惰性扭曲的根数为
$$
\begin{array}{c|cc}
 &\text{原基角色}&\text{在该惰性位真正分歧的扭曲}\\ \hline
\text{最高槽}&-1&+1\\
\text{每个 mixed 槽}&+1&-1 .
\end{array}
\tag{34}
$$
这只是准确根数表，不赋任何导数或 AJ 非零。

R832 的 mixed Chow 收缩是实际
$H_+\otimes H_-\simeq\mathbb L$；有限 Artin base change后仍成立。
因此相应 mixed AJ 是原曲线/阿贝尔因子的点类，而最高槽仍是高权类。R832 在基域用 rank-zero杀掉 mixed 的论证，不能自动扩大到这些新增 ring-class 域。也没有一个已付的全局代数对应把 mixed 点类换成最高类。

若分别用含 $1/h$ 的单角色投影后再到有限域点群，可能把所需整 torsion 信息直接删除。正确顺序是先保(3)、(20)、(22)的全群环格和所有素点，再用(30)–(32)读取指定 CM 符号；这正是本篇采用 $A/I$ 整模型的理由。

## 9. 对原有界整除门的直接判据

在(22)中，局部群被 $h_1$ 杀掉。若 $a_{12}$ 的精确 $p$-幂阶为 $p^t$，其中 $1\le t\le v_p(q_1+1)$，则由(24)
$$
\boxed{
\mathcal N_{12}\notin
p^{\,v_p(q_1+1)-t+1}
 H^1(R_1\otimes R_2\otimes T).
}
\tag{35}
$$
否则其局部像的阶至多为 $p^{t-1}$，矛盾。尤其只要完整原点向量非零，就排除
$$
\mathcal N_{12}\in
(q_1+1)(q_2+1)\,
H^1(R_1\otimes R_2\otimes T).
\tag{36}
$$
原17惯性为 $-1$ 还给相关全局 H¹ torsion-free，所以这种非零局部读取也证明同一双新全局类有理非零。

(35)–(36)是针对**指定原来源**的可检验结论，不是给定了一个非零局部点。它们不证明原首层端点非零，不证明指定普通 $p$ 位的 localization非零，也没有决定 R893 的增广阶 $s$。特别，有限新增位 $q_i$ 的点读取与主目标中普通 $p$ 位的读数是两个不同映射。

本篇没有执行数学程序或扫描素数。

## 引用与规范来源

- [R901 附录 B](R901-original-inert-endpoint-test-matrix-and-local-period.md)：原 universal CM 商、$A\xrightarrow{\sigma-1}I$、原双新提升及全局饱和性。
- [R900](R900-original-inert-layer-parity-and-exact-one-prime-return.md)：原主理想 Frobenius、单惰性返回、最高根数奇偶、全部有限 ordinary Euler。
- [R886](R886-original-highest-cm-auxiliary-units-and-base-preserving-normalization.md)：(5)的原四条角色、固定 Artin 指数及 twist。
- [R897](R897-original-endpoint-complete-wild-tame-system-and-specialization.md)：同源完整 finite/wild 比较、原单位 $\mathcal E_{p,n}$、统一格与全部旧对应。
- [R832](R832-original-triple-chow-purity-and-rank-zero-contractions.md)、[R859](R859-original-supersingular-shadow-and-integral-aj-detection.md)：真实 mixed Chow 收缩、固定 CM 对应、整 Frobenius 除子及 AJ/Kummer 特殊化。
- Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*，[发表稿](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)，Theorem3.3、Corollary3.6、§4与§6：本篇沿其原系数/Shapiro约定；新的局部 cochain 同构由§3–5自含证明。
- Ellenberg–Logan–Srinivasan, *Certifying nontriviality of Ceresa classes of curves*，[作者全文](https://padmask.github.io/CertifyingCeresa.pdf)，Propositions2.10–2.11；实际 specialization 与交积相容的范围沿 R859 已核原文使用，不扩大其非零定理。
