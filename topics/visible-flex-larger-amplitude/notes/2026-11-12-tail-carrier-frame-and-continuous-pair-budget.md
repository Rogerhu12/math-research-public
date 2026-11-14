# 同一真实径向背景的空间框架、位置与连续点对误差预算

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12

**状态：完整条件工具与候选发展约定；本记录没有新的数值结果。**
本工具把已经保存的完整高度两 jet、mean 差和真实正域连接到可核算的
空间位置及单位法向误差。它同时保留右端的水平平移、框架转角和 mean
高度三种偏移。端高度两 jet 相同不等于两端空间边界已同时重合。

相关：
[完整 mean 差](2026-11-12-tail-two-complete-mean-roots-rational-difference.md)、
[完整 mean 径向差](2026-11-12-tail-two-complete-mean-radial-difference.md)、
[R30](../results/R30-source-cut-to-cartesian-boundary-traces.md)。
以下每个全角界均指真实整个角圆周；任何额外形变参数也必须包含在原输入域内。

## 1. 从真实高度得到两条框架系数

设同一真实度量为 $g=E(r)\,dr^2+r^2d\theta^2$，
$E=1+w^2$，$r,w>0$。对一个高度 $h$ 写

$$
 k=h_r,\quad u=h_\theta,\quad
 p=\frac{k}{\sqrt E},\quad q=\frac{u}{r},\quad
 s=\sqrt{1-q^2},\quad \nu=\sqrt{1-p^2-q^2}.
 \tag{F.1}
$$

假设 $s,\nu>0$，取正水平 Jacobian 的定向。若 $X$ 是这个高度的实际
等距浸入，水平单位切向为 $t=(\cos\gamma,\sin\gamma)$，
左法向为 $n=(-\sin\gamma,\cos\gamma)$，则

$$
 X_{\theta,xy}=a\,t,\qquad
 X_{r,xy}=b\,t-c\,n,
$$

$$
 a=rs,\qquad b=-\frac{\sqrt E\,pq}{s},\qquad
 c=\frac{\sqrt E\,\nu}{s}.
 \tag{F.2}
$$

第一式来自 $|X_\theta|^2=r^2$；混合内积及径向长度分别确定 $b,c$。
这里 $c>0$，$\det(X_{r,xy},X_{\theta,xy})=ac>0$。

由于 $u_r=k_\theta$，混合导数相等给
$a_r=b_\theta+c\gamma_\theta$、
$a\gamma_r=b\gamma_\theta-c_\theta$。
逐项化简得到

$$
 \boxed{
 \gamma_\theta=\frac{1}{\sqrt E\,\nu}
       +\frac{p q_\theta}{s^2\nu},\qquad
 \gamma_r=\frac{p(\sqrt E\,p_\theta-q)}{r s^2\nu}.
 }
 \tag{F.3}
$$

第二个等式中的 $h_{\theta\theta}$ 项恰好相消；
它只需实际 $h_r,h_\theta,h_{r\theta}$，没有隐藏第三径向导数。
例如用 $a^2=r^2-u^2$ 展开，其分子为
$rkk_\theta-ku$，分母为 $\sqrt E\,\nu\,a^2$。
背景轴对称状态给 $\gamma_\theta=1,\gamma_r=0$，与圆周框架一致。

(F.3) 也是正定水平度量 $g-dh^2$ 的有向连接系数。
一般候选即使没有满足 Darboux，也可以定义这两个系数；
这时不能假设 $\partial_r\gamma_\theta=\partial_\theta\gamma_r$。

## 2. 非解候选也可采用的明确发展约定

固定左端 $r_L$、角基点 $\theta_0$、一个水平位置 $x_L$ 和一个框架角
$\gamma_L$。先沿 $\theta=\theta_0$ 定义

$$
 \gamma_0(r)=\gamma_L+\int_{r_L}^r\gamma_r(v,\theta_0)\,dv,
$$

$$
 x_0(r)=x_L+\int_{r_L}^r
 \bigl[b(v,\theta_0)t(\gamma_0(v))-c(v,\theta_0)n(\gamma_0(v))\bigr]\,dv.
 \tag{F.4}
$$

再沿每个角圆周定义

$$
 \widehat\gamma(r,\theta)=\gamma_0(r)
      +\int_{\theta_0}^{\theta}\gamma_\theta(r,\eta)\,d\eta,
$$

$$
 \widehat X_{xy}(r,\theta)=x_0(r)
      +\int_{\theta_0}^{\theta}a(r,\eta)t(\widehat\gamma(r,\eta))\,d\eta,
 \qquad \widehat X_z=h(r,\theta).
 \tag{F.5}
$$

这明确规定同一条径向后角向路径，没有偷偷采用任意路径无关性。
若高度是真正 Darboux 解且已付正确 period，(F.4)--(F.5) 就是相应
实际发展；若只是候选，$\widehat X$ 是确定的参考映射，不宣称其等距。

当前非均值 modes 全为偶数，所以高度及 (F.3) 的系数为 $\pi$ 周期。
完整 mean 根准确给 $\int_0^{2\pi}\gamma_\theta\,d\theta=2\pi$；
于是每半圈的积分恰为 $\pi$，从而
$t(\theta+\pi)=-t(\theta)$、$a(\theta+\pi)=a(\theta)$。
这证明 (F.5) 的水平曲线位置准确闭合，而非只有小数值 holonomy。
比较两组这种发展时，可以使用角长不超过 $\pi$ 的同一圆周路径。
若没有偶数模对称，位置闭合必须单独支付，不能仅由总转角推出。

再定义单位参考向量

$$
 \widehat N
 =-\frac{\nu q}{s}\,t(\widehat\gamma)
    +\frac{p}{s}\,n(\widehat\gamma)+\nu\,e_z.
 \tag{F.6}
$$

由 $p^2+q^2+\nu^2=1$ 可直接核 $\lvert\widehat N\rvert=1$。
对实际等距发展它正是向上单位法向。
对非解候选它只是明确的单位参考向量；
本工具从不把它自动当成参考映射的实际法向。

## 3. 同位置两组实际高度的显式系数差

以下 $A,B$ 两组高度采用同一 $r,E$、同一路径和同一左锚点。
可允许一组为实际解、另一组为候选；在这种情况下，以下预算直接比较
实际浸入与明确参考映射/向量，无需先证明候选自己等距。

在一个真实整叶上，设

$$
\begin{gathered}
 |p_i|\le p_*,\quad |q_i|\le q_*,\quad
 |p_{\theta,i}|\le P_*,\quad |q_{\theta,i}|\le Q_*,\\
 s_i\ge s_*>0,\quad \nu_i\ge\nu_*>0,\quad
 r\ge r_*>0,\quad \sqrt E\le e_*,\\
 |\delta p|\le e_p,\quad|\delta q|\le e_q,\quad
 |\delta p_\theta|\le e_{p\theta},\quad
 |\delta q_\theta|\le e_{q\theta}.
\end{gathered}
\tag{F.7}
$$

这些为同一真实位置的差，不是两个采样点之间的值差。
因 $p_i^2+q_i^2<1$，可以安全地与各自的平凡上界 $1$ 取较小者。
记

$$
 d_\nu=\frac{p_*e_p+q_*e_q}{\nu_*},\qquad
 d_{\nu^{-1}}=\frac{p_*e_p+q_*e_q}{\nu_*^3},\qquad
 d_s=\frac{q_*e_q}{s_*}.
$$

有
$|\delta\nu|\le d_\nu$、
$|\delta(\nu^{-1})|\le d_{\nu^{-1}}$、
$|\delta s|\le d_s$、
$|\delta(s^{-2})|\le2q_*e_q/s_*^4$。
对 (F.3) 准确相减得到

$$
\begin{aligned}
 G_\theta={}&d_{\nu^{-1}}
 +\frac{e_p Q_*+p_*e_{q\theta}}{s_*^2\nu_*}\\
 &+p_*Q_*\left(\frac{2q_*e_q}{s_*^4\nu_*}
                 +\frac{d_{\nu^{-1}}}{s_*^2}\right),
\\
 U_*={}&e_*P_*+q_*,\qquad e_U=e_*e_{p\theta}+e_q,\\
 G_r={}&\frac{e_pU_*+p_*e_U}{r_*s_*^2\nu_*}\\
 &+\frac{p_*U_*}{r_*}
 \left(\frac{2q_*e_q}{s_*^4\nu_*}
                  +\frac{d_{\nu^{-1}}}{s_*^2}\right).
\end{aligned}
\tag{F.8}
$$

即 $|\delta\gamma_\theta|\le G_\theta$、
$|\delta\gamma_r|\le G_r$。
第一项只用了 $E^{-1/2}\le1$；共同 $E$ 没有另收背景差。

对 (F.2) 的径向两个系数，可取

$$
\begin{aligned}
 B_\Delta&=e_*\left[
 \frac{e_pq_*+p_*e_q}{s_*}+\frac{p_*q_*^2e_q}{s_*^3}\right],\\
 C_\Delta&=e_*\left[
 \frac{d_\nu}{s_*}+\frac{q_*e_q}{s_*^3}\right].
\end{aligned}
\tag{F.9}
$$

(F.6) 的三个固定框架分量差之和不超过

$$
 N_\Delta=d_\nu+
 \frac{q_*d_\nu+e_q}{s_*}+\frac{q_*^2e_q}{s_*^3}
 +\frac{e_p}{s_*}+\frac{p_*q_*e_q}{s_*^3}.
 \tag{F.10}
$$

以上全是有限有理正表达式。实际输入可取
$s_*=\min(1,A_{\min})$、
$\nu_*=\min(1,D_{\min}/E_{\max})$，
因为 $\sqrt A\ge A$ 对 $0<A\le1$ 成立，
且 $\nu^2=D/E$。取 $e_*=1+w_{\max}^2/2$，
安全包围 $\sqrt{1+w^2}$。
这些选择稍粗，但无需新根式积分或新的源评价。

## 4. 用已有真实叶宽给全连续位置和法向预算

令 $\mathcal A(r)$ 为到 $r$ 的基线框架差上界，
$\mathcal B(r)$ 为基线水平位置差上界。若左锚点一致，初值均为零。
对每个按真实 $r$ 排序的整叶 $I$，用已付宽度 $\Delta r_I^+$ 更新

$$
 \mathcal A_I^+=\mathcal A_I^-+\Delta r_I^+G_{r,I},
$$

$$
 \mathcal B_I^+=\mathcal B_I^-+
 \Delta r_I^+\left[
 B_{\Delta,I}+C_{\Delta,I}
 +e_{*,I}\min(2,\mathcal A_I^+)\right].
 \tag{F.11}
$$

这是全叶上的正累计；没有用中点代替积分。
径向参考向量 $b\,t-c\,n$ 的长度不超过 $\sqrt E$，
故转动部分正是最后一项。单位向量的转动差同时不超过角差与 $2$。

取有理圆周上界 $\pi_+=22/7$，对同一整叶所有角度置

$$
 \Theta_I=\mathcal A_I^++\pi_+G_{\theta,I},\qquad
 \rho_I=\min(2,\Theta_I).
$$

若 $r\le r_I^+$，则

$$
 |\delta\widehat X_{xy}|
 \le \mathcal B_I^+
       +\pi_+r_I^+\bigl(d_{s,I}+\rho_I\bigr),\qquad
 |\delta\widehat N|\le\min(2,N_{\Delta,I}+\rho_I).
 \tag{F.12}
$$

完整空间位置还必须加入同一 mean 账本给的 $|\delta h|$。
可保存水平/竖直两项平方和，或使用其和作为安全的 Euclidean 上界。
这些量覆盖整个连续叶与整个角圆周，不是采样网格上的最大值。

PA/CF 当前保存全部 cosine $H,\overline K,\overline K_r$。
由完整 mean 差可取

$$
 e_p\le w_{\max}\bigl(|\delta c|_{\rm ub}
                         +\|\delta\overline K\|_\infty\bigr),\qquad
 e_q\le \|\partial_\theta\delta H\|_\infty/r_*,
$$

$$
 e_{p\theta}\le w_{\max}\|\delta\overline K_\theta\|_\infty,\qquad
 e_{q\theta}\le\|\partial_{\theta\theta}\delta H\|_\infty/r_*.
 \tag{F.13}
$$

其幅度上界按同一完整 Fourier 和计算；没有丢 mean 或角导数乘子。
(F.11) 只用原 PM 真宽度，完整 mean 高度只用原
$I_{00}+I_{01}=\int w\,dr$。两者不能混作同一个积分。

## 5. 右端误差不能重置

若两个候选的非均值物理两 jet 在右端准确相同，
同一完整根给 $c_A=c_B,c_{A,r}=c_{B,r}$，于是右端的
$p,q,p_\theta,q_\theta$ 与 (F.3) 准确相同。
但从左端累计的基线框架差和水平位置差仍可非零。
完整 mean 高度也有唯一的累计偏移。

若之后的高度导数和真实背景完全相同，则后续两种发展满足同一个
固定水平转动和平移，另加同一个竖直 mean 常数。
设右锚点位置差为 $\varepsilon_R$、框架角差为 $\alpha_R$；
对后续参考点距右锚点的水平距离 $L$，有

$$
 |\delta\widehat X_{xy}|
 \le\varepsilon_R+\min(2,|\alpha_R|)\,L .
 \tag{F.14}
$$

这是沿后续未改区域继续传播的预算，不允许在右端独立重新配准以掩盖它。
要保持实际 held 集合的位置，需由真正的空间接缝条件支付这些偏移，
或在同一个全局刚体选择下把它们纳入完整几何误差。

## 6. 连续点对的严格正常球门

本节不要求参考映射本身等距，也不要求参考单位向量是它的真实法向。
它只要求其与实际浸入的误差已经付清。
对任意一对参数点 $p,q$，设真实点/法向为 $X,N$，
参考值为 $X_0,N_0$，且

$$
 |X(p)-X_0(p)|\le\varepsilon_p,\quad
 |X(q)-X_0(q)|\le\varepsilon_q,\quad
 |N(p)-N_0(p)|\le\eta_p,\quad |N(p)|=1.
$$

设同一连续点对盒上已付

$$
 |X_0(q)-X_0(p)|\ge\ell_0,\qquad
 |X_0(q)-X_0(p)|\le u_0,\qquad
 |N_0(p)\cdot(X_0(q)-X_0(p))|\le b_0.
$$

令 $\varepsilon=\varepsilon_p+\varepsilon_q$。若

$$
 \ell_0>\varepsilon,\qquad
 (\ell_0-\varepsilon)^2
 \ge2\tau\bigl(b_0+\eta_pu_0+\varepsilon\bigr),
 \tag{F.15}
$$

则两实际点不同，且

$$
 |N(p)\cdot(X(q)-X(p))|
 \le\frac{|X(q)-X(p)|^2}{2\tau}.
 \tag{F.16}
$$

证明：实际弦长至少 $\ell_0-\varepsilon$；
实际法向弦积至多 $b_0+\eta_pu_0+\varepsilon$。
误差弦项使用实际单位法向，因此不多收一个 $(1+\eta_p)$ 因子。

若只保存平方下界 $S\le|X_0(q)-X_0(p)|^2$，可完全不用平方根。
记 $B=2\tau(b_0+\eta_pu_0+\varepsilon)$、
$T=S+\varepsilon^2-B$。以下全有理条件等价于使用
$\ell_0=\sqrt S$ 的 (F.15)：

$$
 S>\varepsilon^2,\qquad T\ge0,\qquad T^2\ge4S\varepsilon^2 .
 \tag{F.17}
$$

第二个条件不可省；否则平方会允许错误符号。
对每个连续盒必须使用全盒 $S,u_0,b_0$，不能仅代入中心点或角采样值。

设定义域为紧致、无边界的二维流形。若实际 $C^2$ 浸入的全部不同参数
点对都由严格局部图门和 (F.15) 两类覆盖，且局部图门对相应点对同时保证
点不同及 (F.16)，则由弦长正性可得全局单射；实际面是嵌入。
这里只给局部图存在性或曲率样本不够。
若所有这些对还都满足 (F.16)，则其 reach 至少 $\tau$。
确实，对 $|t|<\tau$，

$$
 |X(p)+tN(p)-X(q)|^2-t^2
 \ge |X(q)-X(p)|^2(1-|t|/\tau)>0 .
$$

任意距离小于 $\tau$ 的外点在紧致面上有最近点；极值正交性使它位于该点
法线，所以上式给最近点唯一。局部近对覆盖必须另付；
固定的绝对误差盒不可能自动处理趋于对角线的所有点对。

## 7. 当前数据能付和不能付的范围

现有 PA/CF 全角实域、完整 mean 及实际两 jet，足以在它们正式成功后
用纯有理流消费器支付 (F.7)--(F.13) 的两种明确参考发展差。
当前只有候选时，这不是实际真解误差。以后若外 Green/Schur 给出同一
真解与某一候选的连续两 jet 差，可直接复用同一公式得到实际空间误差。

(F.15)--(F.17) 还需要同一参考映射的连续位置/单位向量点对盒和近对覆盖。
完整形变时间域、held 集合、直径与位移下界都需保持共同全局放置。
这里没有代替外 $0..9$ 存在性、全频中窗、内外准确接合或整体几何验收。
