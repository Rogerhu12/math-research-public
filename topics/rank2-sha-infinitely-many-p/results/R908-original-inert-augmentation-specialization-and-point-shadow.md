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


## 附录 A：原全群环来源在新增惰性位的几何特殊化

本附录的结论针对**同一个原有限 tame 来源**，包括任意旧的、与 p 互素的允许平方自由 tame 模数 n；它也适用于原双新块。它不把非平凡 finite wild 字符的几何呈示自动视为平凡 nebentypus 的同一模曲线。wild 系统在增广点的结论另由正文(28)准确运输。

### A.1 结论与固定尺度

令 $\widetilde{\mathcal D}_{nq}$ 为 R897、R900 中原 raw asymmetric diagonal 类，保原三个有序对、指定最高 CM 符号、二处 $q_0/q_2$ 端点、全部旧群变量和实际 Shapiro 坐标。这里本附录的新增有理素数记作 q；它与原二处退化映射的下标无关。假设
$$
p>211,\qquad q\nmid30\cdot34pn,\qquad q\text{ 在 }K=\mathbf Q(\omega)\text{ 中惰性},
\qquad h=p^{v_p(q+1)}>1,\quad u=(q+1)/h.
\tag{A1}
$$

**定理。** 存在一个只依赖原固定三组 tame/CM 对应及其格规范的正整数 D，与 p、n、q 无关，使每个原上方素点均满足
$$
\boxed{
D\,\operatorname{loc}_{q}\widetilde{\mathcal D}_{nq}=0.
}
\tag{A2}
$$
此式保留整个 $\mathcal O[G_q]$ 和全部旧群环坐标；不是先投到 $A_q=R_q/(N_q)$ 后的零。

特别，对正文的同一个有限 tame 双新类和其唯一增广提升，
$$
\boxed{
D\,\operatorname{loc}_{q_1}\mathcal N_{12}^{\rm fin}=0,
\qquad
D\,a_{12}^{\rm fin}=0\quad\text{于 }A_2/h_1A_2.
}
\tag{A3}
$$
故在 $p\nmid D$ 时，$a_{12}^{\rm fin}$ **确实为零**；在 $p\mid D$ 时，只得到其阶整除 $p^{v_p(D)}$。这个界与新增素数及旧层无关。没有计算出 D 的最小值，不能把“$p>211$”直接替代“$p\nmid D$”。

正文(28)还给
$$
D\,a_{12}^{\rm wild,sp}=0.
\tag{A4}
$$
这里是原有界 wild 来源的真实增广特殊化，不是其全部非平凡 finite wild 字符值。

以下证明(A2)，再说明(A3)–(A4)。关键是先保完整群环的 CM 映射，不能只证明其 new quotient 在 ordinary 分量上为零：正文(17)的 $N_q\widetilde a$ 本来就会被 $R_q\to A_q$ 删除。

### A.2 原 universal CM 提取给真正的 p-adic Hom

在原第一槽使用 ACR Theorem 3.3、Corollary 3.6 的整同构
$$
\mathcal Q_n=
\mathcal O[R_n]\otimes_{\varphi_n,\mathbb T'}
 H^1_{\rm et}(Y(1,N_\psi(n^2))_{\overline{\mathbf Q}},
                   \mathbf Z_p(1))
 \xrightarrow{\ \nu_n\ }
 \operatorname{Ind}_{K[n]}^{\mathbf Q}
       \mathcal O(\psi_{\mathfrak P}^{-1}),
\tag{A5}
$$
其中固定 conductor 的有限角色提取沿 R897 保留。原 $\psi_{\mathfrak P}^{-1}$ 是 $E_{17}:y^2=x^3+17$ 的指定 Tate 模 CM 线；这里的倒数来自 ACR 的几何 Artin 约定，不能把它改成另一个 CM type。

ACR Lemma 3.5 的 non-Eisenstein 商杀掉开模曲线的 boundary。因此(A5)的各 Mackey 坐标是紧化 Jacobian 的整 Tate 模上的商映射。加上固定 CM 符号幂等元，或同时保留共轭符号，得到到 $T_pE_{17}\otimes\mathcal O$ 的真正 Galois-equivariant 映射。若用 Weil restriction 表述，共轭 CM 符号上的群坐标须同时取逆；这里按实际 Mackey 坐标处理，不将两符号误认成同一个未经反转的 R-linear 置换模。

所需的整 Hom 事实如下。对数域 F 上的阿贝尔簇 B,C，
$$
\operatorname{Hom}_F(B,C)\otimes\mathbf Z_p
 \xrightarrow{\sim}
\operatorname{Hom}_{G_F}(T_pB,T_pC).
\tag{A6}
$$
Faltings 的有理同态定理给满的 $\mathbf Q_p$ 像；整像的饱和性也可直接核定。若实际同态 f 的 Tate 映射被 p 整除，则 $f|_{B[p]}=0$，故 f 经 $[p]:B\to B$ 因子化，因子仍定义于 F。对 $\mathbf Z_p$ 完成先取模 p 的实际同态代表，再重复此论证，得整像饱和；与有理满射合用即为(A6)。有限自由的系数扩张到 $\mathcal O$ 保持它。这个证明不会引入依赖 n 或 q 的 Jacobian 同源次数。

于是，过原定义域 $H_{34}K[n]$，(A5)的每个坐标准确由
$$
F_n\in\operatorname{Hom}(J(C_n),E_{17})\otimes\mathcal O
\tag{A7}
$$
实现，保所有旧群坐标。第二、三槽由原固定 Hecke–CM 对应实现为到 $E_0$ 的同样有限组 Hom，记为 $G_n,H_n$；其曲线输入仍是原 asymmetric 端点。基点取原 cusp。曲线级表达允许有限线性组合；它不是断言每个 p-adic 系数都是一个单独的代数态射。

这一表述足以作整特殊化：将(A7)在任意 $p^v$ 精度写成有限个实际同态的整组合，再各自特殊化。有限域点的 p-primary 部分在足够高精度后不再改变。Hom 的同源规范、corestriction 和下面的点读取均与此连续过程相容。因此不能先把 Hom 张量 $\mathbf Q_p$、再把有限域点群的 torsion 删掉。

### A.3 为什么清分母可以统一为一个固定整数

这里补清 R897 §9 的 $p^{-c_p}$ 在本附录所需的跨 p 来源。

先在特征零一次固定：

1. 原三个 tame Hecke 因子及其整 Betti 格、原 $E_{17}$ 和两份 $E_0$ 的整格；
2. R832/R839 使用的有限组实际 CM 对应、其逆及原指定 coefficient field 的整格；
3. 原 $X_1/X_0$、old-copy 返回、CM 符号和固定 $\vartheta_5/C_5$，其中 $C_5=-216$；
4. 第一槽在 n=1 与原 $E_{17}$ Tate 模的固定校准。

这些都是**固定有限维有理或代数数矩阵**。取正整数 $D_{\rm src}$ 清掉这些矩阵的全部分母和有限格指数，再取 $D_{\rm ret}$ 清掉反向比较的同样有限组分母。原 $1632,816,6,12,18,216$ 等固定倍率可以全部并入二者；不要求此选择最小。

对于第四项，可在固定 level 的整 Betti Hecke 格上取原有理幂等元，清其分母，再与 $E_{17}$ 的整同态格比较。两个固定格的指数由一个固定非零整数控制。到任一 p 后，(A5)在 n=1 的校准与此固定比较的差别只有相应格指数和一个 p-adic 单位。这个单位可在同一个 norm-compatible 系统中一起运输；它不增加分母。ACR 的 $\nu_n$ 对所有 n 本身整，故此后不再逐层付任何 isogeny 指数。权 $(2,2,2)$ 的系数阶乘是1，原有限 tame 图形、退化、restriction 和 corestriction 也全整。

若某个固定对应的曲线级选择另留下 cusp 平移，有限组这样的固定 cusp 像由 Manin–Drinfeld 为 torsion，可将其**实际共同阶**并入 $D_{\rm src}$；不以定义域次数猜其阶。本题原第二、三轴本已从 $X_0(2601)$ 的基点映射，经 R831 的实际 $q_0/q_2$ 拉回，忘掉固定 $\Gamma_1$ 生成元后 diamond 逐点不变，因而不需这项额外放大。更一般地，若只先知道固定 diamond d 在 Hom 上为1，写 $Gd=G+T_d$；由 $d^m=1$ 逐次复合可得 $mT_d=0$。这才是用固定 diamond 群阶控制该常数的依据，不是一个 Galois 域次数论证。

取
$$
D=D_{\rm src}D_{\rm ret}
\tag{A8}
$$
并在必要时乘上述固定共同阶。它与 p,n,q 无关。后文先用 $D_{\rm src}$ 实现原几何来源，最后用 $D_{\rm ret}$ 返回原格；所以(A2)准确使用 D。若另人为扩大一个稳定格，仍须按正文 §7 标注该尺度；这里没有将任意选择的扩大格称作固定全球整格。

### A.4 原全 CM trace 是 Hom 等式，不只是 AJ 范数

固定一个旧 prime-to-p tame 层 n，并逐一保其原坐标；n 包含原允许的 split 与 inert 因子，但 q 不在 n 中。因为 $(q)$ 是有理主理想，q 在所有原 prime-to-q 环类域中完全分裂；特别在 $H_{34}K[n]$ 的选定位，剩余域是
$$
k=\mathbf F_{q^2}.
\tag{A9}
$$
新增 $G_q$ 的 h 部分在此位全分歧。原 $\psi_{\mathfrak P}^{-1}$ 在 q 不分歧。

ACR 刊本 p12 的 inert CM norm 为
$$
\pi_{11*}-\frac{\psi((q))[(q)]}{q^2}\pi_{22*}
 =\pi_{11*}+q^{-1}\pi_{22*},
\tag{A10}
$$
因为原 $\psi((q))=-q$、$[(q)]=1$。令 $\pi_0=\pi_{11}$、$\pi_2=\pi_{22}$。由(A5)的 norm 图及(A6)的忠实性，得到完整坐标的同态等式
$$
\boxed{
\sum_{\sigma\in G_q}F_{nq}^{\sigma}
 =F_n\circ\pi_0+q^{-1}F_n\circ\pi_2
 \quad\text{于 }\operatorname{Hom}(J(C_{nq}),E_{17})\otimes\mathcal O .
}
\tag{A11}
$$
它不含 $1/h$，也不先作角色幂等分解。原第一 CM 符号、所有旧变量和原 fixed-conductor 提取都在(A11)中。

取基点后可将(A11)写为曲线级等式；若在特殊分量上更换其基点，保留下来的就是下一节明确处理的常数。以下只在无挠 Hom 群中约 h，不在有限点群中约 h。

### A.5 真正 full-q 覆盖、q−1 次数与算术惯性

用 ACR §2.1 的真实 $z\mapsto qz$，把 $C_{nq}$ 的 q 部分改写成 ordered split-Cartan level，即中心椭圆曲线上的两个不同 cyclic q 直线 x,y。固定旧的细模问题 $\mathcal P$，它在 q 处有限 étale；原固定 $\Gamma_1$ tame level 已使其 representable。

在包含 $\zeta_q$ 的局部基域上取**固定 Weil pairing**的 full-q 覆盖
$$
\widetilde C_{nq}\longrightarrow C_{nq}.
\tag{A12}
$$
给定两条直线，先选第一条的生成元，再由 Weil pairing 唯一确定第二条生成元，所以(A12)的次数恰为 q−1。这里是细模曲线，不除去一个未经记账的中心。若另用 projective/adelic 呈示，其固定中心次数必须在上下两次 push/pull 中同时保留。由(A1)，q−1 是 p 单位。

Edixhoven–Parent 的完整模型在 tame 全分歧扩张后有 q+1 组 Igusa 分量，按 $L\in\mathbf P^1(\mathbf F_q)$ 标记，另有每个 supersingular 点上的 Drinfeld 分量及可能的有理解消链。每组 Igusa 的正规化是原细模问题的 Igusa 曲线；忘掉 Igusa 生成元到旧曲线的**总次数是 q−1**。若某组不几何连通，这句话指所有分量次数之和。

这里使用的是 EP §2.2.4(12)–(13) 的**算术 Galois 惯性**：其 $\mu_{q+1}$ 子群在每个 Igusa 分量上点态恒等，而在 Drinfeld 分量上通常非平凡。新增 h 次惯性位于这个子群中。因此，目标 $E_{17}$ 良好约化时，
$$
F_{nq}^{\sigma}|_{I_L}=F_{nq}|_{I_L}
\quad(\sigma\in G_q).
\tag{A13}
$$
这是完整 R 的每个真实坐标的相同性。有限 $\mathrm{GL}_2(\mathbf F_q)$ 中的非分裂 torus 是另一种作用，不能拿它替代(A13)；后者在分量标签上反而可能传递。

所有实际同态到良好约化的椭圆曲线均延拓并特殊化；也可由半阿贝尔 Jacobian 的 Hom 延拓得到。按 A.2 的模 $p^v$ 近似，同样适用于 p-adic Hom。为取半稳定模型所作的全分歧基变不改变剩余域；本文是在该模型上计算原 cycle 的特殊化及 proper push，不通过“限制到 h 次局部扩张后类为零”反推原类为零。

### A.6 每个 ordinary 分量的原端点与第一 Hom

令 $\pi_I:I_L\to C_n$ 为上一节的旧曲线映射。采用 EP 的 exotic Igusa 呈示：
中心椭圆曲线写作 $E_b^{(q)}$；直线 L 对应 connected kernel。沿 L quotient 得 $E_b^{(q^2)}$，沿其余直线 quotient 得 $E_b$，并保由 isogeny 运输的旧素于 q 的 level。因原第二、三形式平凡 nebentypus，固定 diamond 已按 A.3 支付。

以 x 为 $\pi_0$ 的 connected 情形、y 为 $\pi_2$ 的 connected 情形，两个原退化映射的表为
$$
\begin{array}{c|ccc}
 &L=x&L=y&L\ne x,y\\ \hline
\pi_0&\operatorname{Fr}_{q^2}&1&1\\
\pi_2&1&\operatorname{Fr}_{q^2}&1 .
\end{array}
\tag{A14}
$$
两条固定目标 $E_0,E_{17}$ 在 q 均有 $a_q=0$，故其 $q^2$ 幂 Frobenius 态射为 $[-q]$。实际两旧轴因此为
$$
G_{nq}|_{I_L}=b_LG_n\pi_I,\qquad
H_{nq}|_{I_L}=c_LH_n\pi_I,
\quad
(b_L,c_L)=(-q,1),(1,-q),(1,1).
\tag{A15}
$$
此处按原 $q_0/q_2$ 和三有序对逐项应用；新增 q 与这些二处对应交换。

把(A13)–(A14)代入(A11)，先取每个分量的 Jacobian Hom 部分：
$$
h\,\overline F_{nq}|_{I_L}
 =r_L\,\overline F_n\pi_I,\qquad
(r_x,r_y,r_o)=\left(-\frac{q^2-1}{q},\,0,\,\frac{q+1}{q}\right).
\tag{A16}
$$
$\operatorname{Hom}(J(I_L),E_{17})\otimes\mathcal O$ 无挠，且每个 $r_L/h$ 已是整 p-adic 数。因此
$$
\overline F_{nq}|_{I_L}=a_L\,\overline F_n\pi_I,\qquad
(a_x,a_y,a_o)=\frac uq\bigl(-(q-1),0,1\bigr).
\tag{A17}
$$
回到曲线映射，可以有常数项：
$$
F_{nq}|_{I_L}=a_LF_n\pi_I+C_L.
\tag{A18}
$$
不将 $C_L$ 默认为零，也不需要在有限点群中约 h。下面允许其含任意 p-primary 常数部分。

### A.7 原旧 CM 两轴给精确 degree-zero，而非一般 supersingular 平移不变

这里将正文 §7 的轴循环置换为“第二、三轴收缩，推第一轴”。这一三循环在三个奇 cohomology 因子上符号为正；第一轴暂保原 $E_{17}$，它到 $E_0$ 的固定 CM 同构及原 Artin/周期规范仍计入(A8)。在最后两份 $E_0$ 上取正文(30)的真实双刚化 cross 除子
$$
D_\varphi=\Gamma_\varphi-E_0\times O-q(O\times E_0),
\qquad \varphi=\operatorname{Fr}_q,\quad
\varphi^2=[-q],\quad \varphi^\dagger=-\varphi.
\tag{A19}
$$
对任意一对在特征零原旧曲线上定义、到 $E_0$ 的实际映射 G,H，置
$c=H_*G^*$。在特征零
$$
c\in\operatorname{End}^0(E_0)=K.
$$
其约化仍是这个 CM 元的约化，而不是任取一个 supersingular quaternion 同态。次数极化公式给
$$
\begin{aligned}
\deg(G,H)^*D_\varphi
&=\deg(H-\varphi G)-\deg H-q\deg G\\
&=-\operatorname{Tr}(c\varphi^\dagger)
 =\operatorname{Tr}(c\varphi)=0 .
\end{aligned}
\tag{A20}
$$
最后一步自含如下：$\delta=1+2\omega$ 满足
$\varphi\delta=-\delta\varphi$，而 c 与 $\delta$ 交换。故用 $\delta$ 共轭把 $c\varphi$ 送到其负，reduced trace 不变，因而为零。对固定系数线性组合逐项成立。任意有限 cover 的拉回同样保持次数零。

定义当前点读取
$$
\mathscr S(F,G,H)=F_*\bigl((G,H)^*D_\varphi\bigr)
\in E_{17}(k)\otimes\mathcal O,
\tag{A21}
$$
其中 push 后取 Albanese，全部 CM 符号投影沿正文 §7 保留。$D_\varphi$ 的刚化使第二、三槽为 Poincaré 双线性；故(A15)的两个标量相乘。由(A20)，把第一槽 F 换成 $F+C_L$ 对(A21)的改变量恰为
$$
C_L\cdot\deg(G,H)^*D_\varphi=0.
\tag{A22}
$$
这支付(A18)的全部常数项，包括可能的 h 阶常数点。

(A20)的 char0 CM 来源至关重要。超奇异纤维上的任意两个映射，其组合可以在整个 quaternion End 中，此时次数未必零；因此不能用 R839 的特征零最高投影平移不变，直接替代本节的计算。

### A.8 全 Igusa 求和及 q−1 覆盖的准确返回

记
$$
\mathscr S_n=\mathscr S(F_n,G_n,H_n).
$$
对固定 L 的全部 Igusa 分量使用 projection formula、(A15)、(A17)、(A22)，其总贡献是
$$
(q-1)\,a_Lb_Lc_L\,\mathscr S_n.
\tag{A23}
$$
q−1 是 $\pi_I$ 的总次数。另一方面，(A12)把原 source cycle 拉到 full-q 源后，再推回恰乘 q−1。因为它是 p 单位，完整返回可除且只除这个显示的 q−1。

于是普通部分的原点读取为
$$
\begin{aligned}
\mathscr S_{\rm ord}
 &=\left(a_x(-q)+a_y(-q)+(q-1)a_o\right)\mathscr S_n\\
 &=\left(u(q-1)+\frac{u(q-1)}q\right)\mathscr S_n\\
 &=\boxed{\frac{(q-1)u(q+1)}q\,\mathscr S_n}.
\end{aligned}
\tag{A24}
$$
表中一般位置有 q−1 个；不能漏掉这个计数。也不能把 full-q 覆盖的 q−1 与原共同目标的 $q(q+1)$ 混为一谈。式(A24)是在当前细模／固定 Weil pairing 规范下的局部 special-fibre 计算，不将它误认成原全局 raw corestriction 的负号系数。

由于 q 在所有旧环类定义域完全分裂，$\mathscr S_n$ 定义于(A9)的 k；固定 coefficient field 只作标量。又
$$
E_{17}(k)=E_{17}[q+1].
\tag{A25}
$$
因此(A24)在完整有限点群的 p-primary 部分中确实为零。这里乘的是 q+1，没有将点群张量 $\mathbf Q_p$，也没有先约去 h。

### A.9 全部 Drinfeld 分量、解消链和基点项

在每个 Drinfeld 分量上，两条旧退化映射的底层椭圆曲线及素于 q 的旧 level 固定；它们都落在旧模曲线的 supersingular 点。因而第二、三轴 $G_{nq},H_{nq}$ 是常值。将任意 line bundle 沿一个常值映射拉回，得到平凡 line bundle，所以
$$
(G_{nq},H_{nq})^*D_\varphi=0
\quad\text{于该分量的 }\operatorname{Pic}.
\tag{A26}
$$
即便第一 CM 映射在该 Drinfeld 分量上非恒定，也没有贡献。这不依赖其亏格或任何 new quotient 的范数。

有理解消链同样无贡献：到椭圆曲线的映射恒定；或者直接沿其到稳定模型的 contraction 使用(A26)。完整 special fibre 的 multiplicities 均在 proper push 中保留。交点、cusp 和节点不产生被遗漏的额外一维 cycle；对目标上的 Cartier line bundle 使用 projection formula，就是各正规化分量上上述拉回的总和。

原 modified-diagonal 的基点项也没有额外影子。实际三映射以原 cusp 为基点；含一个零坐标的项被三份 $h^1$ 提取杀掉，且(A19)在两条坐标轴上刚化为平凡。若改用任何固定 cusp 呈示，其固定对应/平移成本已在 A.3 记录，不能再在这里加入一个随 q 变化的基点归一。

合并(A24)–(A26)，得到完整 full-R 原点向量的零。经过 R859 的同一整 Frobenius 收缩，它在最高 CM 块上的行列式为 q，是 p 单位；再使用(A8)的固定反向尺度，得(A2)。每个 Mackey 坐标和每个原上方素点均作了同一计算，所以不是只证明一个 trace 或一个角色平均为零。

### A.10 双新、任意有限新集合与 wild 增广的准确后果

在原双新 Möbius 展开中，含 $q_1$ 的 raw 项由(A2)在 $q_1$ 局部消失。未含 $q_1$ 的项带原返回因子
$$
c_{q_1}=-\frac{(q_1+1)^2}{q_1h_1}
       =-\frac{u_1}{q_1}(q_1+1).
\tag{A27}
$$
这些旧项在 $q_1$ 不分歧，其原局部最高格的 Frobenius 是 $-q_1$，故局部点／Frobenius 商被 $q_1+1$ 杀掉。所有 restriction 与其它旧群变量保持，遂得(A3)第一式。

正文(22)给
$$
\operatorname{loc}_{q_1}\mathcal N_{12}
 =u_1j_2(a_{12}),\qquad
j_2:A_2/h_1A_2\hookrightarrow R_2/h_1R_2.
$$
$u_1$ 为单位，$j_2$ 为整饱和嵌入，故(A3)第二式随即成立。此处并非把 $R_1\to A_1$ 的局部 quotient-zero 当成 $a_{12}=0$。

同理，对任意有限新增惰性集合 S，在任一 $q_i\in S$ 的完整 Möbius展开中，含 $q_i$ 的 raw 项用(A2)，不含者用(A27)。因此
$$
D\,\operatorname{loc}_{q_i}\mathcal N_S=0.
\tag{A28}
$$
其余 $j_j$ 的张量积仍整、饱和且模 $h_i$ 单射，所以相应全部增广坐标也被 D 杀掉。此处“全部”指原同一有限 tame 系统的完整坐标，不包括未经本附录证明的非平凡 finite wild 几何层。这个简短归纳没有另行扩大原 finite 来源。

最后，正文(28)的实际 ordinary Euler 是单位，且与全群环嵌入、局部坐标和增广特殊化相容，故直接给(A4)。对非平凡 wild 字符层，one-sided ordinary ray、其 nebentypus 及 half-norm twist 应另作几何证明；本附录不凭增广点的零将它们省掉。

(A2)–(A4)、(A28)只关闭这些**新增惰性位的实际局部读取**。它们不说明原 $\mathcal N_S$ 全局为零，不给该全局类新的 scalar 可除性，不证明首层端点为零或非零，也不决定 R893 的 s。指定普通 p 位的 localization 仍是另一个映射。

### 本附录的 primary 依据与精确位置

- Edixhoven–Parent, *Semistable Reduction of Modular Curves Associated with Maximal Subgroups in Prime Level*, Documenta Math. **26** (2021), 231–269，[发表全文](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)。§2.1，printed pp.234–236 的 exotic Igusa 呈示及 Theorem 2.1；§2.2 的完整 Igusa/Drinfeld 模型；§2.2.3 的有限线性群作用；§2.2.4，printed pp.243–244，(12)–(13) 的算术惯性作用。本文使用后者的点态固定，不把它换成非分裂 torus 的作用。
- Alonso–Castella–Rivero，前引 [JIMJ 发表稿](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)。§2.1–2.2 的真实 $z\mapsto qz$ 与退化；printed pp.11–14 的 Theorem 3.3、Lemma 3.5、Corollary 3.6 及 p12 inert norm；Definition 4.3、Lemma 4.4、Proposition 4.5 的原 asymmetric 来源。其 norm 是 Hom trace 的输入；特殊纤维的常数、次数零与完整求和在本附录单独证明。
- Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. **73** (1983), 349–366，DOI [10.1007/BF01388432](https://doi.org/10.1007/BF01388432)，[原文](https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf)。printed p349 的同态定理，及 §2 Lemma 1 的半阿贝尔 Hom 延拓。A.2 另给本题所需整饱和性的论证。
- 原 [R832](R832-original-triple-chow-purity-and-rank-zero-contractions.md)、R839 的固定权一 CM 对应；[R859](R859-original-supersingular-shadow-and-integral-aj-detection.md) 的整 Frobenius 收缩／AJ–specialization；[R897](R897-original-endpoint-complete-wild-tame-system-and-specialization.md) 的原 finite 来源、全部尺度与 whole wild 比较。正文(28)是本附录唯一使用的 wild 特殊化公式。

本附录只有符号证明，没有执行数学程序或作素数扫描。
