# R506 — 原反射轴的整个四度核心与完整 W/C 深度矩形

日期：2026-11-14。**状态：已证明。** 本篇在 R493、R496 的同一个六 sigma 来源中，支付真实反射轴的整个 theta 核。该方向的物理范数为一，但原半系数使实际生成轴具有四度，必须保留二重覆盖和所有周期中心。完成绝对定标后，它在原四态中固定 \(u,v\)，反号 \(z,h\)，并与旧 \(W\) 轴给任意独立深度的完整矩形。

所有等式均保留六个原输入及全部伴随条件。这个方向会移动第一输出 \(Y_s\)，因而本篇不把原中央零免费传播到其深域，也不将新核心视作主目标已经完成。

## 1. 原完整来源、反射和实际坐标

令
\[
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
\gamma=3+\omega,\quad \bar\gamma=2-\omega,
\]
并保原普通 ray、原周期和 R496 的
\[
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda,\qquad \kappa=p\lambda^2.
\]
六输入列为
\[
X=(\xi_1,\xi_2,\xi_3,\xi_4,c,d_0)^t,\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84.
\]
两个原物理输出为
\[
Y_s=(\delta,2\delta,\gamma,\bar\gamma,1,2)X,\qquad
W=(\delta,2\delta,\gamma,\bar\gamma,3\delta,4)X.
\tag{1}
\]
记列向量
\[
b=(1,0,\omega,-\omega^2,-1,0)^t,\qquad
\bar b^{\,t}b=4.
\]
R493 的真实反射是
\[
\boxed{\mathcal U=I-\tfrac12b\bar b^{\,t},\qquad
\mathcal U^2=I,\qquad W\mathcal U=W,\qquad
\mathcal U_*\rho_0=\rho_0+h.}
\tag{2}
\]
这里 \(h=\omega^2T_*\rho_0\) 是原六输入上的完整来源，不是单独边际。

定义本篇的物理输出
\[
\boxed{
C=\tfrac12\bar b^{\,t}X
=\tfrac12(\xi_1+\omega^2\xi_3-\omega\xi_4-c).
}
\tag{3}
\]
其 Hermitian 范数为一，且 \(\langle C,W\rangle=0\)。取五个明确伴随
\[
B_1=\xi_3-\omega\xi_1,\quad
B_2=\xi_4+\omega^2\xi_1,\quad
B_3=c+\xi_1,\quad B_4=\xi_2,\quad B_5=d_0.
\tag{4}
\]
每个 \(B_j\) 都与 \(C\) 正交。完整矩阵 \((C,B_1,\ldots,B_5)\)
的行列式为 \(\pm2\)：在 \((\xi_1,\xi_3,\xi_4,c)\) 上，消去后三行后第一行系数为二。故这是当前所有普通 \(p>19\) 上的整可逆坐标变换。

前三伴随的完整 Gram 为
\[
\begin{pmatrix}
2&-\omega^2&-\omega\\
-\omega&2&\omega^2\\
-\omega^2&\omega&2
\end{pmatrix},
\qquad \det=4;
\tag{5}
\]
\(B_4,B_5\) 各范数一、与前三行正交。特别没有将非对角伴随 Gram
误当五个独立 sigma 来源。

对 \(n\ge0\) 定义真正的物理压深
\[
\boxed{
A_{C,n}=I+\frac{\kappa^n-1}{4}b\bar b^{\,t}.
}
\tag{6}
\]
它把 \(C\) 乘以 \(\kappa^n\)，固定全部五个 \(B_j\)，且
\(A_{C,n}\mathcal O_p^6=\{C\in p^n\mathcal O_p\}\)。
将 \(\kappa^n\) 换成 \(-1\) 时，(6) 正是 (2)。

## 2. 真正的四度空间与全部 quarter 来源

(3) 的半系数不能在 theta 空间中略去。固定 (4)，令物理第一坐标
为 \(C=2z\)。反解原变量时，四个变化的原 sigma 输入准确为
\[
\xi_1=z+\text{伴随项},\quad
\xi_3=\omega z+\text{伴随项},\quad
\xi_4=-\omega^2z+\text{伴随项},\quad
c=-z+\text{伴随项}.
\tag{7}
\]
另外两个输入完全不变。因此原完整生成函数在 \(z\) 上属于标准
偶半特征的 \(\mathcal S_4\)。四个单位系数的范数和为四；
与全部伴随的 Hermitian 交叉为零，周期公式中的线性伴随指数
相消。四个原 odd 半特征的乘积是偶特征，没有遗漏的 flat twist。

沿用原十六个实际来源
\[
f_m=\mathsf T^{72}_{m/4,W}\rho_0,
\qquad m\in\mathcal O_K/4\mathcal O_K.
\tag{8}
\]
因为 \(Wb=0\)，这些原 quarter 平移在 (7) 的第一坐标上全为零，
故它们全部属于同一个 \(\mathcal S_4\) 与完整伴随张量格。
(2) 与每个 (8) 的完整 canonical lift 交换，不只在 projective
Heisenberg 商中交换。

若还要同时展示旧 \(W\) 和本篇 \(C\)，可取四个实际伴随
\[
Q_j=72B_j-\langle B_j,W\rangle W,\qquad 1\le j\le4.
\tag{9}
\]
由于
\[
W=\gamma B_1+\bar\gamma B_2+3\delta B_3+2\delta B_4+4B_5,
\]
完整框架
\[
(2C,W,Q_1,Q_2,Q_3,Q_4)
\tag{10}
\]
的行列式为 \(\pm16\cdot72^4\)。其前两行 Gram 是
\(\operatorname{diag}(4,72)\)，与后四行正交。后四行之间的完整
非对角 Gram 保持；若在它们上清 quarter flat 特征，只需原固定
四倍覆盖，前两行不动。所有覆盖的分母在当前 \(p\) 上均为单位。
这给下文矩形公式的完整实际坐标，并非仅仅两个已知边际。

## 3. 整个四度核心的绝对定标

原 ray 模八给
\[
\pi_0\equiv7+2\omega\pmod8,\qquad
N\pi_0\equiv7\pmod8,\qquad
g=\pi_0/\bar\pi_0\equiv3\pmod8.
\tag{11}
\]
在 \(\mathcal S_4\) 的完整 Heisenberg 生成元上，乘 \(g\) 与
几何反射 \(z\mapsto-z\) 的作用相同。确切地，对生成平移
\(\ell/4\) 有
\(3\ell/4=-\ell/4+\ell\)；标准四度偶特征在整周期 \(\ell\)
上为一，而该同向周期产生的交替 cocycle 为零。由两个生成元
及共同中心，整个有限 Heisenberg 作用相同。

记 \(\mathscr R_C\) 为真实几何反射。完整 Heisenberg 表示
不可约，故真实归一核心 \(K_4\) 满足
\[
K_4=c\,\mathscr R_C
\tag{12}
\]
于整个 \(\mathcal S_4\)，其中 \(c\) 是尚须定标的单位。

使用非零实际截面 \(\sigma(2z)\) 作绝对锚。它属于同一个标准
\(\mathcal S_4\)，并且固定二倍单位变换与原普通限制相容。
原 sigma 的真实 core 是 \(\beta=-\lambda\)，故
\[
K_4\sigma(2z)=-\sigma(2z).
\]
另一方面，sigma 的实际奇性给
\(\mathscr R_C\sigma(2z)=-\sigma(2z)\)。因此 \(c=1\)，准确得到
\[
\boxed{K_4=\mathscr R_C\quad\text{于整个 }\mathcal S_4.}
\tag{13}
\]
这是整空间定标，不是只在该锚截面上声称一个特征值。

由于 (7) 的二倍是 \(p\)-单位，(13) 返回原物理变量给
\[
\boxed{
\nu_\mu|_{C\in p^n\mathcal O_p}
=\lambda^n(A_{C,n})_*\mathcal U_*^{\,n}\nu_\mu
}
\tag{14}
\]
对全部十六个 (8) 及其任意线性组合成立。
五个原伴随的任意紧开条件和连续测试都保留在该等式中。

## 4. 反射在原四态中的完整作用

沿用 R496 的
\[
e_0=\rho_0,\quad e_1=K_W\rho_0,\quad h=e_1+e_2,
\]
\[
u=e_0+h/2,\qquad v=e_1-h/2,\qquad z=q-h/2.
\tag{15}
\]
旧 \(W\) 归一核心在该整个四态空间上是
\[
K_W(u,v,z,h)=(v,u,-z,-h).
\tag{16}
\]
先由 (2) 和 \(\mathcal U^2=I\) 得
\(\mathcal U_*h=-h\)。反射与旧 \(W\) 的整核心交换，故
\[
\mathcal U_*e_1=K_W(e_0+h)=e_1-h.
\]
于是它固定 \(u,v\)。

为确定余下的完整 \(z\)，令
\[
H_2=\sum_{\ell\in\mathcal O_K/2}\mathsf T^{72}_{\ell/2,W}.
\]
原完整半周期相位给 \(h=-H_2e_0/2\)。
又因 (2) 与所有 (8) 交换，整个十六来源张成空间上有
\[
\mathcal U_*=I-\tfrac12H_2.
\tag{17}
\]
R496 的同一 quarter 系数逐项给
\(H_2u=H_2v=0\)、\(H_2z=4z\)、\(H_2h=4h\)。
因此
\[
\boxed{\mathcal U_*(u,v,z,h)=(u,v,-z,-h).}
\tag{18}
\]
这些都是完整来源身份，保原 CM13/19 条件及原全部隐藏伴随；
没有从一个零质量边际推回联合恒等。

## 5. 任意独立深度的 W/C 完整矩形

记旧物理压深
\[
A_{W,m}=I+\frac{\kappa^m-1}{72}\bar W^{\,t}W.
\tag{19}
\]
这里 \(W\) 在矩阵式中表示 (1) 的行向量。
因 \(C\perp W\)，(6)、(19) 交换；它们也都固定 (9)。
(16)、(18) 的来源算子同样交换。

于是对任意 \(m,n\ge0\)，整个原六输入上准确有
\[
\boxed{
\nu_\mu|_{\{W\in p^m,\ C\in p^n\}}
=\lambda^{m+n}(A_{W,m}A_{C,n})_*
K_W^m\mathcal U_*^{\,n}\nu_\mu .
}
\tag{20}
\]
证明可在 (10) 的完整张量格中先取一个方向的限制，再取另一个；
正交性保留内层条件，而已付完整中心保证同一绝对标量。
这个过程从不丢弃四个真实伴随的条件。

具体而言，\(u,v\) 随 \(m\) 的奇偶交换，完全不依赖 \(n\)；
\(z,h\) 的额外符号都是 \((-1)^{m+n}\)。
单位环带、两个浅补集以及任意深矩形之差，均可由 (20)
对实际指示函数作差得到。不同物理域之间没有额外的零积分结论。

## 6. 第一输出的准确变化和原自由 sigma 的关系

逐项计算
\[
Y_sb=3\delta-1=2+6\omega,\qquad Wb=0.
\]
故本篇核心真正的第一权运输是
\[
\boxed{
Y_s\circ A_{C,n}
=Y_s+(\kappa^n-1)(1+3\omega)C,\qquad
W\circ A_{C,n}=W.
}
\tag{21}
\]
所以 \(C\) 是纯 \(W\) 伴随，并非纯 \(Y_s\) 伴随。
使用 (14)、(20) 积分时，原 \(Y_s\) 单位条件、Mellin 权和
任何原 \(Y_s\) 伴随多项式必须按 (21) 一并移动。

最后，把该方向放回 R493 的实际三阶矩阵。于
\(I=(\xi_1,\xi_3,\xi_4,c)\)，原矩阵准确为
\[
T_I=\frac12
\begin{pmatrix}
-\omega&1&\omega^2&\omega\\
-\omega^2&-\omega&1&-\omega^2\\
-1&-\omega^2&-\omega&1\\
-\omega&1&-\omega^2&-\omega
\end{pmatrix},
\tag{22}
\]
其余两输入固定。第三列与 (3) 直接给
\[
\boxed{
Te_{\xi_4}=\omega^2b/2,\qquad
CT=\omega^2\xi_4,\qquad
(T^{-1}X)_{\xi_4}=\omega C.
}
\tag{23}
\]
所以在 \(h=\omega^2T_*\rho_0\) 上，(14) 的 scalar
确实是 \(\beta\)：它就是原自由 \(\xi_4\)-sigma 的真实核心
经 (22) 的完整运输，与 (18) 的负号相符。

(23) 也说明 R493 中的 \(\ell_4\) 权为何必须按
\(\ell_4=\omega C\) 保持。不能将其默认为纯 \(Y_s\) 伴随；
更不能把本篇六输入的算子直接作用到 R500 已消三个 \(Q\) 的
三输入表示，却不恢复那些原条件。与 R504 的新六十五度方向
联立时，使用的是本篇 (13)、(18) 的完整核心，所有混合管
继续按实际矩阵运输。

## 依赖与范围

- [R493：原六 sigma 因式及真实三阶/反射矩阵](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R496：原四态、全部 quarter 相位和完整 W 核](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R501：同一五伴随的完整 CM 交换](R501-whole-cm-exchange-and-identical-five-companion-rows.md)。

本文为完整周期中心、整坐标和来源恒等式证明，没有新增素数扫描。
原三条固定秩二曲线的中央非零以及固定曲线上的无穷多个 \(p\)
仍待证明；(20) 本身不控制其完整单位补域。
