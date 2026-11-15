# 真实固定测试的整条正交 jet 旗保持相邻交换行小量

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 结论与范围

本文接[实际固定测试的完整相邻交换行及同顶部双线性式](R271-appendix-actual-fixed-test-adjacent-swap-row-and-same-top-bilinear-pairing.md)。保留原连续尾
$$
D=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad x\ge1,
$$
以及同一真实物理投影来源
$$
u_f=(P_{V_Q}-P_{K_Q})f,
$$
其中 $f$ 在 $x$ 以后为真空。也可以保前一稿所列的 strong-head / far-tail 版本；此时 $x=m+R$，交换对全部位于远尾，合并头 $C$ 不变。

令
$$
\Pi_r=P_{\ker D^r},\qquad \Pi_0=0,\qquad
F_r=\Pi_r-\Pi_{r-1}\quad(r\ge1).
$$
这里 $F_r$ 是实际物理正交 jet 条带，绝不是顺次 MP 定义的非正交幂等算子。令 $P_i^-=(I-U_i)/2$，$U_i$ 交换物理位 $i,i+1$。本文证明
$$
\boxed{
 \sum_{n\in I}\sum_{r\ge1}\sum_{i\ge x}
 \|P_i^-F_r u_{f,n}\|^2
 \le \frac{49}{x}\|f\|^2
}
\tag{0.1}
$$
对任意输出远孔层集合 $I$ 成立。该常数不含 $Q$、$h$、条带数或物理维数。所有和都是真实正项和；无需将逐层界再乘一个 $Q$。

关键是：单对变形的生成元只把真实旗提高一阶，因此在整条正交旗内严格三对角。这比一般任意旗的三角截断估计更强，不损失 $\log Q$。

本文不把 (0.1) 外推为
$$
\left\|\sum_j D^\dagger\cdots D^\dagger D^j u_{f,n}\right\|
$$
的上界；非正交顺次返回仍未控制，也没有证明 $N=M$。

## 1. 单对变形与完整核旗

固定 $i\ge x$，写
$$
t=i+1,\qquad
\theta_i=\log\frac{t+1}{t},\qquad
a_i=\frac1{t(t+1)},\qquad
H_i=n_{i+1}-n_i.
$$
于是 $H_i=H_i^*$、$\|H_i\|=1$，且
$$
S(\tau)=e^{\tau H_i}
$$
在该二位的基 $00,10,01,11$ 上为
$$
\operatorname{diag}(1,e^{-\tau},e^\tau,1).
$$
将这对权先同时取为 $a_i$，其余权保持原值，记得到的下降算子为 $D_0$。令
$$
D_\tau=S(\tau)D_0S(\tau)^{-1}.
$$
则
$$
D_{\theta_i}=D,\qquad
\ker D_\tau^r=S(\tau)\ker D_0^r
\tag{1.1}
$$
对全部 $r$ 精确成立。每个算子有界，每个核闭；这里只用一对有界可逆变形，没有无限对角相似。

记
$$
\Pi_r(\tau)=P_{\ker D_\tau^r}.
$$
因 (1.1)，这些正交投影关于 $\tau$ 在算子范数中连续可微，并满足
$$
\Pi_r'=(I-\Pi_r)H_i\Pi_r+\Pi_rH_i(I-\Pi_r).
\tag{1.2}
$$
例如将固定核等距嵌入记为 $J$，可直接从
$$
\Pi_r(\tau)=
S(\tau)J\bigl(J^*S(\tau)^2J\bigr)^{-1}J^*S(\tau)
$$
微分得 (1.2)。中间压缩严格正且其逆有界；本式没有交换完整逆与核压缩。

## 2. 生成元对真旗只有一阶跃迁

因为各 $E_j$ 相互交换，
$$
R_\tau=[D_\tau,H_i]
$$
是 $E_i,E_{i+1}$ 的线性组合，故
$$
[D_\tau,R_\tau]=0.
$$
由此
$$
D_\tau^{r+1}H_i
=H_iD_\tau^{r+1}+(r+1)R_\tau D_\tau^r.
$$
因此
$$
\boxed{
H_i\ker D_\tau^r\subseteq\ker D_\tau^{r+1}.
}
\tag{2.1}
$$

先固定任意有限截断旗长度 $h\ge1$，置
$$
F_r(\tau)=\Pi_r(\tau)-\Pi_{r-1}(\tau)\quad(1\le r\le h),
\qquad
F_{h+1}(\tau)=I-\Pi_h(\tau).
$$
这些是完备正交分解。由 (2.1) 及 $H_i$ 自伴，
$$
F_a H_i F_b=0\qquad (|a-b|>1).
\tag{2.2}
$$
最后的 $F_{h+1}$ 保留整个较高旗补空间；没有把它删成零。

令
$$
T_h(\tau)=\sum_{r=1}^h F_{r+1}(\tau)H_iF_r(\tau),
\qquad
\Omega_h(\tau)=T_h(\tau)-T_h(\tau)^*.
$$
不同 summand 的输入、输出分别正交，故
$$
\|T_h(\tau)\|\le1,\qquad
\Omega_h^*=-\Omega_h,\qquad
\|\Omega_h(\tau)\|\le2.
\tag{2.3}
$$
这一步的常数完全独立于 $h$。

由 (2.2)，跨越 $\Pi_r$ 边界的唯一块就是
$F_{r+1}H_iF_r$ 及其伴随。因此 (1.2) 等价于
$$
\Pi_r'=[\Omega_h,\Pi_r]\qquad(1\le r\le h).
\tag{2.4}
$$

## 3. 整条旗的共同物理酉输运

解有界算子常微分方程
$$
W_h'(\tau)=\Omega_h(\tau)W_h(\tau),\qquad W_h(0)=I.
$$
由 (2.3)，$W_h(\tau)$ 为酉算子。式 (2.4) 与相同初值给
$$
\Pi_r(\tau)=W_h(\tau)\Pi_r(0)W_h(\tau)^*,
$$
从而所有 $F_r$ 同时满足
$$
F_r(\tau)=W_h(\tau)F_r(0)W_h(\tau)^*.
\tag{3.1}
$$
而
$$
\boxed{
\|W_h(\tau)-I\|\le2|\tau|.
}
\tag{3.2}
$$
这里只积分一个范数至多 $2$ 的反自伴生成元，不需要指数型 Gronwall 费用。

所有 $\Pi_r(\tau)$ 和 $H_i$ 都保持远孔数，因此 $\Omega_h$、$W_h$ 也保持远孔数。相同证明可逐固定孔层使用，也可直接在全部孔层直和上使用。

平衡时 $D_0$ 与该物理交换 $U_i$ 对易。故全部 $F_r(0)$ 都约化
$$
P_i^-=(I-U_i)/2.
\tag{3.3}
$$
注意原权的 $F_r(\theta_i)$ 一般不与 $P_i^-$ 对易；下面正是支付这一差额。

## 4. 任意实际向量的整旗交换估计

暂记 $P=P_i^-$、$W=W_h(\theta_i)$、$\delta=\|W-I\|$，并令 $v$ 为任意物理向量。由 (3.1)、(3.3)，
$$
PF_r(\theta_i)v
=WF_r(0)PW^*v+[P,W]F_r(0)W^*v.
\tag{4.1}
$$
第一列族的平方和为 $\|PW^*v\|^2$。第二列族的平方和至多
$\|[P,W]\|^2\|v\|^2$。

对正交投影 $P$ 与酉算子 $W$，
$$
\|[P,W]\|
=\max\{\|PW(I-P)\|,\|(I-P)WP\|\}
\le\|W-I\|=\delta.
$$
因此由两个列族的 Hilbert 直和三角不等式，
$$
\begin{aligned}
\left(\sum_{r=1}^{h+1}\|PF_r(\theta_i)v\|^2\right)^{1/2}
&\le\|PW^*v\|+\delta\|v\|\\
&\le\|Pv\|+2\delta\|v\|\\
&\le\|Pv\|+4\theta_i\|v\|.
\end{aligned}
\tag{4.2}
$$
这是保同一实际 $v$ 的估计，不重新选择各条带的代表。

删去最后的非负补空间项后，令 $h\to\infty$，单调收敛给
$$
\boxed{
\left(\sum_{r\ge1}\|P_i^-F_rv\|^2\right)^{1/2}
\le\|P_i^-v\|+4\theta_i\|v\|.
}
\tag{4.3}
$$
对有限孔支撑，和本来就是有限的。对一般向量，(4.3) 证明相应列属于直和空间，不预设无穷列平方可和。

## 5. 对同一实际固定测试端应用

前稿的单对 protected-projection 比较已在原 $V_Q,K_Q$ 的完整物理空间证明
$$
\|P_i^-u_f\|
\le2\sqrt{\cosh(2\theta_i)-1}\,\|f\|
=2\sqrt2\,\sinh\theta_i\,\|f\|.
\tag{5.1}
$$
同时 $K_Q\subset V_Q$，故 $P_{V_Q}-P_{K_Q}$ 本身为正交投影，
$$
\|u_f\|\le\|f\|.
$$
并且
$$
\theta_i\le\frac1{i+1},\qquad
\sinh\theta_i=\frac{2(i+1)+1}{2(i+1)(i+2)}
\le\frac1{i+1}.
$$
将这些代入 (4.3)，得到
$$
\left(\sum_{r\ge1}\|P_i^-F_ru_f\|^2\right)^{1/2}
\le\frac{2\sqrt2+4}{i+1}\|f\|
\le\frac7{i+1}\|f\|.
\tag{5.2}
$$
故
$$
\sum_{i\ge x}\sum_{r\ge1}\|P_i^-F_ru_f\|^2
\le49\sum_{i\ge x}\frac1{(i+1)^2}\|f\|^2
\le\frac{49}{x}\|f\|^2.
\tag{5.3}
$$

令 $P_I$ 为任意输出远孔层集合的正交投影。它与 $P_i^-$、$F_r$ 对易；在 (4.3) 取 $v=P_Iu_f$，用
$$
\|P_i^-P_Iu_f\|\le\|P_i^-u_f\|,\qquad
\|P_Iu_f\|\le\|f\|
$$
即得 (0.1)。因此全部输出孔与全部真实条带已经共同求和，不需再乘孔层数、旗长度或 cut 数。

前稿还允许真实 joined 物理闭和及其嵌套投影差；只要该向量已获得同一单对界 (5.1) 与范数收缩，上述后处理完全相同。本文不把这一前提免费移到任意源坐标中的补空间投影。

## 6. 和实际非正交返回的准确区别

在固定层 $n$，本稿的 $F_r$ 给真正交分解
$$
\mathcal H_n=\bigoplus_{r=1}^{n+1}F_r\mathcal H_n.
$$
另一方面，同顶部双线性恒等式中的
$$
\mathcal P_{n,j}
=D_n^\dagger D_{n-1}^\dagger\cdots D_{n-j+1}^\dagger D^j
$$
是非正交幂等算子。它在这条正交旗中的回返块不由 (5.3) 自动控制。

本文的新支付是：对同一个实际固定测试端，先作完整真实正交 primitive/jet 分解，仍保独立于 $Q,h$ 的相邻交换行小量。未支付的是非正交重建/顺次 MP 对这些条带的混合。在继续估计
$$
\sum_n\langle u_{w,n},\mathscr A_nu_{f,n}\rangle
$$
时，必须保这个混合、两端 partial 和同一个 $w,f$；不得把条带分解后的低交换能量直接说成 $\|\mathscr A_nu_{f,n}\|$ 小。
