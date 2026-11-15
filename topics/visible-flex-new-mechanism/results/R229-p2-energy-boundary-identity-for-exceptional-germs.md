# R229：二次 k 例外端芽的 p2 主算子与准确 quartic 边界身份

日期：2026-11-15。完整纸面恒等式；没有新的研究计算。

本稿接 [R227 的例外端芽](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md) 中的二次算子 $\mathcal G_b$，而不是 [R138](R138-general-pure-G-identity-and-affine-orbit-kernel.md) 中恰好也记作 G 的静态四次系数。R138 (2) 给出了 $\Phi_{p_2}$ 的准确原式；其后成员证书不等于本稿的积分边界身份，也不被重新运行。

## 1. 原算子与必要的左尾

令 $I=[l,r]$，所有输入在两端 collar 恒零。记 $z=x+b$，正右积分

$$
J(F)(x)=\int_x^rF(\eta)\,d\eta,
$$

并定义双线性能量

$$
E_b(u,v)=\frac14\int_l^r
\bigl(z^2u''v''+2u'v'\bigr)\,dx.
\tag{1}
$$

对于复输入始终使用普通双线性乘积，没有复共轭。R227 的原算子为

$$
8\mathcal G_b(f,g)=
4zfg-2z^2(fg'+f'g)+2z^3f'g'
+z^2J\bigl(z^2f''g''+2f'g'\bigr).
\tag{2}
$$

特别 $\mathcal G_0=-\Phi_{p_2}/2$，符号与 R73/R138 相同。

先设 $b>-l$，所以 z 在整个 I 严格为正。对 $f=za,g=zc$，准确乘积微分给

$$
z^2f''g''+2f'g'
=z^4a''c''+
D_x\bigl(2z^3a'c'+2zac\bigr).
\tag{3}
$$

共同右 collar 的端项为零。把 (3) 放入 (2)，全部局部项相消，得到

$$
\boxed{
\mathcal G_b(f,g)
=\frac{z^2}{8}J\!\left[
z^4\left(\frac fz\right)''
\left(\frac gz\right)''
\right].
}
\tag{4}
$$

这只是同一个原算子的分部积分表达式；没有改变实际输入 profile、右锚或几何。

取紧支撑复输入 q，置

$$
y=\frac qz,\qquad R=y'',\qquad
C_b(q)=\int_l^rz^4R^2\,dx.
$$

由 (3) 的两端边界均零，

$$
\boxed{
C_b(q)
=I_2^*(q,q)+2bI_1(q,q)+b^2I_0(q,q).
}
\tag{5}
$$

令 $A=\mathcal G_b(q,q)$。在左 collar，

$$
A(x)=\frac{z^2}{8}C_b(q).
\tag{6}
$$

因此 q 紧支撑并不自动使 A 紧支撑。后面的能量中不能丢掉 (6)。

## 2. 两次恢复的准确短式

记 $H=J(z^4R^2)$，则 $A/z=zH/8$。因

$$
H'=-z^4R^2,\qquad
H''=-4z^3R^2-2z^4RR',
$$

有

$$
\boxed{
\left(\frac Az\right)''
=-\frac{z^4}{4}R(3R+zR').
}
\tag{7}
$$

再次使用 (4)，

$$
\mathcal G_b(q,A)
=-\frac{z^2}{32}J\bigl(z^8R^2(3R+zR')\bigr).
$$

括号中的密度是 $(z^9R^3)'/3$。右端 R 为零，所以

$$
\boxed{
B:=\mathcal G_b(q,A)=\frac{z^{11}R^3}{96}.
}
\tag{8}
$$

B 在两端 collar 恒零；这一结论不要求 $C_b(q)=0$。

## 3. 完整 quartic 是左边界项

由 (3)，任意右 collar 为零的 $u=za,v=zc$ 有

$$
E_b(u,v)=
\frac14\int_l^rz^4a''c''\,dx
+\frac12\bigl[z^3a'c'+zac\bigr]_l^r.
\tag{9}
$$

将 (7)、(8) 代入积分部分，逐项乘积微分得到

$$
\begin{aligned}
&\frac14z^4\left[\left(\frac Az\right)''\right]^2
+\frac12z^4R\left(\frac Bz\right)''\\
&\qquad =
D_x\left[
\frac{3z^{13}R^4+z^{14}R^3R'}{64}
\right].
\end{aligned}
\tag{10}
$$

右侧在两端为零，因为 q 紧支撑。式 (9) 在 $(q,B)$ 上也无边界项；在 $(A,A)$ 上则必须用 (6)。左端

$$
\frac Az=\frac{zC_b(q)}8,\qquad
\left(\frac Az\right)'=\frac{C_b(q)}8.
$$

由此得到完整身份

$$
\boxed{
E_b(\mathcal G_b(q,q),\mathcal G_b(q,q))
+2E_b\bigl(q,\mathcal G_b(q,\mathcal G_b(q,q))\bigr)
=-\frac{(l+b)^3}{64}\,C_b(q)^2.
}
\tag{11}
$$

特别，不能仅凭 q 紧支撑就把左侧称为 universal 零算子。一般非零的 $C_b(q)$ 通过二次恢复的左尾留下了准确的 (11)。

公式 (2)、(1)、(5) 与 (11) 的两侧都是 b 的有限多项式。故先在 $b>-l$ 的开参数区证明后，(11) 也以多项式身份延至任意实 b。若 z 在 I 中过零，这一延拓只涉及原始多项式算子与最终能量身份；不把含 $q/z$ 的 (4)、$R=(q/z)''$ 或 $J(z^4R^2)$ 宣称为该参数处收敛的原积分。

## 4. 对合法三矩圆的结论及未付范围

R183/R199 的合法复输入 $q=f+ig$ 满足

$$
I_0(q,q)=I_1(q,q)=I_2^*(q,q)=0.
\tag{12}
$$

于是对每个 b，$C_b(q)=0$，A 的左尾准确消失，且

$$
\boxed{
E_b(\mathcal G_b(q,q),\mathcal G_b(q,q))
+2E_b\bigl(q,\mathcal G_b(q,\mathcal G_b(q,q))\bigr)=0.
}
\tag{13}
$$

这个零来自完整双线性三矩条件，不是正能量或复绝对值；(12) 对非退化实 f、g 完全可能。

因此 R224/R228 的标准 T 方向正系数不能移植到 R227 的例外 $\mathcal G_b$，即便先证明该候选 quartic 是某个正确的领先部分，它在合法圆上也恰为零。既有三矩平滑补偿一旦准确恢复 (12)，(13) 就准确保持，不是只在近似圆上得到一个小余量。

本稿没有证明 R227 的完整 canonical ruling 偶部落在其三矩子空间。第二历史较低的 h 层、完整第三局部恢复、变化 profile 的链式项和能量的其余层都必须继续保留；(13) 不支付其中任何尚未核过的项。它只将例外端芽中这个明确候选主 quartic 的值准确确定下来。
