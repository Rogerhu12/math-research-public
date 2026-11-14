# 原 $J$ 反射的三维非算术 CM 块

日期：2026-11-14。状态：完整来源与谱界已证明；不登记新的主结果编号。

本 note 保留 R532/R538 中实际 $J$ 反射的来源，说明它不能仅用原三条 $S,H_3,H_5$ 的中央行取回。它没有给新的中央零，也不改变 R538 尚未支付的 $A_5$ 深度和 $J+K$ 近相消补域。

## 1. 同一原六输入

沿用 $E_b:y^2=x^3+b$、$\delta^2=-3$、$\omega=(-1+\delta)/2$、$\gamma=(5+\delta)/2$，以及 R532 的整个正交 frame。为避免与形式变量混淆，下文 $x(z),y(z)$ 表示 Weierstrass 函数，独立的第四个 sigma 输入写作 $\xi_4$。

原第一输出及 $J$ 反射后的输出为
$$
Y=\alpha J+2A_5,\qquad
Y^-=-\alpha J+2A_5,\qquad
\alpha=-2+\frac43\delta .
\tag{1}
$$
反射完整保 $A_5,K,E,B_2,C_{30}$，不是把 $Y$ 固定的伴随操作。原六输入次序为 $(\xi_1,\xi_2,\xi_3,\xi_4,c,d_0)$。准确有
$$
\delta Y^-=
(1+2\delta)\xi_1-6\xi_2+\omega^2\xi_3
-\delta\bar\gamma\,\xi_4-(4+\delta)c+2\delta d_0 .
\tag{2}
$$
六系数的范数依次为 $13,36,1,21,19,12$，总和为 $102$。
因此其真实边际是
$$
F^-(z)=-\frac1{84}
 \sigma((1+2\delta)z)\sigma(-6z)\sigma(\omega^2z)
 \sigma(-\delta\bar\gamma z)\sigma(-(4+\delta)z)\sigma(2\delta z)
 \in\mathcal S_{102}.
\tag{3}
$$
这里 $F^-(z)=Y^-_*\rho_0(\delta z)$。全部 sigma 的实际奇 theta 特征相乘得到 (3) 的标准偶线丛；没有删去任何 flat twist。

## 2. 全函数多项式

写 $X=x^3$，并置
$$
\begin{aligned}
P_{13}(X)&=X^2+(2+6\delta)bX+\frac{40+24\delta}{13}b^2,\\
P_{19}(X)&=X^3+(-24+12\delta)bX^2
                 +(-24+24\delta)b^2X-\frac{224+96\delta}{19}b^3,\\
P_{21}(X)&=X^3+\frac{138+162\delta}{7}bX^2+48b^2X+64b^3.
\end{aligned}
\tag{4}
$$
设 $a_{13}=1+2\delta,\ a_{19}=-(4+\delta),\
a_{21}=-\delta\bar\gamma$。完整同源公式是
$$
\sigma(a_{13}z)=a_{13}\sigma^{13}P_{13}(X),\quad
\sigma(a_{19}z)=a_{19}\sigma^{19}P_{19}(X),\quad
\sigma(a_{21}z)=a_{21}\sigma^{21}xP_{21}(X).
\tag{5}
$$
这些身份的证明先使用完整线丛和 $\mu_6$ 型：相关整空间分别正是
$\sigma^{13}K[X]_{\le2}$、$\sigma^{19}K[X]_{\le3}$、
$\sigma^{21}xK[X]_{\le3}$。随后比较至 $z^{13}$ 或 $z^{19}$ 的三或四个系数，完整决定截面。不是从有限采样推测恒等式。
规范 $\sigma(z)=z+\cdots$ 确定式 (5) 的常数。

R532 的同一个 $G_{16}=\sigma(2z)\sigma(2\delta z)/(4\delta)$ 给
$$
G_{16}(\delta z)=
-3\sigma^{48}x^2
(X+4b)(X+b)(X-8b)^2
(X^3+228bX^2+48b^2X+64b^3).
\tag{6}
$$
于是
$$
\boxed{
F^-=\frac{\delta\omega^2a_{13}a_{21}a_{19}}7\,
\sigma^{102}X(X+4b)(X+b)(X-8b)^2
(X^3+228bX^2+48b^2X+64b^3)
P_{13}P_{21}P_{19}.}
\tag{7}
$$
其多项式次数是 $16$，质量为零，并且
$$
[z^6]F^-=\frac{-93+48\delta}{7}\ne0 .
\tag{8}
$$
所有多项式按 $(X,b)$ 齐次，故 $b=1$ 的准确证书唯一恢复本题 $b=17$；并未更换实际周期框。

## 3. 既付整个十八维 CM 算子的精确作用

使用 R464 的真实 $N_7=\mathscr M_\gamma/\gamma$，以及其整个
$\mathcal V_{102}=\sigma^{102}K[X]_{\le17}$ 的十八个真实七次纤维矩阵。
式 (7) 的完整十八坐标满足
$$
\boxed{N_7^3F^-=\omega F^- .}
\tag{9}
$$
向量 $F^-,N_7F^-,N_7^2F^-$ 线性无关，所以它的完整循环空间恰三维，最小多项式为 $t^3-\omega$。特别
$$
N_7^9F^-=F^-,\qquad K_{102}F^-=-F^- .
\tag{10}
$$
最后一步使用 R464 已支付绝对相位的 whole 恒等式
$K_{102}=-N_7^9$，不是只从同像作用猜标量。

另一方面，原三条算术拉回源为
$$
N_7S(\delta z)=-S(\delta z),\quad
N_7H_3(\delta z)=-\omega H_3(\delta z),\quad
N_7H_5(\delta z)=-\omega^2H_5(\delta z).
$$
它们的 $N_7^3$ 特征全为 $-1$。故
$$
\boxed{\Pi_{\rm ar}F^-=0,\qquad
\Pi_{\rm ar}=\frac{I+N_7^6+N_7^{12}}3 .}
\tag{11}
$$
这三个投影分别严格为零；不是用它们的质量作判据。来源 (3) 本身非零，不能因 (11) 删除它的整个中央或其真实混合域。

随附脚本读取 R464 已发布的完整矩阵 JSON，重新构造 (4)--(7)，核全部十八坐标的 (9)、原算术投影、循环秩和 $N_7^{18}$ 返回。脚本不重跑原七次纤维，也不使用浮点或模素数拟合。

## 4. 本 note 的适用边界

原 $J$ 核的深度运输仍使用 R532/R538 已证明的完整物理逆像；$J$ 反射并不因此成为来源不变的几何操作。式 (11) 只表明这条候选来源不在原三条算术行内，未排除其他真实来源身份，也未推出任何新曲线的秩或 Sha 结论。

本题的无穷多个 $p$ 目标仍未完成。
