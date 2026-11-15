# 保原下降算子的加权交换 resolvent、同源合法链平滑与配对内交换

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 已证结论

本文保原连续远尾
$$
D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad x\ge1,
$$
以及任意已经固定的真实并头 $C=A_m+D_{<}$，$C^h=0$，$x=m+R$。下面构造一个作用于原物理硬核空间的有界算子 $\mathcal R_x$，使
$$
\|\mathcal R_x\|\le2,\qquad
D_x\mathcal R_x=\mathcal R_xD_x,\qquad
C\mathcal R_x=\mathcal R_xC.
\tag{0.1}
$$
它保持每个远孔层、每个 $\ker D_x^j$ 和每个实际 head 旗；不声称与正交投影 $P_{\ker D_x^j}$ 对易。

该算子既在原物理空间强趋 $I$，其伴随也强趋 $I$。它能整体作用于同一个实际 $u_Q$ 的左、右链；全部源、封口和自然域都保留。因而可在原同顶部双线性恒等式内把它从顺次 MP 之前移到之后，差额由一个真正纯 future 零源核消掉，而非假设它与 MP 对易。

此外，对任意向量 $v$，
$$
\sum_{i\ge x}\|P_i^-\mathcal R_xv\|^2
\le x^{-1}\|v\|^2,
\qquad
\|\mathcal L_x\mathcal R_xv\|\le12x^{-1}\|v\|,
\tag{0.2}
$$
其中 $\mathcal L_x$ 是下文定义的闭直和发生器。整条真正交 jet 分解后仍有总交换行界 $81x^{-1}\|v\|^2$。

本文尚未控制 $\mathcal R_x\mathscr A_n$ 或 $\mathscr A_n\mathcal R_x$ 的完整返回作用，不宣称已证明 $N=M$。

## 1. 真正与 $D_x$ 对易的局部交换

记 $U_i$ 为物理位 $i,i+1$ 的酉交换，
$$
P_i^-=\frac{I-U_i}{2},\qquad
\theta_i=\log\frac{i+2}{i+1}.
$$
在二位基 $00,10,01,11$ 上置
$$
S_i=\operatorname{diag}(1,e^{-\theta_i},e^{\theta_i},1),
\qquad
V_i=S_iU_iS_i^{-1}.
\tag{1.1}
$$
将该二位权同时平衡为 $[(i+1)(i+2)]^{-1}$ 后的下降与 $U_i$ 对易，而原下降由 $S_i$ 相似得到。因此
$$
D_xV_i=V_iD_x,\qquad V_i^2=I.
\tag{1.2}
$$
$V_i$ 一般非自伴，不可用 (1.2) 推出它与原正交核投影对易。

$V_i$ 在 $00,11$ 上为恒等，在单占据空间上为
$$
\begin{pmatrix}0&e^{-2\theta_i}\\e^{2\theta_i}&0\end{pmatrix}.
$$
于是准确有
$$
\operatorname{Re}(I-V_i)
=2P_i^--(\cosh(2\theta_i)-1)U_iP_{i,\mathrm{one}},
\tag{1.3}
$$
其中 $P_{i,\mathrm{one}}$ 是该对单占据投影。因
$\|U_iP_{i,\mathrm{one}}\|=1$，
$$
\operatorname{Re}(I-V_i)
\succeq2P_i^--(\cosh(2\theta_i)-1)I.
\tag{1.4}
$$
而
$$
\epsilon_x:=\sum_{i\ge x}(\cosh(2\theta_i)-1)
=2\sum_{i\ge x}\sinh^2\theta_i
\le2\sum_{i\ge x}(i+1)^{-2}\le\frac2x.
\tag{1.5}
$$

## 2. 闭直和发生器和统一 resolvent

令 $\mathcal H_n$ 为远孔 $n$ 层。在该层的有限物理支撑核心上定义
$$
\mathcal L_{x,n}=\sum_{i\ge x}(I-V_i).
\tag{2.1}
$$
对一个 $n$ 孔物理基向量，只有单占据相邻边贡献，最多 $2n$ 条。每个非对角系数至多 $4$，同样的列和估计也成立。因此 Schur 行列和判准给
$$
\|\mathcal L_{x,n}\|\le10n.
\tag{2.2}
$$
所以 (2.1) 在每一固定层唯一延拓为有界算子。$n=0$ 时为零。

定义全空间的闭直和算子
$$
\mathcal L_x=\bigoplus_{n\ge0}\mathcal L_{x,n},\qquad
\operatorname{Dom}\mathcal L_x
=\left\{v:\sum_n\|\mathcal L_{x,n}v_n\|^2<\infty\right\}.
\tag{2.3}
$$
不声称 $\mathcal L_x$ 在全孔层直和上有界。

记交换形式
$$
\mathfrak e_x(v)=\sum_{i\ge x}\|P_i^-v\|^2
$$
为非负和的自然闭形式。由有限和 (1.4)、固定层延拓和单调收敛，
$$
\operatorname{Re}\langle\mathcal L_xv,v\rangle
\ge2\mathfrak e_x(v)-\epsilon_x\|v\|^2
\tag{2.4}
$$
在其自然域上成立。

取
$$
\lambda_x=\frac x4,\qquad
\mathcal R_{x,n}=(I+\lambda_x\mathcal L_{x,n})^{-1}.
\tag{2.5}
$$
由 $\lambda_x\epsilon_x\le1/2$，$I+\lambda_x\mathcal L_{x,n}$ 及其伴随的实部均至少为 $I/2$。它们有闭像且伴随核为零，故 (2.5) 是整个固定层上的有界逆，并且
$$
\|\mathcal R_{x,n}\|\le2.
$$
因此
$$
\mathcal R_x=\bigoplus_{n\ge0}\mathcal R_{x,n}
=(I+\lambda_x\mathcal L_x)^{-1}
\tag{2.6}
$$
是全物理空间上的有界算子，范数至多 $2$，像包含于 (2.3) 的域。

置 $z=\mathcal R_xv$，由 (2.4) 得
$$
\boxed{
\operatorname{Re}\langle v,\mathcal R_xv\rangle
\ge\frac12\|\mathcal R_xv\|^2
+\frac x2\,\mathfrak e_x(\mathcal R_xv).
}
\tag{2.7}
$$
再由
$$
\frac12\|z\|^2+\frac x2\mathfrak e_x(z)
\le\|v\|\|z\|
$$
优化右边关于 $\|z\|$ 的二次式，得到
$$
\boxed{
\mathfrak e_x(\mathcal R_xv)\le\frac{\|v\|^2}{x}.
}
\tag{2.8}
$$
最后
$$
\mathcal L_x\mathcal R_x=\lambda_x^{-1}(I-\mathcal R_x)
$$
给
$$
\boxed{\|\mathcal L_x\mathcal R_xv\|\le\frac{12}{x}\|v\|.}
\tag{2.9}
$$

## 3. 对易、旗保持与共同原物理强极限

在有限支撑核心上，(1.2) 给
$$
D_x\mathcal L_{x,n}=\mathcal L_{x,n-1}D_x.
$$
两边在固定相邻孔层之间有界，故恒等式延拓到完整固定层。由 resolvent 恒等式，
$$
D_x\mathcal R_{x,n}=\mathcal R_{x,n-1}D_x.
\tag{3.1}
$$
原 $D_x$ 在全空间有界，故 (3.1) 也给全空间的有界对易式。作用于独立强头的 $C$ 与 $\mathcal R_x$ 对易。$\mathcal R_x$ 保持每个远孔层，故与所有远孔 cut 及原总尾孔 cut 对易。

因此 $\mathcal R_x$ 保持 $\ker D_x^j$、$\ker C^k$、实际左方程空间 $V_Q$、实际有限核 $K_Q$，以及原裸商用到的各个闭零源旗。它在裸商上诱导范数至多 $2$ 的算子。这里“保持旗”只指不变子空间，不包含与各正交旗投影对易的断言。

所有固定有限物理向量在充分大的 $x$ 后都处于远尾真空层，故被 $\mathcal R_x$ 和 $\mathcal R_x^*$ 精确固定。有限物理支撑稠密，且二者范数均至多 $2$，所以在同一个原物理 Hilbert 空间，
$$
\boxed{\mathcal R_x\longrightarrow I,\qquad
\mathcal R_x^*\longrightarrow I
\quad\text{强收敛}.}
\tag{3.2}
$$
此处不比较不同 Fock 扩张，也没有给强收敛速率。

## 4. 整条正交 jet 旗后的行预算

沿用[整条正交 jet 旗交换行稿](R271-appendix-complete-orthogonal-jet-flag-preserves-fixed-test-exchange-row-budget.md)的
$$
F_r=P_{\ker D_x^r}-P_{\ker D_x^{r-1}}.
$$
该稿已对任意实际 $z$ 证明
$$
\left(\sum_r\|P_i^-F_rz\|^2\right)^{1/2}
\le\|P_i^-z\|+4\theta_i\|z\|.
$$
取 $z=\mathcal R_xv$，再对 $i$ 作 Hilbert 直和三角不等式，利用 (2.8)、$\sum\theta_i^2\le1/x$ 及 $\|\mathcal R_x\|\le2$，得
$$
\begin{aligned}
\left(\sum_{i\ge x,r\ge1}
\|P_i^-F_r\mathcal R_xv\|^2\right)^{1/2}
&\le\mathfrak e_x(\mathcal R_xv)^{1/2}
+4\left(\sum_i\theta_i^2\right)^{1/2}\|\mathcal R_xv\|\\
&\le\frac9{\sqrt x}\|v\|.
\end{aligned}
$$
即
$$
\boxed{
\sum_{i\ge x,r\ge1}
\|P_i^-F_r\mathcal R_xv\|^2
\le\frac{81}{x}\|v\|^2.
}
\tag{4.1}
$$
对任意输出孔层集合 $I$，在 (2.8)、(2.9)、(4.1) 中取 $v=P_Iu$ 即可；它们共同保留 $\|P_Iu\|$，不把每层估计再乘层数。

## 5. 同一个实际顶部的合法右链与配对内交换

沿[同顶部完整顺次链](R271-appendix-same-top-sequential-projection-negative-form-and-complete-return-scalar.md)，现在固定已付窗口中的同一
$$
u=u_Q=P_{V_Q}w-P_{K_Q}w,
$$
并保 $C=A_m+D_{<}$、$D=D_x$、$C^h=0$。对合法 cut $p$ 假设
$$
p+h+R<Q.
\tag{5.1}
$$
记 $u_n$ 为远孔层分量，实际源为
$$
r_p=Cu_p=-Du_{p+1}.
$$
原顺次右链是
$$
c_{p,j}
=D_{p+j}^\dagger\cdots D_{p+1}^\dagger
(-C)^{j-1}r_p
=-\mathcal P_{p+j,j}u_{p+j},
\qquad1\le j\le h,
\tag{5.2}
$$
其中
$$
\mathcal P_{n,j}
=D_n^\dagger\cdots D_{n-j+1}^\dagger D^j.
$$
固定层所有这些 MP 都有界。原链满足
$$
Dc_{p,1}=r_p,\qquad Cc_{p,j}+Dc_{p,j+1}=0,\qquad c_{p,h}=0.
$$
其头旗由
$$
C^{h-j+1}c_{p,j}
=(-1)^{j-1}D^\dagger\cdots D^\dagger C^h r_p
=(-1)^{j-1}D^\dagger\cdots D^\dagger C^{h+1}u_p=0
$$
准确保证。

对整条左、右链同时作用 $\mathcal R_x$，由 §3 得到同一新源
$$
r_p^{\rm reg}=\mathcal R_xr_p
=C\mathcal R_xu_p
$$
的合法左 prefix 与普通完整右链 $\mathcal R_xc_{p,j}$。全部头旗、尾旗及 $c_h=0$ 封口保持。按 (5.1)，拼成的向量仍在原 $K_Q$；没有只在高商中闭口。

也可以对这同一新源重新取顺次 MP，得到
$$
c'_{p,j}
=-\mathcal P_{p+j,j}\mathcal R_xu_{p+j}.
$$
它与 $\mathcal R_xc_{p,j}$ 的差满足首源为零的全部右方程，支撑只在 $p+1,\ldots,p+h$，并满足相同 head 旗和顶端封口。因此二者之差是一个真正纯 future 向量，属于同一 $K_Q$。由 $u\perp K_Q$，
$$
\boxed{
\sum_{j=1}^h
\langle u_{p+j},
(\mathcal R_x\mathcal P_{p+j,j}
-\mathcal P_{p+j,j}\mathcal R_x)u_{p+j}\rangle=0.
}
\tag{5.3}
$$
这只是对同一个实际 $u$ 的完整链配对恒等式，不是算子交换式。

将 prefix 与负右链拼成真核，还得到
$$
\boxed{
\langle P_{\le p}u,\mathcal R_xP_{\le p}u\rangle
=-\sum_{j=1}^h
\langle u_{p+j},\mathcal R_x\mathcal P_{p+j,j}u_{p+j}\rangle
=-\sum_{j=1}^h
\langle u_{p+j},\mathcal P_{p+j,j}\mathcal R_xu_{p+j}\rangle.
}
\tag{5.4}
$$
若采用另一内积线性 convention，两边同时共轭即可。

对 $p=a,\ldots,b$ 求和，令
$$
\mathscr A_n=
\sum_{\substack{1\le j\le h\\a\le n-j\le b}}\mathcal P_{n,j}.
$$
则
$$
\boxed{
\sum_{p=a}^b\langle P_{\le p}u,\mathcal R_xP_{\le p}u\rangle
=-\sum_{n=a+1}^{b+h}
\langle u_n,\mathcal R_x\mathscr A_nu_n\rangle
=-\sum_{n=a+1}^{b+h}
\langle u_n,\mathscr A_n\mathcal R_xu_n\rangle.
}
\tag{5.5}
$$
真实两端 partial 全部保留，没有把端点层换成完整内部和。

## 6. 原同一个 $w$ 的非零左锚和实际 future 小量

沿[固定测试同顶部配对](R271-appendix-actual-fixed-test-adjacent-swap-row-and-same-top-bilinear-pairing.md)及已经支付的母向量、late-cut 窗口，同一 $w\in W$ 满足
$$
\sup_{a\le p\le b}\|P_{\le p}u_Q-w\|\longrightarrow0.
$$
由于 (3.2) 和 $\|\mathcal R_x\|\le2$，
$$
\sup_{a\le p\le b}
\|\mathcal R_xP_{\le p}u_Q-w\|
\le
2\sup_{a\le p\le b}\|P_{\le p}u_Q-w\|
+\|(\mathcal R_x-I)w\|
\longrightarrow0.
$$
所以当 $w\ne0$ 时，(5.5) 的每个左配对实部对充分大的 $m$ 都至少为 $\|w\|^2/2$。这是同一原 $w$ 的强极限锚，没有用未知尾乘增长常数。

令 $F$ 为该窗真实 future 远孔带投影。由 (2.8)、(2.9)、(4.1)，准确有
$$
\mathfrak e_x(\mathcal R_xFu_Q)\le x^{-1}\|Fu_Q\|^2,
$$
$$
\|\mathcal L_x\mathcal R_xFu_Q\|
\le12x^{-1}\|Fu_Q\|,
$$
$$
\sum_{i\ge x,r\ge1}
\|P_i^-F_r\mathcal R_xFu_Q\|^2
\le81x^{-1}\|Fu_Q\|^2.
\tag{6.1}
$$
因此平滑端不仅有交换形式小量，还有同一完整发生器的小残量；各项仍保真实 future 范数，没有另选来源。

## 7. 仍未支付的预算

本文不由 (6.1) 推出 $\mathscr A_n\mathcal R_xu_n$ 小，也没有假设 $\mathcal R_x$ 与正交核投影、MP 或 $\mathscr A_n$ 对易。

若将来能对原模型的同源族或适当完整空间支付
$$
-\sum_n\operatorname{Re}
\langle u_n,\mathcal R_x\mathscr A_nu_n\rangle
\le c_m Q\|Fu_Q\|^2
$$
并使既有同窗或跨 $m$ 条件成立，(5.5)--(6.1) 才可接原闭口。当前已证明的新增内容是一个有界、保持原 $D$ 与全部真实链约束的同源平滑，以及在实际核配对中可准确交换其放置位置。非正交返回预算仍开。
