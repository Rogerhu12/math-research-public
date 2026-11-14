# 逐位熵偏转与增长周期模式的完整实际复右测试障碍

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。

**状态：以下结论均有完整证明。** 第一部分把原纯正锥的共同偏转改为
逐位 Jensen 估计，得到真正按次数指数下降的真空比。
第二部分用有限多模式的独立相位 Fourier 抽取，
处理任意复系数和任意模式间相消。
最后用多项式线性换元除去左因子，统一支付真实 carry。

具体地，令 $q=2^m$。对周期 $1\le r\le q/100$，
把尾指标按模 $r$ 的余类分成 $r$ 个慢尾和。
所有这些模式的复多项式右因子，只要总次数至多 $q^3$，
其真实主理想输出的归一化真空矩都趋零；
系数任意大、相位任意、相消任意。
同样处理各模式独立复参数、模长至多 $q^6$ 的指数右因子。
这包含真正不同坐标类别的相位，但不包含任意无周期的多坐标右因子。

全文保留实际左因子 $Q_m$ 和真实 $G\in A'$。
纯模型只用于已付误差的比较。
不以某个固定非湮灭态代替未知真正常态，不宣称完整理想范数已受控。

## 1. 模型和预算

固定 $S=S_N$ 或 $S=S_Y$，相应统一取 $X_j=N_j$ 或 $Y_j$。
令
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_{j\ge0}a_j<2,\qquad q=2^m,\quad m\ge1,
$$
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad
U_m=\sum_{j\ge m}a_jX_j,\qquad E_j=e_{10}^{(j)}.
\tag{1.1}
$$
原 Haar 尾真空为 $\Omega$，其态为 $\omega_m$。
R253 的真实相位乘积给
$$
P_m=I_{<m}\otimes Q_m\in S\mathcal A,\qquad Q_m\in\mathcal B_m,
$$
$$
\|Q_m-D_m^q\|\le e_m,\qquad
e_m=13a_\Sigma q(3a_\Sigma)^{q-1}
\exp\!\left(-\frac{770}{16}q^4\right).
\tag{1.2}
$$
以下统一使用确定的误差上界
$$
\zeta_m=4a_\Sigma e^{-770q^4}.
\tag{1.3}
$$
它同时控制 $\|U_m-D_m\|$，并控制任何一个子集尾和的实际/纯差。
其来源为
$\|N_j-E_j\|\le\eta_j$、$\|Y_j-E_j\|\le4\eta_j$、
$\eta_j\le e^{-770\,16^j}$。
每个实际子和范数不超过 $3a_\Sigma<6$。

对所有 $k\ge1$，
$$
h_{m,k}=\omega_m(D_m^k)
=k!2^{-k}e_k(a_j:j\ge m)>0.
\tag{1.4}
$$
特别 $h_{m,q}\ge(8eq)^{-q}$。
没有假定纯 $D_m$ 在 Haar 空间上无核。

置
$$
\mathcal H(t)=\frac12\bigl((1+t)\log(1+t)+(1-t)\log(1-t)\bigr),
\quad 0\le t<1,
\qquad a=\frac{\pi}{16}.
\tag{1.5}
$$
因 $\mathcal H(0)=\mathcal H'(0)=0$、
$\mathcal H''(t)=1/(1-t^2)\ge1$，有
$$
\mathcal H(t)\ge t^2/2.
\tag{1.6}
$$

## 2. 任意固定基数的单点入选下界

从任意删去有限集合 $B$ 后的尾指标中，
按正权 $a_A$ 选择 $k$ 元集合 $A$。
对 $j\notin B$，再剔除 $j$，置
$$
C_{B,j}=
\frac{e_{k-1}(a_\nu:\nu\ge m,\ \nu\notin B\cup\{j\})}
     {e_k(a_\nu:\nu\ge m,\ \nu\notin B\cup\{j\})}.
$$
在这个再剔除序列上重新选取 $k$ 个指标，
各入选概率不超过 $\min(1,C_{B,j}a_\nu)$。
由概率总和恰为 $k$，
$$
k\le\sum_{n=1}^{\infty}\min(1,C_{B,j}/n^2)
\le\int_0^\infty\min(1,C_{B,j}/x^2)\,dx
=2\sqrt{C_{B,j}}.
$$
故 $C_{B,j}\ge k^2/4$。
原条件分布中 $p_j=\mathbb P(j\in A)$ 的准确赔率为
$p_j/(1-p_j)=a_jC_{B,j}$，所以
$$
\boxed{
\mathbb P(j\in A)\ge
t_{j,k}:=\frac{k^2}{k^2+4(j+1)^2}
\quad(j\notin B).
}
\tag{2.1}
$$
对总集合 $A\cup B$，若 $j\in B$ 则已经入选，
所以同一个下界对所有 $j\ge m$ 都成立。
这里允许任意有限 $B$，不限制其大小或最大物理位。

## 3. 逐位 Jensen 偏转：纯正锥的指数加强

设
$$
W_0=\sum_{B\ {\rm finite}}c_BE_B,\qquad
c_B\ge0,\quad0<\sum_Bc_B<\infty.
\tag{3.1}
$$
令 $R_0=D_m^kW_0$。
它的算子范数级数及正真空矩都收敛，且
$\omega_m(R_0)>0$。
按每个单项式的正真空矩归一化，就得到总集合 $F=A\cup B$ 的概率分布：
条件于 $B$，$A$ 正是 §2 的 $k$ 元排除分布；
再按各 $B$ 的真空矩作正概率混合。
因此其全部单点概率仍至少为 $t_{j,k}$。

先只改有限个位 $J\subset[m,\infty)$。
在每个 $j\in J$ 取
$$
u_j=
\sqrt{\frac{1+t_{j,k}}2}\,e_0+
\sqrt{\frac{1-t_{j,k}}2}\,e_1,\qquad
v_j=
\sqrt{\frac{1-t_{j,k}}2}\,e_0+
\sqrt{\frac{1+t_{j,k}}2}\,e_1.
\tag{3.2}
$$
其他位保持 Haar 真空，故 $u,v$ 是原尾空间中的单位向量。
记
$$
b_j=1+t_{j,k},\qquad c_j=\sqrt{1-t_{j,k}^2}.
$$
局部准确有
$\langle E_ju_j,v_j\rangle=b_j/2$、
$\langle u_j,v_j\rangle=c_j$。
于是
$$
\frac{\langle R_0u,v\rangle}{\omega_m(R_0)}
=
\mathbb E\prod_{j\in J}
 c_j^{1-\mathbf1_F(j)}b_j^{\mathbf1_F(j)}.
\tag{3.3}
$$
所有量均为正实数。对指数函数用 Jensen，再用
$\mathbb P(j\in F)\ge t_{j,k}$ 及 $\log(b_j/c_j)>0$，得到
$$
\begin{aligned}
\log\frac{\|R_0\|}{\omega_m(R_0)}
&\ge\sum_{j\in J}
 \left(\log c_j+
       \mathbb P(j\in F)\log(b_j/c_j)\right)\\
&\ge\sum_{j\in J}\mathcal H(t_{j,k}).
\end{aligned}
\tag{3.4}
$$
这里只用了各单点概率；没有要求各入选事件独立，
也没有把 Jensen 的方向反过来。

令有限窗口 $J$ 增大，得到
$$
\boxed{
\frac{\omega_m(D_m^kW_0)}{\|D_m^kW_0\|}
\le e^{-\Lambda_{m,k}},\qquad
\Lambda_{m,k}:=\sum_{j\ge m}\mathcal H(t_{j,k}).
}
\tag{3.5}
$$
该和有限，因为远处 $\mathcal H(t)=O(t^2)$、$t_{j,k}=O(j^{-2})$。
(3.5) 是有限位估计的数值极限；
没有定义或使用一个无限偏转乘积向量。

由 (1.6) 和递减积分比较，
$$
\begin{aligned}
\Lambda_{m,k}
&\ge\frac12\sum_{n=m+1}^{\infty}
 \frac1{(1+(2n/k)^2)^2}\\
&\ge\frac{k}{4}\int_{2(m+1)/k}^{\infty}
 \frac{du}{(1+u^2)^2}
\ge \frac{\pi k}{16}-\frac{m+1}{2}.
\end{aligned}
\tag{3.6}
$$
使用了 $\int_0^\infty(1+u^2)^{-2}du=\pi/4$，以及被积函数不超过1。
因此
$$
\boxed{
\frac{\omega_m(D_m^kW_0)}{\|D_m^kW_0\|}
\le \exp\!\left(\frac{m+1}{2}-ak\right).
}
\tag{3.7}
$$
不限制 $W_0$ 的次数或最高位。

### 3.1 固定偏转的简短版本与角度核对

若只取 $J=\{m,\ldots,k-1\}$、$k\ge2m$，则每位入选概率至少 $1/5$。
可统一取
$$
u_j=\sqrt{3/5}\,e_0+\sqrt{2/5}\,e_1,\qquad v_j\text{ 交换两坐标}.
$$
这给选中比 $b=6/5$、未选中比 $c=\sqrt{24}/5$，
(3.4) 的每位贡献至少 $\mathcal H(1/5)\ge1/50$。
若写成旧参数 $u=\cos\theta\,e_0+\sin\theta\,e_1$，
这里是 $\cos(2\theta)=1/5$，不是 $\sin(2\theta)=1/5$。
于是还有较保守但简单的
$h_{m,k}/\|D_m^k\|\le e^{-(k-m)/50}$。

### 3.2 对已发表正锥、相位锥和指数族的影响

共同次数相位 $c_B=e^{i\theta|B|}d_B$、$d_B\ge0$，
仍由有限位统一相位酉和范数极限得到
$\|D_m^kW_\theta^0\|=\|D_m^kW_+^0\|$，
真空矩绝对值不超过正项和。
所以纯相位锥也可把旧保守率加强为 (3.7)。

对实际 $N_B$ 锥，R237 及复相位源稿的原支撑预算
$\limsup b_m/q^4<770/(16\log2)$、
原 $H_m$ 下界和全部实际误差保持不变。
按同一正真空矩归一化误差趋零，故充分大的 $m$ 有
$$
\frac{|\omega_m(Q_mW_\theta)|}{\|Q_mW_\theta\|}
\le2\exp\!\left(\frac{m+1}{2}-aq\right).
\tag{3.8}
$$
实际单项式仍是 $N_B$，不把相同预算免费移到 $Y_B$。

同样，全部 $|z|\le q^6$ 的实际 $Q_me^{zU_m}$，
用旧完整 Duhamel 误差除以 $h_{m,q}$，其误差远小于 (3.7)，
因而也满足 (3.8)。
旧较保守的正式结论继续有效；本节是严格加强。

单标量 Fourier 抽取也给较短的完整次数尾
$$
|\omega_m(V)|
\le\frac{e^{(m+1)/2-aq}}{1-e^{-a}}\|V\|,
\qquad
V\in\overline{D_m^q\mathbb C[D_m]}^{\|\cdot\|}.
\tag{3.9}
$$

## 4. 周期慢模式及移位平方权引理

给整数 $r\ge1$，将 $[m,\infty)$ 按模 $r$ 的余类分为
$I_1,\ldots,I_r$。令 $j_\nu=\min I_\nu$，并置
$$
D_\nu=\sum_{j\in I_\nu}a_jE_j,\qquad
U_\nu=\sum_{j\in I_\nu}a_jX_j\in\mathcal B_m.
\tag{4.1}
$$
于是 $\sum_\nu D_\nu=D_m$、$\sum_\nu U_\nu=U_m$，且各类不交给
$$
\sum_{\nu=1}^r\|U_\nu-D_\nu\|
\le4\sum_{j\ge m}a_j\eta_j\le\zeta_m.
$$
每个余类无限，且 $j_\nu$ 的集合恰为 $\{m,\ldots,m+r-1\}$。

写
$$
b_\nu=(j_\nu+1)/r>0.
$$
每类 $D_\nu$ 是常数 $r^{-2}$ 乘以权
$(n+b_\nu)^{-2}$、$n\ge0$ 的纯张量提升和。
这个常数在每个幂的真空比中消掉。

**引理 4.1。** 对任意 $b>0$ 的移位平方权和 $C_b$，
令 $\omega_b$ 是其 Haar 真空态，则对全部整数 $k\ge0$，
$$
\boxed{
\frac{\omega_b(C_b^k)}{\|C_b^k\|}
\le \exp(b/2+a-ak).
}
\tag{4.2}
$$
$k=0$ 时左边定义为1。

证明。对 $k\ge2$，§2 的计数在任何剔除序列上改为
$$
k\le\sum_{n=0}^{\infty}\min(1,C/(n+b)^2)
\le1+\sum_{n=1}^{\infty}\min(1,C/n^2)
\le1+2\sqrt C.
$$
因此 $C\ge(k-1)^2/4$。
把 §3 的逐位偏转用于
$$
t_n=\frac{(k-1)^2}{(k-1)^2+4(n+b)^2}
$$
并从 $b$ 开始作递减积分，得到
$$
\log\frac{\|C_b^k\|}{\omega_b(C_b^k)}
\ge a(k-1)-b/2.
$$
$k=0,1$ 时 (4.2) 的右边至少1，结论直接成立。
这特别处理 $r>m$ 时某些 $b_\nu<1$ 的情况，不漏掉该端点。

各模式作用在不交坐标上，所以对任意多重指数 $\alpha$，
有限张量范数乘法再取范数极限给
$$
\|D^\alpha\|=\prod_{\nu=1}^r\|D_\nu^{\alpha_\nu}\|,
\qquad
\omega_m(D^\alpha)=\prod_{\nu=1}^r\omega_m(D_\nu^{\alpha_\nu}),
\tag{4.3}
$$
其中 $D^\alpha=\prod_\nu D_\nu^{\alpha_\nu}$。
又
$$
\sum_{\nu=1}^r b_\nu=m+\frac{r+1}{2}.
$$
由 (4.2)--(4.3)，
$$
\boxed{
\frac{\omega_m(D^\alpha)}{\|D^\alpha\|}
\le
\exp\!\left(\frac m2+\frac{r+1}{4}+ar-a|\alpha|\right).
}
\tag{4.4}
$$

## 5. 独立模式相位与所有多重次数求和

令
$$
\mathscr A_{m,r}^0=\overline{\mathbb C[D_1,\ldots,D_r]}^{\|\cdot\|}.
$$
对 $\theta=(\theta_1,\ldots,\theta_r)\in\mathbb T^r$，
先在有限物理位上按所属余类分别作相位酉，
再取范数极限，得到连续等距自同构
$$
\alpha_\theta(F(D_1,\ldots,D_r))
=F(e^{i\theta_1}D_1,\ldots,e^{i\theta_r}D_r).
\tag{5.1}
$$
不假设这些无限位相位在 Haar 表示中可由一个酉实施。

多重 Bochner Fourier 系数投影是收缩。
因此若 $F(z)=\sum_\alpha c_\alpha z^\alpha$，
$$
\boxed{
|c_\alpha|\|D^\alpha\|\le\|F(D)\|.
}
\tag{5.2}
$$
设 $F$ 的全部非零单项式都有总次数至少 $q$。
由 (4.4)、(5.2)，
$$
|\omega_m(F(D))|
\le\Gamma_{m,q,r}\|F(D)\|,
\tag{5.3}
$$
其中可取
$$
\boxed{
\Gamma_{m,q,r}
=
e^{m/2+(r+1)/4+ar}
\binom{q+r-1}{r-1}
\frac{e^{-aq}}{(1-e^{-a})^r}.
}
\tag{5.4}
$$
这也传给这些多项式的算子范数闭包。

完整求和如下。总次数 $n$ 的多重指数数目为
$\binom{n+r-1}{r-1}$，且
$$
\binom{q+\ell+r-1}{r-1}
\le
\binom{q+r-1}{r-1}\binom{\ell+r-1}{r-1}.
\tag{5.5}
$$
逐个 $j=1,\ldots,r-1$ 比较
$j(q+\ell+j)\le(q+j)(\ell+j)$ 即得 (5.5)。
然后使用
$$
\sum_{\ell\ge0}\binom{\ell+r-1}{r-1}t^\ell=(1-t)^{-r},
\quad 0<t<1,
$$
得到 (5.4)。没有只保留最大的一个多重次数或一个相位模式。

如果 $r=o(q)$，由
$\log\binom{q+r}{r}\le r\log(e(q+r)/r)=o(q)$，
以及 $m=O(\log q)$，得到
$$
\Gamma_{m,q,r}\le e^{-aq+o(q)}\longrightarrow0.
\tag{5.6}
$$

### 5.1 一个明确的线性周期范围

更具体地，当 $1\le r\le q/100$ 时，
$$
\boxed{
\Gamma_{m,q,r}
\le \exp\!\left(\frac m2+\frac14-\frac q{10}\right).
}
\tag{5.7}
$$
以下给可检查的粗常数。
有 $3/16<a<1/5$，且
$1-e^{-a}\ge a/(1+a)>3/19$，所以
$-\log(1-e^{-a})<\log(19/3)<2$。
因此 (5.4) 中除组合数和 $e^{-aq}$ 外，
每个模式的对数成本小于 $1/4+1/5+2=49/20$。

又
$$
\log\binom{q+r-1}{r-1}
\le\log\binom{q+r}{r}
\le r\bigl(1+\log(1+q/r)\bigr)
\le(q/100)(1+\log101)<3q/50.
$$
中间函数随 $r>0$ 递增，可直接求导验证。
总的模式及组合成本小于
$49q/2000+3q/50=169q/2000$，
而 $a q>3q/16$。
由于 $3/16-169/2000=103/1000>1/10$，得到 (5.7)。

这个高次数结论只在指定的慢周期模式代数中成立。
它不适用于任意多变量 $E_j$ 的全部高次算子。
例如在任意远处的 $n$ 个位上取
$$
T_n=\frac2{n+2}\sum_{j\in B}E_j,\qquad |B|=n.
$$
物理分层给 $\|\sum_{j\in B}E_j\|\le(n+1)/2$，所以 $\|T_n\|\le1$。
又 $\|T_n\Omega-\Omega\|=\sqrt{n+4}/(n+2)$，故
$\|T_n^q\Omega-\Omega\|\le q\sqrt{n+4}/(n+2)$。
当 $n/q^2\to\infty$ 时，$T_n^q$ 的真空比趋于1，尽管其所有单项式次数都是 $q$。
这说明慢模式假设不能删除；后面的实际结论还明确保留左因子
$D_m^q$ 的主理想约束。

## 6. 多元输出系数不能直接冒充右因子系数

给任意非零复多项式
$p(z_1,\ldots,z_r)=\sum_\gamma b_\gamma z^\gamma$，总次数至多 $N$。
置
$$
F(z)=(z_1+\cdots+z_r)^q p(z),\quad
R_0=F(D)=D_m^q p(D_1,\ldots,D_r),
$$
$$
G=p(U_1,\ldots,U_r),\qquad R=Q_mG.
\tag{6.1}
$$
$R$ 是实际尾主理想输出。

模式幂 $D^\alpha\ne0$，因为各因子的正真空矩非零。
(5.2) 因而证明多项式在这些模式上的演算是忠实的。
普通多项式环无零因子，所以 $p\ne0$ 蕴含 $F\ne0$，从而 $R_0\ne0$。

令 $K=q+N$。对每个模式的 $k$ 次幂，
在其正基本对称多项式中只保留前 $k$ 个指标，得到
$$
\omega_m(D_\nu^k)
\ge k!2^{-k}(m+rk)^{-2k}.
\tag{6.2}
$$
因此对 $|\alpha|\le K$，
$$
\|D^\alpha\|\ge\omega_m(D^\alpha)
\ge [2(m+rK)^2]^{-K}.
\tag{6.3}
$$
右边只作统一下界，允许把各个 $k!\ge1$ 舍去。

写 $F(z)=\sum c_\alpha z^\alpha$。
由 (5.2)、(6.3) 及次数至多 $K$ 的单项式数目，
其系数 $\ell^1$ 范数满足
$$
\|F\|_{\mathrm{coef},1}
\le
\binom{K+r}{r}[2(m+rK)^2]^K\|R_0\|.
\tag{6.4}
$$

这里 $c_\alpha$ 是乘过左因子的系数，不是 $b_\gamma$。
为了合法恢复右因子，令 $x=z_1$、$w=(z_2,\ldots,z_r)$、
$s(w)=z_2+\cdots+z_r$，作线性换元 $x=y-s(w)$。
对任意次数至多 $K$ 的多项式，
该换元把系数 $\ell^1$ 范数放大至多 $r^K$。
而
$$
F(y-s(w),w)=y^q p(y-s(w),w).
$$
精确除以 $y^q$ 仅移动指数，不改变系数 $\ell^1$ 范数。
所得次数至多 $N$，再代回 $y=z_1+s(w)$ 至多放大 $r^N$。
故
$$
\boxed{
\|p\|_{\mathrm{coef},1}
\le r^{q+2N}\|F\|_{\mathrm{coef},1}.
}
\tag{6.5}
$$
$r=1$ 时同样成立，放大因子为1。
这一步是多元实际预算的必要除法，不能省掉。

## 7. 任意复系数的真实多元多项式提升

定义
$$
B_{m,q,r,N}
=
6^N r^{q+2N}
\binom{q+N+r}{r}
[2(m+r(q+N))^2]^{q+N}.
\tag{7.1}
$$
由 (6.4)--(6.5) 及每个 $\|U_\nu\|<6$，
$$
\|G\|\le B_{m,q,r,N}\|R_0\|.
\tag{7.2}
$$
各模式的实际差都不超过 (1.3) 的确定上界 $\zeta_m$。
对一个总次数 $d$ 的有序单项式，
逐因子望远镜给实际/纯差至多 $d6^{d-1}\zeta_m$。
这不要求实际与纯因子交叉交换，且已包含全部真实重复幂。
于是
$$
\|p(U)-p(D)\|
\le \zeta_m N B_{m,q,r,N}\|R_0\|.
\tag{7.3}
$$
最后
$$
\boxed{
\frac{\|Q_mp(U)-D_m^qp(D)\|}{\|R_0\|}
\le
\eta_{m,r,N}:=
B_{m,q,r,N}(e_m+a_\Sigma^q\zeta_m N).
}
\tag{7.4}
$$

**定理 7.1。** 一致于
$$
1\le r\le q/100,\qquad 0\le N\le q^3,
$$
以及每个次数至多 $N$ 的非零复多项式 $p$，
充分大的 $m$ 有 $Q_mp(U)\ne0$，且
$$
\boxed{
\frac{|\omega_m(Q_mp(U))|}{\|Q_mp(U)\|}
\le
\frac{\Gamma_{m,q,r}+\eta_{m,r,N}}{1-\eta_{m,r,N}}
\le
2\exp\!\left(\frac m2+\frac14-\frac q{10}\right).
}
\tag{7.5}
$$

证明。在指定范围内，
$$
\log B_{m,q,r,N}=O(q^3\log q)
$$
且常数不依赖模式数、系数、相位或相消。
所以
$$
\eta_{m,r,N}
\le
\exp\!\left(-\frac{770}{16}q^4+O(q^3\log q)\right)\longrightarrow0
$$
一致成立。
(7.4) 给实际范数至少 $(1-\eta)\|R_0\|>0$，
纯输出的全部次数至少 $q$，故 (5.3) 给其真空矩至多
$\Gamma_{m,q,r}\|R_0\|$。
这证明 (7.5) 的第一个式子。
误差比 (5.7) 还小，得到第二个式子。

同时输出归一化为1后，
$$
\boxed{
\frac{\|p(U)\|}{\|Q_mp(U)\|}
\le\frac{B_{m,q,r,N}}{1-\eta_{m,r,N}}
=\exp(O(q^3\log q)).
}
\tag{7.6}
$$
这是真实右因子的自动范数预算，不是先假定右因子系数受控。
任意巨大复系数均由其自身纯输出范数和 (6.5) 控制。

## 8. 独立周期相位的全部指数参数

给任意 $z_1,\ldots,z_r\in\mathbb C$，
$$
\max_\nu|z_\nu|\le q^6,
$$
令
$$
V=\sum_{\nu=1}^r z_\nu U_\nu,\quad
V_0=\sum_{\nu=1}^r z_\nu D_\nu,\quad
G=e^V,\quad R=Q_mG,\quad R_0=D_m^q e^{V_0}.
\tag{8.1}
$$
$G\in\mathcal B_m\subset A'$ 精确成立。

令 $R_z=\max_\nu|z_\nu|$。
R218 任意系数相位的半群上界，配合有限模式最大模原理及范数极限，
给
$$
\|e^{tV}\|\le e^{16\sqrt{tR_z}},\qquad
\|e^{tV_0}\|\le e^{\pi\sqrt{tR_z}},
\quad 0\le t\le1.
$$
各位系数的模不超过 $R_z a_j$；
模较小的情形由多变量最大模原理得到，低于 $m$ 的系数置零也同样处理。
又 $\|V-V_0\|\le R_z\zeta_m$。
Duhamel 于是给
$$
\|e^V-e^{V_0}\|\le R_z\zeta_m e^{17\sqrt{R_z}},
$$
$$
\|R-R_0\|\le
\Delta_m^*:=e_m e^{16q^3}
+a_\Sigma^q q^6\zeta_m e^{17q^3}.
\tag{8.2}
$$

$R_0$ 属于 §5 高次数类。
此外对所有模式同时作同一全局相位 Fourier 抽取，
其总次数 $q$ 的齐次项准确为 $D_m^q$，因为指数的常数项为1。
收缩系数投影给
$$
\boxed{\|R_0\|\ge\|D_m^q\|\ge h_{m,q}.}
\tag{8.3}
$$
这不依赖各模式的相位，也不依赖可能完全相消的真空矩。

由 $\Delta_m^*/h_{m,q}
=\exp(-(770/16)q^4+16q^3+O(q\log q))$，
(5.3)、(8.2)--(8.3) 与定理7.1相同的比较得到：

**定理 8.1。** 一致于 $1\le r\le q/100$ 及所有
$\max_\nu|z_\nu|\le q^6$，充分大的 $m$ 有 $Q_me^{\sum z_\nu U_\nu}\ne0$，且
$$
\boxed{
\frac{|\omega_m(Q_me^{\sum_\nu z_\nu U_\nu})|}
     {\|Q_me^{\sum_\nu z_\nu U_\nu}\|}
\le2\exp\!\left(\frac m2+\frac14-\frac q{10}\right).
}
\tag{8.4}
$$
这里允许不同余类的参数有完全不同的相位和模长。
真实右因子还满足 $\|G\|\le e^{16q^3}$。

对该参数多圆盘上的有限复测度混合，同一纯高次数界仍成立，
实际误差至多 $\Delta_m^*\|\sigma\|_{\rm TV}$。
所以只要
$\Delta_m^*\|\sigma\|_{\rm TV}/\|Q_mG_\sigma\|\to0$，
其归一化真空比也趋零。
这是具体表示的相对误差条件，不是一般 $A'$ 元素的性质。

## 9. 真湮灭接口与剩余范围

若 $\rho\ge0$ 真正湮灭 $S\mathcal A$，
本稿每个 $G$ 都是实际 $\mathcal B_m\subset A'$ 中的有界右因子，
所以
$$
\operatorname{Tr}\bigl(\rho(I_{<m}\otimes Q_mG)\bigr)=0
$$
精确成立。涉及一般 $A'$ 的延拓可用 R88 有界强逼近和正常迹连续性；
本稿的多项式与指数本身已经在 $\mathcal A$ 中。

上述一致界说明，使用这些周期慢模式，即使允许任意复系数、
数量增长到 $q/100$ 的独立模式、以及可支付的高次数右多项式，
仍不能提供 R253 所需的非消失真空比。
它不证明真正常态存在或不存在。

没有证明任意无周期的系数模式可以用上述小周期数在相对输出范数中逼近。
模式数超过所付范围、任意多坐标算子和非 UHF 右因子均不被此定理覆盖。
尤其没有把“次数至少 $q$”本身当成任意纯交换代数上的障碍；
纯论证使用了每个模式完整的平方衰减尾权。
实际多项式论证始终保留
$(\sum_\nu D_\nu)^q p(D)$ 的左理想身份，并付清恢复 $p$ 的线性换元成本。

## 已证依赖

- R253/R235：真实 $Q_m$、$e_m$、$h_{m,q}$ 和全部真实右测试。
- R237：纯正锥按正真空矩的条件/混合描述；
  本稿重新给出所需单点概率下界，并以逐位 Jensen 加强偏转。
- 全标量 Fourier 源稿：有限相位酉后范数极限的框架；
  本稿独立支付多重次数求和及多元右因子系数除法。
- R215/R218：实际任意相位慢和的 $e^{16\sqrt{|z|}}$ 上界。
- 全部新增结论已在原 Haar 全空间上逐项支付，不把纯核、未知限制的范数
  或相位旋转的空间实施性当作免费输入。
