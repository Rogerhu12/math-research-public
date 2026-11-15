# R724 — 原第一 wild 中央值的解析平均与非实 anti-Fermat 补偿

日期：2026-11-15。**状态：以下原 Hecke 角色、理想上的完整导子 $p^2$ 相位、权二 Mellin 平均及非齐次补偿恒等式已证明。非实残差的严格非消失或足够小的界仍未证明。本篇不把原 $j_{34}=0$ 变成第一 wild 层为零。**

本篇沿用 [R716](R716-original-wild-global-theta-period-and-exact-central-l-value.md) 的原 $S_{34}$、全 $2/3/17$ Schwartz 向量、CM 周期、Hall 提升及局部角色。这里平均的不是任选辅助 Hecke 族，而是同一个原 Hall 周期所给的 $p-1$ 个中央值。

## 1. 固定原角色与完成导子

设
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
E:y^2=x^3+17,\qquad
p>101,\quad p\equiv5\pmod6.
$$
令 $\psi=\psi_{17}$ 为原无穷型 $(1,0)$ Hecke 角色，其有限导子为
$$
\mathfrak f_0=(2\delta\cdot17).
\tag{1}
$$
所有理想和均在非零整理想上，且省去与所示有限导子不互素的理想。原 CM theta 级数
$$
f_\psi(z)=
 \sum_{(\mathfrak a,\mathfrak f_0)=1}
       \psi(\mathfrak a)e^{2\pi iN\mathfrak a z}
 =\sum_{n\ge1}a_n e^{2\pi inz}
\tag{2}
$$
就是原 $E$ 的权二新形式，$a_1=1$。其等级为
$$
N_0=|D_K|N\mathfrak f_0=36\cdot17^2,
\qquad
Q_0=\frac{\sqrt{N_0}}{2\pi}=\frac{51}{\pi}.
\tag{3}
$$
原根号为 $+1$。R290/R298 的原零权平方公式及
$S_{34}(0)=0$ 给
$$
L(\psi,1)=0.
\tag{4}
$$
本篇只使用这个已经支付的原复中央零，不增加任何新的 $p$-adic 中央零。

R716 的实际角色记为
$$
\nu_{p,r}=\widetilde\eta_{p,r},
\qquad r\in\mathbf F_p^\times.
$$
它在 $p$ 处为 $\chi_{p,r}^2$，有限导子恰为 $(p^2)$，阶恰为 $p$。因此 $\psi\nu_{p,r}$ 的完成函数为
$$
\Lambda_r(s)
 =(Q_0p^2)^s\Gamma(s)L(\psi\nu_{p,r},s),
\qquad
\Lambda_r(s)=\Lambda_r(2-s).
\tag{5}
$$
其对应权二形式的等级是 $N_0p^4$，不是 $N_0p^2$。角色是反圆分的，且原 $\psi$ 满足共轭自对偶关系，所以这些权二形式的系数为实数。R716 逐处 theta/epsilon 证明给 (5) 的符号 $+1$；没有从阶 $p$ 或仅从导子奇偶猜根号。

## 2. 理想上的原 anti-Fermat 条件

对 $v\in(\mathcal O_K/p^2)^\times$，保持
$$
q_p(v)=\frac{v^p/\bar v-1}{p}\pmod p,\qquad
\chi_{p,r}(v)=
 e_p\!\left(\operatorname{Tr}_{\mathbf F_{p^2}/\mathbf F_p}
             \frac{34r}{2\delta}q_p(v)\right).
\tag{6}
$$
因为 $h_K=1$，任意与 $p$ 互素的理想 $\mathfrak a$ 可写为 $(\alpha)$。定义
$$
\ell_p(\mathfrak a)
 =-\operatorname{Tr}_{\mathbf F_{p^2}/\mathbf F_p}
             \frac{34}{\delta}q_p(\alpha)
 =-\frac{34}{\delta}\bigl(q_p(\alpha)-\overline{q_p(\alpha)}\bigr)
 \in\mathbf F_p.
\tag{7}
$$
乘生成元的六次单位不改变 (7)：当前 $p\equiv-1\pmod6$，对 $\epsilon\in\mu_6$ 有 $\epsilon^p=\bar\epsilon$，故 $q_p(\epsilon)=0$。

在 R716 的全局 idèle 规范下，原局部 $p$ 字符是 $\chi_{p,r}^2$，而理想 idèle 与全局 $\alpha$ 的比在 $p$ 处为 $\alpha^{-1}$。因而
$$
\boxed{\quad
\nu_{p,r}(\mathfrak a)
 =\chi_{p,r}(\alpha)^{-2}
 =e_p\bigl(r\ell_p(\mathfrak a)\bigr).
\quad}
\tag{8}
$$
若整体采用相反的 Artin 约定，(7)–(8) 同时反号；以下全 $r\ne0$ 的平均及零指示完全不变。没有把原 Hecke twist 的平方漏掉。

条件 $\ell_p(\mathfrak a)=0$ 等价于
$$
q_p(\alpha)=\overline{q_p(\alpha)},
\tag{9}
$$
亦等价于真正的二位条件
$$
\frac{\alpha^{p+1}-\bar\alpha^{p+1}}p
       \equiv0\pmod p.
\tag{10}
$$
这里使用
$$
q_p(\alpha)-\overline{q_p(\alpha)}
 =\frac{\alpha^{p+1}-\bar\alpha^{p+1}}
         {p\,N\alpha}\pmod p,
$$
且 $N\alpha$ 为 $p$-单位。式 (10) 不能改成仅模 $p$ 的范数条件。

尤其，改变一个模 $p$ 代表的任意主单位提升会改变该条件：
$$
q_p(v(1+pz))=q_p(v)-\bar z\pmod p.
\tag{11}
$$
所以 (7) 读取的是原理想生成元的真实模 $p^2$ 值。没有把它换成任选 Teichmüller 提升。平均所投出的只是这个完整角色的 anti 部分；并未声称其余 Fermat 商或实际范数的第二位可由固定同余类控制。

对任意正整数 $a$、$(a,p)=1$，$q_p(a)\in\mathbf F_p$，故有理主理想 $(a)$ 总满足 (9)。但 (9) 也可能有非实生成元；这些理想会全部留在下文残差中。

## 3. 权二中央值的准确指数和

定义原未扭的平滑理想和
$$
S_0(X)=
 \sum_{(\mathfrak a,\mathfrak f_0)=1}
       \frac{\psi(\mathfrak a)}{N\mathfrak a}
       e^{-N\mathfrak a/X},
\qquad X>0.
\tag{12}
$$
其系数满足 $|\psi(\mathfrak a)|=(N\mathfrak a)^{1/2}$，所以对每个正 $X$ 绝对收敛。

对原扭曲形式，Mellin 积分在 $t=(\sqrt{N_0}p^2)^{-1}$ 分开，再用 (5) 的权二 Fricke 变换，严格得到
$$
\boxed{\quad
L(\psi\nu_{p,r},1)=
 2\sum_{(\mathfrak a,\mathfrak f_0p)=1}
       \frac{\psi(\mathfrak a)\nu_{p,r}(\mathfrak a)}
            {N\mathfrak a}
       \exp\!\left(-\frac{N\mathfrak a}{Q_0p^2}\right).
\quad}
\tag{13}
$$

为固定正规化，若 $f(iy)=\sum a_n e^{-2\pi ny}$、等级为 $N$ 且根号 $+1$，则
$$
L(f,1)=2\pi\int_0^\infty f(iy)\,dy.
$$
权二变换 $f(i/(Ny))=Ny^2 f(iy)$ 将 $0<y<N^{-1/2}$ 的积分准确变成 $y>N^{-1/2}$ 的同一积分。积分每个指数项便给 $2a_n e^{-2\pi n/\sqrt N}/n$，即 (13)。这里没有使用渐近的近似函数方程，也没有另一个未写的对偶和。

同一换元对 (12) 在任意分割点给
$$
S_0(X)+S_0(Q_0^2/X)=L(\psi,1)=0.
\tag{14}
$$
特别
$$
S_0(Q_0)=0,\qquad
S_0(Q_0p^2)=-S_0(Q_0/p^2).
\tag{15}
$$

## 4. 全部第一 wild 角色的实际平均

令
$$
\begin{aligned}
\mathcal Z_p
 &=\sum_{\substack{(\mathfrak a,\mathfrak f_0p)=1\\
                   \ell_p(\mathfrak a)=0}}
        \frac{\psi(\mathfrak a)}{N\mathfrak a}
        e^{-N\mathfrak a/(Q_0p^2)},\\
\mathcal S_p
 &=\sum_{(\mathfrak a,\mathfrak f_0p)=1}
        \frac{\psi(\mathfrak a)}{N\mathfrak a}
        e^{-N\mathfrak a/(Q_0p^2)},\\
\mathcal M_p
 &=\frac1{p-1}\sum_{r\in\mathbf F_p^\times}
                   L(\psi\nu_{p,r},1).
\end{aligned}
\tag{16}
$$
式 (8) 及实际有限 Fourier 正交性给
$$
\frac1{p-1}\sum_{r\ne0}\nu_{p,r}(\mathfrak a)
 =\frac{p\,\mathbf1_{\ell_p(\mathfrak a)=0}-1}{p-1}.
\tag{17}
$$
由于 (13) 的绝对收敛，可交换有限平均与理想和：
$$
\mathcal M_p=\frac{2}{p-1}
                     \bigl(p\mathcal Z_p-\mathcal S_p\bigr).
\tag{18}
$$

$p$ 在 $K$ 惰性，原好约化因子为 $1+p^{1-2s}$，所以
$$
\psi((p))=-p,\qquad N((p))=p^2.
$$
去掉被 $(p)$ 整除的理想，准确有
$$
\sum_{(\mathfrak a,\mathfrak f_0p)=1}
   \frac{\psi(\mathfrak a)}{N\mathfrak a}e^{-N\mathfrak a/X}
 =S_0(X)+\frac1p S_0(X/p^2).
\tag{19}
$$
令
$$
\mathcal T_p=S_0(Q_0/p^2).
\tag{20}
$$
由 (15)、(19)，
$$
\mathcal S_p=-\mathcal T_p.
$$
因此原平均准确压成
$$
\boxed{\quad
\mathcal M_p=
 \frac{2p}{p-1}\mathcal Z_p+
 \frac{2}{p-1}\mathcal T_p.
\quad}
\tag{21}
$$
第二项不是任意可删的误差；它是原未扭形式在对偶小尺度上的显示和。

由 $a_1=1$ 及固定形式的系数界，
$$
\mathcal T_p=
 \exp(-p^2/Q_0)
 \left(1+O\bigl(\exp(-p^2/Q_0)\bigr)\right).
\tag{22}
$$
它对充分大的 $p$ 为正，且呈指数衰减。(21) 始终保留其准确值。

## 5. 有理主理想的严格正主项

把 (16) 的真实 $\ell_p=0$ 理想集分为有理主理想 $(a)$（$a\in\mathbf Z_{>0}$）与其余所有理想：
$$
\mathcal Z_p=\mathcal R_p+\mathcal N_p.
\tag{23}
$$
这里 $\mathcal N_p$ 是定义为补集的**全部非实 anti-Fermat 理想和**；不要求这些理想的生成元处在某个任意基本小盒子中。

原椭圆曲线 CM 角色在有理理想上满足
$$
\psi((a))=\chi_{-3}(a)a,\qquad (a,102)=1.
\tag{24}
$$
可逐素数核对 (24)：分裂素数的两个原 Frobenius 乘积为 $\ell$，惰性素数的原理想值为 $-\ell$，再用乘法性；$2,3,17$ 的导子条件仍逐项保留。因此
$$
\boxed{\quad
\mathcal R_p=
 \sum_{\substack{a\ge1\\(a,102p)=1}}
       \frac{\chi_{-3}(a)}a
       \exp\!\left(-\frac{a^2}{Q_0p^2}\right).
\quad}
\tag{25}
$$
每个有理主理想只用正生成元计一次，没有六个单位的重数。

令
$$
R_{102}(X)=
 \sum_{\substack{a\ge1\\(a,102)=1}}
       \frac{\chi_{-3}(a)}a e^{-a^2/X}.
$$
因为 $\chi_{-3}(p)=-1$，去掉 $p\mid a$ 得准确式
$$
\mathcal R_p=
 R_{102}(Q_0p^2)+\frac1p R_{102}(Q_0).
\tag{26}
$$
函数 $a\mapsto\chi_{-3}(a)\mathbf1_{(a,102)=1}$ 周期为 $102$ 且一周期和为零，所以其部分和有固定界。对
$(e^{-x^2/X}-1)/x$ 作分部求和，其总变差为 $O(X^{-1/2})$，得到
$$
R_{102}(X)=
 L(1,\chi_{-3})
 (1-\chi_{-3}(2)/2)(1-\chi_{-3}(17)/17)
 +O(X^{-1/2}).
\tag{27}
$$
所有常数只依固定原曲线，不依 $p$。这一步可直接由有限周期的部分和证明，不要求素数分布或数值检验。

最后
$$
L(1,\chi_{-3})=\int_0^1\frac{dt}{1+t+t^2}
              =\frac{\pi}{3\sqrt3},
\quad
\chi_{-3}(2)=\chi_{-3}(17)=-1.
$$
所以
$$
\boxed{\quad
\mathcal R_p=
 \frac{9\pi}{17\sqrt3}+O(p^{-1}).
\quad}
\tag{28}
$$
其极限严格为正。该常数属于**单个有理理想子和** $\mathcal R_p$。
在未除以 $\Omega_{\mathbf R}$ 的平均 $\mathcal M_p$ 中，它乘
$2p/(p-1)$，相应贡献趋于
$$
\frac{18\pi}{17\sqrt3}.
\tag{29}
$$
(28) 与 (29) 是不同正规化，不能互换。

## 6. 同一个原 Hall 投影的精确能量式

R716 已支付
$$
L(\psi\nu_{p,r},1)
 =\frac{48940416\,\Omega_{\mathbf R}}p
                         |\mathscr S_p(r)|^2,
$$
其中 $\mathscr S_p(r)$ 是同一个固定 $S_{34}$ 幅度及完整 $p^2$ 相位的 Hall 和。代入 (21)–(23) 得
$$
\boxed{\quad
\mathcal R_p+\mathcal N_p+\frac{\mathcal T_p}{p}
 =\frac{48940416\,\Omega_{\mathbf R}}{2p^2}
       \sum_{r\in\mathbf F_p^\times}|\mathscr S_p(r)|^2
 \ge0.
\quad}
\tag{30}
$$
左侧的 $\mathcal N_p$ 为实数：共轭理想同时将 $\psi$ 共轭并将
$\ell_p$ 反号，故 (9) 的集合保持。没有逐项正性的断言。

下列条件准确等价：
$$
\boxed{
\begin{aligned}
&\mathscr S_p(r)=0\quad\text{对全部 }r\ne0;\\
&L(\psi\nu_{p,r},1)=0\quad\text{对全部 }r\ne0;\\
&\mathcal N_p=-\mathcal R_p-\mathcal T_p/p.
\end{aligned}}
\tag{31}
$$
第一、第二条件也各自可由一个非平凡原角色的零推出：
这些角色及原 Hall 零都沿同一个阶 $p$ Galois 轨道运输。
(30) 另直接给全部同时零与第三条件的等价，不依赖任选复相位。

于是本题第一层全零迫使一个很具体的非齐次补偿：
$$
\boxed{\quad
\mathcal N_p=-\frac{9\pi}{17\sqrt3}+O(p^{-1}),
\quad}
\tag{32}
$$
且其精确式为 (31)，包括原对偶尺度项 $\mathcal T_p/p$。
反过来，若能在同一原理想集合上证明
$$
\mathcal N_p>-\mathcal R_p-\mathcal T_p/p,
\tag{33}
$$
则该原第一 wild 族非零。这是一个真实同源判据，不是任意 forcing 的可解性。

## 7. 与实际 tame 平均及原中央的范围

保持既有第一 wild/Rubin 注中同一 rational quaternionic test vector，
$$
A_t=\sum_{\tau\in\Delta}f(x_2(\tau\gamma^t)),
\qquad 0\le t<p.
$$
原 primitive period 为零当且仅当 $A_t$ 全相等；该等价使用
$\Phi_p$ 的不可约性以及 primitive 角色杀掉 stabilization 的旧层项。
R716 又把它接到 (31) 的同一原 Hecke 族。因此 (31) 给这条弱 tame-average 判据的准确解析补偿，不要求 BHKO 的全 $D_1$ 联合满射。

以下尚未获得，不能从本篇推出：

1. 非实理想和 $\mathcal N_p=o(1)$，或足以支付 (33) 的单边界；
2. 由 $a_p=0$ 单独推出 $A_t$ 不全相等；
3. 由原 $j_{34}=0$ 推出 (31)，或由本族非零直接推出 $j_{34}\ne0$；
4. 用固定 $p$ 的深层非消失或 $\mu=0$ 代替原第一导子 $p^2$ 的非消失；
5. 将 (10) 的真实二位条件换成固定模数的 $p$ 射线条件。

本篇新支付的是原第一 wild 族的完整解析平均，以及同一个原全迹零所强迫的明确非实补偿。后续估计必须作用于 (23) 的实际 $\mathcal N_p$，保留 $\psi_{17}$、全部坏位条件、真实 $q_p$ 条件和原指数权。

## 依赖

- [R716](R716-original-wild-global-theta-period-and-exact-central-l-value.md)：原全部局部向量、Hecke 角色、根号、完成导子与 $48940416/p$ 的绝对平方常数。
- R290/R298：原未扭权二形式和同一固定 $S_{34}$ 的零权平方身份，因 $S_{34}(0)=0$ 得 $L(\psi_{17},1)=0$。
- [第一 wild/Rubin 注](../notes/2026-11-15-original-first-wild-rubin-factor-and-central-order.md)：同一个原 Rubin 系数与实际 rational test vector 的第一层 Fourier 判据。
- [R703](R703-original-hall-phase-and-finite-fourier-return.md)、[R705](R705-original-wild-character-and-absolute-weil-projection.md)：原 $p^2$ Hall 相位与 wild 字符的完整定义。
- [R707](R707-original-theta-average-and-three-quarter-trace-height.md)：原平方平均上界；本篇没有将该上界当成 (30) 的严格正下界。

本篇为一般证明，没有新增数值扫描、计算证书或可重算数据文件。


## 附录 A. 原 anti-Fermat 指示的完整加性 Fourier 自对偶

本附录只研究第2节的真实模 $p^2$ 角色，不改变理想生成元的二位提升。设
$$
R=\mathcal O_K/p^2,\qquad
G=\{v\in R^\times:q_p(v)=\overline{q_p(v)}\},
\qquad
h_p=\mathbf1_G-\frac1p\mathbf1_{R^\times}.
\tag{34}
$$
将 $h_p$ 在非单位处按零延拓。令 $[u]$ 为 $u\in\mathbf F_{p^2}^\times$ 的唯一模 $p^2$ Teichmüller 提升。由 (11)，
$$
G=[\mathbf F_{p^2}^\times](1+p\mathbf F_p),
\qquad |G|=p(p^2-1).
\tag{35}
$$
这里 (35) 是对**实际** $G$ 的分解，不是允许把 (7) 中的 $\alpha$ 换成 $[\bar\alpha]$。

原有限角色在单位上写为
$$
\vartheta_r(v)=e_p(r\ell_p(v))=\chi_{p,r}(v)^{-2}.
$$
有限正交性逐点给
$$
h_p(v)=\frac1p\sum_{r\in\mathbf F_p^\times}\vartheta_r(v),
\tag{36}
$$
其中每个 $\vartheta_r$ 在非单位处也按零延拓。

取非归一的 trace Fourier 变换
$$
(\mathcal F_+f)(\xi)=
 \sum_{v\in R}f(v)e_{p^2}(\operatorname{Tr}_{R/\mathbf Z/p^2}(\xi v)).
\tag{37}
$$
原全局规范在 $p$ 处是
$\psi_{{\rm add},p}(x)=e^{-2\pi i\{x\}_p}$，故实际局部变换为
$\mathcal F_-f(\xi)=\mathcal F_+f(-\xi)$。两种符号都会在下文明确保留。

### A.1 原每个 wild 角色的绝对 Gauss 和

由 (7)、(11)，对 $z\in\mathbf F_{p^2}$，
$$
\vartheta_r(1+pz)=
 e_p\!\left(\operatorname{Tr}(k_rz)\right),
\qquad k_r=-\frac{34r}{\delta}\ne0.
\tag{38}
$$
展开 $v=[u](1+pz)$。在 $\xi=1$ 的 Gauss 和中，$z$ 的整条二维和仅在
$$
u=-k_r=34r/\delta
$$
时非零，此时等于 $p^2$。$-k_r$ 为 trace-zero 元，且其 Teichmüller 提升满足
$$
\overline{[-k_r]}=[(-k_r)^p]=[-(-k_r)]=-[-k_r].
$$
所以 $\operatorname{Tr}[-k_r]=0\bmod p^2$。又
$\vartheta_r([u])=1$，从而准确得到
$$
\boxed{\quad
\sum_{v\in R^\times}\vartheta_r(v)
             e_{p^2}(\operatorname{Tr}v)=p^2.
\quad}
\tag{39}
$$
没有遗留一个可选的 $p$ 次根相位。

若 $\xi\in R^\times$，换元 $w=\xi v$ 给
$$
(\mathcal F_+\vartheta_r)(\xi)=p^2\vartheta_r(\xi)^{-1}.
\tag{40}
$$
若 $\xi\in pR$，则 $z$ 求和的参数仍为非零的 $k_r$，故该和严格为零；这包括 $\xi=0$。因此 (40) 以零延拓后对全部 $R$ 成立。
$\vartheta_r(-1)=1$，所以原负号加性角色 $\mathcal F_-$ 也给同一个 (40)，不另改绝对符号。

对 (36) 求和，$r\mapsto-r$ 置换全部非零 $r$，得
$$
\boxed{\quad
\mathcal F_+h_p=\mathcal F_-h_p=p^2h_p
\quad\text{在整个 }R\text{ 上。}
\quad}
\tag{41}
$$
这里 $|R|=p^4$；用单位 Fourier 归一 $p^{-2}\mathcal F_\pm$ 后，本征值恰为 $+1$。

### A.2 不省略非单位的直接核表

完整展开还给
$$
\sum_{v\in G}e_{p^2}(\operatorname{Tr}(\xi v))
=
\begin{cases}
p(p^2-1),&\xi=0,\\
-p,&0\ne\xi\in pR,\\
p(p-1),&\xi\in G,\\
-p,&\xi\in R^\times\setminus G.
\end{cases}
\tag{42}
$$

证明单位情形时，写 $\xi=[\xi_0](1+pz)$。
(35) 中的实主单位求和先要求
$\operatorname{Tr}(\xi_0u)=0$，故
$u=a\delta/\xi_0$、$a\in\mathbf F_p^\times$。
令 $\delta_0=[\delta\bmod p]$，则 $\bar\delta_0=-\delta_0$，余相位为
$$
e_p\bigl(a\operatorname{Tr}(\delta_0z)\bigr).
$$
它对 $a\ne0$ 求和为 $p-1$ 或 $-1$；前者等价于 $z\in\mathbf F_p$，也就是 $\xi\in G$。若 $0\ne\xi\in pR$，主单位的和贡献 $p$，余下非平凡的全 $\mathbf F_{p^2}^\times$ 加性和为 $-1$。$\xi=0$ 则直接计数。

相应单位集的 Fourier 核为
$$
\sum_{v\in R^\times}e_{p^2}(\operatorname{Tr}(\xi v))
=
\begin{cases}
p^4-p^2,&\xi=0,\\
-p^2,&0\ne\xi\in pR,\\
0,&\xi\in R^\times.
\end{cases}
\tag{43}
$$
将 (43) 的 $1/p$ 倍从 (42) 中扣除，正好再次得到 (41)，包括原点和所有非零非单位。

### A.3 同源用途与尚未支付的下界

式 (41) 精确识别 (18) 的原 finite kernel，并付清对应原加性角色的绝对 Gauss 常数。它没有将 (30) 的非负能量变成严格正值：原固定 $\psi_{17}$ 的有限坏位、原 theta 向量和指数权仍必须保留。Fourier 自对偶的带符号函数本身不排除它与这个固定来源的配对为零。

特别，不能仅从 (41) 把第5节的非实和估成 $o(1)$，也不能删除 (31) 的非齐次补偿。乘任意 $c\in R^\times$ 改变加性配对时，准确式是
$$
\mathcal F_{\pm,c}h_p(\xi)=p^2h_p(c\xi);
$$
只有在已知 $c\in G$ 时才可再认成同一个 $h_p(\xi)$。这保留实际原极化与任意新 CM 倍数之间的差别。


## 附录 B. 原非实和的 primitive 理想射线分解

以下只重排 R724 的同一个绝对收敛和，不改原字符、坏位或高斯尺度。

称 $\alpha=a+b_0\omega\in\mathcal O_K$ 为 primitive，若
$\gcd(a,b_0)=1$；这个条件在乘 $\mu_6$ 后不变。每个非零整理想唯一写成
$$
\mathfrak a=(d\alpha),\qquad d\in\mathbf Z_{>0},
\quad \alpha\ {\rm primitive}\bmod\mu_6.
\tag{B1}
$$
仍要求原 $\mathfrak a$ 与 $2\delta17$ 互素。因为 $2,17$ 在 $K$ 中惰性，primitive $\alpha$ 自动不被它们整除；三处则保留 $(\alpha,\delta)=1$。同理，对本篇任一惰性 $p$，primitive $\alpha$ 自动为 $p$-单位。

记
$$
R_{102p}(X)=
 \sum_{\substack{d\ge1\\(d,102p)=1}}
 \frac{\chi_{-3}(d)}d e^{-d^2/X}.
\tag{B2}
$$
原 $\psi$ 的乘法性和其有理整数上的准确限制给
$$
\frac{\psi((d\alpha))}{N(d\alpha)}
 =\frac{\chi_{-3}(d)}d
     \frac{\psi((\alpha))}{N(\alpha)}.
$$
而原 anti-Fermat 角色在 $\mathbf Q^\times$ 上平凡，故
$\ell_p(d\alpha)=\ell_p(\alpha)$。因此
$$
\boxed{
Z_p=
 \sum_{\substack{\alpha\ {\rm primitive}\bmod\mu_6\\
                 (\alpha,\delta)=1,\ \ell_p(\alpha)=0}}
 \frac{\psi((\alpha))}{N(\alpha)}
 R_{102p}\!\left(\frac{Q_0p^2}{N(\alpha)}\right).
}
\tag{B3}
$$
单位类 $\alpha=1$ 恰为正文的 $R_p$；去掉这一项就恰为 $N_p$。
特别原十七处有限角色完整位于 $\psi((\alpha))$ 中，并未变成无权格点计数。

### B.1 径向因子严格为正

先定义
$$
R_3(X)=
\sum_{j\ge0}
\left\{\frac{e^{-(3j+1)^2/X}}{3j+1}
      -\frac{e^{-(3j+2)^2/X}}{3j+2}\right\}>0.
\tag{B4}
$$
严格正来自 $u\mapsto e^{-u^2/X}/u$ 在 $u>0$ 上严格递减。
对惰性素数 $\ell$，删除 $\ell$ 的倍数，准确等于施加
$1+\ell^{-1}\mathcal T_{\ell^2}$，其中
$\mathcal T_cF(X)=F(X/c)$。所以
$$
R_{102p}
=(1+2^{-1}\mathcal T_4)
 (1+17^{-1}\mathcal T_{289})
 (1+p^{-1}\mathcal T_{p^2})R_3>0.
\tag{B5}
$$
这只给径向因子的正性。非实方向的
$\psi((\alpha))/N(\alpha)$ 可以有不同实部符号，不能据此给 $N_p$ 定号。

对任何固定 primitive $\alpha$，保持其实际
$\mathbf1_{\ell_p(\alpha)=0}$，由正文的周期部分和估计得
$$
R_{102p}\!\left(\frac{Q_0p^2}{N(\alpha)}\right)
=\frac{9\pi}{17\sqrt3}+O_\alpha(p^{-1}).
\tag{B6}
$$
故一个固定有限集合 $\mathcal F$ 的原贡献为
$$
\frac{9\pi}{17\sqrt3}
 \sum_{\substack{\alpha\in\mathcal F\\\ell_p(\alpha)=0}}
   \frac{\psi((\alpha))}{N(\alpha)}
 +O_{\mathcal F}(p^{-1}).
\tag{B7}
$$
共轭稳定的 $\mathcal F$ 给实数；共轭两项之和是
$\operatorname{Tr}_{K/\mathbf Q}\psi((\alpha))/N(\alpha)$。
这些有限方向可能贡献非零常数，不能把非实和中的所有固定短向量都计入一个未经证明的 $o(1)$。

### B.2 完整的 projective Teichmüller 条件

令 $\mathcal R=\mathcal O_K/p^2$。原
$G=\ker\ell_p\subset\mathcal R^\times$ 的每个 projective 类恰有一个 tame Teichmüller 提升；共有 $p+1$ 个。对每个这样的方向取其自由秩一
$\mathbf Z/p^2$ 子模 $L_a\subset\mathcal R$。这些子模的模 $p$ 方向互异，且
$$
G=\coprod_{a\in\mathbf P^1(\mathbf F_p)}(L_a\setminus pL_a).
\tag{B8}
$$
所有实际第二位就是 Brandt 注 (10)–(11) 中的 $\kappa_p(a)$。

不同 $L_a$ 只在零相交，而 $pL_a\setminus\{0\}$ 将
$p\mathcal R\setminus\{0\}$ 分割。因此全环上准确有
$$
\sum_a\mathbf1_{L_a}
=\mathbf1_G+\mathbf1_{p\mathcal R}
     +p\mathbf1_{\{0\}},
$$
进而
$$
\boxed{
h=\sum_a\mathbf1_{L_a}
 -(1-p^{-1})\mathbf1_{p\mathcal R}
 -p\mathbf1_{\{0\}}-p^{-1}\mathbf1_{\mathcal R}.
}
\tag{B9}
$$
这是附录 A 的同一个完整 $h$，非单位项一项未删。

在原 trace 加性配对下，
$\widehat{\mathbf1_{L_a}}=p^2\mathbf1_{L_a^\perp}$。
正交补仍属于这些 tame 方向：若 $L_a$ 由 $v$ 生成，可取
$\delta/v$ 生成其 trace 正交补；$\delta$ 的 anti-Fermat 值为零。
所以 (B9) 也直接恢复 $\widehat h=p^2h$。
它没有改变原 Fourier 自对偶的范围，也未添一个正性条件。

### B.3 短和节省必须达到的实际尺度

写原有限坏位字符为
$\psi((\alpha))=\varepsilon_{17}(\alpha)\alpha$；
$\varepsilon_{17}$ 保其完整 $2,3,17$ 规范。取 $\mu_6$-不变的光滑紧支撑函数
$W$，支撑在 $c\le |z|\le C$，其中 $0<c<C$ 固定。考虑原非实和在
$|\alpha|\asymp p$ 上对应的平滑块
$$
N_p(W)=\frac16
 \sum_{\substack{(\alpha,2\delta17p)=1\\
                 \alpha\notin\mu_6\mathbf Z}}
 \frac{\varepsilon_{17}(\alpha)}{\bar\alpha}
 W(\alpha/p)\mathbf1_{\ell_p(\alpha)=0}.
\tag{B10}
$$
令
$$
\mathcal C_{p,r}(W)=
 \sum_{\substack{(\alpha,2\delta17p)=1\\
                 \alpha\notin\mu_6\mathbf Z}}
 \frac{p\,\varepsilon_{17}(\alpha)}{\bar\alpha}
 W(\alpha/p)e_p(r\ell_p(\alpha)).
$$
则精确的全族关系是
$$
\boxed{
N_p(W)=\frac1{6p^2}
              \sum_{r\in\mathbf F_p}\mathcal C_{p,r}(W).
}
\tag{B11}
$$
所有整数代表、坏位权与删去的有理射线都保持原样。

因而在这一固定 annulus 上要由短和证明 $N_p(W)=o(1)$，
所需的实际结论是右边总分子为 $o(p^2)$。
仅有每个非平凡字符的界
$|\mathcal C_{p,r}|\ll p^{2-\epsilon}$
通常只给 $O(p^{1-\epsilon})$；
即使单个字符达到 $O(p)$，逐项绝对值求和也只给 $O(1)$。
原同步字符平均、低尺度 (B7) 以及高斯尾都仍须分别支付。

尤须注意，原字符在整条 $\mathbf Q^\times$ 上平凡。
普通一维 Fermat 商 $e_p(rq_p(n))$ 并不具有这个性质，不能将其短和或跨 $p$ 平均定理直接代入 (B11)。将原加性 Fourier 完成到全环只得到附录 A / (B9) 的同一个自对偶式，不自动提供新的节省。

本附录没有证明 (B11) 的 $o(p^2)$，也没有删除任何非实补偿。


## 附录 C. 原二维 anti-Fermat 核的全部加法交数

本附录保持附录 A 的 $R=\mathcal O_K/p^2$、$G$、$h$ 和非归一 trace Fourier 变换；$|R|=p^4$。写加法卷积为
$$
(f*g)(a)=\sum_{v\in R}f(v)g(a-v).
$$
原 $G=-G$，所以卷积也正是平移交数。由 (42)，若 $A=\mathbf1_G$、$k=|G|=p^3-p$，则
$$
\widehat A(0)=k,\qquad
\widehat A(\xi)=
\begin{cases}
p^2-p,&\xi\in G,\\
-p,&0\ne\xi\notin G.
\end{cases}
\tag{C1}
$$
第二行包括全部非零 $\xi\in pR$；没有删掉非单位方向。

两个非平凡 Fourier 值都是
$t^2-p(p-2)t-p^2(p-1)=0$ 的根。原点的值另准确补齐，从而 Fourier 反演给
$$
\boxed{
A*A=p^2(p-1)\mathbf1_{\{0\}}
       +p(p-2)A+p(p-1)\mathbf1_R.
}
\tag{C2}
$$
特别实际有限交数为
$$
\boxed{
|G\cap(a+G)|=
\begin{cases}
p^3-p,&a=0,\\
2p^2-3p,&a\in G,\\
p^2-p,&a\ne0,\ a\notin G.
\end{cases}
}
\tag{C3}
$$
最后一项亦适用于每个非零 $p$ 倍数。
这是原全部二位 Teichmüller 截面所给的等式，不是普通 $\mathbf F_{p^2}$ 上范数圆锥的 Weil 近似。

对正文的已中心化核，逐点有
$$
h^2=(1-2/p)h+\frac{p-1}{p^2}\mathbf1_{R^\times}.
$$
由于 $\widehat h=p^2h$ 及 $h(-a)=h(a)$，同一反演规范给
$$
h*h=p(p-2)h+\frac{p-1}{p^2}
                     \widehat{\mathbf1_{R^\times}}.
\tag{C4}
$$
保留 (43) 的全部非单位项后，准确为
$$
\boxed{
\sum_vh(v)h(v-a)=
\begin{cases}
(p-1)(p^2-1),&a=0,\\
-(p-1),&0\ne a\in pR,\\
(p-1)(p-2),&a\in G,\\
-(p-2),&a\in R^\times\setminus G.
\end{cases}
}
\tag{C5}
$$
原负号加性角色给同样的表；没有额外根单位。

为明确这些完整相关与原短域之间的关系，定义实际带坏位权的周期化
$$
F_p(v)=
\sum_{\substack{0\ne\alpha\in\mathcal O_K\\
                 \alpha\bmod p^2=v,\;(\alpha,2\delta17)=1}}
 \frac{\psi((\alpha))}{N\alpha}
             e^{-N\alpha/(Q_0p^2)}.
\tag{C6}
$$
它绝对收敛，完整保原理想生成元及 $\psi_{17}$，每个理想计六次。于是原中央能量读取的是**指定平移零**：
$$
\boxed{
\sum_{v\in R}h(v)F_p(v)
       =6\bigl(\mathcal Z_p+\mathcal T_p/p\bigr).
}
\tag{C7}
$$
对任意 $F:R\to\mathbf C$，完整平移二阶平均确实满足
$$
\begin{aligned}
&\sum_a\left|
 \sum_v A(v-a)F(v)-\frac{k}{p^4}\sum_vF(v)
                    \right|^2\\
&\quad=\frac1{p^4}
 \left\{p^2(p-1)^2\sum_{\xi\in G}|\widehat F(\xi)|^2
   +p^2\sum_{\substack{\xi\ne0\\\xi\notin G}}
                                 |\widehat F(\xi)|^2\right\}.
\end{aligned}
\tag{C8}
$$
这保留全部原 Fourier 坐标，但没有将平移 $a=0$ 从平均中分离出来。
(C3)–(C8) 也没有将 $F_p$ 的原 $\lvert\alpha\rvert\asymp p$ 短域换成全环。
因此本附录支付了原二维核的精确加法二阶代数，尚不支付
(C7) 的严格正性、附录 B 的同步 $o(p^2)$ 或任何新的原中央零。
