# R200：二阶实际阻碍的 reference–cyclotomic 抵消与唯一受支撑 Norm 斜率

**状态：已证明的精确 reduction；最后的 Norm 数值仍未知。** 本稿在 2026-11-12 22:16 UTC 环境再次恢复后，从父会话及 CM 分支已经逐式核准的证明重建。前两次运行时丢失了原文件和 store。本稿采用新字节、新 SHA，不声称恢复历史 19373 字节稿或第一次恢复 16512 字节稿的逐字内容。

本结果处理 R176 的同一个实际固定局部型问题。它不从首阶 Selmer 相容性推出实际椭圆曲线，也不从普通全局 lift 推出固定晶体型 lift。主结论将第二个阻碍化为一个带完整 Kummer gauge、完整支撑和固定 Frobenius 规范的单一斜率。对 R171 的 $p=43$ 实例，该式为

$$
\boxed{\Omega_2=\epsilon(13+11v).} \tag{200.1}
$$

因此本层固定型 lift 存在当且仅当 $v=34$。本文没有求出 $v$。R201 后续把同一个未知数改写为规范 Norm 剩余量 $L$，得到 $\Omega_2=\epsilon(10-L)$；这个 $L$ 不能与 R189 的首阶数值 $10$ 混同。

## 1. 固定的表示、支撑与首差

沿用 R168、R171、R176 的标架：

$$
A:y^2=x^3-x,\quad K=\mathbf Q(i),\quad p>37,\quad p\equiv3\pmod4,
$$
$$
\operatorname{ad}^0 A[p]=\mathbf F_p(\eta)J\oplus W,
\qquad \eta=\chi_{-4},\quad J=[i].
$$

固定唯一新增 Tate 支撑 $q\equiv-1\pmod{4p}$，假设 $v_p(q+1)=1$、$\gamma_q=0$、$\lambda_q\ne0$。所有提升均在 $S=\{2,p,q,\infty\}$ 外不分歧，固定行列式；在 $p,2$ 处固定 $T_p(A)$ 的完整局部型，在 $q$ 处固定一个深度 $1$ 的整 Tate 型和乘法符号 $\epsilon$。这里 $q$ 是全部新增支撑，而非只从更多支撑中抽出的最浅素数。

记首差为

$$
c=rJ+w\in Z^1(G_{\mathbf Q,S},\operatorname{ad}^0 A[p]).
$$

R168 给唯一严格 $p$ 的 $W$ 类，其 $q$ 处有限/奇异坐标满足 $a=\lambda_q b$。规范化 $\kappa_q$ 使 $r=-\kappa_q$；在 R171 的 $43$ 实例，它正是 R196 所构造、在 $p$ 全分裂、在 $q$ 奇异坐标为 $1$ 的反循环角色。

另记 $\kappa_p$ 为 R196 的纯 $p$ 反循环角色，$\ell_{\rm cyc}=(\chi_{\rm cyc}/\omega-1)/p\pmod p$，其中 $\omega$ 为 cyclotomic 的 Teichmüller 提升。R196 的实际 CM 比较给出 $W$ 和 $W(1)$ 在相应 Kummer reference 之上的一阶差：

$$
B_{\rm pr}=-\ell_{\rm cyc}-i\kappa_p,
\qquad B_{\rm du}=-i\kappa_p. \tag{200.2}
$$

此外 $[rJ,W]=2irW$，所以实际首差造成的 $WW$ 作用修正是 $-2i\kappa_q$。三者的角色及 $i$ 的方向必须与 R196 同一标架一致。

## 2. 两个 reference 格与 exact dual

令 $T$ 是有限剩余 $W$ 作用的 Teichmüller 格。迹配对把 $T$ 与其线性对偶识别。定义

$$
P=\chi_{\rm cyc}\omega^{-1}T,\qquad
D=\chi_{\rm cyc}T,\qquad
D'=\omega T=P^\vee(1). \tag{200.3}
$$

$P/p=W$、$D/p=D'/p=W(1)$。$P,D$ 都是 Kummer 型格；$D'$ 才是 $P$ 的**精确 Tate 对偶**。模 $p^2$ 有

$$
D'=D(1-p\ell_{\rm cyc}). \tag{200.4}
$$

由 Kummer 代表可选一个全局 $P/p^2$ cocycle $\widetilde w$ 提升 $w$，以及全局 $D/p^2$ cocycle $\widetilde d$ 提升原始 Robert 类 $d=d_0$。选择它们时始终保留同一 $S$ 支撑：primal 角色的类群 $p$ 部消失由 R189 给出，故其 $S$-supported 剩余类可用 $S$-单位表示；dual 原始 Robert 代表本来是单位。这里不要求已经算出这些 primal 单位。由于 $w_p=0$，在 $p$ 处杀掉其剩余 coboundary 后可写

$$
\widetilde w_p=pz_0\pmod{p^2}. \tag{200.5}
$$

这里 $z_0$ 是一个真实的局部类，不能因 $w_p=0$ 就把 $z_0$ 设为零。这正是普通 Kummer reference lift 与固定晶体目标之间可能存在的差别。下文证明它与 cyclotomic primitive 的贡献精确抵消，而不是预先忽略它。

## 3. $q$ 处必须使用完整 Kummer-zero gauge

记完整 CM Frobenius 为 $\varphi$，令 $r_q=\sqrt{-q}\in1+p\mathbf Z_p$，$F=\varphi/r_q$、$K_q=JF$。则 $F^2=K_q^2=1$，$J^2=-1$。在 $D$ 上，$F$ 和 $K_q$ 的 Frobenius 特征值分别是 $q$、$-q$。因此模 $p^2$ 的不分歧一次上同调来自 $K_q$ 方向：

$$
H^1_{\rm ur}(\mathbf Q_q,D/p^2)
\simeq (\mathbf Z/p^2)K_q/(-q-1)K_q.
$$

由于 $v_p(q+1)=1$，到模 $p$ 不分歧上同调的约化是同构。$\widetilde d$ 来自 $q$ 处单位，故不分歧；而 $d_q=0$。所以 $\widetilde d_q$ 本身已经是 coboundary。选局部 $0$-cochain 杀掉它，得到

$$
\widetilde d_q=0,\qquad d_q=0
\quad\text{作为 cochain 的恒等式}. \tag{200.6}
$$

这个规范的模 $p$ 部分唯一：$H^0(\mathbf Q_q,D/p^2)$ 恰在 $pK_q$ 中，其约化为零。因而完整 lift 的两种杀零选择只相差模 $p$ 为零的 $0$-cochain。

这比“局部类为零”强。若将 Robert 单位按低整数权写成两个普通单位 $U,V$，分别随意选择其剩余域中的 $p$ 次根，通常不会得到 (200.6)。R201 后续的 Teichmüller 高权修正给本例低权根 $(\beta_U,\beta_V\zeta^6)$；那个修正属于同一个规范，不能在数值计算中省略。

## 4. 三个 dual primitive 的受支撑存在性

定义三个等变双线性作用

$$
j_c(\ell,z)=-\ell z,\qquad
j_p(\kappa,z)=-i\kappa z,\qquad
j_q(\kappa,z)=-2i\kappa z.
$$

反循环角色的 $\eta$ 因子与乘 $i$ 的反变性互相抵消，所以这些确实是相应 Galois 模之间的等变作用。它们对迹配对的伴随符号是

$$
\varepsilon_c=+1,\qquad \varepsilon_p=\varepsilon_q=-1. \tag{200.7}
$$

写 $\kappa_c=\ell_{\rm cyc}$，选择 $S$-supported $1$-cochains $e_c,e_p,e_q$，使

$$
\delta e_\nu=j_\nu(\kappa_\nu\cup d)
\qquad(\nu=c,p,q). \tag{200.8}
$$

存在性不是从未限制支撑的 Hasse norm 定理直接移来。先核 $\Sha^1_S(W)=0$：在当前单素数分支，严格 $p$ 且允许 $q$ 分歧的全局 $W$ 类是一维；其非零生成元在 $q$ 的有限坐标为 $\lambda_q$ 倍非零奇异坐标。因为 $\lambda_q\ne0$，它不能在 $S$ 全部局部化为零。R161 的最小严格 Selmer 亦为零。Poitou–Tate 对偶遂给

$$
\Sha^2_S(W(1))=0. \tag{200.9}
$$

这里需要的方向是 $\Sha^1(W)$ 对偶 $\Sha^2(W(1))$，不能误引 R176 处理普通 primal 障碍时使用的相反方向。

各个 (200.8) 的右侧都局部为零：$p$ 处 $H^2(\mathbf Q_p,W(1))=H^0(\mathbf Q_p,W)^\vee=0$；$q$ 处 $d_q=0$；$2$ 处局部上同调消失；其余处是不分歧杯积。结合 (200.9) 得到真正保持 $S$ 支撑的 primitive。

改变任一个 $e_\nu$ 只增加全局 $H^1(G_{\mathbf Q,S},W(1))$ 类。在本例该空间由 $d_0,d_q^*$ 生成；最后的局部配对不受这种改变影响，见 §9。

## 5. 二阶实际矩阵方程与 $\eta$ 通道的阶数

在固定行列式的指数坐标中写

$$
\rho_3(g)=\exp\bigl(p\widetilde c(g)+p^2Y(g)\bigr)\rho_A(g)
\pmod{p^3}.
$$

群律的 $p^2$ 项给

$$
\delta Y=-\left(\beta_A(c)+\frac12[c\cup c]\right). \tag{200.10}
$$

这里只涉及首差 $c$。若把二阶未知分成 $Y_\eta+Y_W$，则 $[pw,p^2Y_\eta]$ 从 $p^3$ 项才开始，属于表示模 $p^4$ 的下一层 $\Omega_3$，不反馈当前模 $p^3$ 的 $\Omega_2$。

取 $h_B(g)=ir(g)w(g)$。直接用非齐次 cocycle 公式计算得

$$
\frac12[c\cup c]_W=2ir\cup w+\delta h_B. \tag{200.11}
$$

Kummer reference 使 $\widetilde w$ 的 reference Bockstein 为零。代入 (200.2)、$r=-\kappa_q$ 后，若 $b$ 满足

$$
\delta b=(-\ell_{\rm cyc}-i\kappa_p-2i\kappa_q)\cup w,
\tag{200.12}
$$

则 $Y_W=-b-h_B$。这里 $b$ 是三项**之和**的 primitive；没有声称每个 primal cup 项单独都有全局 primitive。

R176 给普通全局障碍的局部检测；指定的整 Tate 局部 lift 和 $p,2$ 局部目标使当前普通障碍可解。$\eta$ 分量则独立满足一个线性的 $\delta Y_\eta$ 方程。其局部解可用两个全局 $\eta$ 类作三角校准：$\kappa_p$ 调整 $p$ 处而在 $q$ 为零；$\kappa_q$ 调整 $q$ 奇异方向而在 $p$ 为零。$q$ 处 $\eta$ 的有限 $H^1$ 为零。因而可把已得 $W$ 奇异分量配入真实 Tate 比较线 $L_q$。这说明 $\eta$ 二阶未知不添加一个独立的当前 $W$ 阻碍，而不是仅凭 $\operatorname{tr}(\eta W)=0$ 删除它。

在 $p$ 处可将 $c_p,w_p$ 选成零 cochain，故 $h_{B,p}=0$。实际固定晶体偏差是 $z_0-b_p$。沿 R176 的符号规范，唯一阻碍为

$$
\Omega_2=\langle z_0-b_p,d_p\rangle_p. \tag{200.13}
$$

在 $q$ 处与指定整 Tate 目标重新比较产生的有限/奇异校准不会改变 (200.13)：R176 的对偶阻碍线是 $\mathbf F_p d_0$，而 $d_0(q)=0$。因此这不是仅对某个任意普通 lift 的 $p$ 偏差作配对。

## 6. 带伴随符号的 secondary 互反恒等式

给出完整 cochain 计算以固定符号。采用非齐次左作用微分。对 $\nu=c,p,q$ 设

$$
A_\nu(g,h)=j_\nu(\kappa_\nu(g),g w(h)),
\quad R_\nu(g,h)=j_\nu(g\kappa_\nu(h),w(g)),
$$
$$
h_\nu(g)=j_\nu(\kappa_\nu(g),w(g)),
\quad T_\nu=j_\nu(\kappa_\nu\cup d).
$$

直接展开得到

$$
\delta h_\nu=-A_\nu-R_\nu,
\qquad
\operatorname{tr}(R_\nu\cup d)
=\varepsilon_\nu\operatorname{tr}(w\cup T_\nu). \tag{200.14}
$$

利用 $\delta b=\sum A_\nu$、$\delta e_\nu=T_\nu$，定义

$$
\mathcal C=\operatorname{tr}\left(
b\cup d-\sum_\nu\varepsilon_\nu w\cup e_\nu
+\sum_\nu h_\nu\cup d\right). \tag{200.15}
$$

Leibniz 法则与 (200.14) 给 $\delta\mathcal C=0$。在 $p$ 处 $w_p=h_{\nu,p}=0$，只剩 $\operatorname{tr}(b_p\cup d_p)$；在 $q$ 处完整规范 (200.6) 使 $d_q=0$，只剩 $-\sum\varepsilon_\nu\operatorname{tr}(w_q\cup e_{\nu,q})$。

还必须处理 $2$。由于此处 $H^1$ 消失，可写 $d=\delta t$，并选 $e_\nu=-j_\nu(\kappa_\nu\cup t)$。代回 (200.15)，两组 Leibniz 项精确抵消，得到

$$
\mathcal C_2=-\delta\operatorname{tr}\left((b+\sum h_\nu)\cup t\right).
$$

这证明其局部 invariant 为零；不能只说“局部类为零”而把尚未固定的 cochain 项删掉。其余处由 $S$ 支撑及不分歧性给 invariant 零。全局互反于是给

$$
\langle b_p,d_p\rangle_p
=\langle w_q,e_{c,q}-e_{p,q}-e_{q,q}\rangle_q. \tag{200.16}
$$

两个反循环作用的负伴随号正是右侧两个减号的来源。

## 7. exact-dual lift 消去 reference 与 cyclotomic 项

在相同底层模 $p^2$ 模上，(200.4) 改变 coboundary 算子。因为 $\delta e_c=-\ell_{\rm cyc}\cup d$，

$$
\widetilde d'=\widetilde d-p e_c
$$

是 $D'/p^2$ 的 cocycle。$D'=P^\vee(1)$，故

$$
\operatorname{tr}(\widetilde w\cup\widetilde d')
\in Z^2(G_{\mathbf Q,S},\mu_{p^2})
$$

是一个真正的整对偶杯积。

在 $p$ 处利用 (200.5)，其 invariant 的 $p$ 倍部分是 $p\langle z_0,d_p\rangle_p$。在 $q$ 处利用完整 (200.6)，它是 $-p\langle w_q,e_{c,q}\rangle_q$。$2$ 处可先把整 Kummer 类杀成零；剩余 coboundary 与前节一样由 Leibniz 处理，其他处不分歧。全局互反除以 $p$ 给

$$
\langle z_0,d_p\rangle_p
=\langle w_q,e_{c,q}\rangle_q. \tag{200.17}
$$

把 (200.16)、(200.17) 代入 (200.13)，得到主结构式

$$
\boxed{\Omega_2=\langle w_q,e_{p,q}+e_{q,q}\rangle_q.} \tag{200.18}
$$

因此 reference 项并非凭选 gauge 消失；它与 cyclotomic primitive 通过 exact dual 的全局整杯积抵消。若忽略 $z_0$ 或把 $D$ 错当成 $P$ 的精确对偶，就会留下错误的 cyclotomic 未知量或错误地宣称总阻碍已知。

## 8. R198 的纯 $p$ 数值在本 gauge 下仍为 $28K_q$

R198 在 R171 的同一个 $q$、同一个 CM 标记和正算术 Artin 规范下，计算了 $p^2$ Robert Norm 见证的导数。其正 cup primitive、实际系数 $-i$ 及未分歧二次限制的因子给

$$
e_{p,q}=28K_q \quad(p=43). \tag{200.19}
$$

该数值已由 $44\times43\times42$ 个有限域评价和所有 $44$ 个精确 Norm 比值核验；本文只使用该正式证书，不重新定义它的符号。

需要核对的连接是：将 $d_q$ 从原 Kummer 代表改为完整 (200.6) 时，$e_p$ 的校正包含 $j_p(\kappa_p\cup t)$。纯 $p$ 反循环扩张在 $q$ 上全分裂，故在未分歧二次局部扩张 $k_q/\mathbf Q_q$ 上 $\kappa_p$ 是零 cochain，该校正限制后为零。扩张次数为 $2$，与 $p$ 互素，所以局部上同调的 restriction 是单射；下到 $\mathbf Q_q$ 后该校正仍为零。因此 (200.19) 在本节完整 Kummer-zero gauge 中保持。

R198 在 $k_q$ 上完成正 primitive 和实际 $-i$ 作用之后的有限值为 $13i$；回到有理局部域再除以 restriction 次数 $2$，得到 $28K_q$。式 (200.19) 已包含这个次数 $2$，不能再重复除以 $2$，也不能省掉它。

## 9. 唯一规范斜率和 $43$ 的数值式

用 R168 的坐标记任一个 $e_{q,q}$ 的有限/奇异项为 $(u,v_0)$，即有限项 $uK_q$、奇异项 $v_0F_q$。由 $\gamma_q=0$，加 $d_0$ 不改变这两项；而加 $t d_q^*$ 同时把它们改为 $(u+t\lambda_q,v_0+t)$。因此

$$
v:=v_0-\frac{u}{\lambda_q} \tag{200.20}
$$

是与 primitive 选择无关的规范量。它等价于先减 $(u/\lambda_q)d_q^*$，将有限项杀零，再读取奇异坐标。

对 $w_q$ 的有限/奇异坐标 $(a,b)$，R168 的同一 Weil 和算术 reciprocity 规范给

$$
\langle w_q,(c,d)\rangle_q=2(ad-bc),\qquad a=\lambda_q b. \tag{200.21}
$$

所以 $\langle w_q,e_{q,q}\rangle=2av$。本例 R171 给

$$
p=43,\quad\lambda_q=16,\quad
\frac{q+1}{43}=11\pmod{43},\quad x=-1,
$$
$$
a=27\epsilon,\qquad b=-\epsilon.
$$

结合 $e_{p,q}=28K_q$：

$$
\Omega_2=2(27\epsilon v+28\epsilon)
=\epsilon(13+11v)\pmod{43}.
$$

故 $\Omega_2=0$ 恰为 $v=34$。这同时说明两个乘法符号只改变总阻碍的共同非零倍数，不改变本层可积性的零性。

## 10. Norm 算法必须保持的边界

式 (200.18) 中的 $e_q$ 是 $S$-supported primitive。由 Hasse norm 定理取得一个普通 Norm 见证，并不保证它在 $S$ 外没有除子；若有外支撑，必须加入同一 primal 类的局部 Artin 修正。这个修正在附属笔记中逐项给出，符号为正。未经支撑修正的局部残余指数不等于 (200.20)。

R201 进一步证明可以选择两个普通代数 $S$-单位的精确 Norm 见证，并给完整 Kummer lift 所规定的根修正。它证明计算存在且可收敛到正确对象，没有算出实际见证，也没有算出 $v$。在 R201 的低权剩余符号 $L$ 下，$v=-4L-12$，所以

$$
\Omega_2=\epsilon(10-L).
$$

旧 primal Robert 首阶 Frobenius 值 $10$、纯 $p$ 导数中的某个原始坐标 $10$、以及这里的未知 $L$ 是不同定义的量。只有实际同投影、同 $S$ 支撑、同完整 Kummer 根的 Norm 求值，或一条完整证明的互反恒等式，才能判定此最后标量。

## 11. 依赖与原始规范来源

- [R168](R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)：同一 $F_q,K_q$、算术 Frobenius、Weil 配对和 $2(ad-bc)$。
- [R171](R171-principal-norm-selflocal-tate-slope.md)：固定 $q$、$\gamma_q=0$、$\lambda_q=16$、$z=11$ 的严格证书。
- [R176](R176-fixed-support-nonlinear-tate-lifting-tower.md)：固定完整局部型的阻碍空间、$\eta$ 调整和 $d_0$ 对偶线。
- [R196](R196-cm-reference-bockstein-and-the-actual-norm-field.md)：实际 CM/reference Bockstein、纯 $p$ 角色与反循环符号。
- [R198](R198-p-squared-robert-norm-and-a-secondary-contribution.md)：纯 $p$ Norm primitive 的实际贡献。
- [R201](R201-s-class-vanishing-and-the-canonical-norm-residue.md)：$S$-单位 Norm 存在与完整根修正。
- Milne, *Arithmetic Duality Theorems*, 2nd ed., I Theorems 4.10 and 5.1：Poitou–Tate 与全局互反；<https://www.jmilne.org/math/Books/ADTbook.pdf>。
- Milne, *Class Field Theory*, III §4：算术 reciprocity 下 $\chi\cup\kappa(\pi)$ 的符号；<https://www.jmilne.org/math/CourseNotes/CFT.pdf>。
- Nekovář–Plater, Asian J. Math. 4 (2000), §1.2.7：$e(\zeta,t^{1/p})=\zeta$；<https://webusers.imj-prg.fr/~jan.nekovar/pu/parity.pdf>。

本稿的新内容是 §§3–9 的完整规范连接、二阶矩阵阶数和 exact-dual cancellation。没有使用尚未取得的普通 Norm 见证、未发表的非消失命题或把普通 lift 当固定晶体 lift 的替代论证。
