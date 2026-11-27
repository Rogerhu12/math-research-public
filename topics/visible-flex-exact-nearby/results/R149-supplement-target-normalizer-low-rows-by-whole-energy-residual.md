# R149 BR：原 target normalizer 的有限行与完整能量残差

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**已证明。** 原 target coordinate 仍是
[WBP](R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md)
的 $\mathcal B=Id+\mathcal T_wI$。本条给真正
$E_{96}^{a*}\mathcal B^{-1}$ 的首次可计算行公式，并支付其全部
finite/infinite residual。它补的是未计算的归一目标行，不把 SC 的
physical/incoming96 配对当成 $\mathcal B^{-1}$ 完整列。

## BR1. 原空间、adjoint 与两种 Hilbert 单位

圆周长 $\pi/2$，归一测度，频率 $4n$。保持真正
$a=2\mathcal H(0)$、$b=a+\Omega$ 和
$R_aw=-w$。在完整 nonmean 圆周上定义

$$
 G=|\partial_\phi|^{-1},\quad
 \mathscr H=\dot H^{-1/2}_0,\quad
 \|f\|_{\mathscr H}^2=\sum_{n\ne0}\frac{|f_n|^2}{4|n|},
 \qquad I=\partial_\phi^{-1}P.
 \tag{BR.1}
$$

$\mathcal T_w=\Pi_+M_w\Pi_++\Pi_-M_w\Pi_-$ 是原 same-sign
算子，不是 $PM_wP$。普通 $L^2$ adjoint 用 $*$，$\mathscr H$
adjoint 用 $\dagger$。WBP.6--9 给同一个 onto inverse，且

$$
 \mathcal B^*=Id-I\mathcal T_w,\qquad
 \mathcal B^\dagger=Id-\mathcal T_wI=G^{-1}\mathcal B^*G,
 \quad\|\mathcal B^{-1}\|_{\mathscr H},
       \|(\mathcal B^\dagger)^{-1}\|_{\mathscr H}\le1.
 \tag{BR.2}
$$

这是原正 primitive pairing 的 skew correction coercivity，不是普通
$L^2$ 中未经证明的 skew-adjointness。$\mathcal B$ 及其真正 inverse
保持 $Y_a^0=\operatorname{Fix}(R_a)\cap L^2_0$；下面的 trial 不必精确
具有未知真实 $a$ 的 parity，因为其全部差由完整 residual 支付。

令 $v_j^a=\sqrt2\cos(4j\phi-2ja)$。真正第 $j$ 行的代表函数为

$$
 r_j=(\mathcal B^*)^{-1}v_j^a
     =G(\mathcal B^\dagger)^{-1}G^{-1}v_j^a.
 \tag{BR.3}
$$

由原 inverse 的同分布意义与 (BR.2)，此恒等式先在光滑数据成立，
再由两窗口一致性得到整个指定行。两个 elementary embeddings 为
$\|L^2_0\hookrightarrow\mathscr H\|\le1/2$ 和
$\|G:\mathscr H\to L^2_0\|\le1/2$。因此对任意 $N\ge1$，

$$
 \boxed{\ \|E_N^{a*}\mathcal B^{-1}:L^2_0\to\ell^2_N\|
       \le\sqrt N\ },\qquad \|r_j\|_2\le\sqrt j.
 \tag{BR.4}
$$

证明：$\|E_N^{a*}:\mathscr H\to\ell^2_N\|=\sqrt{4N}$，依次乘
真正 $\mathscr H$ inverse 与上述输入 embedding。无需旧大的
$K_{B,0}$，也没有逐行再累加一个 $\sqrt N$。

## BR2. 任意完整 trial 的联合行误差

令 $\widehat y_j$ 为实 mean-zero finite polynomial，定义

$$
 h_j=G^{-1}v_j^a=4jv_j^a,\quad
 d_j=\mathcal B^\dagger\widehat y_j-h_j,\quad
 \widehat r_j=G\widehat y_j.
 \tag{BR.5}
$$

以 $D:\ell^2_{96}\to\mathscr H$ 表示全部96个 $d_j$ 的联合 column
operator。由 (BR.2--3) 和 $G$ 的上述 norm，

$$
 \boxed{\ \|E_{96}^{a*}\mathcal B^{-1}-\widehat R\|_{L^2_0\to\ell^2_{96}}
       \le\tfrac12\|D\|_{\ell^2_{96}\to\mathscr H}\ },
 \qquad(\widehat Rf)_j=\langle f,\widehat r_j\rangle.
 \tag{BR.6}
$$

这是先作整个残差算子，再取 adjoint 的等范数；不把96个 scalar
row estimates 假装正交，不另付 $\sqrt{96}$。

## BR3. 同号完整有限卷积与 true w 的无限差

使用 [BW](R149-supplement-first-signed-target-w-carrier-from-complete-alpha.md)
的整个 signed $\widehat w$，degree $K=2048$，以及两个完整误差
$e_{w,\infty},e_{w,2}$。固定每个 $\widehat y_j$ degree $M=192$。
其完整 finite residual 是

$$
 \widehat d_j=\widehat y_j-\mathcal T_{\widehat w}I\widehat y_j-h_j.
 \tag{BR.7}
$$

对 $n>0$，准确系数为

$$
 (\widehat d_j)_n=(\widehat y_j)_n
 -\sum_{\ell=1}^{192}\widehat w_{n-\ell}
             \frac{(\widehat y_j)_\ell}{4i\ell}
 -{4j\over\sqrt2}e^{-2ija}{\bf1}_{n=j}.
 \tag{BR.8}
$$

这里 $\widehat w_0=0$，$\widehat w_{-k}=\overline{\widehat w_k}$，
而输入和输出都保同一正 sign。负 block 是完整 conjugate，不能把
负输入加入正输出。非循环 Laurent 乘积的所有 $1\le n\le2240$
输出均保留，特别是193--2240；其后才是有限 trial 的精确零。
真实 $w-\widehat w$ 的无限部分从未设零。

使用整个原 $a$ ball 形成 forcing coefficient 的有向球，故下式
同时包住真实 phase 及所有 finite arithmetic：

$$
 F_H=\operatorname{up}\sqrt{
       2\sum_{j=1}^{96}\sum_{n=1}^{2240}
          {\sup| (\widehat d_j)_n|^2\over4n}}.
 \tag{BR.9}
$$

它是完整 residual column operator 的 Hilbert--Schmidt bound；
没有把 Galerkin192 residual 当成整个残差。

令 $Y$ 是全部 trial columns，置

$$
 Z_I=\left(2\sum_{j=1}^{96}\sum_{n=1}^{192}
            {|(\widehat y_j)_n|^2\over(4n)^2}\right)^{1/2},\qquad
 B_I=\sum_{n=1}^{192}\left(\sum_{j=1}^{96}
            {|(\widehat y_j)_n|^2\over(4n)^2}\right)^{1/2}.
 \tag{BR.10}
$$

对 $\delta w=w-\widehat w$，两同号 block 的正交性和逐点
vector Cauchy--Schwarz 给两个完整候选

$$
 \|\mathcal T_{\delta w}IY\|_{\ell^2_{96}\to L^2_0}
 \le e_{w,\infty}Z_I,
 \qquad
 \|\mathcal T_{\delta w}IY\|_{\ell^2_{96}\to L^2_0}
 \le\sqrt2\,e_{w,2}B_I.
 \tag{BR.11}
$$

第一式用 $\|\mathcal T_{\delta w}\|\le\|\delta w\|_\infty$ 及
完整 $IY$ Hilbert--Schmidt norm；第二式对正、负两个输入多项式各
用 $L^\infty$ vector bound，再用输出 sign 正交合成。这个
$\sqrt2$ 来自两个 sign，不是从96行误差累加产生。

两个 whole candidates 都保存读回后，取其整上界较小者 $P_w$。
利用 $L^2_0\hookrightarrow\mathscr H$ 的 norm $1/2$，最终

$$
 \|D\|\le F_H+\tfrac12 P_w,
 \qquad
 \boxed{\ e_R=\tfrac12F_H+\tfrac14P_w\ }.
 \tag{BR.12}
$$

因此所有 finite phase、全部2240输出、未知 $w$ 无限误差均已付清。
无需仅因某个 finite matrix 可逆就假定真正全空间 inverse；真正
inverse 的 onto/coercivity 已来自 WBP，trial 只需通过完整 residual。

## BR4. 如何消费真正完整物理列

设 $X$ 是原完整 physical primitive target $Y_a^0$ 中的一组列，
$\widehat X$ 是其完整 finite trial；在明确输入权重 $D_s$ 下已有

$$
 \|\widehat X D_s^{-1}\|\le x_0,\qquad
 \|(X-\widehat X)D_s^{-1}\|\le\delta_X.
$$

应用 (BR.4)、(BR.6) 得

$$
 \|[E_{96}^{a*}\mathcal B^{-1}X-\widehat R\widehat X]D_s^{-1}\|
 \le e_Rx_0+\sqrt{96}\,\delta_X.
 \tag{BR.13}
$$

式中 $\sqrt{96}$ 是 (BR.4) 已证整个 true receiver norm，绝不是
对 $e_R$ 再加一次行数损失。完整列 $X$ 须含原 true chart、left
receiver、physical mean rank 与所有 ordinary/jump/PDE 误差资格；
若只知道96个已配对标量，则不能形成或认证此列，也不能使用本式
声称原 $\mathcal B^{-1}$ 的完整目标已被观测。

纯模块
[fourfold_codazzi_target_normalizer_finite_rows.py](../scripts/fourfold_codazzi_target_normalizer_finite_rows.py)
给 (BR.8--13) 的完整有向表达式。BW 尚未实际成功时不执行其行目标。
本条不删除两 physical means、真正 $\nu$/phase、完整 high/cross 或
full Schur，也不预报任何 finite gate 或最终嵌入族已经完成。
