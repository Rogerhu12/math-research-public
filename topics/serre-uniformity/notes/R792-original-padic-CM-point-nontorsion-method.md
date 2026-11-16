# 原 CM 点的分裂处非挠证书：准确来源、仿射精度与有限判据

日期：2026-11-15。状态：下列有限证书的数学充分性已证明；本文件不预填一次实际成功，也不把已成标量 RR 候选接受为原坐标。

## 1. 所消费的是同一个原点

固定原 $p=41$、$L=\mathbf Q(b,\zeta)$、$s=1+2\zeta$ 与
$$
C_b:\ y^2=x^3+b,\qquad P=f_4(c_1),\qquad f_4(c_0)=O.
\tag{N1}
$$
R840 的真实四响应来源、原518位商值以及 R841 的准确 DAG 已把这里的 $P$ 绑定到原 free-column1186 的函数 $y$。使用的是那个原关系的模 $\ell^{518}$ 点值与首导，不是把其 RR 建议当成准确的 $L$ 坐标。

记原局部参数为 $z=a-1$，原 R791 已成切向为 $h_0=f_4^*(dx/(2y))/dz|_{c_1}$。原 R791(791R.16) 给
$$
x(P)=\frac{3h_0(y(P)^2-b)}{y'_z(P)}.
\tag{N2}
$$
本消费者只在一个实际验证了分母为单位的原分支上使用(N2)。R792 的原几何证明还给其特征零分母非零；执行中仍逐项记录实际约化条件。已有 CM 值、首导、$h_0$、原模型常数及原同源常数均不重算。

辅助素数固定为已经使用的
$$
\ell=1000000753.
\tag{N3}
$$
旧数据的整数变量为 $B=\lambda b$，不是另一个模型的 $b$。原14个分支记录 $(\bar B,\bar s)$，满足原首一七次 $f_B(\bar B)=0$ 与 $\bar s^2+3=0$。程序先核 $f'_B(\bar B)$、$2\bar s$、$\lambda$ 及所需有理分母是单位，再以这些同一根唯一 Hensel 提升到 $\ell^{518}$。因此得到真正的嵌入 $L\hookrightarrow\mathbf Q_\ell$；这里不能用一般带分歧完成域的形式群阈值代替 $\mathbf Q_\ell$ 的阈值。

原模商数组的次序是 $(B^0,\ldots,B^6,sB^0,\ldots,sB^6)$。按这个次序在提升根处求值，$h_0$ 则直接按原 $(1,\zeta)$ 两多项式在 $b=B/\lambda,\zeta=(s-1)/2$ 处求值。两种基的转换各只做一次。它们都给同一个原 $P$ 的带绝对精度近似；不需要先求所有2420个关系坐标。

## 2. 一个足够的局部非挠证书

**命题 N.1。** 设原分支上的 $b\in\mathbf Z_\ell^\times$、$\ell>3$，并设 $P\in C_b(\mathbf Q_\ell)$ 来自(N1)的准确来源。若有正整数 $m$ 和准确有限计算证明
$$
[m]\bar P=O\quad\text{于 }C_{\bar b}(\mathbf F_\ell),
\qquad
0<v_\ell\bigl(t([m]P)\bigr)<\infty,
\quad t=-x/y,
\tag{N4}
$$
则原 $P\in C_b(L)$ 非挠。

**证明。** 因判别式 $-432b^2$ 是单位，模型具有好约化。第一个条件使 $[m]P$ 属约化核；第二个条件同时证明这个点不为 $O$。

为完整说明这里包括 $\ell\mid m$ 的情形，取约化核的形式群参数 $t\in\ell\mathbf Z_\ell$。单位微分在这个参数中的展开为
$$
\omega=\left(1+\sum_{n\ge1}a_nt^n\right)dt,\quad a_n\in\mathbf Z_\ell,
\quad
\log_F(t)=t+\sum_{n\ge2}\frac{a_{n-1}}n t^n.
\tag{N5}
$$
若 $v_\ell(t)=r\ge1$，则每个高次项的赋值至少 $nr-v_\ell(n)>r$，因为 $\ell>2$。故 $v_\ell(\log_F(t))=r$。形式群的单位微分恒等式使这个收敛级数为从约化核到 $(\mathbf Q_\ell,+)$ 的群同态。因此非零 $t$ 的像非零，而加法群无挠；约化核无挠。若 $P$ 为挠点，则非零 $[m]P$ 仍为挠点，矛盾。这个论证没有要求 $m$ 素于 $\ell$。$\square$

可核文献是 Milne, *Elliptic Curves*, 第二版，II §4–5，尤其 Proposition 5.4 及其约化推论；作者公开文本为 [EC2.pdf](https://jmilne.org/math/Books/EC2.pdf)。上面的(N5)另写出了本处仅需的奇素数形式群论证，并未调用一个未注明分歧条件的 torsion-injectivity 口号。

## 3. 只求约化点的一个消去整数

不必计算整个群的阶。令
$$
H=\lfloor\sqrt{4\ell}\rfloor,
\quad L_0=\ell+1-H,\quad U_0=\ell+1+H,
\quad k=\lceil\sqrt{U_0-L_0+1}\rceil.
\tag{N6}
$$
Hasse 定理保证 $[L_0,U_0]$ 含一个消去 $\bar P$ 的整数：实际群阶就是一个。可用确定性 baby-step/giant-step：保存 $j\bar P$、$0\le j<k$，依次比较
$$
-[L_0]\bar P-[ik]\bar P=j\bar P.
\tag{N7}
$$
若相等且 $m=L_0+ik+j\le U_0$，直接以有限域二进制标量乘再核 $[m]\bar P=O$。遍历 $0\le i<k$ 足够。若 baby 表中有重复点，保存最早的 $j$；对实际群阶给出的命中，这只会减小而不会使所得 $m$ 超过上界，也不会低于 $L_0$。故过程严格有限，不需要随机点或假设约化点阶很大。

关于 Hasse 界及区间内点阶搜索，可核 Sutherland 的 [MIT 18.783 Lecture 8, §§8.1–8.3](https://math.mit.edu/classes/18.783/2015/LectureNotes8.pdf)。本任务只保实际得到的 $m$、约化曲线和点、完整有限域标量乘核验及必要的搜索回执，不声称这个 $m$ 就是群阶或点的准确阶。

## 4. 原始 Jacobian 坐标不能代替精度证书

在相同约化点相加的情形，某些射影加法公式可能落入 base locus，算出的三坐标同时被 $\ell$ 整除。未经 primitive 化而读其 $Z$ 赋值会给假证。本执行契约因此使用真正的 $\mathbf Q_\ell$ 仿射球运算；没有从非 primitive 的三坐标读 $t$ 的分支。

每个数保存成
$$
x=\ell^v u+O(\ell^A),\quad v<A,\quad
u\in(\mathbf Z/\ell^{A-v}\mathbf Z)^\times,
\tag{N8}
$$
或者零球 $O(\ell^A)$。后者只给 $v_\ell(x)\ge A$，不能判定准确零。对于非零球，记录的 $v$ 就是真实赋值。

加法的绝对精度至少为 $\min(A_x,A_y)$。乘法的绝对精度至少为
$$
\min(A_x+v_y,A_y+v_x),
\tag{N9}
$$
其中零球使用其赋值下界。只有(N8)的非零球才可求逆；其逆的绝对精度为 $A_x-2v_x$，单位部分在模 $\ell^{A_x-v_x}$ 下求逆。每次操作后都按真实整除性规范化，不能仅保一个统一的“518位”标签。

二进制标量乘保存每个中间点的准确整数 multiple 标签。标签确相同才使用倍点公式
$$
\mu=\frac{3x^2}{2y},\quad
x_2=\mu^2-2x,\quad y_2=\mu(x-x_2)-y.
\tag{N10}
$$
加上不同标签的点时，只有 $x_Q-x_R$ 的球显示有限赋值，才使用通常的仿射加法。若这个差只是零球，不允许由“模精度相等”决定倍点、互为相反或准确 $O$，而是记录不确定并结束本次充分检验。初始的群零元以及同一整数标签，是唯二不需要数值零判的分支。

每次操作所除的实际非零球、其赋值和余下绝对精度均进入原子 stage。曲线多项式的球应包含零，可作为实现自核；它不取代来源证明中的准确原曲线恒等式。

最终先核有限域(N4)，再由一个非零的 $t=-x/y$ 球读出
$$
1\le v_\ell(t)<A_t.
\tag{N11}
$$
可再核 $v_\ell(x)=-2v_\ell(t)$、$v_\ell(y)=-3v_\ell(t)$。这才是命题 N.1 的证书。遇未确定分母、精度不足或未得到(N11)，只能输出“本次未认证”，不能声称点为挠点。没有任何一步把 RR 建议输入为准确点。

## 5. 此同一点对全部原 Hom 的条件性后果

R616(616.4–5) 的 $c_0,c_1$ 是原 $\mathbf Q$ 点，且
$$
\beta=q_1[c_1-c_0]\in A(\mathbf Q)\otimes\mathbf Q.
\tag{N12}
$$
R728(728.24)、(728.32) 给原 primitive 因子的 $\mathbf Q$ 同源模型及其全实域型有理自同态代数。后者为域，故由 Poincaré 完全可约性，$A$ 在 $\mathbf Q$ 上简单。这里不需要声称 $A_K$ 几何简单，也不把全 Weil restriction 当成这个 primitive 因子。

**命题 N.2。** 若本消费者实际证明 $f_4(c_1)$ 非挠，则(N12)的原 $\beta$ 非挠，且任意非零 $u\in\operatorname{Hom}_L^0(A,C_b)$ 都有 $u(\beta)$ 非挠。

**证明。** 原 $f_4$ 属原 primitive Hom 模块，故是一个非零有理同态与 $q_1$ 的复合；若 $\beta$ 为挠，其像也为挠。对第二句，先统一清 $q_1,u$ 的同源分母，使 $n\beta\in A(\mathbf Q)$ 且 $nu$ 是真实同态。非挠有理点 $n\beta$ 所生成群的 Zariski 闭包是 $\mathbf Q$-定义的代数子群；其单位分量正维，由 $\mathbf Q$-简单性只能是 $A$。因此该循环群在 $A$ 中稠密。如果 $u(\beta)$ 为挠，则某个非零整数倍的 $u$ 消去稠密循环群，从而同态恒零，矛盾。$\square$

这个结论只在实际非挠证书成功后激活。R726 的“全部充分大 $p$”本身不涵盖当前 $p=41$。本文件也没有依据抽象非零 Hom、非零切向或模近似单独预填非挠。

命题 N.2 成立后，同靶两点加法中 $u(\beta)=\pm v(\beta)$ 当且仅当 $u=\pm v$ 于原有理 Hom 模块；非零 $u(\beta)$ 不可能为二挠点。因而已认证 Hom 字可决定那些特殊分支。不过这仍不恢复抽象 $A$ 上未选定的同源核原像，不给原 $\eta$、刚性化函数或高度数值。

## 6. 最小真实来源和输出边界

新 consumer 可直接消费已成功 R841 的一日 carrier：其原 CM165件与 R7919件已经带着四响应、原518位商、原14根、原模型、原 $h_0$ 及全部父子来源。只需附本 R841 的准确 DAG 小证书与来源回执。旧1234大行、完整518位关系 current、14个Schur逆均不再读取。

首 scope 顺序固定：

1. 依旧14分支的原顺序，选第一个实际具有 $b$、$y'_z$、原有理分母单位及合法简单根的分支；没有则诚实未认证。
2. 将该原根提升到518位，求原模 $y,y'_z,h_0,b$ 并按(N2)得到点球；所有求值的旧源 SHA 不变。
3. 新算约化点消去整数 $m$；然后只算这一条 $[m]P$ 的有精度标量乘。
4. 若(N11)成立，输出原 $P$ 非挠真标志；否则输出实际不确定原因。原 expanded-coordinate acceptance、A.1、$\eta$/height 标志始终为 false。

每个 Hensel 根阶段、约化搜索、标量乘步骤及最终证书均保存原子断点；预算续接只读已成阶段。运行时只在本公开仓库 Actions 新算。可重算向量与回执仅在一日 active artifact/carrier 续传；Git 只保存源码、参数、纸面证明及简明 run/SHA 登记。

## 来源

- [R616](../results/R616-original-CM-point-difference-and-explicit-height-basis.md)，原有理 CM 点差及同一 primitive 商。
- [R728](../results/R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md)，原 primitive 模型、真实 $\mathbf Q$ 同源和自同态域。
- [R791](../results/R791-certified-original-Hom-descent-and-eta-inputs.md)，原 h0、(791R.16)及三同源规范；[R792](../results/R792-original-beta-composition-and-Galois-cube-root.md)，原方向与几何非零。
- [准确 unit-chart 消费接口](R787-original-unit-chart-exact-expressions-and-CM-value-consumer.md)及[成功 DAG 接口](R792-original-source-bound-CM-DAG-beta-interface.md)，把有限精度响应绑定到同一准确原点。
- Milne II §4–5 与 Sutherland Lecture 8 的作者公开原文，链接见正文。本文(N5)、(N7)与(N8–11)把当前所需的无挠、有限搜索和精度充分条件逐项写明。
